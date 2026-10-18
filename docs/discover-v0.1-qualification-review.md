# Foundryline Discover v0.1 — Evidence Review and Release Recommendation

**Status:** REVIEW COMPLETE; **SCOPED MANUAL DISCOVER V0.1 ACCEPTED BY MAINTAINER on 2026-10-18**, limited to the recorded macOS/Codex setup.  
**Review date:** 2026-10-18 (Europe/Oslo).  
**Related:** [Issue #6](https://github.com/grove/foundryline/issues/6) · [Issue #4](https://github.com/grove/foundryline/issues/4) · [PR #5](https://github.com/grove/foundryline/pull/5) · [Discover runbook](../patterns/discover.md) · [Retained pilot](../examples/repotend-pilot/README.md).

## Executive conclusion

**Decision: ACCEPT SCOPED V0.1.** This was the review's conditional recommendation; the maintainer accepted it on 2026-10-18, [recorded in issue #6](https://github.com/grove/foundryline/issues/6). The acceptance does **not** add new technical evidence or broaden the test scope.

The retained records support a **real, bounded, manual Discover demonstration** on the specified macOS/Codex setup: an explicitly invoked Gapline skill, source-grounded read-only investigation of a fixed RepoTend snapshot, a useful *source-supported* finding, a separately configured fresh-agent reproduction, an observed missing-source refusal, and an unpublished issue proposal. The project-owned reference and receipt tests also passed in GitHub Actions.

This is **not** a certification of a general-purpose secure agent host, universally reproducible performance, complete product correctness, a demonstrated wrong-root write, or the entire Discover → GitHub issue-publication lifecycle. The fresh-agent reproduction shared an operator and model/provider environment; the full host tool boundary was not adversarially validated. The maintainer has chosen to **accept the narrow first-use manual Discover v0.1 qualification with those limits**. An independently administered rerun would be needed to claim stronger independence, not for this scoped first use. Do not imply universal security or broader host qualification.

This review does not itself create a new audit receipt or approve any effect.

## Review method and independence

This is a **fresh desk review** of the committed public source and retained evidence using a GitHub-connected reading interface. It was conducted after PR #5 merged, outside the original pilot and reproduction sessions. No original operator process was reused; no issue/PR publication to RepoTend and no target code execution were performed by this review. The reviewer inspected the primary/reproduction/negative event logs, command and measurement files, source manifest, source-reader implementation and tests, issue proposal, and referenced pinned RepoTend source excerpts. The actual model processes were **not replayed**. There was **no separately administered live-agent host**, no independent security sandbox probe, and no human reviewer signature in the retained material.

Where this document says **SUPPORTED**, it means the described statement is supported **within the retained record and inspected scope**, not independently certified in every possible host environment. The reviewer cannot authenticate the historical operator's identity, its full external model traffic, or omissions from the stored event stream.

## Evidence checked

- **Target and tools:** RepoTend at [full commit \`bfe410e4d61ddb472e335ce35877997a2f32d91f\`](https://github.com/grove/repotend/tree/bfe410e4d61ddb472e335ce35877997a2f32d91f), Gapline at \`bd6a1dea3677482e2d4a305a5bf8084cb3c95e69\`, Intentline guidance at \`25e926f57e69395193fc0ac258f9e6dd2332cb18\`. The source manifest lists SHA-256s and line counts for ten RepoTend files and two skill files; [the retained tests](../checks/test_pilot_reader.py) check event-carried source text against that manifest. The reviewer independently spot-checked **relevant pinned source lines** via GitHub, not every captured source byte against Git objects.
- **Host:** Both positive runs and the negative used macOS / Codex CLI \`0.163.0\`, explicit installed-skill guidance and a narrow MCP reader over an operator-prepared source bundle. The saved command arguments select \`--sandbox read-only\`, \`approval_policy="never"\`, disabled shell/apps/browser/image interfaces, and a configured source-reader server. Model-provider connectivity remained necessary. Shell/egress options and a tool's \`readOnlyHint\` are **configuration/intent**, not conclusive proof that no other host interface was accessible.
- **Observed agent event types:** Each positive run has 11 completed \`read_source\` tool calls (the Gapline skill followed by all ten allowed RepoTend source files). The negative run has two source calls: the skill and a **failed** read of \`docs/REMEDIATION.md\`. Each recorded stream ends in \`turn.completed\`. The retained event stream shows no project build, test, file-write or tracker call, but does **not** provide a full trace of the host's orchestration wrapper, other advertised tools, OS denials or provider-side activity.
- **Actual usage:** [pilot measurement](../examples/repotend-pilot/receipts/pilot/measurement.json) records 48.390 seconds, 99,099 input / 75,008 cached input / 1,751 output tokens; [fresh-agent reproduction](../examples/repotend-pilot/receipts/reproduction/measurement.json) records 64.791 seconds, 101,419 input / 70,784 cached / 1,766 output; [negative case](../examples/repotend-pilot/receipts/negative/measurement.json) records 41.852 seconds, 61,717 input / 44,288 cached / 610 output. Cached counts are included in input totals. Exact model identity, billable cost, total operator/preflight effort and full task expense were **UNAVAILABLE**. The earlier failed launch is retained separately rather than hidden.

## Issue #4 acceptance assessment

**Historical assessment:** The pending/owner-decision labels in this table record
the review before the [final scoped acceptance](#final-decision-record--accepted).
They remain evidence of that review stage, not current outstanding approval gates.

The original issue's eight criteria were not mechanically checked off in its body; PR #5 closed it. This table assesses the **underlying requirements**, not issue-label history.

| Criterion | Verdict | Supporting observations | Limits or next decision |
| --- | --- | --- | --- |
| **R1 — Qualified setup and actual invocation** | **SUPPORTED (explicit use)** | Pinned source and skill identities, Codex \`0.163.0\`, run commands, fresh installed-skill paths, first call to \`skill:gapline-audit\`, and reports following Scout → Probe → Report are retained. | Demonstrates explicitly directed use, **not** uncued auto-discovery, complete installed-host provenance, or actual model identity. |
| **R2 — Bounded, read-only pilot** | **PARTIAL** | Read-only command settings; \`read_snapshot.py\` exposes a key-only \`read_source\` interface and no project execution function; 11 source-only calls per positive event log; no reported project runs or tracker writes. | Host exposed additional interface metadata. \`functions.exec\` wrapper activity and OS/provider enforcement are incompletely visible; no complete adversarial sandbox proof. |
| **R3 — Evidence-calibrated report** | **SUPPORTED** | [Primary report](../examples/repotend-pilot/receipts/pilot/report.md) and [reproduction](../examples/repotend-pilot/receipts/reproduction/report.md) present one **SUPPORTED** static finding, alternative explanations/counterevidence, other leads withdrawn, and a falsifying **PROPOSED — NOT RUN** check. | No wrong-root runtime failure was demonstrated; full transitive preview behavior was not assessed. |
| **R4 — Original-source and duplicate triage** | **SUPPORTED (bounded)** | The agent/coordinator distinguished documented same-root/approval promises, selected implementation, existing tests and explicit filesystem exceptions. A saved all-states issue inventory covered the returned RepoTend issues; closed #7 was not an obvious duplicate. | Current-main fixes, PRs, discussions, hidden/deleted items and later changes were excluded. No absolute duplicate-free assertion. |
| **R5 — Provisional issue handoff** | **SUPPORTED (drafting only)** | [Issue proposal](../examples/repotend-pilot/issue-proposal.md) is clearly **NOT PUBLISHED**, source-grounded, contains **Confirm before fixing** and **PROPOSED — NOT RUN** checks, and retains meaningful exceptions. No RepoTend issue write or Intentline saved agreement occurred. | Operator used the \`intentline-issue\` guidance; a separate live Intentline skill activation was **not** independently qualified. |
| **R6 — Independent reproduction** | **PARTIAL** | Fresh process/thread and separate work/bundle/MCP configuration received no earlier report; [reproduction report](../examples/repotend-pilot/receipts/reproduction/report.md) reached the same bounded finding. | Same coordinating operator, provider, machine/runtime and source preparation; not a second human, provider or independently administered host. |
| **R7 — Witnessed unavailable-source control** | **SUPPORTED (narrow)** | The source bundle withheld all target files; the reader rejected \`docs/REMEDIATION.md\` and the model's [actual negative report](../examples/repotend-pilot/receipts/negative/report.md) returned **UNQUALIFIED / UNAVAILABLE**, zero invented findings and **NOT ASSESSED** target behavior. | Demonstrates *missing source* refusal, not enforcement against arbitrary filesystem/network/tool misuse. |
| **R8 — Honest qualification and retention** | **PARTIAL / owner decision required** | Actual reports, events, recorded source identities, separate failed launch, measurements, duplicate inventory, and limitations were committed; README says pending. | Exact billed cost, full host activity and separate maintainer acceptance remain unavailable. Human sign-off is an external decision, not a model inference. |

## Independent source-claim spot checks

The most consequential source-level observation survives independent inspection of the **pinned** RepoTend files:

1. [\`docs/REMEDIATION.md\` lines 29–39](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/docs/REMEDIATION.md#L29-L39) and [\`skills/repotend/SKILL.md\` lines 37–44](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/SKILL.md#L37-L44) require an explicitly approved plan and preserving the selected \`--root\` at apply time.
2. [\`remediation.ts\` lines 181–184](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediation.ts#L181-L184) generate a suggested Markdown apply command **without** \`--root\`; [\`remediate-cli.ts\` lines 5–16](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediate-cli.ts#L5-L16) default the repository root to the current directory.
3. [\`remediation.ts\` lines 53–55](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediation.ts#L53-L55) hash the proposal's rule/path/content, not the repository root; a content-identical plan could pass the same digest on another root, subject to the usual destination checks. [The selected CLI test](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/test/remediation.test.mjs#L126-L143) always supplies \`--root\`, so it does not demonstrate the wrong-root behavior.
4. Counterevidence matters: the *documented manual command* and *agent skill* correctly pass \`--root\`; a mismatched plan is rejected and exclusive file creation protects existing destinations. [The documented exceptions](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/docs/REMEDIATION.md#L45-L53) explicitly exclude transactional all-or-nothing semantics and malicious concurrent path-component races.
5. [\`engine.ts\` imports \`workflows.ts\`](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/engine.ts#L1-L5), which was absent from the permitted audit bundle. Therefore complete transitive preview behavior was **NOT ASSESSED**. This gap must not be translated into a demonstrated defect.

This is **source-support validation**, not a reproduced runtime incident or full code review of RepoTend.

## CI evidence

[The merged PR #5 reference CI run](https://github.com/grove/foundryline/actions/runs/39078341692) completed successfully with **10 Python standard-library tests** on Python 3.12.3. They check Foundryline's authored fixture/reference relationships and the retained source-reader/receipt consistency; they do not run Gapline or RepoTend, establish independent agent efficacy, or certify host isolation. This review relies on the actual published CI receipt, not on a freshly executed local test run.

The present review PR should run the same project-owned checks in CI. A passing run there adds document/fixture integrity evidence, **not** a replacement for the actual pilot.

## Release options for the maintainer

### Accepted: a narrowly scoped manual Discover v0.1

An accurate release statement would be:

> Foundryline's **manual Discover reference** has been exercised on macOS with Codex CLI 0.163.0 using a pinned, operator-prepared read-only source bundle. It produced one supported source-level issue proposal, a fresh-agent same-host reproduction, and a witnessed missing-source refusal. The approach has **not** been qualified for general host isolation, autonomous issue publication, schedules, automatic skill discovery, or end-to-end coding and delivery.

The maintainer **accepted this limited manual reference claim** on 2026-10-18. This approval does not qualify additional execution environments or adopters; those need their own supporting evidence.

### If stronger independence or isolation is a requirement: remain pending

Request only the evidence that changes the decision:

1. A second **human maintainer** or independently administered agent environment follows the documented runbook and challenges evidence/host boundaries, recording deviations and actual costs. Merely changing the MCP server name or running a new thread on the same operator host is not that stronger independence.
2. A narrow host-native negative probe establishes that disabled/extraneous agent capabilities cannot perform unintended effects, or the README explicitly limits its claim to the observed source-reader calls and visible no-write configuration. Do not claim unqualified universal safety.

The omission of \`workflows.ts\` is a legitimate explicit *investigation scope* limit; it only blocks a claim about the entire RepoTend preview call graph, **not** the narrower finding about the generated command.

## Final decision record — accepted

- **Decision:** **ACCEPT SCOPED V0.1** on 2026-10-18, as expressly approved by the maintainer in the project discussion and recorded in [Foundryline issue #6](https://github.com/grove/foundryline/issues/6). This is an operator-reported approval in the connected project workflow, **not** independent cryptographic authentication of a person's identity.
- **Accepted capability:** A manual, reproducible **Discover reference pattern** using the recorded macOS/Codex CLI 0.163.0 setup, pinned operator-prepared public source bundle, explicit Gapline invocation, evidence-calibrated findings, source-grounded **NOT PUBLISHED** issue proposal, fresh-agent same-host reproduction, and a source-unavailable refusal.
- **Explicit limits accepted:** Reproduction shared operator, runtime and provider; exact model identity and billable cost were unavailable; additional host interfaces and transitive source behavior were not fully inspected. Source-level finding did **not** demonstrate a runtime wrong-root write. No full host isolation certification.
- **Outside v0.1 qualification:** Automatic issue creation, schedules, coding/repair, PR merging, deployment, independent cross-host or cross-provider replication, and Proofline/Deliver or RepoTend/Maintain pattern qualification.
- **Additional evidence required for this narrow decision:** None. Broader claims require new tests and authority.
- **Approval to document release readiness:** The user authorized recording this acceptance and preparing project-status updates. **No publication of a Git tag, public GitHub Release, RepoTend issue, repair, or deployment is implied.** See the [prepared release notes](releases/v0.1.0.md).

Issue #4's original evidence classifications remain unchanged. A release decision cannot retroactively strengthen sandbox controls or convert proposed checks into executed proof.

## Publication record — after acceptance

On 2026-10-18, following the separately recorded maintainer acceptance, [Foundryline v0.1.0](https://github.com/grove/foundryline/releases/tag/v0.1.0) was **published** with a Git tag pointing to commit `085ed37739b1eaed7933205a99c0ba220a1e13b6`. The [one-time release workflow](https://github.com/grove/foundryline/actions/runs/39110116925) succeeded and the public release/tag were independently read back via GitHub. Publication is a separate effect and does not expand any underlying host/sandbox, reproduction, or product correctness claim. The one-time write-enabled publisher was removed from active workflows after success.
