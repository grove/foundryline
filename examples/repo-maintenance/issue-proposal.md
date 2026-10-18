# Decide whether to add a short contribution guide

**NOT PUBLISHED — authored decision proposal from real audit evidence.**
Issue URL: **NONE**. Approval: **NONE**. Saved Intentline agreement: **NONE**.

Foundryline invites people to try its recipes and contribute, but its pinned
checkout has no recognized contribution guide. A small guide could help someone
prepare a documentation change and find the reference checks. Decide whether
this is useful before adding a new file; the existing README may be enough.

## Evidence

- Actual RepoTend `repo.contributing` version 2: **WARN**, `confidence: verified`,
  `enforced: false`; [raw JSON](receipts/audit-json/report.json). The verified fact
  is absence at the six recognized paths, not a broken contributor workflow.
- Original project context: the pinned [README's invitation](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/README.md#want-to-help)
  asks for recipe trials, confusing steps, useful/no-findings results and issue
  suggestions. It does **not** require a CONTRIBUTING file. This is an optional
  improvement proposal, not an accepted unmet requirement.
- Preservation constraint: [design principles](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/DESIGN.md)
  keep effects separately authorized and evidence honest. Contribution instructions
  should preserve unpublished drafts and proposed-versus-executed checks.
- Existing [reference workflow](https://github.com/grove/foundryline/blob/5dc1dd15836584a1112caec224d479df8deffc9f/.github/workflows/reference-checks.yml)
  runs `python3 -m unittest discover -s checks -v`. These checks validate local
  artifacts, not universal agent safety or target runtime behavior.
- Counterevidence: README already welcomes contributions and links the guides;
  no contributor failure was observed. Inherited community defaults were not
  inspected. Priority: **low / proposed P3**, a discoverability improvement,
  with no demonstrated outage or security impact.
- The [triage record and duplicate lookup](README.md) found no equivalent task
  among four open/closed issues and nine open/closed PRs at lookup time.
  This was not a comments/discussions search; repeat before publication.

## Acceptance criteria (proposed)

- [ ] **R1:** Decide whether existing README guidance suffices. If yes, retain the
  no-action rationale; no new file is required to satisfy an auditor warning.
- [ ] **R2:** If a guide is wanted, provide one short, linked contribution entry
  explaining the existing recipe/example workflow and reference-check command,
  without introducing a service, mandatory model, or automatic issue publication.
- [ ] **R3:** Preserve the project's distinction between authored examples, actual
  receipts, unpublished proposals, and checks that have not been run.

## Verification — PROPOSED — NOT RUN

1. Recheck current source, inherited guidance and existing issues/PRs. Record the
   maintainer's decision; if README suffices, record no action rather than a fix.
2. If adding a guide, follow its links and check command in a fresh Foundryline
   checkout. Confirm a new contributor can locate the existing examples and tests.
3. Review the prose against the design's effect boundaries and evidence labels;
   ensure it does not claim automated or broad host qualification.

These are future checks for this proposal, separate from the audit already run.

## Open decisions and evidence gaps

Whether a dedicated guide is useful remains a maintainer decision. No contributor
usability study or organization-default inspection was performed. A report and
this draft grant no permission to publish an issue or implement its suggestion.
