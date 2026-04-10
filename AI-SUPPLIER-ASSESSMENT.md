# AI Supplier / Third-Party AI Assessment Template
## ISO/IEC 42001:2023 — Annex A Controls A.10.2, A.10.3, A.10.4

---

**Document ID:** AIMS-TEMP-002
**Version:** 1.0
**Owner:** Procurement / AI Governance Lead
**Classification:** Internal — Controlled Document

**Assessment Reference:** TPAI-[YYYY]-[NNN]
**Supplier / Vendor Name:** ___________________________
**AI System / API / Service:** ___________________________
**Assessment Date:** ___________________________
**Assessor:** ___________________________
**Next Review Date:** ___________________________

---

## Purpose

This template supports the assessment of third-party AI systems, APIs, models, and services prior to adoption and at regular intervals thereafter. It implements Annex A control A.10.2 (Third-party AI risk assessment) and informs contract requirements under A.10.3.

---

## SECTION 1: SUPPLIER AND PRODUCT IDENTIFICATION

### 1.1 Supplier Profile

| Field | Details |
|-------|---------|
| Supplier Legal Name | |
| Supplier HQ Location | |
| Supplier Website | |
| Product / Service Name | |
| Product Version / API Version | |
| Type of AI (LLM, classifier, CV, recommendation, other) | |
| Intended Business Use | |
| Integration Method | (API / SDK / Embedded / SaaS / Other) |
| Estimated Volume of Use | |
| Business Criticality | (Critical / High / Medium / Low) |
| Does Personal Data Flow to Supplier? | Yes / No — describe: |
| Data Processing Location | |
| DPA / GDPR Article 28 Agreement in Place? | Yes / No |
| Existing Commercial Relationship? | Yes / No — since: |

### 1.2 Supplier's Role Classification (EU AI Act)

| Question | Response |
|----------|----------|
| Is the supplier a Provider of the AI system (places on market/service)? | Yes / No |
| Is the supplier a Deployer of the AI system on our behalf? | Yes / No |
| Is our organization acting as Deployer of supplier's AI system? | Yes / No |
| What is the AI system's EU AI Act risk classification? | Prohibited / High-Risk / Limited-Risk / Minimal-Risk / Unknown |
| Has the supplier provided an EU AI Act Declaration of Conformity (if required)? | Yes / No / N/A |

---

## SECTION 2: RESPONSIBLE AI AND GOVERNANCE ASSESSMENT

### 2.1 Supplier AI Governance Maturity

| Governance Area | Question | Score (1-5) | Evidence / Notes |
|----------------|----------|-------------|-----------------|
| AI Policy | Does the supplier have a published Responsible AI / Ethical AI policy? | | |
| AI Governance Structure | Does the supplier have a dedicated AI ethics/governance function? | | |
| Standards Compliance | Is the supplier ISO 42001 certified, or working toward it? | | |
| Bias and Fairness | Does the supplier conduct and publish bias evaluations? | | |
| Transparency | Does the supplier publish model cards or system cards? | | |
| Explainability | Does the supplier provide explainability mechanisms? | | |
| Incident Response | Does the supplier have an AI incident response process? | | |
| Human Oversight | Does the supplier support human oversight mechanisms? | | |
| Regulatory Compliance | Does the supplier demonstrate EU AI Act compliance (if applicable)? | | |

**Governance Score:** ___ / 45
**Governance Maturity Assessment:** [ ] Advanced (36-45) | [ ] Intermediate (27-35) | [ ] Basic (18-26) | [ ] Immature (<18)

### 2.2 Prohibited Use Check

| Check | Response |
|-------|----------|
| Does the AI system enable any EU AI Act prohibited practices? (social scoring, mass surveillance, subliminal manipulation) | Yes / No — if Yes: DO NOT PROCEED |
| Is the AI system on our organizational prohibited use list? | Yes / No — if Yes: DO NOT PROCEED |
| Does the AI system use biometric categorization based on sensitive attributes? | Yes / No — if Yes: Escalate for legal review |
| Does the AI system enable real-time remote biometric identification? | Yes / No — if Yes: Escalate for legal review |

---

## SECTION 3: TECHNICAL PERFORMANCE ASSESSMENT

### 3.1 Performance and Reliability

| Aspect | Question | Rating (H/M/L) | Evidence |
|--------|----------|----------------|---------|
| Accuracy | What are the supplier's documented accuracy/performance metrics? | | |
| Reliability | What is the supplier's documented system availability/uptime SLA? | | |
| Scalability | Can the system handle our expected volume and growth? | | |
| Latency | Does the system meet our performance requirements? | | |
| Model Updates | How are model updates communicated and managed? | | |
| Version Control | Can we pin to a specific model version? | | |
| Testing Evidence | Does the supplier provide independent testing results? | | |
| Monitoring | Does the supplier provide performance monitoring/reporting? | | |

### 3.2 Bias and Fairness Technical Assessment

| Fairness Aspect | Evidence Available? | Rating | Notes |
|----------------|--------------------|----|-------|
| Bias evaluation methodology documented | Yes / No / Partial | | |
| Bias testing across demographic groups conducted | Yes / No / Partial | | |
| Fairness metrics defined and published | Yes / No / Partial | | |
| Disparate impact testing results available | Yes / No / Partial | | |
| Bias mitigation techniques documented | Yes / No / Partial | | |
| Ongoing bias monitoring in production | Yes / No / Partial | | |

**Bias Assessment Conclusion:** [ ] Low Concern | [ ] Moderate Concern — controls required | [ ] High Concern — escalate before adoption

---

## SECTION 4: SECURITY ASSESSMENT

### 4.1 AI-Specific Security Controls

| Security Area | Control Present? | Evidence | Risk |
|---------------|-----------------|---------|------|
| Adversarial robustness testing conducted | Yes / No / Partial | | H/M/L |
| Model poisoning protections implemented | Yes / No / Partial | | H/M/L |
| Prompt injection protections (for LLMs) | Yes / No / Partial | | H/M/L |
| Model inversion attack protections | Yes / No / Partial | | H/M/L |
| Unauthorized access to model weights prevented | Yes / No / Partial | | H/M/L |
| Security penetration testing of AI system | Yes / No / Partial | | H/M/L |
| Vulnerability disclosure program exists | Yes / No | | H/M/L |
| CVE/security incident history reviewed | Yes / No | | H/M/L |

### 4.2 Information Security Certifications

| Certification | Held? | Valid Until | Scope |
|--------------|-------|------------|-------|
| ISO/IEC 27001 | Yes / No | | |
| SOC 2 Type II | Yes / No | | |
| CSA STAR | Yes / No | | |
| PCI DSS (if relevant) | Yes / No | | |
| HIPAA BAA (if health data) | Yes / No | | |

**Security Assessment Rating:** [ ] Strong | [ ] Adequate | [ ] Requires improvement | [ ] Inadequate — block adoption

---

## SECTION 5: PRIVACY AND DATA PROTECTION ASSESSMENT

### 5.1 Data Processing Assessment

| Privacy Aspect | Assessment | Risk |
|---------------|-----------|------|
| What personal data does the supplier process? | | H/M/L |
| What is the legal basis for processing? | | H/M/L |
| Where is personal data stored and processed geographically? | | H/M/L |
| Is a GDPR Article 28 Data Processing Agreement in place? | Yes / No / Required | H/M/L |
| Are Standard Contractual Clauses in place for non-EEA transfers? | Yes / No / N/A | H/M/L |
| Does the supplier use personal data to train or improve their models? | Yes / No / Unclear | H/M/L |
| Can the supplier fulfill data subject rights requests? | Yes / No / Partial | H/M/L |
| Is personal data retained beyond the agreed period? | Yes / No / Unclear | H/M/L |
| Does the supplier have a privacy policy covering AI data use? | Yes / No | H/M/L |
| Has the supplier had data breaches in the past 3 years? | Yes / No — if Yes: describe | H/M/L |

**DPIA Required for this supplier integration?** [ ] Yes — complete DPIA before contract | [ ] No — justify: ___________

---

## SECTION 6: REGULATORY AND LEGAL COMPLIANCE ASSESSMENT

### 6.1 EU AI Act Compliance (if high-risk AI)

| Requirement | Supplier Claim | Evidence | Status |
|------------|---------------|---------|--------|
| Conformity assessment completed | | | C / NC / N/A |
| CE marking applied | | | C / NC / N/A |
| EU AI Act Declaration of Conformity available | | | C / NC / N/A |
| Technical documentation (Art. 11) available | | | C / NC / N/A |
| Post-market monitoring system in place | | | C / NC / N/A |
| Serious incident reporting capability | | | C / NC / N/A |
| EU Authorized Representative named (if non-EU) | | | C / NC / N/A |

### 6.2 Sector-Specific Compliance (complete as relevant)

| Sector | Requirement | Status |
|--------|------------|--------|
| Healthcare | UKCA/CE marking; Clinical AI validation; MDR compliance | |
| Financial Services | FCA requirements; SREP; algorithmic trading rules | |
| Education | Children's privacy (COPPA/GDPR); EdTech standards | |
| Public Sector | OECD AI Principles; public procurement rules | |

---

## SECTION 7: TRANSPARENCY AND EXPLAINABILITY ASSESSMENT

| Transparency Aspect | Available? | Quality | Notes |
|--------------------|-----------|---------|-------|
| Model card / system card published | Yes / No | H/M/L | |
| Training data overview provided | Yes / No | H/M/L | |
| Known limitations documented | Yes / No | H/M/L | |
| Performance benchmarks published | Yes / No | H/M/L | |
| Explainability features available | Yes / No | H/M/L | |
| Explanation outputs are meaningful | Yes / No | H/M/L | |
| Human-readable audit logs | Yes / No | H/M/L | |
| Changelog for model updates | Yes / No | H/M/L | |

---

## SECTION 8: CONTRACTUAL REQUIREMENTS CHECKLIST (A.10.3)

The following AI governance requirements must be included in the supplier agreement:

### 8.1 Mandatory Contract Clauses

| Requirement | Included in Contract? | Reference Clause |
|------------|----------------------|-----------------|
| AI system performance SLAs and measurement methodology | Yes / No | |
| Notification of material model changes (minimum 30 days' notice) | Yes / No | |
| Notification of serious AI incidents affecting our deployment | Yes / No | |
| Right to audit AI governance practices | Yes / No | |
| Data protection obligations (GDPR Art. 28 if applicable) | Yes / No | |
| Prohibition on using our data to train/improve supplier models | Yes / No | |
| Bias and fairness testing obligations | Yes / No | |
| Human oversight support requirements | Yes / No | |
| EU AI Act compliance obligations (if high-risk AI) | Yes / No | |
| Intellectual property and liability clauses | Yes / No | |
| Exit and data return/deletion obligations | Yes / No | |
| Subprocessor / sub-provider notification and approval | Yes / No | |

**Contract Review Conclusion:** [ ] Satisfactory | [ ] Requires negotiation of: ___________ | [ ] Do not proceed

---

## SECTION 9: OVERALL SUPPLIER ASSESSMENT

### 9.1 Assessment Scores Summary

| Assessment Area | Max Score | Score | % | Rating |
|----------------|-----------|-------|---|--------|
| Responsible AI Governance | 45 | | | |
| Technical Performance | (qualitative) | — | — | H/M/L |
| Bias and Fairness | (qualitative) | — | — | H/M/L |
| Security | (qualitative) | — | — | H/M/L |
| Privacy and Data Protection | (qualitative) | — | — | H/M/L |
| Regulatory Compliance | (qualitative) | — | — | H/M/L |
| Transparency | (qualitative) | — | — | H/M/L |
| Contract Requirements | (checklist) | — | — | Pass/Fail |

### 9.2 Key Risks Identified

| # | Risk Description | Likelihood | Impact | Risk Level | Mitigation Required |
|---|----------------|-----------|--------|-----------|---------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### 9.3 Assessment Recommendation

[ ] **Approve** — Supplier and AI system meet requirements; proceed to contracting
[ ] **Conditional Approval** — Approve subject to: ___________
[ ] **Deferred** — Reassess after supplier addresses: ___________
[ ] **Reject** — Do not adopt. Reasons: ___________

### 9.4 Ongoing Monitoring Requirements

| Monitoring Activity | Frequency | Owner |
|--------------------|-----------|-------|
| Performance metrics review | | |
| Bias/fairness metric review | | |
| Security incident check | | |
| Regulatory compliance update | | |
| Contract compliance review | | |
| Full re-assessment | Annual | |

---

## SECTION 10: APPROVALS

| Role | Name | Recommendation | Signature | Date |
|------|------|---------------|-----------|------|
| Assessor | | | | |
| Procurement Lead | | | | |
| AI Governance Lead | | | | |
| CISO (if security risk identified) | | | | |
| DPO (if personal data flows) | | | | |
| Legal Counsel (if contractual issues) | | | | |

---

## Appendix: AI Supplier Due Diligence Questionnaire

Send to supplier as part of RFP / onboarding process:

1. Do you have a published Responsible AI or Ethical AI Policy? Please provide.
2. Are you ISO/IEC 42001:2023 certified or in the process of certification?
3. What bias and fairness evaluations have you conducted on this AI system?
4. Please provide your model card or equivalent technical documentation.
5. How do you notify customers of material changes to the AI model?
6. What adversarial robustness testing have you conducted?
7. Can you confirm the geographic location of all data processing?
8. Do you use customer data to train or improve your AI models?
9. What explainability features are available for this AI system?
10. Please describe your AI incident response process.
11. Have you completed any EU AI Act conformity assessments?
12. What information security certifications do you hold?
13. What is your average time to notify customers of security incidents?
14. Can you support fulfillment of data subject access/deletion requests?
15. Please describe your supply chain AI governance (do you use sub-providers)?

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Aligned with ISO/IEC 42001:2023 Annex A Domain A.10 and EU AI Act obligations for deployers*
