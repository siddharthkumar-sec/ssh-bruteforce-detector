#!/usr/bin/env python3
"""SSH brute-force detector: auth log padhta hai aur suspicious IPs report karta hai."""

import argparse
import csv
import ipaddress
import re
import sys
from pathlib import Path

DEFAULT_THRESHOLD = 5
DEFAULT_LOG = Path(__file__).parent / "sample_auth.log"

FAILED_RE = re.compile(
    r"^(?P<time>[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s.*?"
    r"Failed password for (?:invalid user )?(?P<user>\S+) "
    r"from (?P<ip>[0-9A-Fa-f:.]+)"
)


def parse_line(line):
    """Line se (time, user, ip) nikalta hai. Samajh na aaye to None deta hai."""
    match = FAILED_RE.search(line)
    if not match:
        return None
    try:
        ipaddress.ip_address(match["ip"])
    except ValueError:
        return None
    return match["time"], match["user"], match["ip"]


def analyze(path):
    """Return: (ip-wise stats, total lines, skipped lines)."""
    stats = {}
    total_lines = 0
    skipped = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            total_lines += 1
            if "Failed password" not in line:
                continue
            parsed = parse_line(line)
            if parsed is None:
                skipped += 1
                continue
            when, user, ip = parsed
            entry = stats.setdefault(
                ip, {"count": 0, "users": set(), "first": when, "last": when}
            )
            entry["count"] += 1
            entry["users"].add(user)
            entry["last"] = when
    return stats, total_lines, skipped


def build_rows(stats, threshold):
    rows = []
    for ip, e in sorted(stats.items(), key=lambda kv: kv[1]["count"], reverse=True):
        rows.append({
            "ip": ip,
            "failures": e["count"],
            "unique_users": len(e["users"]),
            "first_seen": e["first"],
            "last_seen": e["last"],
            "status": "SUSPICIOUS" if e["count"] >= threshold else "ok",
        })
    return rows


def print_table(rows):
    print(f"{'IP':<40} {'FAILS':>5} {'USERS':>5}  {'FIRST SEEN':<16} {'LAST SEEN':<16} STATUS")
    for r in rows:
        print(
            f"{r['ip']:<40} {r['failures']:>5} {r['unique_users']:>5}  "
            f"{r['first_seen']:<16} {r['last_seen']:<16} {r['status']}"
        )


def write_csv(rows, path):
    fields = ["ip", "failures", "unique_users", "first_seen", "last_seen", "status"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def parse_args():
    p = argparse.ArgumentParser(description="SSH failed-login analyzer")
    p.add_argument("logfile", nargs="?", default=str(DEFAULT_LOG),
                   help="auth log ka path (default: script ke folder ki sample_auth.log)")
    p.add_argument("-t", "--threshold", type=int, default=DEFAULT_THRESHOLD,
                   help=f"itne ya zyada failures par SUSPICIOUS (default {DEFAULT_THRESHOLD})")
    p.add_argument("-o", "--csv", help="report CSV file mein save karo")
    return p.parse_args()


def main():
    args = parse_args()
    print(f"File: {args.logfile} | Threshold: {args.threshold}\n")

    try:
        stats, total, skipped = analyze(args.logfile)
    except OSError as err:
        print(f"Error: {args.logfile} nahi padh paye: {err}", file=sys.stderr)
        return 2

    rows = build_rows(stats, args.threshold)
    if rows:
        print_table(rows)
    else:
        print("Koi failed login nahi mila.")

    suspicious = sum(1 for r in rows if r["status"] == "SUSPICIOUS")
    print(f"\nLines padhi: {total} | Failed IPs: {len(rows)} | "
          f"Suspicious: {suspicious} | Skipped (samajh nahi aayi): {skipped}")

    if args.csv:
        write_csv(rows, Path(args.csv))
        print(f"CSV save hua: {args.csv}")

    return 1 if suspicious else 0


if __name__ == "__main__":
    sys.exit(main())