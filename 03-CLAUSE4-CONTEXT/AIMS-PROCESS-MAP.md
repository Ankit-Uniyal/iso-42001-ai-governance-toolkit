# AIMS Process Map
## ISO/IEC 42001:2023 | Clause 4.4 — Template

**Document ID:** AIMS-PMAP-001
**Version:** 1.0
**Owner:** AI Governance Lead
**Date:** ___________________________
**Review Cycle:** Annual or upon significant AIMS change

---

## 1. Purpose

This document maps all processes within the AI Management System (AIMS), showing their owners, inputs, outputs, and interactions. It satisfies the requirement in Clause 4.4 that the organisation establish, implement, maintain and continually improve an AIMS — including all required processes and their interactions.

---

## 2. AIMS Process Overview

```
[Clause 4 — Context]
      |
            v
            [Clause 5 — Leadership & Policy]
                  |
                        v
                        [Clause 6 — Planning: Risk Assessment, Objectives, SOA]
                              |
                                    v
                                    [Clause 7 — Support: Resources, Competence, Communication, Documents]
                                          |
                                                v
                                                [Clause 8 — Operation: AI Lifecycle, Impact Assessment, Supplier Mgmt]
                                                      |
                                                            v
                                                            [Clause 9 — Performance Evaluation: Monitoring, Audit, Mgmt Review]
                                                                  |
                                                                        v
                                                                        [Clause 10 — Improvement: Corrective Actions, Continual Improvement]
                                                                              |
                                                                                    +---> Feeds back into Clauses 4-9 (continuous loop)
                                                                                    ```

                                                                                    ---

                                                                                    ## 3. Process Register

                                                                                    | Process ID | Process Name | Clause | Owner | Inputs | Outputs | Key Controls | Review Cycle |
                                                                                    |-----------|-------------|--------|-------|--------|---------|--------------|-------------|
                                                                                    | P-01 | Context Analysis | 4.1 / 4.2 | AI Governance Lead | PESTLE factors, stakeholder input | Context Register, Interested Parties Register | Annual review gate | Annual |
                                                                                    | P-02 | Scope Definition | 4.3 | AI Governance Lead | Context Register, AI Systems Inventory | AIMS Scope Statement | Management approval | Annual or on change |
                                                                                    | P-03 | Leadership Commitment | 5.1 | CEO / Top Management | Business strategy, regulatory requirements | AI Policy, governance committee | Board sign-off | Annual |
                                                                                    | P-04 | AI Policy Management | 5.2 | AI Governance Lead | Regulatory requirements, stakeholder needs | Published AI Policy | Version control, approval | Annual |
                                                                                    | P-05 | Roles and Responsibilities | 5.3 | AI Governance Lead | Org chart, AI systems inventory | RACI Matrix, role descriptions | Job description alignment | Annual |
                                                                                    | P-06 | AI Risk Assessment | 6.1 | Risk Manager | Context Register, AI Systems Inventory | AI Risk Register | Defined assessment methodology | Per system, annual minimum |
                                                                                    | P-07 | Risk Treatment Planning | 6.1 | Risk Manager | AI Risk Register | Risk Treatment Plan, SOA | Management approval | Per risk cycle |
                                                                                    | P-08 | AI Objectives Management | 6.2 | AI Governance Lead | AI Policy, Risk Register | AI Objectives Register | Measurable targets | Quarterly review |
                                                                                    | P-09 | Change Management | 6.3 | AI Governance Lead | Change requests, audit findings | Change Log | Impact assessment | As triggered |
                                                                                    | P-10 | Resource Management | 7.1 | AI Governance Lead | AIMS requirements, budget | Resource Plan | Management approval | Annual |
                                                                                    | P-11 | Competence Management | 7.2 | HR / AI Gov Lead | Role requirements, gap analysis | Training Records | Competence evidence | Annual |
                                                                                    | P-12 | Awareness and Communication | 7.3 / 7.4 | AI Governance Lead | Policy updates, stakeholder needs | Communication Plan, records | Delivery confirmation | Ongoing |
                                                                                    | P-13 | Document Control | 7.5 | AI Governance Lead | Document creation requests | Master Document List | Version control, approval | Ongoing |
                                                                                    | P-14 | AI Impact Assessment | 8.2 | AI System Owner | New/changed AI systems | Impact Assessment Reports | Pre-deployment gate | Per deployment |
                                                                                    | P-15 | AI Lifecycle Management | 8.3 | AI System Owner | Design requirements, data, model | System Cards, deployment records | Stage gate reviews | Per system lifecycle |
                                                                                    | P-16 | Supplier Management | 8.4 | Procurement / AI Gov Lead | Third-party AI systems | Supplier Assessments, Supplier Risk Register | Contractual controls | Annual per supplier |
                                                                                    | P-17 | Performance Monitoring | 9.1 | Risk Manager | AI system metrics, AIMS KPIs | Performance Dashboard | Automated monitoring alerts | Continuous / Monthly |
                                                                                    | P-18 | Internal Audit | 9.2 | Internal Auditor | Audit programme, AIMS documentation | Audit Reports, NCRs | Auditor independence | Annual programme |
                                                                                    | P-19 | Management Review | 9.3 | CEO / AI Gov Lead | All AIMS performance inputs | Management Review Minutes, action register | Quorum, agenda discipline | Annual minimum |
                                                                                    | P-20 | Corrective Action | 10.1 | AI Governance Lead | NCRs, incidents, audit findings | Corrective Action Plans, NCR log | Root cause analysis | As triggered |
                                                                                    | P-21 | Continual Improvement | 10.2 | AI Governance Lead | Management review outputs, best practices | Improvement Log | PDCA cycle | Ongoing |

                                                                                    ---

                                                                                    ## 4. Process Interactions

                                                                                    | Process | Feeds Into | Receives From |
                                                                                    |---------|-----------|---------------|
                                                                                    | P-01 Context Analysis | P-02, P-06, P-08 | P-19 Management Review |
                                                                                    | P-06 Risk Assessment | P-07, P-17 | P-01, P-14, P-18 |
                                                                                    | P-14 Impact Assessment | P-15, P-07 | P-06, P-09 |
                                                                                    | P-18 Internal Audit | P-20, P-19 | P-13, all processes |
                                                                                    | P-19 Management Review | P-20, P-21, P-01 | P-17, P-18, P-08 |
                                                                                    | P-20 Corrective Action | P-06, P-21 | P-18, P-19, P-14 |

                                                                                    ---

                                                                                    ## 5. Master Document List Cross-Reference

                                                                                    See `06-CLAUSE7-SUPPORT/MASTER-DOCUMENT-LIST.md` for the complete list of all AIMS documents, owners, versions, and review dates.

                                                                                    ---

                                                                                    ## Review History

                                                                                    | Version | Date | Changes | Approved By |
                                                                                    |---------|------|---------|-------------|
                                                                                    | 1.0 | | Initial issue | |

                                                                                    ---

                                                                                    *ISO/IEC 42001:2023 AI Governance Toolkit | Clause 4.4 | See root README.md for full index*
