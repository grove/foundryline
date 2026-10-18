# Maintain — manual, read-only RepoTend recipe

Check one small repository's maintenance basics, then decide whether any finding
deserves a reviewable issue. This recipe uses [RepoTend](https://github.com/grove/repotend)'s
existing deterministic auditor. **No AI model, GitHub token, or Foundryline service
is required for the audit.** An assistant is optional for interpretation.

**Status: ACCEPTED for the observed narrow manual Maintain scope.** See the
[recorded acceptance and host limits](../docs/maintain-v0.2-qualification-review.md),
[real local example and adoption attempt](../examples/repo-maintenance/README.md),
and [separately witnessed GitHub Actions Run workflow event](https://github.com/grove/foundryline/actions/runs/39112708357).
This does **not** qualify scheduled audits, automatic issue creation, remediation,
general host isolation, or blanket cross-platform operation.
The [Discover recipe](discover.md) provides the related source-grounding workflow.

## First run

| Before the detailed steps | Short path |
| --- | --- |
| Environment | Git, npm, **Node.js >=22.16.0**, POSIX shell. Local evidence is macOS; the separate button run used Ubuntu 24.04 / Node 22.20.0. Upstream supports macOS/Linux and recommends WSL on Windows; other hosts need checks. **No AI, installed agent skill or GitHub token required.** |
| Pinned source | [RepoTend `2d69cce901475380775f674b9cc5755f1f89f82e`](https://github.com/grove/repotend/tree/2d69cce901475380775f674b9cc5755f1f89f82e), with its locked dependencies. |
| Inputs | Readable target/full SHA and dirty-file scope; separate tool and report directories outside the target. |
| First action | In a new work directory, follow [Step 1's pinned setup](#1-prepare-trusted-tools-separately), then select the target and run [Step 3](#3-run-and-retain-actual-outputs) with an explicit `--root`. Authorize setup downloads/tool writes and report writes separately from target reads. |
| Expected artifact | Raw `report.json`, `report.md`, stderr and exit files, plus tool/target identities. Warnings are advisory; a justified issue draft stays **NOT PUBLISHED**. |
| Stop / unavailable | Missing tool, source or report: **UNAVAILABLE / NOT RUN**. Exit 2 or report errors: **UNAVAILABLE / INCOMPLETE**, never a clean audit. |
| Separate approval | Fixes, remediation, issue/PR publication and any later merge or deployment need their own authorization. An assistant for triage and the [GitHub button path](../docs/manual-intake.md) are optional. |

No prompt is an enforcement boundary; configure host permissions for your inputs.
The [recorded adoption attempt](../examples/repo-maintenance/adoption.md) used a
separate agent on the same host. A future uncoached adoption claim needs an actually
new agent/session, disclosed inputs and its own record; this guide adds no such run.

## 1. Prepare trusted tools separately

You need Git, npm, and **Node.js >=22.16.0** (built-in TypeScript stripping).
The recorded run used macOS; upstream supports macOS/Linux and recommends WSL
on Windows. Other hosts need their own checks. You need readable target source
and a place **outside that target** for the tool and reports.

Inspect/trust RepoTend before running it. Setup downloads source/dependencies and
writes a checkout, `node_modules`, and npm cache; it is separate from the read-only
audit. Do not install target dependencies or run target package scripts.

Run these commands in a new, operator-selected work directory (POSIX shell):

~~~sh
mkdir maintain-work
cd maintain-work
git clone https://github.com/grove/repotend.git tool
git -C tool checkout --detach 2d69cce901475380775f674b9cc5755f1f89f82e
git -C tool rev-parse HEAD
node --version
npm --version
cd tool
npm ci --ignore-scripts --no-audit --no-fund
cd ..
~~~

This recipe deliberately pins the source, not moving `main` or `npx latest`.
At this revision RepoTend 0.1.0 locks `yaml` 2.8.1, TypeScript 5.9.3,
`@types/node` 22.15.30, and `undici-types` 6.21.0 in `package-lock.json`.
Use `npm ci`, not a dependency update. `--ignore-scripts` disables install hooks;
it does not make untrusted tool code safe. Do not use `npm run audit` without
an explicit target: its default would inspect the tool checkout.

## 2. Select and pin the target

Choose your own public URL and full commit, or copy this worked example:

~~~sh
git clone https://github.com/grove/foundryline.git target
git -C target checkout --detach 5dc1dd15836584a1112caec224d479df8deffc9f
git -C target rev-parse HEAD
git -C target status --porcelain --untracked-files=all
target_root="$PWD/target"
report_root="$PWD/reports"
mkdir "$report_root"
~~~

Use a fresh disposable checkout with no target hooks, builds, installs, or scripts.
Record URL, full SHA, actual working-tree changes, date, environment, tool revision,
and lockfile identity. A SHA alone does not describe dirty files. For a private
repository, keep reports and source identities private unless publication is
authorized. Provision source through your host when cloning is unavailable.

The scope is RepoTend's 13 local convention/workflow checks under the default
`small-oss` profile. Review any `.repotend.yml` as data: disabled rules are omitted,
enforcement changes exits, and suppressions record exceptions. This reference
target has no such configuration. Do not add configuration to make results green.

## 3. Run and retain actual outputs

Still in `maintain-work`, run only the trusted auditor, with an explicit root:

~~~sh
cd tool
node skills/repotend/scripts/audit.mjs --root "$target_root" --format json > "$report_root/report.json" 2> "$report_root/json.stderr.txt"
json_exit=$?
printf '%s\n' "$json_exit" > "$report_root/json.exit.txt"
node skills/repotend/scripts/audit.mjs --root "$target_root" --format markdown > "$report_root/report.md" 2> "$report_root/markdown.stderr.txt"
markdown_exit=$?
printf '%s\n' "$markdown_exit" > "$report_root/markdown.exit.txt"
cd ..
git -C target status --porcelain --untracked-files=all
~~~

Capture exits immediately; in shells configured to stop on errors, arrange to
retain nonzero exits too. Keep stdout/stderr unedited, even when empty, and retain
the exact commands, cwd, runtime versions, duration and warnings. These are two
invocations, not a fabricated Markdown translation. Do not change inputs between
them. JSON carries confidence, evidence, rule versions, enforcement, and exceptions
that the short Markdown table omits. RepoTend reports `repository.path: "."` rather
than the commit: retain target identity beside the reports.

The audit reads local files. It does **not** run target code, install target
dependencies, change target files, contact GitHub, or invoke remediation. Keep
output redirections outside the target. For hostile inputs use host-enforced
filesystem/network restrictions; this guide and before/after observations are
not a universal sandbox guarantee. Do not call `remediate.mjs` in this recipe.

| Exit | Interpretation |
| --- | --- |
| `0` | Completed without enforced failure; warnings/unknowns may remain |
| `1` | Completed with explicitly enforced verified violations |
| `2` | Configuration/execution error; **UNAVAILABLE / INCOMPLETE**, never clean PASS |
| Missing process, dependency, source, or report | **UNAVAILABLE / NOT RUN**, never a completed audit |

If a process cannot start, preserve the shell error/exit rather than inventing a
RepoTend JSON report. Check both exit status and `errors[]`; partial findings do
not erase execution errors. Stop interpretation as a completed audit on failure.

## 4. Interpret narrowly, then triage

Preserve the upstream fields and meanings; do not invent a health score:

| Status/field | Meaning |
| --- | --- |
| `PASS` | That specific check found its expected condition; no comprehensive security verdict |
| `WARN` | Advisory deviation or heuristic recommendation; may be intentional |
| `FAIL` | Verified violation of a rule explicitly configured for enforcement |
| `UNKNOWN` | Reliable assessment unavailable; not PASS |
| `NOT_APPLICABLE` | The rule does not fit the available repository scope |
| `SUPPRESSED` | Visible WARN/FAIL covered by an active documented exception; not fixed or PASS |
| `confidence: verified` | Directly checked narrow property, e.g. local file presence; not policy authority |
| `confidence: heuristic` | Contextual clue, including some PASSes; investigate maintainer intent |

Keep `ruleId`, `ruleVersion`, `severity`, `enforced`, evidence paths/lines,
recommendations and suppression reason/expiry. Severity is separate from enforcement.
Organization defaults, branch protection, runner costs, runtime bugs and complete
workflow/security validity are outside this local scan. Follow the pinned
[rule catalog](https://github.com/grove/repotend/blob/2d69cce901475380775f674b9cc5755f1f89f82e/docs/RULE_CATALOG.md),
[report contract](https://github.com/grove/repotend/blob/2d69cce901475380775f674b9cc5755f1f89f82e/docs/REPORT_CONTRACT.md),
and [configuration semantics](https://github.com/grove/repotend/blob/2d69cce901475380775f674b9cc5755f1f89f82e/docs/CONFIGURATION.md).

For each finding worth pursuing:

1. Read the cited source at the audited revision. Consult actual project policy,
   original requirements and exceptions; recommendations are not approved obligations.
2. Look for counterevidence, alternate file layouts, inherited organization defaults
   and intentional workflow settings. Treat missing remote context as **UNKNOWN**.
3. When authorized, search open **and closed** issues and relevant PRs. For GitHub:
   `gh issue list --repo OWNER/REPO --state all --limit 100 --json number,title,body,state,url`.
   Record the returned inventory/time; paginate if it reaches the cap. Compare
   behavior/scope, not titles alone. Unavailable/incomplete lookup is **NOT CHECKED**,
   requiring review before any later publication.
4. Choose one useful disposition: propose an issue, investigate, ask for a policy
   decision, defer, identify a duplicate, or take no action. A no-action outcome
   with reasons is successful triage. Never open one issue per warning by default.

## 5. Prepare an unpublished handoff

Optionally use the [shared evidence and decision handoff](../docs/evidence-handoff-template.md)
to summarize existing receipts; see the [Maintain sample](../examples/evidence-handoff-samples.md#maintain).
This adds no required record format or execution stage.

For a justified new task, draft an issue with a plain-language problem, pinned
source/policy links, supporting and counterevidence, rule ID/confidence, priority
rationale, proposed acceptance criteria, decisions/gaps, and verification labeled
**PROPOSED — NOT RUN**. Mark **NOT PUBLISHED**, with no invented issue URL or approval.
Use **Confirm before fixing** for suspected runtime defects without runtime evidence.
For an unresolved policy choice, explicitly draft a decision proposal instead of
claiming a defect. See the [worked proposal](../examples/repo-maintenance/issue-proposal.md).

No saved Intentline record, issue/settings write, fix, commit to the target,
remediation apply, or schedule is authorized by a report or draft. Any later
publication or implementation needs its own effect authorization. Automatic
issue creation and schedules remain future, separately tested options.

## 6. Check adoption and failure behavior

Have another maintainer or separately configured agent follow this guide in a
fresh checkout, recording actual commands, deviations, safety limits, elapsed
effort and unknowns. Shared hardware/operator is a limitation, not independent
administration. Do not substitute a second same-operator rerun for this check.

For a safe negative control, point the auditor at a deliberately nonexistent
absolute path outside all repositories. Retain stderr and exit; expect an
unavailable target (exit 2 at this pin), no completed JSON report, and no issue
from that failed run. Do not create the missing path as a fallback. The
[example receipts](../examples/repo-maintenance/README.md) show the observed outcome.

Record what actually ran separately from proposed future checks. A failure to
install or audit remains an honest failed attempt. Structural reference tests
only check retained artifacts; they do not rerun RepoTend or qualify every host.
