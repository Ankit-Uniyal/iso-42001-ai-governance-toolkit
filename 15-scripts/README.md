# /scripts — GRC Engineering Automation

> **Bridging Policy and Engineering** for ISO/IEC 42001:2023 AI Governance

This folder contains automation scripts that operationalise the governance controls defined in the ISO 42001 toolkit. Rather than treating compliance as a static document exercise, these scripts turn policy requirements into **executable, repeatable checks** — the hallmark of modern GRC Engineering.

---

## Scripts

| Script | Purpose | ISO 42001 Clause |
|--------|---------|-----------------|
| `ai_assessment_checker.py` | Checks assessment currency for all AI systems in inventory | Clause 9.1 — Monitoring, Measurement, Analysis and Evaluation |

---

## ai_assessment_checker.py

### What it does

Reads a CSV inventory of AI systems and evaluates whether each system's **Last Assessment Date** falls within an acceptable window (default: 365 days). It produces:

- A formatted **console report** with status for every system
- A saved **text report** (`assessment_report.txt`) for audit evidence
- A **non-zero exit code** when overdue systems exist (CI/CD pipeline friendly)

### Status levels

| Status | Meaning |
|--------|---------|
| `COMPLIANT` | Assessment is within the threshold window |
| `DUE SOON` | Assessment is within 30 days of becoming overdue |
| `OVERDUE` | Assessment date exceeds the threshold |
| `MISSING DATE` | No assessment date recorded — immediate action required |

### Requirements

- Python 3.9+
- No external dependencies (standard library only)

### Usage

```bash
# Basic run using the sample CSV
python scripts/ai_assessment_checker.py

# Specify a custom input file
python scripts/ai_assessment_checker.py --input path/to/your/ai_inventory.csv

# Use a 180-day threshold instead of 365
python scripts/ai_assessment_checker.py --input scripts/sample_ai_systems.csv --threshold 180

# Specify a custom output report path
python scripts/ai_assessment_checker.py --input scripts/sample_ai_systems.csv --output reports/q2_assessment.txt
```

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
| `last_assessment_date` | Date of last formal assessment (YYYY-MM-DD) | `2025-06-15` |

See `sample_ai_systems.csv` for a working example.

### Sample output

```
================================================================================
  ISO/IEC 42001:2023 — AI System Assessment Currency Report
  Run Date  : 2026-04-11
  Threshold : 365 days
================================================================================

  ID          System Name                   Owner               Risk        Last Assessment      Days Since   Status
  --------------------------------------------------------------------------------------------------------------
  AI-001      Customer Churn Predictor      Data Science Team   High        2025-10-15           178          COMPLIANT
  AI-002      Resume Screening Engine       HR Technology       High        2025-04-20           356          DUE SOON
  AI-003      Fraud Detection Model         Risk & Compliance   Critical    2024-12-01           496          OVERDUE
  AI-006      Loan Approval Assistant       Credit Risk         Critical    2024-11-10           517          OVERDUE
  AI-009      Image Classification Service  Computer Vision     High                             N/A          MISSING DATE

────────────────────────────────────────────────
  SUMMARY
  Total AI Systems : 10
  [OK]  Compliant  : 6
  [!!]  Due Soon   : 1
  [XX]  Overdue    : 2
  [--]  Missing    : 1
────────────────────────────────────────────────

  ACTION REQUIRED: The following systems need immediate reassessment:

    - [AI-003] Fraud Detection Model — Owner: Risk & Compliance
    - [AI-006] Loan Approval Assistant — Owner: Credit Risk
    - [AI-009] Image Classification Service — Owner: Computer Vision Team
```

---

## CI/CD Integration

The script exits with code `1` if any systems are OVERDUE or have MISSING dates, making it suitable for integration into GitHub Actions or any CI pipeline:

```yaml
# .github/workflows/ai-assessment-check.yml
name: AI Assessment Currency Check

on:
  schedule:
    - cron: '0 8 * * 1'   # Every Monday at 08:00 UTC
  workflow_dispatch:

jobs:
  check-assessments:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run AI Assessment Checker
        run: python scripts/ai_assessment_checker.py --input scripts/sample_ai_systems.csv
```

---

## ISO 42001 Alignment

| Control Area | ISO 42001 Reference | How This Script Helps |
|---|---|---|
| Performance evaluation | Clause 9.1 | Automates monitoring of assessment currency across AI inventory |
| Continual improvement | Clause 10.1 | Flags gaps before they become audit findings |
| Risk management | Clause 6.1 | Prioritises overdue high/critical risk systems for remediation |
| Internal audit support | Clause 9.2 | Generates audit-ready evidence reports with timestamps |

---

*Part of the [ISO/IEC 42001:2023 AI Governance Toolkit](../README.md)*
