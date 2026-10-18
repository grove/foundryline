"""Verify saved external native Deliver receipts without running product code.

The original unmodified GitHub Actions ZIP is committed to this PR. These offline
checks verify its bytes and specific report assertions; they do not create new
native sandbox evidence, authenticate the original operator, or approve a release.
"""
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "examples" / "manual-deliver" / "receipts"
NAME = "repotend-issue15-native-39123644533"
MANIFEST = EVIDENCE / (NAME + ".manifest.json")
ARCHIVE = EVIDENCE / (NAME + ".zip")

SHA256 = "31f8eb7ce91eb2a647a2e6af4e12050dddb47a3a73df619c7c24c8410c1883e8"
GIT_BLOB_SHA1 = "a33a6fa58fb13bb25f96393cb43c157799a479c2"
SOURCE_SHA = "e1d61d83be03e8c442d05d1953bd2de47cd3a5a17a755c87d81826c56cb163f8"
CANDIDATE_TREE = "544421686de4112ca1ac8bfb118cde750821e3ef"
LINKED = "LINKED CHECKS PASSED (limited evidence)"


class SavedNativeDeliverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = ARCHIVE.read_bytes()
        cls.manifest = json.loads(MANIFEST.read_bytes())
        cls.zip = ZipFile(io.BytesIO(cls.raw))

    @classmethod
    def tearDownClass(cls):
        cls.zip.close()

    @classmethod
    def obj(cls, name):
        return json.loads(cls.zip.read(name))

    def test_full_original_zip_byte_identity(self):
        self.assertEqual(len(self.raw), 1892994)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), SHA256)
        git_blob = b"blob " + str(len(self.raw)).encode("ascii") + b"\0" + self.raw
        self.assertEqual(hashlib.sha1(git_blob).hexdigest(), GIT_BLOB_SHA1)
        self.assertEqual(self.manifest["retained_copy"]["git_blob_sha1"], GIT_BLOB_SHA1)
        self.assertEqual(self.manifest["original_artifact"]["run_id"], 39123644533)
        self.assertEqual(self.manifest["original_artifact"]["artifact_id"], 12134224973)
        self.assertEqual(self.manifest["original_artifact"]["zip_sha256"], SHA256)
        self.assertEqual(self.manifest["retained_copy"]["zip_sha256"], SHA256)
        self.assertIsNone(self.zip.testzip())
        names = self.zip.namelist()
        self.assertEqual(len(names), len(set(names)))
        for name in names:
            path = PurePosixPath(name)
            self.assertFalse(path.is_absolute())
            self.assertNotIn("..", path.parts)
            self.assertFalse(name.startswith("/"))

    def test_independently_inspected_primary_file_hashes(self):
        for path, expected in self.manifest["member_sha256"].items():
            with self.subTest(path=path):
                self.assertEqual(hashlib.sha256(self.zip.read(path)).hexdigest(), expected)

    def test_exact_original_source_and_advisory_intentline_export(self):
        self.assertEqual(hashlib.sha256(self.zip.read(
            "original/export/source-S1.txt")).hexdigest(), SOURCE_SHA)
        contract = self.obj("original/export/contract.json")
        marker = self.obj("original/export/export-manifest.json")
        self.assertEqual((contract["schema_version"], contract["revision"]), (1, 1))
        self.assertEqual([r["id"] for r in contract["requirements"]], ["R1", "R2"])
        self.assertEqual(marker["record"], "intentline.export")
        self.assertEqual(marker["revision"], 1)
        self.assertEqual(marker["authority"], "unapproved")
        self.assertTrue(marker["advisory"])
        for name, digest in marker["files"].items():
            self.assertEqual(hashlib.sha256(self.zip.read(
                "original/export/" + name)).hexdigest(), digest)

    def test_same_host_node_startup_is_attributed_narrowly(self):
        obs = self.obj("identity.json")
        paired = self.obj("paired-startup-comparison.json")
        allowed = self.obj("node-startup-receipt.json")
        blocked = self.obj("node-baseline-without-file-receipt.json")
        self.assertEqual(obs["run_id"], "39123644533")
        self.assertEqual(obs["source_sha"],
                         "ead77fde6a5a7ba33e54cc81deb76fced8dbc333")
        self.assertEqual(obs["source_tree"], CANDIDATE_TREE)
        self.assertEqual(obs["tool_sha"],
                         "f019a3927e5f4ce8a325b73edb2a28369265a95f")
        self.assertEqual(obs["openssl_read_scope"], "read")
        self.assertFalse(obs["scope"]["network"]["enabled"])
        self.assertTrue(obs["openssl_is_file"])
        self.assertFalse(obs["openssl_symlink"])
        self.assertEqual(paired["read_only_file_grant"],
                         "/System/Library/OpenSSL/openssl.cnf")
        self.assertEqual((allowed["exit_code"], blocked["exit_code"]), (0, 1))
        self.assertEqual(allowed["stdout"], "NODE_BOOTSTRAPPED\n")
        self.assertEqual(allowed["stderr"], "")
        self.assertIn("openssl.cnf", blocked["stderr"])
        self.assertIn("Operation not permitted", blocked["stderr"])
        self.assertTrue(paired["without_grant_openssl_denial"])
        self.assertTrue(paired["same_runner_pins"])
        self.assertTrue(paired["no_proof_of_general_filesystem_isolation"])

    def test_two_native_scenarios_have_bounded_separate_evidence(self):
        scenarios = {
            "r1-only": {"R1": LINKED, "R2": "NOT DEMONSTRATED"},
            "r1-r2": {"R1": LINKED, "R2": LINKED},
        }
        for name, expected in scenarios.items():
            with self.subTest(scenario=name):
                report = self.obj(name + "-record/report.json")
                checks = self.obj(name + "-checks.json")
                links = self.obj(name + "-links.json")
                self.assertEqual(report["status"], "CHECKS PASSED")
                self.assertEqual(report["candidate_tree"], CANDIDATE_TREE)
                self.assertEqual(report["source_sha256"], SOURCE_SHA)
                self.assertEqual(report["model_dispatches"], 0)
                self.assertFalse(report["published"])
                self.assertFalse(report["merged"])
                self.assertEqual(report["boundary"]["assessment"]["status"], "OBSERVED")
                self.assertEqual(report["promise_evidence"]["coverage_completeness"], "UNKNOWN")
                actual = {r["id"]: r["status"]
                          for r in report["promise_evidence"]["requirements"]}
                self.assertEqual(actual, expected)
                self.assertEqual(self.obj(name + "-result.json")["exit"], 0)
                self.assertEqual(self.obj(name + "-status-result.json")["exit"], 0)
                self.assertEqual(len(report["observations"]), len(checks))
                self.assertEqual(len(report["checks"]), len(checks))
                for i, selected in enumerate(checks):
                    requirement = "R1" if i == 0 else "R2"
                    self.assertEqual(links[requirement], [{"index": i, "argv": selected}])
                    self.assertEqual(report["checks"][i], selected)
                    self.assertEqual(selected[-2:], [
                        "--test-name-pattern=^" + requirement, "test/audit-cli.test.mjs"])
                    receipt = self.obj(
                        name + "-record/receipts/check-" + str(i).zfill(3) + ".json")
                    self.assertEqual(receipt["exit_code"], 0)
                    self.assertFalse(receipt["timed_out"])
                    self.assertEqual(receipt["stderr"], "")
                    self.assertIn("# tests 1", receipt["stdout"])
                    self.assertIn("# pass 1", receipt["stdout"])
                    self.assertIn("# fail 0", receipt["stdout"])
                    self.assertEqual(report["observations"][i]["status"], "PASSED")
        self.assertNotIn("R2", self.obj("r1-only-links.json"))

    def test_refusal_did_not_generate_a_fake_positive_report(self):
        bad = self.obj("invalid-map-result.json")
        self.assertEqual(bad["exit"], 1)
        self.assertEqual(self.zip.read("invalid-map.stdout"), b"")
        self.assertIn(b"Intentline R check index/argv differs",
                      self.zip.read("invalid-map.stderr"))
        self.assertNotIn("invalid-map-record/report.json", self.zip.namelist())


if __name__ == "__main__":
    unittest.main()
