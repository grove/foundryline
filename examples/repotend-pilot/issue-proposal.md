# Preserve the selected repository in remediation preview's apply instructions

**NOT PUBLISHED — provisional RepoTend issue proposal.** No issue URL or saved
Intentline agreement exists. Evidence: **SUPPORTED**, from pinned source only.

When someone previews fixes for a repository using `--root`, the Markdown output
suggests an apply command that drops that option. Following it could target the
caller's current directory instead. If both repositories need the same additions,
the reviewed content digest would not distinguish them. No wrong-target write has
been reproduced; the documented manual command and agent workflow keep the root.

**Confirm before fixing:** Confirm or refute this concern on current code using
the disposable, separately authorized check below before changing production behavior.

## Evidence

Pinned investigation: `grove/repotend@bfe410e4d61ddb472e335ce35877997a2f32d91f`.

- Original behavioral support: the [agent skill, lines 37–44](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/SKILL.md#L37)
  requires approval of the plan and applying with the same target root.
  The [manual instructions, lines 29–39](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/docs/REMEDIATION.md#L29)
  preserve `--root` and explicitly distinguish content consistency from consent.
- The [renderer, lines 181–184](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediation.ts#L181)
  omits `--root`. The [CLI, lines 5–16](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediate-cli.ts#L5)
  defaults to the current directory. The [digest, lines 53–55](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/skills/repotend/scripts/remediation.ts#L53)
  binds proposed rule IDs, paths and content, as documented, rather than a root.
- Counterevidence: the documented command and JSON-based skill workflow already
  retain the root; unequal proposal sets fail the stale-plan check. Selected
  [CLI tests, lines 126–143](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/test/remediation.test.mjs#L126)
  always supply `--root`. No test was executed and no whole-suite gap is claimed.
- Duplicate search: all returned open/closed issues (limit 200) yielded only
  closed [#7](https://github.com/grove/repotend/issues/7), about real-agent
  integration. No obvious duplicate in that inventory; PRs/discussions,
  inaccessible/deleted items and subsequent changes were not searched.

## Acceptance criteria (proposed)

- [ ] **R1:** After previewing a selected repository, the generated apply
  instructions retain that target or explicitly require it before a runnable
  command is offered. The selected repository must not silently become the
  caller's current directory. Basis: the same-root skill promise and documented
  manual command cited above. No particular digest or repair design is required.
- [ ] **R2:** Preserve read-only previews, explicit approval of the same reviewed
  content, stale-plan refusal, and protection of existing files, within the
  [documented scope and exceptions, lines 41–53](https://github.com/grove/repotend/blob/bfe410e4d61ddb472e335ce35877997a2f32d91f/docs/REMEDIATION.md#L41).
  This does not add transactionality, consent detection by a digest, or protection
  against malicious concurrent path mutation.

## Verification — PROPOSED — NOT RUN

1. Record the tested revision, local changes, runtime/platform and actual launch
   path. Use two disposable repositories A and B outside the real tool checkout.
   Give A and B identical eligible missing-file proposals. Arrange the generated
   relative tool path to resolve in B, for example by exposing the trusted tool
   scripts there; record that setup. Otherwise a missing script or dependency
   merely masks the concern. Do not insert a proposed repair into the reproducer.
2. From B, preview A with an absolute `--root` and inspect the Markdown apply
   instructions. Only in a separately authorized fixture run, approve and follow
   those instructions. Independently expect A to receive the reviewed additions
   and B to retain its prior contents, or an explicit refusal before any write.
   A write in B supports the concern. Targeting A or refusing ambiguity weakens
   or refutes it. A startup error, unequal proposal set, or skipped apply is
   **inconclusive**, not refutation.
3. If **confirmed**, retain the runtime evidence, repair within authorized scope,
   and keep a regression for R1. If **refuted/already fixed**, record counterevidence
   and recommend correcting or closing the proposal. If **inconclusive**, record
   the missing observation and keep the concern unconfirmed.
4. Under separate execution authorization, use the existing preview, approval-ID,
   stale-plan and existing-file scenarios as regression observations for R2.
   Independently compare before/after contents and intended root. The selected
   source assertions are not passing-run receipts.

## Open decisions and evidence gaps

Current-main behavior, the wrong-root runtime path and a concrete fixture launch
are unverified. Human approval compliance and complete transitive preview behavior
were not assessed; `workflows.ts` was unavailable in the pilot. The next action
is confirmation, not an authorized RepoTend repair or publication.
