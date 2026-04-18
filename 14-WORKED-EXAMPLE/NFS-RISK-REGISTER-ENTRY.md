# AI Risk Register — Worked Examples

## ISO/IEC 42001:2023 | Clause 6.1 & Annex A.6 | FICTIONAL REFERENCE ONLY

**Document ID:** NFS-RISK-REGISTER-EXAMPLE
**Version:** 1.0 | **Owner:** Head of AI Governance | **Date:** 14 March 2025 | **Review Cycle:** Quarterly

> **FICTIONAL EXAMPLE:** All risks, scenarios, and mitigations described here relate to the fictional organisation Nexus Financial Services Ltd and its fictional CreditIQ v2.1 AI system. This is for educational illustration only.

---

## How to Read These Entries

Each risk entry follows the structure of the blank AI Risk Register template in `05-CLAUSE6-PLANNING/AI-RISK-REGISTER.md`. Three complete entries are shown below covering different risk categories: algorithmic bias, model drift, and third-party dependency.

---

## Risk Entry 1: Algorithmic Bias in Credit Decisions

| Field | Entry |
|---|---|
| **Risk ID** | AIMS-RISK-001 |
| **Risk Title** | Algorithmic bias resulting in discriminatory credit decisions for protected characteristic groups |
| **AI System** | CreditIQ v2.1 (AIMS-SYS-001) |
| **Risk Owner** | Head of AI Governance (Priya Sharma) |
| **Date Identified** | 02 September 2024 |
| **Last Reviewed** | 14 March 2025 |
| **Review Cycle** | Monthly |
| **Status** | Active — under monitoring |

### Risk Description

CreditIQ v2.1 may produce systematically different approval rates for applicants sharing protected characteristics (age, gender, ethnicity), even if these characteristics are not directly used as input features. This can occur through proxy variables — for example, postcode correlating with ethnicity, or employment status correlating with age. Such outcomes could constitute indirect discrimination under the Equality Act 2010, violate FCA Consumer Duty fair outcomes requirements, and constitute prohibited practice under EU AI Act Article 5.

### Risk Cause

- Proxy variables in training data encoding protected characteristics
- Historical training data (2019-2023) may reflect societal bias in past lending decisions
- Underrepresentation of certain demographic groups in training data
- Feature interactions producing disparate impact not visible in individual feature analysis

### Risk Consequence

- Regulatory action by FCA (financial penalty up to 10% of annual turnover)
- Legal challenge under Equality Act 2010
- Reputational damage and customer trust loss
- Remediation cost for affected customers (loan offers, compensation)
- EU AI Act infringement proceedings

### Risk Assessment

| Dimension | Score | Basis |
|---|---|---|
| Likelihood (1-5) | 3 — Possible | AI systems in financial services frequently exhibit proxy bias; detected in v1.x |
| Impact (1-5) | 5 — Catastrophic | Regulatory penalty + reputational damage + customer harm |
| Inherent Risk Score | 15 (High) | 3 x 5 |
| Control Effectiveness | 3 — Partial | Bias monitoring implemented; some gaps in self-employed cohort analysis |
| Residual Risk Score | 6 (Medium) | Post-control assessment |
| Risk Appetite | Medium | Board-approved AI risk appetite (NFS-BOARD-2024-003) |
| Risk Status | Within appetite | Residual 6 < appetite threshold 8 |

### Current Controls

| Control | Owner | Status | Evidence |
|---|---|---|---|
| Protected characteristic features explicitly excluded from model inputs | Data Science Lead | Implemented | Feature list in Model Card NFS-MODELCARD-002 |
| Monthly bias monitoring across 4 demographic dimensions | AI Governance | Implemented | Monthly bias report NFS-BIAS-REPORT |
| Quarterly fairness testing (equalised odds, demographic parity) | Data Science | Implemented | Quarterly model review reports |
| Human review mandatory for all declined applications >= GBP 15,000 | Credit Risk | Implemented | Decision Audit System logs |
| Customer right to human review of any adverse decision | Legal/Compliance | Implemented | Website T&Cs; customer communications |
| SHAP explainability for all decisions | Data Science | Implemented | NFS-MODELCARD-002 Section 8 |

### Residual Risk Treatment

Current residual risk of 6 (Medium) is within board-approved appetite. No additional treatment required at this stage. The planned thin-file model variant for 18-24 cohort (CreditIQ v2.2) will further reduce residual risk on age-related disparity.

### Key Risk Indicators

| KRI | Target | Current | Trigger |
|---|---|---|---|
| Gender approval rate disparity | < 5% | 3% (M vs F) | Green |
| Ethnicity demographic parity ratio | 0.90-1.10 | 0.94 | Green |
| Age group (18-24) approval disparity | < 5% | -3.1% | Green (monitoring) |
| Human review override rate | < 12% | 8.2% | Green |

---

## Risk Entry 2: Model Drift Leading to Performance Degradation

| Field | Entry |
|---|---|
| **Risk ID** | AIMS-RISK-002 |
| **Risk Title** | Model drift causing degraded credit scoring accuracy and increased default rates |
| **AI System** | CreditIQ v2.1 (AIMS-SYS-001) |
| **Risk Owner** | Head of Data Science |
| **Date Identified** | 03 June 2024 |
| **Last Reviewed** | 14 March 2025 |
| **Review Cycle** | Monthly |
| **Status** | Active — under monitoring |

### Risk Description

CreditIQ v2.1 was trained on 2019-2023 historical loan data. The macroeconomic environment has changed significantly (cost-of-living crisis, interest rate rises). If the statistical properties of new applicants diverge significantly from the training distribution (concept drift or data drift), the model's credit risk predictions may become inaccurate — leading to either excessive defaults (too many risky approvals) or excessive declines (too many creditworthy customers rejected). Either outcome represents both financial and customer harm.

### Risk Assessment

| Dimension | Score | Basis |
|---|---|---|
| Likelihood (1-5) | 3 — Possible | Economic conditions have changed materially since 2019 training data |
| Impact (1-5) | 4 — Significant | Increased defaults = financial loss; increased false declines = customer harm + Consumer Duty breach |
| Inherent Risk Score | 12 (High) | 3 x 4 |
| Control Effectiveness | 4 — Strong | PSI drift detection + quarterly retraining + automated alerts |
| Residual Risk Score | 4 (Low) | Post-control assessment |
| Risk Status | Within appetite | Residual 4 < appetite threshold 8 |

### Current Controls

| Control | Owner | Status | Evidence |
|---|---|---|---|
| Population Stability Index (PSI) monitoring on all 10 input features | Data Science | Implemented | Monthly PSI report |
| Automated alert when PSI > 0.20 on any feature | Data Science | Implemented | Monitoring dashboard |
| Quarterly model retraining on rolling 5-year window | Data Science | Implemented | Model versioning log |
| AUC-ROC monitoring: alert if drops below 0.80 | Data Science | Implemented | Weekly AUC report |
| Champion/challenger framework for model version comparison | Data Science | Implemented | Model governance procedure |
| Model rollback procedure documented | IT Operations | Implemented | BCP document NFS-BCP-AI-001 |

### Key Risk Indicators

| KRI | Target | Current | Trigger |
|---|---|---|---|
| AUC-ROC | >= 0.80 | 0.847 | Green |
| Maximum PSI (any feature) | < 0.20 | 0.09 (DTI ratio) | Green |
| 90-day default rate vs expected | < +2% deviation | +0.3% | Green |
| Retraining frequency | Quarterly | Quarterly (last Nov 2024) | Green |

---

## Risk Entry 3: Third-Party Data Supplier Dependency (Experian API)

| Field | Entry |
|---|---|
| **Risk ID** | AIMS-RISK-003 |
| **Risk Title** | Experian credit bureau API outage causing inability to make automated credit decisions |
| **AI System** | CreditIQ v2.1 (AIMS-SYS-001) |
| **Risk Owner** | Head of IT Operations |
| **Date Identified** | 03 June 2024 |
| **Last Reviewed** | 14 March 2025 |
| **Review Cycle** | Quarterly |
| **Status** | Active — accepted with controls |

### Risk Description

CreditIQ v2.1 makes a live API call to Experian at decision time to retrieve the applicant's current credit bureau score, which is the primary predictive feature (highest SHAP importance). If the Experian API is unavailable (outage, rate limiting, authentication failure), the system cannot produce a reliable automated decision. This dependency was realised on 12 August 2024 when a 4-hour Experian outage caused CreditIQ to route all applications to manual processing, creating a backlog of approximately 340 applications and a customer-facing delay.

### Risk Assessment

| Dimension | Score | Basis |
|---|---|---|
| Likelihood (1-5) | 2 — Unlikely | Experian SLA is 99.9% uptime; one incident in 9 months of operation |
| Impact (1-5) | 3 — Moderate | Operational disruption; no customer financial harm; reputational risk if extended |
| Inherent Risk Score | 6 (Medium) | 2 x 3 |
| Control Effectiveness | 3 — Partial | Manual fallback exists but labour-intensive; Equifax secondary source not yet integrated |
| Residual Risk Score | 4 (Low) | Post-control assessment |
| Risk Status | Within appetite | Residual 4 < appetite threshold 6 (operational risks) |

### Current Controls

| Control | Owner | Status | Evidence |
|---|---|---|---|
| Experian API health monitoring (30-second ping) | IT Operations | Implemented | Monitoring dashboard |
| Automated failover to manual review queue when API unavailable | IT Operations | Implemented | Tested Aug 2024 incident |
| Manual processing procedure for bureau outage | Credit Operations | Implemented | NFS-OPS-MANUAL-003 |
| Experian contractual SLA: 99.9% uptime, 4-hour RTO | Legal | Implemented | Experian MSA 2023 |
| Customer communication template for processing delays | Customer Services | Implemented | Updated post Aug 2024 incident |

### Planned Additional Controls (Treatment)

| Treatment | Owner | Target Date | Status |
|---|---|---|---|
| Integrate Equifax as secondary bureau source (automatic failover) | Data Science | Q3 2025 | In progress |
| Cache last-known bureau score (max 7 days) for existing NFS customers | IT Operations | Q2 2025 | Planned |
| Explore batch pre-scoring for existing customers | Data Science | Q4 2025 | Under review |

---

## Risk Rating Matrix Reference

| Score | Rating | Description |
|---|---|---|
| 1-3 | Low | Acceptable; monitor only |
| 4-6 | Medium | Active monitoring; consider additional controls |
| 7-12 | High | Treatment plan required; escalate to CRO |
| 13-25 | Critical | Immediate treatment required; board notification |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Worked Example — Clause 6.1 / Annex A.6 | See root README.md for full index*
