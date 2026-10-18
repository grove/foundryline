# Foundryline Maintain — accepted manual reference for v0.2

**Decision: ACCEPTED — NARROW MANUAL MAINTAIN ONLY (2026-10-18).**  
**Authority boundary:** Project-direction acceptance after the merged, evidence-backed Maintain PRs; this records a scope decision, **not** independent cross-host or security certification. Human/operator acceptance is separate from actual CLI runs, agents and CI observations.

**What is accepted:** A copyable operator-invoked, **read-only RepoTend audit recipe**, including a separately observed **GitHub Actions `workflow_dispatch`** launch. Audits produce *advisory evidence for human triage*, not approved fixes, issue publication, health scores or policy changes. See [the recipe](../patterns/maintain.md), [actual local audit](../examples/repo-maintenance/README.md), [separate-agent adoption](../examples/repo-maintenance/adoption.md), [GitHub button instructions](manual-intake.md) and [issue #10](https://github.com/grove/foundryline/issues/10) / [#15](https://github.com/grove/foundryline/issues/15).

## What actually ran

| Evidence | Real observations | Scope |
| --- | --- | --- |
| [Manual local RepoTend pilot](../examples/repo-maintenance/README.md), [PR #14](https://github.com/grove/foundryline/pull/14) | macOS/Darwin 25.6.0 arm64, Node **v26.12.0**, npm **11.20.0**; RepoTend `2d69cce901475380775f674b9cc5755f1f89f82e` audited Foundryline `5dc1dd15836584a1112caec224d479df8deffc9f`. Real JSON and Markdown exit **0**; **6 PASS / 7 WARN**, `errors: []`. Target's 48 recorded files matched before/after. | Default `small-oss` advisory profile, 13 local convention/workflow checks; no target dependency install, tests, repairs or GitHub writes. |
| [Manual pilot negative control](../examples/repo-maintenance/receipts/missing-target/command.json) | Missing selected `--root`: exit **2**, actual ENOENT stderr, **empty stdout and no complete report**. | Must be `UNAVAILABLE / INCOMPLETE`, never a clean audit or `PASS`. |
| [Separate-agent adoption](../examples/repo-maintenance/adoption.md) | Separate agent, fresh checkouts and npm cache reproduced exact JSON and Markdown findings, plus the missing-target refusal. | **Same physical host, account/operator and runtime**. Not an independent other-platform test. |
| [GitHub-hosted PR qualification](https://github.com/grove/foundryline/actions/runs/39112424979), [PR #16](https://github.com/grove/foundryline/pull/16) | GitHub-hosted `ubuntu-24.04`, pinned tool, real audit and missing-target negative, 5 PASS / 8 advisory WARN; report artifact uploaded and read back. | A PR event is not proof of manually clicking the Run button. |
| **[Real manual button run #39112708357](https://github.com/grove/foundryline/actions/runs/39112708357)** | Event **`workflow_dispatch`**, targeted Foundryline revision `845391707f3aa280d2df37969422831489f6f493`, Ubuntu 24.04, Node 22.20.0; report exit **0**, **5 PASS / 8 WARN**, `errors: []`. Missing-target control exit **2**, ENOENT and no JSON; before/after Git statuses clean. Uploaded 7-day [artifact 12130119514](https://github.com/grove/foundryline/actions/runs/39112708357/artifacts/12130119514), separately inspected. | This **proves a manual trigger actually ran** with the narrow pinned setup. The artifact was temporary (expires 2026-10-25); [issue #15](https://github.com/grove/foundryline/issues/15) preserves its identities, digest and witnessed results. |

**CLI identities:** RepoTend's pinned tool SHA for these Maintain runs is a historical, actually tested revision, not floating `main`. GitHub Actions configuration requests `contents: read`, nonpersistent checkout credentials, separate pinned tool/target trees, a seven-day report artifact and an expected-failure control. It does **not** contain `schedule`, issue-writing permission or remediation.

## What human triage actually concluded

The local audit's `repo.contributing` WARN was a useful **policy question**, *not* a confirmed violation. Its [contribution-guide proposal](../examples/repo-maintenance/issue-proposal.md) is explicitly **NOT PUBLISHED** and needs the maintainer's decision before becoming an issue. Other WARNs are advisory and may be intentional.

A finding's `confidence: verified` means a narrow fact was checked, not that a rule is organizational policy or that a fix is authorized. A heuristic PASS/WARN cannot certify security. Neither exit 0 nor a green Actions job means there are no maintenance concerns.

## Acceptance boundaries

**Accepted for these observed configurations and modes:**

- An operator selects the target and revision, installs/trusts a pinned RepoTend checkout separately, runs a manual JSON/Markdown audit, retains raw stderr/exits, and triages warnings.
- A user can use the copyable GitHub `Run workflow` action to collect a bounded, read-only report; at least one **actual `workflow_dispatch`** succeeded on the recorded Ubuntu runner.
- A missing source or execution failure cannot be promoted to a successful completed audit. A separate-agent fresh-workspace reproduction on the same host supports usability.

**Not accepted, not demonstrated or not enabled:**

- **No scheduling**, autonomous Gapline agent on GitHub, periodic discovery/intake, automatic issue creation, PR creation, code fixes, remediation `--apply`, deployment or merges.
- No general cross-host sandbox or arbitrary-repository security guarantee, complete repository-health score, GitHub organization/settings access, target-code verification or proof that advisory warnings are defects.
- No external, independently administered second operator; an independent agent on a shared host is not such an operator.
- A green report is **not** permission to publish or modify the audited target.

This is a qualified **manual reference blueprint**, not a maintained third-party SaaS or a cross-platform certificate. A later scheduled intake or issue-writing workflow requires its *own authorization and real execution evidence*.

## Decision, release implications, and verification

**Scope decision:** Accept Maintain's **manual local path and actually triggered, read-only GitHub Actions example** as usable v0.2 reference material, limited as above. This is not evidence that a schedule has been designed or qualified.

The previous acceptance state for [Discover v0.1](discover-v0.1-qualification-review.md) remains unchanged. The separate [Deliver scoped decision](deliver-v0.2-qualification-review.md) covers code changes and selected Proofline checks, not repository maintenance audits.

All offline structural and receipt tests remain useful regression checks, not new tool executions or host qualifications. Run from Foundryline root:

```sh
python3 -B -m unittest discover -s checks -v
```

**Publication:** Nothing in this decision tags or publishes a release; see the [v0.2.0 release candidate notes](releases/v0.2.0.md) for the separate publication gate.
