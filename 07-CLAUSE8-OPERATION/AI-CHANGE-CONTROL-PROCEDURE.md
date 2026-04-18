# AI Change Control Procedure
## ISO/IEC 42001:2023 | Clause 8.1 — Template

**Document ID:** AIMS-CHGCTRL-001
**Version:** 1.0
**Owner:** AI Governance Lead
**Approved by:** ___________________________
**Date:** ___________________________
**Review Cycle:** Annual

---

## Purpose

This procedure defines how changes to in-scope AI systems are managed in a controlled, documented, and approved manner. It prevents uncontrolled modifications that could introduce new risks or compromise governance controls.

---

## Scope

Applies to all changes to in-scope AI systems including: new system deployments; major updates (new model, new training data, changed architecture, new use case); significant configuration changes affecting system behaviour; changes to data inputs affecting AI outcomes; changes to human oversight processes.

**Minor changes** (bug fixes with no model behaviour impact, documentation updates) may use a simplified notification process — document rationale for classification.

---

## Change Classification

| Type | Description | Review Required |
|------|-------------|----------------|
| Major | New system; new model; new training data; changed risk level | Full review — System Owner + AI Gov Lead + Risk Manager + DPO (if personal data) |
| Standard | Significant update to existing system; changed configuration | Standard review — System Owner + AI Gov Lead |
| Minor | No model behaviour change; no risk impact | Notification only — System Owner notifies AI Gov Lead |

---

## Change Request Process

**Step 1 — Raise** Complete Change Request Form and submit to AI Governance Lead

**Step 2 — Classify** Assign as Major / Standard / Minor per criteria above

**Step 3 — Assess Impact** For Major and Standard changes, assess impact on: Risk Register, Impact Assessment, Annex A controls, regulatory compliance, documentation

**Step 4 — Approve** Obtain required approvals per change type

**Step 5 — Implement** Test in non-production first; verify outcome; re-run relevant tests; complete Deployment Checklist for Major changes

**Step 6 — Document** Update: AI Systems Inventory, Model Card, Risk Register (if new risks), AIMS Change Log (Clause 6.3)

---

## Change Request Form

**Change Request ID:** CHG-[####]
**Date Raised:** ___________________________
**AI System:** ___________________________
**System ID:** ___________________________
**Change Type:** Major / Standard / Minor
**Requested By:** ___________________________
**Target Date:** ___________________________

**Description of Change:**
[What is being changed and why]

**Business Justification:**
[Why is this change needed]

**Impact Assessment Summary:**
[Impact on risk, controls, compliance, documentation]

**Testing Required:**
- [ ] Performance testing
- [ ] Bias and fairness evaluation
- [ ] Adversarial / security testing
- [ ] User acceptance testing
- [ ] No testing required (justification: _______________)

**Approval:**

| Role | Name | Decision | Date |
|------|------|---------|------|
| AI System Owner | | Approve / Reject | |
| AI Governance Lead | | Approve / Reject | |
| Risk Manager (if applicable) | | Approve / Reject | |
| DPO (if personal data affected) | | Approve / Reject | |

---

## Change Register

| Change ID | Date | AI System | Type | Description | Requested By | Approved By | Implemented | Status | Docs Updated |
|-----------|------|---------|------|-------------|-------------|-------------|------------|--------|-------------|
| CHG-001 | | | | | | | | | |
| CHG-002 | | | | | | | | | |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 8.1 | See root README.md for full index*
