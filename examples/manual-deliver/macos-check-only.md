# Optional macOS Proofline check-only walkthrough

**ILLUSTRATIVE — NOT RUN.** Replay the frozen Python coding candidate from the
[real issue #21 trace](intentline-trace/README.md), with its historical native
evidence linked separately. Review the pins and authorize downloads, private
writes and selected tests before opting in. The direct path needs no Intentline
planning, approval service, server, coding agent or controller.

## Direct path

Run in order in **one Bash session**, with Git, npm and Python already installed.
Only the observed **macOS 15.7.9 ARM64 / Python 3.12.10 / native Codex 0.162.1**
combination is supported here. **Stop on drift**; other combinations need separate
qualification. Matching versions still requires native protection canaries.
Node/npm only installs Codex: use its Mach-O binary because the JavaScript
wrapper cannot find Node inside this sandbox.

```bash
set -euo pipefail
umask 077
test "$(uname -s)" = Darwin
test "$(uname -m)" = arm64
test "$(sw_vers -productVersion)" = 15.7.9
PYTHON="$(python3 -B -c 'import os,sys; print(os.path.realpath(sys.executable))')"
test "$("$PYTHON" -B -c 'import platform; print(platform.python_version())')" = 3.12.10
WORK="$(mktemp -d "${TMPDIR:-/tmp}/foundryline-check.XXXXXXXX")"
OUT="$WORK/evidence"
mkdir "$OUT"
export PYTHON OUT

# Full, detached source checkouts; no dependency installation in the candidate.
PRODUCT="$WORK/candidate"
PROOFLINE="$WORK/proofline"
git init -q "$PRODUCT"
git -C "$PRODUCT" fetch https://github.com/grove/foundryline.git f54d44eb1d21fae2d7cfd8aae4216e91019a87d3
git -C "$PRODUCT" checkout -q --detach FETCH_HEAD
git init -q "$PROOFLINE"
git -C "$PROOFLINE" fetch https://github.com/grove/proofline.git 8e117fff4de2459637fe7f74f47ab17fc3341d84
git -C "$PROOFLINE" checkout -q --detach FETCH_HEAD
test "$(git -C "$PRODUCT" rev-parse HEAD)" = f54d44eb1d21fae2d7cfd8aae4216e91019a87d3
test "$(git -C "$PRODUCT" rev-parse 'HEAD^{tree}')" = a003d013419fd1f142f0d05175938c6b0d7008f3
test "$(git -C "$PROOFLINE" rev-parse HEAD)" = 8e117fff4de2459637fe7f74f47ab17fc3341d84
test -z "$(git -C "$PRODUCT" status --porcelain --untracked-files=all)"
test -z "$(git -C "$PROOFLINE" status --porcelain --untracked-files=all)"

npm install --prefix "$WORK/codex" @openai/codex@0.162.1 --ignore-scripts --no-audit --no-fund
NATIVE="$(find "$WORK/codex/node_modules/@openai" -type f -path '*/vendor/aarch64-apple-darwin/bin/codex' -print -quit)"
test -n "$NATIVE" && test -x "$NATIVE"
file "$NATIVE" | /usr/bin/grep -q 'Mach-O.*arm64'
test "$("$NATIVE" --version)" = 'codex-cli 0.162.1'
mkdir "$WORK/bin"
ln -s "$NATIVE" "$WORK/bin/codex"
export PATH="$WORK/bin:$PATH"
test "$(command -v codex)" = "$WORK/bin/codex"
test "$(codex --version)" = 'codex-cli 0.162.1'

# Exact complete historical issue #21 body, not a new task or inferred approval.
cp "$PRODUCT/examples/manual-deliver/intentline-trace/export/source-S1.txt" "$OUT/source-S1.txt"
test "$(shasum -a 256 "$OUT/source-S1.txt" | cut -d ' ' -f 1)" = 3c1a808cc0dfad337b88f47b61a7513182c829ab0a96efbcf8bc443c07a343bf
{
  sw_vers; uname -m; "$PYTHON" --version; codex --version
  file "$NATIVE"
  git -C "$PRODUCT" rev-parse HEAD 'HEAD^{tree}'
  git -C "$PROOFLINE" rev-parse HEAD
  shasum -a 256 "$OUT/source-S1.txt"
} > "$OUT/identity.txt"
git -C "$PRODUCT" bundle create "$OUT/candidate.bundle" HEAD
```

Select source-byte/citation integrity (R1) separately from retained export
identity (R2). These are narrow checks for this historical task. Generate full
argv arrays with your actual interpreter:

```bash
"$PYTHON" -B - <<'PY'
import json, os
from pathlib import Path
out = Path(os.environ["OUT"])
base = [os.environ["PYTHON"], "-B", "-m", "unittest", "discover", "-s", "checks",
        "-p", "test_intentline_trace.py", "-k"]
r1 = base + ["test_complete_source_and_citations", "-v"]
r2 = base + ["test_export_completion_and_file_identities", "-v"]
(out / "r1-checks.json").write_text(json.dumps([r1]) + "\n")
(out / "r1-r2-checks.json").write_text(json.dumps([r1, r2]) + "\n")
PY

# Retain failures as well as successes; never let shell errexit discard readback.
check_candidate() {
  local name="$1" checks="$2" code=0 readback=0
  shift 2
  local command=("$PYTHON" -B "$PROOFLINE/proofline.py" check
    --repo "$PRODUCT" --source "$OUT/source-S1.txt" --checks "$checks"
    --seconds 200 --check-seconds 40 --output "$OUT/$name-record" "$@")
  printf '%q ' "${command[@]}" > "$OUT/$name.argv"
  pwd > "$OUT/$name.cwd"
  "${command[@]}" > "$OUT/$name.stdout" 2> "$OUT/$name.stderr" || code=$?
  printf '%s\n' "$code" > "$OUT/$name.exit"
  if test -f "$OUT/$name-record/report.json"; then
    "$PYTHON" -B "$PROOFLINE/proofline.py" status \
      "$OUT/$name-record/report.json" --show-source \
      > "$OUT/$name-status.stdout" 2> "$OUT/$name-status.stderr" || readback=$?
    printf '%s\n' "$readback" > "$OUT/$name-status.exit"
    cat "$OUT/$name-status.stdout" "$OUT/$name-status.stderr"
  else
    cat "$OUT/$name.stderr"
  fi
  printf '%s: check exit %s (inspect raw outputs)\n' "$name" "$code"
}
check_candidate direct "$OUT/r1-checks.json"
```

The direct route imports **no R IDs**; R2–R7 remain **NOT DEMONSTRATED** by this
selection. Before continuing, inspect `report.json` → `boundary.assessment` and
the raw preflight receipt. Proofline's canaries must observe denied writes to
source/input/candidate/Git HEAD/receipts, denied private receipt/oracle/other-role/
`actual_oracle` reads, denied mode changes and network, permitted scratch writes,
and unchanged inputs. Missing/unverified protection means **EXECUTION UNAVAILABLE**:
stop and retain the refusal. Never alter permissions or substitute unprotected execution.

## Optional: genuine initial-S1 export and exact requirement map

Skip for the direct route. Reuse the **actual unedited** [export](intentline-trace/export/export-manifest.json)
from Intentline `25e926f57e69395193fc0ac258f9e6dd2332cb18`, without installing it.
[Producer provenance/CLI receipts](intentline-trace/README.md#actual-producer-advisory-draft)
retain the genuine initial schema-1/revision-1 S1: advisory, **unapproved**, seven
R IDs, no open decisions. Inspect its complete source, contract and constraints.
For your own task use the [optional producer procedure](../../patterns/deliver.md#optional-intentline-json-export--proofline-evidence-map);
never manufacture an export or relabel these historical requirements as yours.

```bash
cp -R "$PRODUCT/examples/manual-deliver/intentline-trace/export" "$OUT/export"
cmp "$OUT/source-S1.txt" "$OUT/export/source-S1.txt"
"$PYTHON" -B - <<'PY'
import json, os
from pathlib import Path
out = Path(os.environ["OUT"])
r1, r2 = json.loads((out / "r1-r2-checks.json").read_text())
gap = {"R1": [{"index": 0, "argv": r1}]}
linked = {**gap, "R2": [{"index": 1, "argv": r2}]}
wrong = {"R1": [{"index": 0, "argv": ["/nonexistent/mismatched-argv"]}]}
for name, links in (("gap", gap), ("linked", linked), ("wrong", wrong)):
    (out / (name + "-links.json")).write_text(json.dumps(links) + "\n")
PY
check_candidate gap "$OUT/r1-checks.json" \
  --intentline-export "$OUT/export" --intentline-links "$OUT/gap-links.json"
check_candidate linked "$OUT/r1-r2-checks.json" \
  --intentline-export "$OUT/export" --intentline-links "$OUT/linked-links.json"
check_candidate wrong "$OUT/r1-checks.json" \
  --intentline-export "$OUT/export" --intentline-links "$OUT/wrong-links.json"
```

The [historical native run](intentline-trace/README.md#exact-selections-and-observed-gap)
observed `gap`: R1 **LINKED CHECKS PASSED (limited evidence)**, R2–R7 **NOT DEMONSTRATED**;
then `linked`: R1/R2 limited passes, R3–R7 **NOT DEMONSTRATED**, on identical
candidate/export. Both retained `coverage_completeness: UNKNOWN`, not source acceptance.
The [real wrong-map refusal](intentline-trace/README.md#actual-refusal-and-counterevidence)
exited **1**: `Intentline R check index/argv differs from the selected command`.
No check/report was produced; this was import rejection, not a product failure.
Retain your actual outcomes, never substitute the historical expected results.

## Readback, retention and handoff

| Actual result | What to report |
| --- | --- |
| CHECKS PASSED (normally exit 0) | Only the selected commands passed; inspect raw receipts and boundary. |
| CHECKS FAILED (normally exit 1) | A command actually ran and exited nonzero; retain its stdout/stderr. A launch failure is not proof of a product defect. |
| CHECKS UNAVAILABLE / EXECUTION UNAVAILABLE (normally exit 2) | Missing executable, timeout, inadequate evidence or unverified native boundary; no PASS or product-failure inference. |
| Import rejection / no report | Preserve stderr and exit; no selected-check verdict. |
| STALE CHECKS on readback | Identities no longer match; preserve the old record and start a new check. |

For an optional explicit contrast on a qualified host, select these two
diagnostic controls separately. The intentional assertion should yield **CHECKS
FAILED**; the absent executable should yield **CHECKS UNAVAILABLE**. Neither
demonstrates a product defect, and an unavailable boundary supersedes both:

```bash
"$PYTHON" -B - <<'PY'
import json, os
from pathlib import Path
out = Path(os.environ["OUT"])
(out / "failed-checks.json").write_text(json.dumps([
    [os.environ["PYTHON"], "-B", "-c", "raise AssertionError('intentional diagnostic control')"]]) + "\n")
(out / "unavailable-checks.json").write_text(json.dumps([
    ["/nonexistent/foundryline-negative-check"]]) + "\n")
PY
check_candidate failed "$OUT/failed-checks.json"
check_candidate unavailable "$OUT/unavailable-checks.json"
```

The [real missing-command control](native-qualification.md) was **CHECKS UNAVAILABLE**;
the [local boundary refusal](intentline-trace/README.md#actual-refusal-and-counterevidence)
was **EXECUTION UNAVAILABLE**, without selected checks. Neither can be relabeled
PASS. `status` verifies record integrity, not check success. Every new command
block, including these controls, remains **ILLUSTRATIVE — NOT RUN**.

Keep the **whole original record directories**, including `report.json`,
`evidence.json`, `receipts/`, preflight receipts and frozen `inputs/` (including
dotfiles and Git metadata). Preserve the copied source/export, selected JSON,
argv/cwd, stdout/stderr/exits and actual identity file alongside them. Do not
rewrite raw JSON to make paths portable or replace it with a summary.

```bash
tar -czf "$WORK/evidence.tgz" -C "$WORK" evidence
shasum -a 256 "$WORK/evidence.tgz"
printf 'Retain privately before deleting temporary work: %s\n' "$WORK/evidence.tgz"
```

Copy to durable private storage **before** deleting `$WORK` or losing the host.
Read back on the original host first: absolute-path-bound `status` need not replay
elsewhere. The [historical raw ZIP](intentline-trace/native-run.zip) separately
retains original `report.json`/`evidence.json`; it is not your new output.

Handoff in one paragraph: **source** issue URL + SHA-256; **candidate** exact
commit/tree above (not later PR HEAD); **commands** full selected argv JSON;
**actual host/tools** `identity.txt` + canary outcome; **outputs** durable archive
link + digest and report/receipt paths; **results/gaps** actual statuses, unlinked
R IDs and coverage UNKNOWN. Record elapsed time from reports; check-only model
dispatches are 0, while coding tokens, billing and total operator time remain
unknown unless measured. This documentation task runs no A/B study and makes no
quality or savings claim; see the coordinated [Proofline #52 overhead record](https://github.com/grove/proofline/issues/52#issuecomment-6251043392).

No GitHub Actions workflow is needed here. If adapting this to Actions, use only
a **temporary, branch-scoped, least-privilege diagnostic** (`contents: read`,
checkout credentials disabled, exact candidate/tool/action pins, finite timeout,
raw upload even on failure). Retain/download outputs including hidden files and
remove the probe from the PR **after a real run**. It is not a standing scheduler,
agent launcher or publisher and will not work on arbitrary CI hosts. No durable
privileged workflow, permission-bypass fallback, broader release qualification,
push, PR, merge or deployment authority is supplied by this example.
