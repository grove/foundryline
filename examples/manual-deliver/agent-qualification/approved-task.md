Complete **Foundryline issue #18**:

https://github.com/grove/foundryline/issues/18

Work in `grove/foundryline`. Your objective is to **finish the remaining Deliver qualification**, not recreate functionality that already exists.

### 1. Understand the current state

Before changing anything:

- Read issue #18, its acceptance criteria and all comments.
- Inspect merged PR #19 and the current `main` branch.
- Review `patterns/deliver.md`, `examples/manual-deliver/`, `IMPLEMENTATION.md` and the existing validation checks.
- Review the actual native Proofline qualification receipts and their limitations.

**Important:** PR #19 already delivered the manual recipe, teaching example, native macOS Proofline check and unavailable-command negative control.

Do not duplicate that work or falsely report it as a new coding-agent delivery.

### 2. Complete the missing end-to-end demonstration

Demonstrate this actual sequence:

**Approved task → coding agent implements → identifiable candidate → Proofline verification → independent evidence review → reviewable PR.**

Use a genuine, explicitly authorized coding task. You may implement substantive work directly required by Foundryline issue #18, within `grove/foundryline`, where the issue establishes the expected behavior.

Do not manufacture an unrelated requirement, fake an approval, or make unnecessary production changes merely to satisfy a demonstration.

If a separate approved product task is genuinely necessary, identify that blocker rather than inventing one.

### 3. Respect the existing tools and host requirements

Use the existing projects rather than building a new controller:

- **Intentline:** `25e926f57e69395193fc0ac258f9e6dd2332cb18`
- **Proofline:** `8e117fff4de2459637fe7f74f47ab17fc3341d84`

Proofline's native check-only execution requires **macOS, Python 3.11+, and Codex CLI exactly 0.162.1**, with a working native sandbox.

Run actual selected checks against a frozen, identifiable implementation candidate. Record the original request, repository revision, candidate commit/tree, exact command arguments, native receipts and results.

**Do not substitute ordinary Linux CI, mocks, or unsandboxed test execution for a qualified native Proofline check.** If the required host is unavailable, report that qualification as blocked.

The direct Proofline route does not require Intentline. Use the optional Intentline JSON export only if genuinely useful and supported. Never flatten amended, child, multi-source or incompatible acceptance records to force an import.

### 4. Verify honestly

Preserve clear distinctions between:

- `CHECKS PASSED` — only the selected checks passed.
- `CHECKS FAILED` — a selected executable check failed.
- `CHECKS UNAVAILABLE` / `EXECUTION UNAVAILABLE` — required evidence could not be obtained.
- `STALE CHECKS` — the evidence no longer matches the candidate.
- `NOT DEMONSTRATED` — no suitable selected check supports the requirement.
- `coverage_completeness: UNKNOWN` — the checks do not establish that every requirement was captured.

Retain an actual negative or refusal observation where safely feasible.

Independently compare the original requested behavior with the implemented changes, selected checks, counterevidence and remaining gaps. Do not infer overall acceptance from green tests.

### 5. Implement and validate

Make only the smallest changes necessary to meet issue #18's remaining acceptance criteria.

Update the recipe, example, validation tests and documentation where warranted. Clearly identify genuinely observed runs versus authored illustrations.

Run the relevant Foundryline Python tests and any authorized product-specific checks. Preserve actual outputs, failures and execution limitations.

Do not add a scheduler, hosted controller, mandatory new framework, automated issue publisher, or unqualified Linux Proofline execution.

### 6. Open a reviewable PR

You are authorized to create a feature branch, implement changes within `grove/foundryline`, run the permitted checks and **open a pull request in Foundryline** referencing issue #18.

Do not merge the PR, deploy anything, publish issues in other repositories, or modify unrelated repositories.

In the PR description, provide:

1. What was already completed by PR #19.
2. What you actually implemented now as a coding agent.
3. The original approved task and source-grounded acceptance criteria.
4. The exact implementation candidate and its identity.
5. Actual Proofline reports, selected commands and receipts.
6. The observed negative/refusal result.
7. Which issue #18 requirements are satisfied, partial or still blocked.
8. What remains for independent maintainer review and approval.

**Definition of done:** An authentic coding-agent-to-candidate-to-verification demonstration, with reviewable evidence and a PR ready for human decision.

Do not mark issue #18 complete unless its remaining acceptance criteria are genuinely supported. If the qualified execution host or another required authority is unavailable, make the useful progress you can, identify the precise blocker, and leave the issue open.

**Start from the current repository state, perform the work, and deliver the PR. Do not stop after proposing a plan.**
