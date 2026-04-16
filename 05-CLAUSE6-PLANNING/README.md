# Clause 6 — Planning
## ISO/IEC 42001:2023 | Implementation Guide

> **Purpose:** Translate your understanding of context, stakeholders, and leadership commitment into concrete plans — identifying risks and opportunities, setting AI objectives, and planning how to achieve them.

---

## Files in This Folder

| File | Contents |
|------|---------|
| README.md | This clause guide |
| STATEMENT-OF-APPLICABILITY.md | SOA — which Annex A controls apply and why |
| AI-RISK-REGISTER.md | Full AI risk register template and entries |

---

## 6.1 — Actions to Address Risks and Opportunities

### What it requires
You must identify the risks and opportunities that arise from your context (Clause 4) and plan actions to address them. For AI, this includes risks from AI systems themselves, risks to the AIMS, and opportunities to improve outcomes.

### 6.1.1 — General
Actions to address risks and opportunities must:
- Prevent or reduce undesired effects
- Achieve improvement
- Be proportionate to the potential impact on AI system users and affected parties

### 6.1.2 — AI Risk Assessment

You must establish, implement, and maintain a process to:
1. Identify AI risks (technical, ethical, legal, operational)
2. Analyse and evaluate each risk (likelihood x impact)
3. Determine which risks require treatment
4. Document the entire process

### AI Risk Categories to Cover

| Risk Category | Examples |
|--------------|---------|
| Accuracy / Performance | Model drift, incorrect predictions, low accuracy on edge cases |
| Bias and Fairness | Discriminatory outputs against protected groups |
| Privacy | Unauthorised use of personal data in training or inference |
| Security | Adversarial attacks, model inversion, data poisoning |
| Transparency | Inability to explain AI decisions to affected individuals |
| Accountability | No clear owner when something goes wrong |
| Legal / Regulatory | Non-compliance with EU AI Act, GDPR, sector rules |
| Operational | System failure, dependency on third-party AI vendors |
| Societal | Automation of harmful decisions, job displacement |
| Supplier / Third-party | AI vendor risk, data quality from external sources |

### Risk Assessment Template

| Risk ID | AI System | Risk Description | Category | Likelihood (1-5) | Impact (1-5) | Risk Score | Owner | Treatment |
|---------|-----------|-----------------|----------|-----------------|-------------|-----------|-------|-----------|
| AI-R01 | Credit Scoring Model | Model produces biased outcomes for minority groups | Bias | 3 | 5 | 15 | AI System Owner | Implement bias testing per release |
| AI-R02 | Customer Service Bot | Bot provides incorrect medical or legal advice | Accuracy | 4 | 4 | 16 | Product Manager | Add disclaimer, human escalation path |
| AI-R03 | HR Screening Tool | Candidate data used beyond consent | Privacy | 2 | 5 | 10 | DPO | Data minimisation, consent review |

Risk Score = Likelihood x Impact | Treat if score >= 10

### 6.1.3 — AI Risk Treatment

For each risk requiring treatment, document:
- Selected treatment option (avoid / reduce / transfer / accept)
- Specific controls to implement (link to Annex A controls)
- Residual risk after treatment
- Owner of treatment action
- Target completion date

### 6.1.4 — Statement of Applicability (SOA)

After completing risk treatment, produce a Statement of Applicability that:
- Lists all Annex A controls
- States whether each control is applicable or not
- Justifies inclusion or exclusion
- References how applicable controls are implemented

> The SOA template is maintained in this folder as: STATEMENT-OF-APPLICABILITY.md

### Documents Required
- AI Risk Assessment Process Document
- AI Risk Register (maintained in this folder as AI-RISK-REGISTER.md)
- Risk Treatment Plan
- Statement of Applicability (maintained in this folder as STATEMENT-OF-APPLICABILITY.md)

---

## 6.2 — AI Objectives and Planning to Achieve Them

### What it requires
You must establish AI objectives at relevant functions and levels, and plan how to achieve them.

### What makes a good AI objective?

AI objectives must be:
- Consistent with the AIMS policy
- Measurable (with defined metrics)
- Monitored and communicated
- Updated as appropriate
- Supported by a documented plan

### AI Objectives Framework

| Objective | Metric | Target | Frequency | Owner | Status |
|-----------|--------|--------|-----------|-------|--------|
| Ensure AI systems have bias testing before deployment | % of AI releases with documented bias test results | 100% | Per release | AI Gov Lead | Active |
| Maintain AI system inventory | % of AI systems with current documentation | 100% | Quarterly | AI Gov Lead | Active |
| Reduce AI-related incidents | Number of Severity 1/2 AI incidents per quarter | < 2 | Quarterly | Risk Manager | Active |
| Achieve staff AI awareness | % of in-scope staff completing AI ethics training | 90% | Annual | HR Lead | Active |
| Complete AIMS internal audit | Audit completed and reported | Yes/No | Annual | Internal Auditor | Planned |

### Planning to Achieve Objectives
For each objective, document:
1. What will be done
2. Resources required (people, budget, tools)
3. Who is responsible
4. When it will be completed
5. How results will be evaluated

### Documents Required
- AI Objectives Register (with metrics, targets, owners)
- AI Objectives Achievement Plan (actions, resources, timelines)

---

## 6.3 — Planning of Changes

### What it requires
When changes to the AIMS are needed, they must be carried out in a planned way.

### What triggers a change?
- New AI system being deployed
- Major update to an existing AI system (new model, new training data)
- New regulation or legal requirement
- Significant organisational change (merger, new product line)
- Audit finding requiring corrective action
- Management review outcome

### Change Management Process
1. Identify the change and its driver
2. Assess impact on AIMS (risks, controls, documentation, roles)
3. Plan the change (actions, resources, timelines)
4. Implement the change
5. Review effectiveness
6. Update relevant documentation

### Documents Required
- AIMS Change Log (record of all changes, dates, reasons, approvals)
- Change Impact Assessment Template

---

## Clause 6 — Documents Checklist

| # | Document | ISO Ref | Location | Status |
|---|----------|---------|----------|--------|
| 1 | AI Risk Assessment Process | 6.1.2 | This folder | To Do |
| 2 | AI Risk Register | 6.1.2 | AI-RISK-REGISTER.md (this folder) | In Progress |
| 3 | Risk Treatment Plan | 6.1.3 | This folder | To Do |
| 4 | Statement of Applicability (SOA) | 6.1.4 | STATEMENT-OF-APPLICABILITY.md (this folder) | In Progress |
| 5 | AI Objectives Register | 6.2 | This folder | To Do |
| 6 | AI Objectives Achievement Plan | 6.2 | This folder | To Do |
| 7 | AIMS Change Log | 6.3 | This folder | To Do |

---

## What Auditors Check in Clause 6
- Is there a documented risk assessment process — not just a risk register?
- Does the risk register cover AI-specific risks (bias, explainability, data quality)?
- Is the SOA complete — all Annex A controls addressed with justification?
- Are AI objectives SMART — specific, measurable, achievable, relevant, time-bound?
- Is there evidence objectives are monitored?
- Is change management documented — especially for new AI deployments?

---

*ISO/IEC 42001:2023 AI Governance Toolkit — Clause 6 | See root README.md for full index*
