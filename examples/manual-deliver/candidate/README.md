# Authored username-validation candidate

This is a tiny, **deliberately authored** teaching example, not a recorded
coding-agent implementation or a successful Proofline check. The two-line
[original request](../original-request.md) is the only behavior source.

The function rejects blank strings and returns valid nonblank strings without
normalization. The two ordinary Python unit tests exercise the two distinct
source obligations. You can run the whole suite from this `candidate/` directory:

```sh
python3 -B -m unittest discover -s tests -v
```

For the **selected** Proofline command in the [Deliver guide](../../../patterns/deliver.md),
only the R1 test is selected:

```sh
python3 -B -m unittest tests.test_username_validation.UsernameValidationTests.test_rejects_blank
```

Even if that one check passes, R2 is **NOT DEMONSTRATED by the selected
Proofline evidence**. A separate ordinary CI execution of both authored tests
does not change the evidence from a different, explicitly selected Proofline
command.

Proofline requires a real Git repository root. The source tree here is nested
in Foundryline; for the guide's disposable standalone candidate, copy the
`candidate/` directory into a fresh local Git repository before checking.
