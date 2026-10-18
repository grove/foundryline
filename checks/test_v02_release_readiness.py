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

    def test_release_is_unequivocally_not_published(self):
        draft = RELEASE.read_text()
        self.assertIn("RELEASE CANDIDATE NOTES — NOT TAGGED OR PUBLISHED", draft)
        self.assertIn("Explicitly approve", draft)
        self.assertIn("exact v0.2.0 release commit", draft)
        self.assertIn("scheduled intake", draft.lower())
        self.assertIn("defers scheduling", draft)
        self.assertIn("coverage_completeness: UNKNOWN", draft)
        self.assertIn("v0.1.0", draft)
        self.assertNotIn("v0.2.0 is now published", draft.lower())
        self.assertIn("release NOT published", ROADMAP.read_text())

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

    def test_active_workflows_are_not_scheduled_or_publishers(self):
        names = {p.name for p in (ROOT / ".github/workflows").glob("*.yml")}
        standard = {"maintain-audit.yml", "reference-checks.yml"}
        publisher = ".github/workflows/publish-v0.2.0-once.yml"
        # Temporary, explicitly authorized one-shot publication PR only.
        # The cleanup PR MUST delete this workflow and restore this guard.
        if names != standard:
            self.assertEqual(names, standard | {"publish-v0.2.0-once.yml"})
            once = (ROOT / publisher).read_text()
            self.assertIn('branches: [main]', once)
            self.assertIn('"'+publisher+'"', once)
            self.assertIn("RELEASE_TARGET: 8409eebe0389461ec60a4bef6a5ce2aec6fb0903", once)
            self.assertIn("RELEASE_TAG: v0.2.0", once)
            self.assertIn("permissions:\n  contents: write", once)
            self.assertIn("git/matching-refs/tags/", once)
            self.assertIn("gh release create", once)
            self.assertIn("persist-credentials: false", once)
            for disallowed in ("\n  schedule:", "\n  workflow_dispatch:", "\n  issues:", "\n  workflow_run:"):
                self.assertNotIn(disallowed, once)
        workflow = WORKFLOW.read_text()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertNotIn("\n  schedule:", workflow)
        self.assertNotIn("issues: write", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("remediate.mjs --apply", workflow)


if __name__ == "__main__":
    unittest.main()
