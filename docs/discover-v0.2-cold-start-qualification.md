# Discover v0.2 cold-start trial — scoped qualification decision

**Status: MAINTAINER ACCEPTED — QUALIFIED WITH STATED LIMITS (2026-10-20).**  
**Decision source:** [Issue #29](https://github.com/grove/foundryline/issues/29), explicit maintainer approval conveyed to the separate reviewer on 2026-10-20. This document is a public summary of that approval, **not** a claim that the original private logs have been published or an identity-authenticated maintainer signature.  
**Trial:** one bounded, explicitly activated installed-`gapline-audit` Discover run; **not** automatic first-use onboarding or host security certification.  
**Published baseline:** the [v0.2.0 Discover guide](https://github.com/grove/foundryline/blob/v0.2.0/patterns/discover.md) was used for the experiment. The v0.2.0 tag and release remain unchanged.

## Decision

**ACCEPT SCOPED QUALIFICATION** for one actual, fresh-session, native-Gapline **read-only Discover** trial on the recorded macOS / Codex CLI `0.163.0` host and its exact-key MCP source reader. A legitimate **zero-supported-findings** result meets the Discover contract; it is not an assertion that the target is defect-free.

The decision follows a separate evidence review of actual worker messages, native skill traces, reader calls, source integrity proofs, frozen issue/PR search results and permissions. The reviewer recommends **QUALIFIED WITH STATED LIMITS**, and the maintainer accepted **that limited recommendation**. This acceptance does **not** broaden the earlier [Discover v0.1 manual reference decision](discover-v0.1-qualification-review.md).

## Frozen experiment and actual sequence

- **Target:** public [`pallets/markupsafe` at full commit `4e111271b1494995708a9e878a10829b5e10c7ba`](https://github.com/pallets/markupsafe/tree/4e111271b1494995708a9e878a10829b5e10c7ba).
- **Question:** Whether the documented escaping guarantees match the relevant implementation paths for ordinary strings, trusted `Markup`/`__html__` content and Python/C implementations.
- **Inspected source:** `README.md`, `docs/escaping.rst`, `docs/html.rst`, `docs/formatting.rst`, `src/markupsafe/__init__.py`, `src/markupsafe/_native.py`, `src/markupsafe/_speedups.c`, `tests/test_escape.py` and `tests/test_markupsafe.py`.
- **First preflight:** **UNQUALIFIED / UNAVAILABLE**. The available Codex `--sandbox read-only` setting still allowed a benign command (`/usr/bin/true`), so it was not a no-execution boundary. No worker was launched in that attempt; the failed record remains separate.
- **Second attempt:** the operator reused Foundryline's existing [exact-key source reader](../examples/repotend-pilot/host/read_snapshot.py), prepared a source bundle and a frozen tracker inventory, and suppressed worker command/patch and other unnecessary tools. A new Codex worker with native `gapline-audit` activation inspected the nine files and finished in **108.641 seconds**, with **zero supported findings**. No post-launch coaching was observed.
- **Native activation:** host `turn/start` contains a structured skill input for `gapline-audit`; an actual injected skill block appears in the worker's first model input. This is stronger evidence than `skills/list`, pasted instructions or reading the skill file alone. The installed Gapline revision was `bd6a1dea3677482e2d4a305a5bf8084cb3c95e69`.
- **Negative control:** a second fresh worker attempted an unavailable source read, received a real reader `UNAVAILABLE` error and stopped without inventing findings. **Important:** it requested a *prefixed, unknown key*, rather than the correctly named, intentionally withheld `README.md` key. This demonstrates unknown-key denial and appropriate refusal **only**.
- **Measured reads:** 18 primary reader calls, including the nine source files and separately prepared guide/identity/tracker references; the control made one denied reader call and completed in **14.639 seconds**. Exact monetary costs and total operator effort were unavailable.

## Independent review and acceptance mapping

The separate reviewer was **ChatGPT (GPT-6 / OpenAI)**, not either Codex worker, and inspected the supplied evidence in a different environment. The reviewer **shares OpenAI as model provider**, previously advised on the setup, and was **not a second human maintainer or a blind, independently administered test**.

| Issue #29 requirement | Accepted finding | Material boundary |
| --- | --- | --- |
| Native installed Gapline activation in a fresh agent | **SUPPORTED** by structured native skill events and new ephemeral worker sessions | Explicit, operator-selected invocation; **not** automatic skill selection or self-installation |
| Host-enforced read-only source/issue boundary and negative/refusal event | **SUPPORTED WITH MATERIAL LIMIT** by observed restricted tool inventory, exact-key reader and denied control read | Invalid prefixed key, **not** valid-key withholding; no general sandbox, OS or network isolation certification |
| Pinned revision, inspected source, counterevidence, duplicates and 0–3 findings; no publication | **SUPPORTED FOR INSPECTED SCOPE** | Nine source files; 0 supported findings; no project execution or publication observed in worker traces |
| Separate evidence reviewer | **COMPLETED WITH DISCLOSURES** | Different session/host from workers, but same provider and prior advisory involvement |
| Uncoached completion, interventions, blockers and useful guide improvements | **SUPPORTED WITH SCOPE LIMIT** | No post-launch coaching observed; extensive operator setup and earlier failed preflight; cost UNKNOWN |

The reviewer recalculated **787/787** packaged-file hashes against the supplied review manifest, independently validated the pinned Git object chain for the nine files and matched **9/9** actual source reader replies to those blobs. Hashes establish consistency with the supplied evidence, **not** proof that private original host logs were unmodified before packaging.

The primary considered and withdrew a `Markup.format` / `__html__` return-type lead after checking formatter code and its documented behavior. This supports **NO_FINDINGS** for the bounded scope and question; it is **not** a runtime demonstration or a complete security assessment.

The operator's frozen GitHub searches covered **open and closed issues and PRs** (532 returned records across eight pages), which the worker accessed through the reader. This was **not live worker-side tracker access**. It did not cover every comment, review discussion, PR diff, inaccessible/deleted item or subsequent tracker change. **Issue proposals: zero — NOT PUBLISHED**. Checks or reproductions proposed in the report remain **PROPOSED — NOT RUN**. No MarkupSafe project tests, builds or examples were executed during the audit.

## Accepted boundaries — not additional qualifications

1. **Native activation is not automatic adoption.** The operator supplied the installed skill, selected it explicitly, pinned the target, prepared the reader/inventory and set initial instructions. Only the worker's *post-launch* completion was uncoached.
2. **Read-only sandbox is not no-execution.** The first preflight demonstrated that distinction. The accepted attempt relies on the separately observed restricted worker tool inventory and bounded reader, not a universal shell or network containment claim.
3. **The negative control is an unknown-key refusal**, not a verified refusal for a valid key removed from the allowlist. A correctly named withheld-source control would strengthen this one subclaim but is **not required for the narrow decision** taken under the wording of issue #29.
4. **The independent review is separate but not blind or cross-provider.** No second-human, independent host administration or certified provider-side/OS audit occurred.
5. **Private evidence remains private.** Original event streams, redacted ZIP copies, machine details and tracker bodies are retained under operator control outside this public repository. No raw event logs, private file paths, archived bundle or third-party issue dumps are included here. The public summary is intentionally insufficient to independently replay or authenticate private originals.
6. **Previous evidence remains in its original state.** Attempt 01 stays **UNQUALIFIED / UNAVAILABLE**; this decision applies to successful attempt 02 only. The published `v0.2.0` artifact, external target and earlier qualification decisions are unchanged.

## Practical guidance from the failed preflight and accepted attempt

For the next adopter trial:

- Verify the **actual runtime-exposed tool inventory**, not only `--sandbox read-only` and desired configuration. Explicitly disable or omit project command and mutation tools for read-only Discover.
- Retain **native structured skill activation** from the host separately from skill discovery, manual `SKILL.md` reads and conversational mentions.
- For a stronger refusal case, withhold an **otherwise valid exact reader key** and check the worker's *actual attempted key* in the event record.
- Distinguish operator setup, initial prompts and explicit skill selection from **post-launch interventions**. Do not advertise fully uncoached onboarding on this evidence.
- Label **frozen operator-collected tracker results** separately from live worker search, include open/closed issues **and** PRs, and record unavailable monetary costs and reviewer independence.

These are improvements to the manual guide and experiment procedure, **not** authorization to build a new coordinator or to rerun paid agents.

## Decision / publication boundary

The user/maintainer explicitly accepted this **scoped** review disposition on 2026-10-20. The acceptance is recorded here as an **operator-reported decision**, not an identity-authenticated signature. An issue comment or issue closure is a separate GitHub write and must not be implied if it has not actually occurred.

**No** standing authorization follows for new paid agents, cross-host certification, repository changes, issue publication, merge, deployment, a new tag or a GitHub Release. This documentation PR is reviewable on its own and does not change the recorded experiment.
