# Public SCM scorecard — measured snapshot for issue #37

**Scope was recorded first:** [01-protocol.md](01-protocol.md), committed on the pilot branch before this measurement's cohort extraction. This is a **retrospective, self-selected public repository example**, not preregistered independent adoption, not a service outcome experiment, and not an end-to-end Learn qualification.

## Source and collection

- **Primary source:** [GitHub REST closed-PR collection](https://api.github.com/repos/grove/foundryline/pulls?state=closed&per_page=100), accessed 2026-10-20. It returned **25** closed PRs total in one page: **22** merged in the declared observation week and **3** merged on 2026-10-20 outside the window. There were **0** merged PRs in the preceding baseline week. For individual auditable identities and UTC event timestamps follow the linked PR pages below; GitHub's [PR API](https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request) provides the `created_at` and `merged_at` fields. The collection is a **snapshot**, not a retained immutable API capture.
- **Fixed week:** 2026-10-13 00:00:00 ≤ `merged_at` < 2026-10-20 00:00:00 UTC.
- **Baseline:** 2026-10-06 00:00:00 ≤ `merged_at` < 2026-10-13 00:00:00 UTC.
- **Computation:** one record per merged PR, `open_to_merge_seconds = (merged_at - created_at)`. Values below are integer seconds (exact precision of the source timestamps). For 22 records the median is the mean of ordered positions 11 and 12: (116 + 123) / 2 = **119.5 seconds**, approximately **1.99 minutes**. This is **not** the time required to build, review or verify the change.

## Minimal outcome table

| Lens / boundary | Observation | Denominator, primary source and limitation |
| --- | --- | --- |
| SCM merge throughput (**delivery-process proxy; not DORA**) | **22 merged PRs / 7-day observation window; 0 / 7-day baseline** | 22 PR links below, [closed-PR API](https://api.github.com/repos/grove/foundryline/pulls?state=closed&per_page=100). This is a burst of SCM merges, not demonstrated production delivery; no causal change comparison. |
| Open-to-merge elapsed time (**Flow proxy**) | **119.5 seconds median** (~1.99 min) | N=22 merged PRs, `created_at` → `merged_at`, auditable per PR below. Baseline median **NOT APPLICABLE** (N=0). Does not include work before PR creation. |
| First submitted human-review wait (**Flow**) | **NOT MEASURED** | Five [review endpoints](https://api.github.com/repos/grove/foundryline/pulls/22/reviews) spot-checked: PRs #1, #19, #20, #22 and #35 had zero submitted reviews returned. **Not** an exhaustive review-event audit of all 22; never interpret absent reviews as zero wait. |
| Commit-to-production lead time / deployment frequency (**DORA**) | **NOT MEASURED** | Production deployment event, production revision linkage and cohort **UNKNOWN**; merged PRs ≠ production deployments. |
| SRE / SLO, incident / recovery outcomes | **NOT MEASURED** | No scoped approved SLO, service population, telemetry or incident/deployment correspondence; no production service established. |
| Technical checks / correctness | **Limited historical selected-check receipts only; overall correctness UNKNOWN** | [Issue #21 → PR #22](../manual-learn/README.md) includes actual selected native receipt and unlinked obligations; no entire-request correctness inference. |
| Customer adoption, outcome / business value | **NO APPROVED OUTCOME TARGET; NOT MEASURED** | No primary usage, customer, revenue or other impact source; no user population, baseline or counterfactual. |
| Developer experience (SPACE), private telemetry | **NOT COLLECTED** | No separate consent; no person-level scores or account linkage. |

### Per-PR denominator and arithmetic

Each linked PR is a primary SCM record; number is an identifier, **not an author rank**. Seconds are differences of the linked PR's `created_at` and `merged_at` UTC timestamps. All 22 were merged on October 17–18, 2026; there were no other in-window merged PRs in the retrieved collection.

| Merged PR source | Open-to-merge (seconds) |
| --- | ---: |
| [#35](https://github.com/grove/foundryline/pull/35) | 2528 |
| [#34](https://github.com/grove/foundryline/pull/34) | 304 |
| [#33](https://github.com/grove/foundryline/pull/33) | 32 |
| [#27](https://github.com/grove/foundryline/pull/27) | 39 |
| [#26](https://github.com/grove/foundryline/pull/26) | 170 |
| [#24](https://github.com/grove/foundryline/pull/24) | 41 |
| [#23](https://github.com/grove/foundryline/pull/23) | 279 |
| [#22](https://github.com/grove/foundryline/pull/22) | 46 |
| [#20](https://github.com/grove/foundryline/pull/20) | 41 |
| [#19](https://github.com/grove/foundryline/pull/19) | 1428 |
| [#17](https://github.com/grove/foundryline/pull/17) | 75 |
| [#16](https://github.com/grove/foundryline/pull/16) | 416 |
| [#14](https://github.com/grove/foundryline/pull/14) | 336 |
| [#13](https://github.com/grove/foundryline/pull/13) | 21 |
| [#12](https://github.com/grove/foundryline/pull/12) | 24 |
| [#11](https://github.com/grove/foundryline/pull/11) | 32 |
| [#9](https://github.com/grove/foundryline/pull/9) | 116 |
| [#8](https://github.com/grove/foundryline/pull/8) | 123 |
| [#7](https://github.com/grove/foundryline/pull/7) | 442 |
| [#5](https://github.com/grove/foundryline/pull/5) | 38 |
| [#3](https://github.com/grove/foundryline/pull/3) | 335 |
| [#1](https://github.com/grove/foundryline/pull/1) | 134 |

## Two real task examples — don't equate merge with acceptance

| Task, source and observed SCM event | Separate technical acceptance | Human acceptance / overhead | Production, customer and decision impact |
| --- | --- | --- | --- |
| [#18](https://github.com/grove/foundryline/issues/18) → [PR #20](https://github.com/grove/foundryline/pull/20), merged 2026-10-18 10:05:18 UTC | Prior [Learn retrospective](../manual-learn/README.md) links a genuine native selected **27-test** passing receipt; full user-request acceptance **NOT ESTABLISHED** | Express task-level user acceptance **UNKNOWN**; actual human minutes **UNKNOWN** | Deploy/revision, service and customer effect **UNKNOWN / NOT MEASURED** |
| [#21](https://github.com/grove/foundryline/issues/21) → [PR #22](https://github.com/grove/foundryline/pull/22), merged 2026-10-18 10:29:21 UTC | [Source-to-check evidence](../manual-learn/README.md) reports R1/R2 limited linked checks; R3–R7 **NOT DEMONSTRATED** by selected checks. No composite correctness verdict. | Express task-level user acceptance **UNKNOWN**; actual human minutes **UNKNOWN** | Deploy/revision, service and customer effect **UNKNOWN / NOT MEASURED** |

The PRs' merger is a sourced SCM fact, not user acceptance. These two retrospective examples were selected from already-published documentation, **not** randomly sampled.

## Honest no-data case and next decision

**No-data case:** a perfectly real PR merge and passing selected tests for #21 still provide **no commit-to-production lead time, service SLO attainment or customer effect**. Without actual deployment records and a previously accepted service/customer measurement, assigning any numeric improvement or post-delivery impact would be fabrication.

**One reasonable next observation — not performed:** if an authorized service owner identifies a *real production service* and a revision-linked deployment inventory for one adopting repository, record the immutable deployment event/revision and a pre-existing permitted baseline/SLO definition **before** analyzing any outcome. Obtain explicit, separate read permission for private event logs; only use approved, appropriately aggregated voluntary feedback, if any. If none exists, leave outcome **UNKNOWN** and stop.

**Decision utility:** this self-pilot teaches one narrow improvement decision: **STOP / NO NEW DASHBOARD OR TELEMETRY**. Public PR metadata provides a reproducible SCM flow proxy, but cannot answer developer productivity, reliability or value. Do not roll out a composite score or mandatory measurement. An actual authorized owner decision and independent multi-period observation are **NOT RECORDED**; the stop recommendation is an analyst proposal, not a product-owner decision. If a second repo with existing deployment events becomes available, agree the observation period, permissions, baseline and exclusions *prospectively* and repeat as a distinct pilot. No causal claim can follow from this unpaired one-week self-snapshot.
