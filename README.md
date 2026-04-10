# 🤖 ISO/IEC 42001:2023 AI Governance Toolkit

> **"AI is not just a technology decision — it's a governance imperative."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ISO 42001](https://img.shields.io/badge/Standard-ISO%2042001%3A2023-blue)](https://www.iso.org/standard/81230.html)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Ankit%20Uniyal-green)](https://github.com/Ankit-Uniyal)

A **free, practical implementation toolkit** for ISO/IEC 42001:2023 AI Management Systems (AIMS) — built by a practitioner, for practitioners. Includes gap assessment checklists, AI risk register templates, controls mapping, and a phased implementation roadmap.

---

## Table of Contents

- [What is ISO 42001](#what-is-iso-42001)
- [Who Should Use This](#who-should-use-this)
- [Toolkit Contents](#toolkit-contents)
- [ISO 42001 Structure](#iso-42001-structure)
- [Implementation Roadmap](#implementation-roadmap)
- [Clause Breakdown](#clause-breakdown)
- [Framework Mapping](#framework-mapping)
- [Resources](#resources)
- [About the Author](#about-the-author)

---

## What is ISO 42001

**ISO/IEC 42001:2023** is the world's first international standard for **AI Management Systems (AIMS)**. Published in December 2023, it provides a systematic framework for organizations to establish responsible AI governance, assess and treat AI-specific risks, demonstrate accountability to regulators, and align with the EU AI Act, NIST AI RMF, and other AI regulations.

### Key Facts

| Feature | Detail |
|---------|--------|
| Standard | ISO/IEC 42001:2023 |
| Published | December 2023 |
| Type | Management System Standard (like ISO 27001, ISO 9001) |
| Certification | Yes — third-party certification available |
| Scope | Any organization developing, providing, or using AI systems |
| Annex SL | Yes — compatible with ISO 27001, ISO 9001, ISO 22301 |

---

## Who Should Use This

- **GRC Professionals** leading AI governance programs
- **CISOs and Risk Officers** integrating AI risk into enterprise risk frameworks
- **ISO 42001 Lead Implementers and Auditors** preparing for certification
- **AI Product Teams** building responsible AI into development pipelines
- **Compliance Officers** mapping AI to EU AI Act, NIST AI RMF, UAE AI Strategy
- **Internal Auditors** assessing AI governance maturity

---

## Toolkit Contents

| File | Description |
|------|-------------|
| README.md | Overview, structure, roadmap, and clause breakdown |
| GAP-ASSESSMENT.md | Clause-by-clause gap assessment checklist (200+ questions) |
| AI-RISK-REGISTER.md | AI risk register template with scoring methodology |
| CONTROLS-MAPPING.md | ISO 42001 controls mapped to EU AI Act, NIST AI RMF, ISO 27001 |
| AI-POLICY-TEMPLATE.md | Editable AI Policy and AI Ethics Policy templates |
| IMPLEMENTATION-GUIDE.md | Phased 12-month implementation guide with milestones |

---

## ISO 42001 Structure

ISO 42001 follows the **Annex SL** high-level structure (same as ISO 27001):

| Clause | Title | Key Focus |
|--------|-------|-----------|
| 4 | Context of the Organization | Scope, stakeholders, internal/external context |
| 5 | Leadership | AI Policy, roles, top management commitment |
| 6 | Planning | AI risk assessment, risk treatment, AI objectives |
| 7 | Support | Resources, competence, awareness, communication |
| 8 | Operation | AI lifecycle, impact assessment, data governance |
| 9 | Performance Evaluation | Monitoring, internal audit, management review |
| 10 | Improvement | Corrective action, continual improvement |
| Annex A | Controls Reference | 38 controls across 9 control domains |

### Annex A Control Domains

| Domain | Focus Area |
|--------|------------|
| A.2 — Policies for AI | AI policy framework |
| A.3 — Internal organization | AI governance structure and roles |
| A.4 — Resources for AI systems | Compute, data, and human resources |
| A.5 — Assessing impacts of AI | AI system impact assessment (ASIA) |
| A.6 — AI system lifecycle | Design, develop, deploy, decommission |
| A.7 — Data for AI systems | Data quality, bias, provenance |
| A.8 — Information for interested parties | Transparency and disclosure |
| A.9 — Use of AI systems | Responsible use policies |
| A.10 — Third-party and customer relationships | Vendor AI risk, supply chain |

---

## Implementation Roadmap

### Phase 1 — Foundation (Months 1 to 2)

| Activity | Owner | Output |
|----------|-------|--------|
| Executive sponsorship and AI governance mandate | C-Suite | Signed mandate |
| Appoint AI Governance Lead / AIMS Manager | HR / CISO | RACI matrix |
| Define AIMS scope | GRC Team | Scope document |
| AI system inventory — catalog all AI in use | IT / Business | AI asset register |
| Conduct ISO 42001 gap assessment | GRC / Audit | Gap assessment report |
| Identify applicable regulations | Legal / GRC | Regulatory mapping |

### Phase 2 — Risk and Policy Framework (Months 3 to 4)

| Activity | Owner | Output |
|----------|-------|--------|
| Develop AI Policy and AI Ethics Policy | GRC / Legal | Approved policies |
| Define AI risk appetite and tolerance | Risk Committee | Risk appetite statement |
| Build AI risk register | Risk Team | AI risk register v1 |
| Conduct AI impact assessments for high-risk AI | GRC / Product | Impact assessment reports |
| Map interested parties | GRC | Stakeholder register |
| Define AI objectives and KPIs | Leadership | AI objectives document |

### Phase 3 — Controls Implementation (Months 5 to 8)

| Activity | Owner | Output |
|----------|-------|--------|
| Implement Annex A controls | GRC / IT | Controls implementation log |
| Establish AI system lifecycle procedures | IT / AI Teams | Lifecycle procedures |
| Implement data governance for AI training data | Data Team | Data governance framework |
| Deploy AI monitoring and logging | IT / SecOps | Monitoring dashboards |
| Conduct AI security assessment | Security Team | Assessment report |
| Deliver AI awareness training to all staff | HR / GRC | Training completion records |
| Establish AI incident response process | GRC / SecOps | AI IR playbook |

### Phase 4 — Audit and Certification Prep (Months 9 to 10)

| Activity | Owner | Output |
|----------|-------|--------|
| Internal audit against ISO 42001 clauses | Internal Audit | Audit report and findings |
| Corrective action for non-conformities | Process Owners | CAR log |
| Management review meeting | Leadership | Management review minutes |
| Pre-certification readiness assessment | External Consultant | Readiness report |
| Select and engage certification body | GRC Lead | Certification agreement |

### Phase 5 — Certification and Continual Improvement (Months 11 to 12)

| Activity | Owner | Output |
|----------|-------|--------|
| Stage 1 audit (document review) | Certification Body | Stage 1 report |
| Address Stage 1 findings | GRC Team | Evidence package |
| Stage 2 audit (on-site or remote) | Certification Body | Certification decision |
| Continual improvement plan | GRC Lead | Improvement roadmap |
| Annual surveillance audit planning | GRC Lead | Audit schedule |

---

## Clause Breakdown

### Clause 4 — Context

Understand internal and external factors, identify interested parties (regulators, customers, affected communities), and define the AIMS scope. Use PESTLE analysis for external context and SWOT for internal context. Start with a narrow scope — it is easier to certify and expand later.

### Clause 5 — Leadership

Top management must actively demonstrate commitment. Establish a formal AI Policy covering responsible AI principles, prohibited AI uses, data ethics, and human oversight. Consider creating an AI Ethics Board or AI Governance Committee at executive level.

### Clause 6 — Planning

Conduct structured AI risk assessments covering model risks, data risks, operational risks, and societal impacts.

| Risk Category | Examples |
|--------------|----------|
| Bias and fairness | Discriminatory outcomes from AI models |
| Transparency | Inability to explain AI decisions to regulators |
| Data quality and privacy | Training data issues, PII leakage in outputs |
| Security | Adversarial attacks, model poisoning, prompt injection |
| Operational | Model drift, performance degradation, system failure |
| Regulatory | Non-compliance with EU AI Act, GDPR, sector regulations |
| Third-party AI | Risks from vendor AI systems and external APIs |

### Clause 8 — Operation

Implement the full AI system lifecycle with controls at each stage:

| Lifecycle Stage | Key Controls |
|----------------|-------------|
| Data Collection | Data provenance, bias testing, privacy compliance, consent management |
| Model Design | Fairness metrics, explainability requirements, security by design |
| Development | Version control, adversarial testing, documentation standards |
| Validation | Independent testing, bias evaluation, performance benchmarking |
| Deployment | Human oversight mechanisms, monitoring setup, rollback procedures |
| Operation | Continuous monitoring, drift detection, incident logging |
| Decommissioning | Data deletion, model archiving, stakeholder notification |

### Clause 9 — Performance Evaluation

| Metric | Description | Frequency |
|--------|-------------|-----------|
| AI Risk Treatment Rate | % of AI risks with active treatment plans | Monthly |
| Model Performance Drift | Deviation from baseline performance | Per model weekly |
| AI Incident Rate | Number of AI-related incidents | Quarterly |
| Bias Test Coverage | % of AI models with documented bias testing | Quarterly |
| AI Training Completion | % of staff completed AI ethics training | Annually |
| ASIA Completion Rate | % of new AI deployments with impact assessments | Per deployment |
| Control Effectiveness | % of Annex A controls tested and passed | Annually |

---

## Framework Mapping

| Framework | Relationship to ISO 42001 |
|-----------|--------------------------|
| **EU AI Act** | ISO 42001 helps satisfy technical documentation, risk management, and conformity assessment for high-risk AI |
| **NIST AI RMF 1.0** | GOVERN/MAP/MEASURE/MANAGE functions map directly to ISO 42001 clauses 4-10 |
| **ISO/IEC 27001** | AI security controls in ISO 42001 Annex A complement ISO 27001 Annex A |
| **MITRE ATLAS** | AI adversarial threat intelligence that feeds ISO 42001 risk assessments |
| **OWASP LLM Top 10** | Technical AI vulnerability guidance relevant to Clause 8 |
| **UAE National AI Strategy 2031** | ISO 42001 aligns with UAE's national AI governance agenda |
| **GDPR and UAE PDPL** | Data protection requirements relevant to ISO 42001 data governance controls |

---

## Resources

### Official Standards
- [ISO/IEC 42001:2023 — AI Management Systems](https://www.iso.org/standard/81230.html)
- [ISO/IEC 23894:2023 — AI Risk Management Guidance](https://www.iso.org/standard/77304.html)
- [ISO/IEC 38507:2022 — Governance of AI](https://www.iso.org/standard/56641.html)

### Regulatory Frameworks
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [NIST AI Risk Management Framework 1.0](https://airc.nist.gov/RMF)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)

### Technical References
- [MITRE ATLAS](https://atlas.mitre.org/)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [ENISA AI Cybersecurity Guidance](https://www.enisa.europa.eu/topics/artificial-intelligence)

### Certifications
- [ISO 42001 Lead Implementer — PECB](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001)
- [AI Governance Professional — IAPP](https://iapp.org/certify/aigp/)

---

## About the Author

**Ankit Uniyal** — GRC Lead, PureHealth Group | ISO 42001 Lead Auditor | AI Governance Professional

- 10+ years in Information Security, GRC, and IT Audit across healthcare, banking, and fintech
- ISO 42001 Lead Auditor certified — hands-on AIMS implementation experience
- Currently overseeing AI governance across 100+ hospitals at PureHealth Group, Abu Dhabi UAE
- Builder of the free [AI Risk Navigator](https://ankituniyalprofile.com/) — maps AI risks across 12+ frameworks in 5 minutes

**Connect:** [LinkedIn](https://linkedin.com/in/ankituniyal8) | [GitHub](https://github.com/Ankit-Uniyal) | [Portfolio](https://ankituniyalprofile.com/)

---

## Contributing

Contributions are welcome! Please open a Pull Request or Issue if you want to add:
- Additional checklist items from real audit experience
- Sector-specific regulatory mappings (healthcare, financial services, government)
- Tool recommendations for AI governance automation
- Case studies or implementation lessons

---

## License

Released under the [MIT License](LICENSE). Free to use, adapt, and share — attribution appreciated.

---

*Built by a GRC practitioner who believes AI governance should be accessible to everyone, not locked behind expensive consultants.*
