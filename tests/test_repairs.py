"""Offline billing boundaries and real CLI/shell propagation; no provider calls."""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

from island import runner, council, z_desk

ROOT = Path(__file__).resolve().parents[1]
SPEC = {'title': 'test', 'question': 'Q', 'context': '', 'chair_model': 'fake/chair',
        'blind_round': False, 'subs': [{'model': 'fake/sub', 'brief': 'review'}]}
STEMS = ('expert-C1 expert-C2 expert-C3 sub-C1 sub-C2 sub-C3 '
         'heldout-C1 heldout-C2 heldout-C3').split()
FAKE_ENV = {'PATH': os.environ['PATH'], 'OPENROUTER_API_KEY': 'offline-fake-key'}
BAD_COSTS = (None, True, False, '1', -1, float('nan'), float('inf'), -float('inf'), [], {})


def provider(cost, text='answer', missing=False, finish='stop'):
    data = {'id': 'receipt-test-id', 'choices': [{'message': {'content': text},
            'finish_reason': finish}], 'usage': {} if missing else {'cost': cost}}
    with patch.dict(os.environ, FAKE_ENV, clear=True), \
         patch('island.runner.urlopen', return_value=io.StringIO(json.dumps(data))) as http:
        result = runner.openrouter_answer('A', 'fake/model', [], None)
    if http.call_count != 1:
        raise AssertionError('a completion must not be automatically retried')
    return result


class ReceiptRepairs(unittest.TestCase):
    def execute(self, component, answer, cap=10):
        with tempfile.TemporaryDirectory() as tmp, \
             patch.dict(os.environ, FAKE_ENV, clear=True), \
             patch('sys.stderr', new_callable=io.StringIO) as warning, \
             patch('island.runner.time.sleep'):
            out = Path(tmp) / 'run'
            if component == 'runner':
                result = runner.run('demo', '', '', '', '', 'Q', 3, cap, out,
                                    answer=answer, pace='off')
            elif component == 'council':
                result = council.run_council('demo', SPEC, cap, out, answer=answer, pace='off')
            else:
                result = z_desk.run('demo', ['diff', 'man'], {'diff': 'fake/d', 'man': 'fake/m'},
                                    'review', cap, out, answer=answer, pace='off')
            raw = (out / 'bus.jsonl').read_text()
            # Reject nonstandard JSON numbers anywhere, including usage diagnostics.
            def invalid_constant(value):
                raise AssertionError('nonfinite receipt: ' + value)
            events = [json.loads(x, parse_constant=invalid_constant) for x in raw.splitlines()]
            self.assertEqual(events[-1]['type'], 'stop')
            self.assertEqual(events[-1]['reason'], result['stop'])
            self.assertEqual(events[-1]['totals'], result['totals'])
            self.assertTrue((out / ('consult.md' if component == 'desk' else 'transcript.md')).is_file())
            return result, events, (out / 'report.md').read_text(), warning.getvalue()

    def test_raw_invalid_costs_are_explicit_accounting_failures(self):
        for bad in (*BAD_COSTS, 10**400):
            with self.subTest(cost=str(bad)[:20]):
                result = provider(bad)
                self.assertIsNone(result['usage']['cost_usd'])
                self.assertEqual(result['failure'], 'accounting_uncertain')
        self.assertIsNone(provider(None, missing=True)['usage']['cost_usd'])

    def test_raw_numeric_zero_and_positive_costs(self):
        for cost in (0, 0.0, 1, .25):
            result = provider(cost)
            self.assertEqual(result['usage']['cost_usd'], float(cost))
            self.assertIsNone(result['failure'])

    def test_empty_completion_carries_known_or_unknown_cost_without_retry(self):
        for cost in (0, .3, *BAD_COSTS):
            with self.subTest(cost=cost):
                result = provider(cost, text='  ', finish='length')
                known = runner.valid_cost(cost)
                self.assertEqual(result['usage']['cost_usd'], known)
                self.assertEqual(result['failure'], 'error' if known is not None else 'accounting_uncertain')
                self.assertEqual(result['attempts'], 1)

    def test_first_or_later_failed_completion_all_callers(self):
        for component in ('runner', 'council', 'desk'):
            for prior in (False, True):
                for cost in (0, .3, *BAD_COSTS):
                    with self.subTest(component=component, prior=prior, cost=cost):
                        responses = ([provider(.2)] if prior else []) + [provider(cost, text='')]
                        calls = []
                        def answer(*args):
                            calls.append(args[0])
                            return responses[len(calls) - 1]
                        result, events, report, warning = self.execute(component, answer)
                        known = runner.valid_cost(cost)
                        expected = (.2 if prior else 0) + (known or 0)
                        self.assertAlmostEqual(result['totals']['cost_usd'], expected)
                        self.assertEqual(len(calls), 1 + int(prior))
                        receipts = [e for e in events if e['type'] == 'cost_receipt']
                        self.assertEqual(len(receipts), len(calls))
                        self.assertEqual(receipts[-1]['cost_usd'], known)
                        self.assertEqual(receipts[-1]['response_id'], 'receipt-test-id')
                        self.assertEqual(sum(e['type'] in ('turn', 'consult') for e in events), int(prior))
                        self.assertEqual(sum(e['type'] == 'error' for e in events), 1)
                        self.assertFalse(any(e['type'] == 'retry' for e in events))
                        self.assertEqual(result['totals']['unknown_cost_calls'], int(known is None))
                        self.assertEqual(runner.result_exit_code(result), 2 if known is None else 1)
                        self.assertEqual(result['stop'], 'accounting_uncertain' if known is None else 'error')
                        self.assertEqual(result['totals']['accounting_status'], 'UNKNOWN' if known is None else 'KNOWN')
                        self.assertEqual(result['totals']['total_cost_usd'], None if known is None else expected)
                        self.assertIn('Known reported cost:', report)
                        self.assertIn('Unknown charge attempts:', report)
                        self.assertEqual('WARNING: cost UNKNOWN' in warning, known is None)

    def test_usable_text_with_unknown_cost_stops_all_callers(self):
        for component in ('runner', 'council', 'desk'):
            for cost in BAD_COSTS:
                with self.subTest(component=component, cost=cost):
                    calls = []
                    def answer(*args):
                        calls.append(args[0])
                        return {'text': 'unmetered answer', 'usage': {'cost_usd': cost}}
                    result, events, report, _ = self.execute(component, answer)
                    self.assertEqual(len(calls), 1)
                    self.assertEqual(result['stop'], 'accounting_uncertain')
                    self.assertEqual(result['totals']['cost_usd'], 0)
                    self.assertIsNone(result['totals']['total_cost_usd'])
                    self.assertIn('Accounting: UNKNOWN', report)
                    self.assertFalse(any(e['type'] in ('turn', 'consult', 'retry') for e in events))

    def test_none_and_exception_preserve_prior_charges_and_reports(self):
        for component in ('runner', 'council', 'desk'):
            for failure in (None, RuntimeError('RAW_BODY secret prompt ' + 'x' * 1000)):
                with self.subTest(component=component, failure=type(failure).__name__):
                    calls = []
                    def answer(*args):
                        calls.append(args[0])
                        if len(calls) == 1:
                            return provider(.2)
                        if isinstance(failure, Exception):
                            raise failure
                        return failure
                    result, events, report, _ = self.execute(component, answer)
                    self.assertEqual(len(calls), 2)
                    self.assertEqual(result['totals']['cost_usd'], .2)
                    self.assertIsNone(result['totals']['total_cost_usd'])
                    self.assertEqual(result['totals']['unknown_cost_calls'], 1)
                    self.assertNotIn('RAW_BODY', json.dumps(events) + report)
                    self.assertEqual(len([e for e in events if e['type'] == 'cost_receipt']), 2)

    def test_transport_retries_remain_bounded_then_stop_before_peer(self):
        for component in ('runner', 'council', 'desk'):
            for recover in (False, True):
                with self.subTest(component=component, recover=recover):
                    calls = []
                    def answer(*args):
                        calls.append(args[0])
                        if recover and len(calls) == 2:
                            return provider(.1)
                        raise RuntimeError('OpenRouter HTTP 429 retry-after 1')
                    result, events, _, _ = self.execute(component, answer)
                    self.assertEqual(len(calls), 2 if recover else runner.RETRY_MAX + 1)
                    self.assertEqual(len(set(calls)), 1)
                    self.assertEqual(runner.result_exit_code(result), 2)
                    self.assertEqual(sum(e['type'] == 'retry' for e in events), 1 if recover else runner.RETRY_MAX)
                    self.assertFalse(any(e['type'] in ('turn', 'consult') for e in events))

    def test_no_raw_body_or_untrusted_diagnostics_in_errors(self):
        for component in ('runner', 'council', 'desk'):
            result = provider(.3, text='', finish='RAW_BODY secret ' + 'x' * 1000)
            _, events, _, _ = self.execute(component, lambda *args: result)
            self.assertNotIn('RAW_BODY', json.dumps(events))
            self.assertLess(len(next(e for e in events if e['type'] == 'error')['error']), 160)
        for header in ('RAW_BODY secret\n', '1 RAW_BODY', '9' * 1000):
            error = HTTPError('https://example.invalid', 429, 'RAW_BODY',
                              {'Retry-After': header}, io.BytesIO(b'RAW_BODY credential'))
            with patch.dict(os.environ, FAKE_ENV, clear=True), \
                 patch('island.runner.urlopen', side_effect=error):
                with self.assertRaisesRegex(RuntimeError, '^OpenRouter HTTP 429$') as caught:
                    runner.openrouter_answer('A', 'fake/model', [], '')
            self.assertNotIn('RAW_BODY', str(caught.exception))

    def test_malformed_json_is_unknown_without_body_in_errors(self):
        for component in ('runner', 'council', 'desk'):
            def answer(*args):
                with patch('island.runner.urlopen', return_value=io.StringIO('RAW_BODY credential')):
                    return runner.openrouter_answer('A', 'fake/model', [], '')
            result, events, report, _ = self.execute(component, answer)
            self.assertEqual(runner.result_exit_code(result), 2)
            self.assertEqual(result['totals']['unknown_cost_calls'], 1)
            self.assertNotIn('RAW_BODY', json.dumps(events) + report)
            self.assertFalse(any(e['type'] == 'retry' for e in events))

    def test_nonfinite_tokens_do_not_escape_into_receipts(self):
        for component in ('runner', 'council', 'desk'):
            answer = {'text': 'ok', 'usage': {'cost_usd': .1, 'total_tokens': float('nan'),
                      'prompt_tokens': float('inf'), 'completion_tokens': -float('inf')}}
            result, _, _, _ = self.execute(component, lambda *args: answer)
            self.assertEqual(runner.result_exit_code(result), 0)
            self.assertEqual(result['totals']['total_tokens'], 0)

    def test_completion_budget_and_reasoning_unchanged(self):
        captured = []
        def http(request, timeout=None):
            captured.append(json.loads(request.data))
            return io.StringIO(json.dumps({'choices': [{'message': {'content': 'ok'}}], 'usage': {'cost': 0}}))
        with patch.dict(os.environ, FAKE_ENV, clear=True), patch('island.runner.urlopen', side_effect=http):
            runner.openrouter_answer('A', 'fake/model', [], '')
        self.assertEqual(captured[0]['max_tokens'], 8192)
        self.assertEqual(captured[0]['reasoning'], {'effort': 'low'})

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
    def test_status_receipts_attempt_order_and_caps(self):
        cases = [('', '', 0, 9), (STEMS[0], '', 1, 9), (STEMS[-1], '', 1, 9),
                 ('all', '', 1, 9), ('', STEMS[0], 2, 1), (STEMS[0], STEMS[3], 2, 4),
                 ('', STEMS[-1], 2, 9)]
        for fail, unknown, code, count in cases:
            for cap in (None, '0.42'):
                with self.subTest(fail=fail, unknown=unknown, cap=cap), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    (root / 'scripts').mkdir()
                    shutil.copy(ROOT / 'scripts/run-matrix.sh', root / 'scripts/run-matrix.sh')
                    (root / 'scripts/run.sh').write_text('''#!/bin/sh
mkdir -p "runs/$1"
echo receipt > "runs/$1/receipt.txt"
echo "$1 $2" >> attempts
if [ "$1" = "$UNKNOWN_STEM" ]; then exit 2; fi
if [ "$FAIL_STEM" = all ] || [ "$FAIL_STEM" = "$1" ]; then exit 1; fi
exit 0
''')
                    command = ['sh', 'scripts/run-matrix.sh'] + ([] if cap is None else [cap])
                    result = subprocess.run(command, cwd=root, text=True, capture_output=True,
                                            env={**FAKE_ENV, 'FAIL_STEM': fail, 'UNKNOWN_STEM': unknown})
                    self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                    self.assertEqual((root / 'attempts').read_text().splitlines(),
                                     [stem + ' ' + (cap or '1') for stem in STEMS[:count]])
                    self.assertEqual(len(list(root.glob('runs/*/receipt.txt'))), count)
                    self.assertIn('per-run receipts under', result.stdout)
                    if unknown:
                        self.assertIn('accounting uncertainty', result.stdout)
                        self.assertIn('skipped stems:' + (' ' + ' '.join(STEMS[count:]) if count < 9 else ' none'), result.stdout)
                    else:
                        failures = 9 if fail == 'all' else int(bool(fail))
                        self.assertIn(f'{9-failures} ok, {failures} failed', result.stdout)


class CLIPropagation(unittest.TestCase):
    # Real subprocess CLIs and real run.sh; sitecustomize replaces urllib before
    # island imports it. A tiny environment provides fake keys and no credentials.
    HTTP_STUB = '''import io, json, os, urllib.request
calls = 0
def offline(request, timeout=None):
    global calls
    calls += 1
    with open(os.environ['ATTEMPTS'], 'a') as out:
        out.write('mock HTTP\\n')
    code = os.environ['RESULT_CODE']
    text = 'ok' if code == '0' else ''
    usage = {} if code == '2' else {'cost': 0.1}
    return io.StringIO(json.dumps({'choices': [{'message': {'content': text},
             'finish_reason': 'length'}], 'usage': usage}))
urllib.request.urlopen = offline
'''

    def test_cli_usage_errors_are_ordinary_failures(self):
        for entry in ('runner', 'council', 'z_desk'):
            result = subprocess.run([sys.executable, '-m', 'island.' + entry,
                                     '--mode', 'invalid-offline-mode'], cwd=ROOT,
                                    env=FAKE_ENV, text=True, capture_output=True)
            self.assertEqual(result.returncode, 1, result.stderr)

    def test_actual_cli_and_wrapper_status(self):
        for entry in ('runner', 'council', 'z_desk', 'wrapper'):
            for code in (0, 1, 2):
                with self.subTest(entry=entry, code=code), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    (root / 'sitecustomize.py').write_text(self.HTTP_STUB)
                    (root / 'seed.md').write_text('# fake\nquestion: offline Q\nchair: fake/chair\nsub: fake/sub :: review\n')
                    out = root / 'output'
                    if entry == 'wrapper':
                        (root / 'scripts').mkdir()
                        shutil.copy(ROOT / 'scripts/run.sh', root / 'scripts/run.sh')
                        (root / 'docs/seeds').mkdir(parents=True)
                        shutil.copy(root / 'seed.md', root / 'docs/seeds/eko-council-expert-C1.md')
                        # Pin python3 to the interpreter running these tests.
                        (root / 'bin').mkdir()
                        (root / 'bin/python3').symlink_to(sys.executable)
                        command = ['sh', 'scripts/run.sh', 'expert-C1', '.9']
                    else:
                        command = [sys.executable, '-m', 'island.' + entry, '--mode', 'live', '--pace', 'off', '--outdir', str(out)]
                        if entry == 'runner':
                            command += ['--model-a', 'fake/a', '--model-b', 'fake/b', '--turns', '2']
                        elif entry == 'council':
                            command += ['--council-file', str(root / 'seed.md')]
                        else:
                            command += ['--brief', 'offline review', '--diff-model', 'fake/d', '--man-model', 'fake/m']
                    env = {**FAKE_ENV, 'PATH': str(root / 'bin') + os.pathsep + FAKE_ENV['PATH'],
                           'PYTHONPATH': str(root) + os.pathsep + str(ROOT),
                           'ATTEMPTS': str(root / 'attempts'), 'RESULT_CODE': str(code)}
                    result = subprocess.run(command, cwd=root, env=env, text=True, capture_output=True, timeout=15)
                    self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                    if entry == 'wrapper':
                        out, = (root / 'runs').iterdir()
                    events = [json.loads(x) for x in (out / 'bus.jsonl').read_text().splitlines()]
                    self.assertEqual(events[-1]['type'], 'stop')
                    self.assertTrue((out / 'report.md').is_file())
                    if code:
                        self.assertEqual((root / 'attempts').read_text().splitlines(), ['mock HTTP'])
                        self.assertFalse(any(e['type'] in ('turn', 'consult', 'retry') for e in events))
                    if code == 2:
                        self.assertEqual(events[-1]['reason'], 'accounting_uncertain')
                        self.assertIsNone(events[-1]['totals']['total_cost_usd'])


if __name__ == '__main__':
    unittest.main()

