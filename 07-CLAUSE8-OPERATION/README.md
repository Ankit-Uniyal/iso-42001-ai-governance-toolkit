# Clause 8 — Operation
## ISO/IEC 42001:2023 | Implementation Guide

> **Purpose:** This is where AI governance becomes real. Clause 8 covers everything that happens when you actually build, deploy, operate, and retire AI systems — the operational controls that make your AIMS work in practice.

---

## Files in This Folder

| File | Contents |
|------|---------|
| README.md | This clause guide |
| AI-SYSTEM-IMPACT-ASSESSMENT.md | Template for assessing impact of AI systems |
| AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md | End-to-end AI lifecycle management procedure |
| AI-SUPPLIER-ASSESSMENT.md | Third-party AI supplier due diligence template |

---

## 8.1 — Operational Planning and Control

### What it requires
Plan, implement, control, and maintain processes needed to meet requirements and implement actions from Clause 6 (Planning). This means turning your risk treatment plans and objectives into actual operational procedures.

### Key Operational Processes to Establish

| Process | Purpose | Key Output |
|---------|---------|-----------|
| AI System Design Review | Evaluate new AI systems before development | Design approval decision |
| AI Deployment Gate | Control what AI goes into production | Deployment sign-off checklist |
| AI Impact Assessment | Assess potential harms before deployment | Impact Assessment Report |
| Bias and Fairness Testing | Test AI outputs for discriminatory patterns | Bias test report |
| Model Documentation | Record what a model does and how | AI System Card / Model Card |
| AI Monitoring | Track AI performance in production | Monitoring dashboards, alerts |
| AI Change Control | Manage changes to live AI systems | Change request + approval |
| AI Decommissioning | Retire AI systems safely | Decommission checklist |

### Operational Control Principle
Every AI system must have documented controls covering its full lifecycle: from ideation through design, development, testing, deployment, monitoring, and decommissioning.

### Documents Required
- Operational Controls Register (what controls exist for each AI system and lifecycle stage)
- AI Deployment Checklist (pre-deployment gate criteria)
- AI Change Control Procedure
- AI Model Card / System Card Template

---

## 8.2 — AI System Impact Assessment

### What it requires
Before deploying or making significant changes to an AI system, assess its potential impacts on individuals, groups, and society — especially impacts that could be harmful, discriminatory, or infringe rights.

### What an AI Impact Assessment Covers

| Assessment Area | Questions to Answer |
|----------------|-------------------|
| Purpose and Use | What is the AI system designed to do? Who will use it? |
| Affected Persons | Who could be impacted by AI decisions or outputs? |
| Potential Harms | What could go wrong? What is the worst case? |
| Bias and Fairness | Could the system produce discriminatory outcomes? |
| Privacy | Does the system process personal data? What are the risks? |
| Transparency | Can decisions be explained to affected individuals? |
| Human Oversight | Are humans meaningfully in the loop for high-stakes decisions? |
| Legal Compliance | Does the system comply with relevant laws (GDPR, EU AI Act)? |
| Risk Level | Is this a high-risk, limited-risk, or minimal-risk AI system? |
| Residual Risks | What risks remain after mitigations? Are they acceptable? |
| Approval | Who has authority to approve deployment? |

### AI Impact Assessment Process
1. Trigger: Any new AI system or significant change to existing system
2. Assess: Complete the impact assessment template
3. Review: Review with AI Governance Lead, DPO, Legal, Risk Manager
4. Decide: Approve, approve with conditions, or reject
5. Document: Record decision with rationale
6. Reassess: Reassess when system changes significantly or incidents occur

> Full template: see AI-SYSTEM-IMPACT-ASSESSMENT.md in this folder

---

## 8.3 — AI System Lifecycle Management

### What it requires
Establish controls across the full AI system lifecycle, from concept through retirement.

### AI System Lifecycle Stages

**Stage 1: Concept and Design**
- Define system purpose, intended use, and user base
- Assess risk level (high/limited/minimal risk)
- Conduct preliminary impact assessment
- Define data requirements and data governance
- Design for explainability and human oversight from the start

**Stage 2: Data Acquisition and Preparation**
- Identify data sources and assess data quality
- Check data for bias and representativeness
- Ensure legal basis for data use (consent, legitimate interest)
- Document data lineage
- Implement data governance controls

**Stage 3: Model Development and Training**
- Select algorithm with documented rationale
- Train model with version control
- Document model architecture, hyperparameters, training data
- Conduct initial bias testing
- Implement explainability mechanisms (SHAP, LIME, etc.)

**Stage 4: Testing and Validation**
- Performance testing (accuracy, precision, recall, etc.)
- Bias and fairness testing across protected characteristics
- Adversarial robustness testing
- User acceptance testing
- Security testing (model inversion, data poisoning)
- Complete full impact assessment
- Pre-deployment gate review and sign-off

**Stage 5: Deployment**
- Staged rollout (pilot, then full deployment)
- Human oversight mechanisms active
- Monitoring and alerting configured
- User documentation and disclosures in place
- Incident reporting channel established

**Stage 6: Monitoring and Maintenance**
- Monitor performance metrics continuously
- Monitor for model drift (accuracy degradation over time)
- Monitor for fairness drift
- Regular retraining schedule
- Incident detection and response
- Periodic reassessment (at least annually for high-risk systems)

**Stage 7: Decommissioning**
- Decision to decommission with documented rationale
- User notification
- Data disposal per retention schedule
- Model retirement and archiving
- Lessons learned documentation
- Remove from AI Systems Inventory

> Full procedure: see AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md in this folder

---

## 8.4 — AI System Supplier and Third-Party Management

### What it requires
When you use third-party AI systems, components, or data, you must assess and manage the associated risks. You cannot outsource your AI governance responsibilities.

### What to Assess for AI Suppliers

| Assessment Area | What to Check |
|----------------|-------------|
| AI System Transparency | Does the supplier document what their AI does and how it works? |
| Bias and Fairness | Has the supplier tested for bias? Are results available? |
| Data Practices | Where does training data come from? Is it ethically sourced? |
| Security | What security controls protect the AI system? |
| Regulatory Compliance | Does the supplier comply with relevant AI laws? |
| Incident Management | How does the supplier handle AI incidents? What is their SLA? |
| Contractual Protections | Do contracts cover AI liability, audit rights, and data handling? |
| Financial Stability | Is the supplier stable enough to be relied upon? |
| Ethical Standards | Does the supplier have an AI ethics policy? |

### Supplier Risk Tiers

| Tier | Description | Due Diligence Level |
|------|-------------|-------------------|
| Tier 1 — Critical | Core AI infrastructure, high-risk AI systems | Full assessment + annual review + contractual controls |
| Tier 2 — Important | Supporting AI tools, moderate-risk systems | Standard assessment + biennial review |
| Tier 3 — Standard | Low-risk AI tools, SaaS with minimal AI | Questionnaire only + periodic review |

> Full template: see AI-SUPPLIER-ASSESSMENT.md in this folder

---

## Clause 8 — Documents Checklist

| # | Document | ISO Ref | Location | Status |
|---|----------|---------|----------|--------|
| 1 | Operational Controls Register | 8.1 | This folder | To Do |
| 2 | AI Deployment Checklist | 8.1 | This folder | To Do |
| 3 | AI Change Control Procedure | 8.1 | This folder | To Do |
| 4 | AI Model Card Template | 8.1 | This folder | To Do |
| 5 | AI System Impact Assessment Template | 8.2 | AI-SYSTEM-IMPACT-ASSESSMENT.md | Available |
| 6 | AI Lifecycle Management Procedure | 8.3 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md | Available |
| 7 | AI Supplier Assessment Template | 8.4 | AI-SUPPLIER-ASSESSMENT.md | Available |
| 8 | Supplier Risk Register | 8.4 | This folder | To Do |

---

## What Auditors Check in Clause 8
- Is there a formal pre-deployment gate — evidence that AI systems are reviewed before going live?
- Are impact assessments completed for all in-scope AI systems — and are they thorough?
- Is there a documented AI lifecycle process — not just in theory, but followed in practice?
- Are third-party AI suppliers assessed before onboarding?
- Is there a process for managing AI changes — not just for new systems?
- Is human oversight actually implemented for high-risk AI decisions?
- Are AI systems monitored in production — with alerts for performance and fairness drift?

---

*ISO/IEC 42001:2023 AI Governance Toolkit — Clause 8 | See root README.md for full index*
