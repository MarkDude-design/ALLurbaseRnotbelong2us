import sys
import tempfile
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'transport'))
from wire0 import encode, decode, acknowledge, check_ack, accept, WireError

REF = 'MarkDude-design/Puppy#15@6451679731'
class Wire0(unittest.TestCase):
    def test_ascii_packet_fits_sms_sized_payload(self):
        p=encode(12,REF,'BLOCKED','CODEX_KEY404')
        self.assertLessEqual(len(p.encode('ascii')),160)
        self.assertEqual(decode(p)['next_code'],'CODEX_KEY404')
    def test_acked_fidelity_not_model_delivery(self):
        p=encode(12,REF,'BLOCKED','CODEX_KEY404')
        self.assertTrue(check_ack(p,acknowledge(p)))
    def test_corruption_rejected(self):
        p=encode(12,REF,'BLOCKED','CODEX_KEY404')
        with self.assertRaisesRegex(WireError,'CRC'):
            decode(p.replace('KEY404','KEY405'))
    def test_replay_and_conflicting_reuse(self):
        seen={}
        a=encode(12,REF,'WAIT','CODEX')
        b=encode(12,REF,'DONE','CODEX')
        self.assertEqual(accept(a,seen),'NEW')
        self.assertEqual(accept(a,seen),'DUPLICATE')
        self.assertEqual(accept(b,seen),'CONFLICT')
    def test_offline_spool_and_recover(self):
        p=encode(19,REF,'POSTED','Z_REVIEW')
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'outbox.txt'
            path.write_text(p+'\n',encoding='ascii')
            restored=path.read_text(encoding='ascii').strip()
            self.assertTrue(check_ack(restored,acknowledge(restored)))
    def test_long_or_private_freeform_rejected(self):
        with self.assertRaises(WireError):
            encode(1,REF,'POSTED','free text with spaces and credentials')
        with self.assertRaises(WireError):
            encode(1,'https://example.com/secret','POSTED','NEXT')
    def test_non_ascii_rejected(self):
        with self.assertRaises(WireError):
            decode(encode(1,REF,'WAIT','NEXT')+'💻')
    def test_ack_corruption_detected(self):
        p=encode(1,REF,'WAIT','NEXT')
        a=acknowledge(p)
        with self.assertRaisesRegex(WireError,'corrupted ACK'):
            check_ack(p,a[:-1] + ('0' if a[-1]!='0' else '1'))
    def test_ack_for_wrong_message_rejected(self):
        p=encode(1,REF,'WAIT','NEXT')
        wrong=encode(2,REF,'WAIT','NEXT')
        self.assertFalse(check_ack(p,acknowledge(wrong)))
if __name__=='__main__':
    unittest.main()
