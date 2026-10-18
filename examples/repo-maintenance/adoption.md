# Adoption attempt — separate agent, shared host

**Executed, 2026-10-18 UTC.** A separately tasked Codex agent
(`/root/maintain_adoption`) followed [the Maintain guide](../../patterns/maintain.md)
using a new public tool checkout, target checkout, installed dependencies, and npm
cache in `/private/tmp/foundryline-maintain-adoption-1ib6ldm1`. It did not reuse the
reference run's work directory or installed tool. The initiating human, host,
account, network, and runtimes were shared; this is an agent adoption attempt,
not independent administration or evidence from a second operating system.

The observed effort interval was **112.209 seconds**, from 08:15:52 UTC to
08:17:44.208664 UTC, including setup, inspection, execution, and receipt validation.
Initial guide reading preceded the first observed clock and is additional untimed
effort; writing these notes followed the interval. Captured subprocess time totaled
7.693 seconds; the JSON and Markdown audits took 0.220 and 0.194 seconds.

The tool was RepoTend `2d69cce901475380775f674b9cc5755f1f89f82e`; the public target
was Foundryline `5dc1dd15836584a1112caec224d479df8deffc9f`. The tool lockfile SHA-256
was `f17806903690e3f2058655ff974ed45a27ee894cceccd8f54ac50e8c8108d0b6`, unchanged
after installation and audit. The host used Darwin 25.6.0 arm64, Node v26.12.0,
npm 11.20.0, Git 2.54.0, and Python 3.15.0 for temporary output capture.

Both auditor invocations completed with exit **0**, empty stderr, **6 PASS and
7 WARN**, no enforced failures, and `errors: []`. The target had no `.repotend.yml`;
Git status was empty before and after. The missing-path negative control exited
**2**, emitted an ENOENT diagnostic and zero stdout bytes, and remained missing.
It is **UNAVAILABLE**, not a completed audit or PASS. No issue was produced.

The guide was sufficient to install and run without changing target source or
configuration. Operator choices/deviations were:

- Used a uniquely named temporary directory rather than literal `maintain-work`.
- Added a private temporary `--cache` directory to the documented `npm ci`
  command, avoiding reuse of the reference run's dependency cache.
- Captured argv, cwd, stdout, stderr, exits, timestamps, and durations with a
  temporary Python subprocess helper instead of shell redirection. The outputs
  are genuine separate invocations, with no report rewriting.
- Inspected the pinned package manifest/lockfile and audit entrypoint, CLI, and
  engine before running the auditor. “Inspect/trust” does not define an exhaustive
  supply-chain review; this attempt did not perform one.

[Receipts](receipts/adoption/sha256.json) retain every captured command in
[commands.jsonl](receipts/adoption/commands.jsonl), the unedited
[JSON](receipts/adoption/report.json) and [Markdown](receipts/adoption/report.md),
stderr/exits, environment, before/after identities and statuses, and file digests.
[attempt.json](receipts/adoption/attempt.json) records timing and scope.

No target dependencies, hooks, builds, package scripts, or remediation were run;
there were no GitHub writes. Setup used network access to clone public source and
install pinned tool dependencies with install scripts disabled. The audit ran in
the host's ordinary restricted execution environment; source inspection and clean
Git status support the observed read-only result but do not establish a universal
filesystem/network sandbox or detect every possible side effect. Organization
defaults, branch protection, runtime behavior, other hosts, and duplicate issue/PR
lookup were **NOT CHECKED** by this adoption task. Triage and publication remain
separate decisions.
