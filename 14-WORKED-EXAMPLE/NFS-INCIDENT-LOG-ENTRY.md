# AI Incident Log — Worked Examples

## ISO/IEC 42001:2023 | Clause 10.1 & Annex A.9 | FICTIONAL REFERENCE ONLY

**Document ID:** NFS-INCIDENT-LOG-EXAMPLE
**Version:** 1.0 | **Owner:** Head of AI Governance | **Date:** 14 March 2025

> **FICTIONAL EXAMPLE:** All incidents, individuals, and outcomes described here relate to the fictional organisation Nexus Financial Services Ltd. This is for educational illustration of ISO/IEC 42001:2023 Clause 10.1 nonconformity and corrective action documentation only.

---

## How to Read These Entries

These entries follow the structure of the blank Nonconformity and Corrective Action Log in `09-CLAUSE10-IMPROVEMENT/NONCONFORMITY-CORRECTIVE-ACTION-LOG.md`. Two complete AI incident entries are shown: a bias monitoring alert (closed) and a data quality incident (in progress).

---

## Incident Entry 1: Bias Monitoring Alert — 18-24 Age Cohort

### Part A: Incident Identification

| Field | Entry |
|---|---|
| **Incident ID** | AIMS-INC-2025-001 |
| **Incident Title** | CreditIQ bias monitoring alert: 18-24 age group approval rate disparity exceeded threshold |
| **AI System Affected** | CreditIQ v2.1 (AIMS-SYS-001) |
| **Date Detected** | 07 January 2025, 09:14 UTC |
| **Detected By** | Automated bias monitoring dashboard (NFS-BIAS-MON-001) |
| **Detection Method** | Monthly bias metrics report: 18-24 vs 25-55 approval rate disparity reached -5.8% |
| **Reported To** | Head of AI Governance (Priya Sharma) |
| **Report Time** | 07 January 2025, 09:30 UTC |
| **Incident Classification** | Level 2 — Significant (potential regulatory reporting obligation; contained) |
| **AIMS Control Affected** | A.6.2.5 — Fairness monitoring; A.9.3 — Incident response |

### Part B: Incident Description

**What happened:**

The monthly automated bias monitoring report for December 2024 (generated 7 January 2025) flagged that the approval rate for 18-24 year old applicants had dropped to -5.8% below the 25-55 cohort approval rate. The NFS bias monitoring threshold is -5.0%; exceeding this threshold triggers an automatic Level 2 incident and investigation.

The affected period was December 2024 (31 days of production decisions). During this period, CreditIQ processed approximately 4,847 applications from applicants aged 18-24, of which an estimated 240-290 additional applicants (above the expected rate) may have received a DECLINE or HUMAN_REVIEW outcome.

**Initial timeline:**
- 01 Dec 2024: December production period begins
- 07 Jan 2025 09:14: Monthly bias report generated; alert triggered
- 07 Jan 2025 09:30: Head of AI Governance notified
- 07 Jan 2025 10:00: Incident team convened (AI Governance, Data Science, Legal/Compliance)
- 07 Jan 2025 14:00: Root cause hypothesis identified (see Part C)
- 09 Jan 2025: Root cause confirmed; no model change required
- 14 Jan 2025: Incident closed; monitoring enhanced

**Systems affected:**
- CreditIQ v2.1 automated decisioning (primary)
- NFS Loan Portal (customer-facing outcomes)
- Human Review Panel (downstream — increased queue for 18-24 borderline cases)

### Part C: Root Cause Analysis

**Investigation method:** Detailed analysis of December 2024 application population characteristics vs November 2024 and historical averages.

**Root cause identified:** Seasonal data anomaly. December represents an atypical lending period where the 18-24 applicant population shifts toward applicants with weaker credit profiles. Analysis of December applicant bureau scores showed the average Experian score for 18-24 applicants in December 2024 was 587 (vs annual average 623). This is driven by:

1. Students completing term-time employment leading to declared income reductions
2. Pre-Christmas credit applications from higher-risk applicants who had been declined elsewhere
3. Seasonal spending patterns creating higher existing debt-to-income ratios

**Key finding:** The model performed correctly given the input data. The disparity was driven by genuine risk differences in the December 18-24 applicant population, not model bias or proxy discrimination. The model was not behaving inconsistently — it was responding appropriately to legitimate risk signals.

**Excluded causes:**
- Proxy variable encoding of age: Excluded — age, postcode, and related proxies are explicitly excluded features
- Model degradation: Excluded — AUC-ROC remained at 0.847 throughout December
- Data pipeline error: Excluded — Experian data integrity checks passed; no anomalies in input feature distributions (PSI all < 0.10)

### Part D: Impact Assessment

| Dimension | Assessment |
|---|---|
| Customer harm | No direct harm identified. Decisions reflected genuine risk differences in applicant pool. |
| Regulatory obligation | No FCA reporting obligation triggered. Investigation documented. ICO notification not required. |
| Reputational risk | Low. Issue contained; not customer-visible; no press or complaints. |
| Financial impact | None. |
| Affected customers | Approximately 240-290 additional applications may have received less favourable outcomes, all consistent with genuine risk assessment. No remediation required. |
| GDPR implications | None. No personal data breach. |

### Part E: Corrective and Preventive Actions

| Action ID | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| CA-2025-001-01 | Enhance monitoring: add seasonal adjustment to bias thresholds for Dec-Jan period | Data Science | 01 Mar 2025 | Completed |
| CA-2025-001-02 | Add monthly cohort-level bureau score distribution to bias report for contextual analysis | Data Science | 01 Mar 2025 | Completed |
| CA-2025-001-03 | Update incident investigation procedure: include seasonal analysis step | AI Governance | 28 Feb 2025 | Completed |
| CA-2025-001-04 | Brief AI Ethics Committee on December anomaly and investigation conclusions | Head of AI Governance | 15 Jan 2025 | Completed |
| PA-2025-001-01 | Develop thin-file model variant for 18-24 cohort to improve baseline performance year-round (CreditIQ v2.2) | Data Science | Q3 2025 | In progress |

### Part F: Lessons Learned

1. **Threshold context matters:** Static bias thresholds do not account for seasonal population shifts. Seasonally-adjusted thresholds provide better signal vs noise.
2. **Investigation speed:** The 4.5-hour time from alert to root cause hypothesis was good. Target is < 8 hours for Level 2 incidents.
3. **Proactive stakeholder briefing:** Briefing the Ethics Committee proactively (before they asked) built confidence in the AIMS.
4. **Documentation quality:** This incident produced the clearest root cause analysis to date. Template to be used as reference for future investigations.

### Part G: Incident Closure

| Field | Entry |
|---|---|
| **Closure Date** | 14 January 2025 |
| **Closed By** | Priya Sharma, Head of AI Governance |
| **Closure Rationale** | Root cause identified and documented; no customer harm; corrective actions completed or tracked; monitoring enhanced |
| **Post-Closure Monitoring** | Enhanced seasonal bias monitoring in place; January 2025 bias report reviewed — disparity returned to -2.3% (within threshold) |
| **Status** | CLOSED |
| **Approved By** | Sarah Mitchell, Chief Risk Officer — 14 January 2025 |

---

## Incident Entry 2: Experian API Outage

### Part A: Incident Identification

| Field | Entry |
|---|---|
| **Incident ID** | AIMS-INC-2024-003 |
| **Incident Title** | Experian credit bureau API outage — 4-hour CreditIQ automated decisioning unavailability |
| **AI System Affected** | CreditIQ v2.1 (AIMS-SYS-001) |
| **Date Detected** | 12 August 2024, 14:23 UTC |
| **Detected By** | IT Operations monitoring (PagerDuty alert) |
| **Detection Method** | API health check failure: Experian endpoint returning HTTP 503 for > 5 minutes |
| **Reported To** | Head of IT Operations; Head of AI Governance |
| **Incident Classification** | Level 2 — Significant (operational disruption; no customer harm) |
| **AIMS Control Affected** | A.9.3 — AI system incident management; A.7.4 — Operational continuity |

### Part B: Incident Description

At 14:23 UTC on 12 August 2024, the Experian API health check began returning HTTP 503 errors. CreditIQ v2.1 automatically routed all new applications to the manual review queue per the failover procedure. The Experian outage lasted from approximately 14:20 UTC to 18:35 UTC (4 hours 15 minutes).

During the outage, approximately 340 loan applications were queued for manual processing. The manual processing team (12 credit officers) cleared the backlog by 09:00 UTC on 13 August 2024. Customers received automated acknowledgement messages advising of a processing delay.

### Part C: Root Cause

Experian confirmed the outage was caused by a misconfigured load balancer deployment to their production environment at 14:17 UTC. Rollback was completed at 18:35 UTC. This was an Experian infrastructure failure — no NFS systems were at fault.

### Part D: Impact Assessment

| Dimension | Assessment |
|---|---|
| Customer harm | Minor: ~340 customers experienced a processing delay of up to 18 hours vs standard 4-hour SLA |
| Regulatory | No FCA reporting obligation; delay within acceptable service parameters |
| Financial | Staff overtime cost approx GBP 3,200 (manual processing backlog); no revenue loss |
| Reputational | 12 customer complaints received (standard rate is 0-2 per day); all resolved |

### Part E: Corrective Actions (Closed)

| Action ID | Action | Owner | Status |
|---|---|---|---|
| CA-2024-003-01 | Review and update manual processing procedure; add capacity plan for 4-hour+ outages | Credit Operations | Completed Oct 2024 |
| CA-2024-003-02 | Negotiate enhanced Experian SLA: incident notification within 15 minutes | Legal/Procurement | Completed Dec 2024 |
| CA-2024-003-03 | Develop Equifax secondary bureau integration as automated fallback | Data Science | In progress — Q3 2025 |
| CA-2024-003-04 | Implement cached bureau scores for existing NFS customers (max 7-day cache) | IT Operations | In progress — Q2 2025 |
| CA-2024-003-05 | Update BCP AI system continuity procedure to reflect lessons learned | IT Operations | Completed Sep 2024 |

| **Incident Status** | CLOSED — 30 September 2024 |
|---|---|

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Worked Example — Clause 10.1 / Annex A.9 | See root README.md for full index*
