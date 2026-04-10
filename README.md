# 🤖 ISO/IEC 42001:2023 AI Governance Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ISO Standard](https://img.shields.io/badge/Standard-ISO%2FIEC%2042001%3A2023-blue)](https://www.iso.org/standard/81230.html)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Ankit%20Uniyal-green)](https://github.com/Ankit-Uniyal)

> *"AI is not just a technology decision — it's a governance imperative."*

**The most comprehensive open-source ISO/IEC 42001:2023 AI Governance Toolkit available.** Built by an ISO 42001 Lead Auditor for GRC professionals, AI governance practitioners, compliance leads, and organizations seeking certification.

---

## 🎯 What's in this Toolkit?

This toolkit provides **everything you need** to implement, operate, and get certified against ISO/IEC 42001:2023 — the international standard for AI Management Systems (AIMS). It covers all **10 clauses**, all **39 Annex A controls** across **9 control domains**, and every mandatory document required by the standard.

---

## 📁 Complete Document Library

### 🏛️ Governance and Policy Documents

| Document | Description | ISO 42001 Clause | Annex A Controls |
|----------|-------------|-----------------|-----------------|
| [AIMS-POLICY-TEMPLATE.md](./AIMS-POLICY-TEMPLATE.md) | Complete AI Management System Policy — purpose, scope, ethical principles, roles, prohibited uses, lifecycle requirements | Clause 5.2 | A.2.2, A.2.3 |

### 📋 Assessment and Planning Templates

| Document | Description | ISO 42001 Clause | Annex A Controls |
|----------|-------------|-----------------|-----------------|
| [GAP-ASSESSMENT.md](./GAP-ASSESSMENT.md) | Full gap assessment checklist covering all 128 requirements (Clauses 4-10 + Annex A) with scoring and maturity rating | All Clauses | All Annex A |
| [AI-SYSTEM-IMPACT-ASSESSMENT.md](./AI-SYSTEM-IMPACT-ASSESSMENT.md) | 10-part ASIA template covering benefits, fundamental rights, bias, privacy, safety, societal impacts, human oversight | Clause 8.4 | A.5.2, A.5.3, A.5.4 |
| [STATEMENT-OF-APPLICABILITY.md](./STATEMENT-OF-APPLICABILITY.md) | Complete SoA with all 39 Annex A controls — applicability, justification, status, implementation reference | Clause 6.1.3 | All Annex A |
| [AI-RISK-REGISTER.md](./AI-RISK-REGISTER.md) | Risk register with 44 pre-populated risks across 8 categories, scoring matrix, and treatment log | Clause 6.1, 8.2, 8.3 | A.5.2 |

### 🔄 Operational Procedures

| Document | Description | ISO 42001 Clause | Annex A Controls |
|----------|-------------|-----------------|-----------------|
| [AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md](./AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md) | End-to-end AI lifecycle from design to decommissioning — governance gates, model cards, bias evaluation, adversarial testing, monitoring | Clause 8.5 | A.6.1.1 – A.6.5.1 (13 controls) |
| [AI-INCIDENT-RESPONSE-PROCEDURE.md](./AI-INCIDENT-RESPONSE-PROCEDURE.md) | 7-phase incident response lifecycle — detection, classification, containment, investigation, notification, remediation, post-incident review | Clause 10.2 | A.8.5, A.9.4, A.6.4.1 |
| [AI-SUPPLIER-ASSESSMENT.md](./AI-SUPPLIER-ASSESSMENT.md) | Third-party AI due diligence template covering governance maturity, bias, security, privacy, regulatory compliance, and contract requirements | Clause 8.1 | A.10.2, A.10.3, A.10.4 |

### 📊 Audit and Review Templates

| Document | Description | ISO 42001 Clause | Annex A Controls |
|----------|-------------|-----------------|-----------------|
| [INTERNAL-AUDIT-PROCEDURE.md](./INTERNAL-AUDIT-PROCEDURE.md) | Complete internal audit framework — audit program, checklist for all clauses and all 39 Annex A controls, report template, corrective action tracking | Clause 9.2 | All Annex A |
| [MANAGEMENT-REVIEW-TEMPLATE.md](./MANAGEMENT-REVIEW-TEMPLATE.md) | Full management review template with all 13 required inputs, KPI dashboard, risk review, incident review, and output decisions | Clause 9.3 | — |

### 🗺️ Reference and Mapping Documents

| Document | Description | ISO 42001 Clause | Annex A Controls |
|----------|-------------|-----------------|-----------------|
| [CONTROLS-MAPPING.md](./CONTROLS-MAPPING.md) | Cross-reference of all 39 Annex A controls mapped to EU AI Act articles, NIST AI RMF functions, and ISO 27001 controls | Clause 6.1.3 | All Annex A |
| [IMPLEMENTATION-ROADMAP.md](./IMPLEMENTATION-ROADMAP.md) | 12-month implementation roadmap — 4 phases, milestones, deliverables, resource estimates, common pitfalls | All Clauses | All Annex A |

---

## 📖 ISO/IEC 42001:2023 Standard Structure

### Standard Clauses Overview

| Clause | Title | Key Requirements |
|--------|-------|-----------------|
| **4** | Context of the Organization | Define scope, identify interested parties, understand AI context |
| **5** | Leadership | AI Policy, top management commitment, roles and responsibilities |
| **6** | Planning | AI risk assessment, risk treatment, Statement of Applicability, AI objectives |
| **7** | Support | Resources, competence, awareness, communication, documented information |
| **8** | Operation | Risk assessment execution, risk treatment, ASIA, AI lifecycle management |
| **9** | Performance Evaluation | Monitoring, internal audit, management review |
| **10** | Improvement | Nonconformity management, corrective action, continual improvement |

### Annex A Controls by Domain (39 Controls Total)

#### Domain A.2 — Policies for AI (2 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.2.2 | AI Policy | Document, approve, communicate, and review organizational AI policy |
| A.2.3 | AI-Specific Policies | Policies for prohibited uses, ethics, human oversight, acceptable use |

#### Domain A.3 — Internal Organization (4 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.3.2 | AI Governance Roles | Define and assign AI governance responsibilities |
| A.3.3 | Segregation of Duties | Protect AI system integrity through appropriate separation |
| A.3.4 | Contact with AI Authorities | Maintain relationships with AI regulators and standards bodies |
| A.3.6 | AI in Project Management | Embed AI governance into project methodology |

#### Domain A.4 — Resources for AI Systems (3 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.4.2 | AI Competencies | Ensure required AI governance competencies are maintained |
| A.4.3 | AI Infrastructure Security | Secure computing infrastructure for AI systems |
| A.4.4 | AI Tool Security | Assess and control AI development tools and libraries |

#### Domain A.5 — Assessing Impacts of AI Systems (3 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.5.2 | AI System Impact Assessment (ASIA) | Conduct pre-deployment impact assessments |
| A.5.3 | Societal and Ethical Impact | Consider societal, human rights, and fairness impacts |
| A.5.4 | Use of Assessment Results | Use ASIA findings to inform risk treatment decisions |

#### Domain A.6 — AI System Lifecycle (12 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.6.1.1 | AI Design Requirements | Include responsible AI principles in design specifications |
| A.6.1.2 | AI Design Documentation | Document system design, architecture, and responsible AI decisions |
| A.6.2.1 | AI Development Process | Follow controlled, documented development process |
| A.6.2.3 | AI Model Documentation | Maintain model cards for all AI models |
| A.6.2.5 | AI Adversarial Testing | Test resistance to adversarial attacks and manipulation |
| A.6.2.6 | AI Bias Evaluation | Evaluate and mitigate bias across demographic groups |
| A.6.2.8 | Testing in Representative Environments | Pre-deployment testing in production-representative conditions |
| A.6.3.1 | AI Deployment Controls | Controlled deployment with authorization and rollback |
| A.6.3.3 | Human Oversight at Deployment | Operational human oversight mechanisms |
| A.6.4.1 | AI Operation Monitoring | Production monitoring of performance, accuracy, fairness |
| A.6.4.2 | AI Performance Drift Monitoring | Detect and respond to model degradation |
| A.6.5.1 | AI Decommissioning | Secure system retirement with data deletion and archiving |

#### Domain A.7 — Data for AI Systems (5 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.7.2 | AI Data Quality | Define and apply data quality criteria |
| A.7.3 | Data Provenance | Document training data lineage and provenance |
| A.7.4 | Data Privacy for AI | Comply with privacy laws in AI data processing |
| A.7.5 | Bias Mitigation in Data | Identify and mitigate bias in training data |
| A.7.6 | Data Access Controls | Least-privilege access to AI data and models |

#### Domain A.8 — Information for Interested Parties (4 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.8.2 | AI Capability Information | Provide accurate AI capability and limitation information |
| A.8.3 | AI Explainability | Define and implement appropriate explainability |
| A.8.4 | AI Disclosure to Users | Inform users when interacting with AI systems |
| A.8.5 | AI Incident Communication | Communicate AI incidents to affected parties |

#### Domain A.9 — Use of AI Systems (3 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.9.2 | Acceptable Use of AI | Define and enforce AI acceptable use policies |
| A.9.3 | Human Oversight | Implement oversight for high-stakes AI decisions |
| A.9.4 | AI Error Handling | Define processes for AI system error detection and handling |

#### Domain A.10 — Third-Party and Customer AI (3 controls)
| Control | Title | Key Requirement |
|---------|-------|----------------|
| A.10.2 | Third-Party AI Risk Assessment | Assess third-party AI before adoption |
| A.10.3 | AI Supplier Contracts | Include AI governance clauses in supplier agreements |
| A.10.4 | Customer AI Governance | Identify and meet customer AI governance requirements |

---

## 🚀 Quick Start Guide

### For Organizations Starting ISO 42001 Implementation:
1. **Read** [IMPLEMENTATION-ROADMAP.md](./IMPLEMENTATION-ROADMAP.md) — understand the 12-month journey
2. **Conduct** gap assessment using [GAP-ASSESSMENT.md](./GAP-ASSESSMENT.md)
3. **Complete** [STATEMENT-OF-APPLICABILITY.md](./STATEMENT-OF-APPLICABILITY.md) to determine which controls apply
4. **Draft** your AI Policy using [AIMS-POLICY-TEMPLATE.md](./AIMS-POLICY-TEMPLATE.md)
5. **Populate** [AI-RISK-REGISTER.md](./AI-RISK-REGISTER.md) with your organization's AI risks
6. **Conduct** AI System Impact Assessments using [AI-SYSTEM-IMPACT-ASSESSMENT.md](./AI-SYSTEM-IMPACT-ASSESSMENT.md)

### For GRC Professionals Auditing AI Governance:
1. Use [INTERNAL-AUDIT-PROCEDURE.md](./INTERNAL-AUDIT-PROCEDURE.md) as your complete audit toolkit
2. Reference [CONTROLS-MAPPING.md](./CONTROLS-MAPPING.md) for cross-framework evidence mapping
3. Use [GAP-ASSESSMENT.md](./GAP-ASSESSMENT.md) for client maturity assessments

### For AI Teams Building Responsible AI:
1. Follow [AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md](./AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md) for governance-embedded development
2. Use the model card template in the lifecycle document for all AI models
3. Use [AI-SYSTEM-IMPACT-ASSESSMENT.md](./AI-SYSTEM-IMPACT-ASSESSMENT.md) before every deployment

---

## 🔗 Framework Alignment

This toolkit aligns with and maps to:

| Framework | Alignment |
|-----------|-----------|
| **EU AI Act (2024)** | All 39 controls mapped to relevant EU AI Act articles |
| **NIST AI RMF 1.0** | Controls mapped to GOVERN, MAP, MEASURE, MANAGE functions |
| **ISO/IEC 27001:2022** | Controls integrated with information security management |
| **GDPR/UK GDPR** | Privacy requirements embedded throughout data controls (A.7) |
| **OECD AI Principles** | Ethical AI principles aligned with A.2 and A.9 controls |

---

## 📚 Mandatory Documents Checklist

Use this checklist to track your AIMS documentation completeness:

- [ ] AIMS Scope Statement (Clause 4.3)
- [ ] AI Policy — AIMS-POLICY-TEMPLATE.md (Clause 5.2)
- [ ] Statement of Applicability — STATEMENT-OF-APPLICABILITY.md (Clause 6.1.3) ⚠️ MANDATORY
- [ ] AI Risk Assessment Records — AI-RISK-REGISTER.md (Clause 6.1)
- [ ] AI Risk Treatment Plans (Clause 6.1, 8.3)
- [ ] AI Objectives Documentation (Clause 6.2)
- [ ] Evidence of Competence — Training Records (Clause 7.2)
- [ ] AI System Impact Assessments — AI-SYSTEM-IMPACT-ASSESSMENT.md (Clause 8.4)
- [ ] AI Lifecycle Records — AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md (Clause 8.5)
- [ ] Monitoring and Measurement Results (Clause 9.1)
- [ ] Internal Audit Records — INTERNAL-AUDIT-PROCEDURE.md (Clause 9.2)
- [ ] Management Review Records — MANAGEMENT-REVIEW-TEMPLATE.md (Clause 9.3)
- [ ] Nonconformity and Corrective Action Records (Clause 10.2)

---

## 🏆 Certification Journey

### Certification Bodies (ISO 42001)
Accredited CBs offering ISO 42001 certification include:
BSI Group | Bureau Veritas | DNV | SGS | TÜV | LRQA | NQA

### Timeline to Certification
- **Gap Assessment:** 2-4 weeks
- **Implementation:** 6-12 months (depending on organizational size and AI maturity)
- **Stage 1 Audit (Document Review):** Typically 1-2 days
- **Stage 2 Audit (Effectiveness):** 2-5 days (depending on scope)
- **Certification Decision:** 2-4 weeks after Stage 2

---

## 👤 About the Author

**Ankit Uniyal** — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group

- 🌐 [ankituniyalprofile.com](https://ankituniyalprofile.com/)
- ISO/IEC 42001:2023 Lead Auditor Certified
- Practitioner in AI governance, GRC, and information security management
- Experience across healthcare, technology, and financial services

---

## ⚠️ Disclaimer

This toolkit is provided for **guidance purposes only**. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text for definitive requirements. Organizations should seek qualified professional advice for their specific implementation context. Templates must be adapted to your organizational context before use.

The ISO/IEC 42001:2023 standard must be purchased from ISO or your national standards body.

---

## 📄 License

MIT License — free to use, adapt, and distribute with attribution.

---

*If this toolkit helps your AI governance work, please ⭐ star the repository and share with the GRC and AI governance community.*
