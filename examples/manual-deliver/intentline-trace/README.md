# Real Intentline → Proofline trace for issue #21

This implements the user-authorized [issue #21](https://github.com/grove/foundryline/issues/21)
follow-up to [Deliver #18](https://github.com/grove/foundryline/issues/18).
The substantive coding change adds two ordinary Python reference checks for
the complete original request/citations and the real producer export identities.
These protect the retained example from accidental source truncation or export
drift; they do not implement a new controller or certify requirements.

## Original request and authority

[S1](export/source-S1.txt) is the complete GitHub issue body, UTF-8 encoded
without an added newline, captured from [the raw issue response](issue-21.json).
It contains all seven original R1–R7 obligations. No comments existed at capture.
[The displayed user instruction](authorization.txt) is a disclosed chat
transcription authorizing implementation of #21 and PR creation. It is not an
authenticated approval artifact. Neither the contract nor a check grants authority.
The issue itself supplies the bounded native execution and separate review scope.
No merge, closure, deployment, schedule or other issue publication is authorized.

The active OpenAI Codex coding agent started from main
`628996f4bef2701d37a760c58bc3a7fef685d79e`. Its exact model build and coding-stage
tokens/cost are unavailable. This change reaches the new example, its reference
tests, link inventory and the Deliver status links. Existing username callers,
fixtures and optional direct Proofline route are unchanged.

## Actual producer, advisory draft

Intentline at `25e926f57e69395193fc0ac258f9e6dd2332cb18` ran its real
`prepare`, `propose`, `check`, `review`, `render`, then `export --format json`.
Every command exited 0. [The unedited export](export/export-manifest.json)
is initial schema 1/revision 1, single S1, `advisory: true`, `authority: unapproved`.
No adoption was recorded. [producer.zip](producer.zip) retains exact original
source, manifest, draft, saved work/revision, CLI argv/cwd/PYTHONPATH, stdout,
stderr, exits and the actual small capture/authoring scripts.

| Identity | SHA-256 |
| --- | --- |
| Original S1 (8,902 bytes) | `3c1a808cc0dfad337b88f47b61a7513182c829ab0a96efbcf8bc443c07a343bf` |
| Contract | `597ec331556f645de14bd99dfe2a363fc6c83cc43da6f7cfe3e3a5b003a3ba95` |
| Source manifest/bundle | `9a0980a26d6cef5c8ab23d70e3acaa2dd91be01f552644ec52218a1c5568f82e` |

A separately started read-only reviewer inspected the raw S1, issue response,
draft/saved contract, complete citations, constraints, exclusions, open decisions
and actual producer CLI receipts **before export**. It found no blocking semantic
omission or invented obligation, and warned that identity tests provide only
narrow R1/R2 evidence. It shares the operator/provider (OpenAI Codex); this is
independent inspection, not maintainer approval or external attestation.

## Selected checks and planned gap comparison

The actual implementation must be committed before native checking. Native
execution is **PENDING**, not qualified by ordinary Python checks. Proofline pin:
`8e117fff4de2459637fe7f74f47ab17fc3341d84`; supported host: macOS,
Python 3.11+, exact native Codex CLI **0.162.1**, verified sandbox; no fallback.
The full tool checkout exists. The ordinary path remains optional and needs no
Intentline runtime.

Two existing test methods form the explicit selections, with the actual host's
absolute Python substituted and retained in checks/maps/receipts:

```text
SOURCE = [PYTHON, -B, -m, unittest, discover, -s, checks,
          -p, test_intentline_trace.py, -k, test_complete_source_and_citations, -v]
EXPORT = [PYTHON, -B, -m, unittest, discover, -s, checks,
          -p, test_intentline_trace.py, -k, test_export_completion_and_file_identities, -v]
```

First select SOURCE and link only R1 to index 0. Then select SOURCE/EXPORT and
link R2 to index 1 without changing the candidate or export. This adds an
independently meaningful assertion about export integrity, within the authorized
reference-check scope. It supplies no general behavioral proof. R3–R7 remain
unlinked. A separate deliberately mismatched argv map will test actual import
refusal without mutating the good export or record. These consumer steps are
**PROPOSED — NOT RUN** until real receipts are appended.

## Maintainer assessment before native execution

| Original source line | R ID | Implementation change | Selected argv/receipt | Evidence / remaining gap |
| --- | --- | --- | --- | --- |
| S1:36 | R1 | Complete issue/source capture and provenance/citation test | SOURCE, planned index 0 | Exact source identity tested ordinarily; native/candidate evidence pending; authority is the external user instruction. |
| S1:37 | R2 | Real producer CLI/export retention and integrity test | EXPORT, initially unlinked then planned index 1 | Producer steps observed; consumer gap comparison pending; semantic review remains human/agent judgment. |
| S1:38 | R3 | Exact source/export/argv mapping in native run | None | NOT DEMONSTRATED until qualified consumer receipts exist. |
| S1:39 | R4 | Preserve all R IDs; compare R2 unlinked/linked | None | NOT DEMONSTRATED; planned comparison is limited identity-check evidence. |
| S1:40 | R5 | Separate invalid-map control | None | NOT DEMONSTRATED; actual refusal pending. |
| S1:41 | R6 | This readable source-to-evidence handoff | None | Partial; native identities, timing/results pending. |
| S1:42 | R7 | Fresh semantic reviewer and bounded PR scope | None | Partial; final raw receipt review, validation and unmerged PR pending. |

`coverage_completeness: UNKNOWN`. Even linked passing tests cannot establish
complete R1/R2 satisfaction, completeness of the R inventory, sandbox validity,
semantic fidelity, human approval or overall issue completion. Keep #18 and #21
open for the maintainer's assessment. Later evidence/status appendices must be
distinguished from the exact native-checked implementation tree.
