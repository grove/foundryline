# Evidence and decision handoff

Optional summary for Discover, Maintain or Deliver. Copy, omit inapplicable fields
and link existing receipts. See
[completed small samples](../examples/evidence-handoff-samples.md).
Complements the [detailed Discover record](../examples/manual-discover/run-record-template.md);
no required stage, workspace format, status schema or orchestrator.

## Copy and fill

**BLANK TEMPLATE — NO RUN EVIDENCE.**

- **Identity:** date/timezone, recipe, operator, repository, full commit/tree,
  paths, dirty/untracked inputs or **UNKNOWN**; revisions not covered.
- **Request and authority:** complete original request/policy link, exceptions,
  scope/question. Separate authorizations for reads, execution,
  storage, edits and publication; identify authorizer and exact effect.
- **Actually used:** host/version, tool/skill revision, activation evidence versus
  manual guidance; time/usage/cost or **UNAVAILABLE**, unknown identities,
  enforced controls and visibility limits.
- **Activity:** link exact argv/cwd, selected check indices/requirement maps,
  reads, stdout/stderr, exits, unexpected effects and negative controls.

| R / check / finding + source | Actual observation and retained receipt | Limit / next decision |
| --- | --- | --- |
| <source-bound item; no invented obligations> | <outcome, exit if applicable, link> | <unproven scope, owner/action> |

- **Publication and approvals:** **NOT PUBLISHED** until verified; then
  URL/ref and authorizing instruction. Record actual approval/acceptance
  separately from recommendations, drafts and check success.
- **Retention:** evidence location, relevant hashes, expiry/access limits;
  permission/destination for preservation. No automatic upload.

Plain descriptions: **OBSERVED PASS** for an observed check;
**FAILED** for a failed attempt (explain whether a product assertion ran);
**UNAVAILABLE** for missing execution/source; **NOT DEMONSTRATED** for an
unsupported obligation; **PROPOSED — NOT RUN** for future work; **UNKNOWN** for
missing facts. Preserve native wording. No global green score or inferred approval.

For low-risk work, text, links and hashes suffice. Retain complete native
receipts/source-bound exports where needed for material claims/refusals.
GitHub Actions artifacts expire: preserve critical evidence durably
**when authorized**, recording hashes and provenance. A hash
checks identity, not truth or consent. Review privacy/access before sharing;
keep credentials/private sources out of public Git and avoid unnecessary
megabytes. Record storage needs destination authority; Discover's read-only
audit itself does not authorize writes.
