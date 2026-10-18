## RepoTend repository audit (experimental)

> Checks are advisory unless explicitly enforced. A PASS is not a complete security or quality certification.

**6 passed · 7 warnings · 0 enforced failures · 0 suppressed · 0 unknown · 0 not applicable**

| Status | Rule | Observation |
| --- | --- | --- |
| PASS | `repo.license-present` | License is present |
| WARN | `repo.contributing` | Contribution guide was not found |
| WARN | `repo.code-of-conduct` | Code of conduct was not found |
| WARN | `repo.security-policy` | Security policy was not found |
| WARN | `repo.pr-template` | Pull request template was not found |
| WARN | `repo.issue-templates` | No issue templates found |
| WARN | `dx.editorconfig` | EditorConfig was not found |
| PASS | `ci.workflow-validity` | Workflow YAML and basic required structure are valid |
| PASS | `security.workflow-permissions` | An explicit token permissions policy applies to each job |
| WARN | `ci.concurrency` | PR workflows may run superseded jobs without cancellation |
| PASS | `ci.duplicate-triggers` | No obvious overlapping push and pull_request triggers found |
| PASS | `ci.path-filter-safety` | No event-level workflow path filters detected |
| PASS | `security.action-pinning` | External action references are pinned to full SHAs or use local paths |

See docs/DOGFOODING.md for check limitations.
