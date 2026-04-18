# AI Deployment Checklist
## ISO/IEC 42001:2023 | Clause 8.1 — Pre-Deployment Gate Template

**Document ID:** AIMS-DEPCHK-001 / [System-specific instance ID]
**AI System Name:** ___________________________
**System ID:** ___________________________
**Deployment Type:** New System / Major Update / Minor Update
**Version Being Deployed:** ___________________________
**Deployment Date Requested:** ___________________________
**System Owner:** ___________________________
**Review Date:** ___________________________

---

## Instructions

Complete this checklist before any AI system or significant update is deployed to production. All items must be marked PASS, N/A (with justification), or FAIL. Any FAIL items must be resolved before deployment is approved. This checklist must be signed off by the AI Governance Lead and the AI System Owner.

**Deployment Decision:** APPROVED / APPROVED WITH CONDITIONS / REJECTED

---

## Section 1 — Governance and Documentation

| # | Check | Status (PASS/FAIL/N/A) | Evidence / Notes |
|---|-------|----------------------|-----------------|
| 1.1 | AI Systems Inventory has been updated to include this system/version | | |
| 1.2 | AI System Impact Assessment (ASIA) has been completed and approved | | ASIA Ref: |
| 1.3 | AI System Card / Model Card is complete and current | | |
| 1.4 | Risk assessment has been completed for this system/version | | Risk Register Ref: |
| 1.5 | Risk treatment controls are in place for all High/Critical risks | | |
| 1.6 | System Owner has been formally assigned and confirmed | | |
| 1.7 | Change Control record raised (if updating existing system) | | CHG Ref: |

---

## Section 2 — Technical Quality and Testing

| # | Check | Status | Evidence |
|---|-------|--------|---------|
| 2.1 | Performance testing completed (accuracy, precision, recall, F1) | | Test report Ref: |
| 2.2 | Bias and fairness evaluation completed across protected characteristics | | Bias test report Ref: |
| 2.3 | Adversarial and robustness testing completed | | |
| 2.4 | Security testing completed (model inversion, data poisoning, prompt injection) | | |
| 2.5 | User acceptance testing (UAT) completed and signed off | | UAT Ref: |
| 2.6 | Testing conducted in a representative environment | | |
| 2.7 | Model documentation (model card) reviewed for accuracy | | |

---

## Section 3 — Data Governance

| # | Check | Status | Evidence |
|---|-------|--------|---------|
| 3.1 | Training data sources documented with provenance | | |
| 3.2 | Legal basis for data use confirmed (consent / legitimate interest) | | |
| 3.3 | Data quality assessment completed | | |
| 3.4 | Training data reviewed for bias and representativeness | | |
| 3.5 | Personal data handling reviewed with DPO | | DPO sign-off date: |

---

## Section 4 — Transparency and Human Oversight

| # | Check | Status | Evidence |
|---|-------|--------|---------|
| 4.1 | User-facing AI disclosure statement prepared | | |
| 4.2 | Explainability mechanism implemented (where required for high-risk decisions) | | |
| 4.3 | Human oversight mechanisms active for high-stakes decisions | | |
| 4.4 | Escalation path to human review documented | | |
| 4.5 | Users informed when they are interacting with an AI system | | |

---

## Section 5 — Monitoring and Operations

| # | Check | Status | Evidence |
|---|-------|--------|---------|
| 5.1 | Performance monitoring configured and tested | | |
| 5.2 | Fairness drift monitoring configured | | |
| 5.3 | Alert thresholds defined and tested | | |
| 5.4 | Incident reporting channel established | | |
| 5.5 | Rollback / contingency plan documented | | |
| 5.6 | Post-deployment review date scheduled | | Scheduled date: |

---

## Section 6 — Compliance

| # | Check | Status | Evidence |
|---|-------|--------|---------|
| 6.1 | EU AI Act risk classification confirmed | | Risk level: High / Limited / Minimal |
| 6.2 | All applicable EU AI Act requirements addressed | | |
| 6.3 | GDPR/privacy requirements satisfied | | |
| 6.4 | Any sector-specific regulatory requirements satisfied | | |

---

## Deployment Approval

| Role | Name | Decision | Signature | Date |
|------|------|---------|-----------|------|
| AI System Owner | | Approved / Rejected | | |
| AI Governance Lead | | Approved / Rejected | | |
| DPO (if personal data involved) | | Approved / Rejected | | |
| Risk Manager (if High/Critical risk) | | Approved / Rejected | | |

**Overall Deployment Decision:** APPROVED / APPROVED WITH CONDITIONS / REJECTED

**Conditions (if any):** ___________________________

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 8.1 | See root README.md for full index*
