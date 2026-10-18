# Deliver — observed native Proofline check and refusal (2026-10-18)

**ACTUAL, MODEL-FREE NATIVE CHECK; NOT AN END-TO-END CODING-AGENT DELIVERY.**

This record concerns the **authored teaching candidate**, not a feature implemented
by a coding agent or an independently approved product issue. It establishes one
real candidate-bound, macOS-hosted Proofline `check` and one observed
unavailable-command case, without inventing Intentline export or publishing
authority. See [issue #18](https://github.com/grove/foundryline/issues/18) and
the [manual Deliver recipe](../../patterns/deliver.md).

## Verified source, tool, and runner

| Item | Actually observed |
| --- | --- |
| GitHub job | [PR run 39114778567](https://github.com/grove/foundryline/actions/runs/39114778567) — event `pull_request`, **completed success** |
| Authored source checkout | `grove/foundryline` PR merge-test commit `14c20409f89993e52d45a0946f48d10364c95d58` (not the final merged main or a coding agent's implementation) |
| Input request | [Exact illustrative request](original-request.md), SHA-256 `12ee949075e5faaf1d260055cc0ffe193b0c18259f68a06d4e4b4d81b1f0a9b6` |
| Proofline | [commit `8e117fff4de2459637fe7f74f47ab17fc3341d84`](https://github.com/grove/proofline/tree/8e117fff4de2459637fe7f74f47ab17fc3341d84) |
| Environment | GitHub-hosted macOS **15.7.9 ARM64**, Python **3.12**, Node **22.23.2**, native **Codex CLI 0.162.1** (exact pinned CLI version) |
| Example Git candidate initially prepared | `828b8d9327e6a3d7fc2af5f4a43b15bf50ce4756` in the disposable run directory |
| Proofline frozen candidate | `candidate_commit: cdd45db5149b9a4f9c2ef1315d9f49352c455907`; `candidate_tree: 16aebbdc8d43a23049ada8182ca7b6651fbcdfc6` |
| Frozen positive snapshot | `8918d0efee950346a8b8967aec2a4e842f1a559f0fa272bbaee06c8df00df69d` |
| Model calls and saved plans | Proofline check-only `model_dispatches: 0`; Intentline export **NONE**; coding-agent implementation **NOT OBSERVED** |

Only the small authored test example was checked. **No private target code,
real user task or project dependency installation was involved in the check.**
Setup created disposable tool/candidate directories and installed the exact
Codex npm package on the job runner; these are setup effects, not source writes
inside the protected Proofline check. The first published CI run on Linux
[passed ordinary authored tests](https://github.com/grove/foundryline/actions/runs/39114196028)
but that is separate evidence and does not substitute for this macOS check.

## Real positive check

The actual selected argv captured by Proofline (not an inferred shell command)
were:

```json
[
  "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12",
  "-B", "-m", "unittest",
  "tests.test_username_validation.UsernameValidationTests.test_rejects_blank"
]
```

The machine-readable `native-record/report.json` and its single native receipt
independently read back as:

- **`kind: bounded_local_check`, `status: CHECKS PASSED`**, CLI exit **0**,
  Proofline `status` exit **0**. One selected check with
  `observations[0].status: PASSED` and `returncode: 0`.
- Actual native check stderr includes `Ran 1 test` and `OK`, elapsed
  check process approximately **0.211 seconds**; total Proofline check operation
  approximately **1.840 seconds**. These durations exclude prior tool installation,
  GitHub runner queue and review.
- The native boundary's canary assessment was **`OBSERVED`** on the
  actually used host: selected denied reads/writes/network and allowed scratch
  behavior were observed. This is a limited probe, **not** a general OS security
  certificate or every possible host permission inspection.
- Proofline report SHA-256:
  `e28e5a799ee3101765cbadb9e19eabd8552fa4589012d07cd2d202f115c2da78` **(verify against artifact for full raw record)**.
  The selected check process receipt is `receipts/check-000.json`.
- **R1** (reject blank/whitespace-only names) has successful **limited selected-check
  evidence**. **R2** (preserve valid Unicode/spacing) has no selected native
  check; **NOT DEMONSTRATED** by this run. This was a *direct* Proofline
  check, so the illustrative R1/R2 IDs were **not imported from a saved
  Intentline record**; no native `promise_evidence` mapping is falsely claimed.
  Full source-obligation coverage remains **UNKNOWN**.

## Real negative control

On the **same pinned Proofline tool and the same frozen source/candidate tree**,
we intentionally selected the absent executable:

```text
/nonexistent/foundryline-negative-check
```

The second genuine Proofline check produced **`CHECKS UNAVAILABLE`**, CLI
exit **2**, native observation **`UNAVAILABLE`**, no executable return code,
and an observed `[Errno 2] No such file or directory` diagnostic. Its
native boundary preflight separately reported **`OBSERVED`**; absence of the
selected tool was **not** upgraded into failed product behavior. The native
negative report SHA-256 was
`d5d463fa3805feed4b3439483af978d6217c3f513902d189ec24b39bb9e155d4`
**(verify against artifact)**, with receipt at `receipts/check-000.json`.
The negative frozen candidate tree matched the positive tree
`16aebbdc8d43a23049ada8182ca7b6651fbcdfc6`.

## Earlier failed launch, honestly preserved

An earlier real macOS attempt,
[run 39114638979](https://github.com/grove/foundryline/actions/runs/39114638979),
selected the npm `codex` JavaScript wrapper. Inside the deliberately minimal
Proofline sandbox, the wrapper couldn't resolve `/usr/bin/env node`; the
selected product test never ran, even though the raw Proofline report used
`CHECKS FAILED` with exit 127. **That is an infrastructure/launcher failure,
not a demonstrated failing product assertion.** Its
[raw artifact](https://github.com/grove/foundryline/actions/runs/39114638979/artifacts/12131662161)
is separate; no incorrect success was recorded.

The corrected attempt used the *same installed Codex version's native Mach-O
binary directly*, via a temporary symlink in the runner's PATH (outside the
candidate). No sandbox permissions were widened and no unsandboxed fallback
check was substituted. The [exact temporary runner recipe at the tested commit](https://github.com/grove/foundryline/blob/0dc58c86b3aceca96e65fb73eb8debb9f23e7b4f/.github/workflows/deliver-native-probe.yml)
is an independently reviewable qualification setup, **not** a mandatory
Foundryline delivery runner.

## Receipt retention, review and remaining scope

**Raw source:** [GitHub Actions artifact `foundryline-deliver-native-39114778567-1`](https://github.com/grove/foundryline/actions/runs/39114778567/artifacts/12131743490),
ZIP SHA-256 `e4e9722c02f0bdfd35639e8045cf7f1a24bbf102055dc572d1628e9e9f358797`,
expires **2026-10-25**. The ZIP was downloaded and inspected, including
`identity.json`, `native-record/report.json`,
`native-record/receipts/check-000.json`,
`negative-record/report.json`, both exits and native `status` output.
The separately retained public run URL, metadata, this summary, source
references and actual pinned workflow remain discoverable after artifact
expiry, **and the [exact downloaded ZIP](receipts/pr19-native.zip) is now retained in Git,
with its original digest checked by the reference suite**.

The [structured qualification summary](native-qualification.json) is a
compact **readback of observed receipts**. The retained ZIP contains the original
reports, process receipts, frozen candidate files, selected argv, exits and source;
the reference suite compares those bytes with this summary without replaying them. No dollar billing, model spending or second-human operator
work was measured; no cost savings claim is made.

**Not qualified here:** a genuine coding agent implementing a newly authorized
issue; a saved Intentline-plan → JSON export → Proofline importer round trip;
successful evidence for R2 or exhaustive source coverage; an independent
review of all original project obligations; PR publication or merge; deployment;
Linux/Windows native Proofline support; or broad permission isolation.

**Next acceptance step for Foundryline Deliver:** One separately authorized real
issue/candidate coding handoff and, if opting into Intentline, a freshly generated
single-S1 initial JSON export with an actual `--intentline-links` mapping,
followed by independent scope/evidence review and a **separate PR CREATE grant**.
Keep [issue #18](https://github.com/grove/foundryline/issues/18) open for these
unfinished dimensions rather than labeling the whole Deliver journey complete.
