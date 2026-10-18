"""Foundryline Deliver reference/fixture checks, NOT native Proofline qualification.

This suite executes only the small, authored username candidate as ordinary
Python unittest subprocesses. It never launches an agent, Intentline, Proofline,
or any unrelated target project. It cannot establish sandbox/evidence validity.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "manual-deliver"
CANDIDATE = EXAMPLE / "candidate"
SOURCE = EXAMPLE / "original-request.md"
PLAN = EXAMPLE / "verification-plan.json"


class ManualDeliverReferenceTests(unittest.TestCase):
    def test_original_source_identity_and_citations(self) -> None:
        raw = SOURCE.read_bytes()
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        self.assertEqual(raw.count(b"\r"), 0)  # LF is part of the exact input.
        self.assertTrue(raw.endswith(b"\n"))
        self.assertEqual(hashlib.sha256(raw).hexdigest(), plan["source"]["sha256"])
        self.assertEqual(plan["source"]["path"], "original-request.md")
        self.assertEqual(plan["source"]["authority"], "illustrative, not a real authorized GitHub issue")
        lines = raw.decode("utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        rows = plan["illustrative_requirements"]
        self.assertEqual([row["id"] for row in rows], ["R1", "R2"])
        for row in rows:
            with self.subTest(row=row["id"]):
                self.assertEqual(row["source_id"], "S1")
                self.assertEqual(lines[row["line"] - 1], row["quote"])

    def test_selected_exact_argv_template_and_unmapped_requirement(self) -> None:
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        self.assertIn("AUTHORED PRE-RUN PLAN", plan["status"])
        self.assertEqual(plan["observed_follow_up"], "native-qualification.json")
        check = plan["selected_check"]
        self.assertEqual(check["index"], 0)
        self.assertEqual(
            check["argv_template"],
            [
                "HOST_ABSOLUTE_PYTHON",
                "-B", "-m", "unittest",
                "tests.test_username_validation.UsernameValidationTests.test_rejects_blank",
            ],
        )
        self.assertIn("MATCHING DIRECT NATIVE CHECK OBSERVED LATER", check["execution"])
        self.assertIsNone(plan["candidate"]["frozen_git_commit"])
        self.assertIsNone(plan["candidate"]["proofline_report"])
        self.assertEqual(plan["illustrative_requirements"][0]["selected_check_indices"], [0])
        self.assertEqual(plan["illustrative_requirements"][1]["selected_check_indices"], [])
        self.assertEqual(plan["illustrative_requirements"][1]["proofline_evidence"], "NOT DEMONSTRATED")

    def test_authored_candidate_unit_tests_actually_run_as_regular_python(self) -> None:
        # Ordinary Python in CI, not Proofline, sandbox native, coding-agent execution
        # or a check of a customer repository.
        commands = [
            ([sys.executable, "-B", "-m", "unittest",
              "tests.test_username_validation.UsernameValidationTests.test_rejects_blank", "-v"],
             "Ran 1 test"),
            ([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
             "Ran 2 tests"),
        ]
        for argv, expected in commands:
            with self.subTest(command=argv[-1]):
                completed = subprocess.run(
                    argv, cwd=CANDIDATE, text=True, capture_output=True,
                    check=False, timeout=20,
                )
                self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
                self.assertIn(expected, completed.stdout + completed.stderr)
                self.assertIn("OK", completed.stdout + completed.stderr)

    def test_guide_documents_current_real_cli_and_separate_effects(self) -> None:
        guide = (ROOT / "patterns/deliver.md").read_text(encoding="utf-8")
        example = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        handoff = (EXAMPLE / "handoff-template.md").read_text(encoding="utf-8")
        for token in (
            "8e117fff4de2459637fe7f74f47ab17fc3341d84",
            "25e926f57e69395193fc0ac258f9e6dd2332cb18",
            "0.162.1",
            "--repo", "--source", "--checks", "--command",
            "--intentline-export", "--intentline-links", "--output",
            "NOT DEMONSTRATED", "STALE CHECKS", "coverage_completeness: UNKNOWN",
            "PR CREATE", "native-qualification.md",
        ):
            with self.subTest(token=token):
                self.assertIn(token, guide)
        self.assertIn('"R1": [{"index": 0, "argv": argv}]', example)
        self.assertIn("NOT PUBLISHED", handoff)
        self.assertIn("NOT COMPLETED", handoff)
        self.assertIn("NOT DEMONSTRATED", handoff)
        self.assertIn("NOT RUN", example)


    def test_native_observation_summary_has_bounded_real_receipt_identities(self) -> None:
        # Only structural consistency of an observed record; this test does
        # not fetch or replay the original GitHub-hosted macOS process.
        record = json.loads(
            (EXAMPLE / "native-qualification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(record["evidence_source"]["workflow_run_id"], 39114778567)
        self.assertEqual(record["evidence_source"]["workflow_event"], "pull_request")
        self.assertEqual(record["evidence_source"]["proofline_commit"],
                         "8e117fff4de2459637fe7f74f47ab17fc3341d84")
        self.assertEqual(record["host"]["codex_cli"], "0.162.1")
        self.assertEqual(record["host"]["model_dispatches"], 0)
        self.assertTrue(record["source_and_candidate"]["authored_fixture"])
        self.assertEqual(record["source_and_candidate"]["source_sha256"],
                         hashlib.sha256(SOURCE.read_bytes()).hexdigest())
        self.assertIn("NOT OBSERVED", record["source_and_candidate"]["coding_agent_implementation"])
        self.assertEqual(record["positive"]["status"], "CHECKS PASSED")
        self.assertEqual(record["positive"]["native_boundary"], "OBSERVED — NARROW CANARIES")
        self.assertEqual(record["positive"]["check_count"], 1)
        self.assertEqual(record["positive"]["cli_exit"], 0)
        self.assertEqual(record["positive"]["status_readback_exit"], 0)
        self.assertEqual(record["positive"]["selected_argv"][1:],
                         json.loads(PLAN.read_text())["selected_check"]["argv_template"][1:])
        self.assertEqual(record["positive"]["source_coverage"]["completeness"], "UNKNOWN")
        self.assertEqual(record["negative"]["status"], "CHECKS UNAVAILABLE")
        self.assertEqual(record["negative"]["cli_exit"], 2)
        self.assertEqual(record["negative"]["native_observation"], "UNAVAILABLE")
        self.assertIn("NOT DEMONSTRATED", record["positive"]["source_coverage"]["R2"])
        self.assertFalse(record["evidence_source"]["raw_artifact_retained_in_git"])
        for field in ("report_sha256", "receipt_sha256"):
            self.assertEqual(len(record["positive"][field]), 64)
            self.assertEqual(len(record["negative"][field]), 64)
        self.assertIn("coding agent implementation", " ".join(record["not_demonstrated"]))


    def test_refusals_are_proposals_not_invented_observations(self) -> None:
        refusals = (EXAMPLE / "refusals.md").read_text(encoding="utf-8")
        for term in (
            "PROPOSED — NOT RUN", "EXECUTION UNAVAILABLE",
            "CHECKS UNAVAILABLE", "CHECKS FAILED", "STALE CHECKS",
            "NOT DEMONSTRATED", "NOT PUBLISHED",
        ):
            with self.subTest(term=term):
                self.assertIn(term, refusals)
        self.assertIn("ONE ACTUAL NEGATIVE CONTROL OBSERVED", refusals)
        self.assertNotIn("Native run passed", refusals)


if __name__ == "__main__":
    unittest.main()
