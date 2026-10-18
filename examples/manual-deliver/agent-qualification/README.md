# Real approved coding task: retain and validate Deliver receipts

**Current scope:** [Accepted narrow manual Deliver reference](../../../docs/deliver-v0.2-qualification-review.md).
**Historical record:** Pending-review and leave-open statements below describe this
task's original handoff, before the later decision. Failures and unknowns remain
evidence about their original candidates. Start a new run with the
[Deliver first-run guide](../../../patterns/deliver.md#first-run).

This is a separate follow-up to [PR #19](https://github.com/grove/foundryline/pull/19).
That PR supplied the recipe, authored username fixture, native macOS check and
missing-command control. None of those is a new coding-agent implementation.

## Authority and scope

The [original user task](approved-task.md) explicitly authorizes implementation in
`grove/foundryline`, selected checks, a feature branch and a reviewable PR for
[issue #18](https://github.com/grove/foundryline/issues/18). It prohibits merge,
deployment and unrelated repository changes. The task text was transcribed from
the user message in the active Codex session; it is not authenticated by a saved
Intentline record. [The issue snapshot](issue-18.json) retains the original body
and all comments inspected before implementation. Its comment predates PR #19's
merge; GitHub reports the merge at `2026-10-18T09:32:44Z`.

The expected behavior already exists in issue #18:

| Source | Required behavior reached by this change |
| --- | --- |
| R4 | Retain native receipts, source/candidate identities, exact argv and results. |
| Requested deliverables, Python reference checks | Validate links, file identities, source citations and no invented runtime claims. |
| R6 | Preserve bounded results and unknown source coverage. |
| R7/R8 and definition of done | Independent evidence handoff, selected validation and a separately authorized reviewable PR. |

The substantive implementation is durable retention of PR #19's **exact**
downloaded artifact and a reference test that binds its raw reports, process
receipts, selected argv, exits, frozen product bytes and source to the existing
readback. Previously tests checked only summary metadata and hash lengths; the
raw artifact was scheduled to expire on October 25. This directly implements
issue #18's retention/identity requirements without inventing a product feature.

Starting repository revision: `c802795918900735a95aa7b9faf05454feb9cce5`
(PR #19 merged main). The active Codex coding agent implements the test and
retention changes in this repository. Proofline remains an external check-only
tool, with zero coding-model calls inside the verifier.

Affected paths: `checks/test_manual_deliver.py`, the retained ZIP and its existing
summary/documentation, this source/handoff directory, and the recipe/README/
implementation status links. No username implementation or caller changes are
needed. Reference checks read ZIP members without extracting or executing them.

## Selected verification and limits

Use pinned Proofline `8e117fff4de2459637fe7f74f47ab17fc3341d84`, macOS,
Python 3.11+ and native Codex CLI exactly 0.162.1. The direct path needs no
Intentline draft/export; its optional pin remains
`25e926f57e69395193fc0ac258f9e6dd2332cb18` and is not exercised.

The selected command is the actual host interpreter followed by
`-B -m unittest discover -s checks -v`, including the new receipt integrity test.
Ordinary runs remain ordinary Python checks. A qualified native run must retain
its full argv, frozen source/candidate and actual receipts separately. The safe
negative selection is `/nonexistent/foundryline-negative-check`.

## Actual candidate and execution

The implementation was committed **before** native checking:

| Identity | Value |
| --- | --- |
| Implementation commit | `01d2db090713a8852a66d1dfddca90bf7cac548a` |
| Implementation tree | `62f8517b004ba4c80b69da3f6e915cb5cab8518f` |
| Proofline frozen commit | `fc72c56a5ef98838df62626d687278be322f4518` |
| Proofline frozen tree | `62f8517b004ba4c80b69da3f6e915cb5cab8518f` (same implementation bytes) |
| Original task SHA-256 | `5d3e04a3699f9adafa4b65c0178943509f78e3a8e6a82ebe69360dd3aaa8ed5e` |
| One-time workflow commit | `77709987ecb0e6915eb0d57186f6a3d7987febfc` (explicitly checks out the implementation above) |

The [actual GitHub macOS run 39117358329](https://github.com/grove/foundryline/actions/runs/39117358329)
used macOS **15.7.9 ARM64**, Python **3.12.10**, native **Codex CLI 0.162.1**
and the required Proofline pin. The selected argv recorded directly in the report:

```json
["/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12",
 "-B", "-m", "unittest", "discover", "-s", "checks", "-v"]
```

**CHECKS PASSED**, CLI exit **0**, `status` readback exit **0**. One selected
command ran **27 tests**, including the newly implemented raw-receipt validation;
native boundary canaries were **OBSERVED**. The native receipt contains the full
test output (`Ran 27 tests`, `OK`) without stderr truncation. This is bounded
evidence about those tests, not an overall requirement verdict.

The same candidate and tool with selected argv
`["/nonexistent/foundryline-negative-check"]` produced **CHECKS UNAVAILABLE**,
CLI exit **2**, observation `UNAVAILABLE`, no executable return code, and the
actual missing-file diagnostic. The native boundary was separately **OBSERVED**.
It demonstrates unavailable evidence, not failing product behavior.

Before that run, the local macOS **26.6.2** / Python **3.14.8** / exact Codex
**0.162.1** attempts returned **EXECUTION UNAVAILABLE**. The native canaries
reported an allowed `actual_oracle` read, so the boundary was **NOT VERIFIED**.
Both attempts stopped before any selected check ran. No sandbox policy was
changed and no unprotected fallback was substituted. The different GitHub host
passed the unmodified tool's preflight; this does not qualify the local host.

## Raw evidence and replay limits

- [Original PR #19 artifact](../receipts/pr19-native.zip), unchanged ZIP digest
  `e4e9722c02f0bdfd35639e8045cf7f1a24bbf102055dc572d1628e9e9f358797`.
- [New native artifact](native-run.zip), unchanged ZIP digest
  `26fee247cd924aa3c23952d356bf3e38be3402c0e2dcfd95f6d82f9811352326`.
  [GitHub artifact 12132358034](https://github.com/grove/foundryline/actions/runs/39117358329/artifacts/12132358034)
  expires October 25; the exact downloaded ZIP is retained here in Git.
- [Local refusal archive](local-refusal.zip), ZIP digest
  `9e09034115131e87f75729aa4b229562eb8e889f72587a4ecc0b562a7b4f69fd`.
  It includes actual CLI invocations, source, reports, boundary process receipts,
  outputs/exits, Git bundles and ordinary test output. It was packaged locally;
  it is not a GitHub artifact.
- [Structured readback](verification.json) records exact selected argv, full
  Proofline CLI arguments/cwd, native report/receipt hashes, source/candidate
  identities, results, durations, boundaries and limitations. The native CLI
  argument expansion is derived from the [tested one-time workflow](https://github.com/grove/foundryline/blob/77709987ecb0e6915eb0d57186f6a3d7987febfc/.github/workflows/deliver-native-probe.yml)
  and actual runner paths; selected argv are directly observed in the reports.
  [Run metadata](remote-run.json) and [original artifact metadata](remote-artifacts.json)
  retain the host job, digest and timing readbacks.

Inside `native-run.zip`, inspect `identity.json`, `source-S1.txt`, `checks.json`,
`native-record/report.json`, `native-record/receipts/check-000.json`, the equivalent
`negative-record/` files, and CLI/status outputs and exits. Do not treat the
structured readback as a replacement for these raw files.

GitHub's upload omits dotfiles, including the frozen `.git` layout. The included
`native-candidate.bundle` and `negative-candidate.bundle` preserve the **exact Git
commit/tree and tracked bytes**, including `.gitattributes` and `.github` files.
Both bundles were actually restored into temporary bare repositories; all **131**
selected blobs, including the hidden files, matched their manifest hashes and
the named implementation commit. See the [bundle recovery readback](bundle-recovery.json). Bundles do not reconstruct the original `.git` byte layout,
so no portable replay of Proofline's whole-input snapshot digest is claimed.
The successful `status` inspection was observed on the **original host**; moving
or incompletely extracting a record must not be advertised as a fresh PASS.

Measured Proofline elapsed time: positive **2.771 seconds**, negative **1.138
seconds**; the entire GitHub job ran approximately **23 seconds**, excluding queue
and local preparation/review. Check-only model dispatches: **0**. Coding-stage
tokens, dollar billing and model cost were not available. No savings claim.

## Evidence handoff and remaining decisions

The native report belongs to the exact implementation commit above. Subsequent
commits remove the one-time workflow and append raw evidence, review and updated
status documentation; they do not change the checked Python implementation.
**The final PR HEAD is not claimed to have that native receipt.** Ordinary final
repository/link checks cover the later appendices separately; see the
[ordinary validation readback](final-validation.json), [test output](final-tests.txt)
and [local link results](final-links.json). Recheck any new
implementation changes against a new frozen candidate.

The [independent evidence review](independent-review.md) compares the original
task and complete issue body/comments with the diff, raw receipts, selected
tests and counterevidence. It is a fresh read-only agent review under the same
operator, not independent maintainer approval.

| Issue #18 requirement | Evidence and disposition for human review |
| --- | --- |
| R1 manual route | Provided by PR #19; follow-up adds a real scoped coding task and handoff. |
| R2 optional planning | Direct route observed without Intentline. Optional supported export is documented, **NOT RUN**; not required for this task. |
| R3 source/candidate example | PR #19's teaching example retained unchanged; this separate real task adds actual agent implementation and exact identities. Historical unlinked R2 remains **NOT DEMONSTRATED** by its earlier selected R1 native check. |
| R4 native evidence | Observed for the coding-agent implementation on qualified GitHub macOS; local host refused. Raw reports, selected argv, source/candidate/tool and receipt hashes retained. |
| R5 negative/refusal | Observed missing command on qualified native host, plus actual local boundary refusal. Other refusal-matrix scenarios remain proposed. |
| R6 bounded assessment | Selected command outcomes retained; no complete source acceptance inferred. `coverage_completeness: UNKNOWN`. |
| R7 review and approvals | Independent agent review and explicit user grants for coding/checks/PR CREATE. Maintainer review, merge and deployment remain separate. |
| R8 validation and PR | 27 native selected tests passed at the frozen implementation. Later ordinary final checks and reviewable PR recorded in the handoff/PR. Maintainer decision pending; leave issue open. |

The user authorized PR CREATE in the original task, independently of check
results. No merge, deployment, issue closure or unrelated repository mutation is
authorized or performed. Issue #18 remains **OPEN** for maintainer evaluation of
this bounded demonstration and any remaining scope; green checks do not decide it.
