"""Structural guards for the manual GitHub Actions Maintain example.

These checks NEVER launch GitHub Actions, RepoTend or target project code.
Passing cannot qualify a runner, agent, artifact or manual dispatch.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/maintain-audit.yml"
GUIDE = ROOT / "docs/manual-intake.md"


class ManualMaintainActionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.guide = GUIDE.read_text(encoding="utf-8")

    def test_real_manual_entry_with_only_narrow_pr_trigger(self):
        self.assertIn("\non:\n  workflow_dispatch:\n  pull_request:\n    paths:\n", self.workflow)
        for forbidden in ("\n  schedule:", "\n  push:", "\n  issues:", "\n  workflow_run:"):
            self.assertNotIn(forbidden, self.workflow)
        self.assertIn('".github/workflows/maintain-audit.yml"', self.workflow)

    def test_read_only_token_and_trusted_pinned_dependencies(self):
        self.assertIn("\npermissions:\n  contents: read\n", self.workflow)
        self.assertNotIn("contents: write", self.workflow)
        self.assertNotIn("issues: write", self.workflow)
        self.assertEqual(self.workflow.count("persist-credentials: false"), 2)
        refs = re.findall(r"^\s*uses: (actions/[\w-]+)@([a-f0-9]{40})", self.workflow, re.M)
        self.assertEqual(len(refs), 4)
        self.assertEqual([name for name, _ in refs].count("actions/checkout"), 2)
        self.assertIn(("actions/setup-node", "49933ea5288caeca8642d1e84afbd3f7d6820020"), refs)
        self.assertIn(("actions/upload-artifact", "ea165f8d65b6e75b540449e92b4886f43607fa02"), refs)
        self.assertIn("2d69cce901475380775f674b9cc5755f1f89f82e", self.workflow)
        self.assertIn('node-version: "22.20.0"', self.workflow)
        self.assertIn("npm ci --ignore-scripts --no-audit --no-fund", self.workflow)

    def test_real_audit_and_missing_source_failure_are_wired(self):
        self.assertIn("path: target", self.workflow)
        self.assertIn("path: tool", self.workflow)
        self.assertIn("ref: ${{ github.sha }}", self.workflow)
        self.assertIn('node skills/repotend/scripts/audit.mjs --root "$TARGET_DIR" --format json', self.workflow)
        self.assertIn('node skills/repotend/scripts/audit.mjs --root "$REPORT_DIR/absent-target" --format json', self.workflow)
        self.assertIn('if negative_exit != 2', self.workflow)
        self.assertIn('if audit_exit not in (0, 1)', self.workflow)
        self.assertIn('if report.get("errors") != []', self.workflow)
        self.assertIn("UNAVAILABLE / INCOMPLETE", self.workflow)
        self.assertIn("target-status.before", self.workflow)
        self.assertIn("target-status.after", self.workflow)
        self.assertNotIn("remediate.mjs --apply", self.workflow)
        self.assertNotIn("gh issue create", self.workflow)

    def test_real_artifacts_and_no_false_qualification(self):
        self.assertIn("actions/upload-artifact@", self.workflow)
        self.assertIn("if: always()", self.workflow)
        self.assertIn("retention-days: 7", self.workflow)
        self.assertIn("identity.json", self.workflow)
        self.assertIn("negative.stderr", self.workflow)
        self.assertIn("report.json", self.workflow)
        self.assertIn("NOT YET VERIFIED", self.guide)
        self.assertIn("Run workflow", self.guide)
        self.assertIn("no target repository dependencies", self.guide.lower())
        self.assertIn("**Privacy:**", self.guide)


if __name__ == "__main__":
    unittest.main()
