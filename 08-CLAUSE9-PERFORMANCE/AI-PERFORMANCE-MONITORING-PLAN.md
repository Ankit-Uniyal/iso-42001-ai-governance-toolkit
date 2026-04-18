# AI Performance Monitoring Plan
## ISO/IEC 42001:2023 | Clause 9.1 — Template

**Document ID:** AIMS-MONPLAN-001
**Version:** 1.0
**Owner:** Risk Manager / AI Governance Lead
**Date:** ___________________________
**Review Cycle:** Annual; updated when systems or objectives change

---

## Purpose

This plan defines what is monitored across the AIMS and individual AI systems, how monitoring is conducted, when results are analysed, and who is responsible. It satisfies the requirements of Clause 9.1.

---

## Part 1 — Technical AI System Metrics (per AI System)

For each in-scope AI system, monitor the following:

| Metric | Description | Target / Threshold | Monitoring Method | Frequency | Owner | Alert Trigger | Escalation Path |
|--------|-------------|-------------------|------------------|-----------|-------|--------------|----------------|
| Model Accuracy | Overall prediction accuracy | Per system specification | Automated monitoring | Monthly | AI System Owner | > 5% drop from baseline | AI Gov Lead |
| Precision / Recall / F1 | Quality of predictions | Per system specification | Automated monitoring | Monthly | AI System Owner | Below minimum threshold | AI Gov Lead |
| Model Drift | Performance degradation over time | < 5% drift from baseline | Drift detection tool | Monthly | AI Developer | Any drift > 5% | AI System Owner |
| Fairness Score | Disparate impact ratio across protected groups | Between 0.8 and 1.25 | Fairness evaluation tool | Monthly | AI Developer | Outside 0.8–1.25 range | DPO + AI Gov Lead |
| Explainability Coverage | % of high-risk decisions with explanation available | 100% for high-risk decisions | Log review | Per decision | AI System Owner | Any gap | AI Gov Lead |
| System Uptime | AI system availability | Per SLA | Infrastructure monitoring | Continuous | Technical Lead | Below SLA | AI System Owner |
| Error Rate | Rate of system errors / exceptions | Baseline + < 5% increase | Log monitoring | Continuous | Technical Lead | Spike above threshold | AI System Owner |

---

## Part 2 — AIMS Process Metrics (System-Wide)

| Metric | Description | Target | Data Source | Frequency | Owner | Current Value | Status |
|--------|-------------|--------|------------|-----------|-------|--------------|--------|
| Impact Assessments Current | % of in-scope AI systems with current impact assessment | 100% | AI Systems Inventory | Quarterly | AI System Owner | | |
| Training Completion | % of in-scope staff who completed AI awareness training | 90% | LMS / Training Records | Annual | HR | | |
| Audit Programme Progress | % of planned audits completed on schedule | 100% | Audit Programme | Annual | Internal Auditor | | |
| Open Risk Treatments | Number of overdue risk treatment actions | 0 | Risk Register | Monthly | Risk Manager | | |
| AI Incidents | Number of AI-related incidents per quarter | Decreasing trend | Incident Log | Quarterly | AI Gov Lead | | |
| Supplier Assessments Current | % of Tier 1 AI suppliers with current assessment | 100% | Supplier Register | Annual | AI Gov Lead | | |
| Objectives Achievement | % of AI objectives on track | > 80% | Objectives Register | Quarterly | AI Gov Lead | | |
| Document Currency | % of AIMS documents reviewed within review cycle | 95% | Master Document List | Quarterly | AI Gov Lead | | |

---

## Part 3 — Monitoring Records

### Monitoring Log

| Date | Metric | System / Area | Value Measured | Target | Status | Action Required | Owner | Action Due |
|------|--------|--------------|---------------|--------|--------|----------------|-------|-----------|
| | | | | | Green / Amber / Red | | | |
| | | | | | | | | |

---

## Part 4 — Reporting

| Report | Audience | Frequency | Content | Owner |
|--------|---------|-----------|---------|-------|
| AI Performance Dashboard | AI Gov Lead, Risk Manager | Monthly | All system metrics with trend indicators | AI System Owners |
| AIMS KPIs Report | Management | Quarterly | AIMS process metrics vs targets | AI Gov Lead |
| Board AI Risk Summary | Board / Senior Management | Quarterly | Risk status, incidents, objectives | Risk Manager / AI Gov Lead |
| Management Review Input | Management Review Meeting | Annual minimum | Full AIMS performance summary | AI Gov Lead |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 9.1 | See root README.md for full index*
