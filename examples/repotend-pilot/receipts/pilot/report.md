RepoTend’s inspected source supports the main safeguards, with **one supported finding**: the Markdown preview can suggest applying to a different repository. Full preview read-only behavior remains **not assessed** because an imported module is unavailable.

**Target and method**

Audited `grove/repotend` at `bfe410e4d61ddb472e335ce35877997a2f32d91f`, using Scout → Probe → Report and three leads: preview/approval, stale plans, and overwrite protection.

Activated the canonical installed skill by first reading `skill:gapline-audit`. Its supplied provenance is `grove/gapline` at `bd6a1dea3677482e2d4a305a5bf8084cb3c95e69`, with the supplied SKILL.md SHA-256. Neither that provenance nor the operator’s Git-object extraction and retained manifest was independently verified. No working tree was inspected or substituted.

**Accepted promises and exceptions**

- Preview creates no directories or files; apply requires review and explicit approval: `docs/REMEDIATION.md:23–39`.
- Apply re-audits, rejects stale plans, and refuses existing destinations: `docs/REMEDIATION.md:41–49`.
- Consent is an agent obligation, not something the digest proves: `skills/repotend/SKILL.md:37–44`.
- Explicit exceptions include partial writes, no filesystem transaction, and no defense against malicious concurrent path-component changes: `docs/REMEDIATION.md:52`. Organization defaults are not verified: line 25.

**F1 — Suggested apply command loses the selected target**

**SUPPORTED · Medium impact · Interface/approval boundary**

The skill requires applying with the **same reviewed plan ID and target root** (`skills/repotend/SKILL.md:38–42`). However:

- Markdown rendering suggests `node skills/repotend/scripts/remediate.mjs --apply <digest>` without `--root` (`skills/repotend/scripts/remediation.ts:181–184`).
- The CLI defaults the root to the current directory (`skills/repotend/scripts/remediate-cli.ts:5,11,16`).
- The digest covers only rule IDs, paths, and contents—not repository identity (`skills/repotend/scripts/remediation.ts:53–55`).

Consequently, copying that command after previewing another root can select the current directory. A different repository with identical proposals can satisfy the digest check.

**Counterevidence:** the documented apply example includes `--root` (`docs/REMEDIATION.md:31–35`), and the agent skill explicitly preserves it. Different proposal sets are rejected by the digest comparison (`remediation.ts:119–120`). Existing-file protections still apply. This finding concerns the generated command, not those protections.

**Next action:** preserve the selected absolute root in the suggested command, or require callers to supply it explicitly.

**PROPOSED — NOT RUN:** preview repository A from tool checkout B, arranging identical supported proposals in both; inspect and follow the rendered command in a disposable environment. Writing B would support the concern; targeting A or refusing the ambiguous invocation would refute it. No runtime failure was demonstrated.

**Other leads and counterevidence**

- **Preview and approval — partially supported.** The CLI selects planning unless `--apply` has a value (`remediate-cli.ts:7–16`). Planning contains no direct writes (`remediation.ts:65–79`). The skill requires complete diffs, explicit approval, and waiting; denial prohibits alternate edits (`skills/repotend/SKILL.md:31–44`). Lack of an interactive CLI consent prompt is consistent with the documented separation of digest and consent. Actual agent compliance was not validated.
- **Stale plans — supported in inspected source.** Apply regenerates the plan and compares its digest before writes (`remediation.ts:115–127`). Selected tests assert stale replay rejection and preservation of a newly introduced destination (`test/remediation.test.mjs:35–59`). These are source assertions, not passing-run evidence. The digest tracks proposed changes, not every repository-state change.
- **Overwrite protection — supported in inspected source.** Destination inspection rejects existing entries and unsuitable parents; apply rechecks and opens with `O_EXCL` and optional `O_NOFOLLOW` (`remediation.ts:91–112,142–154`). Reader inspection rejects detected symlinks and treats non-files as unknown (`engine.ts:52–73`). Selected tests assert preservation of symlink targets and alternate templates (`test/remediation.test.mjs:61–93`). Concurrent malicious mutation is an explicit exception, not a finding.

**Inspection and limits**

Used only `functions.exec` as a tool-discovery/orchestration wrapper and `mcp__pinned_source__read_source`: **11 source reads**, including the skill. Inspected all ten permitted project sources: the three initial files, both launchers, `engine.ts`, `config.ts`, the RepoTend skill, `package.json`, and `README.md`. No delegation.

**Project code, tests, and builds executed: NONE.** No filesystem writes, network access, publication, tracker operations, or saved agreement.

`engine.ts:4,168` imports/registers unavailable `workflows.ts`. Inspection stopped at that necessary boundary; full transitive read-only/no-target-code behavior cannot be established. Installation, audit entrypoint, live-agent validation receipts, other tests, and platform behavior were unavailable or unassessed. Duplicate checking was not performed.

Additional capabilities were visibly exposed: orchestration helpers, resource/goal tools, user-input tools, clock tools, and collaboration controls. None were invoked beyond the orchestration wrapper needed to discover and call the source reader. Their enforcement boundaries were not tested.

**Outcome:** one supported source-level finding; no demonstrated runtime failures. The remaining inspected safeguards align with the documented promises and explicit exceptions, within the stated omissions.