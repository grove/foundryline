# Signup username policy — fictional fixture

**AUTHORED FIXTURE:** This policy is invented solely for Foundryline's teaching example, not an actual product decision.

In the interactive signup flow, reject usernames that are empty or contain only whitespace.
Accept nonempty Unicode usernames without modifying their characters.
The `register` entry point must enforce those checks even if client-side validation is skipped.

Scope: signup registration only; behavior of sign-in and profile edits is not specified.
