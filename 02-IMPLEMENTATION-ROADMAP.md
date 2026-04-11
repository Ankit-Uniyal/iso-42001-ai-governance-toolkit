# ISO/IEC 42001:2023 Implementation Roadmap
## Complete AIMS Implementation Guide — From Zero to Certification Ready

---

**Document ID:** AIMS-ROAD-001
**Version:** 1.0
**Owner:** AI Governance Lead / CAIO
**Classification:** Internal — Reference Document

---

## Overview

This roadmap provides a structured 12-month pathway to ISO/IEC 42001:2023 certification readiness. It is organized into four phases with clear milestones, deliverables, and resource estimates.

**Total estimated effort:** 6-12 months for initial implementation (depending on organization size and AI maturity)

---

## Pre-Implementation: Assessment and Mobilization (Weeks 1-4)

### Week 1-2: Initiation and Sponsorship

**Activities:**
- [ ] Secure executive sponsorship and top management commitment
- [ ] Define the AIMS business case and objectives
- [ ] Identify and appoint AI Governance Lead / CAIO
- [ ] Establish preliminary AIMS project team
- [ ] Define provisional AIMS scope

**Decisions Required from Top Management:**
1. Confirm organizational commitment to ISO 42001
2. Approve initial AIMS project budget
3. Designate the AI Governance Lead
4. Agree provisional AIMS scope

**Output:** Executive mandate and AI Governance team in place

---

### Week 3-4: Gap Assessment

**Activities:**
- [ ] Conduct ISO 42001 gap assessment using GAP-ASSESSMENT.md template
- [ ] Assess current AI governance maturity
- [ ] Identify all AI systems potentially in scope
- [ ] Review existing policies, procedures, and governance structures
- [ ] Assess current risk management practices
- [ ] Identify key stakeholders and their requirements

**Deliverables:**
- Completed gap assessment report (GAP-ASSESSMENT.md)
- AI systems inventory (preliminary)
- Maturity assessment score
- Gap remediation priority list

**Typical Gap Assessment Findings by Area:**

| AIMS Area | Common Gaps at Maturity Level 1-2 |
|-----------|----------------------------------|
| AI Policy | No dedicated AI policy; general IT policy only |
| Risk Assessment | No AI-specific risk assessment; generic IT risk only |
| Impact Assessment | ASIA process does not exist |
| Lifecycle | No documented AI development process; ad hoc |
| Data Governance | Data quality not assessed; provenance not documented |
| Monitoring | No AI-specific monitoring; general IT monitoring only |
| Incident Response | No AI incident procedure; reliance on IT incident process |
| Third-Party AI | No supplier AI assessment; vendor risk managed by procurement |
| Audit | No AI governance audit; general IT audit covers technology |

---

## PHASE 1: FOUNDATION (Months 1-3)

**Goal:** Establish the fundamental AIMS framework — governance, policy, and scope

### Month 1: AIMS Architecture

#### 1.1 AIMS Scope Definition (Clause 4.3)

**Activities:**
- [ ] Conduct formal stakeholder analysis (Clause 4.2)
- [ ] Define AIMS scope statement (which AI systems, products, services, processes)
- [ ] Document scope exclusions and justifications
- [ ] Confirm scope with top management and AI Governance Committee

**Key Questions for Scope Definition:**
- Which AI systems are we developing or procuring?
- Which AI systems have significant impact on individuals?
- Which AI systems carry highest regulatory risk?
- What is our capacity to govern — should we start narrow and expand?

**Scope Document Template:**
```
AIMS Scope Statement:
The AIMS of [Organization Name] covers the [design / development / deployment / 
operation] of AI systems used in [specify product lines / business units / services],
including [specify AI types: ML models / LLMs / computer vision / etc.] deployed 
in [specify channels: customer-facing / internal / third-party integrated].

Exclusions (with justification):
- [Excluded area]: [Justification why excluded]

AIMS Scope boundaries:
- Organizational: [Which business units / locations]
- Technical: [Which systems / platforms]
- Regulatory: [Which regulatory regimes are in scope]
```

#### 1.2 AI Governance Structure (Clause 5.3, A.3.2)

**Set up governance structures:**
- [ ] Establish AI Governance Committee (terms of reference)
- [ ] Define and document roles and responsibilities (RACI)
- [ ] Appoint AI System Owners for all in-scope AI systems
- [ ] Create AI governance organizational chart
- [ ] Define escalation paths

**Recommended Governance Structure (scaled by organization size):**

| Size | Recommended Structure |
|------|----------------------|
| Enterprise (>5,000 employees) | Board AI Committee → CAIO → AI Governance Committee → AI System Owners → AI Development Teams |
| Mid-size (500-5,000) | Executive Sponsor → AI Governance Lead → AI Governance Committee (cross-functional) → AI System Owners |
| SME (<500) | CEO/CTO as sponsor → AI Governance Lead (part-time) → AI System Owners |

#### 1.3 AI Policy (Clause 5.2, A.2.2, A.2.3)

- [ ] Draft AI Policy using AIMS-POLICY-TEMPLATE.md
- [ ] Conduct stakeholder review (legal, HR, technology, business units)
- [ ] Obtain top management approval
- [ ] Communicate to all relevant staff
- [ ] Publish to relevant external parties

---

### Month 2: Risk Management Foundation

#### 2.1 AI Risk Assessment Process (Clause 6.1, 8.2)

**Activities:**
- [ ] Define risk assessment methodology (criteria, likelihood scale, consequence scale)
- [ ] Document risk assessment procedure (AIMS-PROC-001)
- [ ] Define risk appetite and thresholds
- [ ] Conduct initial organizational-level AI risk assessment
- [ ] Populate AI Risk Register (AI-RISK-REGISTER.md)

**Risk Assessment Procedure Key Elements:**
```
AIMS-PROC-001: AI Risk Assessment Procedure

1. Scope: Which AI systems and activities are assessed?
2. Frequency: When are assessments conducted? (Initial / Annual / On-change / Incident-triggered)
3. Methodology: How are risks identified? (Brainstorming / STRIDE / FAIR / Structured interviews)
4. Criteria: How are likelihood and consequence scored? (Use AI-RISK-REGISTER.md methodology)
5. Approval: Who approves risk assessments? (AI Governance Lead / Committee)
6. Documentation: Where are results recorded? (AI Risk Register)
7. Treatment: How are risk treatment options selected and documented?
8. Review: How often are risks reviewed?
```

#### 2.2 Statement of Applicability (Clause 6.1.3)

- [ ] Review all 39 Annex A controls
- [ ] Determine applicability of each control
- [ ] Document justification for any exclusions
- [ ] Record current implementation status for applicable controls
- [ ] Get SoA approved by AI Governance Lead and top management

**This is a mandatory document — cannot be deferred.**

---

### Month 3: Core Procedures and Documentation

#### 3.1 Documented Information Framework (Clause 7.5)

**Create document management structure:**
- [ ] Document naming and reference convention
- [ ] Version control procedure
- [ ] Review and approval workflow
- [ ] Document storage and access control
- [ ] Retention schedule

**Mandatory Documented Information (ISO 42001):**

| Document | Reference | Status |
|----------|-----------|--------|
| AIMS scope statement | Clause 4.3 | |
| AI Policy | Clause 5.2 | |
| AI risk assessment results | Clause 6.1, 8.2 | |
| AI risk treatment plan | Clause 6.1, 8.3 | |
| Statement of Applicability | Clause 6.1.3 | |
| AI objectives | Clause 6.2 | |
| Evidence of competence | Clause 7.2 | |
| AI System Impact Assessments | Clause 8.4 | |
| AI system lifecycle records | Clause 8.5 | |
| Monitoring and measurement results | Clause 9.1 | |
| Internal audit program and results | Clause 9.2 | |
| Management review records | Clause 9.3 | |
| Nonconformity and corrective action records | Clause 10.2 | |

#### 3.2 Key Procedures (Priority Order)

**Month 3 Priority Procedures:**
1. AI Risk Assessment Procedure (Clause 6.1)
2. AI System Lifecycle Procedure (Clause 8.5) — use AIMS-PROC-002
3. AI System Impact Assessment procedure (Clause 8.4) — use AIMS-TEMP-001
4. AI Incident Response Procedure (Clause 10.2) — use AIMS-PROC-003

---

## PHASE 2: CONTROL IMPLEMENTATION (Months 4-7)

**Goal:** Implement all applicable Annex A controls and operational procedures

### Month 4-5: Lifecycle and Data Controls (A.6, A.7)

#### Annex A.6 Controls Implementation

**A.6.1 Design Controls:**
- [ ] Create responsible AI design requirements template
- [ ] Integrate into project initiation process
- [ ] Train AI architects and designers
- [ ] Implement design documentation standard

**A.6.2 Development Controls:**
- [ ] Implement AI development lifecycle procedure (AIMS-PROC-002)
- [ ] Set up model registry and versioning
- [ ] Implement experiment tracking (MLflow / Weights & Biases / etc.)
- [ ] Create model card template and library
- [ ] Implement bias evaluation tooling (Fairlearn / IBM AIF360 / Aequitas)
- [ ] Implement adversarial testing framework
- [ ] Set up staging/representative test environment

**A.6.3 Deployment Controls:**
- [ ] Create deployment checklist and governance gate process
- [ ] Implement change management for AI systems
- [ ] Set up rollback procedures
- [ ] Implement human oversight mechanisms

**A.6.4 Monitoring Controls:**
- [ ] Implement AI-specific monitoring (Evidently AI / Fiddler / Arize / custom)
- [ ] Define monitoring metrics and alert thresholds
- [ ] Set up drift detection
- [ ] Create monitoring dashboards

**A.6.5 Decommissioning Controls:**
- [ ] Create decommissioning checklist
- [ ] Integrate with data retention/deletion procedures

#### Annex A.7 Data Controls Implementation

**A.7.2 Data Quality:**
- [ ] Define data quality framework and criteria
- [ ] Implement data quality assessment process
- [ ] Create data quality scorecards

**A.7.3 Data Provenance:**
- [ ] Implement data lineage tracking (Great Expectations / dbt / Apache Atlas)
- [ ] Create data catalog
- [ ] Document provenance for all in-scope training datasets

**A.7.4 Privacy:**
- [ ] Conduct DPIAs for all AI systems processing personal data
- [ ] Implement privacy-by-design in AI development
- [ ] Review consent and legal bases for all training data

**A.7.5 Bias Mitigation:**
- [ ] Implement bias assessment in AI development workflow
- [ ] Define fairness thresholds by AI tier
- [ ] Document bias mitigation approaches

**A.7.6 Access Controls:**
- [ ] Implement access control matrix for AI training data and models
- [ ] Configure least-privilege access
- [ ] Enable audit logging for data and model access

---

### Month 5-6: Governance Controls (A.2 through A.5, A.8 through A.10)

#### A.2-A.5 Governance Controls

**A.3 Internal Organization:**
- [ ] Finalize RACI and role descriptions
- [ ] Implement segregation of duties in AI development
- [ ] Establish regulatory contact list and engagement schedule
- [ ] Integrate AI governance into project methodology

**A.4 Resources:**
- [ ] Conduct AI governance competency assessment
- [ ] Create training plan and complete priority training
- [ ] Assess AI infrastructure security
- [ ] Create approved AI tools list

**A.5 Impact Assessment:**
- [ ] Implement ASIA process using AIMS-TEMP-001
- [ ] Conduct ASIAs for all in-scope AI systems
- [ ] Integrate ASIA results with risk register

#### A.8-A.10 Operational Controls

**A.8 Information for Stakeholders:**
- [ ] Implement AI disclosure for all user-facing AI
- [ ] Implement explainability mechanisms (SHAP / LIME / custom explanations)
- [ ] Create user-facing AI capability documentation

**A.9 Use of AI:**
- [ ] Draft and publish Acceptable Use of AI Policy
- [ ] Implement human oversight procedures
- [ ] Test and document human override mechanisms

**A.10 Third-Party AI:**
- [ ] Assess all existing third-party AI using AIMS-TEMP-002
- [ ] Update supplier contracts to include AI governance clauses
- [ ] Establish ongoing third-party AI monitoring

---

### Month 7: Training, Awareness, and Communication

#### A.4.2 Training Implementation

**Training Curriculum by Role:**

| Role | Required Training | Recommended Hours |
|------|-----------------|-------------------|
| All staff | AI awareness, AI Policy, acceptable use | 2-3 hours |
| AI developers | Responsible AI, bias/fairness, model cards, security | 8-16 hours |
| AI system owners | AI risk assessment, ASIA, governance requirements | 4-8 hours |
| Managers | AI governance framework, oversight responsibilities | 4 hours |
| AIMS team | ISO 42001 Lead Implementer / Auditor course | 16-24 hours |
| Internal auditors | ISO 42001 internal auditor training | 16 hours |

**Training Resources:**
- ISO/IEC 42001:2023 standard (purchase from ISO)
- ISO 42001 Lead Implementer courses (PECB, BSI, Bureau Veritas)
- EU AI Act training (available from EU AI Office)
- Responsible AI training (Google, Microsoft, IBM — many free resources)
- Bias/fairness tooling training (Fairlearn, AIF360 documentation)

---

## PHASE 3: OPERATIONAL EFFECTIVENESS (Months 8-10)

**Goal:** Demonstrate that the AIMS is operating effectively and generating required records

### Month 8: Operational Running

**Activities:**
- [ ] All procedures operating for at least 3 months (for audit evidence)
- [ ] AI Risk Register being actively maintained and reviewed
- [ ] All in-scope AI systems have completed ASIA
- [ ] Model cards maintained for all AI models in scope
- [ ] Monitoring and alerting operating and generating records
- [ ] Human oversight operating and generating override records
- [ ] Third-party AI assessments current
- [ ] Training completions documented

### Month 9: Internal Audit

**Activities:**
- [ ] Conduct AIMS internal audit using INTERNAL-AUDIT-PROCEDURE.md
- [ ] Cover all clauses and applicable Annex A controls
- [ ] Document all findings (major NC, minor NC, observations)
- [ ] Issue audit report
- [ ] Initiate corrective actions for all nonconformities

**Pre-Audit Readiness Checklist:**
- [ ] All mandatory documented information complete and current
- [ ] Statement of Applicability complete and approved
- [ ] At least 3 months of operational records for key processes
- [ ] AI Risk Register current (reviewed within 3 months)
- [ ] All ASIAs complete for in-scope AI systems
- [ ] Training records current
- [ ] Previous nonconformities closed or in progress with credible plans

### Month 10: Corrective Actions and Remediation

- [ ] All Major NCs from internal audit addressed with root cause analysis
- [ ] Corrective action plans approved and in progress
- [ ] Evidence of effectiveness of corrective actions documented
- [ ] AIMS documentation updated where gaps identified

---

## PHASE 4: CERTIFICATION READINESS (Months 11-12)

**Goal:** Achieve certification readiness and pass Stage 1 / Stage 2 external audit

### Month 11: Management Review and Final Preparation

**Activities:**
- [ ] Conduct AIMS Management Review using MANAGEMENT-REVIEW-TEMPLATE.md
- [ ] Management Review outputs documented with decisions and actions
- [ ] All corrective actions from internal audit closed or on track
- [ ] SoA reviewed and updated to reflect current status
- [ ] AIMS documentation final review and approval
- [ ] Select and engage accredited certification body

**Selecting a Certification Body:**
- Ensure the CB is accredited for ISO 42001 by a national accreditation body
- Key CBs offering ISO 42001: BSI, Bureau Veritas, DNV, SGS, TÜV, LRQA
- Consider: geographic coverage, sector expertise, pricing, audit team AI expertise
- Request CV/profile of proposed lead auditor

### Month 12: External Audit Preparation and Stage 1

**Stage 1 Audit (Document Review):**
The certification body's Stage 1 audit reviews AIMS documentation to confirm readiness:

| Document | Certification Requirement | Our Reference |
|----------|--------------------------|---------------|
| AIMS scope | Mandatory | Clause 4.3 documentation |
| AI Policy | Mandatory | AIMS-POL-001 |
| Statement of Applicability | Mandatory | AIMS-SOA-001 |
| Risk assessment records | Mandatory | AI-RISK-REGISTER.md |
| Risk treatment plans | Mandatory | Risk register treatment columns |
| Management review records | Mandatory | MANAGEMENT-REVIEW-TEMPLATE.md |
| Internal audit records | Mandatory | INTERNAL-AUDIT-PROCEDURE.md |

**Stage 2 Audit (Effectiveness Audit):**
The Stage 2 audit assesses whether the AIMS is effectively implemented and operating:

Focus areas for Stage 2 auditors:
1. Is the AI Policy known and followed by staff?
2. Are AI risk assessments being conducted in practice?
3. Are ASIAs completed for all significant AI systems?
4. Are model cards maintained and accurate?
5. Is monitoring generating alerts that are acted upon?
6. Are human oversight mechanisms actually used?
7. Are incidents being identified, logged, and addressed?
8. Are corrective actions followed through?

---

## Document Checklist: Complete AIMS Documentation Set

### Tier 1 — Mandatory Documents (Required by Standard)

| # | Document | Clause | Template Available |
|---|----------|--------|-------------------|
| 1 | AIMS Scope Statement | 4.3 | In GAP-ASSESSMENT.md |
| 2 | AI Policy | 5.2 | AIMS-POLICY-TEMPLATE.md ✓ |
| 3 | Statement of Applicability | 6.1.3 | STATEMENT-OF-APPLICABILITY.md ✓ |
| 4 | AI Risk Assessment Records | 6.1, 8.2 | AI-RISK-REGISTER.md ✓ |
| 5 | AI Risk Treatment Plans | 6.1, 8.3 | In AI-RISK-REGISTER.md ✓ |
| 6 | AI Objectives and Plans | 6.2 | In MANAGEMENT-REVIEW-TEMPLATE.md ✓ |
| 7 | Competency Evidence | 7.2 | Training records |
| 8 | AI System Impact Assessments | 8.4 | AI-SYSTEM-IMPACT-ASSESSMENT.md ✓ |
| 9 | AI Lifecycle Records | 8.5 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md ✓ |
| 10 | Monitoring/Measurement Results | 9.1 | In MANAGEMENT-REVIEW-TEMPLATE.md ✓ |
| 11 | Internal Audit Program and Results | 9.2 | INTERNAL-AUDIT-PROCEDURE.md ✓ |
| 12 | Management Review Records | 9.3 | MANAGEMENT-REVIEW-TEMPLATE.md ✓ |
| 13 | Nonconformity and Corrective Action Records | 10.2 | In INTERNAL-AUDIT-PROCEDURE.md ✓ |

### Tier 2 — Strongly Recommended Documents

| # | Document | Purpose | Template Available |
|---|----------|---------|-------------------|
| 1 | AI Incident Response Procedure | Clause 10.2, A.8.5, A.9.4 | AI-INCIDENT-RESPONSE-PROCEDURE.md ✓ |
| 2 | AI Lifecycle Management Procedure | Clause 8.5, A.6 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md ✓ |
| 3 | AI Supplier Assessment | A.10.2, A.10.3 | AI-SUPPLIER-ASSESSMENT.md ✓ |
| 4 | Controls Mapping | Clause 6.1, Annex A | CONTROLS-MAPPING.md ✓ |
| 5 | Acceptable Use of AI Policy | A.9.2 | Build from AIMS-POLICY-TEMPLATE.md |
| 6 | Model Card Template | A.6.2.3 | In AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md ✓ |
| 7 | AI Data Governance Procedure | A.7 | Build from lifecycle procedure |
| 8 | Human Oversight Framework | A.9.3, A.6.3.3 | In lifecycle procedure |
| 9 | Bias Evaluation Methodology | A.6.2.6 | In lifecycle procedure ✓ |

---

## Resource Requirements Estimate

### Staffing

| Role | Estimated Effort (Implementation) | Ongoing (Annual) |
|------|----------------------------------|-----------------|
| AI Governance Lead | 100% for 6-12 months | 50% ongoing |
| AI Governance Analyst | 50% for 6-12 months | 25% ongoing |
| DPO (AI scope) | 25% for 6-12 months | 10% ongoing |
| CISO (AI scope) | 25% for 6-12 months | 10% ongoing |
| Internal Auditor (AI) | 20% for 6-12 months | 10% ongoing |
| AI Developer Time (controls) | 10% of dev team | 5% ongoing |

### Technology and Tools

| Tool Category | Purpose | Examples |
|--------------|---------|---------|
| Model Registry | Version control for AI models | MLflow, W&B, DVC |
| Bias/Fairness Testing | A.6.2.6 | Fairlearn, AIF360, Aequitas |
| Adversarial Testing | A.6.2.5 | Adversarial Robustness Toolbox, TextAttack |
| AI Monitoring | A.6.4.1, A.6.4.2 | Evidently AI, Fiddler, Arize AI, WhyLabs |
| Explainability | A.8.3 | SHAP, LIME, InterpretML |
| GRC Platform | AIMS documentation | ServiceNow, OneTrust, LogicGate, Archer |
| Data Lineage | A.7.3 | Apache Atlas, OpenMetadata, dbt |

### Budget Estimate

| Item | Small Org | Mid-Size | Enterprise |
|------|-----------|---------|-----------|
| Staff (internal governance) | £30-60k | £80-150k | £200-400k |
| Training and certification | £10-20k | £20-40k | £40-100k |
| External advisory (optional) | £20-50k | £50-100k | £100-200k |
| Technology tools | £5-20k | £20-80k | £80-200k |
| External certification audit | £5-15k | £10-25k | £20-50k |
| **Estimated Total** | **£70-165k** | **£180-395k** | **£440-950k** |

---

## Common Implementation Pitfalls to Avoid

| Pitfall | Prevention |
|---------|-----------|
| Scoping too broadly — trying to govern all AI at once | Start narrow; demonstrate success; expand scope |
| Treating ISO 42001 as paper compliance exercise | Focus on operational effectiveness; auditors test practice, not paperwork |
| Not securing genuine top management commitment | Document commitment in writing; ensure resource allocation follows |
| Underestimating data governance complexity | Start data governance early; it takes longest to implement |
| Not involving AI developers early | Governance must be embedded in development workflow, not bolted on |
| Ignoring third-party AI systems | Many organizations use more third-party AI than internal — don't exclude |
| Waiting for perfect processes before starting | Start implementing imperfect processes; improve through cycles |
| Not allocating sufficient internal audit resource | Internal audit is a mandatory requirement; resource it adequately |
| Disconnecting AIMS from ISMS/ISO 27001 | Integrate AI governance with information security governance |
| Overlooking regulatory timelines (EU AI Act) | Map regulatory deadlines to AIMS implementation milestones |

---

## Certification Timeline Summary

```
Month 1-3:   FOUNDATION
  ├── Week 1-2: Executive mandate, governance structure
  ├── Week 3-4: Gap assessment
  ├── Month 1:  Scope, policy, governance
  ├── Month 2:  Risk management, SoA
  └── Month 3:  Core procedures and documentation

Month 4-7:   CONTROL IMPLEMENTATION
  ├── Month 4-5: A.6 (Lifecycle), A.7 (Data)
  ├── Month 5-6: A.2-A.5, A.8-A.10 (Governance)
  └── Month 7:   Training and awareness

Month 8-10:  OPERATIONAL EFFECTIVENESS
  ├── Month 8:  Operational running (build evidence)
  ├── Month 9:  Internal audit
  └── Month 10: Corrective actions

Month 11-12: CERTIFICATION READINESS
  ├── Month 11: Management review, CB selection
  └── Month 12: Stage 1 external audit

Post Month 12: Stage 2 (Effectiveness) external audit → CERTIFICATION
```

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*This roadmap is for guidance purposes. Adapt to your organization's context, resources, and AI risk profile.*
