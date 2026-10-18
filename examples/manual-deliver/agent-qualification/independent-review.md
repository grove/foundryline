# Independent evidence review — 2026-10-18

Retained verbatim from fresh read-only agent `/root/independent_evidence_review`.
The agent received the original task, issue snapshot, baseline/candidate identities
and raw evidence locations. It did not inherit the implementation conversation.
This is a same-operator agent review, not independent maintainer approval. The
original finding below was corrected; the reviewer's subsequent addendum follows.

---

The checked implementation is suitable for a reviewable, unmerged PR, after correcting the exact-argv readback described below. I found no supported defect in implementation commit `01d2db090713a8852a66d1dfddca90bf7cac548a`.

I independently compared the original approved task and issue body/comments against baseline `c802795…` → implementation `01d2db0…`. The substantive change is genuine issue #18 work: retaining PR #19’s exact raw artifact and adding the integrity test at `checks/test_manual_deliver.py:140`. It is not a new implementation of the inherited username fixture.

One concrete documentation finding:

- **DEMONSTRATED — incorrect reconstructed Proofline argv.** Current `agent-qualification/verification.json` adds an extra `native-record/` or `negative-record/` component to `--source`, `--checks`, and `--output`. The inspected workflow sets `WORK=/Users/runner/work/_temp/foundryline-deliver-native`; source/check input files belong directly under that directory, while outputs are `WORK/native-record` and `WORK/negative-record`. Raw reports and workflow are consistent; the authored readback needs correction.

Evidence I independently checked:

- GitHub’s read-only artifact API confirms artifact `12132358034`, run `39117358329`, workflow commit `77709987…`, and ZIP digest `26fee247…`.
- Local SHA-256 of `native-run.zip` matches that GitHub digest.
- Candidate `01d2db0…` resolves to tree `62f8517b004ba4c80b69da3f6e915cb5cab8518f`.
- Both native reports match their `evidence.json` hashes. Both process receipts match their hashes and embedded receipt objects.
- All **128 visible selected product files** in each native archive record match both manifest SHA-256 values and committed implementation bytes.
- Frozen source bytes match committed `approved-task.md`, source hash `5d3e04a3…`, and the retained top-level source.
- Native process receipt records the exact selected Python unittest command, **27 passing tests**, including the new receipt-integrity test, without truncation. Positive CLI exit is `0`; report is `CHECKS PASSED`.
- Negative receipt records the absent executable, launch exit `127`, CLI exit `2`, and `CHECKS UNAVAILABLE`.
- Local refusal archive digest matches `9e090341…`; both attempts report `EXECUTION UNAVAILABLE`, `actual_oracle: allowed`, boundary `NOT VERIFIED`, and no selected checks. No fallback success is claimed.
- PR #19’s retained ZIP has digest `e4e9722c…`; its report/receipt hashes and all four frozen teaching-product files match the existing readback and candidate.
- Inspected the pinned Proofline snapshot/native-check source to interpret synthetic candidate identity, boundary observations, truncation handling, and relocation limits.

Acceptance assessment:

| Requirement | Assessment |
|---|---|
| R1 | Satisfied by inherited manual route; final status links require ordinary validation. |
| R2 | Direct path demonstrated without Intentline. Optional export/import remains documented, **NOT RUN**. |
| R3 | Supported by inherited clearly authored example plus this distinct approved coding task. Historical unlinked username R2 remains **NOT DEMONSTRATED**. |
| R4 | Supported for exact implementation tree `62f8517…`, qualified macOS/native Codex `0.162.1`, selected commands and retained receipts. |
| R5 | Supported by remote missing-command control and accurately retained local boundary refusal. |
| R6 | Supported; results remain bounded and completeness **UNKNOWN**. |
| R7 | Partial until this review is retained and the authorized reviewable PR exists. Maintainer approval remains outstanding. |
| R8 | Checked candidate’s 27-test native receipt passes. Final appendices need ordinary tests/link checks and an unmerged PR. |

The archive omits `.gitattributes` and two `.github/workflows/` files. Its Git-bundle headers identify synthetic commit `fc72c56…`; I did not independently restore those bundles. Candidate source/tree recovery through a bundle must remain distinct from replaying the original filesystem snapshot, which includes omitted `.git` layout. Historical on-host `status` exit `0` is retained; relocated replay is not established.

This is a separate agent evidence review within the same operator/model family, not independent maintainer approval. Final evidence/documentation appendices are outside the native-checked implementation tree.

Project code, tests and builds executed by this reviewer: **NONE**. I used read-only file/Git inspection, standard-library ZIP/hash comparisons, and read-only GitHub metadata queries; no edits or publication.

Skipped optional Intentline execution, full sandbox-security review, bundle restoration and final PR-state verification. Remaining risk: selected checks and internally consistent receipts do not certify complete original-request acceptance.

---

Addendum — 2026-10-18: **The exact-argv readback finding is resolved.** I reread current `verification.json` and compared both reconstructed commands against workflow commit `77709987ecb0e6915eb0d57186f6a3d7987febfc` and raw report paths.

Both commands now correctly record the tool checkout as `cwd`, the Python launcher, repository, source/check files at the `WORK` root, respective time limits, and outputs at `WORK/native-record` and `WORK/negative-record`. No remaining mismatch was found in these fields.

I did not rerun product commands or tests. The original review’s candidate, archive-relocation, coverage and maintainer-approval limitations remain applicable.
