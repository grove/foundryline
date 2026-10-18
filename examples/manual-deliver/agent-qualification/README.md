# Real approved coding task: retain and validate Deliver receipts

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

**Execution pending in this implementation snapshot.** This paragraph is not a
native result. No approval, exhaustive requirement coverage or independent
maintainer acceptance follows from these tests. `coverage_completeness: UNKNOWN`.
