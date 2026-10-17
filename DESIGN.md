# Foundryline — Design

**Status:** Proposed blueprint, pre-v0.1.  
**Decision date:** 2026-10-18.  
**Companion documents:** [README](README.md) · [Implementation plan](IMPLEMENTATION.md).

## 1. Product decision

**Foundryline is a reusable, local-first software-factory blueprint, not an orchestrator product or shared hosted service.** Its primary deliverable is a small, reproducible collection of patterns, host-specific examples, and honest verification exercises connecting existing independent tools.

A project can copy a single recipe, run it manually, or schedule it with the execution facilities it already trusts. The adopter—not Foundryline—owns agent configuration, credentials, approval, repository state, issue tracker, sandboxing, and delivery effects.

### Principles

1. **Compose instead of subsume.** Preserve Intentline, Gapline, Proofline, RepoTend, and optional peers as autonomous projects with their native interfaces and authority boundaries.
2. **Manual-first, then automate what worked.** Demonstrate an end-to-end human-operated recipe before adding schedules or standing permissions.
3. **Sources before assertions.** Findings are leads; acceptance obligations require the applicable original outcome/policy and exceptions.
4. **Uncertainty stays visible.** A hypothesis does not become a defect because an issue was written; a passing check does not prove the entire contract.
5. **Effects need independent authorization.** Reading, planning, issue writing, code writing, executing checks, publishing, merging, and deploying are distinct grants.
6. **Evidence binds to exact scope.** Identify repository, ref, inspected paths/working tree (and gaps), source captures, candidate, commands, receipts, and report freshness where supported.
7. **Opt in to ceremony.** Skip duplicate planning, expensive agent audits, and unnecessary handoff schemas for routine work.
8. **Portable recipe, qualified execution.** Do not assume that a skill install, GitHub Actions workflow, or generic container confers a verified agent sandbox or host support.

### Goals

- Describe three adoptable workflows: Discover, Deliver, Maintain.
- Make issue intake possible manually and, eventually, on a schedule without turning audit output into unauthorized changes.
- Show a bounded, evidence-grounded handoff from finding to issue proposal and optional acceptance draft.
- Supply one pinned, real-host exemplar and practical negative/refusal cases.
- Make optional tools and unsupported handoffs explicit.
- Prefer adoptable configuration and examples over custom runtime code.

### Non-goals for v0.1

A hosted service, dashboard, cross-repository fleet scheduler, plugin marketplace, central evidence database, universal issue schema, semantic proof of correctness, autonomous deployment, new coding model, custom mutation engine, or proprietary workflow runtime. An automated Linux Proofline execution path, direct Intentline-to-P2P contract bridge, and automatically approved findings are specifically **not** claimed.

## 2. Ownership and system boundary

~~~text
Adopting project / operator
  ├── scope, original source/policy, priorities, repo identity
  ├── host tools, skills, project runtimes, permissions
  ├── private working records and cost limits
  └── publication / implementation / release decisions
              │
              ▼
     Foundryline reference patterns
       Discover  Deliver  Maintain
              │
       optional native tool calls
              │
       ┌──────┼────────┬─────────┐
       ▼      ▼        ▼         ▼
    Gapline Intentline Proofline RepoTend
       (also optional Lore, Faultline later, ITP/P2P)
              │
              ▼
     native outputs / reviewable handoffs
              │
              ▼
   operator-controlled tracker, Git, CI
~~~

Foundryline **documents** these steps; it does not claim to enforce them. Actual permission and isolation must be enforced by the executing host. Agent instructions are not a security sandbox.

No sibling automatically invokes another. A report or skill instruction is **untrusted input** for the next stage. The factory recipe preserves provenance and disagreements instead of synthesizing an authoritative consensus.

## 3. Pattern contracts

### Discover

**Trigger:** a manual operator request identifying a target and question, or a separately enabled periodic scan of named repositories/components.  
**Input:** permitted repository snapshot, scope/inspection budget, available authoritative behavioral sources, existing issue inventory when accessible, and a publication mandate if one exists.  
**Read-only inquiry:** ask \`gapline-audit\` to Scout → Probe → Report; at most three substantive findings by default; no project code execution, test run, build, file write, or publication. It must expose supporting and counterevidence, sampled limits, and \`DEMONSTRATED\`/\`SUPPORTED\`/\`HYPOTHESIS\`/\`REFUTED\`/\`NOT ASSESSED\` qualification as appropriate.  
**Triage:** follow report pointers to original product requirements, established policy, and accepted exceptions; challenge severity and false leads; search open *and closed* issues; decide whether the next action is observe, specify, fix, defer, or drop. Treat an unverified runtime concern as **confirm before fixing**. A no-findings run is successful if correctly reported.  
**Planning:** use \`intentline-plan\` *optionally*, only when a separately requested saved acceptance agreement adds value and there is a valid original source and private output. A draft does not approve behavior or grant tracker writes.  
**Issue drafting:** use \`intentline-issue\` to REVIEW/create a **NOT PUBLISHED** proposal with plain-language context, evidence, proposed R-ID criteria, \`PROPOSED — NOT RUN\` verification, and open decisions. A simple well-grounded issue may skip formal planning.  
**Publication:** invoke CREATE once, only under a specific operator instruction or a separately configured standing mandate with repository scope and limits; use the agent host's authenticated issue tool. Read back the outcome. A failed/uncertain write means lookup before retry.  
**Output:** no findings, rejected findings, or a bounded set of local drafts / verified issue identities with exact evidence caveats. No coding, PR, or implied approval.

A scheduled trigger **does not** authorize write effects on its own. The initial schedule should create a private/read-only proposal artifact or job summary for review, not issues. If auto-creation is explicitly adopted later, the mandate must define repository destinations, allowed evidence categories, rate caps, duplicate policy, exceptions, spend, and revocation.

### Deliver

**Trigger:** an externally admitted issue/request and separate permitted code effects.  
**Input:** actual source/request, constraints, known original decisions, fixed comparison base, candidate location, selected checks, and independently granted host permissions.  
**Flow:** optional Intentline draft → authorized coding agent → identifiable frozen candidate → explicitly selected Proofline checks on the host qualified by Proofline → review of linked and unlinked obligations → delivery proposal. Publication, merge, and deployment require their own authority.  
**Output:** candidate identity and the exact claims supported by receipts, test gaps, unknown coverage, stale/mismatched evidence, and delivery state.

The existing Intentline-to-Proofline adapter accepts only an initial schema-1, revision-1, **S1-only, unamended** JSON export. Never flatten amendments, slice plans, missing context or prior approvals to force a fit. Imported R rows without exact check links remain **NOT DEMONSTRATED**. Linked passing checks are *limited evidence* and inventory completeness remains **UNKNOWN**. Proofline native check execution is currently qualified for a particular macOS/Codex CLI environment. Not meeting preconditions returns **UNAVAILABLE**, not a weaker substitute described as equivalent verification.

[Promise to Proof](https://github.com/grove/promise-to-proof) can be selected as an alternative integrated delivery process. It has its own agreement format, independent review/proof controller, effect mandates and macOS/Codex requirements. An Intentline adoption assertion is not a P2P approval: no direct agreement/authority conversion is designed here.

### Maintain

**Trigger:** manual RepoTend audit, PR-specific inspection, or a deliberately configured periodic scan.  
**Input:** pinned repository tree, audit version and configuration, rule applicability, read-only authorization.  
**Flow:** run the current RepoTend deterministic auditor without executing target project code, retain the actual \`PASS\`, \`WARN\`, \`FAIL\`, \`UNKNOWN\`, \`NOT_APPLICABLE\` results, and triage useful deviations. Do not treat a heuristic security warning as a verified security failure.  
**Output:** repository-health report and deduplicated proposals that may feed Discover; no automatic changes to GitHub settings or code.

RepoTend's initial 13 rules are narrower than its proposed full release. Enforced failures are opt-in on verified rules. The blueprint must not imply that advisory defaults can block CI.

## 4. Trigger and authority model

| Event/action | Baseline default | Who can authorize |
| --- | --- | --- |
| Manual read-only audit | Permitted with host read access and defined scope | Operator/host permissions |
| Scheduled read-only audit | Off until explicitly enabled | Repository maintainer configuring scheduler and access |
| Draft an issue in agent response/job artifact | Permitted, no remote write | Operator running recipe |
| Save Intentline work records | Separate explicit request and private storage | Operator |
| Create/update issue | Off; only specific create/update or scoped standing mandate | Tracker-authorized actor |
| Execute project code/tests | Off for Gapline; separately authorized for proper stage | Host/operator with qualified execution isolation |
| Implement candidate | Separate work admission and source write | Operator |
| Open PR, merge, deploy | Separate gates; never inherited from reports | Appropriate authorized actor |

A scheduled GitHub Actions trigger (\`schedule\` or \`workflow_dispatch\`) is merely a transport mechanism. Schedule runs may be delayed or skipped. A generic example with \`runs-on: ubuntu-latest\` cannot credibly claim to provide Proofline native checks or run Codex just by installing skill instructions. A qualified workflow must explicitly install tools, provide runner/model auth where needed, limit credentials, pin dependencies/actions, control target scopes, and record actual outcomes.

Do not put private source text, logs, credentials, or unredacted contracts into public issues, PR descriptions, artifacts, or third-party model calls without separate authority. In cross-repository publication, the calling repository's default GitHub token is not presumed to have write rights to the target repository.

## 5. Issue-intake lifecycle and deduplication

Recommended logical states (labels are **not** yet created or required in GitHub):

~~~text
DISCOVERED → TRIAGED → DRAFTED → PUBLISHED → ADMITTED
                ├── REJECTED
                ├── NEEDS_OBSERVATION
                └── DEFERRED
~~~

\`PUBLISHED\` means tracker write was verified. \`ADMITTED\` means a separate delivery decision, not merely label placement. Rescans must compare repository/ref, behavior or rule identity, affected scope, original source and applicable exceptions, and both open and previously closed issues. A reoccurring string-match alone is neither a reliable duplicate nor a reason to reopen. Favor no write when identity or issue inventory is uncertain.

A reusable issue proposal should contain:

- A standalone explanation of expected and suspected behavior, affected workflow, and likely consequence (qualified).
- Pointers to actual inspected files/revisions and **applicable original behavioral sources**, including scoped exceptions.
- Evidence strength, counterevidence, execution status, and areas not assessed.
- Proposed stable acceptance outcomes when supported, clearly separating unapproved inferences.
- The smallest falsifying observation, clearly labeled **PROPOSED — NOT RUN**.
- Material outcome decisions and evidence gaps separately.
- Existing related/duplicate issues and next action.
- No invented hashes, approvals, test receipts, or published links.

## 6. Compatibility and adapter policy

Adapters must preserve the upstream's native JSON/output and meanings. Do not impose a shared normative schema on siblings or make all reports look like test results. A reference example can add a *non-authoritative* manifest with exact upstream tool revisions, paths/hashes, repository commit, invocation context and status. This is a convenience index; it does not authenticate a reviewer or prove semantic validity.

For every handoff: record the producer's actual status; validate only constraints that the consumer itself supports; propagate unknown/stale/refused states; do not silently retry changed inputs; do not use an export, prompt, issue or report to grant actions.

**Optional context:** Lore can provide relevant source-backed documentary decisions, but its advisory interpretations are not project authority. ITP can settle a rough product idea before technical intake; it may return a no-build decision. Faultline is design-only and must not appear as an implemented gate or actual mutation result.

## 7. Alternative designs considered

| Option | Decision | Rationale |
| --- | --- | --- |
| New Python controller + central storage | **Reject for v0.1** | Duplicates responsibility, adds runtime and security complexity before a reference pattern is shown useful |
| Use P2P as mandatory controller | **Reject as universal default** | Mature integrated flow, but different contract/authority semantics and a narrower qualified host |
| Require Intentline saved draft for every finding | **Reject** | Unnecessary state and planning overhead for routine or uncertain work |
| Automatically publish every finding | **Reject** | Amplifies hypotheses, duplicates, noise and authority confusion |
| Support manual and scheduled intake as equivalent from day one | **Defer** | Schedules need actual runner qualification, explicit credentials and measured signal-to-noise |
| Provide copyable examples with tests and explicit limits | **Choose** | Portable, inspectable, low coupling; can be improved by real adoption evidence |

## 8. Evaluation and acceptance

Success is **not** the number of issues produced. Compare Foundryline adoption with ordinary agent use on matched tasks. Track evidence correctness, actionable issue yield, false/duplicate rate, maintainer review time, end-to-end effort and model cost, authorization violations, and unqualified result claims. Preserve no-findings, blocked, unavailable and rejected results instead of hiding them.

A v0.1 design is ready to claim *usable manual Discover guidance* only when an external adopter can follow it with pinned inputs, real skill activation evidence, useful or honestly empty findings, issue draft(s) that distinguish suspected from proven behavior, and no unintended writes. A scheduled path is a separate, later qualification.

**Outlook:** use the smallest automation that genuinely improves this workflow. Keep an implementation backlog in [IMPLEMENTATION.md](IMPLEMENTATION.md); do not present proposed paths, schemas, CI jobs or adapters as shipped software.
