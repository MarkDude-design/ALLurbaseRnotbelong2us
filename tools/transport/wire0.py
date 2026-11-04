#!/usr/bin/env python3
"""WIRE0: small ASCII handoff/ACK frames. Offline, no I/O beyond CLI/stdout.

CRC32 detects accidental corruption, NOT tampering. Neither receipt proves a
native-model read, delivery, approval, or successful execution.
"""
from __future__ import annotations
import argparse
import re
import sys
import zlib

MAX_BYTES = 160
REF = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+#[1-9][0-9]*@[1-9][0-9]*\Z")
NEXT = re.compile(r"[A-Z0-9_:-]{1,32}\Z")
STATES = {"WAIT", "BLOCKED", "POSTED", "DONE"}

class WireError(ValueError):
    pass

def _crc(text: str) -> str:
    return f"{zlib.crc32(text.encode('ascii')) & 0xffffffff:08X}"

def _fields(seq: int, ref: str):
    if type(seq) is not int or not 1 <= seq <= 999999999:
        raise WireError("seq must be a positive integer <= 999999999")
    if not REF.fullmatch(ref) or len(ref) > 96:
        raise WireError("ref must be owner/repo#issue@comment, max 96 chars")

def encode(seq: int, ref: str, state: str, next_code: str) -> str:
    _fields(seq, ref)
    if state not in STATES or not NEXT.fullmatch(next_code):
        raise WireError("bad state/next action code")
    body = f"W0|{seq}|{ref}|{state}|{next_code}"
    packet = body + "|" + _crc(body)
    if len(packet.encode("ascii")) > MAX_BYTES:
        raise WireError("frame exceeds 160 bytes")
    return packet

def decode(packet: str) -> dict:
    if not isinstance(packet, str) or not packet.isascii() or len(packet.encode('ascii')) > MAX_BYTES:
        raise WireError("non-ASCII or oversized frame")
    fields = packet.split("|")
    if len(fields) != 6 or fields[0] != "W0":
        raise WireError("not a WIRE0 frame")
    _, raw_seq, ref, state, next_code, checksum = fields
    if not raw_seq.isdecimal() or str(int(raw_seq)) != raw_seq:
        raise WireError("bad sequence")
    seq = int(raw_seq)
    _fields(seq, ref)
    if state not in STATES or not NEXT.fullmatch(next_code):
        raise WireError("invalid frame fields")
    if checksum != _crc("|".join(fields[:-1])):
        raise WireError("bad CRC: re-fetch original, do not guess")
    return {"seq": seq, "ref": ref, "state_declared": state,
            "next_code": next_code, "crc": checksum}

def acknowledge(packet: str) -> str:
    p = decode(packet)
    # ACK means frame parsed by a receiver, NOT native-model delivery or acceptance.
    body = f"A0|{p['seq']}|{p['ref']}|{p['crc']}"
    return body + "|" + _crc(body)

def check_ack(packet: str, ack: str) -> bool:
    if not isinstance(ack, str) or not ack.isascii() or len(ack) > MAX_BYTES:
        raise WireError("bad ACK")
    bits = ack.split("|")
    if len(bits) != 5 or bits[0] != "A0" or bits[-1] != _crc("|".join(bits[:-1])):
        raise WireError("corrupted ACK")
    return ack == acknowledge(packet)

def accept(packet: str, seen: dict[tuple[str, int], str]) -> str:
    """In-memory demonstration; caller persists seen records if desired."""
    p = decode(packet)
    key = (p["ref"], p["seq"])
    old = seen.get(key)
    if old is None:
        seen[key] = p["crc"]
        return "NEW"
    if old == p["crc"]:
        return "DUPLICATE"
    return "CONFLICT"  # same identity, different content: never overwrite

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("encode")
    a.add_argument("seq", type=int)
    a.add_argument("ref")
    a.add_argument("state", choices=sorted(STATES))
    a.add_argument("next_code")
    for cmd in ("decode", "ack"):
        sub.add_parser(cmd).add_argument("frame")
    a = sub.add_parser("check-ack")
    a.add_argument("frame")
    a.add_argument("ack_frame")
    args = ap.parse_args(argv)
    try:
        if args.cmd == "encode":
            result = encode(args.seq, args.ref, args.state, args.next_code)
        elif args.cmd == "decode":
            result = str(decode(args.frame))
        elif args.cmd == "ack":
            result = acknowledge(args.frame)
        else:
            result = "MATCH" if check_ack(args.frame, args.ack_frame) else "MISMATCH"
        print(result)
        return 0 if result != "MISMATCH" else 1
    except WireError as e:
        print(f"BLOCKED: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
