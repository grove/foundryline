"""Retained issue #21 identities, not native execution or acceptance proof."""

import hashlib
import json
import unittest
from pathlib import Path


EXAMPLE = Path(__file__).resolve().parents[1] / "examples/manual-deliver/intentline-trace"
EXPORT = EXAMPLE / "export"


class IntentlineTraceTests(unittest.TestCase):
    def test_complete_source_and_citations(self):
        raw = (EXPORT / "source-S1.txt").read_bytes()
        issue = json.loads((EXAMPLE / "issue-21.json").read_bytes())
        self.assertEqual(issue["url"], "https://github.com/grove/foundryline/issues/21")
        self.assertEqual(issue["comments"], [])
        self.assertEqual(raw, issue["body"].encode("utf-8"))
        self.assertEqual(hashlib.sha256(raw).hexdigest(),
                         "3c1a808cc0dfad337b88f47b61a7513182c829ab0a96efbcf8bc443c07a343bf")
        contract = json.loads((EXPORT / "contract.json").read_bytes())
        self.assertEqual([row["id"] for row in contract["requirements"]],
                         [f"R{i}" for i in range(1, 8)])
        lines = raw.decode("utf-8").splitlines(keepends=True)
        for row in (*contract["requirements"], *contract["constraints"],
                    *contract["out_of_scope"]):
            for ref in row["source_refs"]:
                with self.subTest(ref=ref):
                    self.assertEqual(ref["source_id"], "S1")
                    self.assertTrue(1 <= ref["line_start"] <= ref["line_end"] <= len(lines))
                    quote = "".join(lines[ref["line_start"] - 1:ref["line_end"]])
                    self.assertEqual(ref["quote"], quote.rstrip("\r\n"))

    def test_export_completion_and_file_identities(self):
        marker = json.loads((EXPORT / "export-manifest.json").read_bytes())
        self.assertEqual(marker["record"], "intentline.export")
        self.assertEqual(marker["format"], "json")
        self.assertEqual(marker["revision"], 1)
        self.assertTrue(marker["advisory"])
        self.assertEqual(marker["authority"], "unapproved")
        self.assertEqual(set(marker["files"]),
                         {"contract.json", "source-manifest.json", "source-S1.txt"})
        self.assertEqual({p.name for p in EXPORT.iterdir()},
                         {"export-manifest.json", *marker["files"]})
        for name, expected in marker["files"].items():
            self.assertEqual(hashlib.sha256((EXPORT / name).read_bytes()).hexdigest(), expected)
        for name in ("export-manifest.json", "contract.json", "source-manifest.json"):
            raw = (EXPORT / name).read_bytes()
            canonical = (json.dumps(json.loads(raw), sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
            self.assertEqual(raw, canonical)
        self.assertEqual(marker["contract_sha256"], marker["files"]["contract.json"])
        self.assertEqual(marker["source_bundle_sha256"], marker["files"]["source-manifest.json"])
        contract = json.loads((EXPORT / "contract.json").read_bytes())
        self.assertEqual(contract["schema_version"], 1)
        self.assertEqual(contract["revision"], 1)
        self.assertEqual(contract["change_notes"], [{"kind": "initial", "revision": 1}])
        self.assertEqual(contract["source_bundle_sha256"], marker["source_bundle_sha256"])
        self.assertEqual(contract["open_decisions"], [])
        manifest = json.loads((EXPORT / "source-manifest.json").read_bytes())
        self.assertEqual(manifest["schema_version"], 1)
        self.assertEqual(len(manifest["sources"]), 1)
        source = manifest["sources"][0]
        raw = (EXPORT / "source-S1.txt").read_bytes()
        self.assertEqual((source["source_id"], source["role"]), ("S1", "request"))
        self.assertEqual(source["bytes"], len(raw))
        self.assertEqual(source["sha256"], hashlib.sha256(raw).hexdigest())
