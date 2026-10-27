"""Offline billing-boundary and shell regressions; no provider calls."""
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from island import runner, council, z_desk

ROOT = Path(__file__).resolve().parents[1]
SPEC = {'title': 'test', 'question': 'Q', 'context': '', 'chair_model': 'chair',
        'blind_round': False, 'subs': [{'model': 'sub', 'brief': 'review'}]}


class ReceiptRepairs(unittest.TestCase):
    def provider(self, cost, text='answer', missing=False):
        data = {'id': 'receipt-test-id', 'choices': [{'message': {'content': text}}],
                'usage': {} if missing else {'cost': cost}}
        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', return_value=io.StringIO(json.dumps(data))):
            return runner.openrouter_answer('A', 'model', [], None)

    def test_raw_invalid_costs_never_become_numbers(self):
        for bad in (None, True, False, '1', -1, float('nan'), float('inf'), -float('inf')):
            with self.subTest(cost=bad):
                self.assertIsNone(self.provider(bad)['usage']['cost_usd'])
        self.assertIsNone(self.provider(None, missing=True)['usage']['cost_usd'])

    def test_raw_numeric_costs(self):
        for cost in (0, 0.0, 1, .25):
            self.assertEqual(self.provider(cost)['usage']['cost_usd'], float(cost))

    def execute(self, component, answer, cap=10):
        with tempfile.TemporaryDirectory() as tmp, patch('sys.stderr', new_callable=io.StringIO) as warning:
            out = Path(tmp) / 'run'
            if component == 'runner':
                result = runner.run('demo', '', '', '', '', 'Q', 2, cap, out, answer=answer, pace='off')
            elif component == 'council':
                result = council.run_council('demo', SPEC, cap, out, answer=answer, pace='off')
            else:
                result = z_desk.run('demo', ['diff', 'man'], {'diff': 'd', 'man': 'm'},
                                    'review', cap, out, answer=answer, pace='off')
            events = [json.loads(x) for x in (out / 'bus.jsonl').read_text().splitlines()]
            return result, events, (out / 'report.md').read_text(), warning.getvalue()

    def test_empty_text_known_and_unknown_charges_all_callers(self):
        for component in ('runner', 'council', 'desk'):
            for cost in (.3, None):
                with self.subTest(component=component, cost=cost):
                    first = self.provider(cost, text='')
                    responses = iter([first, self.provider(.2)])
                    result, events, report, warning = self.execute(component, lambda *a: next(responses))
                    receipts = [e for e in events if e['type'] == 'cost_receipt']
                    self.assertEqual(receipts[0]['cost_usd'], cost)
                    self.assertEqual(receipts[0]['response_id'], 'receipt-test-id')
                    self.assertEqual(result['totals']['unknown_cost_calls'], int(cost is None))
                    expected = (cost or 0) + (.2 if component == 'desk' else 0)
                    self.assertAlmostEqual(result['totals']['cost_usd'], expected)
                    self.assertEqual(sum(e['type'] == 'error' for e in events), 1)
                    self.assertEqual(sum(e['type'] in ('turn', 'consult') for e in events), int(component == 'desk'))
                    self.assertIn('Unknown charge attempts:', report)
                    self.assertEqual('WARNING: cost UNKNOWN' in warning, cost is None)

    def test_unknown_cost_with_usable_text_continues_all_callers(self):
        for component, expected_calls in (('runner', 2), ('council', 3), ('desk', 2)):
            calls = []
            def answer(*args):
                calls.append(args[0])
                return self.provider(False if len(calls) == 1 else .2)
            result, events, _, warning = self.execute(component, answer)
            self.assertEqual(len(calls), expected_calls)
            self.assertEqual(result['totals']['unknown_cost_calls'], 1)
            self.assertAlmostEqual(result['totals']['cost_usd'], .2 * (expected_calls - 1))
            self.assertIn('WARNING: cost UNKNOWN', warning)
            self.assertEqual(events[-1]['type'], 'stop')

    def test_desk_known_charge_for_empty_text_honors_soft_cap(self):
        calls = []
        def answer(*args):
            calls.append(args[0])
            return self.provider(.6, text='')
        result, _, _, _ = self.execute('desk', answer, cap=.5)
        self.assertEqual(calls, ['diff'])
        self.assertEqual(result['totals']['cost_usd'], .6)

    def test_stop_interrupt_propagates_without_peer_call(self):
        for component in ('runner', 'council', 'desk'):
            calls = []
            def answer(*args):
                calls.append(args[0])
                raise KeyboardInterrupt('owner STOP')
            with self.assertRaises(KeyboardInterrupt):
                self.execute(component, answer)
            self.assertEqual(len(calls), 1)


class MatrixRepairs(unittest.TestCase):
    def test_all_success_mixed_and_all_failure_keep_nine_receipts(self):
        for fail, count in (('', 0), ('expert-C2 sub-C1', 2), ('all', 9)):
            with self.subTest(fail=fail), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / 'scripts').mkdir()
                (root / 'scripts/run-matrix.sh').write_text((ROOT / 'scripts/run-matrix.sh').read_text())
                (root / 'scripts/run.sh').write_text('''#!/bin/sh
mkdir -p "runs/$1"
echo receipt > "runs/$1/receipt.txt"
echo "$1" >> attempts
case " $FAIL_STEMS " in
  *" $1 "*|" all ") exit 1 ;;
esac
exit 0
''')
                result = subprocess.run(['sh', 'scripts/run-matrix.sh'], cwd=root, text=True,
                                        capture_output=True, env={'PATH': '/usr/bin:/bin',
                                        'OPENROUTER_API_KEY': 'offline-dummy', 'FAIL_STEMS': fail})
                self.assertEqual(result.returncode, int(count > 0))
                self.assertEqual(len((root / 'attempts').read_text().splitlines()), 9)
                self.assertEqual(len(list(root.glob('runs/*/receipt.txt'))), 9)
                self.assertIn(f'{9-count} ok, {count} failed', result.stdout)
