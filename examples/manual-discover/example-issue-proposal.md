# NOT PUBLISHED — synthetic issue proposal

**Status:** NOT PUBLISHED. AUTHORED FIXTURE. Not a live GitHub issue, not approved for implementation, not produced by a real `intentline-issue` invocation, and not a saved Intentline contract.

**Proposed title:** Confirm signup rejects whitespace-only usernames at the registration entry point

The fictional signup policy requires empty and whitespace-only usernames to be rejected. The selected static code excerpt rejects an empty string but does not visibly reject a nonempty whitespace-only string. If the behavior also occurs in a real execution path, it could allow invalid signup names. This **has not been demonstrated at runtime**.

**Confirm before fixing:** Reproduce or refute the concern on the exact candidate and actual registration entry point before changing production behavior. Preserve valid Unicode names and existing empty-name rejection.

## Evidence

- **Authoritative fixture policy:** [`registration-policy.md`, lines 5–7](fixtures/docs/registration-policy.md) — empty/whitespace rejection, Unicode preservation, and registration-entry-point enforcement.
- **Inspected static code:** [`registration.py`, lines 4–7](fixtures/src/registration.py) — checks falsey strings; nonempty whitespace-only input is not visibly excluded.
- **Selected fixture tests:** [`test_registration.py`, lines 9–15](fixtures/tests/test_registration.py) — empty and Unicode test cases only; no executed result.
- **Illustrative audit finding:** [F1 in example-report.md](example-report.md) — **SUPPORTED** for selected source text, *not* a reproduced runtime defect.
- **Counterevidence / limits:** A caller could normalize names first, but the invented policy still requires the entry point to validate. No real project, full caller graph, actual environment or full test suite was inspected.
- **Existing issues:** **NOT CHECKED**. Do not publish before permitted deduplication and an explicit create authorization.

## Acceptance criteria (proposed)

- [ ] **R1:** At the signup registration entry point, reject an empty string and strings consisting only of whitespace with an observable validation failure. Source: [fixture policy, line 5](fixtures/docs/registration-policy.md).
- [ ] **R2:** Preserve the characters of nonempty Unicode usernames that otherwise satisfy the fictional policy. Source: [fixture policy, line 6](fixtures/docs/registration-policy.md).
- [ ] **R3:** Enforce R1 and R2 at `register` even without client-side validation. Source: [fixture policy, line 7](fixtures/docs/registration-policy.md).

No other features, authorization policy, username length limits or normalization strategy are proposed.

## Verification — PROPOSED — NOT RUN

1. In an **explicitly authorized isolated run**, call the real registration entry point with `""` and `"   "`. Expected from fictional policy: both are rejected; an accepted whitespace-only value would confirm the suspected failure.
2. Submit a nonempty Unicode name such as `"Åsa"`. Expected: successful registration without character changes. This detects a proposed fix that rejects valid Unicode or silently rewrites it.
3. Exercise the same entry point without UI preprocessing. Expected: the same outcomes; this detects repairs that rely solely on client validation.
4. Record the exact candidate, commands/arguments, environment, actual outputs and any limitations. **No tests have been run for this example.**

## Open decisions and evidence gaps

- Runtime behavior and isolation environment remain **UNVERIFIED**.
- The actual product's authoritative contract and whether these fixture expectations apply to it remain **UNKNOWN**.
- No real tracker duplicate search occurred; a prospective publisher must inspect open and closed issues.

**Next action:** If this were a real project, seek authorized reproduction and deduplication first. Do not automatically implement or publish a repair issue.

**Saved Intentline agreement:** NONE. **Approval:** NONE. **Issue URL:** NONE.
