# Statement of Applicability (SoA)
## ISO/IEC 42001:2023 | Clause 6.1.3

**Document ID:** AIMS-SOA-001  
**Organisation:** [Organisation Name]  
**Version:** 1.1  
**Prepared By:** AI Governance Lead  
**Approved By:** [CEO / Top Management]  
**Date:** ___________________________  
**Review Cycle:** Annual or after significant risk assessment changes

---

## Purpose

This Statement of Applicability (SoA) documents which Annex A controls of ISO/IEC 42001:2023 are applicable to this organisation's AI Management System (AIMS), the justification for each inclusion or exclusion, and whether each control is currently implemented.

This document is mandatory under Clause 6.1.3 of ISO/IEC 42001:2023 and is a primary audit artefact.

---

## AIMS Scope Reference

This SoA applies to the AIMS scope defined in: `03-CLAUSE4-CONTEXT/AIMS-SCOPE-STATEMENT.md`

Scope summary: [Insert one-line scope description.]

---

## How to Use This Document

- **Included (Y):** Control applies to the organisation and must be implemented.
- **Excluded (N):** Control does not apply — a justification must be documented.
- **Status:** Implemented / Partial / Planned / Not Started.
- **Evidence:** Document, record or system where evidence of implementation can be found.

All 38 Annex A controls of ISO/IEC 42001:2023 are listed below across the nine control domains (A.2 to A.10). Replace the placeholder status and evidence values with your organisation's actual position.

---

## Annex A Controls — Full Mapping

### Domain 1: Policies Related to AI (A.2)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI policy | A.2.2 | Y | Mandatory — establishes the top-level governance framework | Planned | `04-CLAUSE5-LEADERSHIP/AIMS-POLICY-TEMPLATE.md` |
| Alignment with other organisational policies | A.2.3 | Y | Required — AI policy must be consistent with security, privacy and data policies | Planned | `06-CLAUSE7-SUPPORT/MASTER-DOCUMENT-LIST.md` |
| Review of the AI policy | A.2.4 | Y | Mandatory — policy must be reviewed at planned intervals and on change | Planned | `08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md` |

---

### Domain 2: Internal Organization (A.3)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI roles and responsibilities | A.3.2 | Y | Mandatory — accountability must be assigned for each AI system | Planned | `04-CLAUSE5-LEADERSHIP/RACI-MATRIX.md` |
| Reporting of concerns | A.3.3 | Y | Required — staff and third parties must have a protected route to raise AI concerns | Planned | `09-CLAUSE10-IMPROVEMENT/AI-INCIDENT-RESPONSE-PROCEDURE.md` |

---

### Domain 3: Resources for AI Systems (A.4)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Resource documentation | A.4.2 | Y | Required — resources across the AI life cycle must be identified and documented | Planned | `06-CLAUSE7-SUPPORT/AIMS-RESOURCE-PLAN.md` |
| Data resources | A.4.3 | Y | Required — organisation uses data to develop and operate AI systems | Planned | `03-CLAUSE4-CONTEXT/AI-SYSTEMS-INVENTORY.md` |
| Tooling resources | A.4.4 | Y | Required — organisation uses ML frameworks, libraries and pre-trained models | Planned | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |
| System and computing resources | A.4.5 | Y | Required — AI systems depend on managed compute and environments | Planned | `06-CLAUSE7-SUPPORT/AIMS-RESOURCE-PLAN.md` |
| Human resources | A.4.6 | Y | Mandatory — competence and awareness are required for responsible AI | Planned | `06-CLAUSE7-SUPPORT/COMPETENCE-REQUIREMENTS-MATRIX.md` |

---

### Domain 4: Assessing Impacts of AI Systems (A.5)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI system impact assessment process | A.5.2 | Y | Mandatory — a defined impact assessment process is required | Planned | `07-CLAUSE8-OPERATION/AI-SYSTEM-IMPACT-ASSESSMENT.md` |
| Documentation of AI system impact assessments | A.5.3 | Y | Mandatory — assessment results must be documented and retained | Planned | `06-CLAUSE7-SUPPORT/RECORDS-RETENTION-SCHEDULE.md` |
| Assessing AI system impact on individuals or groups | A.5.4 | Y | Required — AI systems affect individuals and identifiable groups | Planned | `07-CLAUSE8-OPERATION/AI-SYSTEM-IMPACT-ASSESSMENT.md` |
| Assessing societal impacts of AI systems | A.5.5 | Y | Required — broader societal and environmental effects must be considered | Planned | `04-CLAUSE5-LEADERSHIP/AI-ETHICS-FRAMEWORK.md` |

---

### Domain 5: AI System Life Cycle (A.6)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Objectives for responsible development of AI systems | A.6.1.2 | Y | Required — responsible development objectives must guide design | Planned | `05-CLAUSE6-PLANNING/AI-OBJECTIVES-REGISTER.md` |
| Processes for responsible AI system design and development | A.6.1.3 | Y | Required — organisation develops or configures AI systems | Planned | `07-CLAUSE8-OPERATION/AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md` |
| AI system requirements and specification | A.6.2.2 | Y | Required — purpose and responsible-AI requirements must be specified | Planned | `07-CLAUSE8-OPERATION/AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md` |
| Documentation of AI system design and development | A.6.2.3 | Y | Required — design decisions and rationale must be recorded | Planned | `07-CLAUSE8-OPERATION/AI-MODEL-CARD-TEMPLATE.md` |
| AI system verification and validation | A.6.2.4 | Y | Mandatory — systems must be tested against defined acceptance criteria | Planned | `07-CLAUSE8-OPERATION/AI-DEPLOYMENT-CHECKLIST.md` |
| AI system deployment | A.6.2.5 | Y | Required — deployment must be controlled and approved | Planned | `07-CLAUSE8-OPERATION/AI-DEPLOYMENT-CHECKLIST.md` |
| AI system operation and monitoring | A.6.2.6 | Y | Mandatory — operational performance and drift must be monitored | Planned | `08-CLAUSE9-PERFORMANCE/AI-PERFORMANCE-MONITORING-PLAN.md` |
| AI system technical documentation | A.6.2.7 | Y | Required — technical documentation must be produced and maintained | Planned | `07-CLAUSE8-OPERATION/AI-MODEL-CARD-TEMPLATE.md` |
| AI system recording of event logs | A.6.2.8 | Y | Required — logging is needed for traceability and investigation | Planned | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |

---

### Domain 6: Data for AI Systems (A.7)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Data for development and enhancement of AI systems | A.7.2 | Y | Required — data requirements must be defined per AI system | Planned | `03-CLAUSE4-CONTEXT/AI-SYSTEMS-INVENTORY.md` |
| Acquisition of data | A.7.3 | Y | Required — data must be obtained lawfully and with authorisation | Planned | `03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md` |
| Quality of data for AI systems | A.7.4 | Y | Mandatory — data quality directly affects AI outcomes | Planned | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |
| Data provenance | A.7.5 | Y | Required — origin and permitted use of data must be traceable | Planned | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |
| Data preparation | A.7.6 | Y | Required — cleaning, labelling and bias treatment must be governed | Planned | `07-CLAUSE8-OPERATION/AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md` |

---

### Domain 7: Information for Interested Parties of AI Systems (A.8)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| System documentation and information for users | A.8.2 | Y | Required — users need capability and limitation information | Planned | `07-CLAUSE8-OPERATION/AI-MODEL-CARD-TEMPLATE.md` |
| External reporting | A.8.3 | Y | Required — regulatory reporting obligations apply | Planned | `03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md` |
| Communication of incidents | A.8.4 | Y | Mandatory — AI incidents must be communicated within required timescales | Planned | `09-CLAUSE10-IMPROVEMENT/AI-INCIDENT-RESPONSE-PROCEDURE.md` |
| Information for interested parties | A.8.5 | Y | Required — AI involvement must be disclosed to affected parties | Planned | `06-CLAUSE7-SUPPORT/AWARENESS-COMMUNICATION-PLAN.md` |

---

### Domain 8: Use of AI Systems (A.9)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Processes for responsible use of AI systems | A.9.2 | Y | Mandatory — acceptable use, oversight and error handling must be defined | Planned | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |
| Objectives for responsible use of AI systems | A.9.3 | Y | Required — objectives and limits for AI use must be documented | Planned | `05-CLAUSE6-PLANNING/AI-OBJECTIVES-REGISTER.md` |
| Intended use of the AI system | A.9.4 | Y | Mandatory — systems must be used per their intended purpose | Planned | `07-CLAUSE8-OPERATION/AI-MODEL-CARD-TEMPLATE.md` |

---

### Domain 9: Third-Party and Customer Relationships (A.10)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Allocating responsibilities | A.10.2 | Y | Required — responsibilities across the AI value chain must be allocated | Planned | `07-CLAUSE8-OPERATION/AI-SUPPLIER-ASSESSMENT.md` |
| Suppliers | A.10.3 | Y | Required — organisation uses third-party AI systems and services | Planned | `07-CLAUSE8-OPERATION/AI-SUPPLIER-CONTRACT-CLAUSES.md` |
| Customers | A.10.4 | Y | Included where the organisation provides AI systems or services to customers | Planned | `07-CLAUSE8-OPERATION/AI-SUPPLIER-ASSESSMENT.md` |

---

## Exclusions Summary

| Control | Ref | Reason for Exclusion |
|---------|-----|---------------------|
| None at this time | — | All 38 Annex A controls are currently assessed as applicable |

**Note:** If your organisation excludes any controls, document a clear justification here. Auditors scrutinise exclusions closely. Controls may only be excluded where the relevant AI risk genuinely does not apply to the defined scope.

---

## Implementation Status Summary

| Status | Count | % of Total |
|--------|-------|-----------|
| Implemented | 0 | 0% |
| Partial | 0 | 0% |
| Planned | 38 | 100% |
| Not Started | 0 | 0% |
| **Total Controls** | **38** | **100%** |

Update this table as implementation progresses. Target: all applicable controls at "Implemented" before the certification audit.

---

## SoA Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| AI Governance Lead | | | |
| Risk Manager | | | |
| Top Management | | | |

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Ankit Uniyal | Initial release |
| 1.1 | August 2026 | Ankit Uniyal | Rebuilt the control list against the correct ISO/IEC 42001:2023 Annex A structure (38 controls across 9 domains), corrected all control references and titles, and fixed the broken table formatting |

---

*Part of the ISO 42001 AI Governance Toolkit — maintained by Ankit Uniyal*
