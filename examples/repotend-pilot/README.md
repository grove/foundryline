# RepoTend Discover pilot — actual run record

**Actual runs, not authored fixtures. Qualification: PENDING MAINTAINER REVIEW.**
This record addresses [Foundryline #4](https://github.com/grove/foundryline/issues/4)
using the [Discover runbook](../../patterns/discover.md) and
[run-record template](../manual-discover/run-record-template.md).
It does not certify v0.1 or universal host isolation.

## Run identity and setup

- Operator: the coordinating coding agent acting on the implementation request;
  no second human maintainer participated.
- Date: 2026-10-18 Europe/Oslo (2026-10-17 UTC in the receipts).
- Target: public `grove/repotend`, exactly
  `bfe410e4d61ddb472e335ce35877997a2f32d91f`.
- Snapshot: source text extracted from the pinned Git objects with `git show`,
  not a checkout of moving `main`. There is no target working tree in the audit
  directories. The operator verified the objects; agents relied on supplied
  provenance. No claim about the developer's existing RepoTend working tree.
- Question: does remediation preserve documented preview/read-only behavior,
  explicit approval, stale-plan handling, and existing-file protection?
- Initial scope: `docs/REMEDIATION.md`,
  `skills/repotend/scripts/remediation.ts`, `test/remediation.test.mjs`.
  Seven necessary caller/configuration/documentation files were also allowed;
  [source-manifest.json](receipts/source-manifest.json) lists every source,
  SHA-256 and line count.
- Host: Codex CLI `0.163.0` on macOS. Model: CLI default, exact identity not
  exposed in retained events. Account/provider and machine were shared across
  the runs; this is not cross-provider or cross-platform replication.
- Gapline: public `grove/gapline` at
  `bd6a1dea3677482e2d4a305a5bf8084cb3c95e69`, canonical
  `gapline-audit/SKILL.md`, SHA-256
  `5ecfeab4894c5d4fbf5b99eb3930a7535e9c4a9e86b557a971c782bb0f02e567`.
  The skill was installed in each fresh directory's `.agents/skills/gapline-audit`.
  Invocation was explicit `$gapline-audit` with canonical source-reader access;
  automatic skill discovery from an ordinary natural-language request was not tested.
- Budget per run: at most three leads/findings, 18 source reads, 600 seconds.
  The operator's launcher imposed the timeout; the lead/read ceilings were
  instructions and were observed, not enforced by the reader.

## Actual activity and permission boundary

The [reader](host/read_snapshot.py) loads an operator-prepared JSON mapping
once, then exposes only `read_source(key)`. Requests select exact mapping keys;
no request opens a filesystem path, executes a command, writes, or uses network.
All bundle text was verified against **public upstream Git objects**, including
both skills. Source setup, tracker inspection and receipt storage occurred
outside the read-only Gapline stage.

The retained commands select `--sandbox read-only`, `approval_policy="never"`,
`--ignore-user-config`, `--ignore-rules`, `--ephemeral`, `--no-daemon`, disabled
shell/apps/browser/computer/image tools, disabled web search, and exactly one
configured MCP source server. No target project executable or dependency was
installed in the audit directories. Model-provider communication was allowed;
no tracker server or credential was supplied to the agents.

Each positive run first actually read `skill:gapline-audit`, then read all ten
permitted target files and applied Scout → Probe → Report. Their reports cite
source observations, examine counterevidence and withdraw other leads. This is
activation-and-use evidence, beyond skill installation or reading alone.

The retained JSON events show **11 source calls per positive run**, and no
command-execution, file-change or tracker events. The agents reported no project
code/tests/builds executed, writes, publication, or delegation. The source adapter
cannot perform those effects; shell execution was disabled and filesystem writes
were configured read-only. No RepoTend tests or builds were run by the operator.
Foundryline's own structural/adapter checks were run separately.

**Visibility limits:** the agents also saw orchestration, goal/resource, input,
clock and collaboration interfaces. Their reports describe `functions.exec`
discovery/orchestration calls; the JSON event stream does not expose those wrapper
calls individually. No OS-level denial trace or complete provider-side activity
trace was retained. Native sandbox configuration and the narrow MCP implementation
are evidence of controls, not an adversarial test of all provider interfaces.
Agents' claims of “no network access” refer to retrieval tools, not the allowed
model-provider traffic. Do not generalize these receipts to complete host isolation.

The first nested-sandbox launch failed before a model turn with an app-server
`Operation not permitted` error; [its receipt](receipts/failed-launch/stderr.txt)
is retained. An escalated launch was then rejected by automatic approval review
because local skill text's sensitivity/provenance and provider destination were
unverified. The operator verified both upstream repositories were public and
compared/fetched the exact Git objects before the approved retry. The three
successful commands still selected their own read-only agent sandbox. The
approval-review rejection had no model/tool activity receipt; it is not an audit
or the deliberate negative control.

## Findings, original sources and handoff

Both runs retained one **SUPPORTED** finding: the Markdown preview suggests an
apply command without the preview's selected root. The CLI defaults to the
current directory, and content-identical plans can share a digest across roots.
No wrong-target write was reproduced. See the unchanged
[primary report](receipts/pilot/report.md) and
[independent report](receipts/reproduction/report.md).

The coordinator re-read the cited pinned originals and verified:

- Source support: `remediation.ts:53–55,181–184` and
  `remediate-cli.ts:5–16` establish the content digest and omitted root.
- Behavioral authority: `skills/repotend/SKILL.md:37–44` requires the same
  reviewed plan **and target root**; `docs/REMEDIATION.md:29–39` documents
  explicit approval and an apply command retaining `--root`.
- Counterevidence: the documented command and JSON-based agent instructions
  already preserve the root. Different proposal sets fail the digest check.
  Existing-file checks remain relevant. Tests at `test/remediation.test.mjs:126–143`
  always pass `--root`; they are assertion evidence, not executed results.
- Exceptions retained: the digest is not proof of consent; organization defaults
  are not verified; two-file application is not transactional and concurrent
  malicious path mutation is outside its design (`docs/REMEDIATION.md:25,39,52`).
  No repository-identity hash or transactional-write requirement is invented.

Duplicate triage ran outside Gapline with authenticated read-only
`gh issue list --repo grove/repotend --state all --limit 200`, requesting bodies,
comments, state and timestamps. [The returned inventory](receipts/repotend-issues.json)
contains zero open issues and one closed issue,
[RepoTend #7](https://github.com/grove/repotend/issues/7), with no comments.
Its body covers real-agent installation/approval validation and requires retaining
existing interfaces; it does not describe the rendered-command root omission.
No obvious duplicate was found in that inventory. PRs, discussions, deleted or
inaccessible items, subsequent changes and current-main fixes were **NOT CHECKED**.
The live issue inventory is later context, not part of the pinned source revision.

The coordinating agent used `intentline-issue` **drafting guidance only**, from
public `grove/intentline` at `25e926f57e69395193fc0ac258f9e6dd2332cb18`.
The installed skill matched the public Git object (hash in the manifest);
`docs/ISSUE_WORKFLOW.md`, `docs/CONTRACT.md`, and `docs/TRUST_AND_AUTHORITY.md`
were read from that revision. Its original-source, provisional-evidence and
confirmation guidance was applied to the [issue proposal](issue-proposal.md).
This was not a second live skill-activation qualification. The operator retained
the resulting proposal here after drafting, outside the audit/review stage.

**Issue proposal: NOT PUBLISHED. RepoTend CREATE/UPDATE: NONE. Saved Intentline
agreement: NOT CREATED.** The separately requested Foundryline PR publishes this
record, not a RepoTend issue or repair. Executable follow-ups remain
**PROPOSED — NOT RUN**.

## Independent reproduction and witnessed negative control

The reproduction used a fresh Codex process/thread, a separate work directory,
its own installed skill and bundle, and its own MCP configuration named
`independent_source` rather than `pinned_source`. It received the same pinned
inputs and runbook but no primary report, findings or conversation. Processes
ran concurrently. It independently identified the same root omission and the
same unavailable transitive context; identical findings were not required.
Both configurations were prepared by the same coordinating agent using the same
recipe and shared runtime/provider. This is fresh-agent reproduction, not an
independently administered host or a second human's review.

For the separately arranged negative run, the mapping contained **only the two
public skills**; every target key was withheld. The actual reader rejected
`docs/REMEDIATION.md`, and the agent stopped with **UNQUALIFIED / UNAVAILABLE**,
zero findings and all target behavior **NOT ASSESSED**. See the
[actual response](receipts/negative/report.md) and
[events](receipts/negative/events.jsonl). It did not invent source citations,
approval, test results or a fallback audit. This observed refusal is distinct
from the initial host-startup failure.

## Measured outcomes

| Run | Start (UTC, 2026-10-17) | Elapsed seconds | Source calls | Input tokens | Cached input | Output tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Pilot | 23:09:59.888 | 48.390 | 11 | 99,099 | 75,008 | 1,751 |
| Reproduction | 23:10:09.571 | 64.791 | 11 | 101,419 | 70,784 | 1,766 |
| Negative | 23:10:09.921 | 41.852 | 2 | 61,717 | 44,288 | 610 |

All three CLI processes exited `0` with empty stderr. Usage is exactly the
CLI's reported aggregate, including repeated context; cached tokens are a subset
of input, not additional tokens. Reasoning-output counters are retained in each
measurement without inferring billing. **Billable cost and exact model identity:
UNAVAILABLE.** Setup, capability preflight, coordinator work, GitHub calls,
review and PR delivery costs/time are not included. The earlier capability
preflight reported 13,824 input / 8,960 cached / 218 output tokens; it was not an
audit, and its complete raw stream was not retained. There is no total task-cost
or total end-to-end time claim.

## Qualification decision and remaining unknowns

| Issue criterion | Evidence retained / limit |
| --- | --- |
| R1 | Version, pinned skills/source, explicit activation and actual method use, paths, budget and commands retained. Exact model unavailable. |
| R2 | Bounded public-source reader, configured read-only/no-shell runs and activity retained. Extra provider interfaces and wrapper visibility remain limited. |
| R3 | One source-supported finding per positive run, counterevidence, proposed falsification and unassessed areas retained. No runtime failure demonstrated. |
| R4 | Applicable pinned docs/skill and explicit exceptions reviewed; all returned open/closed issues triaged with coverage limits. |
| R5 | Source-grounded, unpublished “Confirm before fixing” proposal; no tracker write or saved agreement. |
| R6 | Fresh independently configured process reproduced the procedure; same operator, runtime/provider and setup recipe disclosed. |
| R7 | Actual source-unavailable error and qualified refusal retained. |
| R8 | Public receipts, time/usage and unknowns retained; coordinator reviewed material citations, counterevidence, tool calls and handoff. Maintainer review pending. |

**PENDING MAINTAINER REVIEW; v0.1 is not labeled live-qualified.** In particular,
`engine.ts:4,168` imports `workflows.ts`, which was outside the permitted bundle;
complete preview transitive behavior remains **NOT ASSESSED**. Runtime, actual
RepoTend-agent approval interactions, filesystem/platform races, and other tests
were not assessed. The raw reports are preserved, including these limitations;
source agreement between two agents is not runtime proof.

The next owner decision is whether this host-specific, fresh-agent reproduction
and its disclosed visibility limits meet #4's intended independence and boundary
standard. If stronger evidence is required, retain this result and arrange the
missing host/reviewer capability rather than upgrading its claims.

## Repeat the procedure

[host/README.md](host/README.md) describes preparing the same public Git-object
bundle, starting separately configured processes, and arranging the control.
The receipts preserve exact prompts, commands, output events and measurements:
[pilot](receipts/pilot/command.json),
[reproduction](receipts/reproduction/command.json),
[negative](receipts/negative/command.json).
The ordinary [structural checks](../../checks/test_manual_discover.py) and
[reader/receipt checks](../../checks/test_pilot_reader.py) need no model or network
and do not themselves qualify a live run.
