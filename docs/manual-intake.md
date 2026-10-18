# Run a read-only repository health check from GitHub

**Status: manual GitHub-hosted RepoTend audit QUALIFIED for the observed Ubuntu 24.04 / Node 22 runner.** The [manual `workflow_dispatch` run](https://github.com/grove/foundryline/actions/runs/39112708357) completed successfully on 2026-10-18 after [PR #16](https://github.com/grove/foundryline/pull/16) merged. The report, negative test, target commit, exact tool version and retained artifact were independently inspected. This completes [issue #15](https://github.com/grove/foundryline/issues/15) for the **narrow deterministic manual-audit scenario**, not scheduled intake, Gapline agents, issue publication or a general sandbox guarantee.

You do **not** need an AI account to run this check. It uses [RepoTend](https://github.com/grove/repotend), a deterministic auditor that checks useful GitHub repository basics. It never creates issues or applies fixes on your behalf.

## Run it in Foundryline

1. Open the repository's [GitHub Actions](https://github.com/grove/foundryline/actions) page.
2. Select **Manual RepoTend maintenance audit** and click **Run workflow**. Choose the branch you want to inspect. Only repositories where the workflow is present on the default branch will offer this button.
3. Open the resulting run. Read the **RepoTend read-only audit** job summary, then download the **repotend-maintain-…** artifact for raw findings, actual commands/versions and errors.
4. Review any findings yourself. A warning is a suggestion, **not** proof that something must be changed. Use the [Maintain recipe](../patterns/maintain.md) for source/exception checks and duplicate triage before writing an issue.

There is no schedule. In addition to the manual button, this reference also runs **on PRs that change the workflow, this guide or its checks**, which helped verify the implementation before merge. **The later, distinct `workflow_dispatch` run is now observed and recorded below.**

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

**Limits of the PR qualification:** PR-mode results alone did not qualify the manual button. That missing observation was separately supplied by the actual `workflow_dispatch` run below. No independently administered second runner/operator, general network/filesystem sandbox guarantee, automated issue publication or schedule has been qualified. The runner's Node 20-based pinned setup/upload actions emitted a deprecation warning while the host used a Node 24 override; both steps passed. Review tool-action versions on future updates.

## Observed manual-button workflow dispatch — 2026-10-18

This is the separate, **real `workflow_dispatch`** qualification that the earlier PR run could not establish. It is not an authored fixture or inferred result.

- **Run:** [GitHub Actions #39112708357](https://github.com/grove/foundryline/actions/runs/39112708357), event `workflow_dispatch`, initiated by GitHub actor `grove` on 2026-10-18 at **08:45:54 UTC**; completed **success** at approximately 08:46:13 UTC.
- **Audited target:** `grove/foundryline` at merge commit `845391707f3aa280d2df37969422831489f6f493`. **Pinned tool:** `grove/repotend@2d69cce901475380775f674b9cc5755f1f89f82e`.
- **Runner:** GitHub-hosted `ubuntu-24.04` (Linux `6.17.0-1022-azure`, x86-64), Node `v22.20.0`, npm `10.9.3`, RepoTend report version `0.1.0`, `small-oss` profile.
- **Observed audit:** `audit.exit: 0`, JSON `schemaVersion: "0.1"`, `mode: "audit"`, `errors: []`, **13 results: 5 PASS, 8 advisory WARN**. These are narrow repository-convention findings, not an overall health/security certification.
- **Observed negative control:** The deliberately nonexistent `absent-target` produced exit **2**, an ENOENT error in stderr, **no JSON/stdout**, and `validation.json` classified this as **UNAVAILABLE / INCOMPLETE** rather than a clean audit.
- **No observed target edits:** The captured Git working-tree statuses before/after the audit were both empty. This observation does not establish universal sandbox isolation or account for all possible side effects.
- **Evidence artifact:** [`repotend-maintain-39112708357-1`](https://github.com/grove/foundryline/actions/runs/39112708357/artifacts/12130119514), downloaded and inspected. ZIP SHA-256 `45091a26589f4779ce25a376abfdb9006446e8f703a15cd9f56c93c0b272516a`, expires **2026-10-25**. The inspected `identity.json`, `validation.json`, `report.json`, exit/stderr and before/after status are consistent with the run metadata and summary. The linked GitHub Actions run and [issue #15's evidence record](https://github.com/grove/foundryline/issues/15) remain available after the artifact expires.

**Qualified:** A real manually triggered RepoTend audit and expected unavailable-source control on **this specific GitHub-hosted runner and pinned tool setup**. **Not qualified:** schedules, general host isolation, unattended issue publication, code repair, Codex/Gapline agent invocation on GitHub Actions, cross-platform execution or automatic delivery.

## What this example does not do

No automatic GitHub issue publishing, fix application, self-scheduling, Gapline skill/model execution, PR creation, merging or deployment. A report is **information for a human decision**, not permission to change the repository.

**Qualification boundary:** Both the PR-run evidence and the **distinct manual `workflow_dispatch` evidence** above are observed in GitHub Actions, with a real missing-source control. Qualification applies only to the recorded pinned tool, runtime and runner; it does not authorize a schedule, issue/PR publication, remediation or general-purpose agent execution. The prior [local Maintain pilot](../examples/repo-maintenance/README.md) has separate host and reviewer limits.
