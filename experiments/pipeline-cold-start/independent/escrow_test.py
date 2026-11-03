"""Capability escrow: a tiny offline event reducer and its acceptance tests.

No network, filesystem persistence, clock daemon, model API, or native sessions.
Run: python3 escrow_test.py
"""
from copy import deepcopy
import unittest


class Rejected(ValueError):
    pass


CAPABILITIES = {
    "Mark": {"read", "write", "terminal"},
    "QC": {"read", "write", "terminal"},
    "Bing": {"read"},
    "Q": {"read", "write"},
    "Z": {"read"},
    "courier": {"relay"},
}


def envelope(event_id, actor, operation, **payload):
    return {"id": event_id, "actor": actor, "operation": operation,
            "payload": deepcopy(payload), "via": []}


def relay(original, courier):
    if "relay" not in CAPABILITIES.get(courier, set()):
        raise Rejected("courier lacks relay capability")
    forwarded = deepcopy(original)
    forwarded["via"].append(courier)
    return forwarded


class Escrow:
    def __init__(self):
        self.active = "Puppy"
        self.tickets = {}
        self.fragments = []
        self.events = []
        self.seen = {}

    def accept(self, incoming):
        e = deepcopy(incoming)
        fingerprint = {k: e[k] for k in ("id", "actor", "operation", "payload")}
        if e["id"] in self.seen:
            if self.seen[e["id"]] != fingerprint:
                raise Rejected("event id reused with different content")
            return "duplicate"
        actor, op, p = e["actor"], e["operation"], e["payload"]
        caps = CAPABILITIES.get(actor, set())
        if not caps:
            raise Rejected("unknown original actor")
        if op == "fragment":
            self.fragments.append({"project": p["project"], "text": p["text"]})
        elif op == "open":
            if actor != "Mark" or p["project"] != self.active or p["ticket"] in self.tickets:
                raise Rejected("only Mark opens a new active-project ticket")
            self.tickets[p["ticket"]] = {
                "project": p["project"], "repo": p["repo"], "needs": p["needs"],
                "holder": None, "generation": 0, "committed": [], "done": False,
            }
        elif op in {"claim", "replace", "checkpoint", "complete"}:
            t = self.tickets[p["ticket"]]
            if t["done"] or t["project"] != self.active or p["repo"] != t["repo"]:
                raise Rejected("closed, inactive, or wrong repository")
            if not set(t["needs"]).issubset(caps):
                raise Rejected("original actor lacks task capabilities")
            if op in {"claim", "replace"}:
                if p["generation"] != t["generation"]:
                    raise Rejected("stale claim generation")
                if op == "claim" and t["holder"] is not None:
                    raise Rejected("ticket already held")
                # Replacement is explicit, never caused by a timer or incoming chat.
                if op == "replace" and (actor != "Mark" or t["holder"] is None):
                    raise Rejected("only Mark replaces an interrupted claim")
                t["holder"] = actor
                t["generation"] += 1
            else:
                if actor != t["holder"] or p["generation"] != t["generation"]:
                    raise Rejected("stale or foreign holder")
                if p["cursor"] != len(t["committed"]):
                    raise Rejected("must continue from committed cursor")
                if op == "checkpoint":
                    t["committed"].append(p["result"])
                else:
                    t["done"] = True
        elif op == "question":
            if p["route"] != ["Z"]:
                raise Rejected("routine questions start with Z")
        elif op == "escalate":
            prior = next((x for x in self.events if x["id"] == p["question"]), None)
            if not prior or prior["operation"] != "question" or actor not in {"Z", "Mark"}:
                raise Rejected("Z or Mark must explicitly escalate a recorded question")
        else:
            raise Rejected("unknown operation")
        self.seen[e["id"]] = fingerprint
        self.events.append(e)
        return "committed"

    @classmethod
    def replay(cls, committed_events):
        recovered = cls()
        for e in committed_events:
            recovered.accept(e)
        return recovered


class EscrowAcceptance(unittest.TestCase):
    def setUp(self):
        self.desk = Escrow()
        self.desk.accept(envelope("open-1", "Mark", "open", ticket="P1",
                                  project="Puppy", repo="puppy/repo", needs=["write"]))

    def event(self, eid, actor, op, **extra):
        return envelope(eid, actor, op, ticket="P1", repo="puppy/repo", **extra)

    def test_read_only_worker_cannot_claim_write_ticket_even_through_relay(self):
        e = self.event("claim-1", "Bing", "claim", generation=0)
        with self.assertRaisesRegex(Rejected, "original actor lacks"):
            self.desk.accept(relay(e, "courier"))
        self.assertIsNone(self.desk.tickets["P1"]["holder"])

    def test_relay_preserves_original_actor_and_payload(self):
        original = self.event("claim-1", "QC", "claim", generation=0)
        carried = relay(original, "courier")
        self.assertEqual(carried["actor"], original["actor"])
        self.assertEqual(carried["payload"], original["payload"])
        self.assertEqual(original["via"], [])
        self.desk.accept(carried)
        self.assertEqual(self.desk.events[-1]["actor"], "QC")

    def test_duplicate_delivery_does_not_complete_twice(self):
        self.desk.accept(self.event("claim-1", "QC", "claim", generation=0))
        e = self.event("done-1", "QC", "complete", generation=1, cursor=0)
        self.assertEqual(self.desk.accept(e), "committed")
        self.assertEqual(self.desk.accept(relay(e, "courier")), "duplicate")
        self.assertEqual(sum(x["operation"] == "complete" for x in self.desk.events), 1)
        changed = deepcopy(e)
        changed["payload"]["cursor"] = 999
        with self.assertRaisesRegex(Rejected, "different content"):
            self.desk.accept(changed)

    def test_interrupted_claim_resumes_only_from_committed_state(self):
        self.desk.accept(self.event("claim-1", "QC", "claim", generation=0))
        self.desk.accept(self.event("cp-1", "QC", "checkpoint", generation=1,
                                    cursor=0, result="verified input"))
        uncommitted_draft = "finished output existing only in lost worker memory"
        recovered = Escrow.replay(deepcopy(self.desk.events))
        self.assertEqual(recovered.tickets["P1"]["committed"], ["verified input"])
        self.assertNotIn(uncommitted_draft, str(recovered.events))
        recovered.accept(self.event("replace-1", "Mark", "replace", generation=1))
        with self.assertRaisesRegex(Rejected, "stale or foreign"):
            recovered.accept(self.event("late-1", "QC", "complete", generation=1, cursor=1))
        with self.assertRaisesRegex(Rejected, "committed cursor"):
            recovered.accept(self.event("skip-1", "Mark", "complete", generation=2, cursor=2))
        recovered.accept(self.event("done-1", "Mark", "complete", generation=2, cursor=1))
        self.assertTrue(recovered.tickets["P1"]["done"])

    def test_castle_fragment_does_not_switch_active_puppy_project(self):
        self.desk.accept(envelope("fragment-1", "Mark", "fragment",
                                  project="Castle", text="Consider a moat later"))
        self.assertEqual(self.desk.active, "Puppy")
        self.assertEqual(self.desk.fragments[0]["project"], "Castle")
        self.desk.accept(self.event("claim-1", "Q", "claim", generation=0))
        with self.assertRaisesRegex(Rejected, "wrong repository"):
            self.desk.accept(envelope("wrong-1", "Q", "complete", ticket="P1",
                                      repo="castle/repo", generation=1, cursor=0))

    def test_question_is_z_first_and_escalation_is_explicit(self):
        with self.assertRaisesRegex(Rejected, "start with Z"):
            self.desk.accept(envelope("q-bad", "Q", "question", route=["QC"], text="Where is input?"))
        self.desk.accept(envelope("q-1", "Q", "question", route=["Z"], text="Where is input?"))
        with self.assertRaisesRegex(Rejected, "explicitly escalate"):
            self.desk.accept(envelope("esc-bad", "Q", "escalate", question="q-1", route=["QC"]))
        self.desk.accept(envelope("esc-1", "Z", "escalate", question="q-1", route=["QC"],
                                  reason="Z cannot resolve repository access"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
