## Target and method

Audited **grove/repotend @ `bfe410e4d61ddb472e335ce35877997a2f32d91f`**, read-only, using **Scout → Probe → Report**. Activated the canonical `skill:gapline-audit` by reading it first.

**Answer:** The inspected implementation supports default preview, stale-plan refusal, and exclusive creation. Explicit human approval is an agent obligation, intentionally not proved by the digest. **One supported finding** concerns the generated apply command losing the selected repository root. Complete transitive read-only behavior remains unassessed.

Provenance is operator-supplied Git-object extraction with original numbered lines and a retained SHA-256 manifest. I could not independently verify extraction, manifest, installed skill hash, or working-tree identity.

## Accepted promises and exceptions

These expectations come from documentation, separately from implementation and tests:

- Preview changes no files or directories: `docs/REMEDIATION.md:14–23`.
- The agent shows the full preview and waits for explicit approval; shell permission and a digest do not establish consent: `docs/REMEDIATION.md:29–39`; `skills/repotend/SKILL.md:37–44`.
- Apply re-audits, rejects changed plans, refuses existing destinations, and creates exclusively: `docs/REMEDIATION.md:41–49`.
- **Explicit exceptions:** partial writes can remain; application is not transactional; concurrently malicious path mutation is outside the design: `docs/REMEDIATION.md:52`. Organization defaults are not verified: line 25.
- Broader planned capabilities in `README.md:7–26` are not current promises.

## Finding G1 — Suggested apply command drops the target root

**Category:** interface/documentation consistency  
**Evidence:** **SUPPORTED** source observation; runtime consequence unverified  
**Priority:** Medium — a user following the preview’s command could create files in a different repository.

**Expected:** Apply the reviewed plan to the same selected repository. The agent workflow explicitly requires the same root (`skills/repotend/SKILL.md:38–41`), and documented manual apply includes `--root` (`docs/REMEDIATION.md:31–35`).

**Supporting evidence:**

- Markdown rendering suggests an apply command without `--root`: `skills/repotend/scripts/remediation.ts:181–184`.
- The CLI defaults the root to `process.cwd()`: `skills/repotend/scripts/remediate-cli.ts:5–16`.
- The digest includes rule IDs, paths, and contents, but no repository identity: `skills/repotend/scripts/remediation.ts:53–55`.
- Consequently, another repository with identical eligible additions can produce the same digest; the stale-plan comparison alone cannot distinguish those repositories (`remediation.ts:118–120`).

**Counterevidence and limits:** The documented command and agent workflow preserve the root. Running from the target repository also avoids this mismatch. Existing destination checks still prevent overwriting. The inspected CLI test always supplies `--root`, so it does not distinguish this case (`test/remediation.test.mjs:126–143`). No wrong-target write was observed.

**Smallest next action:** Carry the selected root into the rendered command.

**PROPOSED — NOT RUN:** Preview repository A while the caller’s working directory is repository B, with identical missing-file proposals. Follow the rendered command. Creation in B supports the concern; targeting A or refusing before writes refutes it.

## Other leads: supporting evidence and counterevidence

| Lead | Inspected implementation | Inspected test assertions | Conclusion |
|---|---|---|---|
| Preview and approval | Preview plans through audit/probes; CLI applies only with an argument (`remediation.ts:65–79`; `remediate-cli.ts:9–17`). Consent is explicitly delegated to the agent. | Directory contents unchanged after preview; missing apply ID rejected (`test/remediation.test.mjs:20–33,126–143`). | No supported approval-bypass finding. Human compliance was not observed. |
| Stale plans | Fresh planning and digest comparison precede destination preflight and writes (`remediation.ts:115–127`). | Replay and newly introduced destination rejected; existing content preserved (`test/remediation.test.mjs:35–59`). | Concern withdrawn within the documented content-based plan contract. |
| Overwriting | Fixed allowlist, destination `lstat`, parent checks, exclusive open, and verification (`remediation.ts:8–21,91–112,121–165`). Reader treats symlinks/non-files as unknown (`engine.ts:52–72`). | Symlink and alternate-template preservation assertions (`test/remediation.test.mjs:61–93`). | No supported overwrite finding within the stated concurrency exception. |

These are source and test-oracle observations, **not passing test results**.

## Inspection, boundaries, and omissions

**11 source reads:** canonical skill plus all ten permitted repository files: the three initial files, `remediate-cli.ts`, `remediate.mjs`, `engine.ts`, `config.ts`, repository `SKILL.md`, `package.json`, and `README.md`. Three leads; one finding; no delegation.

Actual tools used: `functions.exec` for metadata discovery and source-reader orchestration, and `mcp__independent_source__read_source`. No shell commands.

**Additional exposed capabilities:** the host advertised orchestration, collaboration, input, clock, and other tool metadata despite the stated source-reader-only setup. None was invoked beyond the orchestration wrapper needed to discover and call the reader. Their effective availability and enforcement were not tested.

**Project code, tests, and builds executed: NONE.** No writes, network access, publication, tracker activity, or saved agreement. Duplicates were not checked.

Inspection stopped at unavailable transitive context: `engine.ts:4,168` imports and registers `workflows.ts`, which was not permitted. Its behavior prevents complete assurance that the entire preview call graph is read-only and executes no target code. Installation, live agent approval behavior, referenced validation receipts, filesystem races, and platform behavior were also unassessed.

**Outcome: one supported finding; no runtime failure demonstrated.**