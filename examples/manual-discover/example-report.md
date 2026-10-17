# Synthetic Gapline-style audit report — NOT AN ACTUAL RUN

**Provenance:** AUTHORED FIXTURE, not produced by Gapline or a coding agent. No source checkout, skill invocation, file inspection, test execution, verification or sandbox qualification occurred. This is a teaching illustration using neighboring files in this directory.

| Field | Illustrative value |
| --- | --- |
| Target | Fictional username-registration fixture in `fixtures/` |
| Git SHA / working tree | **NOT AVAILABLE** — no real target revision was pinned |
| Scope represented | `fixtures/docs/registration-policy.md`, `fixtures/src/registration.py`, and `fixtures/tests/test_registration.py` |
| Tools executed | **NONE**; manually authored example |
| Project code, tests, builds executed | **NONE** |
| Budget / elapsed time / model cost | **NOT MEASURED** |
| Real host skill activation | **NO** |
| Actual issue inventory / duplicates | **NOT CHECKED** |
| Relevant unassessed scope | Other potential callers, validation middleware, full tests, deployment and runtime |

## Finding F1 — whitespace-only signup validation

**Illustrative evidence level:** SUPPORTED *for this source-level observation only*. No runtime failure was reproduced.

**Fictional expected behavior:** [registration-policy.md, line 5](fixtures/docs/registration-policy.md) says reject empty or whitespace-only usernames; [lines 6–7](fixtures/docs/registration-policy.md) additionally require Unicode preservation and registration-entry-point validation.

**Static implementation observation:** [registration.py, lines 4–7](fixtures/src/registration.py) rejects only values that are falsey and then returns the input unchanged. A nonempty whitespace-only string is truthy in Python. The excerpt therefore does not show the required whitespace-only rejection.

**Selected test observation:** [test_registration.py, lines 9–15](fixtures/tests/test_registration.py) checks the empty-string and Unicode cases but has no whitespace-only assertion. This says nothing about tests outside the selected fixture.

**Counterevidence / alternative explanation:** A separate caller might normalize input before it reaches the entry point; the fictional policy expressly requires enforcement at `register` even if client-side validation is skipped. No other callers or guards were inspected in this example, so this is not a runtime reproduction claim.

**Why it matters (hypothetical):** A whitespace-only username could be accepted in the fictitious signup path, contrary to the authored policy. User impact in any real product is **UNKNOWN**.

**Smallest falsifying observation (PROPOSED — NOT RUN):** In a separately authorized, isolated test run, submit `"   "` directly to `register` and observe rejection with a clear validation error. Also check `""` rejection and `"Åsa"` preservation. A whitespace-only value accepted would support the suspected runtime effect; consistent rejection at the actual entry point would refute it.

**Disposition:** ISSUE_CANDIDATE for **confirm-before-fixing**; no issue was published and no contract was saved.

## Limits

This report is a sample of how findings should be written, **not evidence that a real Gapline skill returned a finding, that a test passed or failed, or that a security boundary was enforced**. Do not use it to check off any real-host acceptance criterion.
