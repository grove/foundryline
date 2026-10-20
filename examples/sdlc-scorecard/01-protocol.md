# SDLC scorecard pilot #37 — scope and measurement protocol

**Status:** small, public-data **retrospective self-pilot** for [issue #37](https://github.com/grove/foundryline/issues/37), not independent Foundryline adoption or a qualified Learn execution. This protocol is being committed **before this pilot's new GitHub API cohort extraction**, but **after** the observation periods and after the author read the already-published [Learn example](../manual-learn/README.md) (including facts about PRs #20 and #22). It is **not prospective preregistration** and cannot eliminate selection bias.

## Scope, permission and privacy boundary

- **One repository:** [grove/foundryline](https://github.com/grove/foundryline), applying the guidance to its own public SCM history. This repository is a documentation/playbook project, **not a demonstrated production service**.
- **Observation window (UTC, start inclusive/end exclusive):** 2026-10-13 00:00:00 to 2026-10-20 00:00:00. **Descriptive baseline:** the immediately preceding seven days, 2026-10-06 00:00:00 to 2026-10-13 00:00:00. Baseline is a *time-window reference*, not a matched counterfactual or a measured pre-adoption state.
- **Population:** all GitHub pull requests with `merged_at` inside either window, regardless of creation date. No exclusions based on outcome, size or author. One GitHub PR counts once. A PR opened before the window and merged within it is eligible; unmerged/closed-without-merge PRs are ineligible for **merged-PR** measures (not silently coded as successful delivery).
- **Task-level convenience examples:** the pre-existing linked issue #18 → PR #20 and issue #21 → PR #22, chosen because the [manual Learn retrospective](../manual-learn/README.md) already provides independent source/check context. Report which window contains them. These examples are not a representative/random cohort.
- **Permitted collection:** public GitHub issue/PR metadata and public PR reviews only; no private GitHub endpoints, account cross-linking, developer feedback, service telemetry, surveys, local log collection, or new scheduled monitoring. No personal productivity rankings. Writing these public-data Markdown files on a feature branch and opening a review PR is the only publication; it does not authorize other public/private disclosures. Separate, explicit permission would be needed for any private deployment/SLO data or voluntary aggregated DevEx feedback.

## Primary data sources and reproducible manual method

1. Read GitHub's public [closed PR REST collection](https://api.github.com/repos/grove/foundryline/pulls?state=closed&per_page=100) (follow all pages until exhausted); filter by actual `merged_at` in the declared UTC windows rather than by the API's sort order, `closed_at` or issue labels. Record each included PR number, `html_url`, `created_at` and `merged_at`. Its individual PR page / [REST PR resource](https://api.github.com/repos/grove/foundryline/pulls/22) is the auditable source.
2. For an eligible PR, the optional [reviews resource](https://api.github.com/repos/grove/foundryline/pulls/22/reviews) can establish whether a qualifying *submitted human review* exists. Do not equate an issue comment, bot review, review request, GitHub merge, or no-review case with an observed review wait. If the source lacks a defensible first human review event, report **UNKNOWN/NOT MEASURED**, not zero.
3. Use original task/PR and [existing check receipts](../manual-learn/README.md) for **technical evidence only**. Explicit owner/user acceptance, human effort, customer usage, production deploys, incidents, service SLOs and success targets require their *own* primary records; do not infer them from merge/test status.

## Definitions and denominators (fixed before extraction)

| Lens | Definition | Denominator and limit |
| --- | --- | --- |
| **SCM merge throughput (not DORA)** | Count of PRs with `merged_at` in each exact seven-day window | **Per seven-day window**; a merge is *not* a deployment |
| **PR open-to-merge elapsed time (Flow proxy)** | For each eligible PR, `merged_at - created_at` in hours, UTC; summarize median | **N merged PRs** with both timestamps; not PR review wait, coding time or commit-to-production lead time |
| **First human review wait (Flow)** | `first qualifying submitted review time - created_at`, when defensibly observed | **N reviewed eligible PRs**; also report all eligible PRs lacking such a record; absent is **UNKNOWN**, not zero |
| **DORA / SRE / value** | Only actual revision-linked production deployments, defined service SLO or owner-approved customer/business outcome | **NOT MEASURED** without those first-party sources and an appropriate denominator; never substitute PRs, CI or releases |
| **Task acceptance / effort** | Explicit original-task approval, user acceptance and independently recorded human minutes per example task | **UNKNOWN** absent attributable primary records; do not use merged state as acceptance |

Report source links for **each numeric value**, UTC cutoffs, per-PR arithmetic and missing event links. Keep delivery, selected technical checks, customer value and unobserved fields in separate columns. No person-level performance, cross-repo ranking or composite Grove score. Any window comparison is descriptive only; this is an unpaired, tiny, retrospectively selected period with potentially competing changes.

**Decision gate:** Recommend a specific useful next observation only if its owner, source and permission are identifiable. If these public records do not change a real improvement decision, recommend **STOP / NO NEW INFRASTRUCTURE**, retain the no-data case and leave Learn unqualified. A proposed decision here is not an owner's actual acceptance.
