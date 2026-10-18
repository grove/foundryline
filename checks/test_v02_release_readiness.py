"""Offline consistency checks for Foundryline v0.2 manual-only acceptance.

These tests NEVER publish a GitHub release, run a target audit or invoke an agent.
They test authored scope and retained-evidence references, not qualification.
"""

from pathlib import Path
import hashlib
import unittest


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "docs/releases/v0.2.0.md"
DELIVER = ROOT / "docs/deliver-v0.2-qualification-review.md"
MAINTAIN = ROOT / "docs/maintain-v0.2-qualification-review.md"
ROADMAP = ROOT / "IMPLEMENTATION.md"
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github/workflows/maintain-audit.yml"
ZIP = ROOT / "examples/manual-deliver/receipts/repotend-issue15-native-39123644533.zip"
ORIGINAL_ZIP_SHA256 = "31f8eb7ce91eb2a647a2e6af4e12050dddb47a3a73df619c7c24c8410c1883e8"


class ManualV02ReadinessChecks(unittest.TestCase):
    def test_acceptance_documents_and_links_are_present(self):
        for path in (RELEASE, DELIVER, MAINTAIN, ROADMAP, README, ZIP):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertTrue(path.is_file())
        readme = README.read_text()
        for path in (
            "docs/releases/v0.2.0.md",
            "docs/maintain-v0.2-qualification-review.md",
            "docs/deliver-v0.2-qualification-review.md",
        ):
            self.assertIn(path, readme)

    def test_release_records_actual_verified_publication(self):
        record = RELEASE.read_text()
        self.assertIn("**Published:** [Foundryline v0.2.0", record)
        self.assertIn("https://github.com/grove/foundryline/releases/tag/v0.2.0", record)
        self.assertIn("8409eebe0389461ec60a4bef6a5ce2aec6fb0903", record)
        self.assertIn("refs/tags/v0.2.0", record)
        self.assertIn("39127978408", record)
        self.assertIn("non-draft", record)
        self.assertIn("defers scheduling", record)
        self.assertIn("coverage_completeness: UNKNOWN", record)
        self.assertIn("v0.1.0", record)
        self.assertNotIn("RELEASE CANDIDATE NOTES — NOT TAGGED OR PUBLISHED", record)
        roadmap = ROADMAP.read_text()
        self.assertIn("v0.2.0 PUBLISHED", roadmap)
        self.assertIn("v0.1.0 and v0.2.0 are both published", roadmap)

    def test_maintain_acceptance_names_real_both_modes_and_limits(self):
        review = MAINTAIN.read_text()
        self.assertIn("ACCEPTED — NARROW MANUAL MAINTAIN", review)
        self.assertIn("39112708357", review)
        self.assertIn("workflow_dispatch", review)
        self.assertIn("39112424979", review)
        self.assertIn("6 PASS / 7 WARN", review)
        self.assertIn("5 PASS / 8 WARN", review)
        self.assertIn("UNAVAILABLE / INCOMPLETE", review)
        self.assertIn("same physical host", review.lower())
        self.assertIn("not accepted", review.lower())
        self.assertIn("not an independent", review.lower())
        self.assertIn("ACCEPTED for the observed narrow manual Maintain scope", (ROOT / "patterns/maintain.md").read_text())

    def test_deliver_acceptance_keeps_gaps_and_actual_sha(self):
        review = DELIVER.read_text()
        self.assertIn("ACCEPTED — NARROW, MANUAL DELIVER", review)
        self.assertIn("39123644533", review)
        self.assertIn("ead77fde6a5a7ba33e54cc81deb76fced8dbc333", review)
        self.assertIn("NOT DEMONSTRATED", review)
        self.assertIn("coverage_completeness: UNKNOWN", review)
        self.assertIn("f019a3927e5f4ce8a325b73edb2a28369265a95f", review)
        self.assertIn("independently administered", review)
        self.assertIn("host", review.lower())

    def test_durable_original_record_did_not_change(self):
        self.assertEqual(hashlib.sha256(ZIP.read_bytes()).hexdigest(), ORIGINAL_ZIP_SHA256)
        self.assertIn(ORIGINAL_ZIP_SHA256, DELIVER.read_text())
        self.assertIn(ORIGINAL_ZIP_SHA256, RELEASE.read_text())

    def test_first_runs_expose_inputs_pins_stops_and_permissions(self):
        readme = README.read_text()
        required = {
            "discover": ("0.163.0", "bd6a1dea3677482e2d4a305a5bf8084cb3c95e69",
                         "installed `gapline-audit`", "NOT CHECKED"),
            "maintain": ("22.16.0", "2d69cce901475380775f674b9cc5755f1f89f82e",
                         "No AI", "--root", "report.json"),
            "deliver": ("0.162.1", "8e117fff4de2459637fe7f74f47ab17fc3341d84",
                        "no saved contract", "EXECUTION UNAVAILABLE", "failed for Node"),
        }
        for recipe, tokens in required.items():
            with self.subTest(recipe=recipe):
                self.assertIn(f"patterns/{recipe}.md#first-run", readme)
                guide = (ROOT / f"patterns/{recipe}.md").read_text()
                first_run = guide.split("\n## First run\n", 1)[1].split("\n## ", 1)[0]
                for field in ("Environment", "Pinned source", "Inputs", "First action",
                              "Expected artifact", "Stop / unavailable", "Separate approval"):
                    self.assertIn(f"| {field} |", first_run)
                for token in tokens:
                    self.assertIn(token, first_run)
                self.assertIn("No prompt is an enforcement boundary", first_run)
        self.assertNotIn("skills@latest", readme + (ROOT / "patterns/discover.md").read_text())

    def test_current_acceptance_is_distinct_from_historical_handoffs(self):
        for recipe, decision in (
            ("discover", "discover-v0.1-qualification-review.md"),
            ("maintain", "maintain-v0.2-qualification-review.md"),
            ("deliver", "deliver-v0.2-qualification-review.md"),
        ):
            with self.subTest(recipe=recipe):
                intro = (ROOT / f"patterns/{recipe}.md").read_text().split("\n## ", 1)[0]
                self.assertIn("ACCEPTED", intro)
                self.assertIn(decision, intro)
                self.assertNotIn("pending", intro.lower())
        for example, decision in (
            ("repotend-pilot", "discover-v0.1-qualification-review.md"),
            ("repo-maintenance", "maintain-v0.2-qualification-review.md"),
            ("manual-deliver/agent-qualification", "deliver-v0.2-qualification-review.md"),
            ("manual-deliver/intentline-trace", "deliver-v0.2-qualification-review.md"),
        ):
            with self.subTest(example=example):
                intro = (ROOT / f"examples/{example}/README.md").read_text().split("\n## ", 1)[0]
                self.assertIn("Current scope", intro)
                self.assertIn("Historical record", intro)
                self.assertIn(decision, intro)

    def test_active_workflows_are_not_scheduled_or_publishers(self):
        names = {p.name for p in (ROOT / ".github/workflows").glob("*.yml")}
        self.assertEqual(names, {"maintain-audit.yml", "reference-checks.yml"})
        workflow = WORKFLOW.read_text()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertNotIn("\n  schedule:", workflow)
        self.assertNotIn("issues: write", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("remediate.mjs --apply", workflow)


if __name__ == "__main__":
    unittest.main()
