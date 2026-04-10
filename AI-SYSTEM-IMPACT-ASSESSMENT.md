# AI System Impact Assessment (ASIA) Template
## ISO/IEC 42001:2023 — Clause 8.4 & Annex A Controls A.5.2, A.5.3, A.5.4

---

**Document ID:** AIMS-TEMP-001
**Version:** 1.0
**Classification:** Internal — Controlled Document
**ASIA Reference Number:** ASIA-[YYYY]-[NNN]
**AI System Name:** ___________________________
**AI System Owner:** ___________________________
**Assessment Lead:** ___________________________
**Assessment Date:** ___________________________
**Next Review Date:** ___________________________

---

## PART 1: AI SYSTEM DESCRIPTION AND CONTEXT

### 1.1 AI System Overview

| Field | Details |
|-------|---------|
| AI System Name | |
| System Version | |
| Business Unit / Department | |
| Business Purpose | |
| AI Technology Type | (e.g., ML classifier, LLM, computer vision, recommendation engine, NLP) |
| Deployment Environment | (e.g., cloud SaaS, on-premise, hybrid, embedded in product) |
| AI Provider / Developer | (Internal development / Third-party vendor — specify) |
| Intended Users | (e.g., employees, customers, patients, citizens) |
| Estimated Users Affected | |
| Geographic Scope | |
| Planned Deployment Date | |

### 1.2 AI System Functional Description

Provide a clear description of what the AI system does, including inputs, processing, and outputs:

**Inputs:**
_Describe what data inputs the AI system receives (type, source, format)_

**Processing:**
_Describe how the AI system processes inputs (model type, algorithms used, training data overview)_

**Outputs:**
_Describe what the AI system produces (decisions, recommendations, classifications, predictions, content)_

**How outputs are used:**
_Describe how the outputs are used in practice — automated decisions, human-reviewed recommendations, information provision, etc._

### 1.3 AI System Classification

#### 1.3.1 EU AI Act Risk Classification

| Question | Response |
|----------|----------|
| Does the AI system fall into a prohibited use category? (Art. 5) | Yes / No |
| Is this a high-risk AI system? (Art. 6, Annex III) | Yes / No |
| If high-risk, which Annex III category? | |
| Is this a General-Purpose AI (GPAI) model? | Yes / No |
| Is this a limited-risk AI system (chatbot, deep fake)? | Yes / No |

**EU AI Act Conclusion:** [ ] Prohibited — CANNOT deploy | [ ] High-Risk | [ ] Limited-Risk | [ ] Minimal-Risk

#### 1.3.2 Organizational AI Risk Tier

| Tier | Description | Selected |
|------|-------------|----------|
| Tier 1 — Critical | AI makes or substantially automates consequential decisions affecting individual rights, safety, health, finances, or employment | |
| Tier 2 — High | AI significantly influences consequential decisions but human review occurs | |
| Tier 3 — Medium | AI provides recommendations or information in lower-stakes contexts | |
| Tier 4 — Low | AI used for internal optimization, analytics, or low-stakes automation | |

---

## PART 2: STAKEHOLDER AND AFFECTED PARTY ANALYSIS

### 2.1 Interested Parties Identification

| Stakeholder Group | Nature of Interest / Concern | Engagement Method |
|-------------------|-------------------------------|-------------------|
| Direct Users (internal) | | |
| End Users / Customers | | |
| Affected Individuals | | |
| Regulators | | |
| Data Subjects | | |
| Employees (job impact) | | |
| Suppliers / Partners | | |
| Broader Society | | |
| Vulnerable Groups | | |

### 2.2 Vulnerable Group Assessment

Assess whether the AI system may disproportionately affect any of the following groups:

| Vulnerable Group | Likelihood of Disproportionate Impact (H/M/L/N) | Specific Concern |
|-----------------|------------------------------------------------|-----------------|
| Children and minors | | |
| Elderly persons | | |
| Persons with disabilities | | |
| Persons in financial hardship | | |
| Ethnic or racial minorities | | |
| Religious minorities | | |
| Gender minorities / LGBTQ+ | | |
| Immigrants / asylum seekers | | |
| Persons with mental health conditions | | |
| Persons with low digital literacy | | |

---

## PART 3: IMPACT ASSESSMENT — BENEFITS

### 3.1 Expected Benefits

| Benefit Category | Description | Who Benefits? | Magnitude (H/M/L) |
|-----------------|-------------|--------------|-------------------|
| Efficiency / time savings | | | |
| Improved decision quality | | | |
| Cost reduction | | | |
| Improved customer experience | | | |
| Safety improvement | | | |
| Accessibility improvement | | | |
| Environmental benefit | | | |
| Innovation / competitive advantage | | | |
| Social benefit | | | |

### 3.2 Benefit Realization Assessment

**Net benefit assessment:** Are the expected benefits proportionate to the risks identified in Part 4?

[ ] Yes — Benefits clearly outweigh risks
[ ] Yes — Benefits outweigh risks with recommended controls in place
[ ] Uncertain — Further analysis required
[ ] No — Risks outweigh benefits; recommend not to proceed

---

## PART 4: IMPACT ASSESSMENT — RISKS AND HARMS

### 4.1 Fundamental Rights Impact Assessment

Assess the potential impact on each fundamental right:

| Fundamental Right | Impact Likelihood (H/M/L/N) | Severity (H/M/L) | Affected Groups | Mitigation Required |
|-------------------|-----------------------------|-----------------|-----------------|---------------------|
| Human dignity | | | | |
| Privacy and data protection | | | | |
| Non-discrimination / equality | | | | |
| Freedom of expression | | | | |
| Freedom of movement | | | | |
| Right to fair trial / due process | | | | |
| Right to work and employment | | | | |
| Right to education | | | | |
| Right to healthcare | | | | |
| Consumer protection rights | | | | |
| Right to effective remedy | | | | |

### 4.2 Bias and Fairness Impact Assessment

#### 4.2.1 Protected Characteristics Analysis

| Protected Characteristic | Potential for Disparate Impact? | Evidence / Concern | Treatment Plan |
|--------------------------|--------------------------------|-------------------|----------------|
| Race / Ethnicity | | | |
| Gender | | | |
| Age | | | |
| Disability | | | |
| Religion / Belief | | | |
| Sexual orientation | | | |
| Pregnancy / Maternity | | | |
| National origin | | | |
| Socioeconomic status | | | |

#### 4.2.2 Bias Assessment Summary

**Training data bias:** Was the training data assessed for representation and historical bias?
[ ] Yes — no significant bias identified | [ ] Yes — bias identified, mitigation applied | [ ] Not yet conducted | [ ] N/A

**Algorithmic bias:** Was the model tested for differential performance across demographic groups?
[ ] Yes — no significant difference | [ ] Yes — differences found, mitigation applied | [ ] Not yet conducted | [ ] N/A

**Outcome bias:** Are AI outputs monitored for discriminatory patterns in production?
[ ] Yes — monitoring in place | [ ] Planned | [ ] Not planned | [ ] N/A

### 4.3 Privacy Impact Assessment

| Privacy Risk | Present? | Severity | Treatment |
|-------------|----------|----------|-----------|
| Personal data processing without adequate legal basis | | | |
| Special category data processing (health, biometrics, etc.) | | | |
| AI model memorizing and reproducing personal data | | | |
| Re-identification risk from AI outputs | | | |
| Data subject rights not facilitated (access, erasure, objection) | | | |
| Cross-border transfer without adequate safeguards | | | |
| Profiling or automated decision-making affecting individuals | | | |
| Excessive data collection for AI training | | | |

**DPIA Required?** [ ] Yes — must be completed before deployment | [ ] No — justify: ___________

### 4.4 Safety and Security Impact Assessment

| Safety/Security Risk | Present? | Severity | Treatment |
|---------------------|----------|----------|-----------|
| Physical safety risk from AI errors | | | |
| AI failure causing harm to users or third parties | | | |
| Adversarial manipulation of AI outputs | | | |
| AI system used to cause harm (weapon, surveillance abuse) | | | |
| Cybersecurity risk (model theft, poisoning, injection) | | | |
| AI reliability failure in critical applications | | | |
| Inadequate human oversight of safety-critical decisions | | | |

### 4.5 Societal and Environmental Impact Assessment

| Impact Area | Description | Severity (H/M/L/N) |
|-------------|-------------|-------------------|
| Employment displacement / job impact | | |
| Environmental impact (compute energy use, carbon footprint) | | |
| Concentration of power / market distortion | | |
| Disinformation / manipulation risk | | |
| Erosion of human autonomy | | |
| Impact on social cohesion or trust | | |
| Democratic process impact | | |
| Digital divide exacerbation | | |

### 4.6 Transparency and Explainability Assessment

| Aspect | Requirement Met? | Gap / Action Required |
|--------|-----------------|----------------------|
| Users informed they are interacting with AI | | |
| AI capabilities and limitations documented and disclosed | | |
| Decisions can be explained to affected individuals | | |
| Decision logic is auditable by regulators | | |
| Meaningful human review of consequential decisions | | |
| Right to challenge/contest AI decisions provided | | |

---

## PART 5: HUMAN OVERSIGHT ASSESSMENT

### 5.1 Human Oversight Requirements

| Question | Response |
|----------|----------|
| What level of human oversight is required (full automation / human-in-loop / human-on-loop / human-in-command)? | |
| Are humans with appropriate competence overseeing AI outputs? | Yes / No / Partial |
| Can human operators understand and interpret AI outputs? | Yes / No / Partial |
| Can humans override or disable the AI system? | Yes / No |
| Is there a defined escalation path for AI anomalies? | Yes / No |
| Are oversight mechanisms documented and trained? | Yes / No |

### 5.2 Human Oversight Design

Describe the human oversight mechanism implemented:

_[Describe how human oversight is implemented in practice — who reviews AI outputs, how often, under what circumstances they override, and how this is documented]_

---

## PART 6: DATA GOVERNANCE ASSESSMENT

### 6.1 Training Data Assessment

| Data Governance Aspect | Status | Evidence | Gap / Action |
|------------------------|--------|----------|--------------|
| Training data sources documented | | | |
| Data quality assessed (completeness, accuracy, representativeness) | | | |
| Data provenance and lineage recorded | | | |
| Licensing and IP rights confirmed | | | |
| Personal data legal basis confirmed | | | |
| Bias evaluation conducted | | | |
| Data minimization applied | | | |
| Data retention policy applied | | | |

### 6.2 Operational Data Assessment

| Operational Data Aspect | Status | Gap / Action |
|------------------------|--------|--------------|
| Real-time data inputs protected in transit | | |
| Inference data retained only as required | | |
| User data not used for unauthorized re-training | | |
| Data subject requests can be fulfilled | | |

---

## PART 7: OVERALL IMPACT ASSESSMENT CONCLUSION

### 7.1 Impact Summary

| Impact Category | Overall Rating (Critical/High/Medium/Low/Negligible) | Key Concerns |
|-----------------|------------------------------------------------------|--------------|
| Fundamental Rights Impact | | |
| Bias and Fairness Impact | | |
| Privacy Impact | | |
| Safety and Security Impact | | |
| Societal Impact | | |
| Transparency Impact | | |

### 7.2 Overall Impact Rating

**Overall ASIA Rating:**
[ ] **Critical** — Fundamental risks that cannot be adequately mitigated. Do NOT deploy.
[ ] **High** — Significant risks. Deployment conditional on completion of mandatory controls.
[ ] **Medium** — Moderate risks. Deploy with standard controls and enhanced monitoring.
[ ] **Low** — Minor risks manageable with routine controls and monitoring.
[ ] **Negligible** — No significant impacts identified.

### 7.3 Deployment Recommendation

[ ] **Approve for deployment** — All required controls implemented, risks acceptable
[ ] **Conditional approval** — Deploy once listed conditions are met: ___________
[ ] **Defer deployment** — Significant gaps requiring remediation before deployment
[ ] **Do not deploy** — Risks or harms outweigh benefits; prohibited use identified

### 7.4 Conditions for Approval

| # | Condition / Required Action | Owner | Due Date | Priority |
|---|------------------------------|-------|----------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## PART 8: MONITORING AND REVIEW PLAN

### 8.1 Post-Deployment Monitoring Requirements

| Metric / Indicator | Monitoring Method | Frequency | Threshold for Alert | Owner |
|-------------------|------------------|-----------|---------------------|-------|
| Model accuracy / performance | | | | |
| Bias / fairness metrics by group | | | | |
| Incident rate | | | | |
| Human override rate | | | | |
| User complaint rate | | | | |
| Data quality metrics | | | | |

### 8.2 ASIA Review Triggers

This ASIA shall be reviewed and updated when:
- [ ] The AI system undergoes significant changes (algorithm, training data, deployment scope)
- [ ] New types of individuals or communities are affected
- [ ] Significant new regulatory requirements apply
- [ ] A significant incident occurs
- [ ] Annual review is due
- [ ] Other: ___________

---

## PART 9: APPROVALS AND SIGN-OFF

| Role | Name | Decision | Signature | Date |
|------|------|----------|-----------|------|
| AI System Owner | | Approve / Reject / Conditional | | |
| AI Governance Lead | | Approve / Reject / Conditional | | |
| Data Protection Officer | | Approve / Reject / Conditional | | |
| CISO (if security risk) | | Approve / Reject / Conditional | | |
| Legal Counsel (if required) | | Approve / Reject / Conditional | | |
| AI Governance Committee Chair | | Approve / Reject / Conditional | | |

---

## PART 10: DOCUMENT HISTORY

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | | | Initial assessment |
| | | | |

---

## Appendix A: AI Act High-Risk Categories Reference (Annex III)

The following categories of AI systems are classified as high-risk under Annex III of the EU AI Act:

1. **Biometric systems** — Remote biometric identification, biometric categorization, emotion recognition
2. **Critical infrastructure** — AI in management of critical infrastructure (water, gas, electricity, transport)
3. **Education and vocational training** — AI in access to education, exam assessment, monitoring students
4. **Employment and workers management** — CV screening, hiring decisions, work allocation, performance monitoring
5. **Essential private and public services** — Credit scoring, insurance risk assessment, social benefits eligibility
6. **Law enforcement** — Risk assessment of individuals, lie detection, crime prediction, evidence evaluation
7. **Migration, asylum and border control** — Risk assessment of persons, document authentication
8. **Justice and democratic processes** — AI in legal research, dispute resolution, electoral campaigns

---

## Appendix B: Assessment Methodology Notes

This assessment template is aligned with:
- ISO/IEC 42001:2023 Clause 8.4 (AI System Impact Assessment)
- ISO/IEC 42001:2023 Annex A controls A.5.2, A.5.3, A.5.4
- EU AI Act Article 27 (Fundamental Rights Impact Assessment)
- NIST AI RMF MAP function
- ISO/IEC 29134 (Privacy Impact Assessment guidelines)
- ICO AI and Data Protection Risk Toolkit

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*This template must be adapted to the specific context of each AI system and organization.*
