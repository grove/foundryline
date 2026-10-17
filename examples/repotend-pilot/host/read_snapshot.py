"""One-run stdio MCP reader for an operator-prepared, public source bundle.

The model can select bundle keys, never filesystem paths or commands.
Run outside the Gapline stage; this adapter has no project imports.
"""
import json
import sys
from pathlib import Path


def respond(request, sources):
    method = request.get('method')
    if method == 'initialize':
        return {'protocolVersion': request['params']['protocolVersion'],
                'capabilities': {'tools': {}},
                'serverInfo': {'name': 'pinned-source-reader', 'version': '1'}}
    if method == 'tools/list':
        return {'tools': [{'name': 'read_source',
                          'description': 'Read one exact allowed source with original line numbers. Unknown keys are unavailable; no writes, execution, or network.',
                          'inputSchema': {'type': 'object', 'properties': {'key': {'type': 'string'}},
                                          'required': ['key'], 'additionalProperties': False},
                          'annotations': {'readOnlyHint': True, 'openWorldHint': False}}]}
    if method == 'tools/call':
        params = request.get('params', {})
        args = params.get('arguments', {})
        if params.get('name') != 'read_source' or set(args) != {'key'} or not isinstance(args['key'], str) or args['key'] not in sources:
            return {'isError': True, 'content': [{'type': 'text', 'text': 'UNAVAILABLE: source not in this run bundle; no fallback access.'}]}
        key = args['key']
        lines = '\n'.join(f'{n}: {line}' for n, line in enumerate(sources[key].splitlines(), 1))
        return {'content': [{'type': 'text', 'text': f'{key}\n{lines}'}]}
    if method == 'ping':
        return {}
    raise ValueError('Unsupported method')


def main():
    # Load once; subsequent requests cannot change the backing path or source bytes.
    sources = json.loads(Path(sys.argv[1]).read_text())
    if not isinstance(sources, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in sources.items()):
        raise ValueError('Expected a mapping of source keys to text')
    for line in sys.stdin:
        request = json.loads(line)
        if 'id' not in request:
            continue
        try:
            response = {'jsonrpc': '2.0', 'id': request['id'], 'result': respond(request, sources)}
        except (KeyError, TypeError, ValueError):
            response = {'jsonrpc': '2.0', 'id': request['id'], 'error': {'code': -32601, 'message': 'Unsupported request'}}
        print(json.dumps(response), flush=True)


if __name__ == '__main__':
    main()
