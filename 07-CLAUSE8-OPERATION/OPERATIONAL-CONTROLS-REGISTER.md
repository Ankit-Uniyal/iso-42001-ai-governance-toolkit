————————————————# Operational Controls Register
## ISO/IEC 42001:2023 | Clause 8.1 — Template

**Document ID:** AIMS-OPCONT-001
**Version:** 1.0
**Owner:** AI Governance Lead
**Date:** ___________________________
**Review Cycle:** Annual; updated when systems or controls change

---

## Purpose

This register documents all operational controls in place for each in-scope AI system, across every stage of the AI lifecycle. It demonstrates that the organisation has planned, implemented, and is maintaining the controls required by Clause 8.1 and the applicable Annex A controls.

---

## Controls Register

| Control ID | AI System (ID) | Lifecycle Stage | Control Description | Annex A Ref | Responsible Owner | Implementation Status | Evidence Location | Last Verified | Review Date |
|-----------|---------------|----------------|--------------------|-----------|-----------------|--------------------|-----------------|--------------|------------|
| OPC-001 | All systems | Design | AI design requirements documented before development begins | A.6.1.1 | AI System Owner | | | | |
| OPC-002 | All systems | Design | AI System Impact Assessment completed before development | A.5.2 | AI System Owner | | | | |
| OPC-003 | All systems | Development | Model documentation (model card) maintained | A.6.2.3 | AI Developer | | | | |
| OPC-004 | All systems | Development | Bias evaluation conducted during development | A.6.2.6 | AI Developer | | | | |
| OPC-005 | All systems | Development | Adversarial and robustness testing performed | A.6.2.5 | AI Developer | | | | |
| OPC-006 | All systems | Development | Data quality criteria defined and applied | A.7.2 | AI Developer | | | | |
| OPC-007 | All systems | Development | Data provenance and lineage documented | A.7.3 | AI Developer | | | | |
| OPC-008 | All systems using PD | Development | Personal data handling reviewed with DPO | A.7.4 | DPO | | | | |
| OPC-009 | All systems | Testing | Pre-deployment testing in representative environment | A.6.2.8 | AI Developer | | | | |
| OPC-010 | All systems | Deployment | AI Deployment Checklist completed and approved | A.6.3.1 | AI System Owner | | | | |
| OPC-011 | High-risk systems | Deployment | Human oversight mechanism active | A.6.3.3, A.9.3 | AI System Owner | | | | |
| OPC-012 | All systems | Deployment | User-facing AI disclosure in place | A.8.4 | AI System Owner / Legal | | | | |
| OPC-013 | All systems | Operation | Performance monitoring active | A.6.4.1 | AI System Owner | | | | |
| OPC-014 | All systems | Operation | Fairness drift monitoring active | A.6.4.2 | AI System Owner | | | | |
| OPC-015 | All systems | Operation | AI incident reporting channel established | A.8.5, A.9.4 | AI System Owner | | | | |
| OPC-016 | All 3rd-party AI | Operation | Supplier assessment completed and on file | A.10.2 | AI Gov Lead | | | | |
| OPC-017 | All 3rd-party AI | Operation | Contractual AI governance controls in supplier contracts | A.10.3 | Legal | | | | |
| OPC-018 | All systems | Decommission | Decommission procedure followed; data disposed per schedule | A.6.5.1 | AI System Owner | | | | |
| OPC-019 | All systems | All stages | Change control procedure followed for all system changes | 8.1 | AI System Owner | | | | |

---

## Implementation Status Codes

| Code | Meaning |
|------|---------|
| Implemented | Control is in place and operating effectively |
| Partial | Control exists but gaps remain |
| Planned | Control is planned; not yet implemented |
| Not Applicable | Control does not apply to this system (justification required) |
| Not Implemented | Control is required but not in place |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 8.1 | See root README.md for full index*
