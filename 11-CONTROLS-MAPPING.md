# ISO/IEC 42001:2023 Controls Mapping

> Cross-reference of ISO 42001 Annex A controls mapped to EU AI Act, NIST AI RMF, and ISO 27001.
> Use this to demonstrate alignment across frameworks and avoid duplicating compliance efforts.

---

## How to Use This Mapping

This document helps organizations that need to comply with **multiple AI governance frameworks simultaneously**. For each ISO 42001 control, it shows the equivalent or related requirements in other major frameworks.

**Coverage:**
- ISO/IEC 42001:2023 Annex A (38 controls across 9 domains)
- EU AI Act 2024 (key articles for high-risk AI)
- NIST AI RMF 1.0 (GOVERN, MAP, MEASURE, MANAGE functions)
- ISO/IEC 27001:2022 (related information security controls)

---

## Domain A.2 — Policies for AI

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.2.2 | AI policy — establish, document, communicate, and review an organizational AI policy | Art. 9 (Risk management system), Art. 13 (Transparency) | GOVERN 1.1, GOVERN 1.2 | A.5.1 (Policies for information security) |
| A.2.3 | AI-specific policies — address prohibited uses, ethics principles, human oversight, and acceptable use | Art. 5 (Prohibited practices), Art. 9 | GOVERN 1.3, GOVERN 1.4, GOVERN 6.1 | A.5.1, A.5.10 |

---

## Domain A.3 — Internal Organization

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.3.2 | AI governance roles — define and assign responsibilities for AI governance | Art. 9(5), Art. 26 (Obligations of deployers) | GOVERN 2.1, GOVERN 2.2 | A.5.2 (Information security roles and responsibilities) |
| A.3.3 | Segregation of duties in AI — apply appropriate segregation where AI system integrity is at risk | Art. 9 | GOVERN 2.1 | A.5.3 (Segregation of duties) |
| A.3.4 | Contact with AI authorities — maintain contact with AI regulators, standards bodies | Art. 70 (Cooperation with authorities), Art. 74 | GOVERN 5.1 | A.5.5 (Contact with authorities) |
| A.3.6 | AI in project management — integrate AI governance into project management methodology | Art. 9 | GOVERN 1.7 | A.5.8 (Information security in project management) |

---

## Domain A.4 — Resources for AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.4.2 | AI competencies — ensure staff have required AI governance competencies | Art. 9(4), Art. 26(6) | GOVERN 2.2, GOVERN 4.1 | A.6.3 (Information security awareness, education, training) |
| A.4.3 | AI infrastructure security — ensure computing infrastructure meets AI security requirements | Art. 9, Art. 17 | MANAGE 2.2, MANAGE 4.1 | A.8.1 (User endpoint devices), A.8.8 (Management of technical vulnerabilities) |
| A.4.4 | AI tool security — assess and control tools used in AI development | Art. 17 | MAP 3.5 | A.8.25 (Secure development lifecycle) |

---

## Domain A.5 — Assessing Impacts of AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.5.2 | AI system impact assessment (ASIA) — conduct impact assessments before deployment | Art. 9(2), Art. 27 (Fundamental rights impact assessment) | MAP 1.1, MAP 1.5, MAP 2.3 | A.5.30 (ICT readiness for business continuity) |
| A.5.3 | Societal and ethical impact — consider societal, human rights, and fairness impacts | Art. 27, Recital 47 | MAP 1.5, MAP 2.3 | — |
| A.5.4 | Use of assessment results — inform risk treatment decisions with ASIA findings | Art. 9, Art. 27 | MAP 2.3, MAP 5.1 | A.5.29 (Information security during disruption) |

---

## Domain A.6 — AI System Lifecycle

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.6.1.1 | AI design requirements — include responsible AI principles in design specifications | Art. 9, Art. 13, Art. 14 | MAP 1.1, MAP 3.1, MAP 3.5 | A.8.25 (Secure development lifecycle) |
| A.6.1.2 | AI design documentation — document AI system design and architecture | Art. 11 (Technical documentation) | MAP 3.1 | A.5.37 (Documented operating procedures) |
| A.6.2.1 | AI development process — follow a documented development process | Art. 17 (Quality management) | MAP 3.1, MANAGE 1.3 | A.8.25 |
| A.6.2.3 | AI model documentation — maintain model cards documenting model characteristics | Art. 11, Art. 13 | MAP 3.1, MEASURE 2.5 | A.5.37 |
| A.6.2.5 | AI adversarial testing — conduct adversarial robustness testing | Art. 9(7), Art. 15 (Accuracy, robustness, cybersecurity) | MEASURE 2.6, MEASURE 2.7 | A.8.29 (Security testing in development and acceptance) |
| A.6.2.6 | AI bias evaluation — conduct bias and fairness evaluation | Art. 9(7), Art. 10(5) | MEASURE 2.5, MEASURE 2.11 | — |
| A.6.2.8 | AI testing in representative environments — test in production-representative environment before deployment | Art. 9(6) | MEASURE 2.7, MANAGE 1.3 | A.8.29 |
| A.6.3.1 | AI deployment controls — implement controls for safe deployment | Art. 9, Art. 26 | MANAGE 1.0, MANAGE 1.3 | A.8.32 (Change management) |
| A.6.3.3 | Human oversight at deployment — ensure human oversight mechanisms in deployed systems | Art. 14 (Human oversight) | MANAGE 1.2 | — |
| A.6.4.1 | AI operation monitoring — monitor deployed AI system performance | Art. 9(1)(f), Art. 72 (Post-market monitoring) | MEASURE 1.1, MANAGE 4.1 | A.8.16 (Monitoring activities) |
| A.6.4.2 | AI performance drift monitoring — detect and respond to model performance degradation | Art. 72 | MEASURE 2.2, MANAGE 4.1 | A.8.16 |
| A.6.5.1 | AI decommissioning — secure decommissioning with data deletion and model archiving | Art. 10(6) | MANAGE 4.2 | A.8.10 (Information deletion) |

---

## Domain A.7 — Data for AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.7.2 | AI data quality — define and apply data quality criteria for AI training | Art. 10(2)(3) (Data and data governance) | MAP 2.3, MEASURE 2.5 | A.8.1 |
| A.7.3 | Data provenance — document AI training data lineage and provenance | Art. 10(3) | MAP 2.3 | A.5.13 (Labelling of information) |
| A.7.4 | Data privacy for AI — handle personal data in AI training per privacy regulations | Art. 10(5), GDPR Article 6 | MAP 1.5 | A.5.34 (Privacy and protection of PII) |
| A.7.5 | Bias mitigation in data — identify and mitigate bias in AI training data | Art. 10(2)(f), Art. 10(5) | MEASURE 2.5 | — |
| A.7.6 | Data access controls — control access to AI training and operational data | Art. 10 | MANAGE 2.4 | A.5.15 (Access control), A.8.3 (Information access restriction) |

---

## Domain A.8 — Information for Interested Parties

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.8.2 | AI capability information — provide accurate information about AI capabilities and limitations | Art. 13 (Transparency and provision of information to deployers) | GOVERN 1.6, MAP 1.6 | — |
| A.8.3 | AI explainability — define and implement explainability requirements | Art. 13, GDPR Art. 22 (right to explanation) | MEASURE 2.8 | — |
| A.8.4 | AI disclosure to users — inform users when interacting with an AI system | Art. 50 (Obligations for providers of general-purpose AI) | GOVERN 1.6 | — |
| A.8.5 | AI incident communication — communicate AI incidents and performance issues to affected parties | Art. 73 (Reporting of serious incidents) | MANAGE 3.2 | A.5.24 (Information security incident management planning) |

---

## Domain A.9 — Use of AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.9.2 | Acceptable use of AI — define acceptable use policies for AI systems | Art. 26(1) | GOVERN 6.1, GOVERN 6.2 | A.5.10 (Acceptable use of information) |
| A.9.3 | Human oversight — implement human oversight for high-stakes AI decisions | Art. 14 (Human oversight) | GOVERN 6.2, MANAGE 1.2 | — |
| A.9.4 | AI error handling — define processes to detect and handle AI system errors | Art. 9(1)(c), Art. 15 | MANAGE 3.1, MANAGE 3.2 | A.5.26 (Response to information security incidents) |

---

## Domain A.10 — Third-Party and Customer AI

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|----|-----------|
| A.10.2 | Third-party AI risk assessment — assess AI-related risks before adopting third-party AI | Art. 25 (Obligations of distributors), Art. 28 | MAP 3.5, MAP 5.2 | A.5.21 (Managing information security in the ICT supply chain) |
| A.10.3 | AI supplier contracts — include AI governance requirements in supplier agreements | Art. 25, Art. 26(7) | MAP 3.5 | A.5.20 (Addressing information security within supplier agreements) |
| A.10.4 | Customer AI governance — identify and meet customer AI governance requirements | Art. 13, Art. 26 | GOVERN 5.1 | A.5.19 (Information security in supplier relationships) |

---

## Summary: ISO 42001 to NIST AI RMF Function Mapping

| NIST AI RMF Function | Key Activities | Primary ISO 42001 Clauses | Key Annex A Controls |
|---------------------|----------------|--------------------------|---------------------|
| **GOVERN** | AI governance structures, policies, culture, roles | Clause 4, 5, 6.2 | A.2, A.3, A.9 |
| **MAP** | Context, risk identification, AI system classification | Clause 4, 6.1 | A.5, A.6.1, A.7, A.10 |
| **MEASURE** | Risk evaluation, testing, monitoring, metrics | Clause 6.1, 8.2, 9.1 | A.6.2, A.6.4, A.7 |
| **MANAGE** | Risk treatment, incident response, continual improvement | Clause 6.1.3, 8.3, 10 | A.6.3, A.8.5, A.9.4 |

---

## Summary: ISO 42001 to EU AI Act Article Mapping

| EU AI Act Requirement | Key Articles | Primary ISO 42001 Clauses | Key Annex A Controls |
|----------------------|--------------|--------------------------|---------------------|
| Risk Management System | Art. 9 | Clause 6, 8.2, 8.3 | A.2, A.5, A.6.2 |
| Data and Data Governance | Art. 10 | Clause 8.5 | A.7 |
| Technical Documentation | Art. 11 | Clause 7.5, 8.5 | A.6.1.2, A.6.2.3 |
| Transparency and Provision of Information | Art. 13 | Clause 7.4 | A.8.2, A.8.3, A.8.4 |
| Human Oversight | Art. 14 | Clause 8.6 | A.9.3 |
| Accuracy, Robustness, Cybersecurity | Art. 15 | Clause 8.5 | A.6.2.5, A.4.3 |
| Quality Management System | Art. 17 | Clause 4-10 (entire AIMS) | All Annex A |
| Fundamental Rights Impact Assessment | Art. 27 | Clause 8.4 | A.5.2, A.5.3 |
| Post-Market Monitoring | Art. 72 | Clause 9.1 | A.6.4 |
| Reporting of Serious Incidents | Art. 73 | Clause 10.2 | A.8.5 |

---

*Maintained by [Ankit Uniyal](https://github.com/Ankit-Uniyal) — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*This mapping is for guidance purposes. Always refer to the original standards for definitive requirements.*
