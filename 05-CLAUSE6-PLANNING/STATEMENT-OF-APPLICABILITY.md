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
- - **Excluded (N):** Control does not apply — justification must be documented
  - - **Implementation Status:** Implemented / Partial / Planned / Not Started
    - - **Evidence Reference:** Document, record, or system where evidence of implementation can be found
     
      - ---

      ## Annex A Controls — Full Mapping

      ### Domain 1: Policies for AI (A.2)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | AI policy | A.2.2 | Y | Mandatory — establishes governance framework | Implemented | AIMS-POLICY-TEMPLATE.md |
      | Allocation of roles and responsibilities | A.2.3 | Y | Mandatory — accountability for each AI system | Implemented | RACI-MATRIX.md |
      | Reporting obligations | A.2.4 | Y | Required for regulatory compliance and management oversight | Planned | MANAGEMENT-REVIEW-TEMPLATE.md |
      | Addressing AI considerations in contracts | A.2.5 | Y | Organisation uses third-party AI systems | Partial | AI-SUPPLIER-ASSESSMENT.md |
      | Records related to AI systems | A.2.6 | Y | Mandatory documented information requirement | Implemented | MASTER-DOCUMENT-LIST.md |

      ---

      ### Domain 2: Human Oversight of AI Systems (A.3)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Establishment of human oversight mechanisms | A.3.2 | Y | Required for all AI systems affecting individuals | Planned | AI-DEPLOYMENT-CHECKLIST.md |

      ---

      ### Domain 3: Responsibilities Related to AI Systems (A.4)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Intended use | A.4.2 | Y | Mandatory — defines acceptable use boundaries | Implemented | AI-MODEL-CARD-TEMPLATE.md |
      | Accuracy, reliability and performance of AI systems | A.4.3 | Y | Core operational control | Partial | AI-PERFORMANCE-MONITORING-PLAN.md |
      | Safety of AI systems | A.4.4 | Y | Required for all AI systems | Planned | OPERATIONAL-CONTROLS-REGISTER.md |
      | Security of AI systems | A.4.5 | Y | Mandatory — AI systems are subject to adversarial threats | Partial | OPERATIONAL-CONTROLS-REGISTER.md |
      | Availability of AI systems | A.4.6 | Y | Business continuity requirement | Planned | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
      | Eliminating bias and promoting fairness | A.4.7 | Y | Legal and ethical requirement (GDPR, EU AI Act) | Partial | AI-SYSTEM-IMPACT-ASSESSMENT.md |
      | Transparency | A.4.8 | Y | Required for explainability and stakeholder trust | Partial | AI-MODEL-CARD-TEMPLATE.md |
      | Privacy | A.4.9 | Y | GDPR and data protection requirement | Partial | INTERESTED-PARTIES-REGISTER.md |
      | Accountability | A.4.10 | Y | Core governance principle — ownership for each system | Implemented | AI-SYSTEM-OWNERSHIP-REGISTER.md |

      ---

      ### Domain 4: Impact Assessment for AI Systems (A.5)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | AI system impact assessment process | A.5.2 | Y | Mandatory before deploying AI systems affecting individuals | Partial | AI-SYSTEM-IMPACT-ASSESSMENT.md |
      | Documentation of AI system impact assessments | A.5.3 | Y | Mandatory documented information | Planned | AI-SYSTEM-IMPACT-ASSESSMENT.md |

      ---

      ### Domain 5: AI System Lifecycle (A.6)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | General | A.6.1.2 | Y | Lifecycle controls mandatory for all AI systems in scope | Implemented | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
      | Data for AI systems | A.6.2.2 | Y | Data quality directly affects AI reliability and fairness | Partial | OPERATIONAL-CONTROLS-REGISTER.md |
      | Acquisition of AI systems and components | A.6.2.3 | Y | Organisation acquires third-party AI components | Implemented | AI-SUPPLIER-ASSESSMENT.md |
      | Design and development of AI systems | A.6.2.4 | Y | Organisation develops AI models internally | Partial | AI-MODEL-CARD-TEMPLATE.md |
      | Testing of AI systems | A.6.2.5 | Y | Pre-deployment testing is mandatory | Planned | AI-DEPLOYMENT-CHECKLIST.md |
      | AI system documentation | A.6.2.6 | Y | Mandatory documented information | Partial | AI-MODEL-CARD-TEMPLATE.md |
      | Deployment of AI systems | A.6.2.7 | Y | Deployment controls mandatory | Partial | AI-DEPLOYMENT-CHECKLIST.md |
      | Operation of AI systems | A.6.2.8 | Y | Ongoing operational monitoring required | Partial | AI-PERFORMANCE-MONITORING-PLAN.md |
      | Human oversight of AI systems during operation | A.6.2.9 | Y | Required — especially for high-risk AI systems | Planned | OPERATIONAL-CONTROLS-REGISTER.md |
      | Monitoring AI systems | A.6.2.10 | Y | Performance monitoring mandatory | Partial | AI-PERFORMANCE-MONITORING-PLAN.md |
      | Change management of AI systems | A.6.2.11 | Y | Change control required for all AI modifications | Implemented | AI-CHANGE-CONTROL-PROCEDURE.md |
      | Decommissioning of AI systems | A.6.2.12 | Y | Lifecycle control — must manage end-of-life | Planned | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
      | Incident management for AI systems | A.6.2.13 | Y | Mandatory — AI incidents must be captured and resolved | Partial | AI-INCIDENT-RESPONSE-PROCEDURE.md |

      ---

      ### Domain 6: Responsible and Trustworthy AI (A.7)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Responsible and ethical use | A.7.2 | Y | Core AIMS principle — policy commitment | Partial | AIMS-POLICY-TEMPLATE.md |

      ---

      ### Domain 7: AI System Suppliers (A.8)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Supplier relationships for AI systems | A.8.2 | Y | Organisation depends on third-party AI systems and components | Implemented | AI-SUPPLIER-RISK-REGISTER.md |

      ---

      ### Domain 8: Documentation and Information Related to AI Systems (A.9)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Documentation of AI systems | A.9.2 | Y | Mandatory documented information requirement | Partial | MASTER-DOCUMENT-LIST.md |

      ---

      ### Domain 9: AI Standards and Sector-Specific Issues (A.10)

      | Control | Ref | Included | Justification | Status | Evidence |
      |---------|-----|----------|--------------|--------|----------|
      | Compliance with applicable standards | A.10.2 | Y | ISO 42001, GDPR, EU AI Act, ISO 27001 alignment required | Partial | 11-CONTROLS-MAPPING.md |

      ---

      ## Exclusions Summary

      | Control | Ref | Reason for Exclusion |
      |---------|-----|---------------------|
      | None at this time | — | All 38 Annex A controls are applicable to this organisation |

      > **Note:** If your organisation excludes any controls, you must document a clear justification here. Auditors will scrutinise exclusions closely. Controls may only be excluded where the relevant AI risk genuinely does not apply to your scope.
      >
      > ---
      >
      > ## Implementation Status Summary
      >
      > | Status | Count | % of Total |
      > |--------|-------|-----------|
      > | Implemented | 9 | 24% |
      > | Partial | 17 | 45% |
      > | Planned | 9 | 24% |
      > | Not Started | 3 | 8% |
      > | **Total Controls** | **38** | **100%** |
      >
      > > Update this table as implementation progresses. Target: all controls at "Implemented" before certification audit.
      > >
      > > ---
      > >
      > > ## SoA Sign-Off
      > >
      > > | Role | Name | Signature | Date |
      > > |------|------|-----------|------|
      > > | AI Governance Lead | | | |
      > > | Risk Manager | | | |
      > > | CEO / Top Management | | | |
      > > | Certification Preparation Lead | | | |
      > >
      > > ---
      > >
      > > ## Review History
      > >
      > > | Version | Date | Changes | Approved By |
      > > |---------|------|---------|-------------|
      > > | 1.0 | | Initial issue — all 38 controls assessed | |
      > > | | | | |
      > >
      > > ---
      > >
      > > *ISO/IEC 42001:2023 AI Governance Toolkit | Clause 6.1.3 — Statement of Applicability | See root README.md for full index*
