# 12-SCRIPTS — GRC Engineering Automation

> **Bridging Policy and Engineering** for ISO/IEC 42001:2023 AI Governance

This folder contains automation scripts that operationalise the governance controls defined in the ISO 42001 toolkit. Rather than treating compliance as a static document exercise, these scripts turn policy requirements into **executable, repeatable checks** — the hallmark of modern GRC Engineering.

All commands below are written to be run from the **repository root**.

---

## Scripts

| Script | Purpose | ISO 42001 Reference |
|--------|---------|--------------------|
| `ai_assessment_checker.py` | Checks assessment currency for every AI system in an inventory CSV | Clause 9.1 — Monitoring, Measurement, Analysis and Evaluation |
| `aims_soa_tracker.py` | Tracks implementation status of all 38 Annex A controls and reports overall AIMS readiness | Clause 6.1.3 — Statement of Applicability |

### Requirements

- Python 3.9+
- No external dependencies (standard library only)

---

## ai_assessment_checker.py

### What it does

Reads a CSV inventory of AI systems and evaluates whether each system's **Last Assessment Date** falls within an acceptable window (default: 365 days). It produces:

- A formatted **console report** with status for every system
- A saved **text report** for audit evidence (default: `12-SCRIPTS/reports/assessment_report.txt`)
- A **non-zero exit code** when overdue or undated systems exist (CI/CD pipeline friendly)

### Status levels

| Status | Meaning |
|--------|---------|
| `COMPLIANT` | Assessment is within the threshold window |
| `DUE SOON` | Assessment is within 30 days of becoming overdue |
| `OVERDUE` | Assessment date exceeds the threshold |
| `MISSING DATE` | No assessment date recorded — immediate action required |

### Usage

```bash
# Basic run using the sample CSV
python 12-SCRIPTS/ai_assessment_checker.py

# Specify a custom input file
python 12-SCRIPTS/ai_assessment_checker.py --input path/to/your/ai_inventory.csv

# Use a 180-day threshold instead of 365
python 12-SCRIPTS/ai_assessment_checker.py --input 12-SCRIPTS/sample_ai_systems.csv --threshold 180

# Specify a custom output report path
python 12-SCRIPTS/ai_assessment_checker.py --output 12-SCRIPTS/reports/q2_assessment.txt
```

The output directory is created automatically if it does not already exist.

### CSV format

Your input CSV must include the following columns:

```
system_id, system_name, owner, risk_level, last_assessment_date
```

| Column | Description | Example |
|--------|-------------|---------|
| `system_id` | Unique identifier | `AI-001` |
| `system_name` | Descriptive name of the AI system | `Fraud Detection Model` |
| `owner` | Team or individual responsible | `Risk & Compliance` |
| `risk_level` | Risk classification | `Critical / High / Medium / Low` |
| `last_assessment_date` | Date of last formal assessment (YYYY-MM-DD) | `2026-02-05` |

See `sample_ai_systems.csv` for a working example.

### Sample output (abridged)

```
================================================================================
   ISO/IEC 42001:2023 — AI System Assessment Currency Report
   Run Date  : 2026-08-02
   Threshold : 365 days
================================================================================

  ID         System Name                   Owner              Risk      Last Assessment  Days Since  Status
  ------------------------------------------------------------------------------------------------------------
  AI-001     Customer Churn Predictor      Data Science Team  High      2026-02-05       178         COMPLIANT
  AI-002     Resume Screening Engine       HR Technology      High      2025-08-11       356         DUE SOON
  AI-003     Fraud Detection Model         Risk & Compliance  Critical  2025-03-24       496         OVERDUE
  AI-006     Loan Approval Assistant       Credit Risk        Critical  2025-03-03       517         OVERDUE
  AI-009     Image Classification Service  Computer Vision T  High                       N/A         MISSING DATE

  ------------------------------------------------------------
  SUMMARY
  Total AI Systems  : 10
  [OK] Compliant    : 6
  [!!] Due Soon     : 1
  [XX] Overdue      : 2
  [--] Missing      : 1
  ------------------------------------------------------------
```

---

## aims_soa_tracker.py

### What it does

Holds the full ISO/IEC 42001:2023 Annex A control set — all **38 controls across 9 domains (A.2 to A.10)** — and tracks the implementation status of each one. It produces a readiness report, supports per-domain filtering, and can export the Statement of Applicability to CSV for inclusion in an audit pack.

State is persisted to a JSON file between runs (default: `soa_state.json`), so progress accumulates.

### Usage

```bash
# Full readiness report for all 38 controls
python 12-SCRIPTS/aims_soa_tracker.py

# Report on a single Annex A domain
python 12-SCRIPTS/aims_soa_tracker.py --domain "AI System Lifecycle"

# Interactively update control statuses
python 12-SCRIPTS/aims_soa_tracker.py --update

# Export the SoA to CSV for the audit pack
python 12-SCRIPTS/aims_soa_tracker.py --export-csv 12-SCRIPTS/reports/soa_report.csv

# Use a specific state file
python 12-SCRIPTS/aims_soa_tracker.py --state 12-SCRIPTS/reports/soa_state.json
```

---

## CI/CD Integration

`ai_assessment_checker.py` exits with code `1` if any systems are OVERDUE or have MISSING dates, which makes it suitable for a scheduled pipeline check. The workflow shipped with this repository is `.github/workflows/ai-assessment-check.yml`. It runs weekly, uploads the report as a build artifact, and is deliberately marked `continue-on-error` so that the sample inventory does not fail the repository build. Remove `continue-on-error` when you point it at a real inventory and want the pipeline to block.

---

## ISO 42001 Alignment

| Control Area | ISO 42001 Reference | How These Scripts Help |
|---|---|---|
| Performance evaluation | Clause 9.1 | Automates monitoring of assessment currency across the AI inventory |
| Continual improvement | Clause 10.1 | Flags gaps before they become audit findings |
| Risk management | Clause 6.1 | Prioritises overdue high and critical risk systems for remediation |
| Risk treatment and SoA | Clause 6.1.3 | Tracks and exports Annex A control implementation status |
| Internal audit support | Clause 9.2 | Generates audit-ready evidence reports with timestamps |

---

*Part of the [ISO/IEC 42001:2023 AI Governance Toolkit](../README.md)*
