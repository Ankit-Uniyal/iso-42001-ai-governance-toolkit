# AI Incident Response Procedure
## ISO/IEC 42001:2023 — Clause 10.2, Annex A Controls A.8.5, A.9.4, A.6.4.1

---

**Document ID:** AIMS-PROC-003
**Version:** 1.0
**Owner:** CISO / AI Governance Lead
**Classification:** Internal — Controlled Document

---

## 1. Purpose and Scope

### 1.1 Purpose
This procedure establishes a structured process for identifying, classifying, containing, investigating, and resolving AI system incidents. It ensures timely response to AI-related failures, harmful outputs, security breaches, bias incidents, and regulatory events affecting AI systems within the AIMS scope.

### 1.2 Scope
This procedure applies to all AI systems within the AIMS scope, including:
- AI systems developed internally
- Third-party AI APIs and services integrated into products or processes
- AI tools used by employees that cause or contribute to incidents

### 1.3 Definitions

| Term | Definition |
|------|-----------|
| **AI Incident** | Any unplanned event, failure, harmful output, or near-miss involving an AI system that causes or could cause harm to individuals, the organization, or society |
| **AI System Failure** | Technical malfunction causing the AI system to operate incorrectly or become unavailable |
| **Harmful Output** | AI-generated content or decision that causes or could cause harm (bias, discrimination, misinformation, safety hazard) |
| **AI Security Incident** | Adversarial attack, data breach, model compromise, or unauthorized access related to AI systems |
| **Near-Miss** | An event that could have caused harm but was identified and contained before harm occurred |
| **Serious Incident** | An AI incident resulting in significant harm, rights violation, safety risk, or requiring regulatory notification |

---

## 2. AI Incident Classification

### 2.1 Incident Category Types

| Category | Code | Description | Examples |
|----------|------|-------------|---------|
| Harmful Output | HO | AI produces content or decisions that cause harm | Biased decisions, discriminatory outputs, dangerous advice, hallucinations with harm |
| Bias/Fairness | BF | AI exhibits discriminatory or unfair behavior toward groups | Protected group disparate impact, demographic performance gap |
| Privacy Breach | PB | AI incident involving personal data exposure or privacy violation | Training data leakage, re-identification, unauthorized profiling |
| Security Attack | SA | Adversarial or malicious attack on AI system | Prompt injection, model poisoning, adversarial inputs, model theft |
| System Failure | SF | Technical failure causing AI system unavailability or incorrect operation | Performance degradation, model drift, infrastructure failure |
| Transparency | TR | AI used deceptively or without required disclosure | Undisclosed AI interaction, false capability claims |
| Regulatory | RE | AI incident creating regulatory exposure | EU AI Act violation, GDPR breach via AI, sector-specific violation |
| Third-Party AI | TP | Incident originating from third-party AI vendor or API | Vendor model change, third-party breach, supplier non-compliance |

### 2.2 Incident Severity Levels

| Severity | Description | Response SLA | Examples |
|----------|-------------|-------------|---------|
| **P1 — Critical** | Severe harm to individuals, fundamental rights violation, regulatory mandatory notification, significant safety risk | Immediate — within 1 hour | AI medical error causing patient harm, mass discriminatory decisions, EU AI Act serious incident, data breach via AI affecting >500 people |
| **P2 — High** | Significant harm, material bias impact, substantial privacy risk, major system failure | Within 4 hours | Systematic bias against protected group, GDPR breach requiring DPA notification, complete AI system outage, security breach of AI infrastructure |
| **P3 — Medium** | Moderate harm, isolated bias events, limited privacy impact, partial system degradation | Within 24 hours | Individual harmful output, isolated unfair decision, model drift detected, prompt injection attempt contained |
| **P4 — Low** | Minor issue, near-miss, performance degradation below alert threshold, potential concern | Within 72 hours | Minor performance drop, user complaint about output quality, potential bias indicator, suspicious activity detected |

---

## 3. Incident Response Team

### 3.1 AI Incident Response Team Structure

| Role | Primary Responsibility | Escalation Contact |
|------|----------------------|-------------------|
| **AI Incident Commander** | Overall incident ownership and coordination | AI Governance Lead / CAIO |
| **AI Technical Lead** | Technical investigation, containment, remediation | AI Engineering Manager |
| **Data Protection Officer** | Privacy impact assessment, regulatory notification | DPO |
| **CISO / Security Lead** | Security incidents, forensics, vulnerability assessment | CISO |
| **Legal Counsel** | Legal exposure assessment, regulatory communication | General Counsel |
| **Communications Lead** | Internal and external communications | PR / Communications Director |
| **AI System Owner** | System-specific knowledge, business impact assessment | Business Unit Head |

### 3.2 RACI Matrix

| Activity | AI Incident Commander | Technical Lead | DPO | CISO | Legal | Communications |
|----------|----------------------|----------------|-----|------|-------|----------------|
| Incident detection and logging | C | A | I | I | I | I |
| Initial classification | A | R | C | C | I | I |
| Containment | A | R | I | C | I | I |
| Investigation | A | R | C | C | I | I |
| Regulatory notification | A | I | R | I | C | I |
| Communication (internal) | A | I | I | I | C | R |
| Communication (external) | A | I | C | I | C | R |
| Remediation | A | R | C | C | I | I |
| Post-incident review | A | R | R | C | C | I |
| Lessons learned | A | R | R | R | C | I |

---

## 4. Incident Response Lifecycle

### Phase 1: DETECTION AND REPORTING

#### 4.1 Detection Sources

AI incidents may be detected through:
- **Automated monitoring** — Performance drift alerts, anomaly detection, bias metric thresholds
- **User reports** — End users reporting harmful, unfair, or incorrect AI outputs
- **Employee reports** — Internal staff identifying AI system issues
- **Human oversight reviews** — Human reviewers identifying AI error patterns
- **Audit findings** — Internal or external audit identifying non-conformances
- **Third-party notification** — Vendor notification of AI system compromise or change
- **Regulatory notification** — Regulator flagging potential non-compliance
- **Media / public reports** — Public attention to AI system harm

#### 4.2 Incident Reporting

**All AI incidents must be reported** by any employee who identifies them.

**Reporting channels:**
- Primary: [AI Incident Reporting Portal / URL]
- Secondary: [Email: ai-incident@organization.com]
- Emergency (P1): [Phone: CISO hotline]

**Information required for initial report:**
1. Date and time of detection
2. AI system name and version
3. Description of the incident
4. Affected individuals / groups (estimate)
5. Any immediate harm observed
6. Reporter contact details

#### 4.3 Initial Incident Log Entry

**Incident ID:** AI-INC-[YYYY]-[NNN]
**Date/Time Reported:** ___________
**Reported By:** ___________
**AI System Affected:** ___________
**Incident Category:** (select from 2.1) ___________
**Initial Severity Assessment:** P1 / P2 / P3 / P4
**Incident Commander Assigned:** ___________
**Initial Description:** ___________

---

### Phase 2: TRIAGE AND CLASSIFICATION

#### 4.4 Triage Process (Target: Within 30 minutes of P1/P2 report, 4 hours for P3/P4)

The Incident Commander shall:

**Step 1 — Validate the incident**
- Confirm the incident is real and not a false positive
- Gather initial facts from reporter and system logs

**Step 2 — Classify severity**
Use the severity criteria in Section 2.2. When in doubt, escalate to the higher severity level.

**Step 3 — Activate response team**
- P1: Activate full AI Incident Response Team immediately
- P2: Activate AI Incident Commander, Technical Lead, DPO, CISO
- P3: Activate AI Incident Commander and Technical Lead
- P4: Assign to AI System Owner for assessment

**Step 4 — Assess immediate harm**
- Is harm actively occurring? If yes, proceed immediately to containment.
- Has harm already occurred? Assess scope and affected individuals.
- Is there risk of harm spreading? Implement precautionary containment.

**Step 5 — Regulatory notification assessment**
Assess whether the incident triggers mandatory notification obligations:
- EU AI Act Article 73 (Serious incident to market surveillance authority)
- GDPR Article 33 (Personal data breach to supervisory authority — 72 hours)
- GDPR Article 34 (Notification to data subjects where high risk)
- Sector-specific obligations (healthcare, financial services, etc.)

**Step 6 — Initial communication**
Notify relevant stakeholders per the communication plan (Section 7).

---

### Phase 3: CONTAINMENT

#### 4.5 Containment Actions

**Immediate Containment (P1/P2) — Actions within first hour:**

| Containment Action | When Applicable | Responsible |
|-------------------|----------------|-------------|
| Disable or suspend the AI system | P1 incidents; when AI is causing active harm | Technical Lead |
| Switch to fallback/manual process | When AI system suspended | AI System Owner |
| Block malicious input source | Security incidents (prompt injection, poisoning) | CISO |
| Revoke compromised API keys or access | Security breach | CISO |
| Preserve evidence (logs, model state) | All incidents requiring investigation | Technical Lead |
| Notify affected users | Harmful output incidents | Communications Lead |
| Initiate data breach protocol | Privacy breach incidents | DPO |

**Containment Decision Matrix:**

| Scenario | Recommended Containment |
|----------|------------------------|
| AI producing discriminatory decisions at scale | Suspend AI, activate manual review of affected decisions |
| AI system security breach | Isolate system, revoke credentials, forensic preservation |
| AI hallucinations causing user harm | Disable feature, review all recent outputs, user notification |
| Model drift causing performance degradation | Rate-limit or suspend, rollback to previous model version |
| Prompt injection attack | Block attack vectors, log and analyze, security patch |
| Third-party AI vendor compromise | Suspend integration, activate alternative, notify vendor |

---

### Phase 4: INVESTIGATION

#### 4.6 Investigation Process

**Investigation objectives:**
1. Determine the root cause of the incident
2. Establish the full scope (how many affected, how long)
3. Identify whether this is a systemic issue or isolated event
4. Determine what data or systems were compromised/affected
5. Assess regulatory and legal exposure
6. Gather evidence for reporting and corrective action

**Investigation log template:**

| Investigation Item | Finding | Evidence | Owner |
|-------------------|---------|---------|-------|
| Root cause (technical) | | | |
| Root cause (process/governance) | | | |
| Timeline of events | | | |
| Affected individuals / scope | | | |
| Affected data (if privacy incident) | | | |
| Contributing factors | | | |
| Controls that failed | | | |
| Controls that worked | | | |

**Technical investigation checklist:**
- [ ] AI system logs reviewed for the incident period
- [ ] Model performance metrics analyzed
- [ ] Input data analyzed for anomalies
- [ ] Training data reviewed if model behavior anomaly
- [ ] API access logs reviewed
- [ ] Security event logs analyzed (if security incident)
- [ ] Third-party vendor logs/reports obtained (if relevant)
- [ ] Model card and documentation reviewed
- [ ] Bias metrics analyzed across demographic groups (if bias incident)

---

### Phase 5: NOTIFICATION AND COMMUNICATION

#### 4.7 Regulatory Notification Requirements

| Regulation | Trigger | Deadline | Recipient | Content Required |
|-----------|---------|---------|---------|-----------------|
| EU AI Act Art. 73 | Serious incident from high-risk AI causing death, serious health impact, rights violation, or major property damage | Without undue delay | National market surveillance authority | Description of incident, AI system details, corrective measures |
| GDPR Art. 33 | Personal data breach (unless no risk to individuals) | 72 hours | Supervisory Authority (e.g., DPA) | Nature of breach, categories/volume of data, DPO contact, consequences, measures |
| GDPR Art. 34 | High-risk breach (no mitigation) | Without undue delay | Affected data subjects | Clear description, DPO contact, likely consequences, remediation |
| Sector-specific | Varies by sector | Varies | Sector regulator | Varies |

**Notification Decision Log:**

| Regulation | Notification Required? | Rationale | Notification Date | Regulatory Reference # |
|-----------|----------------------|-----------|------------------|----------------------|
| EU AI Act Art. 73 | Yes / No | | | |
| GDPR Art. 33 | Yes / No | | | |
| GDPR Art. 34 | Yes / No | | | |
| Sector regulation | Yes / No | | | |

#### 4.8 Internal Communication Template

**Subject:** AI Incident Notification — [Severity] — [AI System Name] — [Incident ID]

**To:** [Senior Leadership / Affected Business Units / All Staff as appropriate]

---
**AI Incident Summary**

- **Incident ID:** [AI-INC-YYYY-NNN]
- **Date/Time:** [When detected]
- **AI System Affected:** [System name]
- **Severity:** [P1/P2/P3/P4]
- **Status:** [Active / Contained / Under Investigation / Resolved]
- **Summary:** [2-3 sentence description]
- **Affected Parties:** [Estimate of affected individuals/systems]
- **Current Actions:** [What is being done]
- **Next Update:** [When next update will be provided]

---

#### 4.9 External Communication Guidance

For incidents requiring customer/user notification:
- Communicate promptly and clearly — do not delay notification to protect reputation
- Use plain language — avoid technical jargon
- State clearly what happened, what data/decisions were affected
- Explain what steps have been taken to address the incident
- Provide contact information for individuals to ask questions
- Explain what individuals should do to protect themselves (if applicable)

---

### Phase 6: REMEDIATION AND RECOVERY

#### 4.10 Remediation Plan

| Remediation Item | Description | Owner | Target Date | Status |
|-----------------|-------------|-------|------------|--------|
| Root cause fix | Address the underlying technical cause | | | |
| Affected decision review | Review and potentially reverse AI-influenced decisions | | | |
| Model retraining / update | Update AI model if root cause is in model | | | |
| Control implementation | Implement new controls to prevent recurrence | | | |
| Testing and validation | Test fixes before redeployment | | | |
| System restoration | Restore AI system to service | | | |

#### 4.11 Return to Service Criteria

Before restoring a suspended AI system to service, the following criteria must be met:
- [ ] Root cause identified and confirmed
- [ ] Remediation implemented and tested
- [ ] Bias/fairness evaluation repeated and passed
- [ ] Security assessment completed (if security incident)
- [ ] Privacy impact re-assessed (if privacy incident)
- [ ] Regulatory notifications completed
- [ ] AI Governance Committee approval obtained
- [ ] Enhanced monitoring in place for 30 days post-restoration
- [ ] Communication to affected users completed

---

### Phase 7: POST-INCIDENT REVIEW

#### 4.12 Post-Incident Review Process

A post-incident review (PIR) shall be conducted:
- P1 incidents: Within 5 business days of resolution
- P2 incidents: Within 10 business days of resolution
- P3/P4 incidents: Within 30 days of resolution (may be done as batch)

**PIR Template:**

**Incident ID:** ___________
**PIR Date:** ___________
**PIR Facilitator:** ___________
**Attendees:** ___________

**1. Incident Summary**
What happened, when, who was affected, severity, duration?

**2. Timeline of Events**
(Chronological timeline from first indication to resolution)

**3. Root Cause Analysis**
(5-Why or fishbone analysis)
- **Why 1:** Why did the incident occur?
- **Why 2:** Why did [Why 1] happen?
- **Why 3:** Why did [Why 2] happen?
- **Why 4:** Why did [Why 3] happen?
- **Why 5:** Why did [Why 4] happen?
- **Root Cause:** ___________

**4. What Worked Well**
What controls, processes, and team actions worked effectively?

**5. What Needs Improvement**
What gaps in controls, monitoring, processes, or communication were identified?

**6. Lessons Learned**
Key insights to apply across all AI systems in the organization.

**7. Corrective Actions**

| Action | Owner | Target Date | Priority |
|--------|-------|------------|---------|
| | | | |

**8. AIMS Updates Required**
- Risk register updates: [ ] Yes / [ ] No
- Control updates: [ ] Yes / [ ] No
- Procedure updates: [ ] Yes / [ ] No
- Training updates: [ ] Yes / [ ] No
- Policy updates: [ ] Yes / [ ] No

---

## 5. Incident Register

All AI incidents shall be logged in the AI Incident Register:

| Incident ID | Date | AI System | Category | Severity | Status | Root Cause | Corrective Action | PIR Completed | Closed Date |
|-------------|------|-----------|----------|---------|--------|-----------|------------------|--------------|-------------|
| AI-INC-2024-001 | | | | | | | | | |
| | | | | | | | | | |

**Incident Register Review:** The incident register shall be reviewed:
- Monthly by the AI Governance Lead
- Quarterly as input to management review
- Annually for trend analysis and AIMS improvement

---

## 6. Metrics and KPIs

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| Mean Time to Detect (MTTD) | < 4 hours for P1/P2 | Monthly |
| Mean Time to Contain (MTTC) | < 2 hours for P1, < 8 hours for P2 | Monthly |
| Mean Time to Resolve (MTTR) | < 24 hours for P1, < 72 hours for P2 | Monthly |
| Regulatory notification timeliness | 100% within legal deadline | Per incident |
| Post-incident review completion rate | 100% for P1/P2, >90% for P3 | Quarterly |
| Repeat incidents (same root cause) | 0 | Quarterly |
| AI incident training completion | >95% of AIMS-scoped staff | Annual |

---

## 7. Related Documents

| Document | Reference |
|----------|-----------|
| AIMS Policy | AIMS-POL-001 |
| AI Risk Register | AIMS-RSKR-001 |
| AI System Impact Assessment Template | AIMS-TEMP-001 |
| Data Breach Response Procedure | [GDPR-PROC-001] |
| Business Continuity Plan | [BCP-001] |
| EU AI Act Compliance Checklist | AIMS-COMP-001 |

---

## Appendix: Incident Response Quick Reference Card

**P1 CRITICAL — IMMEDIATE ACTIONS (within 1 hour):**
1. Alert AI Incident Commander and CISO immediately
2. Assess if active harm is ongoing — if yes, SUSPEND AI SYSTEM
3. Preserve all evidence (logs, model state, inputs)
4. Notify DPO if personal data involved
5. Begin regulatory notification assessment
6. Notify senior leadership

**P2 HIGH — ACTIONS (within 4 hours):**
1. Alert AI Incident Commander and Technical Lead
2. Assess containment options
3. Begin investigation
4. Assess regulatory notification requirements
5. Prepare stakeholder communication

**Key regulatory deadlines:**
- GDPR data breach: **72 hours** to supervisory authority
- EU AI Act serious incident: **Without undue delay** (interpret as promptly as practicable)
- Sector-specific: Check applicable regulation

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Aligned with ISO/IEC 42001:2023, EU AI Act Art. 73, GDPR Art. 33/34*
