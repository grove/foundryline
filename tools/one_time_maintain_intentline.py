#!/usr/bin/env python3
"""Independent script-led Maintain replication, not a cold-start agent qualification.

Based on Foundryline v0.2.0 manual Maintain; no target code, target installs,
remediation, GitHub issue writes, model calls, or publisher permissions.
All underlying process stdout/stderr/argv/cwd/exits are preserved as evidence.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import time


ROOT = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
RECEIPTS = ROOT / "receipts"
TOOL = ROOT / "tool"
TARGET = ROOT / "target"
GUIDE = ROOT / "guide"
RECEIPTS.mkdir(mode=0o700, exist_ok=True)
EXPECTED = {
    "tool": "2d69cce901475380775f674b9cc5755f1f89f82e",
    "target": "25e926f57e69395193fc0ac258f9e6dd2332cb18",
    "guide": "8409eebe0389461ec60a4bef6a5ce2aec6fb0903",
}


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    path = RECEIPTS / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def git(repo, *args):
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True, timeout=30).strip()


def run(label, argv, cwd, *, timeout=90):
    started = utc()
    t0 = time.monotonic()
    stdout_name = label + ".stdout.txt"
    stderr_name = label + ".stderr.txt"
    try:
        proc = subprocess.run(
            argv, cwd=str(cwd), capture_output=True, timeout=timeout, check=False)
        output, errors, exit_code = proc.stdout, proc.stderr, proc.returncode
        signal = None
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        output, errors = exc.stdout or b"", exc.stderr or b""
        exit_code = None
        signal = "timeout"
        timed_out = True
    (RECEIPTS / stdout_name).write_bytes(output)
    (RECEIPTS / stderr_name).write_bytes(errors)
    result = {
        "label": label, "argv": argv, "cwd": str(cwd),
        "started_at_utc": started, "finished_at_utc": utc(),
        "elapsed_seconds": time.monotonic() - t0,
        "exit_code": exit_code, "timed_out": timed_out, "signal": signal,
        "stdout": {"file": stdout_name, "bytes": len(output), "sha256": digest(output)},
        "stderr": {"file": stderr_name, "bytes": len(errors), "sha256": digest(errors)},
    }
    save(label + ".command.json", result)
    return result, output, errors


def snapshot(repo):
    """Snapshot all target working-tree paths, modes and hashes, excluding .git data."""
    entries = {}
    for p in sorted(repo.rglob("*"), key=lambda x: x.relative_to(repo).as_posix()):
        rel = p.relative_to(repo).as_posix()
        if ".git" in p.relative_to(repo).parts:
            continue
        metadata = p.lstat()
        mode = stat.S_IMODE(metadata.st_mode)
        if p.is_symlink():
            value = {"kind": "symlink", "mode": mode, "destination": os.readlink(p)}
        elif p.is_file():
            raw = p.read_bytes()
            value = {"kind": "file", "mode": mode, "bytes": len(raw), "sha256": digest(raw)}
        elif p.is_dir():
            value = {"kind": "directory", "mode": mode}
        else:
            raise RuntimeError(f"Unexpected target file type: {rel}")
        entries[rel] = value
    return entries


began = utc()
started = time.monotonic()
for name, sha in EXPECTED.items():
    got = git({"tool": TOOL, "target": TARGET, "guide": GUIDE}[name], "rev-parse", "HEAD")
    if got != sha:
        raise RuntimeError(f"Wrong {name} checkout: {got} != {sha}")
guide_text = (GUIDE / "patterns/maintain.md").read_text(encoding="utf-8")
assert "read-only RepoTend" in guide_text and "## 6. Check adoption and failure behavior" in guide_text
for token in ("UNAVAILABLE / INCOMPLETE", "NOT PUBLISHED", "Node.js >=22.16.0"):
    assert token in guide_text, token
node_version = subprocess.check_output(["node", "--version"], text=True).strip()
npm_version = subprocess.check_output(["npm", "--version"], text=True).strip()
git_version = subprocess.check_output(["git", "--version"], text=True).strip()
if tuple(int(x) for x in node_version.lstrip("v").split(".")[:2]) < (22, 16):
    raise RuntimeError("RepoTend requires Node 22.16+")

before = snapshot(TARGET)
save("target-before.json", before)
status_before = git(TARGET, "status", "--porcelain", "--untracked-files=all")
save("environment.json", {
    "started_at_utc": began,
    "experiment_mode": "scripted fresh GitHub Actions runner, not a cold-start coding agent",
    "no_independent_operator_claim": True,
    "permissions": "GitHub Actions contents:read; target has no write intention",
    "runtime": {
        "runner_os": os.environ.get("RUNNER_OS"), "runner_arch": os.environ.get("RUNNER_ARCH"),
        "node": node_version, "npm": npm_version, "git": git_version, "python": sys.version,
        "node_executable": shutil.which("node"), "npm_executable": shutil.which("npm"),
    },
    "revisions": EXPECTED, "target_repository": "https://github.com/grove/intentline",
    "tool_repository": "https://github.com/grove/repotend",
    "guide_release": "https://github.com/grove/foundryline/releases/tag/v0.2.0",
    "target_files_before": len(before), "status_before": status_before,
    "npm_cache_outside_target": str(Path(os.environ["RUNNER_TEMP"]) / "foundryline-intentline-npm-cache"),
    "tools": {"git_actions_trigger": os.environ.get("GITHUB_EVENT_NAME"),
              "run_id": os.environ.get("GITHUB_RUN_ID"),
              "source_sha": os.environ.get("GITHUB_SHA")},
})
if status_before:
    raise RuntimeError("Target checkout is dirty before auditor execution")

install, install_out, install_err = run(
    "tool-install",
    ["npm", "ci", "--ignore-scripts", "--no-audit", "--no-fund",
     "--cache", str(Path(os.environ["RUNNER_TEMP"]) / "foundryline-intentline-npm-cache")],
    TOOL, timeout=160)
if install["exit_code"] != 0:
    raise RuntimeError("Pinned RepoTend installation failed; see retained raw receipt")

node = str(Path(shutil.which("node")).resolve())
base = [node, "skills/repotend/scripts/audit.mjs"]
j, stdout_json, stderr_json = run(
    "audit-json",
    base + ["--root", str(TARGET), "--format", "json"], TOOL, timeout=100)
md, stdout_md, stderr_md = run(
    "audit-markdown",
    base + ["--root", str(TARGET), "--format", "markdown"], TOOL, timeout=100)

unavailable = RECEIPTS / "deliberately-nonexistent-target"
if unavailable.exists():
    raise RuntimeError("Missing-target negative path unexpectedly exists")
neg, stdout_missing, stderr_missing = run(
    "missing-target",
    base + ["--root", str(unavailable), "--format", "json"], TOOL, timeout=100)

after = snapshot(TARGET)
save("target-after.json", after)
status_after = git(TARGET, "status", "--porcelain", "--untracked-files=all")
save("observed-source-excerpts.json", {
    "contribution_guidance": [
        line for line in (TARGET / "README.md").read_text(encoding="utf-8").splitlines()
        if "contribut" in line.lower() or "pull request" in line.lower()
    ][:14],
    "workflow_action_lines": [
        line for line in (TARGET / ".github/workflows/ci.yml").read_text(encoding="utf-8").splitlines()
        if "uses:" in line
    ],
})

try:
    report = json.loads(stdout_json)
except json.JSONDecodeError as err:
    save("summary.json", {"outcome": "UNAVAILABLE", "reason": f"invalid JSON: {err}"})
    raise
counts = dict(sorted(Counter(row["status"] for row in report["findings"]).items()))
report_ids = [x["ruleId"] for x in report["findings"]]
markdown_has_all = all(rule in stdout_md.decode(errors="replace") for rule in report_ids)
completed = (
    report.get("mode") == "audit" and report.get("errors") == [] and
    j["exit_code"] in (0, 1) and md["exit_code"] in (0, 1) and
    bool(report["findings"]) and markdown_has_all
)
negative_ok = (
    neg["exit_code"] == 2 and stdout_missing == b"" and
    b"ENOENT" in stderr_missing and not unavailable.exists()
)
unchanged = before == after and not status_before and not status_after
save("summary.json", {
    "started_at_utc": began, "finished_at_utc": utc(),
    "whole_script_elapsed_seconds": time.monotonic() - started,
    "tool_sha": EXPECTED["tool"], "target_sha": EXPECTED["target"],
    "published_guide_sha": EXPECTED["guide"], "report_schema": report.get("schemaVersion"),
    "report_tool_version": report.get("toolVersion"),
    "report_profile": report.get("profile"), "findings": len(report["findings"]),
    "status_counts": counts, "errors": report.get("errors"),
    "audit_json_exit": j["exit_code"], "audit_markdown_exit": md["exit_code"],
    "negative_exit": neg["exit_code"], "negative_stdout_bytes": len(stdout_missing),
    "negative_stderr_has_ENOENT": b"ENOENT" in stderr_missing,
    "target_manifest_unchanged": unchanged, "target_status_after": status_after,
    "target_entries": len(before), "markdown_mentions_all_rule_ids": markdown_has_all,
    "real_audit_complete": completed,
    "missing_target_handled_as_unavailable": negative_ok,
    "target_code_or_tests_invoked": False,
    "remediation_invoked": False, "git_issue_or_pr_published": False,
    "additional_independent_agent_adoption": "NOT RUN",
    "cross_host_isolation_certified": False,
})
print(json.dumps({
    "counts": counts, "audit_json_exit": j["exit_code"],
    "audit_markdown_exit": md["exit_code"], "negative_exit": neg["exit_code"],
    "negative_is_unavailable": negative_ok, "target_unchanged": unchanged,
    "complete": completed, "target_entries": len(before)
}, indent=2), flush=True)
if not (completed and negative_ok and unchanged):
    raise RuntimeError("Genuine Maintain workflow failed validation; see raw receipts")
