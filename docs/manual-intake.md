# Run a read-only repository health check from GitHub

**Status: real GitHub-hosted PR audit passed; the manual button launch is NOT YET VERIFIED.** This page tracks [Foundryline issue #15](https://github.com/grove/foundryline/issues/15). The identical audit job has run successfully on GitHub's Ubuntu 24.04 runner in PR mode, including its negative case. A PR run does **not** demonstrate that the **Run workflow** button has been clicked: after merge, a separate observed `workflow_dispatch` execution is required for that claim.

You do **not** need an AI account to run this check. It uses [RepoTend](https://github.com/grove/repotend), a deterministic auditor that checks useful GitHub repository basics. It never creates issues or applies fixes on your behalf.

## Run it in Foundryline (after this workflow is merged)

1. Open the repository's [GitHub Actions](https://github.com/grove/foundryline/actions) page.
2. Select **Manual RepoTend maintenance audit** and click **Run workflow**. Choose the branch you want to inspect. Only repositories where the workflow is present on the default branch will offer this button.
3. Open the resulting run. Read the **RepoTend read-only audit** job summary, then download the **repotend-maintain-…** artifact for raw findings, actual commands/versions and errors.
4. Review any findings yourself. A warning is a suggestion, **not** proof that something must be changed. Use the [Maintain recipe](../patterns/maintain.md) for source/exception checks and duplicate triage before writing an issue.

There is no schedule. In addition to the manual button, this reference also runs **on PRs that change the workflow, this guide or its checks**, so the first version can be tested on a real GitHub runner before merge. That PR-based qualification is **not** proof that someone clicked the manual button.

## What is actually executed?

The [workflow](../.github/workflows/maintain-audit.yml) runs on GitHub's `ubuntu-24.04` runner using **Node.js 22.20.0**.

- Check out the **selected commit** of the current repository under `target/`. For a PR qualification run, this is GitHub's PR merge commit; for a manual launch, it is the chosen workflow branch's commit. Record the exact SHA rather than claiming it audited another revision.
- Check out **RepoTend at exactly `2d69cce901475380775f674b9cc5755f1f89f82e`** under separate `tool/`. Both checkout actions are pinned to a reviewed action SHA; both use `persist-credentials: false`.
- Install **only the pinned RepoTend tool dependencies** using `npm ci --ignore-scripts --no-audit --no-fund`. This downloads trusted tool dependencies in the tool directory. **No target repository dependencies, hooks, tests, builds or scripts are run.**
- Invoke the actual RepoTend `audit.mjs --root <selected target> --format json`. Preserve the real, unedited report, stderr and exit status outside the target checkout, together with tool/target SHA, Node/npm version and runner identity.
- Invoke the same auditor against a **deliberately absent target**, preserving the expected **exit 2**, nonempty error and empty stdout. It is a failure-control test, **not** a second successful audit.
- Confirm that the Git working-tree status is unchanged before and after; validate the report contract and the missing-target behavior. Upload a **7-day** artifact even if validation fails.

The workflow requests only GitHub `contents: read`. It supplies no model keys, issue-writing permissions, deployment credentials or remediation approval. Report creation and dependency installation happen **outside** the target checkout. Git status observations and configuration are meaningful limits, not a universal sandbox security proof.

## How to read the result

RepoTend's real JSON report is the source of truth.

| Result | Plain-language meaning |
| --- | --- |
| `PASS` | That specific rule passed; **not** a full security or CI certification |
| `WARN` | Advisory issue or suggestion; normal audit may still exit `0` |
| `FAIL` | An explicitly enforced rule did not pass; a completed audit may exit `1` |
| `UNKNOWN` | Missing information; **never** treat this as PASS |
| `NOT_APPLICABLE` | The check does not apply to this repository |
| `SUPPRESSED` | A visible finding has an applicable documented exception, not a fix |
| `confidence: heuristic` | Suggestion depends on context; check original policy and evidence |
| `confidence: verified` | A narrow property was directly checked; it is **not** an approved requirement |
| Audit exit `2` / invalid or missing report / nonempty `errors[]` | **UNAVAILABLE / INCOMPLETE**: investigate the execution rather than using any findings as a complete audit |

The workflow summary reports counts only. Download the artifact to see the underlying rule IDs and evidence. It deliberately does **not** draft or publish a GitHub issue, calculate a health score, or infer that a missing local file violates organization policy.

## Copy this into another repository

Copy [`.github/workflows/maintain-audit.yml`](../.github/workflows/maintain-audit.yml) to the *same path* in your repository. Review the workflow and the pinned upstream RepoTend revision with your own trust and dependency policy. The workflow audits the repository containing it, not a hard-coded Foundryline path. Keep the tool and target in separate checkouts, preserve `--root`, `contents: read`, credential non-persistence and the error checks.

For a simple manually triggered workflow you may **remove the narrowly scoped `pull_request` trigger** after qualification. Leave `workflow_dispatch`. Do **not** enable a `schedule` or automatic issue creation simply because this manual experiment works; they require separate validation and publication authority.

The selected GitHub runner must permit the pinned GitHub Actions and outbound downloads for Node/RepoTend dependencies. A failed install, disabled Actions setting, missing runtime, unknown target or absent artifact is an **incomplete run**, not a clean repository. Review [RepoTend's report contract](https://github.com/grove/repotend/blob/2d69cce901475380775f674b9cc5755f1f89f82e/docs/REPORT_CONTRACT.md) before customizing how findings are interpreted.

**Privacy:** In a private repository, audit results and file paths may reveal private project structure. Artifacts are stored by GitHub for seven days and their availability depends on repository permissions. Do not upload secret files, make them public, or copy receipts to an issue without authorization. This example has only been exercised with public Foundryline source; another host/visibility context needs its own review.

## Observed GitHub-hosted PR qualification — 2026-10-18

This section records an **actual** workflow run, not authored sample output.

- **Run:** [PR #16's RepoTend audit, GitHub Actions run 39112223810](https://github.com/grove/foundryline/actions/runs/39112223810), event `pull_request`. All job steps, including pinned-tool setup, audit validation and artifact upload, completed successfully.
- **Source actually audited:** GitHub's PR merge commit `d7f15d7d72d769ee425d35360131f54e3521185c` for Foundryline, **not** the feature branch head or moving `main`. RepoTend: `2d69cce901475380775f674b9cc5755f1f89f82e`.
- **Runner and toolchain:** Linux `6.17.0-1022-azure` / Ubuntu 24.04, Node `v22.20.0`, npm `10.9.3`, RepoTend report version `0.1.0`, default `small-oss` profile.
- **Real output:** Audit exit `0`, `errors: []`, **5 PASS, 8 WARN**, 0 enforced FAIL. The `report.json` retained all 13 actual rule records. Advisory warnings do not imply failed execution or approved fixes.
- **Witnessed failure control:** Audit against an intentionally missing source returned **exit 2**, an ENOENT diagnostic, and **zero stdout bytes**. Its validation explicitly recorded **UNAVAILABLE / INCOMPLETE**.
- **Mutation observation:** Both captured Git status files were empty/identical; no target repository changes observed. This is not an OS-level write trace or proof of host isolation.
- **Artifact:** [`repotend-maintain-39112223810-1`](https://github.com/grove/foundryline/actions/runs/39112223810/artifacts/12130584153), SHA-256 ZIP digest `0825279c93bfa73aeba6df9e4d4705129b692b60c7cc1c76fd7f8d3066ce6379`, expires 2026-10-25. The archive was **downloaded and inspected**: `identity.json`, `validation.json`, `report.json`, stderr, both exits, and before/after Git statuses matched the above observations.
- **Reference checks:** [The same PR's structural validation run](https://github.com/grove/foundryline/actions/runs/39112223790) passed all **20 Python tests**. Those tests alone cannot demonstrate real runner behavior.

**Unqualified:** No `workflow_dispatch` event has yet been observed, no separately administered second runner/operator repeated this job, and no generic network/filesystem sandbox guarantee is asserted. The runner's Node 20-based pinned setup/upload actions emitted a deprecation warning while the hosted runner used the Node 24 override; both steps nevertheless passed. Review tool-action versions on future updates.

## What this example does not do

No automatic GitHub issue publishing, fix application, self-scheduling, Gapline skill/model execution, PR creation, merging or deployment. A report is **information for a human decision**, not permission to change the repository.

**Qualification boundary:** The PR-run evidence above is observed and archived in GitHub Actions; `workflow_dispatch` verification remains **PROPOSED — NOT RUN** until a separately observed manual launch. See the previously tested [local Maintain pilot](../examples/repo-maintenance/README.md), which has separate host/runner limits.
