# ISO/IEC 42001:2023 AI Governance Toolkit
## Detailed Implementation Guide

An open-source implementation toolkit for ISO/IEC 42001:2023 — the international standard for AI Management Systems (AIMS). Built by an ISO 42001 Lead Auditor.

Covers all of Clauses 4 to 10, all 38 Annex A controls across nine domains (A.2 to A.10), and every item of documented information the standard requires.

> [README.md](README.md) is the quick index. This file is the phased implementation guide: what to produce, when, who owns it, and when to revisit it.

---

## How to Use This Toolkit

Files are organised into numbered folders that follow the ISO/IEC 42001:2023 clause structure. Work through the phases below in order. Each clause folder has its own `README.md` listing the documents in reading order.

---

## PHASE 1 — UNDERSTAND AND PLAN
*Establish your baseline and build the implementation plan*

### [01-GAP-ASSESSMENT.md](01-GAP-ASSESSMENT.md)
**Use: first, before any implementation begins**

| Field | Detail |
|-------|--------|
| Purpose | Baseline assessment of current AI governance maturity against the whole standard |
| Covers | Clauses 4 to 10 and all 38 Annex A controls (124 checklist items) |
| Output | Maturity score, gap list, prioritised remediation plan |
| ISO 42001 Clause | Clause 4 (Context), Clause 6 (Planning) |
| Who completes it | AI Governance Lead / GRC Lead / Consultant |
| When to revisit | Before the Stage 1 certification audit; annually as a management review input |

### [02-IMPLEMENTATION-ROADMAP.md](02-IMPLEMENTATION-ROADMAP.md)
**Use: after the gap assessment, to structure the programme**

| Field | Detail |
|-------|--------|
| Purpose | 12-month phased implementation plan with milestones, deliverables and resource estimates |
| Covers | Four phases: Foundations, Core AIMS, Operational Controls, Audit and Certification |
| Output | Project plan, responsibility assignments, milestone tracker |
| ISO 42001 Clause | All clauses |
| Who completes it | AI Governance Lead / Project Manager |
| When to revisit | Monthly to track progress; quarterly to adjust |

---

## PHASE 2 — CONTEXT
*Clause 4 — folder [03-CLAUSE4-CONTEXT/](03-CLAUSE4-CONTEXT/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [CONTEXT-REGISTER.md](03-CLAUSE4-CONTEXT/CONTEXT-REGISTER.md) | 4.1 | Internal and external issues (PESTLE) |
| 2 | [AI-SYSTEMS-INVENTORY.md](03-CLAUSE4-CONTEXT/AI-SYSTEMS-INVENTORY.md) | 4.1 | Every AI system in scope, with owner and risk level |
| 3 | [INTERESTED-PARTIES-REGISTER.md](03-CLAUSE4-CONTEXT/INTERESTED-PARTIES-REGISTER.md) | 4.2 | Stakeholder needs and which are binding |
| 4 | [LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md](03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md) | 4.2 | Legal, regulatory and contractual AI obligations |
| 5 | [AIMS-SCOPE-STATEMENT.md](03-CLAUSE4-CONTEXT/AIMS-SCOPE-STATEMENT.md) | 4.3 | Formal, management-approved scope — **mandatory** |
| 6 | [AIMS-PROCESS-MAP.md](03-CLAUSE4-CONTEXT/AIMS-PROCESS-MAP.md) | 4.4 | AIMS processes, owners and interactions |

**Who owns this phase:** AI Governance Lead, with sign-off from top management.
**When to revisit:** annually, and whenever scope, regulation or the AI portfolio changes.

---

## PHASE 3 — LEADERSHIP
*Clause 5 — folder [04-CLAUSE5-LEADERSHIP/](04-CLAUSE5-LEADERSHIP/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [AIMS-POLICY-TEMPLATE.md](04-CLAUSE5-LEADERSHIP/AIMS-POLICY-TEMPLATE.md) | 5.2 | The AI policy — **mandatory**; supports A.2.2, A.2.3, A.2.4 |
| 2 | [LEADERSHIP-COMMITMENT-STATEMENT.md](04-CLAUSE5-LEADERSHIP/LEADERSHIP-COMMITMENT-STATEMENT.md) | 5.1 | Evidence of top management commitment |
| 3 | [AI-ETHICS-FRAMEWORK.md](04-CLAUSE5-LEADERSHIP/AI-ETHICS-FRAMEWORK.md) | 5.1 / 5.2 | Eight responsible AI principles and governance structure |
| 4 | [RACI-MATRIX.md](04-CLAUSE5-LEADERSHIP/RACI-MATRIX.md) | 5.3 | Roles, responsibilities and authorities; supports A.3.2 |
| 5 | [AI-SYSTEM-OWNERSHIP-REGISTER.md](04-CLAUSE5-LEADERSHIP/AI-SYSTEM-OWNERSHIP-REGISTER.md) | 5.3 | A named accountable owner for every AI system |

**Who owns this phase:** top management, facilitated by the AI Governance Lead.
**When to revisit:** annually; after significant incidents or reorganisations.

---

## PHASE 4 — PLANNING
*Clause 6 — folder [05-CLAUSE6-PLANNING/](05-CLAUSE6-PLANNING/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [AI-RISK-ASSESSMENT-PROCESS.md](05-CLAUSE6-PLANNING/AI-RISK-ASSESSMENT-PROCESS.md) | 6.1.2 | Documented, repeatable AI risk assessment process — **mandatory** |
| 2 | [AI-RISK-REGISTER.md](05-CLAUSE6-PLANNING/AI-RISK-REGISTER.md) | 6.1.2 | 44 pre-populated AI risks across eight categories, with scoring |
| 3 | [RISK-TREATMENT-PLAN.md](05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md) | 6.1.3 | Treatment option and controls per risk, with owner sign-off |
| 4 | [STATEMENT-OF-APPLICABILITY.md](05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md) | 6.1.3 | All 38 Annex A controls with justification and status — **mandatory** |
| 5 | [AI-OBJECTIVES-REGISTER.md](05-CLAUSE6-PLANNING/AI-OBJECTIVES-REGISTER.md) | 6.2 | Measurable AI objectives, KPIs, owners and plans — **mandatory** |
| 6 | [AIMS-CHANGE-LOG.md](05-CLAUSE6-PLANNING/AIMS-CHANGE-LOG.md) | 6.3 | Planned changes to the AIMS with impact assessment |

The AI system impact assessment *process* is required by Clause 6.1.4; the template and completed assessments live in Phase 6 under Clause 8.4.

**Who owns this phase:** AI Risk Manager and AI Governance Lead; SoA approved by top management.
**When to revisit:** quarterly for the risk register; annually for the SoA and objectives.

---

## PHASE 5 — SUPPORT
*Clause 7 — folder [06-CLAUSE7-SUPPORT/](06-CLAUSE7-SUPPORT/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [AIMS-RESOURCE-PLAN.md](06-CLAUSE7-SUPPORT/AIMS-RESOURCE-PLAN.md) | 7.1 | People, budget and infrastructure; supports A.4.2 to A.4.5 |
| 2 | [COMPETENCE-REQUIREMENTS-MATRIX.md](06-CLAUSE7-SUPPORT/COMPETENCE-REQUIREMENTS-MATRIX.md) | 7.2 | Required competence per role and gap analysis; supports A.4.6 |
| 3 | [TRAINING-PLAN.md](06-CLAUSE7-SUPPORT/TRAINING-PLAN.md) | 7.2 | Training catalogue, schedule and records — **mandatory evidence** |
| 4 | [AWARENESS-COMMUNICATION-PLAN.md](06-CLAUSE7-SUPPORT/AWARENESS-COMMUNICATION-PLAN.md) | 7.3 / 7.4 | Internal awareness and external AI disclosure; supports A.8.5 |
| 5 | [MASTER-DOCUMENT-LIST.md](06-CLAUSE7-SUPPORT/MASTER-DOCUMENT-LIST.md) | 7.5 | Master list of all AIMS documented information |
| 6 | [DOCUMENT-CONTROL-PROCEDURE.md](06-CLAUSE7-SUPPORT/DOCUMENT-CONTROL-PROCEDURE.md) | 7.5 | Creation, approval, versioning and withdrawal |
| 7 | [RECORDS-RETENTION-SCHEDULE.md](06-CLAUSE7-SUPPORT/RECORDS-RETENTION-SCHEDULE.md) | 7.5 | Retention and disposal rules for AIMS records |

---

## PHASE 6 — OPERATION
*Clause 8 — folder [07-CLAUSE8-OPERATION/](07-CLAUSE8-OPERATION/)*

| Order | Document | Clause / Control | Purpose |
|---|---|---|---|
| 1 | [OPERATIONAL-CONTROLS-REGISTER.md](07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md) | 8.1 | Every operational control across the AI lifecycle |
| 2 | [AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md](07-CLAUSE8-OPERATION/AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md) | 8.1 / A.6 | Design to decommissioning, with governance gates |
| 3 | [AI-SYSTEM-IMPACT-ASSESSMENT.md](07-CLAUSE8-OPERATION/AI-SYSTEM-IMPACT-ASSESSMENT.md) | 8.4 / A.5 | Ten-part impact assessment — **mandatory** |
| 4 | [AI-DEPLOYMENT-CHECKLIST.md](07-CLAUSE8-OPERATION/AI-DEPLOYMENT-CHECKLIST.md) | 8.1 / A.6.2.5 | Pre-deployment gate checks |
| 5 | [AI-CHANGE-CONTROL-PROCEDURE.md](07-CLAUSE8-OPERATION/AI-CHANGE-CONTROL-PROCEDURE.md) | 8.1 | Change classification and approval |
| 6 | [AI-MODEL-CARD-TEMPLATE.md](07-CLAUSE8-OPERATION/AI-MODEL-CARD-TEMPLATE.md) | 8.1 / A.6.2.7 | Model documentation per AI system |
| 7 | [AI-SUPPLIER-ASSESSMENT.md](07-CLAUSE8-OPERATION/AI-SUPPLIER-ASSESSMENT.md) | 8.1 / A.10.2 | Third-party AI due diligence questionnaire |
| 8 | [AI-SUPPLIER-RISK-REGISTER.md](07-CLAUSE8-OPERATION/AI-SUPPLIER-RISK-REGISTER.md) | 8.1 / A.10.3 | Tiered register of AI suppliers |
| 9 | [AI-SUPPLIER-CONTRACT-CLAUSES.md](07-CLAUSE8-OPERATION/AI-SUPPLIER-CONTRACT-CLAUSES.md) | 8.1 / A.10.3 | Standard AI governance contract clauses |

> Clause 8 of ISO/IEC 42001:2023 contains only 8.1 to 8.4. AI system life cycle requirements sit in Annex A domain A.6, and supplier and customer requirements in A.10; both are implemented here through the Clause 8.1 operational controls.

---

## PHASE 7 — PERFORMANCE EVALUATION
*Clause 9 — folder [08-CLAUSE9-PERFORMANCE/](08-CLAUSE9-PERFORMANCE/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [AI-PERFORMANCE-MONITORING-PLAN.md](08-CLAUSE9-PERFORMANCE/AI-PERFORMANCE-MONITORING-PLAN.md) | 9.1 | What to monitor, how, how often, who reviews — **mandatory evidence** |
| 2 | [ISO42001-INTERNAL-AUDIT-GUIDE.md](08-CLAUSE9-PERFORMANCE/ISO42001-INTERNAL-AUDIT-GUIDE.md) | 9.2 | Full audit methodology and checklists for all 38 controls |
| 3 | [INTERNAL-AUDIT-PROCEDURE.md](08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROCEDURE.md) | 9.2 | Planning, executing and following up audits — **mandatory** |
| 4 | [ANNUAL-AUDIT-PROGRAMME.md](08-CLAUSE9-PERFORMANCE/ANNUAL-AUDIT-PROGRAMME.md) | 9.2 | 12-month rolling audit schedule |
| 5 | [INDIVIDUAL-AUDIT-PLAN-TEMPLATE.md](08-CLAUSE9-PERFORMANCE/INDIVIDUAL-AUDIT-PLAN-TEMPLATE.md) | 9.2 | Per-audit scope, criteria, team and schedule |
| 6 | [MANAGEMENT-REVIEW-TEMPLATE.md](08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md) | 9.3 | 13 structured inputs and recorded outputs — **mandatory** |

---

## PHASE 8 — IMPROVEMENT
*Clause 10 — folder [09-CLAUSE10-IMPROVEMENT/](09-CLAUSE10-IMPROVEMENT/)*

| Order | Document | Clause | Purpose |
|---|---|---|---|
| 1 | [NCR-REGISTER.md](09-CLAUSE10-IMPROVEMENT/NCR-REGISTER.md) | 10.2 | Nonconformity and corrective action records — **mandatory** |
| 2 | [AI-INCIDENT-RESPONSE-PROCEDURE.md](09-CLAUSE10-IMPROVEMENT/AI-INCIDENT-RESPONSE-PROCEDURE.md) | 10.2 / A.8.4 | Seven-phase AI incident response lifecycle |
| 3 | [CONTINUAL-IMPROVEMENT-LOG.md](09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md) | 10.1 | Improvement initiatives with PDCA tracking |

> In ISO/IEC 42001:2023, Clause 10.1 is *Continual improvement* and Clause 10.2 is *Nonconformity and corrective action* — the reverse of the order used in some other management system standards.

---

## REFERENCE — USED THROUGHOUT

| Document | Purpose |
|---|---|
| [10-ANNEX-A-CONTROLS.md](10-ANNEX-A-CONTROLS.md) | Control-by-control implementation, audit and evidence guide for all 38 Annex A controls |
| [11-CONTROLS-MAPPING.md](11-CONTROLS-MAPPING.md) | Annex A mapped to EU AI Act articles, NIST AI RMF functions and ISO/IEC 27001:2022 controls |
| [12-ANNEX-B-AI-CONCEPTS.md](12-ANNEX-B-AI-CONCEPTS.md) | AI concepts, terminology and risk classification reference |
| [13-ANNEX-C-AI-DEVELOPERS.md](13-ANNEX-C-AI-DEVELOPERS.md) | Guidance for organisations that build AI for other organisations |
| [15-SCRIPTS/](15-SCRIPTS/) | Python automation: assessment currency checker and SoA implementation tracker |
| [14-WORKED-EXAMPLE/](14-WORKED-EXAMPLE/) | Completed templates for a fictional organisation, Nexus Financial Services |

---

## Documented Information Required by the Standard

| # | Documented information | Clause | Where in this toolkit |
|---|---|---|---|
| 1 | AIMS scope | 4.3 | `03-CLAUSE4-CONTEXT/AIMS-SCOPE-STATEMENT.md` |
| 2 | AI policy | 5.2 | `04-CLAUSE5-LEADERSHIP/AIMS-POLICY-TEMPLATE.md` |
| 3 | AI risk assessment process | 6.1.2 | `05-CLAUSE6-PLANNING/AI-RISK-ASSESSMENT-PROCESS.md` |
| 4 | AI risk treatment process | 6.1.3 | `05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md` |
| 5 | Statement of Applicability | 6.1.3 | `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md` |
| 6 | AI system impact assessment process | 6.1.4 | `07-CLAUSE8-OPERATION/AI-SYSTEM-IMPACT-ASSESSMENT.md` |
| 7 | AI objectives | 6.2 | `05-CLAUSE6-PLANNING/AI-OBJECTIVES-REGISTER.md` |
| 8 | Evidence of competence | 7.2 | `06-CLAUSE7-SUPPORT/TRAINING-PLAN.md` |
| 9 | Documented information control | 7.5 | `06-CLAUSE7-SUPPORT/DOCUMENT-CONTROL-PROCEDURE.md` |
| 10 | Evidence that operational processes ran as planned | 8.1 | `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md` |
| 11 | Results of AI risk assessments | 8.2 | `05-CLAUSE6-PLANNING/AI-RISK-REGISTER.md` |
| 12 | Results of AI risk treatment | 8.3 | `05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md` |
| 13 | Results of AI system impact assessments | 8.4 | `07-CLAUSE8-OPERATION/AI-SYSTEM-IMPACT-ASSESSMENT.md` |
| 14 | Monitoring and measurement results | 9.1 | `08-CLAUSE9-PERFORMANCE/AI-PERFORMANCE-MONITORING-PLAN.md` |
| 15 | Audit programme and audit results | 9.2 | `08-CLAUSE9-PERFORMANCE/ANNUAL-AUDIT-PROGRAMME.md`, `INTERNAL-AUDIT-PROCEDURE.md` |
| 16 | Management review results | 9.3 | `08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md` |
| 17 | Nonconformity and corrective action records | 10.2 | `09-CLAUSE10-IMPROVEMENT/NCR-REGISTER.md` |

---

## Standard Structure Reference

| Clause | Title | Key requirements |
|--------|-------|-----------------|
| 4 | Context of the organisation | 4.1 issues, 4.2 interested parties, 4.3 scope, 4.4 the AIMS |
| 5 | Leadership | 5.1 commitment, 5.2 AI policy, 5.3 roles and authorities |
| 6 | Planning | 6.1.1 general, 6.1.2 risk assessment, 6.1.3 risk treatment and SoA, 6.1.4 impact assessment, 6.2 objectives, 6.3 planning of changes |
| 7 | Support | 7.1 resources, 7.2 competence, 7.3 awareness, 7.4 communication, 7.5 documented information |
| 8 | Operation | 8.1 operational planning and control, 8.2 risk assessment, 8.3 risk treatment, 8.4 impact assessment |
| 9 | Performance evaluation | 9.1 monitoring, 9.2 internal audit, 9.3 management review |
| 10 | Improvement | 10.1 continual improvement, 10.2 nonconformity and corrective action |
| Annex A | Controls (normative) | 38 controls across nine domains, A.2 to A.10 |
| Annex B | Implementation guidance for the Annex A controls (informative) | — |
| Annex C | Potential AI-related organisational objectives and risk sources (informative) | — |
| Annex D | Use of the AIMS across domains or sectors (informative) | — |

---

## Framework Alignment

| Framework | Alignment |
|-----------|-----------|
| EU AI Act (2024) | All 38 controls mapped to relevant articles — see [11-CONTROLS-MAPPING.md](11-CONTROLS-MAPPING.md) |
| NIST AI RMF 1.0 | Controls mapped to GOVERN, MAP, MEASURE and MANAGE functions |
| ISO/IEC 27001:2022 | Controls integrated with information security management |
| GDPR / UK GDPR | Privacy requirements embedded throughout the data controls (A.7) |

---

## Certification

**Certification bodies:** BSI Group, Bureau Veritas, DNV, SGS, TUV, LRQA, NQA.

| Stage | Typical duration |
|-------|------------------|
| Gap assessment | 2–4 weeks |
| Implementation | 6–12 months |
| Stage 1 audit (documentation review) | 1–2 days |
| Stage 2 audit (implementation effectiveness) | 2–5 days |
| Certification decision | 2–4 weeks after Stage 2 |

---

## About

**Ankit Uniyal** — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group. GRC and information security management practitioner with experience across healthcare, technology and financial services.

Website: ankituniyalprofile.com

---

## Disclaimer

This toolkit is provided for guidance purposes only. It does not constitute legal, regulatory or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text for definitive requirements, and adapt every template to your organisational context before use. The standard must be purchased from ISO or your national standards body.

---

## Licence

MIT Licence — free to use, adapt and distribute with attribution. See [LICENSE](LICENSE).
