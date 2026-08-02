# Statement of Applicability (SoA)
## ISO/IEC 42001:2023 | Clause 6.1.3

**Document ID:** AIMS-SOA-001
**Organisation:** [Organisation Name]
**Version:** 1.0
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

Scope summary: [Insert one-line scope description, e.g., "Design, deployment and monitoring of AI systems used in customer credit scoring and HR screening at [Org Name]."]

---

## How to Use This Document

- **Included (Y):** Control applies to the organisation — must be implemented
- **Excluded (N):** Control does not apply — justification must be documented
- **Implementation Status:** Implemented / Partial / Planned / Not Started
- **Evidence Reference:** Document, record, or system where evidence of implementation can be found

---

## Annex A Controls — Full Mapping

> All 38 controls of ISO/IEC 42001:2023 Annex A across 9 domains. Control references and titles follow the standard.

### Domain 1: Policies Related to AI (A.2)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI policy | A.2.2 | Y | Mandatory — establishes the top-level AI governance framework | Implemented | AIMS-POLICY-TEMPLATE.md |
| Alignment with other organizational policies | A.2.3 | Y | Required — AI policy must be consistent with security, privacy and data policies | Partial | AIMS-POLICY-TEMPLATE.md; MASTER-DOCUMENT-LIST.md |
| Review of the AI policy | A.2.4 | Y | Mandatory — policy must be reviewed at planned intervals and on change | Planned | MANAGEMENT-REVIEW-TEMPLATE.md |

---

### Domain 2: Internal Organization (A.3)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI roles and responsibilities | A.3.2 | Y | Mandatory — accountability must be allocated for each AI system | Implemented | RACI-MATRIX.md; AI-SYSTEM-OWNERSHIP-REGISTER.md |
| Reporting of concerns | A.3.3 | Y | Required — personnel need a protected route to raise AI concerns | Planned | AI-INCIDENT-RESPONSE-PROCEDURE.md |

---

### Domain 3: Resources for AI Systems (A.4)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Resource documentation | A.4.2 | Y | Required — resources must be identified across the AI life cycle | Partial | AIMS-RESOURCE-PLAN.md |
| Data resources | A.4.3 | Y | Required — organisation relies on data for AI development | Partial | AI-SYSTEMS-INVENTORY.md |
| Tooling resources | A.4.4 | Y | Required — ML frameworks, libraries and pre-trained models are in use | Partial | AIMS-RESOURCE-PLAN.md |
| System and computing resources | A.4.5 | Y | Required — compute and environments support AI development and operation | Partial | AIMS-RESOURCE-PLAN.md |
| Human resources | A.4.6 | Y | Mandatory — competence and awareness are required for responsible AI | Implemented | COMPETENCE-REQUIREMENTS-MATRIX.md; TRAINING-PLAN.md |

---

### Domain 4: Assessing Impacts of AI Systems (A.5)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| AI system impact assessment process | A.5.2 | Y | Mandatory — a defined impact assessment process is required | Implemented | AI-SYSTEM-IMPACT-ASSESSMENT.md |
| Documentation of AI system impact assessments | A.5.3 | Y | Mandatory — assessments must be recorded and retained | Partial | AI-SYSTEM-IMPACT-ASSESSMENT.md; RECORDS-RETENTION-SCHEDULE.md |
| Assessing AI system impact on individuals or groups | A.5.4 | Y | Required — AI systems affect individuals and identifiable groups | Partial | AI-SYSTEM-IMPACT-ASSESSMENT.md |
| Assessing societal impacts of AI systems | A.5.5 | Y | Required — wider societal and environmental effects must be considered | Planned | AI-ETHICS-FRAMEWORK.md |

---

### Domain 5: AI System Life Cycle (A.6)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Objectives for responsible development of AI systems | A.6.1.2 | Y | Required — responsible development objectives must guide design | Planned | AI-ETHICS-FRAMEWORK.md; AI-OBJECTIVES-REGISTER.md |
| Processes for responsible AI system design and development | A.6.1.3 | Y | Mandatory — a documented development process is required | Implemented | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
| AI system requirements and specification | A.6.2.2 | Y | Mandatory — requirements must be specified per AI system | Partial | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
| Documentation of AI system design and development | A.6.2.3 | Y | Required — design decisions and rationale must be documented | Partial | AI-MODEL-CARD-TEMPLATE.md |
| AI system verification and validation | A.6.2.4 | Y | Mandatory — testing, bias evaluation and robustness checks are required | Partial | AI-DEPLOYMENT-CHECKLIST.md |
| AI system deployment | A.6.2.5 | Y | Mandatory — controlled release with approval and rollback | Implemented | AI-DEPLOYMENT-CHECKLIST.md; AI-CHANGE-CONTROL-PROCEDURE.md |
| AI system operation and monitoring | A.6.2.6 | Y | Mandatory — ongoing monitoring including drift is required | Partial | AI-PERFORMANCE-MONITORING-PLAN.md |
| AI system technical documentation | A.6.2.7 | Y | Mandatory — technical documentation must be maintained | Partial | AI-MODEL-CARD-TEMPLATE.md |
| AI system recording of event logs | A.6.2.8 | Y | Mandatory — logging is required for traceability and investigation | Planned | OPERATIONAL-CONTROLS-REGISTER.md |

---

### Domain 6: Data for AI Systems (A.7)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Data for development and enhancement of AI systems | A.7.2 | Y | Mandatory — data requirements must be defined per system | Partial | AI-SYSTEMS-INVENTORY.md |
| Acquisition of data | A.7.3 | Y | Mandatory — data must be lawfully and appropriately acquired | Partial | LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md |
| Quality of data for AI systems | A.7.4 | Y | Mandatory — data quality requirements must be defined and verified | Partial | AI-RISK-REGISTER.md |
| Data provenance | A.7.5 | Y | Mandatory — origin and chain of custody must be recorded | Planned | AI-MODEL-CARD-TEMPLATE.md |
| Data preparation | A.7.6 | Y | Mandatory — preparation and bias treatment must be documented | Partial | AI-MODEL-CARD-TEMPLATE.md |

---

### Domain 7: Information for Interested Parties of AI Systems (A.8)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| System documentation and information for users | A.8.2 | Y | Mandatory — users need capability, limitation and use information | Partial | AI-MODEL-CARD-TEMPLATE.md |
| External reporting | A.8.3 | Y | Required — regulatory and contractual reporting duties apply | Planned | LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md |
| Communication of incidents | A.8.4 | Y | Mandatory — AI incidents must be communicated to those who need to know | Implemented | AI-INCIDENT-RESPONSE-PROCEDURE.md |
| Information for interested parties | A.8.5 | Y | Mandatory — AI involvement must be disclosed to affected parties | Partial | AWARENESS-COMMUNICATION-PLAN.md |

---

### Domain 8: Use of AI Systems (A.9)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Processes for responsible use of AI systems | A.9.2 | Y | Mandatory — acceptable use and human oversight must be defined | Implemented | OPERATIONAL-CONTROLS-REGISTER.md |
| Objectives for responsible use of AI systems | A.9.3 | Y | Required — objectives must balance efficiency against responsible use | Planned | AI-OBJECTIVES-REGISTER.md |
| Intended use of the AI system | A.9.4 | Y | Mandatory — systems must be used within their validated purpose | Partial | AI-MODEL-CARD-TEMPLATE.md |

---

### Domain 9: Third-Party and Customer Relationships (A.10)

| Control | Ref | Included | Justification | Status | Evidence |
|---------|-----|----------|--------------|--------|----------|
| Allocating responsibilities | A.10.2 | Y | Mandatory — responsibilities across the AI value chain must be allocated | Partial | AI-SUPPLIER-ASSESSMENT.md; RACI-MATRIX.md |
| Suppliers | A.10.3 | Y | Required — organisation procures third-party AI systems and services | Partial | AI-SUPPLIER-RISK-REGISTER.md; AI-SUPPLIER-CONTRACT-CLAUSES.md |
| Customers | A.10.4 | Y | Required where AI systems or AI-based services are provided to customers | Planned | AI-SUPPLIER-CONTRACT-CLAUSES.md |

---

## Exclusions Summary

| Control | Ref | Reason for Exclusion |
|---------|-----|---------------------|
| None at this time | — | All 38 Annex A controls are applicable to this organisation |

> **Note:** If your organisation excludes any controls, you must document a clear justification here. Auditors will scrutinise exclusions closely. Controls may only be excluded where the relevant AI risk genuinely does not apply to your scope.

---

## Implementation Status Summary

| Status | Count | % of Total |
|--------|-------|-----------|
| Implemented | 8 | 21% |
| Partial | 21 | 55% |
| Planned | 9 | 24% |
| Not Started | 0 | 0% |
| **Total Controls** | **38** | **100%** |

> Update this table as implementation progresses. Target: all controls at "Implemented" before the certification audit.

---

## SoA Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| AI Governance Lead | | | |
| Risk Manager | | | |
| CEO / Top Management | | | |
| Certification Preparation Lead | | | |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue — all 38 controls assessed | |
| 1.1 | | Control references and titles corrected to align with ISO/IEC 42001:2023 Annex A | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 6.1.3 — Statement of Applicability | See root README.md for full index*
