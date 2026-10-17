# Manual Discover — authored teaching examples

**All material under this directory is synthetic unless it is explicitly labeled as a completed, independently inspected real-host receipt. There are no real-host receipts here yet.**

These files teach the [manual Discover pattern](../../patterns/discover.md). They are **not** evidence that `gapline-audit`, `intentline-issue` or `intentline-plan` was activated, that a project was run, or that a GitHub issue was created. Do not count them toward the live pilot or independent reproduction for [Foundryline #2](https://github.com/grove/foundryline/issues/2).

## Contents

| File | What it illustrates |
| --- | --- |
| [fixtures/docs/registration-policy.md](fixtures/docs/registration-policy.md) | Fictional *accepted* behavioral authority for a small signup system |
| [fixtures/src/registration.py](fixtures/src/registration.py) | Deliberately limited code to examine **without executing it** |
| [fixtures/tests/test_registration.py](fixtures/tests/test_registration.py) | Selected authored tests showing why a green result, if observed, would not establish the whitespace boundary |
| [example-report.md](example-report.md) | A supported, source-level observation with counterevidence and scope limits |
| [example-issue-proposal.md](example-issue-proposal.md) | Proposed acceptance and checks; **NOT PUBLISHED** |
| [example-no-findings.md](example-no-findings.md) | A legitimate no-findings result within a smaller inspected scope |
| [example-refusal.md](example-refusal.md) | Unavailable inspection / no authority to produce findings |
| [run-record-template.md](run-record-template.md) | Blank actual-host pilot and independent-reproduction record |

## How to use

1. Read the fictional [policy](fixtures/docs/registration-policy.md) *before* reading the implementation. The code and tests are not the authority for expected product behavior.
2. Compare [registration.py](fixtures/src/registration.py) and [selected tests](fixtures/tests/test_registration.py). Note the difference between a source-level observation and an actually reproduced runtime failure.
3. Compare the [illustrative audit report](example-report.md) with the [issue draft](example-issue-proposal.md). Check that the policy and its limits remain visible, unsupported claims are not upgraded, and proposed tests have no execution receipts.
4. Examine the [no-findings](example-no-findings.md) and [refusal](example-refusal.md) cases. Neither is a defect count or failure to fill an issue quota.
5. In a **separately authorized, real agent host**, follow [patterns/discover.md](../../patterns/discover.md) against a pinned external repository. Use the [blank record](run-record-template.md) to capture actual observations. An authored fixture is not a substitute for that experiment.

To check the repository's reference documents and sample links (this does **not** execute the target fixture's code), from the Foundryline checkout:

~~~sh
python3 -m unittest discover -s checks -v
~~~

The reference test suite uses Python's standard library. Its successful result establishes narrow repository-document integrity, **not agent efficacy, model correctness, runtime isolation, or proof of a target system**.

## Example learning points

- Policy citations must refer to actual approved source material, not to code that happens to implement one behavior.
- Findings need supporting evidence, counterevidence, and disclosed uninspected scope.
- The suspected whitespace-only bug is **not an observed runtime defect** in these teaching fixtures.
- The selected authored tests are not the complete test suite of a real product.
- Duplicate issue lookup is **NOT CHECKED** in the synthetic example, so publication is not justified.
- `intentline-issue` REVIEW gives a proposal in the response; a formal saved Intentline agreement is a different, separately authorized operation.
- No issue, run record, approval or test result should be made to look real just to complete a checklist.
