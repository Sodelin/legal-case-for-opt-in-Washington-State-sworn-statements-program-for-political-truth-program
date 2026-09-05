"""Check documentation integrity and fictional arithmetic; never legal/live readiness."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    manifest = (ROOT / "audit/CANONICAL_CHECKSUMS.md").read_text()
    entries = re.findall(r"^([0-9a-f]{64})  (.+)$", manifest, re.M)
    require(len(entries) >= 15, "Incomplete source manifest")
    for expected, relative in entries:
        path = ROOT / relative
        require(path.is_file(), f"Missing source: {relative}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"Checksum mismatch: {relative}")
    for file, field, expected in [
        ("OWNER_DECISION_REGISTER.csv", "decision_id",
         {f"CR-{i:02}" for i in range(1, 17)}),
        ("NONSWORN_REVIEW_CROSSWALK.csv", "condition_id",
         {f"PB-{i:02}" for i in range(1, 19)}
         | {f"D-{i:02}" for i in range(1, 22)}
         | {f"P5-{i:02}" for i in range(1, 9)}),
    ]:
        rows = list(csv.DictReader((ROOT / "audit" / file).open()))
        ids = [row[field] for row in rows]
        require(len(ids) == len(expected) and set(ids) == expected,
                f"Missing or duplicate rows: {file}")
    example = (ROOT / "operations/NONSWORN_SYNTHETIC_EXAMPLE.md").read_text()
    payloads = re.findall(r"```json\n(.*?)\n```", example, re.S)
    hashes = re.findall(r"`([0-9a-f]{64})`", example)
    require(len(payloads) == len(hashes) == 3, "Expected three fixtures")
    for payload, expected in zip(payloads, hashes):
        require(hashlib.sha256(payload.encode()).hexdigest() == expected,
                "Fictional payload checksum mismatch")
    require(sum(json.loads(payloads[0]).values()) == 28, "Arithmetic mismatch")
    require(json.loads(payloads[1])["claim"] == 30, "v1 mismatch")
    require(json.loads(payloads[2])["claim"] == 28, "v2 mismatch")
    require(hashlib.sha256((payloads[1] + " ").encode()).hexdigest() != hashes[1],
            "Changed-byte fixture failed")
    print(f"PASS: {len(entries)} source hashes, 16 decisions, 47 conditions, 3 fictional payloads.")
    print("These checks do not test workflow enforcement, people, efficacy or legal clearance.")


if __name__ == "__main__":
    main()
