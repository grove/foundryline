# Repeat this host-specific pilot

These are manual setup instructions, not a Foundryline controller. Setup and
receipt storage are outside the read-only Gapline stage. Use a disposable
operator-owned directory, public source only, an already authenticated Codex
host, and an explicit model budget. Do not copy authentication files into it.
The observed host was macOS / Codex CLI `0.163.0`; other versions/platforms need
their own capability review. See the [recorded limits](../README.md).

## Prepare pinned public inputs

Create a temporary bare or ordinary Git repository and fetch these exact public
objects into it using `git fetch --depth=1 <repository-url> <full-sha>`:

| Repository | Exact revision |
| --- | --- |
| `https://github.com/grove/repotend.git` | `bfe410e4d61ddb472e335ce35877997a2f32d91f` |
| `https://github.com/grove/gapline.git` | `bd6a1dea3677482e2d4a305a5bf8084cb3c95e69` |
| `https://github.com/grove/intentline.git` | `25e926f57e69395193fc0ac258f9e6dd2332cb18` |

Do not execute, install dependencies from, or check out the target. In a trusted
operator Python process, prepare the mapping using the checked-in manifest:

```python
import hashlib
import json
import subprocess
from pathlib import Path

objects = Path('/absolute/path/to/temporary-git-repository')
example = Path('/absolute/path/to/foundryline/examples/repotend-pilot')
run_root = Path('/absolute/path/to/fresh-pilot-directory')
manifest = json.loads((example / 'receipts/source-manifest.json').read_text())
skills = {
    'skill:gapline-audit': ('bd6a1dea3677482e2d4a305a5bf8084cb3c95e69', 'gapline-audit/SKILL.md'),
    'skill:intentline-issue': ('25e926f57e69395193fc0ac258f9e6dd2332cb18', 'intentline-issue/SKILL.md'),
}
bundle = {}
for key, identity in manifest['sources'].items():
    revision, path = skills.get(key, (manifest['revision'], key))
    raw = subprocess.check_output(['git', '-C', str(objects), 'show', f'{revision}:{path}'])
    assert hashlib.sha256(raw).hexdigest() == identity['sha256'], key
    text = raw.decode('utf-8')
    assert len(text.splitlines()) == identity['lines'], key
    bundle[key] = text
run_root.mkdir(exist_ok=False)
(run_root / 'bundle.json').write_text(json.dumps(bundle))
installed = run_root / '.agents/skills/gapline-audit'
installed.mkdir(parents=True)
(installed / 'SKILL.md').write_text(bundle['skill:gapline-audit'])
```

The assertions verify bytes, not source authority or runtime behavior. The
reader serves that mapping from memory; it does not expose `objects` or other
files to model-selected paths. Keep the tool implementation outside target
sources, use a trusted Python runtime, and inspect any host-managed configuration
that CLI flags cannot override. Native agent and provider tools may remain
visible despite disabled features; disclose them.

## Invoke and retain actual output

Run the following from the fresh directory, replacing the two absolute paths.
The retained [primary command](../receipts/pilot/command.json) records the actual
arguments including runtime paths. The prompt is the exact
[primary prompt](../receipts/pilot/prompt.txt), not the result of an earlier run.

```sh
codex --no-daemon exec --ignore-user-config --ignore-rules --ephemeral \
  --skip-git-repo-check --sandbox read-only \
  --config 'approval_policy="never"' --config 'web_search="disabled"' \
  --disable shell_tool --disable apps --disable skill_mcp_dependency_install \
  --disable image_generation --disable browser_use --disable computer_use \
  --disable view_image --disable multi_agent \
  --config 'mcp_servers.pinned_source={command="python3",args=["/absolute/path/to/read_snapshot.py","/absolute/path/to/fresh-pilot-directory/bundle.json"]}' \
  --json --output-last-message report.md - < prompt.txt > events.jsonl 2> stderr.txt
```

The CLI's receipt files are host output capture, not agent-authorized repository
writes. Stop the process at 600 seconds; record actual UTC start/end or elapsed
time, exit code, reported `turn.completed` usage, and missing model/cost data.
Inspect every actual tool call and report; tool annotations alone are not
permission enforcement. If the CLI cannot start or a necessary source is missing,
retain the failure, disclose the limit, and do not fabricate a successful audit.
Provider connectivity is needed outside shell execution; do not disable or
bypass the selected agent sandbox to solve a launch problem.

For independent reproduction, prepare a new directory, installed skill and
mapping, use the [reproduction prompt](../receipts/reproduction/prompt.txt), and
configure `mcp_servers.independent_source` instead. Start a separate process
without importing a primary conversation or report. The original run shared
operator, provider and runtime; arrange a separately administered host or another
maintainer if stronger independence is required.

For the safe negative control, prepare another fresh directory but filter its
mapping to keys starting with `skill:` **before launching the reader**. Use the
[negative prompt](../receipts/negative/prompt.txt). Verify that the actual
`docs/REMEDIATION.md` read fails and that the agent stops without invented target
evidence or fallback access. An instruction saying a file is unavailable is not
the control; withholding it from the reader is.

After Gapline exits, review original promises and exceptions, perform separate
read-only duplicate triage, use Intentline's drafting guidance only for a
sufficiently supported lead, and retain public results as a separate record.
Keep private inputs/output private. No target execution, issue publication,
saved agreement, repair, merge or deployment is authorized by this procedure.
