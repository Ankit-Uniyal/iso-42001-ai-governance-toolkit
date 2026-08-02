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

## Domain A.2 — Policies Related to AI

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.2.2 | AI policy — establish, document, communicate and review a top-level AI policy | Art. 17; Art. 26 | GOVERN 1.1, GOVERN 1.2 | A.5.1 |
| A.2.3 | Alignment with other organizational policies — reconcile the AI policy with related policies | Art. 17 | GOVERN 1.1, GOVERN 2.1 | A.5.1 |
| A.2.4 | Review of the AI policy — review at planned intervals and on significant change | Art. 17; Art. 9 | GOVERN 1.1, MANAGE 4.1 | A.5.1 |

---

## Domain A.3 — Internal Organization

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.3.2 | AI roles and responsibilities — define, assign and communicate accountability | Art. 26; Art. 22 | GOVERN 2.1, GOVERN 2.2 | A.5.2 |
| A.3.3 | Reporting of concerns — accessible, protected channel for raising AI concerns | Art. 26; Art. 73; Dir. (EU) 2019/1937 | GOVERN 4.1, GOVERN 4.2, GOVERN 4.3 | A.6.8 |

---

## Domain A.4 — Resources for AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.4.2 | Resource documentation — identify and document resources across the life cycle | Art. 17; Art. 11 | GOVERN 1.2, MAP 1.1 | A.5.9 |
| A.4.3 | Data resources — document and manage the data resources AI systems rely on | Art. 10 | MAP 2.3, MEASURE 2.2 | A.5.9, A.5.34 |
| A.4.4 | Tooling resources — govern frameworks, libraries, pre-trained models and MLOps tooling | Art. 15 | MAP 4.1, MANAGE 2.2 | A.8.28, A.8.31 |
| A.4.5 | System and computing resources — manage compute, storage, networking and environments | Art. 15 | MAP 4.1, MANAGE 3.1 | A.8.1, A.8.9 |
| A.4.6 | Human resources — roles, competence, training and awareness for AI | Art. 4; Art. 26 | GOVERN 2.2, GOVERN 3.2 | A.6.3 |

---

## Domain A.5 — Assessing Impacts of AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.5.2 | AI system impact assessment process — defined, triggered and approved process | Art. 27; Art. 9 | MAP 5.1, MAP 5.2 | A.5.35 |
| A.5.3 | Documentation of AI system impact assessments — record, retain and make available | Art. 27; Art. 11; Art. 18 | MAP 5.1, GOVERN 1.4 | A.5.33 |
| A.5.4 | Assessing impact on individuals or groups — harms, severity and subgroup analysis | Art. 27; Art. 5; Art. 14 | MAP 1.1, MAP 3.3, MEASURE 2.11 | A.5.34 |
| A.5.5 | Assessing societal impacts — wider social, economic and environmental effects | Art. 27; Recital 27 | MAP 3.1, MAP 5.1 | — |

---

## Domain A.6 — AI System Life Cycle

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.6.1.2 | Objectives for responsible development of AI systems | Art. 9; Art. 17 | GOVERN 1.1, GOVERN 3.2, MAP 1.4 | Clause 6.2 |
| A.6.1.3 | Processes for responsible AI system design and development | Art. 9; Art. 17 | MAP 1.1, MANAGE 1.1 | A.8.25 |
| A.6.2.2 | AI system requirements and specification | Art. 9; Art. 13 | MAP 1.1, MAP 2.1 | A.8.26 |
| A.6.2.3 | Documentation of AI system design and development | Art. 11; Annex IV | MAP 2.2, GOVERN 1.4 | A.5.37 |
| A.6.2.4 | AI system verification and validation, including bias and robustness testing | Art. 9; Art. 15; Art. 10 | MEASURE 2.1, MEASURE 2.5, MEASURE 2.7, MEASURE 2.11 | A.8.29 |
| A.6.2.5 | AI system deployment, including release approval and rollback | Art. 16; Art. 43 | MANAGE 1.1, MANAGE 2.1 | A.8.32 |
| A.6.2.6 | AI system operation and monitoring, including drift and retirement | Art. 72; Art. 26 | MEASURE 2.4, MANAGE 4.1 | A.8.16 |
| A.6.2.7 | AI system technical documentation | Art. 11; Art. 13; Annex IV | MAP 2.2, MEASURE 1.1 | A.5.37 |
| A.6.2.8 | AI system recording of event logs | Art. 12; Art. 19; Art. 26 | MEASURE 1.1, MEASURE 2.4 | A.8.15, A.8.16 |

---

## Domain A.7 — Data for AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.7.2 | Data for development and enhancement of AI systems | Art. 10 | MAP 2.3, MEASURE 2.2 | A.5.9 |
| A.7.3 | Acquisition of data, including lawful basis and access control | Art. 10; Art. 53 | MAP 2.3, MANAGE 2.2 | A.5.15, A.5.34, A.8.12 |
| A.7.4 | Quality of data for AI systems | Art. 10 | MEASURE 2.2, MEASURE 2.3 | A.5.12 |
| A.7.5 | Data provenance and lineage | Art. 10; Art. 53 | MAP 2.3, MEASURE 2.2 | A.5.13 |
| A.7.6 | Data preparation, including labelling and bias treatment | Art. 10 | MEASURE 2.11, MAP 2.3 | A.5.12 |

---

## Domain A.8 — Information for Interested Parties of AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.8.2 | System documentation and information for users, including explainability | Art. 13; Art. 11 | MEASURE 2.8, MEASURE 2.9 | A.5.37 |
| A.8.3 | External reporting to authorities and other external parties | Art. 73; Art. 49; Art. 71; Art. 62 | GOVERN 4.3, MANAGE 4.1 | A.5.5, A.5.31 |
| A.8.4 | Communication of incidents to those who need to know | Art. 73; Art. 26 | MANAGE 4.1, MANAGE 4.3 | A.5.24, A.5.26, A.6.8 |
| A.8.5 | Information for interested parties, including AI disclosure | Art. 50; Art. 13; Art. 86 | GOVERN 5.1, MAP 5.2 | A.5.34 |

---

## Domain A.9 — Use of AI Systems

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.9.2 | Processes for responsible use, including human oversight and error handling | Art. 26; Art. 14 | GOVERN 5.1, MANAGE 1.1, MANAGE 2.3 | A.5.10 |
| A.9.3 | Objectives for responsible use of AI systems | Art. 26; Art. 14 | GOVERN 1.1, GOVERN 5.1, MANAGE 1.1 | Clause 6.2 |
| A.9.4 | Intended use of the AI system and prevention of out-of-scope use | Art. 26; Art. 25; Art. 13 | MAP 1.1, MAP 3.4, MANAGE 1.2 | A.5.10 |

---

## Domain A.10 — Third-Party and Customer Relationships

| ISO 42001 Control | Control Description | EU AI Act | NIST AI RMF | ISO 27001 |
|-------------------|--------------------|-----------|-------------|-----------|
| A.10.2 | Allocating responsibilities across the AI value chain | Art. 25; Art. 26; Art. 16 | GOVERN 2.1, GOVERN 6.1, GOVERN 6.2 | A.5.19, A.5.2 |
| A.10.3 | Suppliers — assessment, contractual terms and ongoing monitoring | Art. 25; Art. 16 | GOVERN 6.1, GOVERN 6.2, MAP 4.1 | A.5.19, A.5.20, A.5.21, A.5.22 |
| A.10.4 | Customers — information, support and contractual commitments | Art. 13; Art. 25; Art. 26 | GOVERN 5.1, GOVERN 6.1 | A.5.20 |

---

## Summary: ISO 42001 to NIST AI RMF Function Mapping

| NIST AI RMF Function | Key Activities | Primary ISO 42001 Clauses | Key Annex A Controls |
|---------------------|----------------|--------------------------|---------------------|
| **GOVERN** | AI governance structures, policies, culture, roles | Clause 4, 5, 6.2 | A.2, A.3, A.9 |
| **MAP** | Context, risk identification, AI system classification | Clause 4, 6.1 | A.5, A.6.1, A.7, A.10 |
| **MEASURE** | Risk evaluation, testing, monitoring, metrics | Clause 6.1, 8.2, 9.1 | A.5, A.6.2, A.7 |
| **MANAGE** | Risk treatment, incident response, continual improvement | Clause 6.1.3, 8.3, 10 | A.6.2, A.8.4, A.9.2 |

---

## Summary: ISO 42001 to EU AI Act Article Mapping

| EU AI Act Requirement | Key Articles | Primary ISO 42001 Clauses | Key Annex A Controls |
|----------------------|--------------|--------------------------|---------------------|
| Risk Management System | Art. 9 | Clause 6, 8.2, 8.3 | A.2, A.5, A.6.2 |
| Data and Data Governance | Art. 10 | Clause 8.5 | A.7 |
| Technical Documentation | Art. 11 | Clause 7.5, 8.5 | A.6.2.3, A.6.2.7 |
| Transparency and Provision of Information | Art. 13 | Clause 7.4 | A.8.2, A.8.5 |
| Human Oversight | Art. 14 | Clause 8.6 | A.9.2 |
| Accuracy, Robustness, Cybersecurity | Art. 15 | Clause 8.5 | A.6.2.4, A.4.5 |
| Quality Management System | Art. 17 | Clause 4-10 (entire AIMS) | All Annex A |
| Fundamental Rights Impact Assessment | Art. 27 | Clause 8.4 | A.5.2, A.5.3, A.5.4 |
| Post-Market Monitoring | Art. 72 | Clause 9.1 | A.6.2.6 |
| Reporting of Serious Incidents | Art. 73 | Clause 10.2 | A.8.3, A.8.4 |

---

*Maintained by [Ankit Uniyal](https://github.com/Ankit-Uniyal) — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*This mapping is for guidance purposes. Always refer to the original standards for definitive requirements.*
