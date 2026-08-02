# AIMS Internal Audit Procedure and Checklist
## ISO/IEC 42001:2023 — Clause 9.2

---

**Document ID:** AIMS-PROC-006
**Version:** 1.0
**Owner:** Head of Internal Audit / AI Governance Lead
**Classification:** Internal — Controlled Document

---

## 1. Purpose and Scope

This procedure establishes the process for planning, conducting, and reporting ISO/IEC 42001:2023 AI Management System (AIMS) internal audits. Internal audits provide assurance that the AIMS conforms to organizational requirements and ISO 42001 requirements, and that it is effectively implemented and maintained.

---

## 2. Audit Program Planning

### 2.1 Annual Audit Program

The AIMS internal audit program shall cover all elements of ISO/IEC 42001:2023 over a defined cycle. The Head of Internal Audit / AI Governance Lead shall prepare an annual audit plan considering:

- Importance of processes to the AIMS
- Changes affecting the organization
- Results of previous audits
- AI risk assessment results
- Incident history
- Management review inputs

**Minimum audit frequency by area:**

| AIMS Area | Minimum Frequency | Risk-Based Frequency |
|-----------|------------------|---------------------|
| AI Policy and objectives (Cl. 4-6) | Annual | Annual |
| Leadership and governance (Cl. 5) | Annual | Annual |
| Risk assessment and treatment (Cl. 6) | Annual | 6-monthly (if high AI risk profile) |
| Operations and lifecycle (Cl. 8) | Annual | 6-monthly (active AI development) |
| Annex A controls | Annual (full cycle) | Targeted by risk |
| Third-party AI systems (A.10) | Annual | Per new significant deployment |
| Post-incident (triggered) | As needed | Within 30 days of P1/P2 incident |

### 2.2 Audit Plan Template

**Annual AIMS Internal Audit Plan — [Year]**

| Audit # | Audit Scope | AIMS Clauses / Controls | Planned Date | Auditor(s) | Auditee |
|---------|------------|------------------------|-------------|-----------|---------|
| AIMS-AUD-[Y]-001 | Context, Leadership, Planning | Cl. 4, 5, 6 | | | |
| AIMS-AUD-[Y]-002 | Support and Operations | Cl. 7, 8 | | | |
| AIMS-AUD-[Y]-003 | Performance and Improvement | Cl. 9, 10 | | | |
| AIMS-AUD-[Y]-004 | Annex A Domain A.2-A.5 | A.2, A.3, A.4, A.5 | | | |
| AIMS-AUD-[Y]-005 | Annex A Domain A.6-A.7 | A.6, A.7 | | | |
| AIMS-AUD-[Y]-006 | Annex A Domain A.8-A.10 | A.8, A.9, A.10 | | | |

---

## 3. Auditor Competence and Independence

### 3.1 Auditor Requirements

Internal auditors conducting AIMS audits shall:
- Have knowledge of ISO/IEC 42001:2023 requirements
- Have understanding of AI systems and AI governance concepts
- Have completed internal auditor training (ISO 42001 or equivalent)
- Be independent of the area being audited (no audit of own work)
- Maintain objectivity throughout the audit process

### 3.2 Lead Auditor vs. Audit Team Member

| Role | Requirements |
|------|-------------|
| Lead Auditor | ISO 42001 Lead Auditor qualified or equivalent; minimum 2 years governance audit experience |
| Audit Team Member | ISO 42001 awareness training; supervised by Lead Auditor |

---

## 4. Audit Process

### Phase 1: Audit Preparation

**4.1 Opening Meeting Agenda Template**

1. Introduction of audit team and auditees
2. Confirmation of audit scope, objectives, and criteria
3. Confirmation of audit schedule
4. Overview of audit methodology
5. Communication channels during audit
6. Confirmation of confidentiality requirements
7. Question and answer

**4.2 Document Review**
Before fieldwork, auditors shall review:
- [ ] AIMS Policy (AIMS-POL-001)
- [ ] Previous audit reports and corrective actions
- [ ] AI Risk Register (current version)
- [ ] Statement of Applicability (current version)
- [ ] AI System Impact Assessments for in-scope systems
- [ ] Management review minutes
- [ ] Incident register
- [ ] Training records
- [ ] Relevant operational procedures

### Phase 2: Fieldwork (Evidence Gathering)

**4.3 Evidence Collection Methods**

| Method | Description | When to Use |
|--------|-------------|------------|
| Interview | Discussions with staff responsible for AIMS processes | All audit areas |
| Document review | Examining policies, procedures, records, logs | All audit areas |
| Observation | Observing AI governance processes in practice | Operational areas |
| Technical testing | Testing monitoring systems, access controls | Clause 8, A.6, A.7 |
| Data sampling | Sampling AI system logs, incident records, training records | Performance areas |

**4.4 Audit Evidence Standards**
Evidence shall be:
- **Relevant** — Related to the audit criteria being assessed
- **Verifiable** — Capable of being confirmed by another auditor
- **Sufficient** — Enough to support audit findings
- **Reliable** — From trustworthy sources

### Phase 3: Reporting

**4.5 Finding Classification**

| Finding Type | Definition | Required Action |
|-------------|-----------|----------------|
| **Major Nonconformity** | Absence or total breakdown of a system element; or accumulation of minor nonconformities indicating systemic failure | Corrective action required; no certification/re-certification until closed |
| **Minor Nonconformity** | Single lapse in conformance against a requirement; isolated failure not indicating systemic breakdown | Corrective action required within defined timeframe |
| **Observation** | Situation not a nonconformity but that could lead to future noncompliance if not addressed | Improvement opportunity; no mandatory corrective action required |
| **Positive Finding** | Evidence of good practice, effective implementation, or innovative approach | Recognize and potentially share across organization |

---

## 5. AIMS Internal Audit Checklist

### PART A: CONTEXT OF THE ORGANIZATION (Clause 4)

**Audit Reference:** ___________
**Auditee:** ___________
**Date:** ___________
**Auditor:** ___________

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 4.1.1 | What process is used to identify external issues relevant to AI governance? | Evidence of environmental scanning; documented issues | C / NC / OBS | |
| 4.1.2 | Are internal issues relevant to AI governance identified and documented? | Internal context documentation | C / NC / OBS | |
| 4.1.3 | How are internal and external issues reviewed? When were they last reviewed? | Review records; revision history | C / NC / OBS | |
| 4.2.1 | How were interested parties identified? Who are they? | Interested party register | C / NC / OBS | |
| 4.2.2 | Are requirements of interested parties documented? | Requirements documentation | C / NC / OBS | |
| 4.2.3 | How are interested party requirements monitored for change? | Monitoring process; evidence of reviews | C / NC / OBS | |
| 4.3.1 | What is the AIMS scope? Is it clearly defined and documented? | Scope document; AIMS scope statement | C / NC / OBS | |
| 4.3.2 | Does the scope statement consider all required factors? | Scope document; evidence of consideration | C / NC / OBS | |
| 4.4.1 | Is the AIMS established, implemented, maintained, and continually improved? | AIMS documentation; process evidence | C / NC / OBS | |
| 4.4.2 | Are AIMS processes defined and their interactions understood? | Process maps; procedure documents | C / NC / OBS | |

### PART B: LEADERSHIP (Clause 5)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 5.1.1 | How does top management demonstrate commitment to the AIMS? | Management review minutes; resource allocation records; communication evidence | C / NC / OBS | |
| 5.1.2 | Is the AI Policy established and communicated? | AI Policy document; communication evidence | C / NC / OBS | |
| 5.1.3 | Are AIMS objectives aligned with strategic direction? | Strategic plan; objectives documentation | C / NC / OBS | |
| 5.1.4 | Are adequate resources allocated to the AIMS? | Resource allocation records; budget evidence | C / NC / OBS | |
| 5.2.1 | Is there a documented AI Policy? | AIMS-POL-001; approval evidence | C / NC / OBS | |
| 5.2.2 | Does the policy include commitment to responsible AI? | Policy content review | C / NC / OBS | |
| 5.2.3 | Does the policy include commitment to legal compliance? | Policy content review | C / NC / OBS | |
| 5.2.4 | How is the policy communicated internally and externally? | Communication records; awareness evidence | C / NC / OBS | |
| 5.3.1 | Are roles and responsibilities for AI governance assigned? | RACI matrix; job descriptions; org chart | C / NC / OBS | |

### PART C: PLANNING (Clause 6)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 6.1.1 | How are AI risks and opportunities identified? | Risk assessment process document | C / NC / OBS | |
| 6.1.2 | Is there a documented AI risk assessment process? | AIMS-PROC-001 or equivalent | C / NC / OBS | |
| 6.1.3 | Do risk assessments cover all relevant AI risk categories? | Risk register; assessment methodology | C / NC / OBS | |
| 6.1.4 | Are risk criteria (likelihood and consequence) defined? | Risk methodology; risk matrix | C / NC / OBS | |
| 6.1.5 | Are risk assessment results documented and retained? | Risk register; assessment records | C / NC / OBS | |
| 6.1.6 | Is there a documented risk treatment process? | Risk treatment procedure | C / NC / OBS | |
| 6.1.7 | Are risk treatment options selected and implemented? | Risk treatment plans; evidence of implementation | C / NC / OBS | |
| 6.1.8 | Is a Statement of Applicability produced and maintained? | AIMS-SOA-001; version history | C / NC / OBS | |
| 6.1.9 | Are risk treatment plans documented and approved? | Treatment plans; approval records | C / NC / OBS | |
| 6.2.1 | Are AI objectives established at relevant levels? | Objectives documentation | C / NC / OBS | |
| 6.2.2 | Are AI objectives measurable and consistent with policy? | Objectives with KPIs; policy alignment | C / NC / OBS | |
| 6.2.3 | Are plans for achieving objectives documented? | Action plans; responsibility assignments | C / NC / OBS | |

### PART D: SUPPORT (Clause 7)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 7.1.1 | Are AIMS resources identified and provided? | Resource plan; budget; staffing | C / NC / OBS | |
| 7.2.1 | Are AI governance competency requirements defined? | Competency framework; job descriptions | C / NC / OBS | |
| 7.2.2 | Do staff have required AI governance competencies? | CVs; certificates; training records | C / NC / OBS | |
| 7.2.3 | Are competency gaps identified and addressed? | Training plans; gap analysis | C / NC / OBS | |
| 7.2.4 | Is evidence of competence documented? | Training records; certificates | C / NC / OBS | |
| 7.3.1 | Are staff aware of the AI Policy? | Awareness records; training evidence | C / NC / OBS | |
| 7.3.2 | Are staff aware of their contribution to AIMS? | Training records; induction materials | C / NC / OBS | |
| 7.4.1 | Is there a defined internal AI governance communication process? | Communication procedure; evidence of communications | C / NC / OBS | |
| 7.4.2 | Is there a defined external AI governance communication process? | External communication procedure; transparency reports | C / NC / OBS | |
| 7.5.1 | Does the AIMS include all required documented information? | Document list vs. standard requirements | C / NC / OBS | |
| 7.5.2 | Are AIMS documents controlled? | Document control procedure; version records; approval evidence | C / NC / OBS | |

### PART E: OPERATION (Clause 8)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 8.1.1 | Are AI governance processes planned, implemented, and controlled? | Process documentation; evidence of implementation | C / NC / OBS | |
| 8.2.1 | Are AI risk assessments performed at planned intervals? | Risk assessment schedule; assessment records | C / NC / OBS | |
| 8.2.2 | Are risk assessment results documented? | Risk assessment reports | C / NC / OBS | |
| 8.3.1 | Are risk treatment plans implemented? | Treatment plans; implementation evidence | C / NC / OBS | |
| 8.4.1 | Is there a process for AI System Impact Assessments? | ASIA procedure; ASIA register | C / NC / OBS | |
| 8.4.2 | Do ASIAs consider societal impacts, fairness, privacy, human rights? | ASIA template; completed ASIAs | C / NC / OBS | |
| 8.4.3 | Are ASIA results used to inform risk treatment? | Evidence of ASIA → risk treatment linkage | C / NC / OBS | |
| 8.1.2 | Is there a defined AI system lifecycle process? | Lifecycle procedure | C / NC / OBS | |
| 8.1.3 | Are data governance controls in place for AI training data? | Data governance documentation; controls evidence | C / NC / OBS | |
| 8.1.4 | Are AI development processes documented and controlled? | Development procedure; version control evidence | C / NC / OBS | |
| 8.1.5 | Are AI systems tested and validated before deployment? | Test results; validation records | C / NC / OBS | |
| 8.1.6 | Are deployment processes controlled with human oversight? | Deployment checklist; oversight documentation | C / NC / OBS | |
| 8.1.7 | Are deployed AI systems monitored? | Monitoring system; alert configuration; monitoring reports | C / NC / OBS | |
| 8.1.8 | Is there a decommissioning process? | Decommissioning procedure; any completed records | C / NC / OBS | |

### PART F: PERFORMANCE EVALUATION (Clause 9)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 9.1.1 | Are AI governance metrics defined? | KPIs/metrics documentation | C / NC / OBS | |
| 9.1.2 | Are metrics monitored at defined intervals? | Monitoring records; reports | C / NC / OBS | |
| 9.1.3 | Are analysis results used for decision making? | Management reports; action records | C / NC / OBS | |
| 9.2.1 | Is there a documented internal audit program? | Audit program; annual audit plan | C / NC / OBS | |
| 9.2.2 | Are internal audits conducted at planned intervals? | Audit schedule; completed audit reports | C / NC / OBS | |
| 9.2.3 | Are audit findings reported to management? | Audit reports; management communications; corrective actions | C / NC / OBS | |
| 9.3.1 | Does top management review the AIMS at planned intervals? | Management review schedule; meeting invitations | C / NC / OBS | |
| 9.3.2 | Do management reviews include required inputs? | Management review minutes; agenda | C / NC / OBS | |
| 9.3.3 | Are management review outputs documented? | Management review records; action items | C / NC / OBS | |

### PART G: IMPROVEMENT (Clause 10)

| # | Audit Question | Evidence Requested | Finding | Notes |
|---|---------------|-------------------|---------|-------|
| 10.1.1 | Is continual improvement evident? | Improvement plans; trend data; improvements implemented | C / NC / OBS | |
| 10.2.1 | Are nonconformities identified and reacted to? | NC log; immediate actions | C / NC / OBS | |
| 10.2.2 | Are root cause analyses conducted? | RCA records; methodology | C / NC / OBS | |
| 10.2.3 | Are corrective actions implemented and evaluated? | CA plans; effectiveness reviews | C / NC / OBS | |
| 10.2.4 | Are nonconformity records retained? | NC register; documentation | C / NC / OBS | |

### PART H: ANNEX A CONTROLS AUDIT

All 38 Annex A controls of ISO/IEC 42001:2023, across the nine domains A.2 to A.10.

**A.2 — Policies Related to AI**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.2.2 | Is the AI Policy documented, approved, communicated and available? Show current version, approval and distribution evidence. | Policy document; approval record; communication evidence | C / NC / OBS |
| A.2.3 | Is the AI Policy aligned with related policies (security, privacy, data, HR, procurement)? How were conflicts reconciled? | Policy set; cross-references; reconciliation record | C / NC / OBS |
| A.2.4 | Is the AI Policy reviewed at planned intervals and on significant change? Show the last review. | Review record; review triggers; version history | C / NC / OBS |

**A.3 — Internal Organization**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.3.2 | Are AI roles, responsibilities and authorities defined, assigned and communicated, including separation of conflicting duties? | RACI; job descriptions; org chart; access controls | C / NC / OBS |
| A.3.3 | Can staff and third parties raise concerns about AI systems through a defined, protected channel? | Reporting channel; awareness evidence; concerns log | C / NC / OBS |

**A.4 — Resources for AI Systems**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.4.2 | Are the resources needed across the AI life cycle identified and documented? | Resource plan; resource register per AI system | C / NC / OBS |
| A.4.3 | Are the data resources used by AI systems documented and managed? | Data inventory; dataset records; access controls | C / NC / OBS |
| A.4.4 | Are AI tooling resources (frameworks, libraries, pre-trained models) assessed and controlled before use? | Approved tools list; model registry; assessment records | C / NC / OBS |
| A.4.5 | Are system and computing resources for AI managed and secured? | Infrastructure inventory; security controls; DR plan | C / NC / OBS |
| A.4.6 | Do people involved in AI have the required competence, and how is it assessed? | Competency framework; training records; gap assessments | C / NC / OBS |

**A.5 — Assessing Impacts of AI Systems**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.5.2 | Is there a defined process for assessing AI system impacts, with clear triggers and approvals? | Impact assessment procedure; template; trigger criteria | C / NC / OBS |
| A.5.3 | Are impact assessment results documented, retained and available to those who need them? | Assessment register; completed assessments; retention evidence | C / NC / OBS |
| A.5.4 | Are impacts on individuals and identifiable groups assessed, and are the findings acted on? | Completed assessments; subgroup analysis; risk treatment records | C / NC / OBS |
| A.5.5 | Are wider societal and environmental impacts assessed? | Societal impact sections; ethics review; stakeholder engagement | C / NC / OBS |

**A.6 — AI System Life Cycle**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.6.1.2 | Are objectives for responsible development of AI systems documented and communicated? | Responsible AI objectives; design briefs | C / NC / OBS |
| A.6.1.3 | Are there defined processes for responsible AI system design and development? | Development lifecycle procedure; governance gates; evidence of use | C / NC / OBS |
| A.6.2.2 | Are AI system requirements and specifications documented, including intended purpose and acceptance criteria? | Requirements specification; acceptance criteria | C / NC / OBS |
| A.6.2.3 | Is AI system design and development documented, including rationale and dependencies? | Architecture documentation; design decisions; version control | C / NC / OBS |
| A.6.2.4 | Are AI systems verified and validated before release, including bias, robustness and adversarial testing? | Test plans; bias evaluation; adversarial test results | C / NC / OBS |
| A.6.2.5 | Is AI system deployment controlled and authorised, with a tested rollback path? | Deployment procedure; authorisation records; rollback test | C / NC / OBS |
| A.6.2.6 | Are deployed AI systems operated and monitored, including drift detection and decommissioning? | Monitoring configuration; dashboards; drift reports; decommissioning records | C / NC / OBS |
| A.6.2.7 | Is technical documentation produced and maintained for each AI system? | Model cards; technical documentation; update history | C / NC / OBS |
| A.6.2.8 | Are event logs recorded, protected and retained for AI systems? | Logging design; retention settings; sample log extract | C / NC / OBS |

**A.7 — Data for AI Systems**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.7.2 | Are data requirements defined for developing and enhancing each AI system? | Data requirements; dataset catalogue; split documentation | C / NC / OBS |
| A.7.3 | Is data acquired lawfully and with appropriate authorisation? What legal bases are used? | Lawful basis records; licensing register; DPIAs; DPAs | C / NC / OBS |
| A.7.4 | Are data quality criteria defined and assessed for AI data? | Data quality framework; quality assessment records | C / NC / OBS |
| A.7.5 | Is data provenance and lineage documented and traceable? | Provenance records; lineage documentation; data catalogue | C / NC / OBS |
| A.7.6 | Is data preparation governed, including labelling and bias treatment? | Preparation procedures; labelling guidelines; bias mitigation evidence | C / NC / OBS |

**A.8 — Information for Interested Parties of AI Systems**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.8.2 | Is accurate documentation about capabilities, limitations and explanations provided to users? | User documentation; capability sheets; explanation mechanisms | C / NC / OBS |
| A.8.3 | Are external reporting obligations to authorities and other external parties identified and met? | Obligation register; regulatory watch list; reports made | C / NC / OBS |
| A.8.4 | Is there a process for communicating AI incidents to those who need to know, within defined timescales? | Incident communication procedure; templates; communications sent | C / NC / OBS |
| A.8.5 | Are interested parties informed where AI is involved in decisions affecting them? | Disclosure policy; UI evidence; customer communications | C / NC / OBS |

**A.9 — Use of AI Systems**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.9.2 | Are there processes for responsible use of AI, covering acceptable use, oversight and error handling? | Acceptable use policy; error handling procedure; enforcement evidence | C / NC / OBS |
| A.9.3 | Are objectives and limits for the responsible use of AI systems documented? | Responsible use objectives; reporting to management review | C / NC / OBS |
| A.9.4 | Are AI systems used only for their intended purpose, and is out-of-scope use prevented or detected? | Intended use statements; usage monitoring; override logs | C / NC / OBS |

**A.10 — Third-Party and Customer Relationships**

| Control | Audit Question | Evidence | Finding |
|---------|---------------|---------|---------|
| A.10.2 | Are responsibilities allocated across the AI value chain and recorded? | Third-party AI inventory; responsibility matrix; assessment records | C / NC / OBS |
| A.10.3 | Are AI suppliers assessed, contracted and monitored appropriately? | Supplier assessments; AI contract clauses; monitoring records | C / NC / OBS |
| A.10.4 | Are customer requirements and information needs for AI systems identified and met? | Customer requirements; customer-facing documentation; compliance evidence | C / NC / OBS |

---

## 6. Audit Report Template

**AIMS Internal Audit Report**

**Audit Reference:** ___________
**Audit Date(s):** ___________
**Audit Scope:** ___________
**Lead Auditor:** ___________
**Audit Team:** ___________
**Auditees:** ___________

### Executive Summary

_[2-3 paragraph summary of audit scope, overall conclusion, significant findings, and recommendations]_

### Overall Audit Conclusion

[ ] **Conforms** — The AIMS conforms to ISO/IEC 42001:2023 requirements and is effectively implemented
[ ] **Conforms with Minor Nonconformities** — The AIMS generally conforms with minor gaps identified
[ ] **Conforms with Major Nonconformities** — Significant gaps exist that require corrective action
[ ] **Does Not Conform** — Fundamental gaps exist in AIMS implementation

### Findings Summary

| Finding # | Classification | Clause/Control | Description | Root Cause | Required Action |
|-----------|---------------|---------------|-------------|-----------|----------------|
| | | | | | |

### Positive Findings / Good Practice

| # | Area | Good Practice Observed |
|---|------|----------------------|
| | | |

### Corrective Action Requirements

For each nonconformity, the auditee shall submit a corrective action plan within:
- Major NC: 14 days for plan, 90 days for implementation
- Minor NC: 30 days for plan, 120 days for implementation

### Auditor Declaration

_The audit was conducted in accordance with the AIMS Internal Audit Procedure (AIMS-PROC-006) and ISO 19011 guidance. The findings are based on evidence gathered during the audit and represent a sample of the activities reviewed. The audit team maintains independence from the areas audited._

**Lead Auditor Signature:** ___________
**Date:** ___________

---

## 7. Corrective Action Tracking

| CAR # | Linked Audit | Finding # | Classification | Description | Owner | Plan Due | Implementation Due | Status | Effectiveness Review Date |
|-------|-------------|---------|---------------|-------------|-------|---------|-------------------|--------|--------------------------|
| | | | | | | | | | |

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Aligned with ISO/IEC 42001:2023 Clause 9.2 and ISO 19011 Guidelines for Auditing Management Systems*
