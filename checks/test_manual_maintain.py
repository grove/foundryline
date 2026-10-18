"""Check retained Maintain evidence, without installing or executing RepoTend.

Hashes check artifact consistency, not historical authenticity or host isolation.
"""

import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples/repo-maintenance'
RECEIPTS = EXAMPLE / 'receipts'
TOOL_SHA = '2d69cce901475380775f674b9cc5755f1f89f82e'
TARGET_SHA = '5dc1dd15836584a1112caec224d479df8deffc9f'
LOCK_SHA = 'f17806903690e3f2058655ff974ed45a27ee894cceccd8f54ac50e8c8108d0b6'


def read_json(path):
    return json.loads(path.read_text())


class ManualMaintainTests(unittest.TestCase):
    def test_tool_and_target_identities_and_unchanged_files(self):
        env = read_json(RECEIPTS / 'environment.json')
        self.assertEqual(env['tool']['commit'], TOOL_SHA)
        self.assertEqual(env['tool']['lockfile_sha256'], LOCK_SHA)
        self.assertEqual(env['target']['commit'], TARGET_SHA)
        before, after = env['target']['files_before'], env['target']['files_after']
        self.assertEqual(len(before), 48)
        self.assertEqual(before, after)
        self.assertIn('.github/workflows/reference-checks.yml', before)
        for flag in ('target_code_executed', 'target_dependency_install',
                     'remediation_invoked', 'github_writes_during_audit'):
            self.assertIs(env[flag], False)

    def test_process_receipts_bind_commands_exits_and_raw_bytes(self):
        for name, exit_code in [('setup', 0), ('audit-json', 0),
                                ('audit-markdown', 0), ('missing-target', 2)]:
            with self.subTest(name=name):
                folder = RECEIPTS / name
                command = read_json(folder / 'command.json')
                self.assertEqual(command['exit_code'], exit_code)
                self.assertGreater(command['elapsed_seconds'], 0)
                self.assertTrue(command['started_at_utc'].endswith('+00:00'))
                self.assertEqual(command['cwd'], '/private/tmp/foundryline-maintain/tool')
                for stream in ['stdout', 'stderr']:
                    info = command[stream]
                    raw = (folder / info['file']).read_bytes()
                    self.assertEqual(len(raw), info['bytes'])
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), info['sha256'])
                argv = command['argv']
                if name == 'setup':
                    self.assertEqual(argv[:5], ['npm', 'ci', '--ignore-scripts', '--no-audit', '--no-fund'])
                else:
                    target = 'unavailable-target' if name == 'missing-target' else 'target'
                    output_format = 'markdown' if name == 'audit-markdown' else 'json'
                    self.assertEqual(argv, ['node', 'skills/repotend/scripts/audit.mjs',
                                           '--root', f'/private/tmp/foundryline-maintain/{target}',
                                           '--format', output_format])

    def test_completed_reports_preserve_actual_findings(self):
        report = read_json(RECEIPTS / 'audit-json/report.json')
        self.assertEqual((report['mode'], report['schemaVersion'], report['toolVersion']),
                         ('audit', '0.1', '0.1.0'))
        self.assertEqual(report['repository'], {'path': '.'})
        self.assertEqual(report['profile'], 'small-oss')
        self.assertEqual(report['errors'], [])
        self.assertEqual(Counter(f['status'] for f in report['findings']), {'PASS': 6, 'WARN': 7})
        expected = {
            'repo.license-present': ('PASS', 'verified'),
            'repo.contributing': ('WARN', 'verified'),
            'repo.code-of-conduct': ('WARN', 'verified'),
            'repo.security-policy': ('WARN', 'verified'),
            'repo.pr-template': ('WARN', 'verified'),
            'repo.issue-templates': ('WARN', 'verified'),
            'dx.editorconfig': ('WARN', 'verified'),
            'ci.workflow-validity': ('PASS', 'verified'),
            'security.workflow-permissions': ('PASS', 'heuristic'),
            'ci.concurrency': ('WARN', 'heuristic'),
            'ci.duplicate-triggers': ('PASS', 'heuristic'),
            'ci.path-filter-safety': ('PASS', 'heuristic'),
            'security.action-pinning': ('PASS', 'verified'),
        }
        self.assertEqual({f['ruleId']: (f['status'], f['confidence']) for f in report['findings']}, expected)
        markdown = (RECEIPTS / 'audit-markdown/report.md').read_text()
        for finding in report['findings']:
            self.assertIn(f"| {finding['status']} | `{finding['ruleId']}` | {finding['summary']} |", markdown)
            self.assertFalse(finding['enforced'])
            self.assertTrue(finding['ruleVersion'])
            self.assertTrue(finding['evidence'])

    def test_missing_target_is_not_a_completed_or_clean_audit(self):
        folder = RECEIPTS / 'missing-target'
        self.assertEqual(read_json(folder / 'command.json')['exit_code'], 2)
        self.assertEqual((folder / 'stdout.txt').read_bytes(), b'')
        self.assertIn('RepoTend audit failed: ENOENT', (folder / 'stderr.txt').read_text())
        self.assertFalse((folder / 'report.json').exists())
        self.assertFalse((folder / 'report.md').exists())
        guide = (ROOT / 'patterns/maintain.md').read_text()
        for phrase in ('UNAVAILABLE / INCOMPLETE', 'UNAVAILABLE / NOT RUN',
                       'never clean PASS', 'no completed JSON report'):
            self.assertIn(phrase, guide)

    def test_separate_adoption_retains_success_and_failure_evidence(self):
        folder = RECEIPTS / 'adoption'
        attempt = read_json(folder / 'attempt.json')
        self.assertEqual(attempt['toolCommit'], TOOL_SHA)
        self.assertEqual(attempt['targetCommit'], TARGET_SHA)
        self.assertEqual(attempt['toolLockfileSha256'], LOCK_SHA)
        self.assertGreater(attempt['elapsedSeconds'], 0)
        self.assertNotEqual(attempt['workDirectory'], '/private/tmp/foundryline-maintain')
        for filename, digest in read_json(folder / 'sha256.json').items():
            with self.subTest(filename=filename):
                self.assertEqual(hashlib.sha256((folder / filename).read_bytes()).hexdigest(), digest)
        commands = {c['label']: c for c in map(json.loads, (folder / 'commands.jsonl').read_text().splitlines())}
        self.assertEqual(len(commands), 13)
        for label, command in commands.items():
            expected_exit = 2 if label == 'negative' else 0
            self.assertEqual(command['exitCode'], expected_exit)
            self.assertEqual(int((folder / f'{label}.exit.txt').read_text()), expected_exit)
            self.assertTrue((folder / command['stdout']).is_file())
            self.assertTrue((folder / command['stderr']).is_file())
        for name, primary in [('report.json', 'audit-json'), ('report.md', 'audit-markdown')]:
            self.assertEqual((folder / name).read_bytes(), (RECEIPTS / primary / name).read_bytes())
        for stage in ['before', 'after']:
            self.assertEqual((folder / f'target-status-{stage}.stdout.txt').read_bytes(), b'')
        self.assertEqual((folder / 'negative.stdout.txt').read_bytes(), b'')
        self.assertIn('ENOENT', (folder / 'negative.stderr.txt').read_text())
        self.assertIn('shared host', (EXAMPLE / 'adoption.md').read_text())

    def test_lookup_and_unpublished_decision_are_honest(self):
        lookup = read_json(RECEIPTS / 'lookup.json')
        for filename, count in [('issues.json', 4), ('pull-requests.json', 9)]:
            raw = (RECEIPTS / filename).read_bytes()
            meta = lookup['outputs'][filename]
            self.assertEqual(meta['count'], count)
            self.assertEqual(len(json.loads(raw)), count)
            self.assertEqual(meta['sha256'], hashlib.sha256(raw).hexdigest())
            self.assertIn('all', meta['argv'])
        proposal = (EXAMPLE / 'issue-proposal.md').read_text()
        for phrase in ('NOT PUBLISHED', 'PROPOSED — NOT RUN', 'NEEDS_DECISION',
                       'not an accepted unmet requirement'):
            source = (EXAMPLE / 'README.md').read_text() if phrase == 'NEEDS_DECISION' else proposal
            self.assertIn(phrase, source)


if __name__ == '__main__':
    unittest.main()
