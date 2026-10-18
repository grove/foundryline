# Run a read-only repository health check from GitHub

**Status: implementation and qualification in progress.** This page describes the workflow proposed in [Foundryline issue #15](https://github.com/grove/foundryline/issues/15). A PR or local check cannot prove that the **Run workflow** button works: qualification requires an observed real GitHub-hosted job **and**, after merge, an observed manual dispatch. Until then, describe the button-driven flow as **NOT YET VERIFIED**.

You do **not** need an AI account to run this check. It uses [RepoTend](https://github.com/grove/repotend), a deterministic auditor that checks useful GitHub repository basics. It never creates issues or applies fixes on your behalf.

## Run it in Foundryline (after this workflow is merged)

1. Open the repository's [GitHub Actions](https://github.com/grove/foundryline/actions) page.
2. Select **Manual RepoTend maintenance audit** and click **Run workflow**. Choose the branch you want to inspect. Only repositories where the workflow is present on the default branch will offer this button.
3. Open the resulting run. Read the **RepoTend read-only audit** job summary, then download the **repotend-maintain-…** artifact for raw findings, actual commands/versions and errors.
4. Review any findings yourself. A warning is a suggestion, **not** proof that something must be changed. Use the [Maintain recipe](../patterns/maintain.md) for source/exception checks and duplicate triage before writing an issue.

There is no schedule. In addition to the manual button, this reference also runs **on PRs that change the workflow, this guide or its checks**, so the first version can be tested on a real GitHub runner before merge. That PR-based qualification is **not** proof that someone clicked the manual button.

## What is actually executed?

The [workflow](../.github/workflows/maintain-audit.yml) runs on GitHub's \`ubuntu-24.04\` runner using **Node.js 22.20.0**.

- Check out the **selected commit** of the current repository under \`target/\`. For a PR qualification run, this is GitHub's PR merge commit; for a manual launch, it is the chosen workflow branch's commit. Record the exact SHA rather than claiming it audited another revision.
- Check out **RepoTend at exactly \`2d69cce901475380775f674b9cc5755f1f89f82e\`** under separate \`tool/\`. Both checkout actions are pinned to a reviewed action SHA; both use \`persist-credentials: false\`.
- Install **only the pinned RepoTend tool dependencies** using \`npm ci --ignore-scripts --no-audit --no-fund\`. This downloads trusted tool dependencies in the tool directory. **No target repository dependencies, hooks, tests, builds or scripts are run.**
- Invoke the actual RepoTend \`audit.mjs --root <selected target> --format json\`. Preserve the real, unedited report, stderr and exit status outside the target checkout, together with tool/target SHA, Node/npm version and runner identity.
- Invoke the same auditor against a **deliberately absent target**, preserving the expected **exit 2**, nonempty error and empty stdout. It is a failure-control test, **not** a second successful audit.
- Confirm that the Git working-tree status is unchanged before and after; validate the report contract and the missing-target behavior. Upload a **7-day** artifact even if validation fails.

The workflow requests only GitHub \`contents: read\`. It supplies no model keys, issue-writing permissions, deployment credentials or remediation approval. Report creation and dependency installation happen **outside** the target checkout. Git status observations and configuration are meaningful limits, not a universal sandbox security proof.

## How to read the result

RepoTend's real JSON report is the source of truth.

| Result | Plain-language meaning |
| --- | --- |
| \`PASS\` | That specific rule passed; **not** a full security or CI certification |
| \`WARN\` | Advisory issue or suggestion; normal audit may still exit \`0\` |
| \`FAIL\` | An explicitly enforced rule did not pass; a completed audit may exit \`1\` |
| \`UNKNOWN\` | Missing information; **never** treat this as PASS |
| \`NOT_APPLICABLE\` | The check does not apply to this repository |
| \`SUPPRESSED\` | A visible finding has an applicable documented exception, not a fix |
| \`confidence: heuristic\` | Suggestion depends on context; check original policy and evidence |
| \`confidence: verified\` | A narrow property was directly checked; it is **not** an approved requirement |
| Audit exit \`2\` / invalid or missing report / nonempty \`errors[]\` | **UNAVAILABLE / INCOMPLETE**: investigate the execution rather than using any findings as a complete audit |

The workflow summary reports counts only. Download the artifact to see the underlying rule IDs and evidence. It deliberately does **not** draft or publish a GitHub issue, calculate a health score, or infer that a missing local file violates organization policy.

## Copy this into another repository

Copy [\`.github/workflows/maintain-audit.yml\`](../.github/workflows/maintain-audit.yml) to the *same path* in your repository. Review the workflow and the pinned upstream RepoTend revision with your own trust and dependency policy. The workflow audits the repository containing it, not a hard-coded Foundryline path. Keep the tool and target in separate checkouts, preserve \`--root\`, \`contents: read\`, credential non-persistence and the error checks.

For a simple manually triggered workflow you may **remove the narrowly scoped \`pull_request\` trigger** after qualification. Leave \`workflow_dispatch\`. Do **not** enable a \`schedule\` or automatic issue creation simply because this manual experiment works; they require separate validation and publication authority.

The selected GitHub runner must permit the pinned GitHub Actions and outbound downloads for Node/RepoTend dependencies. A failed install, disabled Actions setting, missing runtime, unknown target or absent artifact is an **incomplete run**, not a clean repository. Review [RepoTend's report contract](https://github.com/grove/repotend/blob/2d69cce901475380775f674b9cc5755f1f89f82e/docs/REPORT_CONTRACT.md) before customizing how findings are interpreted.

**Privacy:** In a private repository, audit results and file paths may reveal private project structure. Artifacts are stored by GitHub for seven days and their availability depends on repository permissions. Do not upload secret files, make them public, or copy receipts to an issue without authorization. This example has only been exercised with public Foundryline source; another host/visibility context needs its own review.

## What this example does not do

No automatic GitHub issue publishing, fix application, self-scheduling, Gapline skill/model execution, PR creation, merging or deployment. A report is **information for a human decision**, not permission to change the repository.

**Qualification records:** Once actual runs exist, link their GitHub Actions URLs, tool/target identities, observed counts, negative-path result and caveats here. Before that, any expected outcome is **PROPOSED — NOT RUN**. See the separately qualified [manual Maintain pilot](../examples/repo-maintenance/README.md), which is useful prior evidence but **does not substitute** for a real GitHub-hosted workflow run.
