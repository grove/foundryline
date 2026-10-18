# Deliver — from an approved task to check evidence and a reviewable PR

**Status: ACCEPTED as a narrowly qualified, human-operated manual Deliver reference on the pinned, observed host and tool versions.** PR #19 supplied the [authored fixture and original native check](../examples/manual-deliver/native-qualification.md). The separate [approved receipt-validation task](../examples/manual-deliver/agent-qualification/README.md) records actual coding-agent implementation, a frozen candidate, native Proofline checks and refusal evidence for independent review and an explicitly authorized PR. The [issue #21 trace](../examples/manual-deliver/intentline-trace/README.md) adds an actual initial S1 Intentline draft/export, native import, gap/relink comparison and safe map rejection. See the [scoped Deliver acceptance decision](../docs/deliver-v0.2-qualification-review.md), [source issue #18](https://github.com/grove/foundryline/issues/18), and [durable real external native ZIP](../examples/manual-deliver/receipts/repotend-issue15-native-39123644533.zip). The **manual recipe** is accepted, not complete product correctness, universal sandbox security or automatic publication/merge authority.

**In one sentence:** Choose an authorized task, let your existing coding agent implement it, check the exact candidate with [Proofline](https://github.com/grove/proofline), then decide separately whether to open or merge a pull request.

You can use the direct Proofline route without Intentline. Structured acceptance is an **optional** extra when a task deserves it.

## 1. Admit one real request — no automatic approval

Start with the complete applicable original issue or request, including its comments, policies, constraints and exceptions. Freeze the source bytes/revision you intend to act on; if the task is disputed, first ask for a decision. A Gapline hypothesis or a RepoTend warning is not automatically an approved coding task.

Record the adopting repository and Git revision/working-tree changes, the exact requested outcome, authorized paths, agent host, budgets and allowed code modifications. **Authorization to investigate, draft an issue, plan acceptance, edit code, run checks, publish a PR, merge, and deploy are separate decisions.** Do not infer approval from a passing CI run, saved contract, PR comment or tool permission.

For a simple issue, **skip planning** and continue with the exact original request. If acceptance clauses are helpful, follow [Intentline's planning skill](https://github.com/grove/intentline/blob/25e926f57e69395193fc0ac258f9e6dd2332cb18/skills/intentline-plan/SKILL.md) and separately authorize saving a private draft. Check the full original source against each drafted requirement, its constraints/exclusions and open decisions. Intentline can check record shape, **not** whether the draft is the true/approved product requirement.

## 2. Authorize an existing coding agent to make an identifiable candidate

Use your chosen coding agent (or a human developer) in its properly configured workspace; **Foundryline does not start one**. Grant exactly the implementation scope and time/tool budget needed. It may edit permitted files only. No implicit issue tracker writes, push, merge or deploy. Keep unresolved decisions visible.

Capture the implementation candidate as an **exact** Git commit/tree and all relevant staged, unstaged and nonignored untracked changes (or identify a clean fixed commit). Stop writes before taking the check snapshot. Do not treat a branch name such as `main` as the candidate identity.

If tests/dependencies need installation, do that **separately, with authorization, before** invoking Proofline. Proofline itself does not install dependencies.

## 3. Choose checks; use Proofline only on a qualified native host

**Pinned interface (verified from published upstream source):** [Proofline `8e117fff4de2459637fe7f74f47ab17fc3341d84`](https://github.com/grove/proofline/tree/8e117fff4de2459637fe7f74f47ab17fc3341d84), with **macOS, Python 3.11+, and exact Codex CLI `0.162.1`** for native checks. The CLI is `proofline.py check` (existing implementation, not a second agent); it uses Codex's protected native execution, **with no coding-model invocation in check-only mode**. Linux reference CI is not qualified native execution; never fall back to unprotected shell checks while claiming Proofline evidence. A skill installation alone does not install the Proofline CLI.

**Node/macos qualification detail:** The original pinned Proofline revision
`8e117fff4de2459637fe7f74f47ab17fc3341d84` applies to the earlier
qualified **Python** teaching checks; on the observed macOS host it **could
not run Node checks** because Node could not read its OpenSSL config inside
that version's sandbox. The [independently reviewed, merged Proofline fix
`adc0eb21c17bc70310b5f231ba8a092ca0d7d4e4`](https://github.com/grove/proofline/pull/60)
adds read access to that **exact regular macOS configuration file**, with
no corresponding broad directory/network permission. The [successful external
RepoTend Node experiment](../docs/deliver-v0.2-qualification-review.md) used
the **actually tested precursor tool revision**
`f019a3927e5f4ce8a325b73edb2a28369265a95f`, whose native permission
source blob matches the merged revision. This is evidence for **one specific
macOS/Node/Codex setup**; choose and pin a reviewed compatible revision and
reconfirm the native canaries on your own host. Never claim the old unpatched
Node execution succeeded or assume all future Node versions are supported.


Inspect/trust the pinned tool and supported environment first, keep a full Proofline checkout available, and require an **actual** sandbox preflight. Choose project commands that exist, are authorized to run, and do not require writing into the frozen candidate or network access. Examples use an absolute Python interpreter and `-B` to prevent import-cache writes.

### Minimal check-only path — Intentline NOT required

The following is a **command template, not an executed receipt**. `$PRODUCT` must be an actual Git root with an implementation candidate; `$ORIGINAL` must contain the complete original request bytes. `$PROOFLINE` must point to the reviewed, pinned checkout. The selected check command needs actual product tests, and `$RECORD` must be a **new, private path outside the product**.

```sh
PYTHON="$(python3 -B -c 'import os,sys; print(os.path.realpath(sys.executable))')"
"$PYTHON" -B "$PROOFLINE/proofline.py" check \
  --repo "$PRODUCT" --source "$ORIGINAL" \
  --command "$PYTHON -B -m unittest discover -s tests" \
  --output "$RECORD"
"$PYTHON" -B "$PROOFLINE/proofline.py" status "$RECORD/report.json" --show-source
```

The report's original-source SHA-256, candidate snapshot/commit/tree identity, **selected argv**, exit statuses, elapsed time and bounded native stdout/stderr receipts bind evidence to that one candidate. Capture actual CLI/version/host, record path, tool/command hashes when available, full source, remaining gaps, check/model costs where actually measurable, and effects observed. **A selected check passing is only evidence about that check.** A new candidate after a fix needs a new check; an old frozen record remains historical evidence about the *old* candidate.

The [teaching candidate](../examples/manual-deliver/README.md) now has an **observed model-free native Proofline check-only run on macOS**: one selected R1 unit test passed on a frozen candidate, while the separate R2 requirement remains unselected and unproven by that check. Its [real receipts](../examples/manual-deliver/native-qualification.md) bind the result to source/candidate identities. The optional Intentline-import path for this authored username fixture is **PROPOSED — NOT RUN**; no coding agent performed this example's implementation. The separate [real issue #21 trace](../examples/manual-deliver/intentline-trace/README.md) exercises the genuine producer/consumer path.

### Optional Intentline JSON export → Proofline evidence map

If you separately created and inspected a supported Intentline acceptance draft, the **existing** producer interface at [Intentline `25e926f57e69395193fc0ac258f9e6dd2332cb18`](https://github.com/grove/intentline/tree/25e926f57e69395193fc0ac258f9e6dd2332cb18) is:

```sh
python -B -m intentline check --work "$INTENTLINE_WORK"
python -B -m intentline review --work "$INTENTLINE_WORK" --json
python -B -m intentline export --work "$INTENTLINE_WORK" \
  --format json --out "$INTENTLINE_EXPORT" --json
```

`$INTENTLINE_WORK` must be a genuine completed draft for **one original request S1**, initial acceptance `schema_version: 1`, `revision: 1`, with no additional context/amendments/slices/lineage and no unresolved decisions. `$INTENTLINE_EXPORT` must be a new owner-private directory outside the project. The export must contain the final completion marker, source-S1 bytes, contract and manifests/hashes. Do not invent those files by hand or edit them until they pass the consumer's original-byte/hash validation.

```sh
"$PYTHON" -B "$PROOFLINE/proofline.py" check \
  --repo "$PRODUCT" \
  --source "$INTENTLINE_EXPORT/source-S1.txt" \
  --checks "$CHECKS_JSON" \
  --intentline-export "$INTENTLINE_EXPORT" \
  --intentline-links "$LINKS_JSON" \
  --output "$RECORD"
"$PYTHON" -B "$PROOFLINE/proofline.py" status "$RECORD/report.json"
```

`$CHECKS_JSON` holds the **selected argv arrays**, and optional `$LINKS_JSON` holds exact zero-based command `index` and complete matching `argv` for each linked R ID. For the worked example, [the plan](../examples/manual-deliver/verification-plan.json) maps **R1** to one actual named test and deliberately leaves **R2 unlinked**. The [example instructions](../examples/manual-deliver/README.md) show how to generate **matching, host-specific argv arrays**; replace planned association IDs if an actual Intentline contract differs. **R2 remains NOT DEMONSTRATED by the selected Proofline check even if ordinary fixture CI separately passes its R2 test.** Coverage completeness remains **UNKNOWN**.

`--promises` and `--intentline-export` are mutually exclusive. Do not silently convert rejected revised, multi-source, amended, child, native, partially copied, stale, tampered or symlinked exports into one S1 request; stop with **UNSUPPORTED/UNAVAILABLE** and use the direct original-request path or resolve the contract upstream. The Intentline draft is advisory: even `ADOPTED_ASSERTED` is only an unverified operator assertion, not externally authenticated permission for implementation or publication. See [producer integration contract](https://github.com/grove/intentline/blob/25e926f57e69395193fc0ac258f9e6dd2332cb18/docs/INTEGRATIONS.md) and [consumer contract](https://github.com/grove/proofline/blob/8e117fff4de2459637fe7f74f47ab17fc3341d84/README.md#intentline-handoff-also-optional).

## 4. Examine what the checker actually said — including refusal

Read the full `report.json` and bounded receipts using `status`; do not infer anything solely from a shell exit code, PR green check or an agent's summary. Proofline may report:

| Report result | Safe interpretation |
| --- | --- |
| **CHECKS PASSED** | The selected commands ran on the frozen candidate and passed; not an overall requirement verdict |
| **CHECKS FAILED** | Selected command(s) actually exited nonzero; examine receipts before calling it a defect |
| **CHECKS UNAVAILABLE** | Command execution produced inadequate evidence (timeout, missing executable, incomplete receipt, etc.); not a failed product |
| **EXECUTION UNAVAILABLE** | Required sandbox/earlier execution boundary could not run; **no valid fallback check** |
| **STALE CHECKS** | The record's frozen source, candidate, commands or receipts cannot be matched; recheck |
| **NOT DEMONSTRATED** (a particular R ID) | No **selected exact check mapping** establishes evidence for that imported obligation |
| **coverage_completeness: UNKNOWN** | Even linked passing checks do **not** prove that all true original obligations were inventoried |

A check failure is not automatically a runtime product bug; a passed check does not certify all promised behavior. If needed, choose additional behavior-focused checks with known authorization, re-freeze/re-run and retain the new record separately. Old check records refer to their original frozen candidate; don't retroactively overwrite them.

The [refusal matrix](../examples/manual-deliver/refusals.md) records PR #19's **one witnessed native negative control**: an intentionally absent selected executable returned **CHECKS UNAVAILABLE**, not failed product behavior. The later [issue #21 trace](../examples/manual-deliver/intentline-trace/README.md) adds an actual mismatched-map import rejection and retains a local native-boundary refusal. Other matrix scenarios remain **PROPOSED — NOT RUN**. These controls do **not** qualify the complete software-delivery journey.

## 5. Prepare a reviewable handoff — publication remains separate

Summarize the original request/authority, R IDs and source lines, candidate commit/tree and any uncommitted inputs, authorized edits, selected argv, native record/report and receipts, demonstrated check results, **NOT DEMONSTRATED** obligations, environment/unknowns and outstanding decisions. See the [handoff template](../examples/manual-deliver/handoff-template.md).

Get independent human/agent review as appropriate; it must evaluate the **original behavior**, not just a passing checker output. To create a PR, obtain **separate explicit PR CREATE authorization**. A reviewer then decides on merge, and deploy/release needs another authorization. `intentline-plan`, a `proofline check` report, a GitHub issue and this recipe **never** grant those rights.

For a small, routine task, just use your existing coding agent and chosen Proofline checks. Don't add a saved acceptance record when it adds no value.

## Observed scope and remaining qualification

The [real coding-agent follow-up](../examples/manual-deliver/agent-qualification/README.md)
uses an actual user-approved part of issue #18: retaining original native receipts
and validating their identities. The implementation commit/tree, complete original
task, pinned tools, selected argv, raw reports, independent evidence review and
publication boundaries are retained separately from PR #19's authored example.
The selected repository suite passed through native Proofline on GitHub macOS;
a missing executable was **CHECKS UNAVAILABLE**. A local macOS attempt first
returned **EXECUTION UNAVAILABLE** because its canary boundary was not verified;
no unsafe fallback was used.

These observations cover one bounded direct-route task. Linux reference tests
remain ordinary checks. Evidence belongs to the exact frozen implementation,
not the later PR evidence/status appendices. Independent maintainer approval,
merge and deployment remain separate decisions. The optional Intentline
single-S1 export/import route was skipped for that direct-route task. The separate
[issue #21 trace](../examples/manual-deliver/intentline-trace/README.md) now retains
a real producer export, native consumer, R2 gap/relink comparison and mismatched-map
rejection against its own frozen implementation. That does not execute the
authored username fixture's proposed import path or certify all requirements. Historical unlinked R2 evidence stays **NOT DEMONSTRATED**
by the earlier selected R1 check, and `coverage_completeness: UNKNOWN` applies
throughout. Keep absent evidence **NOT RUN/UNAVAILABLE**.

The [external RepoTend issue #15 behavior pilot](../docs/deliver-v0.2-qualification-review.md)
also exercised the **real source-to-behavior trace**, not merely source-file
integrity: the R1-only native check passed while R2 was **NOT DEMONSTRATED**;
then separate actual R1 and R2 tests both passed on the exact same frozen
coding-agent implementation using the original unaltered Intentline export.
The archived evidence includes a real bad-map refusal and the earlier/paired
OpenSSL failure controls. This supports a **proposed scoped manual Deliver
acceptance**, pending independent maintainer review. Do not promote it to
universal sandbox isolation, complete requirement satisfaction, PR/merge
approval or a fully automatic controller.

