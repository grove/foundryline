# Learn — review what happened after delivery (optional, manual)

**Status: PROPOSED DOCUMENTATION — NOT QUALIFIED.** This is a manual fourth recipe, not part of the accepted v0.2.0 Discover / Deliver / Maintain scope. It does not run tools, collect telemetry, create issues, or assert any adoption or outcome.

**Question:** We agreed to change something, and selected checks may have passed. **Did the actual change produce the expected outcome, and what do we know versus merely hope?**

Use an existing coding assistant or a human reviewer. No Foundryline runtime, central database, dashboard, model dispatch, special permissions or additional agent is needed. Skip Learn for a change with no defensible post-delivery observation; recording **UNKNOWN** and a next observation is useful.

## First run: one approved change, one outcome

1. **Identify authority and scope.** Choose one real request/issue with its *original* text and accepted decisions/exceptions; record the exact repository, relevant commits/candidate, PR, and any known deployment/version correspondence. A closed issue or merged PR does not establish deployed behavior. Check access to each record. Do not infer access or authority from a URL.
2. **Separate the promises.** State (a) the user-visible technical acceptance obligation from the source, and (b) the desired user/business effect **only if it was actually supplied or approved**. Without the latter, say `NO APPROVED OUTCOME TARGET`; don't invent a goal or retrofit a successful metric.
3. **Read existing verification, don't simulate it.** Link any genuine Proofline report/status and exact selected check identities, or ordinary test receipts if available. Preserve `CHECKS PASSED` as evidence for *selected checks*, not proof of complete requirements. Missing/unlinked obligations are `NOT DEMONSTRATED`; stale/missing receipts are `STALE`/`UNAVAILABLE` as applicable.
4. **Look for primary post-delivery observations.** With authorized read access, check the exact deployed revision and event/time window where possible. Examples: change-to-production timestamps for DORA, actual incident/recovery records for SRE/SLO, PR waiting time for Flow, a pre-existing usage/customer outcome measure for OKR. State numerator/denominator, timezone, comparison baseline and limitations for any number. Do not use issue closure, a green CI run, generated prose, or a code commit as a proxy for production performance or customer value. **If attribution to the deployed candidate is unavailable, the outcome is UNKNOWN.**
5. **Decide what follows.** A human reviewer challenges alternate explanations and missing data, then records one limited decision: `CONTINUE`, `INVESTIGATE`, `CHANGE PLAN`, `DEFER`, or `NO ACTION`, including who decided and why. Optional: ask Gapline for a separately authorized, **read-only** inquiry of an observed mismatch. No permission to execute, create issues, fix code, merge or deploy passes automatically from Learn.

## One-page handoff (copy into an approved private place, if desired)

Use the existing [evidence and decision handoff](../docs/evidence-handoff-template.md) and link native records. This short outline is **not** a replacement schema:

| Question | Record only what primary sources establish |
| --- | --- |
| What was requested? | Original request/policy link, accepted exceptions, technical obligations, owner |
| What changed? | Repository, base/candidate SHA, PR, and **observed** deployed revision if known |
| What was checked? | Genuine command/test receipts, status, source and candidate identities, omissions |
| What happened after delivery? | Real incident, deployment, SLO, usage or customer records and window; otherwise **UNKNOWN / NOT OBSERVED** |
| Did we achieve the objective? | Approved outcome and its observed value/baseline, or **NOT ESTABLISHED** |
| What's next? | Competing explanations, one smallest next observation, human decision and publication permissions |

### Worked evidence-limited example — historical sources, not a Learn execution

See the [source-linked issue #21 → PR #22 retrospective and separate no-data control](../examples/manual-learn/README.md). Its independent GitHub PR merge observation establishes delivery in source control only, not a production or customer outcome.

The [Deliver requirement trace](../examples/manual-deliver/intentline-trace/README.md) documents a real, limited source-to-candidate check and a `NOT DEMONSTRATED` state for an unlinked obligation. The [Deliver qualification review](../docs/deliver-v0.2-qualification-review.md) limits the accepted claim to selected checks and explicitly keeps overall requirement coverage unknown.

From those records alone, this **Learn example** can state:

- **Original request / candidate / checks:** see the actual linked Deliver records; they are historical verification evidence, not a new execution of this recipe.
- **What selected checks showed:** limited source-linked evidence, with unlinked requirements explicitly not demonstrated; do not claim the full original request was satisfied.
- **Deployed production revision and date:** **UNKNOWN — NOT OBSERVED** in these referenced Deliver records.
- **DORA change lead time, change failure/rework, SLO, usage, business outcome:** **NOT MEASURED**. No release event, service telemetry, customer denominator or approved product success measure has been established by this example.
- **Possible next observation:** if an authorized owner wants a production evaluation, first identify a specific deployment event and an existing, permitted primary outcome source; otherwise stop without manufacturing success evidence.
- **New decision / authorization:** **NONE RECORDED**. This documentation is not a product-owner release decision.

The example deliberately **does not demonstrate a successful post-delivery observation**. An actual end-to-end Learn qualification requires a separate, real, authorized deployment/outcome observation linked to the selected candidate. Until then, mark the new recipe **UNQUALIFIED**.

## Guardrails and evaluation

- Do not automatically collect personal developer data. SPACE/DevEx feedback is opt-in, appropriately aggregated, and separate from individual performance scoring.
- DORA metrics need actual deployment/incident identities and consistent definitions; Flow measures need timestamped workflow transitions; SRE/SLO need approved service objectives and monitored intervals; OKR/customer claims need an actual decision-maker and primary source. Leave absent data **UNKNOWN**.
- Observed association is not causal attribution. Account for selection, traffic, release differences and competing factors before claiming impact.
- Reads, model access, saving evidence, running commands and publishing an issue each need independently scoped permission. Prompt text alone does not enforce read-only access.
- To qualify Learn, run a new manual pilot on one accessible real change with a source-bound technical obligation and actual post-delivery primary evidence; record time/overhead and a no-data control, obtain independent review, and compare whether Learn changed a useful decision. **No pilot was run by adding this file.**

Related: [post-delivery Learn issue #36](https://github.com/grove/foundryline/issues/36), [metrics pilot issue #37](https://github.com/grove/foundryline/issues/37), [cold-start Discover #29](https://github.com/grove/foundryline/issues/29), and [cold-start Deliver #30](https://github.com/grove/foundryline/issues/30).
