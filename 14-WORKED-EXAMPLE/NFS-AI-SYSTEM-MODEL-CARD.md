# AI System Model Card — CreditIQ v2.1

## ISO/IEC 42001:2023 | Clause 8.4 & Annex A.6 | FICTIONAL REFERENCE ONLY

**Document ID:** NFS-MODELCARD-002
**Version:** 2.1.3 | **Owner:** Head of AI Governance | **Date:** 01 April 2025 | **Review Cycle:** Quarterly

> **FICTIONAL EXAMPLE:** CreditIQ v2.1 is a fictional AI system created for educational illustration of ISO/IEC 42001:2023 compliance. No real organisation, credit data, or individuals are represented.

---

## Section 1: System Identity

| Field | Details |
|---|---|
| **System Name** | CreditIQ |
| **Version** | v2.1 (production); v2.2 (in development) |
| **System ID** | AIMS-SYS-001 |
| **System Type** | Supervised machine learning — gradient boosting classifier (XGBoost) |
| **Primary Purpose** | Automated credit scoring and loan approval/rejection recommendation for personal loans |
| **Deployment Status** | Live in production |
| **Go-Live Date** | 03 June 2024 |
| **System Owner** | Head of Retail Credit Risk, NFS |
| **Model Card Author** | Priya Sharma, Head of AI Governance |
| **Last Updated** | 01 April 2025 |

---

## Section 2: Intended Use

CreditIQ v2.1 is designed exclusively for scoring credit applications, generating approval/decline recommendations for personal loans, producing explanation summaries for the Human Review Panel for borderline cases, and supporting credit risk officers with ranked feature importance for manual reviews.

**Out-of-Scope Uses (explicitly prohibited):**
- Mortgage lending decisions
- Business lending or commercial credit decisions
- Decisions involving customers under 18
- Use outside the United Kingdom
- Any use not covered by the current DPIA (ICO ref: DPIA-NFS-2024-007)

---

## Section 3: AI System Classification

| Dimension | Classification | Basis |
|---|---|---|
| **EU AI Act risk category** | High Risk | Annex III, Category 5(b): creditworthiness evaluation |
| **NFS internal risk tier** | Tier 1 — Critical | Directly affects financial access; high volume |
| **Human oversight level** | Level 2 — Human-in-the-loop (mandatory for borderline/declined) | NFS AI Oversight Policy §4.2 |
| **Data sensitivity** | Special — financial and personal data | UK GDPR; FCA data classification |
| **Reversibility** | Partially reversible — declined applications can request human review | Consumer Duty requirement |

---

## Section 4: Technical Architecture

| Parameter | Value |
|---|---|
| Algorithm | XGBoost v1.7 (gradient boosting decision trees) |
| Training framework | Python 3.11, scikit-learn 1.4, XGBoost 1.7 |
| Model artefact | creditiq_v2.1_prod.pkl (saved via joblib) |
| Serving infrastructure | NFS on-premise API server (Red Hat Linux 9.2), FastAPI v0.104 |
| Decision threshold | Score >= 720: Approve / Score < 600: Decline / 600-719: Human review |
| Inference latency (p99) | 340ms |
| Throughput | ~1,200 decisions/hour at peak |

**Input Features:** Credit bureau score (Experian), active credit accounts (Equifax), CCJs (Experian), months at address, employment status, net income (declared), debt-to-income ratio (derived), NFS transaction history, loan amount and term.

**Excluded features (fairness controls):** Age, gender, ethnicity, nationality, postcode, disability status.

**Output:** Decision (APPROVE/DECLINE/HUMAN_REVIEW), credit score (300-850), top 5 SHAP feature contributions, confidence band, recommended loan terms.

---

## Section 5: Training Data

| Aspect | Details |
|---|---|
| Training dataset | NFS historical loan applications 2019-2023 (n = 847,000) |
| Validation dataset | NFS applications Q1-Q2 2024 (n = 94,000), held out |
| Test dataset | NFS applications Q3 2024 (n = 47,000), held out |
| DPIA reference | DPIA-NFS-2024-007 (UK ICO registered) |
| Known class imbalance | Default rate 4.2% — handled via SMOTE oversampling |
| Data refresh cadence | Model retrained quarterly with rolling 5-year window |
| Data retention | Training data retained 7 years per FCA record-keeping rules |

---

## Section 6: Performance Metrics (Q1 2025)

| Metric | Value | Threshold | Status |
|---|---|---|---|
| AUC-ROC | 0.847 | >= 0.80 | PASS |
| Gini coefficient | 0.694 | >= 0.65 | PASS |
| Precision (defaults caught) | 71.3% | >= 65% | PASS |
| Recall (defaults caught) | 68.9% | >= 60% | PASS |
| False positive rate | 12.4% | <= 15% | PASS |
| Decision override rate | 8.2% | <= 12% | PASS |
| Average decision time | 1.8 seconds | <= 5 seconds | PASS |
| System uptime (rolling 90 days) | 99.94% | >= 99.5% | PASS |

---

## Section 7: Fairness and Bias Assessment

| Characteristic | Metric Used | Result (Q1 2025) | Status |
|---|---|---|---|
| Gender | Equalised odds ratio | 0.97 (M vs F) | PASS (threshold: 0.90-1.10) |
| Age group (18-24 vs 25-55) | Approval rate disparity | -3.1% for 18-24 cohort | MONITORING |
| Ethnicity | Demographic parity ratio | 0.94 | PASS |
| Disability (declared) | Approval rate | No significant difference | PASS |

**Known limitations:** 18-24 age group has slight approval rate disparity due to thinner credit files (not model bias). Self-employed applicants have higher HUMAN_REVIEW rate (23% vs 8% avg). New-to-NFS customers have slightly lower AUC (0.831 vs 0.853).

---

## Section 8: Explainability

SHAP (SHapley Additive exPlanations) values are calculated per decision. Plain English summaries of top 3 adverse factors are generated for all declined/borderline cases. Customers can request full written explanation within 30 days per UK GDPR Art.22.

**Example customer explanation:**
> "Your application was not approved on this occasion. The main factors considered were: your current level of existing credit commitments, the number of recent credit applications in the past 6 months, and your declared debt-to-income ratio. You have the right to request a review of this decision by a human credit officer."

---

## Section 9: Human Oversight

| Oversight Mechanism | Description |
|---|---|
| Mandatory human review | All DECLINE decisions on applications >= 15,000 GBP |
| Borderline review | All HUMAN_REVIEW outputs go to credit officer queue (SLA: 4 business hours) |
| Override capability | Credit Risk Officers can override any recommendation with documented justification |
| Audit trail | All decisions, overrides, and reasons logged for 7 years |
| Customer appeal | Customers may request human review within 30 days |

---

## Section 10: Security and Data Protection

| Control | Status |
|---|---|
| Model artefact encryption (AES-256) | Implemented |
| API authentication (OAuth 2.0 + mTLS) | Implemented |
| Data minimisation | Only required features passed; no PII in model artefact |
| Access control | Role-based; production model access limited to 4 named Data Scientists |
| Penetration testing | Annual — last Nov 2024; no critical findings |
| DPIA status | Completed; ICO registered; next review Jun 2025 |

---

## Section 11: Incident and Change History

| Date | Type | Description | Outcome |
|---|---|---|---|
| 12 Aug 2024 | Incident | Experian API outage — 4-hour approval outage | RCA completed; fallback updated |
| 19 Nov 2024 | Change | Retrained on Q3 2024 data; AUC improved 0.831 to 0.847 | Deployed after UAT and bias checks |
| 07 Jan 2025 | Incident | Bias alert: 18-24 approval disparity spike to 5.8% | Data anomaly (holiday period); no model change |
| 15 Mar 2025 | Change | Decision threshold adjusted: HUMAN_REVIEW lower bound 610 to 600 | Reduced false decline rate by 0.8% |

---

## Section 12: Approval

| Role | Name | Date |
|---|---|---|
| Head of AI Governance | Priya Sharma | 01 April 2025 |
| Head of Credit Risk | David Okonkwo | 01 April 2025 |
| Data Protection Officer | Rachel Ford | 28 March 2025 |
| Information Security | Tom Briggs | 31 March 2025 |

---

## Review History

| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0 | 03 Jun 2024 | Initial model card at go-live | P. Sharma |
| 2.0 | 19 Nov 2024 | Updated for v2.1 retrain; bias section added | P. Sharma |
| 2.1.3 | 01 Apr 2025 | Q1 2025 metrics update; incident log updated | P. Sharma |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Worked Example — Clause 8.4 / Annex A.6 | See root README.md for full index*
