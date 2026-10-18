# Foundryline Deliver — accepted scoped manual qualification for v0.2

**Status: ACCEPTED — NARROW, MANUAL DELIVER REFERENCE (2026-10-18).**  
**Review date:** 2026-10-18 (Europe/Oslo).  
**Decision recorded:** Accept a **manual, optional, specifically host-qualified Deliver blueprint**, **not** an autonomous coding controller, complete-requirements proof, universally isolated runner or publication/merge authority. This project-direction acceptance follows the merged [review PR #23](https://github.com/grove/foundryline/pull/23); it is not an independently administered human/security attestation or proof that any particular person personally re-executed the tests.

**Tracking:** [Foundryline #18](https://github.com/grove/foundryline/issues/18) · [#21](https://github.com/grove/foundryline/issues/21) · [Deliver guide](../patterns/deliver.md) · [RepoTend #15](https://github.com/grove/repotend/issues/15) · [Proofline PR #60](https://github.com/grove/proofline/pull/60).

## Summary in plain language

We can now point to a **real external software change**: the approved RepoTend audit command improvement. A coding agent implemented useful `--help` and invalid-format behavior in [RepoTend PR #16](https://github.com/grove/repotend/pull/16). An original, unapproved but source-grounded Intentline acceptance export captured two user-facing obligations, R1 and R2. The *same frozen candidate* was later checked with real Proofline native commands on a GitHub-hosted Mac.

With **only the help test** selected, R1's selected check passed and R2 was **NOT DEMONSTRATED**. With **both independently runnable tests** selected, each passed; those are **limited evidence for those exact selected behaviors**, not proof that every requirement, test oracle or repository property is correct. An intentionally mismatched mapping was rejected, and a paired macOS startup control pinpointed the OpenSSL startup blocker. The native file-read fix was [merged into Proofline](https://github.com/grove/proofline/pull/60) after review.

This is more than two tools exchanging documents: **both actual RepoTend behavior tests ran in Proofline's protected native check-only mode**. It demonstrates a bounded, optional source → coding candidate → acceptance export → selected-check evidence → reviewable PR composition. It does **not** turn Foundryline into a general-purpose automatic delivery system.

## Primary evidence preserved in Foundryline

The entire **original GitHub Actions ZIP**, **byte for byte**, is preserved under:

- [Retained raw ZIP](../examples/manual-deliver/receipts/repotend-issue15-native-39123644533.zip) — **1,892,994 bytes**, SHA-256 `31f8eb7ce91eb2a647a2e6af4e12050dddb47a3a73df619c7c24c8410c1883e8`; Git blob SHA-1 `a33a6fa58fb13bb25f96393cb43c157799a479c2`.
- [Source/run/member checksum manifest](../examples/manual-deliver/receipts/repotend-issue15-native-39123644533.manifest.json) — pins original artifact ID, run, candidate, host, and individually hashed raw member bytes.
- [Offline ZIP/receipt integrity reference checks](../checks/test_deliver_external_qualification.py) — use only the Python standard library; verify full ZIP identity, selected raw reports, exact check mapping, canary observations, source hashes and refusal. **Passing these offline tests is not a new native check.**

**Original source:** [Proofline Actions run #39123644533](https://github.com/grove/proofline/actions/runs/39123644533), [artifact 12134224973](https://github.com/grove/proofline/actions/runs/39123644533/artifacts/12134224973), originally scheduled to expire **October 25, 2026**. The original ZIP digest and its Git object hash were independently computed locally and matched the verified GitHub blob added by a **one-time checksum-guarded Foundryline Actions transfer** ([verified transfer job](https://github.com/grove/foundryline/actions/runs/39125313131)). Its write-enabled workflow was **removed immediately** from the review branch after committing the byte-identical ZIP. No permanent privileged workflow or schedule remains in the proposed change. The [review PR #23](https://github.com/grove/foundryline/pull/23) **has merged**; the original byte-identical ZIP is now durably committed on `main`, independent of GitHub's seven-day Actions artifact retention.

**Archive retention note:** The ZIP contains exact raw input/source/export bytes, check selection/mapping JSON, native `report.json` and `evidence.json`, receipts, before/after and positive/negative startup probes. It also includes an immutable original prior local/refusal record. Review it as data; do not execute arbitrary extracted code, trust archived paths as authenticated host identities or interpret the historical failures as successes. The blob is larger than normal documentation because this is one deliberately bounded, real-host qualification record.

## Scope and host identities

| Dimension | Actual qualified observation |
| --- | --- |
| Approved product issue | [RepoTend #15](https://github.com/grove/repotend/issues/15): help and invalid-format behavior, separate permission to implement/PR |
| Coding-agent product candidate | `grove/repotend@ead77fde6a5a7ba33e54cc81deb76fced8dbc333`; tree `544421686de4112ca1ac8bfb118cde750821e3ef` |
| Product review | [RepoTend PR #16](https://github.com/grove/repotend/pull/16) merged; **67 ordinary Node tests** on two Node versions, separate from Proofline native execution |
| Acceptance producer | Intentline `25e926f57e69395193fc0ac258f9e6dd2332cb18`; real initial schema-1/revision-1 **single-S1 JSON export**, `authority: unapproved` |
| Complete source identity | Original RepoTend issue body S1, SHA-256 `e1d61d83be03e8c442d05d1953bd2de47cd3a5a17a755c87d81826c56cb163f8` |
| Check runner | GitHub-hosted macOS **15.7.9 ARM64**, Python **3.12.10**, Node **22.16.0**, native Codex CLI **exactly 0.162.1** |
| Proofline actually tested | `f019a3927e5f4ce8a325b73edb2a28369265a95f`, temporary qualified probe revision with the narrowly scoped native Mac OpenSSL read grant |
| Proofline now merged | `adc0eb21c17bc70310b5f231ba8a092ca0d7d4e4` ([PR #60](https://github.com/grove/proofline/pull/60)); its `host_probe.py` and offline test Git **blobs match the actually tested code**, but there has been no separately claimed post-merge native replay of the entire new commit |
| Model calls within checks | **0** (Proofline check-only); coding-agent model tokens/cost/whole operator overhead were not completely measured |

Using an installed skill is not itself executable verification. Proofline needs the complete pinned tool and a genuinely qualified macOS/Codex execution boundary. The original unpatched Proofline SHA `8e117fff4de2459637fe7f74f47ab17fc3341d84` **failed** for Node on this macOS runner because of an OpenSSL read denial; its historical results are not retroactively converted to passes.

## Trace from real source requirements to actual behavior

The actual selected argv were recorded inside both raw reports, from the Node binary at `/Users/runner/hostedtoolcache/node/22.16.0/arm64/bin/node`:

- **R1:** `node --test --test-name-pattern=^R1 test/audit-cli.test.mjs` (full absolute argv and receipt saved)
- **R2:** `node --test --test-name-pattern=^R2 test/audit-cli.test.mjs` (a **distinct** selection/receipt)

The selected tests invoke the real RepoTend `audit.mjs` entrypoint, checking help or invalid-format stdout/stderr/exit and that audit engine loading and target modifications do not occur.

| Source obligation | Candidate implementation | R1-only native record | Both-linked native record |
| --- | --- | --- | --- |
| **R1** from S1 line 15 — `--help` explains usage, exits 0, no audit | `skills/repotend/scripts/cli.ts`, actual audit entrypoint and independently selected `^R1` behavior test | **LINKED CHECKS PASSED (limited evidence)**, TAP 1/1; `r1-only-record/receipts/check-000.json` | **LINKED CHECKS PASSED (limited evidence)**, TAP 1/1; `r1-r2-record/receipts/check-000.json` |
| **R2** from S1 line 23 — invalid `--format xml` gives clear error, no report/audit | Same CLI + independently selected `^R2` behavior test | **NOT DEMONSTRATED**, no R2 selected command | **LINKED CHECKS PASSED (limited evidence)**, TAP 1/1; `r1-r2-record/receipts/check-001.json` |

Both completed Proofline native records report `CHECKS PASSED`, CLI exit **0**, on-host `status --show-source` exit **0**, `boundary.assessment.status: OBSERVED`, source hash and exact candidate tree intact, and no model dispatches. Selected commands returned 0 with complete, untruncated stdout and no stderr. The original acceptance was not silently adopted. **`coverage_completeness: UNKNOWN`** in both records.

### The witnessed negatives matter

- **Bad mapping:** an intentionally wrong R1 `index/argv` association returned **exit 1** with `Intentline R check index/argv differs from the selected command`; no product report was generated. This is a correct import **refusal**, not a failing product test.
- **Same-run Node startup A/B:** without the *single* proposed read-only entry for `/System/Library/OpenSSL/openssl.cnf`, Node exited **1** with OpenSSL `Operation not permitted`; with that entry on the **same host**, Node exited **0** and printed `NODE_BOOTSTRAPPED`. No broad `/System` read, writes, private file access or network was granted. Native process canaries continued to deny their tested private reads, target/source/receipt writes, mode changes and loopback access; scratch writes were permitted.
- **Historical failures remain recorded:** local macOS native boundary qualification failed in earlier attempts; [RepoTend PR #17](https://github.com/grove/repotend/pull/17) preserved a GitHub-hosted Node startup failure as raw `CHECKS FAILED` with an interpretive **EXECUTION UNAVAILABLE** because no product assertion ran. The corrected later run does not rewrite those original outcomes.

## Evidence review and its independence

I compared the retrieved artifact's original ZIP checksum, GitHub blob SHA-1, member hashes, exact source/export, both completed native reports, process receipts, requirement maps and paired startup control. The previously recorded [separately started agent reviews](https://github.com/grove/repotend/blob/main/docs/evidence/issue-15/independent-review.md) and [Proofline issue #59 report](https://github.com/grove/proofline/blob/main/evaluation/results/issue59-macos-openssl/README.md) describe their own scope and limitations.

**Independence limit:** The review conducted here is a read-only desk inspection by an assistant; the earlier independent agent reviews shared operators/providers. No separately administered human reviewer, full adversarial security evaluation or general cross-host repeatability is established by this record.

## Decision recorded and boundaries

**Decision: ACCEPT the narrow manual Deliver reference described below.** This is the project/operator's explicit scope decision following merged PR #23 and a read-only review of the retained records. It does **not** independently authenticate a human maintainer's personal inspection, certify the host security boundary or turn limited selected-check evidence into overall requirements acceptance. The evidence and its limitations remain visible for future reviewer challenge.

**Accepted scope:**

- Documented **manual** Deliver route: original full request → optional Intentline draft/export → authorized existing coding agent → frozen candidate → actual selected Proofline checks → human-reviewed, separately authorized PR.
- Observed direct Proofline route from [Foundryline PR #20](https://github.com/grove/foundryline/pull/20) and optional S1 producer/consumer route from [PR #22](https://github.com/grove/foundryline/pull/22), with this stronger **external RepoTend user-facing behavior** test.
- The specific macOS/Codex/Node and pinned tool revisions above only. Explicit preservation of refusal, stale/unavailable/not-demonstrated evidence. No authoritative promise inventory, complete user-request acceptance or all-host security warranty.

**Excluded from this acceptance (not qualified or not built):** scheduled issue intake, automatic publication, autonomous coding orchestration, full product requirement attestation, P2P-native contract conversion, Linux/Windows native Proofline execution, broad host isolation, deploy or merge automation.

**Issue disposition:** Foundryline [#21](https://github.com/grove/foundryline/issues/21) and [#18](https://github.com/grove/foundryline/issues/18) may be closed **only as completed for this explicitly scoped manual reference**, with links to the original and negative evidence. Resolve [RepoTend #15](https://github.com/grove/repotend/issues/15) and [Proofline #59](https://github.com/grove/proofline/issues/59) independently for their own actually merged product fixes, keeping their historical failed receipts. An issue closure is not additional runtime evidence.

**Release readiness:** [Maintain's scoped acceptance](maintain-v0.2-qualification-review.md) is now documented separately, and the three manual recipes have real but different evidence boundaries. The manual-only [Foundryline v0.2.0 public release](https://github.com/grove/foundryline/releases/tag/v0.2.0) was authorized and published **separately from** this acceptance at source commit `8409eebe0389461ec60a4bef6a5ce2aec6fb0903`. See the [verified publication record](releases/v0.2.0.md). The older conditional roadmap discussed scheduled intake, but **scheduling remains deferred, not qualified and not enabled**.

## How a maintainer can verify the archived record

From the repository root, without executing any archived product:

```sh
python3 -B -m unittest checks.test_deliver_external_qualification -v
```

The tests use only Python's standard library to read ZIP bytes, verify the full original ZIP checksum and Git object identity, selected primary member hashes, genuine source identity, limited per-R native outcomes and refusal. They are **offline reference checks**, *not* a fresh model call or a newly qualified native sandbox. Also review the full ZIP and the immutable Actions run directly before choosing to accept the scope.
