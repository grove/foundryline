# Deliver — from an approved task to check evidence and a reviewable PR

**Status: manual reference implemented; a Foundryline native Proofline pilot is NOT YET RUN.** This recipe is a guide, not an agent controller or permission-granting program. Follow [issue #18](https://github.com/grove/foundryline/issues/18) for actual host qualification. The [worked example](../examples/manual-deliver/README.md) is deliberately authored and its ordinary Python tests can run in CI; they are **not native Proofline receipts**.

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

The concrete [teaching candidate](../examples/manual-deliver/README.md) supplies the actual Python test commands and a source with two requirements, but its native Proofline commands remain **PROPOSED — NOT RUN**.

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

The [authored refusal matrix](../examples/manual-deliver/refusals.md) defines expected behaviors. **None of those specific Foundryline/Proofline native negative controls have been executed as part of this PR.** They must be witnessed on a qualified host before claiming Deliver is live-qualified.

## 5. Prepare a reviewable handoff — publication remains separate

Summarize the original request/authority, R IDs and source lines, candidate commit/tree and any uncommitted inputs, authorized edits, selected argv, native record/report and receipts, demonstrated check results, **NOT DEMONSTRATED** obligations, environment/unknowns and outstanding decisions. See the [handoff template](../examples/manual-deliver/handoff-template.md).

Get independent human/agent review as appropriate; it must evaluate the **original behavior**, not just a passing checker output. To create a PR, obtain **separate explicit PR CREATE authorization**. A reviewer then decides on merge, and deploy/release needs another authorization. `intentline-plan`, a `proofline check` report, a GitHub issue and this recipe **never** grant those rights.

For a small, routine task, just use your existing coding agent and chosen Proofline checks. Don't add a saved acceptance record when it adds no value.

## What still needs qualification

This repository can run **authored Python fixture tests and structural checks on Linux**, but it cannot treat those as a live native Proofline run on its qualified macOS/Codex environment. This Deliver recipe and candidate are **copyable and testable as examples**, not proof of a completed Foundryline coding-agent → Proofline → PR delivery.

To qualify Deliver, independently inspect one **real macOS/Codex CLI 0.162.1 native check-only run**, the exact frozen candidate and original source, a real refusal/failure case, the full Intentline export if used, and a reviewable **NOT PUBLISHED** handoff. Record actual host model calls, if any, separately from model-free checks. **If the host or receipts are unavailable, report NOT RUN/UNAVAILABLE rather than upgrading the claim.**
