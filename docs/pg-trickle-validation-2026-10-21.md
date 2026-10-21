# pg-trickle Deliver and Learn validation

**Decision: NO CLEAR BENEFIT in this pilot.**

**Action: KEEP FOUNDRYLINE UNCHANGED.**

Four fresh attempts satisfied the executed independent assessments, with no material regression found in those checks. Ordinary coding identified the relevant negative cases and performed comparably. Deliver added useful source/candidate records and honest uncertainty labels, but did not demonstrate a better implementation or additional executed native verification. This is a bounded decision from two issues, four attempts and one Learn retrospective, not a universal verdict or complete correctness claim. No recipe, tool or mandatory process change is proposed.

Experiment completed 2026-10-21 UTC. No product commits or remote mutations occurred during the experiment. This publication contains documentation and selected evidence only; it does not adopt the implementation patches or modify pg-trickle.

## Method and identities

Used the complete original [#1179](https://github.com/trickle-labs/pg-trickle/issues/1179) and [#1177](https://github.com/trickle-labs/pg-trickle/issues/1177), including confirmation that each had zero comments. Both originally described source-supported concerns without runtime reproduction. All attempts started clean at **`0cbd84dce4fede39fa36f2c8716e0faa0a9b1b14`**, tree `05ee73d25ae6d10adcd4788a2826525d30eb8085`. The source retains both defects; its locked dependencies, local PG18/pgrx toolchain and existing Docker builder supported actual builds/tests.

Read upstream `AGENTS.md`, project conventions, and Foundryline's [Deliver](../patterns/deliver.md), [Learn](../patterns/learn.md) and [handoff](evidence-handoff-template.md) at Foundryline `cc80099b4d955ba789509ceca4e7af113ae440ad`. Four separate repositories and fresh agents used the same inherited model configuration, **medium reasoning**, 20-minute budgets and existing infrastructure. Exact underlying model build, token usage and monetary cost were unavailable. Three worker slots required the fourth attempt to start later. No counterpart changes, assessment checks or previous results were supplied to workers; no fifth coding attempt occurred.

The [selected public evidence ZIP](pg-trickle-validation-2026-10-21-public-evidence.zip) contains 75 artifacts: source records, unchanged final patches, handoffs, assessment code, selected command/log excerpts and native refusal excerpts. Its [JSON integrity index](pg-trickle-validation-2026-10-21-public-evidence.json) records public member hashes, original member hashes, selection/redaction notes and artifact identities. The requested reviewed/public input files were not found; this subset was curated from the original report and private archive. The raw archive remains private. Machine-local paths are replaced with documented placeholders; these derivatives are not intact native receipts. Checksums establish copy integrity, not authenticity or complete coverage.

Public ZIP SHA256: `c8756d416305a39e20dbaed7fe3d54843b4fcb70c7829e24a89ecc825d544cfc`.

Candidate trees are historical local snapshots, not published commits:

| Attempt | Final tree |
| --- | --- |
| A ordinary | `b545ed25c1254c17c8f04c205b51a777e673b9fd` |
| A Deliver | `9bf65bc54ff336fc858cd4144a9c7ba2a187e13a` |
| B ordinary | `a64fe106ee933d98b46254424a140f72dd816ed4` |
| B Deliver | `f4131b0e8651518f06de2d34ea39d44bcd1e0b49` |

All ordinary indexes remained unstaged; final candidates had no nonignored untracked files. Proofline created isolated synthetic snapshot commits, retained separately from the product repositories.

## Deliver observations

| Attempt | Worker's actual verification | Independent assessment | Agent elapsed time |
| --- | --- | --- | --- |
| A ordinary | fmt/lint; 2,615 units; 21-test outbox suite; SQL attachment/collision probe using repository pg_tide stub | Correct helper behavior; all four assessment tests pass | 13m07s |
| A Deliver | fmt/lint; 2,615 units; own focused baseline/candidate comparison; native execution unavailable | Correct helper behavior; same four assessment tests pass; SQL integration not demonstrated by this worker | Approximately 8m35s–9m21s; first-action timestamp not exactly sampled |
| B ordinary | fmt/lint; own owner/payload/private-table regression passes | Correct tested access boundaries; independent role/isolation check and complete 20-test v108 suite pass | 10m03s |
| B Deliver | fmt/lint; complete 20-test v108 suite passes; native execution unavailable | Correct tested access boundaries; same independent role/isolation check passes | 8m24s |

Suite counts include three harness/oracle helper tests where present. These are selected-check results, not full-project certification. The selected artifacts distinguish worker self-tests, later independent assessments, ordinary repository checks and unexecuted native selections; full raw records remain private.

**#1179 was reproduced independently before attributing fixes:** the unchanged helper panics at byte54 inside `é`; ASCII compatibility passes. Both implementations retreat to a character boundary and preserve the original full-input xxh64 suffix. Assessment of the exact extracted helpers covered 2,123 valid 2/3/4-byte identifier cases, the 63-byte limit, unchanged short/ASCII/threshold output, deterministic hashing and tested common-prefix collisions. No tested requirement was missing. Extraction avoids PostgreSQL FFI and does not establish real pg_tide compatibility; ordinary's additional SQL evidence uses the project's contract stub.

**#1177 was reproduced on an independently built baseline:** registration and activation succeed, but reading the returned payload as the non-superuser owner fails with SQLSTATE42501, missing `pgtrickle_changes` schema access. Both fixes grant only owner-specific schema USAGE beside existing payload SELECT, preserving role quoting/error handling and documenting the change. The separate Testcontainers assessment passes on both source-built candidate images: exact payload content, repeat registration, resnapshot/acknowledgment rollback, quoted role name, cross-owner payload isolation, denial of private CDC reads, unrelated-role registration/consumer denial and private-schema CREATE denial. No material missing requirement or compatibility regression was found in those checks. Existing v108 conformance also passed on both candidates.

Both arms identified relevant negative cases themselves: Unicode boundary/hash collisions for A; payload usability while denying private-table reads for B. Assessment additionally checked cross-owner/unrelated-role isolation. Ordinary and Deliver agents both encountered and corrected environment/test-fixture problems; retained failures were not counted as product bugs. The assessor's two initial B harness mistakes—initial FULL policy and missing required source MAINTAIN—are separately preserved; neither established the reported defect.

### Added ceremony and practical limits

Both Deliver agents followed the direct published route without corrective implementation coaching; neither used optional Intentline. Operator-prepared source/tool checkouts mean unassisted installation/adoption was not demonstrated. The only post-launch coordinator message acknowledged avoiding a shared Docker tag.

The recipe pins Proofline `8e117fff4de2459637fe7f74f47ab17fc3341d84` and Codex CLI `0.162.1`. Installed CLI `0.163.0` caused **EXECUTION UNAVAILABLE** in both final native records, before canaries or selected commands ran. No protected check passed and no protections were relaxed. Separately authorized project tests remain ordinary evidence. A's first snapshot also refused generated build-directory changes. B's initial and corrected candidate/native records remain distinct in the private originals; the public subset identifies the final candidate and excerpts its refusal.

Additional work included private snapshots, check/status invocations, refusal inspection and handoff indexing. A spent about26 seconds in its two check invocations; B about8 seconds across four invocations, excluding reading/setup/status work. Total recipe overhead was not isolated. Common recording was required in both arms for this experiment, reducing the observable evidence-documentation difference. B Deliver selected a generic static privilege check for Proofline; that command passes the defective baseline too when run ordinarily by the assessor. It cannot demonstrate owner payload access.

No human debugging intervention occurred. Shared CPU/build caches, cache warming, different chosen test scope, operator setup and incomplete first-action timing prevent a speed/cost comparison. Incidental sibling image names/compiler paths were visible on the shared host; workers report no counterpart source/results use. Isolation was by separate context/repository and instruction, not an enforced filesystem boundary. Full project/upgrade suites and real pg_tide integration were not run. Unavailable/unrun checks are not passes.

## Learn: useful reconstruction, no new outcome demonstrated

Applied the published manual recipe separately to [PR1197](https://github.com/trickle-labs/pg-trickle/pull/1197), [issue1198](https://github.com/trickle-labs/pg-trickle/issues/1198), [post-merge CI39397208394](https://github.com/trickle-labs/pg-trickle/actions/runs/39397208394) and existing [PR1199](https://github.com/trickle-labs/pg-trickle/pull/1199). The public ZIP includes `learn-handoff.md` and selected primary-source/log excerpts under `learn/`. Remote state below is historical, as observed during the experiment, not a current status claim.

| Question | Primary observation |
| --- | --- |
| Intended change | Preserve USING predicates through composed-view inlining/differential refresh, retaining results, ownership, constrained MAINTAIN and rollback. The recorded sole-owner decision accepted a bounded fail-closed guard; it was not independent second-person approval. |
| Before merge | Head `82fb802582dcee9486e1a5c7684fba3791ec1783`; [CI39387305034](https://github.com/trickle-labs/pg-trickle/actions/runs/39387305034) succeeded, including 2,615 units and selected integration suites. Packaged light E2E was skipped by draft gating; other broad checks were also skipped. Local MDM successes and two OOM terminations remain author-reported, distinct artifact evidence. |
| Source-control delivery | Merged 2026-10-20 08:57:53 UTC as `04391eca2d53e548eafc84e82256df91eec01ea5`. Head and merge share tree `0a8a6079917b74820ebfe58b5818d555e94abadd`; changed CI selection explains the different coverage. |
| Actual post-merge result | [Job118624985581](https://github.com/trickle-labs/pg-trickle/actions/runs/39397208394/job/118624985581): 454 executed, 453 passed, one failed, six skipped. Existing `test_v104_delta_reference_consumer_reads_and_acknowledges` failed on all three retries: valid five-alias INNER USING rejected at creation, before later consumer assertions. This confirms a compatibility regression observed in CI. |
| Engineering decision followed | Existing issue1198/PR1199 changed the plan to proven merged-column provenance and new exact-artifact qualification, keeping producer release qualification blocked. This validation neither reimplemented1198 nor touched1199. At inspection,1199 was open/unmerged at `d8fb570afbbf6a50d14fe9fb5ce387f40bde742b`; head CI39630599345 remained in progress. Repair acceptance is UNKNOWN. |
| Deployment/customer outcome | Deployed revision/time and production/customer impact **UNKNOWN**. **NO APPROVED OUTCOME TARGET** for business metrics; DORA/SLO/customer effects not measured. The separate reported TPC-H SF1 timeout is not attributed to USING. |

The historical pg-trickle response changed its engineering plan, as already recorded in issue1198 and PR1199. Learn reconstructed that response; it did not produce a new decision or demonstrate independent production/customer impact. Reads overlapped the coding trials; exclusive Learn time/cost was not instrumented. This retrospective does not qualify production-outcome attribution or establish causal benefit over ordinary review. No further experiment or follow-up project is proposed here.

**Practical lesson: A verification check must distinguish the correct implementation from the original defect to provide meaningful evidence for that requirement.** The generic privilege check selected during the Deliver attempt did not establish the actual non-superuser payload-access outcome: it passed the defective baseline too. Retain this observation without adding a mandatory verification layer. The original recipes and historical examples remain unchanged.
