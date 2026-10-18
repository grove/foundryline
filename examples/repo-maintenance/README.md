# Real manual Maintain example

**ACTUAL EXECUTION, not an authored report fixture.** On 2026-10-18, a Codex
operator ran RepoTend's deterministic auditor on a separate public Foundryline
checkout. The [manual recipe](../../patterns/maintain.md) is the portable procedure.
The summaries, triage and [issue proposal](issue-proposal.md) are authored analysis;
the raw process outputs below are unedited. **No maintenance issue was published.**

## Identities and scope

| Input | Observed identity |
| --- | --- |
| Tool | [grove/repotend at `2d69cce901475380775f674b9cc5755f1f89f82e`](https://github.com/grove/repotend/tree/2d69cce901475380775f674b9cc5755f1f89f82e), package/report version 0.1.0 |
| Target | [grove/foundryline at `5dc1dd15836584a1112caec224d479df8deffc9f`](https://github.com/grove/foundryline/tree/5dc1dd15836584a1112caec224d479df8deffc9f), fresh detached checkout |
| Tool environment | macOS / Darwin 25.6.0 arm64, Node v26.12.0, npm 11.20.0; no audit model/API |
| Dependencies | `npm ci --ignore-scripts --no-audit --no-fund`; lockfile SHA-256 `f17806903690e3f2058655ff974ed45a27ee894cceccd8f54ac50e8c8108d0b6` |
| Configuration | No `.repotend.yml`; default `small-oss`, all 13 rules advisory |
| Scope | Local convention files and `.github/workflows/reference-checks.yml`; no target code execution, installs, remediation, GitHub writes, or settings inspection |

Full environment, pinned identities and before/after file hashes/modes are in
[environment.json](receipts/environment.json). The target's 48 file entries were
identical before/after both auditor invocations and the negative control. This
compares working-tree files outside `.git`, not a syscall trace or proof of
arbitrary-host isolation. The target is the historical pin, **not this PR tree**.

## Commands and genuine receipts

Setup used fresh repositories under `/private/tmp/foundryline-maintain`:

~~~sh
git -C /private/tmp/foundryline-maintain/tool init
git -C /private/tmp/foundryline-maintain/tool remote add origin https://github.com/grove/repotend.git
git -C /private/tmp/foundryline-maintain/tool fetch --depth=1 origin 2d69cce901475380775f674b9cc5755f1f89f82e
git -C /private/tmp/foundryline-maintain/tool checkout --detach FETCH_HEAD
git -C /private/tmp/foundryline-maintain/target init
git -C /private/tmp/foundryline-maintain/target remote add origin https://github.com/grove/foundryline.git
git -C /private/tmp/foundryline-maintain/target fetch --depth=1 origin 5dc1dd15836584a1112caec224d479df8deffc9f
git -C /private/tmp/foundryline-maintain/target checkout --detach FETCH_HEAD
~~~

The directories were created before `git init`. Fetch/setup used host network
access; the audit commands ran locally. Dependencies were installed once to
prepare the tool, then `npm ci` was repeated with captured stdout/stderr using
the populated cache. The retained setup is that second, genuine installation.
It wrote tool dependencies and a separate npm cache, not target files.

Every command record below retains argv, cwd, UTC start, elapsed seconds, exit,
stdout/stderr lengths and SHA-256. A temporary Python `subprocess.run` capture
wrote the bytes outside the target; it is not a Foundryline runtime or new engine.

| Execution | Command record | Raw stdout | Raw stderr | Exit / elapsed |
| --- | --- | --- | --- | --- |
| Locked dependency setup | [setup command](receipts/setup/command.json) | [installation output](receipts/setup/stdout.txt) | [setup stderr](receipts/setup/stderr.txt) | 0 / 0.523 s |
| JSON audit | [JSON command](receipts/audit-json/command.json) | [report.json](receipts/audit-json/report.json) | [JSON stderr](receipts/audit-json/stderr.txt) | 0 / 0.200 s |
| Markdown audit | [Markdown command](receipts/audit-markdown/command.json) | [report.md](receipts/audit-markdown/report.md) | [Markdown stderr](receipts/audit-markdown/stderr.txt) | 0 / 0.197 s |
| Missing-target control | [negative command](receipts/missing-target/command.json) | [empty stdout](receipts/missing-target/stdout.txt) | [actual ENOENT error](receipts/missing-target/stderr.txt) | 2 / 0.190 s |

The exact audit commands, from the separate tool checkout, were:

~~~sh
node skills/repotend/scripts/audit.mjs --root /private/tmp/foundryline-maintain/target --format json
node skills/repotend/scripts/audit.mjs --root /private/tmp/foundryline-maintain/target --format markdown
node skills/repotend/scripts/audit.mjs --root /private/tmp/foundryline-maintain/unavailable-target --format json
~~~

## Results and triage

**6 PASS, 7 WARN, 0 FAIL, 0 UNKNOWN, 0 NOT_APPLICABLE, 0 SUPPRESSED.** Both real
audit processes exited 0 with empty stderr and `errors: []` in JSON. This is
advisory completion, not comprehensive security approval. We did not manufacture
findings to demonstrate all statuses. `verified` identifies a checked property,
not a mandatory policy; some workflow PASSes are explicitly `heuristic`.

| Rule(s) | Actual status / confidence | Source-grounded disposition |
| --- | --- | --- |
| `repo.license-present` | PASS / verified | Root LICENSE present; legal compatibility not assessed |
| `repo.contributing` | WARN / verified | **NEEDS_DECISION:** propose a small contribution guide if maintainers find it useful; see unpublished draft |
| `repo.code-of-conduct`, `repo.security-policy` | WARN / verified | **DEFERRED:** no local recognized files; organization defaults/private reporting settings and maintainer policy unknown; no claim of vulnerability |
| `repo.pr-template`, `repo.issue-templates` | WARN / verified | **DEFERRED:** optional templates; no demonstrated missing information or policy violation |
| `dx.editorconfig` | WARN / verified | **DEFERRED:** no formatting problems demonstrated; a file-presence warning alone does not justify another config |
| `ci.workflow-validity` | PASS / verified | Basic YAML/structure only; not full actionlint/Actions validation |
| `security.workflow-permissions` | PASS / heuristic | Explicit `contents: read`; no least-privilege certification |
| `ci.concurrency` | WARN / heuristic | **DEFERRED:** small reference-check job has no cancellation group; no observed waste measurement, so do not change CI from this hint alone |
| `ci.duplicate-triggers`, `ci.path-filter-safety` | PASS / heuristic | Main-only push plus PR checks, no event path filters; neither cost nor required-check behavior measured |
| `security.action-pinning` | PASS / verified | Checkout uses a full SHA; action safety itself is unassessed |

Triage read the pinned [README contribution invitation](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/README.md#want-to-help),
[design principles and effect boundaries](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/DESIGN.md#principles),
[actual reference workflow](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/.github/workflows/reference-checks.yml),
and existing reference tests. RepoTend's pinned rule catalog/engine was consulted
to confirm recognized paths and confidence limits. There is no local suppression
or CONTRIBUTING file. The README already gives contribution ideas, which reduces
urgency: missing a convention filename is not proof contributors are blocked.

Open **and closed** GitHub issue and PR bodies/titles were read on 2026-10-18:
[issue inventory](receipts/issues.json), [PR inventory](receipts/pull-requests.json),
and [lookup commands/time/identities](receipts/lookup.json). Four issues and nine
PRs were returned, below each limit of 100; no matching contribution-guide task
was found. Issue #10 covers this recipe, not implementing every reported warning.
This is a point-in-time title/body comparison, not a comments/discussions or
organization-wide search. Recheck before any later publication.

## Negative control and adoption

**UNAVAILABLE / INCOMPLETE:** the deliberate nonexistent target returned exit 2,
an ENOENT stderr, and zero stdout bytes. It produced **no JSON report** and no
clean PASS or maintenance proposal. No fallback directory was created. The
successful audits above remain distinct from this failed execution.

The [separate-agent adoption record](adoption.md) retains a fresh setup attempt,
observed effort, deviations and limits. Shared hardware/provider/operator is
disclosed; it is not independent administration or cross-platform qualification.

Machine-measured durations above cover processes only. Total primary authoring
and triage time was not separately instrumented; model billing is unavailable.
RepoTend itself required no model. Structural checks verify links, receipt
identities/consistency, report rows and failed-run handling; they do not recreate
history or authenticate arbitrary operator assertions. Maintainer review is
pending; no new release or broader qualification is asserted.

**Executed reference validation:** `python3 -m unittest discover -s checks -v`
passed all 16 tests on 2026-10-18. These are Foundryline's artifact checks, run in
the implementation workspace, separately from the read-only target audit.
