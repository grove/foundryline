"""Structural checks for Foundryline's authored manual Discover blueprint.

These checks do NOT run Gapline, Intentline, any sample target project, or
an agent host. Passing tests cannot qualify the manual Discover workflow.
"""

from __future__ import annotations

import ast
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "manual-discover"
PATTERN = ROOT / "patterns" / "discover.md"

DOCUMENTS = (
    ROOT / "README.md",
    ROOT / "DESIGN.md",
    ROOT / "IMPLEMENTATION.md",
    ROOT / "docs" / "discover-v0.1-qualification-review.md",
    ROOT / "docs" / "deliver-v0.2-qualification-review.md",
    ROOT / "docs" / "maintain-v0.2-qualification-review.md",
    ROOT / "docs" / "manual-intake.md",
    ROOT / "docs" / "releases" / "v0.1.0.md",
    ROOT / "docs" / "releases" / "v0.2.0.md",
    PATTERN,
    EXAMPLE / "README.md",
    EXAMPLE / "example-report.md",
    EXAMPLE / "example-issue-proposal.md",
    EXAMPLE / "example-no-findings.md",
    EXAMPLE / "example-refusal.md",
    EXAMPLE / "run-record-template.md",
    ROOT / "examples/repotend-pilot/README.md",
    ROOT / "examples/repotend-pilot/issue-proposal.md",
    ROOT / "examples/repotend-pilot/host/README.md",
    ROOT / "patterns/maintain.md",
    ROOT / "patterns/deliver.md",
    ROOT / "examples/manual-deliver/README.md",
    ROOT / "examples/manual-deliver/macos-check-only.md",
    ROOT / "examples/manual-deliver/candidate/README.md",
    ROOT / "examples/manual-deliver/refusals.md",
    ROOT / "examples/manual-deliver/handoff-template.md",
    ROOT / "examples/manual-deliver/native-qualification.md",
    ROOT / "examples/manual-deliver/agent-qualification/README.md",
    ROOT / "examples/manual-deliver/intentline-trace/README.md",
    ROOT / "examples/repo-maintenance/README.md",
    ROOT / "examples/repo-maintenance/issue-proposal.md",
    ROOT / "examples/repo-maintenance/adoption.md",
)

LOCAL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ManualDiscoverReferenceTests(unittest.TestCase):
    def test_expected_documents_and_fixtures_exist(self) -> None:
        fixture_paths = (
            EXAMPLE / "fixtures/docs/registration-policy.md",
            EXAMPLE / "fixtures/src/registration.py",
            EXAMPLE / "fixtures/tests/test_registration.py",
        )
        for path in (*DOCUMENTS, *fixture_paths):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertTrue(path.is_file())

    def test_relative_links_resolve(self) -> None:
        checked = 0
        for document in DOCUMENTS:
            for raw_destination in LOCAL_LINK.findall(read(document)):
                url = urlsplit(raw_destination)
                if url.scheme or url.netloc:
                    continue
                path = (document.parent / unquote(url.path)).resolve() if url.path else document
                with self.subTest(source=str(document.relative_to(ROOT)), link=raw_destination):
                    self.assertTrue(path.is_file(), f"broken local link: {raw_destination}")
                    if url.fragment and path.suffix == ".md":
                        headings = re.findall(r"^#{1,6} (.+)$", read(path), re.MULTILINE)
                        anchors = {
                            re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
                            for heading in headings
                        }
                        self.assertIn(unquote(url.fragment), anchors,
                                      f"broken heading link: {raw_destination}")
                checked += 1
        self.assertGreaterEqual(checked, 10)

    def test_pattern_has_manual_and_read_only_boundaries(self) -> None:
        pattern = read(PATTERN)
        for required in (
            "manual, read-only",
            "gapline-audit",
            "intentline-issue",
            "intentline-plan",
            "NOT PUBLISHED",
            "PROPOSED — NOT RUN",
            "working tree: UNKNOWN",
            "NOT CHECKED",
            "UNQUALIFIED",
            "No supported findings",
            "actual skill activation",
        ):
            with self.subTest(required=required):
                self.assertIn(required.lower(), pattern.lower())

    def test_fixture_claim_is_source_grounded_and_not_runtime_proof(self) -> None:
        policy = read(EXAMPLE / "fixtures/docs/registration-policy.md").splitlines()
        code = read(EXAMPLE / "fixtures/src/registration.py").splitlines()
        selected_tests = read(EXAMPLE / "fixtures/tests/test_registration.py")
        self.assertIn("empty or contain only whitespace", policy[4])
        self.assertIn("Unicode", policy[5])
        self.assertIn("register", policy[6])
        self.assertIn("if not username:", code[5])
        self.assertIn('return {"username": username}', code[7])
        self.assertIn("test_empty_rejected", selected_tests)
        self.assertIn("test_unicode_name_preserved", selected_tests)
        # Parse, but never import or execute authored target code/tests.
        ast.parse("\n".join(code))
        ast.parse(selected_tests)
        report = read(EXAMPLE / "example-report.md")
        self.assertIn("NOT AN ACTUAL RUN", report)
        self.assertIn("SUPPORTED", report)
        self.assertIn("No runtime failure was reproduced", report)
        self.assertIn("Counterevidence", report)
        self.assertIn("NOT CHECKED", report)

    def test_issue_proposal_is_not_published_or_approved(self) -> None:
        draft = read(EXAMPLE / "example-issue-proposal.md")
        for required in (
            "NOT PUBLISHED",
            "AUTHORED FIXTURE",
            "Confirm before fixing",
            "R1:",
            "R2:",
            "R3:",
            "PROPOSED — NOT RUN",
            "NOT CHECKED",
            "Saved Intentline agreement:** NONE",
            "Issue URL:** NONE",
        ):
            with self.subTest(required=required):
                self.assertIn(required, draft)

    def test_no_findings_and_refusal_have_honest_limits(self) -> None:
        no_findings = read(EXAMPLE / "example-no-findings.md")
        refusal = read(EXAMPLE / "example-refusal.md")
        self.assertIn("NOT AN ACTUAL RUN", no_findings)
        self.assertIn("NO_SUPPORTED_FINDINGS_IN_INSPECTED_SCOPE", no_findings)
        self.assertIn("not", no_findings.lower())
        self.assertIn("UNQUALIFIED / UNAVAILABLE", refusal)
        self.assertIn("Gapline skill was not invoked", refusal)
        self.assertIn("NOT PUBLISHED", refusal)

    def test_blank_run_record_cannot_masquerade_as_receipt(self) -> None:
        template = read(EXAMPLE / "run-record-template.md")
        self.assertIn("BLANK TEMPLATE", template)
        self.assertIn("NO ACTUAL RUN EVIDENCE ENTERED", template)
        self.assertIn("UNQUALIFIED", template)
        self.assertIn("Independent reproduction", template)
        self.assertIn("negative control", template.lower())
        self.assertIn("UNVERIFIED", template)
        self.assertIn("NOT PUBLISHED", template)


if __name__ == "__main__":
    unittest.main()
