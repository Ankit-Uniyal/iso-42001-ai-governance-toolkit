#!/usr/bin/env python3
"""
AIMS Statement of Applicability (SoA) Tracker
ISO/IEC 42001:2023 | Clause 6.1.3 GRC Automation Script

Purpose:
    Tracks the implementation status of all 38 Annex A controls across 9 domains.
        Generates a progress report showing overall AIMS implementation readiness.

        Usage:
            python aims_soa_tracker.py
                python aims_soa_tracker.py --export-csv soa_report.csv
                    python aims_soa_tracker.py --domain "AI System Lifecycle"

Author: ISO 42001 Lead Auditor | GRC Lead
Toolkit: github.com/Ankit-Uniyal/iso-42001-ai-governance-toolkit
License: MIT
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# ALL 38 ANNEX A CONTROLS — ISO/IEC 42001:2023
# ─────────────────────────────────────────────────────────────────────────────

ANNEX_A_CONTROLS = [
      # Domain 1: Policies for AI (A.2)
    {"id": "A.2.2", "domain": "Policies for AI", "control": "AI policy", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.2.3", "domain": "Policies for AI", "control": "Allocation of roles and responsibilities", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.2.4", "domain": "Policies for AI", "control": "Reporting obligations", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.2.5", "domain": "Policies for AI", "control": "Addressing AI considerations in contracts", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.2.6", "domain": "Policies for AI", "control": "Records related to AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 2: Human Oversight (A.3)
      {"id": "A.3.2", "domain": "Human Oversight of AI Systems", "control": "Establishment of human oversight mechanisms", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 3: Responsibilities (A.4)
      {"id": "A.4.2", "domain": "Responsibilities Related to AI Systems", "control": "Intended use", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.3", "domain": "Responsibilities Related to AI Systems", "control": "Accuracy, reliability and performance of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.4", "domain": "Responsibilities Related to AI Systems", "control": "Safety of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.5", "domain": "Responsibilities Related to AI Systems", "control": "Security of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.6", "domain": "Responsibilities Related to AI Systems", "control": "Availability of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.7", "domain": "Responsibilities Related to AI Systems", "control": "Eliminating bias and promoting fairness", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.8", "domain": "Responsibilities Related to AI Systems", "control": "Transparency", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.9", "domain": "Responsibilities Related to AI Systems", "control": "Privacy", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.4.10", "domain": "Responsibilities Related to AI Systems", "control": "Accountability", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 4: Impact Assessment (A.5)
      {"id": "A.5.2", "domain": "Impact Assessment for AI Systems", "control": "AI system impact assessment process", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.5.3", "domain": "Impact Assessment for AI Systems", "control": "Documentation of AI system impact assessments", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 5: AI System Lifecycle (A.6)
      {"id": "A.6.1.2", "domain": "AI System Lifecycle", "control": "General lifecycle management", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.2", "domain": "AI System Lifecycle", "control": "Data for AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.3", "domain": "AI System Lifecycle", "control": "Acquisition of AI systems and components", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.4", "domain": "AI System Lifecycle", "control": "Design and development of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.5", "domain": "AI System Lifecycle", "control": "Testing of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.6", "domain": "AI System Lifecycle", "control": "AI system documentation", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.7", "domain": "AI System Lifecycle", "control": "Deployment of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.8", "domain": "AI System Lifecycle", "control": "Operation of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.9", "domain": "AI System Lifecycle", "control": "Human oversight of AI systems during operation", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.10", "domain": "AI System Lifecycle", "control": "Monitoring AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.11", "domain": "AI System Lifecycle", "control": "Change management of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.12", "domain": "AI System Lifecycle", "control": "Decommissioning of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
      {"id": "A.6.2.13", "domain": "AI System Lifecycle", "control": "Incident management for AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 6: Responsible and Trustworthy AI (A.7)
      {"id": "A.7.2", "domain": "Responsible and Trustworthy AI", "control": "Responsible and ethical use", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 7: AI System Suppliers (A.8)
      {"id": "A.8.2", "domain": "AI System Suppliers", "control": "Supplier relationships for AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 8: Documentation and Information (A.9)
      {"id": "A.9.2", "domain": "Documentation and Information Related to AI Systems", "control": "Documentation of AI systems", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},

      # Domain 9: AI Standards and Sector-Specific Issues (A.10)
      {"id": "A.10.2", "domain": "AI Standards and Sector-Specific Issues", "control": "Compliance with applicable standards", "mandatory": True, "status": "not_started", "evidence": "", "owner": ""},
]

STATUS_OPTIONS = ["implemented", "partial", "planned", "not_started", "excluded"]
STATUS_LABELS = {
      "implemented": "IMPLEMENTED",
      "partial": "PARTIAL",
      "planned": "PLANNED",
      "not_started": "NOT STARTED",
      "excluded": "EXCLUDED",
}
STATUS_WEIGHTS = {
      "implemented": 1.0,
      "partial": 0.5,
      "planned": 0.1,
      "not_started": 0.0,
      "excluded": 0.0,
}


def load_soa_state(filepath: str) -> list:
      """Load SoA state from a JSON file (previously saved progress)."""
      try:
                with open(filepath, "r") as f:
                              saved = json.load(f)
                          control_map = {c["id"]: c for c in saved}
                controls = []
                for control in ANNEX_A_CONTROLS:
                              if control["id"] in control_map:
                                                controls.append({**control, **control_map[control["id"]]})
      else:
                        controls.append(control.copy())
                print(f"[INFO] Loaded SoA state from {filepath}")
        return controls
except FileNotFoundError:
        print(f"[INFO] No saved state found at {filepath}. Starting fresh.")
        return [c.copy() for c in ANNEX_A_CONTROLS]


def save_soa_state(controls: list, filepath: str) -> None:
      """Save current SoA state to a JSON file."""
    with open(filepath, "w") as f:
              json.dump(controls, f, indent=2)
          print(f"[INFO] SoA state saved to {filepath}")


def calculate_completion(controls: list) -> dict:
      """Calculate completion statistics."""
    total = len(controls)
    by_status = {}
    for status in STATUS_OPTIONS:
              count = sum(1 for c in controls if c["status"] == status)
              by_status[status] = count

    weighted_score = sum(STATUS_WEIGHTS.get(c["status"], 0) for c in controls)
    completion_pct = (weighted_score / total) * 100 if total > 0 else 0

    by_domain = {}
    for control in controls:
              domain = control["domain"]
              if domain not in by_domain:
                            by_domain[domain] = {"total": 0, "implemented": 0, "partial": 0, "planned": 0, "not_started": 0, "excluded": 0}
                        by_domain[domain]["total"] += 1
        by_domain[domain][control["status"]] += 1

    return {
              "total_controls": total,
              "by_status": by_status,
              "completion_pct": round(completion_pct, 1),
              "by_domain": by_domain,
              "timestamp": datetime.now().isoformat(),
    }


def print_report(controls: list, domain_filter: Optional[str] = None) -> None:
      """Print a formatted SoA progress report to the console."""
    stats = calculate_completion(controls)

    print("\n" + "=" * 80)
    print("  ISO/IEC 42001:2023 — STATEMENT OF APPLICABILITY TRACKER")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)

    # Overall progress
    print(f"\n  OVERALL IMPLEMENTATION PROGRESS: {stats['completion_pct']}%")
    bar_len = 50
    filled = int(bar_len * stats["completion_pct"] / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"  [{bar}]")

    print(f"\n  Controls: {stats['total_controls']} total")
    for status, count in stats["by_status"].items():
              pct = round(count / stats["total_controls"] * 100, 1)
        label = STATUS_LABELS[status]
        print(f"    {label:<15} {count:>3} ({pct}%)")

    # Domain breakdown
    print("\n" + "-" * 80)
    print("  PROGRESS BY DOMAIN")
    print("-" * 80)
    for domain, counts in stats["by_domain"].items():
              if domain_filter and domain_filter.lower() not in domain.lower():
                            continue
                        impl = counts["implemented"]
        partial = counts["partial"]
        total_d = counts["total"]
        domain_score = (impl + partial * 0.5) / total_d * 100 if total_d > 0 else 0
        bar_d = "█" * int(domain_score / 5) + "░" * (20 - int(domain_score / 5))
        print(f"\n  {domain}")
        print(f"  [{bar_d}] {round(domain_score, 0):.0f}%  ({impl} impl / {partial} partial / {total_d} total)")

    # Control detail
    print("\n" + "-" * 80)
    print("  CONTROL DETAIL")
    print("-" * 80)
    current_domain = None
    for control in controls:
              if domain_filter and domain_filter.lower() not in control["domain"].lower():
                            continue
                        if control["domain"] != current_domain:
                                      current_domain = control["domain"]
                                      print(f"\n  Domain: {current_domain}")
                                  status_label = STATUS_LABELS.get(control["status"], "UNKNOWN")
        owner = f" | Owner: {control['owner']}" if control["owner"] else ""
        evidence = f" | Evidence: {control['evidence']}" if control["evidence"] else ""
        print(f"    {control['id']:<12} [{status_label:<15}] {control['control']}{owner}{evidence}")

    print("\n" + "=" * 80)

    # Audit readiness assessment
    pct = stats["completion_pct"]
    if pct >= 95:
              readiness = "AUDIT READY — Excellent implementation coverage"
elif pct >= 80:
        readiness = "NEAR READY — Complete remaining partial/planned controls before audit"
elif pct >= 60:
        readiness = "IN PROGRESS — Significant work remaining before audit readiness"
elif pct >= 40:
        readiness = "EARLY STAGE — Substantial implementation work required"
else:
        readiness = "INITIAL STAGE — Full implementation programme needed"

    print(f"\n  AUDIT READINESS: {readiness}")
    print("=" * 80 + "\n")


def export_csv(controls: list, filepath: str) -> None:
      """Export SoA controls to CSV for use in Excel or GRC tools."""
    fieldnames = ["id", "domain", "control", "mandatory", "status", "evidence", "owner"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
              writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(controls)
    print(f"[INFO] SoA exported to CSV: {filepath}")


def interactive_update(controls: list) -> list:
      """Interactive CLI to update control status."""
    print("\nINTERACTIVE SOA UPDATE MODE")
    print("Enter control ID to update (e.g., A.4.7), or 'q' to quit, 'list' to show all IDs\n")

    control_map = {c["id"]: i for i, c in enumerate(controls)}

    while True:
              user_input = input("Control ID: ").strip()
        if user_input.lower() == "q":
                      break
                  if user_input.lower() == "list":
                                for c in controls:
                                                  print(f"  {c['id']:<12} [{STATUS_LABELS.get(c['status'], 'UNKNOWN'):<15}] {c['control']}")
                                              continue
        if user_input not in control_map:
                      print(f"  [ERROR] Control ID '{user_input}' not found. Try 'list' to see all IDs.")
            continue

        idx = control_map[user_input]
        control = controls[idx]
        print(f"\n  Control: {control['control']}")
        print(f"  Current status: {STATUS_LABELS.get(control['status'], 'UNKNOWN')}")
        print(f"  Status options: {', '.join(STATUS_OPTIONS)}")

        new_status = input("  New status: ").strip().lower()
        if new_status not in STATUS_OPTIONS:
                      print(f"  [ERROR] Invalid status. Choose from: {', '.join(STATUS_OPTIONS)}")
            continue

        new_evidence = input(f"  Evidence reference (current: '{control['evidence']}'): ").strip()
        new_owner = input(f"  Owner (current: '{control['owner']}'): ").strip()

        controls[idx]["status"] = new_status
        if new_evidence:
                      controls[idx]["evidence"] = new_evidence
        if new_owner:
                      controls[idx]["owner"] = new_owner
        print(f"  [OK] Updated {user_input} to {STATUS_LABELS[new_status]}\n")

    return controls


def main():
      parser = argparse.ArgumentParser(
                description="ISO/IEC 42001:2023 Annex A SoA Tracker",
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog="""
                Examples:
                  python aims_soa_tracker.py
                    python aims_soa_tracker.py --export-csv soa_report.csv
                      python aims_soa_tracker.py --domain "AI System Lifecycle"
          python aims_soa_tracker.py --update --state soa_state.json
            python aims_soa_tracker.py --state soa_state.json --export-csv soa_report.csv
                    """,
      )
    parser.add_argument("--state", default="soa_state.json", help="JSON file to load/save SoA state (default: soa_state.json)")
    parser.add_argument("--export-csv", metavar="FILE", help="Export SoA to CSV file")
    parser.add_argument("--domain", metavar="NAME", help="Filter report to a specific domain")
    parser.add_argument("--update", action="store_true", help="Interactively update control statuses")
    parser.add_argument("--version", action="version", version="AIMS SoA Tracker 1.0.0")
    args = parser.parse_args()

    # Load or initialise controls
    controls = load_soa_state(args.state)

    # Interactive update mode
    if args.update:
              controls = interactive_update(controls)
        save_soa_state(controls, args.state)

    # Print report
    print_report(controls, domain_filter=args.domain)

    # Export CSV
    if args.export_csv:
              export_csv(controls, args.export_csv)


if __name__ == "__main__":
      main()
