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

    def test_completion_budget_covers_reasoning(self):
        # PAID-NO-TEXT ROOT CAUSE (runs 41505052609-1 + 41509741842, 2026-11-02):
        # max_tokens is the COMPLETION budget and covers reasoning + content
        # together. At 1600, low-effort reasoning starved content to empty
        # while the call still charged (~1600 completion tokens, no text).
        # At 4096 the same class struck twice more (runs 41515254395-1 +
        # 41515989287: completion_tokens exactly 4096, finish_reason "length",
        # no text). Pin the repair: 8192, reasoning effort low.
        data = {'id': 'budget-test-id', 'choices': [{'message': {'content': 'ok'},
                'finish_reason': 'stop'}], 'usage': {'cost': 0}}
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured['payload'] = json.loads(request.data.decode('utf-8'))
            return io.StringIO(json.dumps(data))

        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', side_effect=fake_urlopen):
            runner.openrouter_answer('A', 'model', [], None)
        self.assertEqual(captured['payload']['max_tokens'], 8192)
        self.assertEqual(captured['payload']['reasoning']['effort'], 'low')

    def test_empty_text_error_carries_finish_reason(self):
        # Same repair, diagnosis side: an empty-content miss receipts the
        # provider's finish_reason on the error event, so a future starve is
        # diagnosed on the bus instead of arriving as mystery money.
        for component in ('runner', 'council', 'desk'):
            with self.subTest(component=component):
                # LENGTH-RETRY LANE note: both HTTP attempts starve here, so
                # the runner's one bounded retry runs and still returns the
                # honest empty-text result with the finish_reason receipt.
                def fake_urlopen(request, timeout=None):
                    data = {'id': 'fr-test-id', 'choices': [{'message': {'content': ''},
                            'finish_reason': 'length'}], 'usage': {'cost': 0.3}}
                    return io.StringIO(json.dumps(data))
                with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
                     patch('island.runner.urlopen', side_effect=fake_urlopen):
                    first = runner.openrouter_answer('A', 'model', [], None)
                self.assertEqual(first['finish_reason'], 'length')
                self.assertEqual(first['attempts'], 2)  # retry fired, both starved
                responses = iter([first, self.provider(.2)])
                _, events, _, _ = self.execute(component, lambda *a: next(responses))
                errors = [e for e in events if e['type'] == 'error']
                self.assertEqual(len(errors), 1)
                self.assertIn('finish_reason: length', errors[0]['error'])

    def test_stop_interrupt_propagates_without_peer_call(self):
        for component in ('runner', 'council', 'desk'):
            calls = []
            def answer(*args):
                calls.append(args[0])
                raise KeyboardInterrupt('owner STOP')
            with self.assertRaises(KeyboardInterrupt):
                self.execute(component, answer)
            self.assertEqual(len(calls), 1)

    def test_length_retry_once_sums_costs(self):
        # LENGTH-RETRY LANE (owner-approved, 2026-11-02): content starved at
        # the cap (finish_reason "length", empty text — live receipts
        # 41515254395-1 + 41515989287 at 4096, ~$0.031 each) retries ONCE at
        # double budget; both attempts' charges sum into ONE receipt so the
        # wasted spend stays visible.
        first = {'id': 'len-1', 'choices': [{'message': {'content': ''},
                 'finish_reason': 'length'}], 'usage': {'cost': 0.03}}
        second = {'id': 'len-2', 'choices': [{'message': {'content': 'recovered'},
                 'finish_reason': 'stop'}], 'usage': {'cost': 0.01}}
        payloads = []

        def fake_urlopen(request, timeout=None):
            payloads.append(json.loads(request.data.decode('utf-8')))
            data = first if len(payloads) == 1 else second
            return io.StringIO(json.dumps(data))

        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', side_effect=fake_urlopen):
            result = runner.openrouter_answer('A', 'model', [], None)
        self.assertEqual(result['text'], 'recovered')
        self.assertEqual(result['attempts'], 2)
        self.assertTrue(result['length_retry'])
        self.assertEqual(result['first_attempt_cost_usd'], 0.03)
        self.assertAlmostEqual(result['usage']['cost_usd'], 0.04)
        self.assertEqual(len(payloads), 2)
        self.assertEqual(payloads[0]['max_tokens'], 8192)
        self.assertEqual(payloads[1]['max_tokens'], 16384)

    def test_length_retry_bounded_to_one(self):
        # A second starve returns the honest empty-text result: bounded at
        # one retry, no runaway spend loop.
        starved = {'id': 'x', 'choices': [{'message': {'content': ''},
                   'finish_reason': 'length'}], 'usage': {'cost': 0.03}}
        calls = []

        def fake_urlopen(request, timeout=None):
            calls.append(1)
            return io.StringIO(json.dumps(starved))

        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', side_effect=fake_urlopen):
            result = runner.openrouter_answer('A', 'model', [], None)
        self.assertEqual(result['attempts'], 2)
        self.assertEqual(len(calls), 2)
        self.assertEqual(result['text'], '')
        self.assertAlmostEqual(result['usage']['cost_usd'], 0.06)

    def test_no_length_retry_when_text_present(self):
        # Usable text is success: no retry, attempts=1 — even if the provider
        # stamped finish_reason "length".
        data = {'id': 'x', 'choices': [{'message': {'content': 'ok text'},
                'finish_reason': 'length'}], 'usage': {'cost': 0.01}}
        calls = []

        def fake_urlopen(request, timeout=None):
            calls.append(1)
            return io.StringIO(json.dumps(data))

        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', side_effect=fake_urlopen):
            result = runner.openrouter_answer('A', 'model', [], None)
        self.assertEqual(result['attempts'], 1)
        self.assertEqual(len(calls), 1)
        self.assertAlmostEqual(result['usage']['cost_usd'], 0.01)

    def test_unknown_charge_on_length_retry_stays_unknown(self):
        # If either attempt's charge is missing, the summed receipt stays
        # UNKNOWN (cost None) — never fabricate the wasted spend.
        first = {'id': 'len-1', 'choices': [{'message': {'content': ''},
                 'finish_reason': 'length'}], 'usage': {}}
        second = {'id': 'len-2', 'choices': [{'message': {'content': 'ok'},
                 'finish_reason': 'stop'}], 'usage': {'cost': 0.01}}

        def fake_urlopen(request, timeout=None):
            fake_urlopen.calls += 1
            data = first if fake_urlopen.calls == 1 else second
            return io.StringIO(json.dumps(data))

        fake_urlopen.calls = 0
        with patch.dict(os.environ, {'OPENROUTER_API_KEY': 'offline-dummy'}, clear=True), \
             patch('island.runner.urlopen', side_effect=fake_urlopen):
            result = runner.openrouter_answer('A', 'model', [], None)
        self.assertEqual(result['attempts'], 2)
        self.assertIsNone(result['usage']['cost_usd'])


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
