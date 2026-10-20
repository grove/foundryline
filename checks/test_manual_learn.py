"""Structural Learn docs checks, not a Learn execution or impact qualification."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "patterns/learn.md"
EXAMPLE = ROOT / "examples/manual-learn/README.md"
README = ROOT / "README.md"
TEMPLATE = ROOT / "docs/evidence-handoff-template.md"
LOCAL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

class ManualLearnReferenceTests(unittest.TestCase):
    def test_manual_scope_and_unknowns(self):
        guide = GUIDE.read_text()
        example = EXAMPLE.read_text()
        self.assertIn("NOT QUALIFIED", guide)
        self.assertIn("no post-delivery", guide.lower())
        self.assertIn("UNKNOWN", guide)
        self.assertIn("PROPOSED — NOT RUN", example)
        self.assertIn("NOT OBSERVED", example)
        self.assertIn("NOT MEASURED", example)
        self.assertIn("Independent review questions (NOT PERFORMED", example)
        self.assertIn("NO APPROVED OUTCOME TARGET", example)
        self.assertIn("separate read permission", example.lower())
        for lens in ("DORA", "SRE / SLO", "Flow", "OKR / business"):
            self.assertIn(lens, example)
        self.assertIn("../examples/manual-learn/README.md", guide)
        self.assertIn("examples/manual-learn/README.md", README.read_text())
        self.assertIn("Discover, Maintain, Deliver or Learn", TEMPLATE.read_text())

    def test_real_source_candidate_receipt_and_no_data_control(self):
        example = EXAMPLE.read_text()
        for source in (
            "https://github.com/grove/foundryline/issues/21",
            "https://github.com/grove/foundryline/pull/22",
            "https://github.com/grove/foundryline/actions/runs/39118875068",
            "f54d44eb1d21fae2d7cfd8aae4216e91019a87d3",
            "a003d013419fd1f142f0d05175938c6b0d7008f3",
            "https://github.com/grove/foundryline/pull/20",
            "https://github.com/grove/foundryline/actions/runs/39117358329",
            "27 selected tests",
            "NOT DEMONSTRATED", "coverage_completeness: UNKNOWN",
        ):
            with self.subTest(source=source):
                self.assertIn(source, example)
        self.assertIn("merged", example)
        self.assertIn("not", example.lower())
        self.assertIn("deployed revision", example)

    def test_local_references_and_heading_fragments(self):
        for document in (GUIDE, EXAMPLE, README, TEMPLATE):
            content = document.read_text(encoding="utf-8")
            for raw in LOCAL_LINK.findall(content):
                parsed = urlsplit(raw)
                if parsed.scheme or parsed.netloc:
                    continue
                target = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
                with self.subTest(document=document.name, raw=raw):
                    self.assertTrue(target.is_file(), raw)
                    if parsed.fragment and target.suffix == ".md":
                        headings = re.findall(r"^#{1,6} (.+)$", target.read_text(encoding="utf-8"), re.M)
                        anchors = {
                            re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-")
                            for h in headings
                        }
                        self.assertIn(unquote(parsed.fragment), anchors, raw)

if __name__ == "__main__":
    unittest.main()
