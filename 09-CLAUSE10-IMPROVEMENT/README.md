# Clause 10 — Improvement
## ISO/IEC 42001:2023 | Implementation Guide

> **Purpose:** An AIMS is not a one-time project — it is a continuously improving system. Clause 10 ensures that when things go wrong (or could go better), the organisation takes structured action to fix problems, prevent recurrence, and systematically improve AI governance over time.

---

## Files in This Folder

| File | Contents |
|------|---------|
| README.md | This clause guide |
| AI-INCIDENT-RESPONSE-PROCEDURE.md | How to detect, respond to, and learn from AI incidents |
| NCR-REGISTER.md | Nonconformity and Corrective Action Register template |
| CONTINUAL-IMPROVEMENT-LOG.md | Continual Improvement Log template |

---

## 10.1 — Nonconformity and Corrective Action

### What it requires
When a nonconformity occurs (something does not meet requirements), the organisation must:
1. React to the nonconformity and take action to control and correct it
2. Evaluate the need for action to eliminate the cause
3. Implement any action needed
4. Review the effectiveness of the corrective action taken
5. Update risks and opportunities if necessary
6. Make changes to the AIMS if necessary

### What Counts as a Nonconformity?

| Type | Examples |
|------|---------|
| AIMS process failure | Impact assessment not completed before deployment |
| Policy breach | AI system deployed without required approvals |
| Legal / regulatory breach | AI system violates GDPR or EU AI Act requirement |
| Audit finding | Internal audit identifies missing documentation |
| AI system failure | Model produces discriminatory outputs in production |
| Supplier nonconformity | Third-party AI vendor fails contractual requirements |
| Incident | AI system causes harm to a user or affected person |
| Objective not met | AI governance KPI falls below acceptable threshold |

### Nonconformity and Corrective Action Process

**Step 1 — Detect and Record**
- Source: audit finding, incident report, monitoring alert, stakeholder complaint, management review
- Record the nonconformity: what happened, when, where, who identified it
- Assign a severity level (Critical / Major / Minor / Observation)

**Step 2 — Contain the Immediate Problem**
- Stop the harm or prevent it spreading
- Examples: suspend AI system, disable feature, halt data processing, notify affected users
- Document containment actions taken

**Step 3 — Root Cause Analysis**
- Determine why the nonconformity occurred — not just what happened
- Methods: 5 Whys, Fishbone (Ishikawa) diagram, fault tree analysis
- Example: Model bias detected. Why? Training data was not representative. Why? No data quality check in the development process. Why? The development process did not include this step. Root cause: gap in AI development procedure.

**Step 4 — Plan Corrective Action**
- Define specific actions to address the root cause
- Assign owner and deadline for each action
- Ensure actions are proportionate to the severity of the nonconformity

**Step 5 — Implement Corrective Action**
- Execute the planned actions
- Update documentation, procedures, training as needed
- Communicate changes to relevant staff

**Step 6 — Verify Effectiveness**
- After the correction is implemented, check it worked
- Re-test the AI system, re-audit the process, or monitor the metric
- Close the nonconformity only when the root cause is confirmed eliminated

**Step 7 — Update the AIMS**
- If the nonconformity reveals a systemic issue, update relevant AIMS elements
- Risk register, procedures, training, controls — whatever needs updating

### Nonconformity and Corrective Action Register Template

| NCR ID | Date | Source | Description | Severity | Root Cause | Corrective Action | Owner | Deadline | Status | Effectiveness Check |
|--------|------|--------|-------------|----------|-----------|------------------|-------|----------|--------|---------------------|
| NCR-001 | 2025-03-15 | Internal Audit | AI system deployed without completed impact assessment | Major | Development checklist not enforced | Update deployment gate to require IA sign-off; retrain developers | AI Gov Lead | 2025-04-15 | Open | Pending |
| NCR-002 | 2025-04-01 | Incident Report | Customer service bot gave incorrect medical information | Critical | No scope limitation controls on bot | Add content filtering; update bot terms of use | Product Manager | 2025-04-10 | Closed | Effective — no recurrence in 60 days |

### AI Incidents and Corrective Action
When an AI system causes harm or near-harm (an incident), the response must be both immediate (contain the harm) and systemic (prevent recurrence). This is why incidents feed directly into the corrective action process.

> Full incident response procedure: see AI-INCIDENT-RESPONSE-PROCEDURE.md in this folder

### Documents Required
- Nonconformity and Corrective Action Register (NCR log)
- Root Cause Analysis Records (per nonconformity)
- Corrective Action Plans
- Effectiveness Review Records

---

## 10.2 — Continual Improvement

### What it requires
The organisation must continually improve the suitability, adequacy, and effectiveness of the AIMS.

### The Difference Between Corrective Action and Continual Improvement

| Corrective Action (10.1) | Continual Improvement (10.2) |
|--------------------------|------------------------------|
| Reactive — triggered by a problem | Proactive — not necessarily triggered by a failure |
| Addresses a specific nonconformity | Addresses systemic or strategic improvement opportunities |
| Required when something goes wrong | Required even when things are going well |
| Example: Fix a process that failed | Example: Adopt better bias testing tools before they are required |

### Sources of Improvement Opportunities
- Management review outputs (Clause 9.3)
- Internal audit observations (Clause 9.2)
- AI performance trends (Clause 9.1)
- Stakeholder feedback
- New AI governance best practices or standards updates
- Industry incidents and lessons learned from peers
- Staff suggestions and innovation
- Emerging regulations (e.g., new EU AI Act requirements)
- Technology improvements (better explainability tools, fairness metrics)

### Continual Improvement Framework

Use a Plan-Do-Check-Act (PDCA) cycle applied to your AIMS:

**PLAN:** Identify improvement opportunity, set objectives, plan the change
**DO:** Implement the improvement
**CHECK:** Monitor and measure the results of the improvement
**ACT:** If effective, standardise it across the AIMS. If not, try again.

### Continual Improvement Log Template

| ID | Date Identified | Source | Description | Expected Benefit | Priority | Owner | Target Date | Status | Result |
|----|----------------|--------|-------------|-----------------|----------|-------|-------------|--------|--------|
| CI-001 | 2025-02-01 | Management Review | Implement automated model drift monitoring | Earlier detection of performance issues | High | MLOps Lead | 2025-Q2 | In Progress | TBD |
| CI-002 | 2025-03-01 | Audit Observation | Create AI ethics training e-learning module | Increase staff awareness efficiency | Medium | HR Lead | 2025-Q3 | Planned | TBD |
| CI-003 | 2025-04-01 | Industry Best Practice | Adopt NIST AI RMF playbook for risk assessment | Improve risk assessment quality | Low | Risk Manager | 2025-Q4 | Backlog | TBD |

### Improvement Review Cycle
1. Monthly: Review open improvement actions and progress
2. Quarterly: Identify new improvement opportunities from metrics and incidents
3. Annual: Comprehensive review at management review meeting (Clause 9.3)
4. As needed: React to external developments (new regulations, major incidents)

### Documents Required
- Continual Improvement Log
- Improvement Review Records (evidence improvements were evaluated)

---

## The Improvement Loop — How Clause 10 Connects Everything

Clause 10 is the engine that makes the entire AIMS self-correcting and self-improving:

- Clause 9 (Performance Evaluation) identifies what is working and what is not
- Clause 10.1 (Corrective Action) fixes what went wrong
- Clause 10.2 (Continual Improvement) makes things better proactively
- Improvements feed back into Clauses 4-9, updating context, policies, plans, controls, and measurements

This creates a genuine management system — not a static compliance checklist.

---

## Clause 10 — Documents Checklist

| # | Document | ISO Ref | Location | Status |
|---|----------|---------|----------|--------|
| 1 | Nonconformity and Corrective Action Register | 10.1 | This folder | To Do |
| 2 | Root Cause Analysis Records | 10.1 | This folder | Per NCR |
| 3 | Corrective Action Plans | 10.1 | This folder | Per NCR |
| 4 | Effectiveness Review Records | 10.1 | This folder | Per NCR |
| 5 | AI Incident Response Procedure | 10.1 | AI-INCIDENT-RESPONSE-PROCEDURE.md | Available |
| 6 | Continual Improvement Log | 10.2 | This folder | To Do |
| 7 | Improvement Review Records | 10.2 | This folder | To Do |

---

## What Auditors Check in Clause 10
- Is there a nonconformity register — and is it actually used?
- Are root cause analyses documented — not just corrective actions?
- Is there evidence that corrective actions were effective?
- Are AI incidents linked to the corrective action process?
- Is there a continual improvement log with proactive improvements (not just reactions to failures)?
- Do improvement actions trace back to management review or audit findings?
- Is there evidence the AIMS is actually getting better over time?

---

## Summary — The Complete ISO 42001 AIMS Document Set

| Clause | Folder | Key Documents |
|--------|--------|--------------|
| 4 — Context | 03-CLAUSE4-CONTEXT | Context Register, Interested Parties Register, Scope Statement, AI Systems Inventory |
| 5 — Leadership | 04-CLAUSE5-LEADERSHIP | AI Management Policy, Leadership Commitment, Roles and RACI Matrix |
| 6 — Planning | 05-CLAUSE6-PLANNING | Risk Register, SOA, AI Objectives, Risk Treatment Plan |
| 7 — Support | 06-CLAUSE7-SUPPORT | Resource Plan, Competence Matrix, Training Records, Master Document List |
| 8 — Operation | 07-CLAUSE8-OPERATION | Impact Assessments, Lifecycle Procedure, Supplier Assessments, Deployment Checklists |
| 9 — Performance | 08-CLAUSE9-PERFORMANCE | Monitoring Dashboard, Audit Programme, Audit Reports, Management Review Minutes |
| 10 — Improvement | 09-CLAUSE10-IMPROVEMENT | NCR Register, Root Cause Analyses, Improvement Log, Incident Response Procedure |

---

*ISO/IEC 42001:2023 AI Governance Toolkit — Clause 10 of 10 | See root README.md for full index*
