# Small evidence and decision handoffs

Completed summaries of **historical retained evidence**, using the optional
[shared template](../docs/evidence-handoff-template.md). These samples add no live
recipe execution, approval or upload. Detailed records
remain authoritative for their observations; their later scope decisions do not
rewrite historical failures.

## Discover

- **Identity:** 2026-10-18 Europe/Oslo (receipts: 2026-10-17 UTC); coordinating
  Codex agent; `grove/repotend@bfe410e4d61ddb472e335ce35877997a2f32d91f`.
  Ten Git-object source files, [hashes/scope](repotend-pilot/receipts/source-manifest.json);
  no target working tree, no claim about developer dirty files or current main.
- **Request/authority:** [Foundryline #4](https://github.com/grove/foundryline/issues/4),
  inspect remediation preview/approval/root safety. [Original policy and exceptions](repotend-pilot/issue-proposal.md#evidence)
  require the same approved plan/root; digest is not consent and writes are not
  transactional. Audit permitted source reads only; setup, tracker lookup and
  record storage were separate operator actions. No target execution or tracker writes.
- **Actually used:** macOS, Codex CLI `0.163.0`, explicitly activated installed
  Gapline `bd6a1dea3677482e2d4a305a5bf8084cb3c95e69`; Intentline
  `25e926f57e69395193fc0ac258f9e6dd2332cb18` drafting guidance only.
  [Exact launcher argv](repotend-pilot/receipts/pilot/command.json),
  [events](repotend-pilot/receipts/pilot/events.jsonl) and
  [measurements](repotend-pilot/receipts/pilot/measurement.json): 11 source calls,
  exit 0, 48.390 s. Read-only/no-shell settings and bounded reader observed;
  wrapper/OS/provider visibility incomplete. Exact model and billing **UNAVAILABLE**.

| R / check / finding + source | Actual observation and retained receipt | Limit / next decision |
| --- | --- | --- |
| Root-preserving preview, pinned policy above | **SUPPORTED**, renderer omits root; [report](repotend-pilot/receipts/pilot/report.md). Docs and JSON guidance already retain root. | Runtime wrong-root write **NOT DEMONSTRATED**; confirm before fixing, **PROPOSED — NOT RUN**. |
| Read-only activity | Events contain source reads, no project runs/writes; [fresh reproduction](repotend-pilot/receipts/reproduction/measurement.json) exit 0. | Same operator/provider; not independent administration or complete host isolation. |
| Missing-source control | **UNAVAILABLE**, zero findings; [negative response](repotend-pilot/receipts/negative/report.md), [process exit 0](repotend-pilot/receipts/negative/measurement.json). | Process completion is not a successful audit. |
| Initial launch | **FAILED**, exit 1, [startup error](repotend-pilot/receipts/failed-launch/stderr.txt). | No model turn or product assertion ran. |

- **Publication/approvals:** RepoTend [proposal](repotend-pilot/issue-proposal.md)
  **NOT PUBLISHED**; no issue approval or saved agreement. The
  [full record](repotend-pilot/README.md) attributes Foundryline record publication
  to a separately requested PR; exact authorizer/transcript **UNKNOWN** in retained
  receipts. Later [maintainer scoped acceptance](../docs/discover-v0.1-qualification-review.md)
  is a separate decision, not authority to publish the RepoTend issue.
- **Retention:** public commands/events/reports and source hashes retained in Git;
  no expiring Actions dependency for this pilot. Transitive `workflows.ts`, runtime
  behavior and current tracker completeness remain unassessed; see full record.

## Maintain

- **Identity:** 2026-10-18 Europe/Oslo, Codex operator;
  `grove/foundryline@5dc1dd15836584a1112caec224d479df8deffc9f`, fresh detached
  checkout. [Environment and 48 file hashes/modes](repo-maintenance/receipts/environment.json)
  matched before/after; this excludes `.git` and does not cover the later PR tree.
- **Request/authority:** [Foundryline #10](https://github.com/grove/foundryline/issues/10),
  finite read-only maintenance audit and unpublished triage. The
  [pinned README/design context](repo-maintenance/issue-proposal.md#evidence)
  invites contributions but does not require CONTRIBUTING. Separate tool setup
  and outside-target report writes; no target installs/tests, remediation,
  settings access or GitHub writes during audit.
- **Actually used:** RepoTend `2d69cce901475380775f674b9cc5755f1f89f82e`, report
  version `0.1.0`, default advisory `small-oss` profile; macOS/Darwin 25.6.0 arm64,
  Node `v26.12.0`, npm `11.20.0`. Direct deterministic auditor; no model or native
  skill-activation claim. [JSON argv/cwd/exits/stream hashes](repo-maintenance/receipts/audit-json/command.json)
  and [Markdown command](repo-maintenance/receipts/audit-markdown/command.json)
  both exit 0; target files unchanged is not syscall-level isolation evidence.

| R / check / finding + source | Actual observation and retained receipt | Limit / next decision |
| --- | --- | --- |
| Finite 13-rule audit | **OBSERVED PASS** for process completion only, 6 PASS / 7 WARN in [raw report](repo-maintenance/receipts/audit-json/report.json). | Advisory findings, some heuristic; no overall health/security approval. |
| `repo.contributing`, README context above | WARN / verified absence; [triage](repo-maintenance/README.md#results-and-triage) says NEEDS_DECISION. | README already welcomes contributions; maintainer decides whether a guide helps. |
| Missing-target control | **UNAVAILABLE / INCOMPLETE**, [exact command](repo-maintenance/receipts/missing-target/command.json) exit 2, ENOENT, empty stdout; no report. | Never a clean audit; no fallback target or resulting issue. |

- **Publication/approvals:** maintenance [proposal](repo-maintenance/issue-proposal.md)
  **NOT PUBLISHED**, approval **NONE**. Exact authorization for historical
  record-PR publication is **UNKNOWN** in these receipts; the
  [full audit](repo-maintenance/README.md) and later
  [project-direction acceptance](../docs/maintain-v0.2-qualification-review.md)
  do not authorize fixes or publication of this proposal. Next: decide or defer.
- **Retention:** small text/JSON reports and command-bound SHA-256s already in Git;
  no archive needed for this sample. No Actions expiry dependency. Settings,
  inherited community defaults and target runtime behavior remain **UNKNOWN**.

## Deliver

- **Identity:** 2026-10-18 Europe/Oslo, OpenAI Codex coding agent;
  `grove/foundryline@f54d44eb1d21fae2d7cfd8aae4216e91019a87d3`, tree
  `a003d013419fd1f142f0d05175938c6b0d7008f3`; native snapshot commit
  `191c64bf4d7c785a668b5d035e8063dd257b7244`, same tree. Native evidence excludes
  later evidence/status commits and any unknown dirty inputs; exact model build
  and coding cost **UNAVAILABLE**.
- **Request/authority:** complete [issue #21 S1](manual-deliver/intentline-trace/export/source-S1.txt),
  [captured issue](manual-deliver/intentline-trace/issue-21.json) and
  [user instruction transcription](manual-deliver/intentline-trace/authorization.txt)
  authorize implementing #21 and creating a PR, including its bounded native checks.
  Transcription is not authenticated approval. No merge/deploy/schedule authority.
- **Actually used:** Intentline `25e926f57e69395193fc0ac258f9e6dd2332cb18`
  CLI prepare/propose/check/review/render/export, all exit 0; advisory/unapproved
  export, no adoption. Proofline `8e117fff4de2459637fe7f74f47ab17fc3341d84`
  native check-only on GitHub macOS 15.7.9 ARM64, Python 3.12.10, Codex CLI
  `0.162.1`, zero check-model calls. No inferred skill activation from CLI use.
  [Full expanded argv/cwd/exits](manual-deliver/intentline-trace/verification.json)
  and [exact selections](manual-deliver/intentline-trace/README.md#exact-selections-and-observed-gap)
  distinguish SOURCE (citation test) and EXPORT (export-integrity test).

| R / check / finding + source | Actual observation and retained receipt | Limit / next decision |
| --- | --- | --- |
| S1:36, R1 | **OBSERVED PASS**, SOURCE index 0 in [gap map](manual-deliver/intentline-trace/gap-links.json), CHECKS PASSED, exit 0. | Limited issue-byte/citation evidence, not authenticated provenance. |
| S1:37, R2 | **NOT DEMONSTRATED** in gap record; expanded [checks](manual-deliver/intentline-trace/linked-checks.json)/[map](manual-deliver/intentline-trace/linked-links.json) add EXPORT index 1; CHECKS PASSED, exit 0. | Same candidate/export, limited integrity evidence; earlier gap stays visible. |
| S1:38–42, R3–R7 | Unlinked, **NOT DEMONSTRATED** by selected checks; [full evidence table](manual-deliver/intentline-trace/README.md#maintainer-handoff-original-request--implementation--evidence). | Raw observations/review separate; `coverage_completeness: UNKNOWN`. No global acceptance. |
| Mismatched argv / local boundary | Import rejected, exit 1 (no report); local **EXECUTION UNAVAILABLE**, exit 2 (no selected check ran). [Raw negatives and limits](manual-deliver/intentline-trace/README.md#actual-refusal-and-counterevidence). | Refusals, not product-test failures; successful remote host does not qualify local host. |

- **Publication/approvals:** historical [PR #22](https://github.com/grove/foundryline/pull/22)
  published under the user's transcribed instruction above. Agent review shared
  operator/provider and was not maintainer approval. Later
  [scoped acceptance](../docs/deliver-v0.2-qualification-review.md) is separate;
  native check success supplied no publication/merge permission.
- **Retention:** [original producer/export/native/refusal archives and hashes](manual-deliver/intentline-trace/README.md#raw-records-review-and-limits)
  retained durably in Git for this authorized evidence task. Native ZIP SHA-256
  `278ba30ee5ec16aca688616eebb7c5d670d6ea5d7aaaa6e0f32fe5c277e246cd`;
  original Actions artifact expires October 25, 2026. No new archive/upload here.
  Native boundary observations are narrow; review full receipts before decisions.

For any new handoff, use proportional retention and privacy/access boundaries
in the shared template; these public historical records are not permission to
publish another project's private source or credentials.
