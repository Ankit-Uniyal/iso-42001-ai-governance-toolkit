# Clause 9 — Performance Evaluation
## ISO/IEC 42001:2023 | Implementation Guide

> **Purpose:** You cannot manage what you do not measure. Clause 9 ensures you systematically monitor, measure, analyse, and evaluate your AIMS — and report results to management so they can drive improvement.

---

## Files in This Folder

| File | Contents |
|------|---------|
| README.md | This clause guide |
| INTERNAL-AUDIT-PROCEDURE.md | How to plan and conduct AIMS internal audits |
| MANAGEMENT-REVIEW-TEMPLATE.md | Agenda and template for management review meetings |
| ISO42001-INTERNAL-AUDIT-GUIDE.md | Detailed guide for auditing each clause |

---

## 9.1 — Monitoring, Measurement, Analysis and Evaluation

### What it requires
Determine what to monitor and measure, how to do it, when to analyse results, and who is responsible. Then actually do it and keep records.

### AI Performance Metrics Framework

**Technical Performance Metrics (per AI System)**

| Metric | Description | Target | Frequency |
|--------|-------------|--------|-----------|
| Model Accuracy | Overall prediction accuracy | As per system spec | Monthly |
| Precision / Recall / F1 | Quality of positive predictions | As per system spec | Monthly |
| Model Drift | Degradation in performance over time | < 5% drift from baseline | Monthly |
| Fairness Score | Disparate impact ratio across protected groups | < 0.8 or > 1.25 triggers review | Monthly |
| Explainability Coverage | % of decisions that can be explained on request | 100% for high-risk decisions | Per decision |
| System Uptime | AI system availability | As per SLA | Continuous |

**AIMS Process Metrics (system-wide)**

| Metric | Description | Target | Frequency |
|--------|-------------|--------|-----------|
| Impact Assessments Completed | % of in-scope AI systems with current impact assessment | 100% | Quarterly |
| Training Completion | % of in-scope staff who completed AI awareness training | 90% | Annual |
| Audit Programme Progress | % of planned audits completed on schedule | 100% | Annual |
| Open Risk Treatments | Number of overdue risk treatment actions | 0 | Monthly |
| AI Incidents | Number of AI-related incidents per quarter | Target: decreasing trend | Quarterly |
| Supplier Assessments Current | % of Tier 1 AI suppliers with current assessment | 100% | Annual |
| Objectives Achievement | % of AI objectives on track | > 80% | Quarterly |

### Monitoring Process
1. Define metrics and targets (link to Clause 6.2 AI Objectives)
2. Assign monitoring owners for each metric
3. Collect data (automated dashboards, manual reports, audit results)
4. Analyse results — trends, anomalies, root causes
5. Evaluate against targets — is performance acceptable?
6. Report to management at defined intervals
7. Take corrective action when targets are not met (feeds into Clause 10)

### Documents Required
- AI Performance Monitoring Plan (what, how, when, who)
- AI Performance Dashboard / Report (actual measurement results)
- AIMS Metrics and KPIs Register

---

## 9.2 — Internal Audit

### What it requires
Conduct internal audits at planned intervals to determine whether the AIMS:
- Conforms to the organisation's own requirements for AIMS
- Conforms to ISO 42001 requirements
- Is effectively implemented and maintained

### Audit Programme
The audit programme must cover:
- The scope of each audit
- Frequency (typically annual for full AIMS; more frequent for high-risk areas)
- Methods (interviews, document review, process observation, system testing)
- Responsibilities (who conducts, who reviews, who receives report)
- Reporting requirements

### Annual AIMS Audit Plan Template

| Audit Area | Clauses | Month | Lead Auditor | Status |
|-----------|---------|-------|-------------|--------|
| Context and Scope | 4.1–4.4 | March | [Name] | Planned |
| Leadership and Policy | 5.1–5.3 | March | [Name] | Planned |
| Planning and Risk | 6.1–6.3 | April | [Name] | Planned |
| Support | 7.1–7.5 | April | [Name] | Planned |
| Operations | 8.1–8.4 | May | [Name] | Planned |
| AI Impact Assessments | 8.2 | May | [Name] | Planned |
| Supplier Management | 8.4 | June | [Name] | Planned |
| Performance Evaluation | 9.1–9.3 | June | [Name] | Planned |
| Continual Improvement | 10.1–10.2 | June | [Name] | Planned |

### Auditor Independence
Auditors must be independent of the areas they audit — they cannot audit their own work.

### Audit Process
1. Plan: Define scope, criteria, methods, schedule
2. Notify: Inform auditees in advance
3. Gather Evidence: Review documents, conduct interviews, observe processes
4. Evaluate: Compare evidence against requirements
5. Report: Issue findings — conformances, nonconformances, observations
6. Follow Up: Verify corrective actions are implemented

> Full procedure: see INTERNAL-AUDIT-PROCEDURE.md in this folder
> Detailed audit guide: see ISO42001-INTERNAL-AUDIT-GUIDE.md in this folder

### Documents Required
- Annual Audit Programme
- Individual Audit Plans (per audit)
- Audit Reports (findings, nonconformances, observations)
- Audit Evidence Records
- Corrective Action Tracking Log (links to Clause 10)

---

## 9.3 — Management Review

### What it requires
Top management must review the AIMS at planned intervals to ensure it remains suitable, adequate, and effective — and to drive continual improvement.

### Management Review Frequency
At minimum: annually. Best practice: quarterly or semi-annually for active AI programmes.

### Management Review Inputs (what you must bring to the meeting)

| Input | Source | Owner |
|-------|--------|-------|
| Status of actions from previous management reviews | Previous minutes | AI Gov Lead |
| Changes in external and internal issues relevant to the AIMS | Context analysis update | AI Gov Lead |
| AI performance and trend information | Monitoring dashboard | Risk Manager |
| Audit results (internal and external) | Audit reports | Internal Auditor |
| Nonconformities and corrective actions | NCR log | AI Gov Lead |
| Monitoring and measurement results | KPI report | AI Gov Lead |
| Interested party feedback | Stakeholder feedback log | AI Gov Lead |
| Risk treatment effectiveness | Risk register | Risk Manager |
| Opportunities for continual improvement | Improvement log | AI Gov Lead |
| AI Objectives achievement | Objectives tracker | AI Gov Lead |

### Management Review Outputs (what must come out)
- Decisions and actions on opportunities for continual improvement
- Any needed changes to the AIMS (policy, objectives, controls)
- Resource needs

### Management Review Agenda Template

    AIMS MANAGEMENT REVIEW AGENDA
    Date: [Date] | Attendees: [Names and Roles] | Chair: [AI Governance Lead / CEO]

    1. Review of actions from last meeting (10 min)
    2. AIMS performance dashboard review (15 min)
    3. AI incidents review and trend analysis (10 min)
    4. Internal audit results and open findings (10 min)
    5. Risk register review — new/changed risks, overdue treatments (15 min)
    6. AI objectives achievement (10 min)
    7. Stakeholder feedback and interested party requirements changes (5 min)
    8. Regulatory and standards updates (5 min)
    9. Continual improvement opportunities (10 min)
    10. Resource needs and decisions (5 min)
    11. Actions, owners, and deadlines (10 min)

> Full template: see MANAGEMENT-REVIEW-TEMPLATE.md in this folder

### Documents Required
- Management Review Meeting Minutes (with decisions and actions)
- Management Review Input Reports
- Action Register from Management Review

---

## Clause 9 — Documents Checklist

| # | Document | ISO Ref | Location | Status |
|---|----------|---------|----------|--------|
| 1 | AI Performance Monitoring Plan | 9.1 | This folder | To Do |
| 2 | AI Performance Dashboard / Report | 9.1 | This folder | To Do |
| 3 | Annual Audit Programme | 9.2 | This folder | To Do |
| 4 | Individual Audit Plans | 9.2 | This folder | Per audit |
| 5 | Audit Reports | 9.2 | This folder | Per audit |
| 6 | Internal Audit Procedure | 9.2 | INTERNAL-AUDIT-PROCEDURE.md | Available |
| 7 | ISO 42001 Audit Guide | 9.2 | ISO42001-INTERNAL-AUDIT-GUIDE.md | Available |
| 8 | Management Review Minutes | 9.3 | This folder | Per review |
| 9 | Management Review Template | 9.3 | MANAGEMENT-REVIEW-TEMPLATE.md | Available |

---

## What Auditors Check in Clause 9
- Are there defined metrics with targets — not just data collection?
- Is monitoring actually happening — are there records of measurements?
- Is the audit programme documented and followed?
- Are auditors independent of the areas they audit?
- Are audit reports issued with findings and corrective actions?
- Are management reviews held at defined intervals — with records?
- Do management review records show real decisions and actions?
- Is there evidence that management review inputs were actually reviewed?

---

*ISO/IEC 42001:2023 AI Governance Toolkit — Clause 9 | See root README.md for full index*
