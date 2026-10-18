# Foundryline

**A simple, reusable playbook for building and looking after software with AI.**

Welcome! 👋

AI coding assistants can write code. But good software takes more than writing code. How do you know **what needs fixing**, **what “done” means**, and **whether a change really works**?

That's where **Foundryline** comes in.

Foundryline is a collection of **step-by-step recipes** that help you use existing AI tools together. Think of it like a cookbook for software projects: pick a recipe, follow the steps, and adapt it to your project.

**It's not another app you have to run.** There's no Foundryline server, subscription, or special coding agent. You bring your own repository, coding assistant, and tools. Foundryline shows how they can work together.

## The big idea

A healthy software project has a simple loop:

~~~text
Find something worth improving
              ↓
Explain what should happen
              ↓
Make the change
              ↓
Check what actually works
              ↓
Review and decide what to ship
~~~

Foundryline helps make each step clear and repeatable. It also keeps an important distinction: **“The AI thinks there might be a problem” is not the same as “We've proved there's a bug.”**

You stay in charge of what gets changed, published, or merged.

## Pick a recipe

You don't have to use everything. Start with the part that's useful to you.

| Recipe | In plain English | Where it stands |
| --- | --- | --- |
| **[Discover](patterns/discover.md)** | Ask an AI assistant to look through a project for meaningful problems or missing behavior, then help you draft a clear GitHub issue. | **Scoped v0.1 accepted:** manual guide, worked examples, and a recorded macOS/Codex pilot |
| **[Deliver](patterns/deliver.md)** | Start with an approved task, use your coding agent to make a change, and gather evidence about what was checked. | **Bounded direct and optional S1 routes observed:** native macOS checks, requirement gap/relink and refusal; maintainer decision pending |
| **[Maintain](patterns/maintain.md)** | Check whether your repository has useful basics such as good contribution guidance, sensible CI, and safer workflows. | **Manual reference:** real pinned RepoTend audit, failure control, and separate-agent adoption record; pending maintainer review |

All three are designed to be **copied into other projects**, not tied to this repository or to one AI provider.

## Try your first Discover

Imagine you maintain a small GitHub project. You suspect there are things worth improving, but you don't know where to start.

With Foundryline, you can ask your coding assistant to **look for a few important issues, explain the evidence, and suggest what to do next**. If nothing convincing turns up, that's a perfectly good result too.

### 1. Get your assistant ready

You need a coding assistant that can read the repository you want to inspect and supports agent *skills* (reusable instructions for the assistant). The manual pilot used Codex on macOS; other setups need their own checks.

Install the [Gapline](https://github.com/grove/gapline) skill using the instructions for your assistant. For a compatible Skills CLI setup, you can start with:

~~~sh
npx skills@latest add grove/gapline
~~~

When you're ready to turn a finding into a proposed issue, you can also install the [Intentline](https://github.com/grove/intentline) skills:

~~~sh
npx skills@latest add grove/intentline
~~~

These commands install **agent instructions**, not an AI model or a running Foundryline service. Installing a skill does not mean the assistant has actually used it. For issue drafting alone, you do **not** need the separate Intentline Python program.

### 2. Ask for a careful investigation

Choose a repository and, ideally, a specific Git commit so you can tell exactly which version was inspected. Then ask your assistant:

> Use **gapline-audit** to look through this repository **read-only**. Find up to three meaningful problems or gaps. For each one, show the files that support it, look for reasons it might *not* be a problem, and explain what we would need to check next. Don't run the project, change files, or create issues. It's okay to find nothing.

Your assistant should report **what it looked at, what it found, and what it couldn't check**.

*Important:* “Read-only” must also be enforced by your assistant's actual tool permissions. A prompt alone is not a security boundary.

### 3. Turn a useful finding into an issue draft

If a finding looks worth pursuing, ask:

> Use **intentline-issue** guidance to draft a GitHub issue for this finding. Check what the project originally promised, look for existing issues, and explain how we could verify the concern. Mark it **NOT PUBLISHED**. Don't create the issue or change code.

Review the draft yourself. If the behavior has not actually been reproduced, the issue should say **“Confirm before fixing.”** You decide whether and when to publish it.

That's your first Foundryline workflow! 🎉

For the full procedure—including evidence checks, limits, and cases where the assistant should stop—follow the [manual Discover guide](patterns/discover.md).

## A real example

We tried Discover on [RepoTend](https://github.com/grove/repotend), a tool for keeping GitHub repositories in good shape.

The AI-assisted investigation noticed that a suggested command **left out the repository being worked on**. That *could* lead someone to apply changes in the wrong folder.

A second, separately started agent found the same concern. Another trial deliberately hid necessary source files, and the agent correctly said it **couldn't assess the project** instead of making up an answer.

That gave us a useful [issue proposal](examples/repotend-pilot/issue-proposal.md)—**not a confirmed runtime bug, and not a published RepoTend issue**.

Curious about the details? See the [real pilot record](examples/repotend-pilot/README.md), the [example issue draft](examples/manual-discover/example-issue-proposal.md), or the [qualification review](docs/discover-v0.1-qualification-review.md).

## Try a manual Maintain check

The [Maintain guide](patterns/maintain.md) shows how to run RepoTend against a
specific repository revision, understand its advisory findings, and prepare an
unpublished maintenance proposal. The deterministic audit needs Git, npm and
Node.js 22.16 or newer; it needs no AI model or GitHub token.

Our [real Foundryline example](examples/repo-maintenance/README.md) retained
6 PASSes and 7 warnings, a missing-target error, and a separate-agent adoption
attempt. The [worked proposal](examples/repo-maintenance/issue-proposal.md) asks
whether a contribution guide would help; a warning does not make it mandatory.
Nothing in this recipe applies fixes or publishes issues.

**Want to run that check from GitHub instead of your computer?** Use the [read-only GitHub Actions example](docs/manual-intake.md): open the **Manual RepoTend maintenance audit** workflow, select your branch, and click **Run workflow**. We [verified an actual manual launch](https://github.com/grove/foundryline/actions/runs/39112708357) on GitHub-hosted Ubuntu: **5 PASS, 8 advisory WARN**, plus a correctly handled missing-target failure and a downloadable report. It **does not** schedule itself, publish issues, apply fixes, or certify your entire repository. Other projects must review their own permissions and privacy.

## Try the Deliver example

When you already have an **approved task** and a coding agent has implemented it,
the [manual Deliver recipe](patterns/deliver.md) shows how to check the exact
candidate using Proofline and prepare a reviewable handoff. Intentline planning
is **optional**. The [small username example](examples/manual-deliver/README.md)
has source-linked R1/R2 expectations and runnable Python tests, and illustrates
why one passing selected check does **not** demonstrate an unlinked requirement.

The username example remains **authored**, with PR #19's [native check-only receipt](examples/manual-deliver/native-qualification.md). A separate [approved coding-agent follow-up](examples/manual-deliver/agent-qualification/README.md) now retains those original receipts and validates their identities. Its frozen implementation passed the selected 27-test suite through native Proofline on macOS, with an actual missing-command control and a retained local boundary refusal. This is bounded direct-route evidence for human review.

The [issue #21 trace](examples/manual-deliver/intentline-trace/README.md) adds a
real Intentline initial S1 draft/export from the complete user-authorized task and
separate source/export integrity checks. The real native import first left R2
NOT DEMONSTRATED, then reported limited linked-check evidence after its check
was selected; a mismatched map was rejected. Overall completeness stays unknown.

## The tools behind the recipes

Foundryline doesn't replace these tools. It helps you choose when to use them.

| Tool | What it helps with |
| --- | --- |
| [Gapline](https://github.com/grove/gapline) | Investigate possible problems by reading code and documentation |
| [Intentline](https://github.com/grove/intentline) | Write down what is expected and prepare clear issues or acceptance plans |
| [Proofline](https://github.com/grove/proofline) | Record what selected checks actually showed for a particular version of the code |
| [RepoTend](https://github.com/grove/repotend) | Find repository setup and maintenance improvements |

Other tools can fit too. You can use your preferred coding assistant, and **you don't need every tool** to adopt a recipe.

## What's ready today?

**Foundryline is still an early project.** The manual Discover guide, examples, source-reading helper, and reference tests exist. We also have **one real, recorded Discover pilot** on macOS with a specific Codex CLI version, including a fresh-agent reproduction and a missing-source test. The manual Maintain reference now adds a deterministic RepoTend audit and adoption records, pending maintainer review.

**Manual Discover v0.1 has been accepted for the specific macOS/Codex setup we tested.** This is a modest, evidence-backed milestone—not a claim that every coding-agent setup is safe or that the full software factory is running. See the [scope and maintainer decision](docs/discover-v0.1-qualification-review.md) and [published Foundryline v0.1.0 release](https://github.com/grove/foundryline/releases/tag/v0.1.0).

In particular, Foundryline does **not** currently run scheduled audits, publish GitHub issues automatically, implement code, or merge changes for you. The [manual Deliver follow-up](examples/manual-deliver/agent-qualification/README.md) records an approved coding-agent task and native candidate checks for a human PR decision. It supplies no autonomous publication or merge authority; automated Maintain options remain future work.

We would rather explain what we've actually tested than promise magic.

## Want to help?

You're very welcome here. A great way to contribute is to:

- Try the [Discover guide](patterns/discover.md) in a project you know.
- Try the [manual Maintain guide](patterns/maintain.md) for a local, advisory repository check.
- Tell us which step is confusing or missing.
- Share a useful result **or** an honest no-findings outcome, without publishing private code or secrets.

You can also open an issue with suggestions for a recipe you'd like to see.

## Learn more

- [Design](DESIGN.md) — why Foundryline works this way and how the pieces fit together
- [Implementation plan](IMPLEMENTATION.md) — what's done, what's next, and what's intentionally postponed
- [Discover examples](examples/manual-discover/README.md) — friendly, made-up examples for learning
- [Real pilot and its limits](examples/repotend-pilot/README.md) — what we actually tried
- [Real Maintain audit and adoption](examples/repo-maintenance/README.md) — pinned RepoTend outputs, triage and failure handling
- [v0.1 evidence review](docs/discover-v0.1-qualification-review.md) — what's supported, the accepted scope, and what's not qualified
- [v0.1.0 release](https://github.com/grove/foundryline/releases/tag/v0.1.0) — the published manual Discover blueprint and its scope

**License:** [Apache-2.0](LICENSE).
