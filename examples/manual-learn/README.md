# Learn retrospective — issue #21 to PR #22 (evidence-limited)

**Retrospective assembled from existing public records; NOT a new Learn pilot.**
This is a worked example for the [optional Learn recipe](../../patterns/learn.md).
No tool was run against a deployed service, no customer outcome was measured, and
no human product decision is claimed here. The original records, not this summary,
are the authority for their narrow observations.

## 1. Original intent and approved change

- **Real source:** [Foundryline issue #21](https://github.com/grove/foundryline/issues/21),
  the complete [original S1 body](../manual-deliver/intentline-trace/export/source-S1.txt),
  SHA-256 `3c1a808cc0dfad337b88f47b61a7513182c829ab0a96efbcf8bc443c07a343bf`.
  [Issue capture](../manual-deliver/intentline-trace/issue-21.json) has the source and
  [the authorization transcription](../manual-deliver/intentline-trace/authorization.txt)
  records implementation/PR permission, not an authenticated product-owner
  deployment approval. The issue's R1–R7 address source/coding provenance,
  actual Intentline export, Proofline linkage, evidence gaps, refusals and handoff.
- **Approved change as recorded:** Add real producer/export identity and source
  citation checks with an optional Intentline → Proofline trace; do not convert
  selected checks into whole-request acceptance. The
  [implementation account](../manual-deliver/intentline-trace/README.md#original-request-and-authority)
  and [merged PR #22](https://github.com/grove/foundryline/pull/22) describe that
  scope. A draft acceptance export was **unapproved**, not a product decision.
- **Frozen coding candidate:** `grove/foundryline@f54d44eb1d21fae2d7cfd8aae4216e91019a87d3`,
  tree `a003d013419fd1f142f0d05175938c6b0d7008f3`.
  Proofline's synthetic frozen snapshot commit
  `191c64bf4d7c785a668b5d035e8063dd257b7244` has that **same tree**.
  These identities come from the
  [candidate/consumer record](../manual-deliver/intentline-trace/README.md#frozen-candidate-and-actual-native-consumer)
  and [structured readback](../manual-deliver/intentline-trace/verification.json);
  they are **not** the final PR HEAD or a deployed release identity.

## 2. Four separate kinds of evidence

| Layer | What is actually supported | Limit |
| --- | --- | --- |
| **A. Source-grounded technical acceptance** | S1 has R1–R7, with source line references and separate acceptance obligations; the [source/citation inventory](../manual-deliver/intentline-trace/README.md#maintainer-handoff-original-request--implementation--evidence) records each. | An advisory Intentline export and human-readable mapping are not human approval or complete acceptance. `coverage_completeness: UNKNOWN`. |
| **B. Selected verification** | Real [macOS native run 39118875068](https://github.com/grove/foundryline/actions/runs/39118875068), exact [SOURCE/EXPORT selections](../manual-deliver/intentline-trace/README.md#exact-selections-and-observed-gap), [gap mapping](../manual-deliver/intentline-trace/gap-links.json), [linked mapping](../manual-deliver/intentline-trace/linked-links.json), [readback](../manual-deliver/intentline-trace/verification.json), and retained [raw native ZIP](../manual-deliver/intentline-trace/native-run.zip). | The first selected SOURCE test passed for R1 while R2–R7 were **NOT DEMONSTRATED**. Adding the separate EXPORT test gave R1/R2 **LINKED CHECKS PASSED (limited evidence)**; R3–R7 remain **NOT DEMONSTRATED** by selected checks. No total-request proof. |
| **C. Independently sourced post-delivery event** | GitHub [PR #22](https://github.com/grove/foundryline/pull/22) records **merged** on **2026-10-18 10:29:21 UTC**. This is a real SCM delivery event, sourced from GitHub PR metadata rather than inferred from a test report. | A merged PR is **not** evidence of a production deployment, runtime behavior, user adoption, or outcome. The checked implementation tree is not demonstrated to match a deployed artifact. |
| **D. Unobserved impact** | **NOT OBSERVED / UNKNOWN:** deployed revision and deployment timestamp, service/incident observations, customer usage, business effect, and any approved success target. | There is no valid attribution window, population, baseline or denominator for a production or business claim. |

The [native validation record](../manual-deliver/intentline-trace/README.md#actual-refusal-and-counterevidence)
also retains a rejected mismatched argv map (exit 1) and a distinct local
`EXECUTION UNAVAILABLE` (exit 2). These are genuine limits/refusals, **not**
proof of broken or successful production behavior. Historical
[Deliver acceptance](../../docs/deliver-v0.2-qualification-review.md) is a
narrow recipe-scope decision, not an outcome measurement for issue #21.

**Loop:** original issue #21 intent → approved, frozen coding candidate →
selected native SOURCE/EXPORT receipts → independently observed PR #22 merge
*only* → **decision: impact UNKNOWN, request evidence before any impact claim**.
That last phrase is a proposed analytical disposition here, **not** a
recorded owner decision.

## 3. Negative/no-data control — green checks are not impact

A second real, bounded record illustrates the same refusal to infer impact:
[issue #18](https://github.com/grove/foundryline/issues/18) →
[PR #20](https://github.com/grove/foundryline/pull/20).
Its [documented frozen implementation](../manual-deliver/agent-qualification/README.md#actual-candidate-and-execution)
was `01d2db090713a8852a66d1dfddca90bf7cac548a`, and
[native run 39117358329](https://github.com/grove/foundryline/actions/runs/39117358329)
reported `CHECKS PASSED` for **27 selected tests** on a matching frozen tree.
GitHub records PR #20 merged on **2026-10-18 10:05:18 UTC**.
**Post-delivery service/customer observation: NOT OBSERVED / UNKNOWN.**
There is no demonstrated deployed revision or approved impact baseline in the
cited records. Do **not** turn 27 passing checks plus a merge into improved
reliability, faster delivery, customer value, or ROI. This is a documentation
no-data control using historical evidence, **not a newly executed negative test**.

## 4. Metrics and the next authorized decision

| Lens | Primary data required before reporting a value | Status here |
| --- | --- | --- |
| **DORA** | Deployment events linked to exact revisions, incidents/rollback or restore events, defined period and consistent change population; throughput and instability must not be inferred from one PR. | **NOT MEASURED** |
| **SRE / SLO** | Approved service-level objective, actual service telemetry, eligibility/denominator and observation window. | **NOT MEASURED** |
| **Flow** | Defined workflow boundaries, timestamped start/wait/end records, cohort and timezone. A merge timestamp alone is insufficient. | **NOT MEASURED** |
| **OKR / business** | Pre-existing authorized outcome target, baseline, primary customer/business source, population/window and alternatives. | **NO APPROVED OUTCOME TARGET / UNKNOWN** |

**Concrete next check, PROPOSED — NOT RUN:** Ask the authorized repository or
service owner whether PR #22 corresponds to an identifiable deployed artifact.
If it does, obtain **separate read permission** for a narrowly scoped existing
deployment log and its service or customer observation for a specified interval.
Confirm the candidate-to-deployment mapping, comparison baseline and competing
changes before considering an outcome claim. If it does not, record
`NOT DEPLOYED` **only if a primary deployment inventory confirms it**;
otherwise retain `UNKNOWN`. If no suitable primary source exists, stop.

**Permission boundaries:** Reading public issue/PR and historical receipts
does **not** authorize private telemetry access, saving a record in a tracker,
publishing a new issue, making a code change, scheduling checks, or deployment.
The optional [shared handoff template](../../docs/evidence-handoff-template.md)
can be copied into an **explicitly authorized** destination after access and
privacy review; nothing in Learn performs a write automatically.

**Independent review questions (NOT PERFORMED for this example):** Can a
reviewer verify the S1 hash and candidate tree against the raw linked records?
Do the selected assertions test user behavior or only provenance? Was the
exact candidate deployed, and where is that record? What else changed in the
window, and what evidence would disprove a claimed effect? Which source/denominator
is absent? The answer here cannot be `SUCCESSFUL IMPACT` just because GitHub
reports `merged`.
