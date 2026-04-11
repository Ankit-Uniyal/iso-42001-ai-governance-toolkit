#!/usr/bin/env python3
"""
ai_assessment_checker.py
--------------------------
ISO/IEC 42001:2023 AI Governance Toolkit — GRC Engineering Automation

Purpose:
    Reads a CSV file containing AI systems and their last assessment dates,
    then flags any system whose assessment is overdue (older than 365 days).
    Supports ISO 42001 Clause 9.1 (Monitoring, Measurement, Analysis and Evaluation).

Usage:
    python scripts/ai_assessment_checker.py --input scripts/sample_ai_systems.csv
    python scripts/ai_assessment_checker.py --input scripts/sample_ai_systems.csv --threshold 180

Expected CSV Columns:
    system_id, system_name, owner, risk_level, last_assessment_date (YYYY-MM-DD)

Output:
    - Console summary table
    - Saves a report to: scripts/assessment_report.txt

Author:  Ankit Uniyal
Toolkit: ISO/IEC 42001:2023 AI Governance Toolkit
Version: 1.0.0
"""

import csv
import argparse
import sys
from datetime import datetime, date
from pathlib import Path


# ── Constants ─────────────────────────────────────────────────────────────────
DEFAULT_THRESHOLD_DAYS = 365
DATE_FORMAT = "%Y-%m-%d"

STATUS_OK       = "COMPLIANT"
STATUS_OVERDUE  = "OVERDUE"
STATUS_WARNING  = "DUE SOON"
WARNING_BUFFER  = 30


# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), DATE_FORMAT).date()
    except (ValueError, AttributeError):
        return None


def days_since(assessment_date):
    return (date.today() - assessment_date).days


def evaluate_status(assessment_date, threshold):
    if assessment_date is None:
        return "MISSING DATE", None
    age = days_since(assessment_date)
    if age > threshold:
        return STATUS_OVERDUE, age
    elif age > (threshold - WARNING_BUFFER):
        return STATUS_WARNING, age
    else:
        return STATUS_OK, age


# ── Core logic ────────────────────────────────────────────────────────────────

def check_assessments(csv_path, threshold):
    results = []
    path = Path(csv_path)

    if not path.exists():
        print(f"[ERROR] File not found: {csv_path}")
        sys.exit(1)

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required_cols = {"system_id", "system_name", "owner", "risk_level", "last_assessment_date"}
        if not required_cols.issubset(set(reader.fieldnames or [])):
            missing = required_cols - set(reader.fieldnames or [])
            print(f"[ERROR] CSV is missing required columns: {missing}")
            sys.exit(1)

        for row in reader:
            assessment_date = parse_date(row["last_assessment_date"])
            status, age = evaluate_status(assessment_date, threshold)
            results.append({
                "system_id":            row["system_id"].strip(),
                "system_name":          row["system_name"].strip(),
                "owner":                row["owner"].strip(),
                "risk_level":           row["risk_level"].strip(),
                "last_assessment_date": row["last_assessment_date"].strip(),
                "days_since":           age,
                "status":               status,
            })
    return results


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_report(results, threshold):
    today_str  = date.today().strftime(DATE_FORMAT)
    total      = len(results)
    compliant  = sum(1 for r in results if r["status"] == STATUS_OK)
    warning    = sum(1 for r in results if r["status"] == STATUS_WARNING)
    overdue    = sum(1 for r in results if r["status"] == STATUS_OVERDUE)
    missing    = total - compliant - warning - overdue

    print("\n" + "=" * 80)
    print("  ISO/IEC 42001:2023 — AI System Assessment Currency Report")
    print(f"  Run Date  : {today_str}")
    print(f"  Threshold : {threshold} days")
    print("=" * 80)

    header = f"  {'ID':<10}  {'System Name':<28}  {'Owner':<18}  {'Risk':<10}  {'Last Assessment':<20}  {'Days Since':<11}  {'Status'}"
    print("\n" + header)
    print("  " + "-" * 110)

    for r in results:
        days_display = str(r["days_since"]) if r["days_since"] is not None else "N/A"
        print(f"  {r['system_id']:<10}  {r['system_name'][:27]:<28}  {r['owner'][:17]:<18}  "
              f"{r['risk_level']:<10}  {r['last_assessment_date']:<20}  {days_display:<11}  {r['status']}")

    print(f"\n{'─' * 60}")
    print(f"  SUMMARY")
    print(f"  Total AI Systems : {total}")
    print(f"  [OK]  Compliant  : {compliant}")
    print(f"  [!!]  Due Soon   : {warning}")
    print(f"  [XX]  Overdue    : {overdue}")
    print(f"  [--]  Missing    : {missing}")
    print(f"{'─' * 60}\n")

    if overdue > 0 or missing > 0:
        print("  ACTION REQUIRED: The following systems need immediate reassessment:\n")
        for r in results:
            if r["status"] in (STATUS_OVERDUE, "MISSING DATE"):
                print(f"    - [{r['system_id']}] {r['system_name']} — Owner: {r['owner']}")
        print()


def save_report(results, threshold, output_path):
    today_str = date.today().strftime(DATE_FORMAT)
    lines = [
        "ISO/IEC 42001:2023 — AI System Assessment Currency Report",
        f"Run Date  : {today_str}",
        f"Threshold : {threshold} days",
        "",
        f"{'ID':<10}  {'System Name':<28}  {'Owner':<18}  {'Risk':<10}  {'Last Assessment':<20}  {'Days Since':<11}  {'Status'}",
        "-" * 115,
    ]
    for r in results:
        days_display = str(r["days_since"]) if r["days_since"] is not None else "N/A"
        lines.append(
            f"{r['system_id']:<10}  {r['system_name'][:27]:<28}  {r['owner'][:17]:<18}  "
            f"{r['risk_level']:<10}  {r['last_assessment_date']:<20}  {days_display:<11}  {r['status']}"
        )

    overdue_items = [r for r in results if r["status"] in (STATUS_OVERDUE, "MISSING DATE")]
    if overdue_items:
        lines += ["", "ACTION REQUIRED — Systems needing immediate reassessment:"]
        for r in overdue_items:
            lines.append(f"  - [{r['system_id']}] {r['system_name']} (Owner: {r['owner']})")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"  Report saved to: {output_path}\n")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="ISO 42001 GRC Engineering — AI Assessment Currency Checker"
    )
    parser.add_argument(
        "--input", "-i",
        default="scripts/sample_ai_systems.csv",
        help="Path to the AI systems CSV file (default: scripts/sample_ai_systems.csv)"
    )
    parser.add_argument(
        "--threshold", "-t",
        type=int,
        default=DEFAULT_THRESHOLD_DAYS,
        help=f"Max days since last assessment before flagging overdue (default: {DEFAULT_THRESHOLD_DAYS})"
    )
    parser.add_argument(
        "--output", "-o",
        default="scripts/assessment_report.txt",
        help="Path for the output report file (default: scripts/assessment_report.txt)"
    )
    args = parser.parse_args()

    results = check_assessments(args.input, args.threshold)
    print_report(results, args.threshold)
    save_report(results, args.threshold, args.output)

    # Exit with non-zero code if any systems are overdue (useful for CI/CD pipelines)
    overdue_count = sum(
        1 for r in results
        if r["status"] in (STATUS_OVERDUE, "MISSING DATE")
    )
    sys.exit(1 if overdue_count > 0 else 0)


if __name__ == "__main__":
    main()
