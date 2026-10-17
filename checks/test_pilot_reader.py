"""Check the pilot's host adapter, without running any target code or model."""
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('reader', Path(__file__).resolve().parents[1] / 'examples/repotend-pilot/host/read_snapshot.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)


class PilotReaderTests(unittest.TestCase):
    def test_only_exact_bundle_keys_can_be_read(self):
        sources = {'docs/policy.md': 'A promise.\nAn exception.\n'}
        def call(name, arguments):
            return reader.respond({'method': 'tools/call', 'params': {'name': name, 'arguments': arguments}}, sources)
        self.assertEqual(call('read_source', {'key': 'docs/policy.md'})['content'][0]['text'],
                         'docs/policy.md\n1: A promise.\n2: An exception.')
        for name, args in [('read_source', {'key': '/etc/passwd'}),
                           ('read_source', {'key': '../docs/policy.md'}),
                           ('read_source', {'key': 'docs/policy.md', 'command': 'echo unsafe'}),
                           ('write_source', {'key': 'docs/policy.md'}),
                           ('read_source', {'key': []})]:
            with self.subTest(name=name, args=args):
                self.assertTrue(call(name, args)['isError'])
        self.assertEqual(sources, {'docs/policy.md': 'A promise.\nAn exception.\n'})

    def test_protocol_advertises_only_read_tool(self):
        init = reader.respond({'method': 'initialize', 'params': {'protocolVersion': '2024-11-05'}}, {})
        self.assertEqual(init['protocolVersion'], '2024-11-05')
        tools = reader.respond({'method': 'tools/list'}, {})['tools']
        self.assertEqual([tool['name'] for tool in tools], ['read_source'])
        self.assertTrue(tools[0]['annotations']['readOnlyHint'])


class PilotReceiptTests(unittest.TestCase):
    def test_retained_calls_and_reports_match_recorded_inputs(self):
        receipts = Path(__file__).resolve().parents[1] / 'examples/repotend-pilot/receipts'
        manifest = json.loads((receipts / 'source-manifest.json').read_text())['sources']
        for run in ['pilot', 'reproduction', 'negative']:
            with self.subTest(run=run):
                root = receipts / run
                events = [json.loads(line) for line in (root / 'events.jsonl').read_text().splitlines()]
                completed = [e['item'] for e in events if e['type'] == 'item.completed']
                self.assertTrue(all(item['type'] in ['agent_message', 'mcp_tool_call'] for item in completed))
                calls = [item for item in completed if item['type'] == 'mcp_tool_call']
                self.assertEqual(calls[0]['arguments'], {'key': 'skill:gapline-audit'})
                self.assertLessEqual(len(calls), 18)
                for call in calls:
                    self.assertEqual(call['tool'], 'read_source')
                    key = call['arguments']['key']
                    text = call['result']['content'][0]['text']
                    if run == 'negative' and key == 'docs/REMEDIATION.md':
                        self.assertEqual(call['status'], 'failed')
                        self.assertIn('UNAVAILABLE', text)
                        continue
                    self.assertEqual(call['status'], 'completed')
                    lines = text.splitlines()
                    self.assertEqual(lines[0], key)
                    original = []
                    for number, line in enumerate(lines[1:], 1):
                        prefix = f'{number}: '
                        self.assertTrue(line.startswith(prefix))
                        original.append(line[len(prefix):])
                    self.assertEqual(len(original), manifest[key]['lines'])
                    raw = ('\n'.join(original) + '\n').encode()
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), manifest[key]['sha256'])
                if run == 'negative':
                    self.assertEqual([c['arguments']['key'] for c in calls],
                                     ['skill:gapline-audit', 'docs/REMEDIATION.md'])
                measurement = json.loads((root / 'measurement.json').read_text())
                self.assertEqual(events[-1]['type'], 'turn.completed')
                self.assertEqual(measurement['usage'], events[-1]['usage'])
                self.assertEqual(measurement['source_reads'], len(calls))
                self.assertEqual(measurement['exit_code'], 0)
                self.assertEqual((root / 'report.md').read_text().strip(), completed[-1]['text'].strip())
