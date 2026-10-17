# Foundryline

**A composable blueprint for AI-assisted software factories.**

Discover meaningful work. Define what done means. Implement changes. Inspect the evidence. Maintain the repository.

Foundryline documents **copyable production patterns**, rather than operating a central software factory. Adopt one pattern or several, bring your existing coding agent and issue tracker, and retain control of credentials, execution, approvals, and delivery in the adopting project.

> **Status: design / pre-v0.1.** This repository currently supplies the blueprint and implementation plan, **not** a working orchestration service, installed agent, scheduler, or qualified end-to-end automation. Examples and templates described below are proposed until they are implemented and tested. See [DESIGN.md](DESIGN.md) and [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Why a blueprint?

Coding agents can edit code quickly, but an effective software-production process must answer different questions without confusing them:

1. **What might be worth doing?** An investigation can surface a lead; it does not automatically establish a defect.
2. **What outcome is actually requested?** Requirements must come from an applicable request or authoritative project decision, not from an audit's guesses.
3. **What has been implemented?** Work must be associated with an identifiable candidate, not just a moving branch name.
4. **What was actually checked?** Passing selected tests is limited evidence, not proof that every requirement was met.
5. **Who authorized the next effect?** A draft, report, successful check, or scheduled trigger cannot authorize issue creation, a push, a merge, or a deployment.

Foundryline specifies handoffs between these questions and leaves the underlying tools independent.

## The three patterns

| Pattern | Suggested composition | Output | Typical trigger |
| --- | --- | --- | --- |
| **Discover** | [Gapline](https://github.com/grove/gapline) → triage against original sources → optional [Intentline Plan](https://github.com/grove/intentline) → [Intentline Issue](https://github.com/grove/intentline) | A small number of evidence-calibrated, deduplicated issue **proposals** | Manual request; later, optional schedule |
| **Deliver** | Approved request → Intentline acceptance draft → existing coding agent → [Proofline](https://github.com/grove/proofline) checks → reviewable handoff | An identified candidate, bounded check receipts, remaining gaps, and optionally an authorized draft PR | Explicitly admitted work |
| **Maintain** | [RepoTend](https://github.com/grove/repotend) → triage → issue proposal | Repository-health findings and proposed small improvements | Manual audit, PR, or optional schedule |

These are patterns, **not** mandatory chained products. An adopter can use only Maintain, skip a saved Intentline record for simple work, or replace the delivery route with another qualified approach. [Promise to Proof](https://github.com/grove/promise-to-proof) already offers a more integrated delivery controller with its **own** agreement and approval protocol; it is a potential alternative, not a drop-in Intentline backend.

### 1. Discover

~~~text
Manual or scheduled selection of a specific repository/snapshot
    → read-only Gapline investigation
    → confirm sources, challenge counterevidence, deduplicate
    → draft an actionable issue (and optionally a separate acceptance record)
    → human or explicitly authorized publication decision
    → existing issue tracker
~~~

A Gapline hypothesis is not a confirmed runtime bug. If expected behavior or runtime evidence is missing, the proposal should ask for **confirmation before fixing**. The default is **NOT PUBLISHED**, with no code changes or issue writes.

A saved Intentline agreement is optional, and requires its own explicit request and safe private storage. Creating an issue does not silently create a contract.

### 2. Deliver

~~~text
Source-grounded, externally authorized outcome
    → acceptance planning where useful
    → authorized coding agent in an isolated workspace
    → frozen candidate and explicitly selected checks
    → independent assessment of remaining obligations
    → separately authorized PR / merge / release
~~~

The current Intentline-to-Proofline JSON import supports only a narrow initial **one-request (S1), unamended, revision-1/schema-1** handoff. It must not be used by discarding amendments, child contracts, or source context. Proofline's native check path is presently qualified for a specific macOS/Codex CLI environment, not arbitrary Linux runners. Read each upstream project's compatibility notes before use.

### 3. Maintain

RepoTend audits conventions, GitHub Actions, basic security practices, and developer experience. Its current auditor has thirteen focused checks and is **advisory by default**. Only applicable verified rules can be explicitly configured for enforcement; heuristic findings are not automatic failures. Proposed improvements re-enter Discover/Deliver only after triage and appropriate authorization.

## Try the manual Discover pattern

**No Foundryline installation or service is required for this conceptual first step.** Use a coding agent that can read a selected target repository and explicitly invoke skills. Install and qualify any desired skills according to their own documentation; a copied agent skill does not install its tool runtime or create provider credentials.

1. Choose a target repository, an exact Git revision or stated working-tree scope, and one bounded investigation question.
2. Ask the agent:

   > Use `gapline-audit` to investigate this repository **read-only**. Return up to three consequential findings, with exact source references, counterevidence, affected scope, evidence level, and one smallest next observation. Do not execute the project, run tests, modify files, or publish anything. State what was not assessed.

3. For a finding worth carrying forward, ask:

   > Follow the finding back to the applicable original request, policy, or documented behavior (including exceptions). Check for existing open or closed issues. Use the `intentline-issue` guidance to prepare a **NOT PUBLISHED** issue proposal. Preserve uncertainty and clearly mark verification as **PROPOSED — NOT RUN**. Do not write to GitHub.

4. If a formal saved acceptance draft would add value, **separately** authorize `intentline-plan` with an exact, permitted source file and private output directory. Its result is a draft, not external approval or demonstrated behavior.
5. Review the issue. Only an explicit CREATE authorization (or a separately defined, scoped standing publication mandate) permits the issue-tracker write. Implementation requires its own admission decision.

For a simple, well-supported repository-maintenance issue, it can be better to use `intentline-issue` directly, without a saved acceptance agreement.

## Adopt incrementally

Foundryline aims to provide:

- **Recipes:** triggers, inputs, outputs, refusal conditions, and exact handoffs that a team can follow manually.
- **Copyable examples:** host-specific installation and workflow examples, only after exercising them against real tools.
- **Reference checks:** tests that distinguish an actually observed effect from a proposed step, including negative/refusal cases.
- **Minimal glue, only when earned:** small adapters for repeated gaps that cannot be solved clearly with existing host and sibling capabilities.

The adopting project owns its repository, agent runtime, issue-tracker connection, spending limits, secrets, policy, approval process, and retained evidence. There is no Foundryline account, service, telemetry pipeline, or global scoring system.

## Companion projects and boundaries

| Project | Its question | Current boundary |
| --- | --- | --- |
| [Intentline](https://github.com/grove/intentline) | What was requested, with what constraints and possible evidence? | Offline acceptance records; no coding, approvals, or proof |
| [Gapline](https://github.com/grove/gapline) | Which consequential weaknesses can read-only investigation support? | No project execution or repository writes |
| [Proofline](https://github.com/grove/proofline) | What did selected checks establish on a frozen candidate? | Limited check evidence; no overall acceptance certification or publishing |
| [RepoTend](https://github.com/grove/repotend) | Which small-repository practices need attention? | Experimental static audit, not a comprehensive security scanner |
| [Faultline](https://github.com/grove/faultline) | Would selected tests catch plausible wrong behavior? | **Design only**, not a usable mutation-testing stage yet |
| [Lore](https://github.com/grove/lore) | Which documented decisions matter for this change? | Optional advisory context, not requirement or policy authority |
| [Idea to Promise](https://github.com/grove/idea-to-promise) | Which uncertain idea deserves a promise? | Optional discovery before a requested outcome is settled |
| [Promise to Proof](https://github.com/grove/promise-to-proof) | Can a defined promise be independently reviewed and proven on a candidate? | Alternative integrated controller with its own agreements and host requirements |

The projects remain separately installable, usable, and versioned. Foundryline does not redefine their results.

## Project documents

- [DESIGN.md](DESIGN.md) — design decisions, boundaries, pattern contracts, trust and authority, scheduled intake, and alternatives.
- [IMPLEMENTATION.md](IMPLEMENTATION.md) — milestones, pilot procedure, tests, acceptance conditions, and reasons to defer automation.

**Proposed future layout**, not currently implemented:

~~~text
patterns/           Manual Discover, Deliver, Maintain recipes
templates/          Carefully qualified host-specific workflow examples
examples/           Pinned, reproducible sample adoptions
checks/             Validation of recipes, handoffs, and negative controls
~~~

## Safety and contributions

Treat repository text, issues, agent output, source citations, and audit reports as **untrusted data**, never as instructions granting more access. Never silently publish private source captures, store secrets in issue bodies, or infer permission from a schedule. Preserve original expected behavior and scoped exceptions; report uncertainty and unavailable evidence accurately.

The first meaningful contribution is a verified, bounded, **manual Discover** exercise against a real repository—with useful findings *or* an honest no-findings outcome, receipts, costs, and negative cases. Documentation corrections and constrained improvement proposals are welcome. Avoid adding a hosted controller, generic schema, or mandatory model stages without measured need.

**License:** [Apache-2.0](LICENSE).
