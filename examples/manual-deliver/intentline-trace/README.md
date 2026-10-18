# Real Intentline → Proofline trace for issue #21

**Current scope:** [Accepted narrow manual Deliver reference](../../../docs/deliver-v0.2-qualification-review.md).
**Historical record:** Pending-review and keep-open statements below predate the
later decision. The original failures, unlinked R2 and unknown coverage stay
unchanged. Start a new run with the [Deliver first-run guide](../../../patterns/deliver.md#first-run).

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

## Frozen candidate and actual native consumer

| Identity | Value |
| --- | --- |
| Coding implementation commit | `f54d44eb1d21fae2d7cfd8aae4216e91019a87d3` |
| Implementation tree | `a003d013419fd1f142f0d05175938c6b0d7008f3` |
| Proofline synthetic snapshot commit | `191c64bf4d7c785a668b5d035e8063dd257b7244` (same tree) |
| Proofline revision | `8e117fff4de2459637fe7f74f47ab17fc3341d84` |
| Export completion-marker SHA-256 | `b4bdce24f1d88fdc98f1464aa0386a8c506830713478dd07b73458979ff873e1` |
| One-time workflow commit | `951bf4bf2f81c2ab1afdb347191b71bea4ede301` |

[Native run 39118875068](https://github.com/grove/foundryline/actions/runs/39118875068)
ran on **macOS 15.7.9 ARM64**, **Python 3.12.10**, exact native **Codex CLI
0.162.1**. The full pinned Proofline checkout was present. Both native boundary
preflights were **OBSERVED**; denied reads included `actual_oracle`, writes to
candidate/source/receipts were denied, and network was denied. No unprotected
fallback was used. Check-only coding-model dispatches: **0**.

The [actual workflow](https://github.com/grove/foundryline/blob/951bf4bf2f81c2ab1afdb347191b71bea4ede301/.github/workflows/deliver-native-probe.yml)
explicitly checked out the coding commit above and copied the **real local
producer export byte for byte**. Proofline used `--source export/source-S1.txt`,
`--intentline-export export`, `--checks` and `--intentline-links`. Full expanded
CLI argv/cwd are retained in [verification.json](verification.json) and each
raw `*-invocation.json`. The temporary workflow is removed from the final PR;
it has no schedule and adds no continuing runner expense.

### Exact selections and observed gap

`SOURCE` below is this **complete actual argv**, not an inferred prose link:

```json
["/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12",
 "-B", "-m", "unittest", "discover", "-s", "checks",
 "-p", "test_intentline_trace.py", "-k", "test_complete_source_and_citations", "-v"]
```

`EXPORT` is this separate complete actual argv:

```json
["/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12",
 "-B", "-m", "unittest", "discover", "-s", "checks",
 "-p", "test_intentline_trace.py", "-k", "test_export_completion_and_file_identities", "-v"]
```

| Native record | Explicit selection/map | Actual outcome |
| --- | --- | --- |
| `gap-record` | [SOURCE at index 0](gap-checks.json); [R1 → 0/complete argv](gap-links.json) | CHECKS PASSED, exit 0; one test ran. R1 **LINKED CHECKS PASSED (limited evidence)**; R2–R7 **NOT DEMONSTRATED**. |
| `linked-record` | [SOURCE/EXPORT at indices 0/1](linked-checks.json); [R1 → 0, R2 → 1/complete argv](linked-links.json) | CHECKS PASSED, exit 0; two commands each ran one test. R1/R2 **LINKED CHECKS PASSED (limited evidence)**; R3–R7 **NOT DEMONSTRATED**. |

The second selection executed the separate export-integrity assertion within the
authorized evidence-retention task. Candidate, full S1, draft and export did not
change. R2 gained **limited evidence about retained export identity**, not proof
that every producer step, source meaning or whole R2 outcome was correct. The
complete seven-R inventory stayed present. Native `status --show-source` exited
0 on both original-host records. No later PR HEAD is claimed to have these receipts.

### Actual refusal and counterevidence

The separate [invalid map](invalid-map-links.json) linked index 0 to
`["/nonexistent/mismatched-argv"]`, while [the selected command](invalid-map-checks.json)
remained SOURCE. The real consumer exited **1**, stderr exactly:

```text
Intentline R check index/argv differs from the selected command
```

This is an **import rejection**, with no product check or report, not CHECKS
FAILED or a product defect. Original good export hashes matched before/after;
the good records were not edited. Raw `invalid-map-invocation.json`, stdout,
stderr and exit are in the native ZIP.

Before GitHub execution, the local macOS **26.6.2** / Python **3.14.8** / exact
native Codex **0.162.1** run imported all seven R IDs but returned **EXECUTION
UNAVAILABLE**, exit **2**. Its boundary was **NOT VERIFIED** because
`actual_oracle` read was allowed. **No selected check ran**. R1 was CHECK
UNAVAILABLE; unlinked R2–R7 were NOT DEMONSTRATED. [local-refusal.zip](local-refusal.zip)
retains that real attempt, invocation, identity, raw report/inputs and boundary
receipt. The successful different host does not qualify this local host.

## Maintainer handoff: original request → implementation → evidence

The table separates the **consumer's per-R selected-check result** from the raw
workflow evidence a maintainer must also inspect. Unlinked R IDs are never PASS.

| Original request/source line | R ID | Implementation change | Selected argv / raw receipt | Observed evidence / remaining gap |
| --- | --- | --- | --- | --- |
| S1:36 — genuine source/coding provenance | R1 | Full issue capture, authorization transcription and source/citation test | SOURCE; `gap-record/receipts/check-000.json`, `linked-record/receipts/check-000.json` | **LINKED CHECKS PASSED (limited evidence)** for exact issue bytes/citations. Agent/build/billing authentication is not proved by that test; commit/tree and external user authority are recorded separately. |
| S1:37 — real producer/export | R2 | Actual producer CLI, immutable export and export-integrity test | Initially none, then EXPORT; `linked-record/receipts/check-001.json` | **NOT DEMONSTRATED → LINKED CHECKS PASSED (limited evidence)**. Raw producer receipts and separate semantic inspection support the real round trip; test success alone does not prove complete R2. |
| S1:38 — real consumer/mapping | R3 | Real pinned native import, exact map and per-R retention | No R3-linked command; inspect native `*-invocation.json`, `*-record/report.json`, `identity.json` | Per-R **NOT DEMONSTRATED**. Qualified native execution and exact imported bytes/maps observed independently in raw workflow evidence. |
| S1:39 — meaningful evidence gap | R4 | R2 gap/expanded-selection comparison on identical candidate/export | No R4-linked command; compare both reports and R2's receipt | Per-R **NOT DEMONSTRATED**. Actual gap and new selected integrity assertion observed; no broader product-behavior or completeness claim. |
| S1:40 — safe refusal | R5 | Separate mismatched argv control; local boundary refusal retained | No R5-linked command; `invalid-map.stderr/exit`, local report | Per-R **NOT DEMONSTRATED**. Actual import rejection (exit 1) and local EXECUTION UNAVAILABLE (exit 2); neither is a product defect. |
| S1:41 — readable handoff | R6 | This table, identities, actual argv, raw receipts and cost/time limits | No R6-linked command; this handoff and structured readback | Per-R **NOT DEMONSTRATED**. Maintainer must judge readability and fidelity; no automated overall verdict. |
| S1:42 — independent review/bounded PR | R7 | Fresh raw-evidence review, ordinary checks and explicitly authorized unmerged PR | No R7-linked command; separate review and final validation linked below | Per-R **NOT DEMONSTRATED**. Same-operator/provider review is not maintainer approval; merge, closure, deploy and schedules remain unauthorized. |

`coverage_completeness: UNKNOWN`, including completeness of the R inventory.
This example preserves every original criterion; it does not use green tests to
silently approve the contract or decide that the whole issue is satisfied.

## Raw records, review and limits

- [producer.zip](producer.zip): unchanged original producer files, CLI inputs,
  outputs/exits and saved work; SHA-256
  `65419073f2dae549c1c0992f2ae5d979390222a0bc5516993ad12613da78d0fb`.
- [native-run.zip](native-run.zip): exact downloaded
  [GitHub artifact 12133581853](https://github.com/grove/foundryline/actions/runs/39118875068/artifacts/12133581853),
  SHA-256 `278ba30ee5ec16aca688616eebb7c5d670d6ea5d7aaaa6e0f32fe5c277e246cd`.
  GitHub expiry is October 25; these original bytes are retained durably in Git.
- [local-refusal.zip](local-refusal.zip): locally packaged real refusal;
  SHA-256 `dce7bbca3c234e5eb35a20cfd41794cba46ffcd06620e3f0a05d31b8f052fd33`.
- [verification.json](verification.json), [run metadata](remote-run.json),
  [artifact metadata](remote-artifacts.json) and [actual runner log](remote-log.txt)
  support navigation; they do not replace the raw reports/receipts.

Inside the native ZIP, read `identity.json`, all `*-checks.json`, `*-links.json`,
`*-invocation.json`, stdout/stderr/exits, `export/`,
`gap-record/report.json`, `linked-record/report.json`, their `receipts/` and
`intentline-export/` copies, and the negative outputs. Both included candidate
Git bundles were actually restored into temporary bare repositories; all **150
tracked blobs**, including hidden files, match the retained product and frozen
implementation tree. The artifact includes hidden files. No portable replay of
absolute-path-bound native `status` or certification of another host is claimed.

Proofline elapsed times: gap **3.280 seconds**, expanded links **1.637 seconds**;
wrapper times **3.603/1.735 seconds**. Native job approximately **30 seconds**,
excluding queue and local planning/coding/review. Each run had a 200-second cap,
40 seconds per check; job cap 12 minutes. Check-only model calls **0**. Coding
model tokens, dollar billing and total operator time were not exposed; no cost or
savings estimate is invented.

The native receipt covers the exact implementation tree above. Later commits
remove the one-time workflow and append evidence, review and status changes;
they change no checked Python implementation. Ordinary final reference/link
checks cover those appendices separately. Independent maintainer acceptance is
pending; keep **#18 and #21 open**. PR publication is explicitly authorized by the
user and supplies no merge/deploy/closure authority.

The [separate raw-evidence review](independent-review.md) found no blocking
finding. Its maintainer assessment supports the recorded R1/R2/R3/R5/R6 facts,
marks R4 partial because evidence is limited to identity assertions, and leaves
R7's final validation/publication to the later steps. This assessment never
relabels the consumer's unlinked R3–R7 rows as passing.

[Final ordinary validation](final-validation.json), [test output](final-tests.txt)
and [local-link results](final-links.json) record **29 passing reference tests**,
resolved local links and `git diff --check`. These are ordinary repository checks,
not new native receipts. The PR remains unmerged for maintainer review.
