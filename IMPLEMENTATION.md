# Foundryline — Implementation Plan

**Status:** Manual Discover **v0.1 accepted with the tested macOS/Codex host scope** (maintainer decision recorded in [issue #6](https://github.com/grove/foundryline/issues/6) on 2026-10-18). Reference checks/CI and pilot receipts exist; no hosted controller, scheduler, autonomous issue publisher, or broad host-isolation certification is implied. The [v0.1.0 release](https://github.com/grove/foundryline/releases/tag/v0.1.0) was published separately on 2026-10-18.  
**Decision date:** 2026-10-18.  
**See:** [README](README.md) · [Design](DESIGN.md).

**Implementation progress:** The [manual Discover recipe](patterns/discover.md), [authored examples](examples/manual-discover/README.md), blank [run-record template](examples/manual-discover/run-record-template.md), and [reference structural tests](checks/test_manual_discover.py) are provided as reviewable artifacts. An [actual pinned RepoTend pilot record](examples/repotend-pilot/README.md) now retains a live read-only audit, fresh-agent reproduction, witnessed source-unavailable refusal, unpublished proposal and usage. The [Discover v0.1 evidence review](docs/discover-v0.1-qualification-review.md) recommended narrow host-specific acceptance; the maintainer **accepted that limited scope on 2026-10-18**. Host-visibility limits, shared-operator reproduction and unknown cost/model identity remain disclosed. The [v0.1.0 release notes](docs/releases/v0.1.0.md) describe the supported manual blueprint; the [public GitHub Release](https://github.com/grove/foundryline/releases/tag/v0.1.0) is published at the accepted commit `085ed37739b1eaed7933205a99c0ba220a1e13b6`.

## 0. Objective and development approach

Prove that Foundryline is a **copyable blueprint for composing existing software-development tools**, not a new controller or hosted service. Start with one real manual **Discover** journey; only then introduce qualified copyable material and optional scheduled inspection. The output must be useful even when the result is **no supported findings**.

We will not create a custom scheduler, replace native sibling records, generate a shared contract format, install an LLM backend, or publish issues automatically to demonstrate v0.1.

### Current starting state

The initial repository contained only the Apache-2.0 license. These three documentation files propose the shape of future work. In particular:

- `gapline-audit` is an existing read-only agent skill; it does not execute code or write files.
- `intentline-issue` can REVIEW, CREATE, or UPDATE via an appropriately permissioned host tracker tool; issue CREATE/UPDATE alone is **not** permission to save a separate Intentline record.
- `intentline-plan` saves a source-bound draft only when explicitly requested with the separate Python 3.11+ Intentline runtime available.
- RepoTend has a deterministic auditor and 13 advisory-first rules; it is not a full static security scanner.
- Faultline is design-only; Proofline's check-only execution and Intentline export consumer have specific host, candidate, and revision restrictions.

Do not claim any of those tools was invoked by Foundryline merely because its instructions are present in a repository.

## 1. Milestone A — Manual Discover reference (first usable deliverable)

**Goal:** Let a maintainer follow one small recipe without a Foundryline runtime, scheduler, or tracker-write requirement.

**Deliverables, once implemented:**

1. `patterns/discover.md`: prerequisites, precise target/ref/scope, allowed read-only host actions, capped budget, Gapline call, evidence qualification, source lookup, counterevidence, duplicate checks, provisional issue construction, and handoff states.
2. `examples/manual-discover/`: an authored example with original source references, plausible counterevidence, a **NOT PUBLISHED** issue, and explicit **PROPOSED — NOT RUN** verification, identified as a fixture rather than a real audit.
3. A manual adopter runbook covering how to install the portable skills, confirm actual skill activation, distinguish skill installation from Python runtime setup, and proceed if access or original behavioral sources are missing.
4. A small `checks/` package that validates the repository's own reference links and stated sample artifact structure without declaring behavioral agent efficacy.

**First exercise:** Select a bounded public repository snapshot, record its Git commit and inspected paths, run Gapline read-only through a real authorized agent host, follow a consequential supported finding (if any) to original expectations, and draft an issue using intentline-issue REVIEW guidance. Compare the draft against a plain-agent issue-writing baseline when feasible. If no issue is substantiated, retain a valid no-findings report rather than inventing one.

**Acceptance:**

- A second maintainer can reproduce the manual procedure without Foundryline code.
- The actual host, skill activation, snapshot, files inspected, limitations, costs and time are recorded.
- No test/build/project execution or file/tracker writes occur during the Gapline audit.
- A hypothetical runtime bug is labeled **confirm before fixing**; original sources and exceptions are correctly qualified.
- Existing open and closed issues are checked where accessible; uncertain duplicate lookup produces a warning, not a new issue.
- No resulting issue is claimed published; no approval, check receipt, or contract ID is fabricated.
- A no-findings or not-assessed result remains usable and accurate.

**Stop / revise if:** a proposed issue requires invented product requirements, the agent cannot demonstrate read-only scope, or the procedure creates more noise than actionable evidence.

## 2. Milestone B — Source-grounded issue and optional saved planning

**Goal:** Show both the lightweight issue-only route and the explicit saved-acceptance route without conflating their effects.

**Deliverables:**

- Expand `patterns/discover.md` with an issue preparation checklist grounded in Intentline's ISSUE_WORKFLOW, including original-source lookup, current issue readback and conflict checks, preservation of unrelated fields, and uncertainty labels.
- `examples/issue-only/`: REVIEW produces a local issue draft; an authorized CREATE action may later write exactly one issue and verify its URL.
- `examples/acceptance-draft/`: separate saved plan from `intentline-plan`, with actual source bytes, output location/hashes when available, exact CLI/runtimes used, and clear DRAFT status. No local record is generated as a side effect of REVIEW/CREATE.
- Publish a source/authority decision table for when to skip formal planning, write an investigation issue, request a product decision, or save a structured draft.

**Acceptance:**

- The issue-only route requires neither the Intentline Python runtime nor a second model.
- The saved-plan route explicitly checks safe private storage and the presence of a compatible Python runtime.
- An issue edit does not silently update a prior saved contract: stale historical identities are acknowledged.
- All published issue identities are read back; failure or uncertainty leads to lookup before retry, avoiding duplicate remote writes.
- An acceptance draft never becomes an assertion of approval or runtime verification.

## 3. Milestone C — Maintain reference using RepoTend

**Goal:** Give repositories a second, deterministic source of work proposals without requiring a coding agent to run the audit.

**Implementation evidence (2026-10-18, pending maintainer review):** The
[manual Maintain recipe](patterns/maintain.md) and
[real pinned Foundryline audit](examples/repo-maintenance/README.md) retain
RepoTend JSON/Markdown outputs, exact commands/environment, source-grounded
triage and an unpublished decision proposal, a missing-target execution error,
and a separate-agent adoption attempt. The actual successful report has PASS
and WARN outcomes; other statuses are explained without synthetic receipts.
This is a manual reference, not a new release or qualification of schedules,
automatic issue creation, remediation, or other platforms.

**Deliverables:**

- `patterns/maintain.md` and a real RepoTend invocation example using its current checkout and Node.js requirements.
- A small pinned fixture/reference repository and an example audit report showing `PASS`, `WARN`, `FAIL`, `UNKNOWN`, and `NOT_APPLICABLE` where naturally supported by real engine behavior.
- A triage recipe that distinguishes confirmed, objective deviations from heuristic workflow/security recommendations.
- Optional issue draft from a real RepoTend finding. No automatic fix, workflow mutation or GitHub settings change.

**Acceptance:**

- Reports are produced by the real RepoTend implementation with its pinned dependencies, not imagined output.
- Advisory defaults do not block a merge; enforcement is represented only where the upstream engine and adopter config actually support it.
- The audit does not execute the target repository's project code.
- A RepoTend issue feeds the same deduplication and authorization handoff as a Gapline-derived proposal.

## 4. Milestone D — Qualified manual trigger and optional scheduled read-only intake

**Qualified narrow first slice — [issue #15](https://github.com/grove/foundryline/issues/15) completed:** The [manual GitHub Actions RepoTend audit](docs/manual-intake.md) has been **actually exercised by a `workflow_dispatch` event** on GitHub-hosted Ubuntu 24.04, [run #39112708357](https://github.com/grove/foundryline/actions/runs/39112708357), after [PR #16](https://github.com/grove/foundryline/pull/16) merged. The real audit returned **5 PASS / 8 advisory WARN, exit 0, no report errors**; an independently observed missing-target control returned **exit 2**, ENOENT, and no output report. The target Git working tree was unchanged before/after and a short-lived raw report artifact was uploaded and inspected. **Qualified scope:** this one button-triggered, deterministic RepoTend audit on the recorded Ubuntu/Node/pinned-tool configuration, not a generally secure sandbox. **Still planned/unqualified:** optional schedules, AI/Gapline agent host qualification on GitHub, issue publication and autonomous repairs.


**Goal:** Provide a **copyable** workflow only after testing it in a real host; do not ship a YAML file that claims automation without installing/calling an agent.

**Deliverables:**

- `templates/github/intake.yml`, initially an example template with `workflow_dispatch`, optionally `schedule`, that explicitly invokes a qualified tool/agent entry point instead of relying on skills being present.
- A runner qualification record for OS, agent CLI/version, skill discovery/activation, credentials scope, network/egress, source checkout, token budget, command restrictions, and effect isolation.
- Bounded output: Markdown or structured artifact summarizing scope, no-findings/findings, evidence grade, existing issue lookup, potential issue drafts and areas unassessed.
- Clear distinction between scheduled read-only proposal mode and a **separately authorized** publish mode.

**Future scheduled/AI-intake trigger prototype (NOT YET IMPLEMENTED; the RepoTend-only manual trigger above is real):**

~~~yaml
on:
  workflow_dispatch:
    inputs:
      scope:
        description: "Bounded audit question or component"
        type: string
        required: false
  schedule:
    - cron: "17 7 * * 1" # UTC, weekly
~~~

This snippet **does not run an agent**. A future example must pin/install a compatible host agent, invoke the real installed skill, supply permitted GitHub read access, retain actual results, and disclose cases where the host lacks the required model/runtime credentials. GitHub schedule timing is not guaranteed to be exact.

**Acceptance:**

- The manual workflow produces real bounded outcomes on a qualified runner and can refuse correctly when prerequisites are missing.
- The scheduled workflow runs only where explicitly enabled and uses read-only repository permissions for discovery.
- Neither mode publishes an issue without a separately configured write path and publication authorization.
- Runner failures, timeouts, zero findings, uncertain skill invocation, and agent failures cannot appear as completed audits.

**Defer automatic publication until:** the manual and scheduled data establish acceptable quality/noise, deduplication works against real existing issues, and explicit standing limits can be safely enforced. Define allowed repos, categories, max issues per period, read-before-write semantics, credential separation and revoke controls before enabling any autonomous issue CREATE.

## 5. Milestone E — Document Deliver (optional for initial release)

**Bounded direct-route implementation and native checks observed; maintainer decision pending in [issue #18](https://github.com/grove/foundryline/issues/18):** PR #19 supplied the [Deliver recipe](patterns/deliver.md), [authored username example](examples/manual-deliver/README.md), its native macOS check and missing-command control. The separate [approved coding-agent follow-up](examples/manual-deliver/agent-qualification/README.md) implements durable raw-receipt retention and validation, freezes the actual implementation, and records a new native Proofline run of all 27 selected repository tests, a missing-command result and a local boundary refusal. The original task, candidate/argv identities, raw reports and independent evidence review are retained for a separately authorized reviewable PR. Native evidence covers the exact implementation commit, not later evidence appendices. That direct-route task skipped Intentline; `coverage_completeness: UNKNOWN`. Keep issue #18 open pending independent maintainer review; passing selected checks is not overall acceptance.


The [issue #21 trace](examples/manual-deliver/intentline-trace/README.md) now
retains a genuine complete initial S1 Intentline draft/export and source/export
identity checks. A real native macOS consumer run now observes R2 initially
NOT DEMONSTRATED, then limited linked-check evidence after selecting its integrity
check; a separate mismatched map is rejected. All seven original obligations
remain present and overall completeness stays UNKNOWN. Evidence belongs to the
frozen implementation, with final evidence/status appendices checked ordinarily.

**External-product qualification proposed, not maintainer-accepted:** The
[Deliver v0.2 evidence review](docs/deliver-v0.2-qualification-review.md)
now preserves the **full original GitHub-hosted macOS Proofline artifact** for
[RepoTend's actual CLI feature](https://github.com/grove/repotend/pull/16).
After [Proofline's narrowly scoped macOS OpenSSL read fix](https://github.com/grove/proofline/pull/60),
the *same frozen candidate and unmodified original Intentline export* had R1
linked passing-check evidence while R2 was **NOT DEMONSTRATED**, then separate
R1/R2 behavior tests both gave **limited linked passing evidence**. A wrong
argv map was refused, and a paired startup check reproduced the old system
read denial without the exact read grant. Native canaries were OBSERVED only
within their checked scope; `coverage_completeness: UNKNOWN`. Historical
blocked outcomes remain genuine. **Foundryline #18/#21 remain open** until
an explicit, independent maintainer acceptance decision. No release or
automatic workflow is authorized by this evidence review.

**Goal:** Document one end-to-end candidate-and-check handoff without rebuilding the existing P2P controller.

**Deliverables:**

- `patterns/deliver.md` with independent admission, source capture, code effects, test execution and publication gates.
- A pinned example showing the narrow, currently supported Intentline JSON export into Proofline `check --intentline-export` with exact matching S1 source and explicit R-to-command mappings when available.
- A refusal example for amended contracts, child slicing, missing native sandbox, stale candidate, unavailable selected commands or missing permission.
- An optional comparison of the modular path against a separately qualified P2P-native delivery, without implying approval or evidence equivalence.

**Acceptance:**

- The example records the actual supported Proofline host and command identities; the live native checker runs only on the qualified host and within its sandbox.
- An unlinked requirement remains **NOT DEMONSTRATED** even if other checks pass; inventory completeness is not overstated.
- The evidence record binds to the exact candidate and selected checks, and indicates when rechecking is required.
- Neither an Intentline record nor Proofline report authorizes a PR, merge, deploy, or a P2P contract conversion.

**Defer:** Linux-native Proofline assertions, universal contract adapter, integration with amended/sliced lineage and automatic controller resume unless upstream support exists and is qualified.

## 6. Proposed repository structure

Introduce directories only as milestones make them real:

~~~text
foundryline/
├── LICENSE
├── README.md
├── DESIGN.md
├── IMPLEMENTATION.md
├── patterns/
│   ├── discover.md            # Milestone A/B
│   ├── maintain.md            # Milestone C
│   └── deliver.md             # Milestone E
├── examples/
│   ├── manual-discover/       # Milestone A
│   ├── issue-only/            # Milestone B
│   ├── acceptance-draft/      # Milestone B
│   └── repo-maintenance/      # Milestone C
├── templates/
│   └── github/intake.yml     # Milestone D (qualified example)
└── checks/                    # Small tests of reference artifacts
~~~

No `src/foundryline` runtime package, queue, database or service is warranted at this stage. When the same handoff becomes repeatedly error-prone across real adopters, write the smallest independent helper and retain a manual path.

## 7. Test strategy and evaluation

### Structural and contract checks

Validate Markdown links, expected example files, documented version constraints, that sample outputs clearly identify **NOT PUBLISHED**, **DRAFT**, **UNKNOWN**, and **PROPOSED — NOT RUN** where applicable, and that every future workflow names a real invocation path rather than only a skill installation. These tests are guardrails for documentation and fixture integrity, **not evidence that agents follow instructions**.

### Real-host negative controls

- Agent cannot access target files: report `NOT ASSESSED`, do not invent findings.
- No authoritative expected behavior: issue remains provisional/investigation-focused rather than a confirmed product requirement.
- Existing issue matches lead: propose deduplication rather than writing a duplicate.
- Conflicting approved exception: preserve the scoped exception and do not introduce an unsanctioned acceptance criterion.
- Missing runtime or tracker tool: produce local guidance, not a fabricated saved contract or issue URL.
- Inaccessible/stale remote issue: do not overwrite; report blocker.
- Model worker exceeds the read-only boundary: fail qualification, report incident, do not call audit success.
- No verified agent activation: report no audit was executed.
- Zero supported findings: report no-findings and inspected/uninspected scope faithfully.
- Proofline unsupported host or stale receipt: **UNAVAILABLE/STALE**, not verified.

### Comparative evaluation

For a small predeclared set of varied repositories/components, compare:

1. Ordinary coding agent asked to suggest meaningful improvement issues.
2. Same host/model given the manual Foundryline Discover pattern.
3. Where meaningful, RepoTend-assisted maintenance issue selection.

Use the same source permissions, time/token limits, and review criteria. Collect independently reviewed actionable findings, false/duplicate proposals, correctness of original-source citations, missing counterevidence, maintainer intervention, elapsed time and model/tool costs. A pattern that finds no more useful issues and adds material overhead should be simplified or omitted. Preserve negative and incomplete results; do not claim effectiveness from scripted examples alone.

## 8. Release definitions and priorities

**v0.1 (accepted, limited scope):** Manual Discover reference and recorded macOS/Codex pilot with same-operator fresh-agent reproduction, witnessed withheld-source refusal, source-grounded unpublished issue proposal, and structural/receipt checks. See the [accepted qualification scope](docs/discover-v0.1-qualification-review.md). No scheduler, automatic issue publication, cross-host qualification or broader isolation certification is implied.

**v0.2 (proposed, manual-only scope pending acceptance):** Three copyable manual patterns (Discover, Maintain, Deliver) with specified host/tool evidence, including the genuinely button-triggered **read-only RepoTend** audit and optional direct/initial-S1 native Deliver check. **Scheduled intake is explicitly DEFERRED and NOT QUALIFIED.** Maintain formal acceptance, the Deliver review above, and a separate release/tag/publication decision remain prerequisites. No default issue-writing, automatic repair, code publication or merge privileges.

**v0.3 (conditional):** Controlled issue publication when justified, with a scoped standing mandate and robust duplicate handling; optional bounded Deliver reference.

**v0.1.0 is now a published, narrowly scoped release.** Later versions are planning labels, not tagged/published releases or commitments to implement all stages.

## 9. First issue to execute

**Title:** Document and qualify Foundryline's manual Discover pattern.

**Description:** A maintainer needs a repeatable way to investigate one exact repository revision, qualify up to three findings, trace a chosen finding to authoritative behavior, check for existing issues, and prepare an issue draft without running project code or publishing anything.

**Acceptance criteria (proposed):**

- [ ] A documented manual invocation activates the actual Gapline skill on a fixed public repository revision with read-only host permissions.
- [ ] The retained report includes inspected scope, evidence levels, counterevidence, tools/commands actually used, limitations, and actual model/time cost.
- [ ] A supported finding leads to a source-grounded **NOT PUBLISHED** issue proposal with **PROPOSED — NOT RUN** checks; if none is supported, a no-findings record is retained.
- [ ] The guide distinguishes an issue-only draft from a separately authorized saved Intentline agreement.
- [ ] No unapproved repository/test/tracker mutation occurs; missing original behavior or unavailable host capability fails honestly.

**Verification — PROPOSED — NOT RUN:** Inspect the actual host invocation receipt and the exact report/issue output, check against the selected source and existing issue inventory, exercise at least one unavailable-evidence/refusal path, and have a second maintainer follow the runbook.

**Non-goals:** Scheduled deployment, automatic issue creation, new agent controller, coding implementation or runtime proof.
