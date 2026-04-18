# AI Ethics Framework
## ISO/IEC 42001:2023 | Clause 5.2 / Annex A.7

**Document ID:** AIMS-ETHICS-001
**Version:** 1.0
**Owner:** AI Governance Lead / Chief Ethics Officer
**Approved By:** [CEO / Board]
**Date:** ___________________________
**Review Cycle:** Annual

---

## Purpose

This AI Ethics Framework establishes the ethical principles, commitments, and governance mechanisms that govern how [Organisation Name] develops, deploys, and operates AI systems. It underpins the AIMS Policy and operationalises the responsible AI commitments made under Annex A.7 of ISO/IEC 42001:2023.

This framework is aligned with:
- ISO/IEC 42001:2023 Annex A.7 — Responsible and Trustworthy AI
- ISO/IEC TR 24368:2022 — AI ethical and societal concerns
- OECD AI Principles (2019, updated 2024)
- UNESCO Recommendation on the Ethics of AI (2021)
- EU AI Act — ethical requirements for AI systems

---

## Our Ethical AI Commitments

### 1. Fairness

We commit to designing and operating AI systems that treat all individuals fairly and do not unlawfully discriminate on the basis of protected characteristics including age, gender, race, ethnicity, disability, sexual orientation, religion, or any other characteristic protected by applicable law.

**In practice this means:**
- Evaluating AI systems for bias before deployment and continuously during operation
- Applying fairness testing across relevant demographic groups
- Documenting and remediating identified bias
- Maintaining audit trails of fairness assessments for each AI system
- Ensuring training data is representative and not systematically biased

**Minimum standard:** All AI systems affecting individuals must pass a fairness evaluation before deployment. See `AI-SYSTEM-IMPACT-ASSESSMENT.md`.

---

### 2. Transparency

We commit to being open and honest about our use of AI — with our customers, employees, regulators, and the public.

**In practice this means:**
- Informing people when AI is being used to make or influence decisions that affect them
- Providing meaningful explanations of AI decisions when requested
- Documenting the purpose, capabilities, and limitations of each AI system
- Publishing AI system documentation (model cards) for material AI systems
- Disclosing AI system failures and material incidents to relevant stakeholders

**Minimum standard:** Any AI system making or significantly influencing a decision about an individual must include a disclosure mechanism and an explanation capability. See `AI-MODEL-CARD-TEMPLATE.md` and `AWARENESS-COMMUNICATION-PLAN.md`.

---

### 3. Accountability

We commit to clear ownership and accountability for every AI system we operate. No AI system is "ungoverned."

**In practice this means:**
- Every AI system has a named, accountable AI System Owner
- The AI System Owner is personally responsible for the system's performance and compliance
- The AI Governance Lead has organisation-wide accountability for the AIMS
- Board-level sponsor ensures strategic alignment and resources
- Accountability does not diminish when AI systems are operated by third parties — suppliers are held to the same standards through contracts and audits

**Minimum standard:** See `AI-SYSTEM-OWNERSHIP-REGISTER.md` for the register of all AI systems and their accountable owners.

---

### 4. Human Oversight and Control

We commit to maintaining meaningful human oversight and control over AI systems, especially in high-stakes contexts.

**In practice this means:**
- Defining appropriate human oversight levels for each AI system (human-in-loop, human-on-loop, or human-in-command)
- Ensuring humans can review, challenge, override, and switch off AI systems
- Not deploying fully autonomous AI decision-making in high-risk contexts without explicit senior approval and rigorous safeguards
- Training staff on how to exercise effective oversight and recognise AI errors
- Maintaining override capabilities that are regularly tested

**Minimum standard:** Human oversight requirements must be defined in each AI system's model card and deployment checklist. See `AI-DEPLOYMENT-CHECKLIST.md`.

---

### 5. Privacy and Data Protection

We commit to protecting personal data throughout the AI lifecycle, embedding privacy by design from the earliest stages of AI development.

**In practice this means:**
- Processing personal data for AI only with a lawful basis under applicable data protection law
- Conducting Data Protection Impact Assessments before deploying AI systems that process personal data at scale
- Minimising personal data used in AI training and operation to what is strictly necessary
- Implementing appropriate security controls to protect personal data in AI systems
- Respecting data subject rights including the right to explanation for automated decisions

**Minimum standard:** All AI systems processing personal data must have a completed DPIA. See `AI-SYSTEM-IMPACT-ASSESSMENT.md` and `LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md`.

---

### 6. Safety and Security

We commit to ensuring our AI systems are safe and secure — that they do not cause unacceptable harm and are resilient against malicious misuse.

**In practice this means:**
- Conducting safety and security assessments before deploying AI systems
- Testing AI systems for adversarial vulnerabilities before deployment
- Maintaining incident response capabilities for AI-specific incidents
- Not deploying AI systems where the risk of harm is unacceptably high and cannot be adequately mitigated
- Maintaining fallback procedures for when AI systems fail

**Minimum standard:** All AI systems must pass security and safety testing before deployment. See `AI-DEPLOYMENT-CHECKLIST.md` and `AI-INCIDENT-RESPONSE-PROCEDURE.md`.

---

### 7. Reliability and Robustness

We commit to operating AI systems that perform consistently, reliably, and as intended — and monitoring them continuously to detect degradation.

**In practice this means:**
- Establishing performance baselines and monitoring against them continuously
- Detecting and responding to model drift, data drift, and performance degradation
- Testing AI systems in representative environments before production deployment
- Documenting known limitations and acceptable use boundaries for each system
- Not making material changes to AI systems without going through the change control process

**Minimum standard:** See `AI-PERFORMANCE-MONITORING-PLAN.md` and `AI-CHANGE-CONTROL-PROCEDURE.md`.

---

### 8. Societal and Environmental Responsibility

We commit to considering the broader societal and environmental impacts of our AI systems, not just the immediate business benefit.

**In practice this means:**
- Assessing potential societal harms in AI system impact assessments
- Considering the environmental footprint of AI compute (energy consumption, carbon emissions)
- Not developing or deploying AI systems intended for harmful purposes
- Engaging with affected communities where AI systems have significant societal impact
- Contributing to the responsible AI ecosystem through open-source contributions and knowledge sharing

**Minimum standard:** Societal impact must be assessed in `AI-SYSTEM-IMPACT-ASSESSMENT.md` for all Tier 1 and Tier 2 AI systems.

---

## Ethical Red Lines

The following uses of AI are **prohibited** regardless of business justification:

| # | Prohibited Use | Basis |
|---|---------------|-------|
| 1 | AI systems that manipulate individuals through subliminal or deceptive techniques | EU AI Act Art. 5 / Ethics |
| 2 | AI-based social scoring of individuals by public authorities | EU AI Act Art. 5 |
| 3 | Real-time biometric surveillance in public spaces (except where legally permitted) | EU AI Act Art. 5 |
| 4 | AI systems that exploit vulnerabilities of specific groups (age, disability, etc.) | EU AI Act Art. 5 / Ethics |
| 5 | AI systems designed to generate non-consensual intimate imagery | Legal / Ethics |
| 6 | AI systems designed to facilitate discrimination in violation of applicable law | Legal |
| 7 | AI systems used to make fully automated decisions with legal or similarly significant effects without human review | GDPR Art. 22 / Ethics |
| 8 | AI systems that process sensitive personal data (health, biometrics, political views) without explicit consent or legal basis | GDPR / Legal |

---

## Ethical Decision-Making Process

When faced with an ethically ambiguous AI decision, apply the following process:

**Step 1 — Identify the ethical question**
What is the potential harm? Who could be affected? What are the competing interests?

**Step 2 — Apply the principles**
Does this action align with all eight principles above? Which principles are in tension?

**Step 3 — Consult**
For significant ethical questions, consult the AI Governance Lead and, where appropriate, the AI Ethics Committee or DPO.

**Step 4 — Document**
Record the ethical question, the reasoning applied, and the decision made. Undocumented ethical decisions create accountability gaps.

**Step 5 — Escalate if unresolved**
If the ethical question cannot be resolved at working level, escalate to the AI Governance Committee. If still unresolved, escalate to board level.

---

## AI Ethics Governance Structure

| Role | Ethics Responsibilities |
|------|------------------------|
| Board / CEO | Ultimate accountability; approve ethical red lines and major ethical decisions |
| AI Governance Lead | Day-to-day ethics oversight; maintain this framework; chair AI Ethics Committee |
| AI Ethics Committee | Review material ethical questions; advise on edge cases; annual framework review |
| AI System Owners | Responsible AI operation within their systems; flag ethical concerns |
| DPO | Privacy ethics; DPIA oversight; data subject rights |
| Legal / Compliance | Regulatory ethics obligations; contract ethics clauses |
| All Staff | Awareness; report concerns; comply with this framework |

---

## Relationship to OECD AI Principles

| OECD Principle | How Addressed in This Framework |
|---------------|--------------------------------|
| Inclusive growth, sustainable development | Section 8 — Societal and Environmental Responsibility |
| Human-centred values and fairness | Section 1 — Fairness; Section 4 — Human Oversight |
| Transparency and explainability | Section 2 — Transparency |
| Robustness, security, safety | Section 6 — Safety; Section 7 — Reliability |
| Accountability | Section 3 — Accountability |

---

## Ethics Review Process

| Trigger | Review Type | Frequency | Owner |
|---------|-------------|-----------|-------|
| New AI system deployment | Ethics pre-assessment | Per system | AI System Owner |
| Material change to AI system | Ethics change review | Per change | AI System Owner |
| Significant incident | Post-incident ethics review | Per incident | AI Governance Lead |
| Annual AIMS review | Full framework review | Annual | AI Governance Lead |
| Regulatory change | Targeted review | As triggered | Legal / DPO |

---

## Review and Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| AI Governance Lead | | | |
| DPO | | | |
| Legal | | | |
| CEO / Board | | | |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue | |
| | | | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 5.2 / Annex A.7 — AI Ethics Framework | See root README.md for full index*
