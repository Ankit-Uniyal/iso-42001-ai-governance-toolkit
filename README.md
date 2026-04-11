# ISO/IEC 42001:2023 AI Governance Toolkit

An open-source implementation toolkit for ISO/IEC 42001:2023 — the international standard for AI Management Systems (AIMS). Built by an ISO 42001 Lead Auditor.

Covers all 10 clauses, all 39 Annex A controls across 9 domains, and every mandatory document required by the standard.

---

## How to Use This Toolkit

The files are designed to be used in sequence, following the ISO/IEC 42001:2023 clause structure. The order below is the correct implementation journey — from establishing context through to continual improvement.

---

## Files in Correct Implementation Order

---

### PHASE 1 — UNDERSTAND AND PLAN
*Clauses 4 and 6 | Establish your baseline and build the implementation plan*

---

#### File 1 — GAP-ASSESSMENT.md
**Use: First — before any implementation begins**

| Field | Detail |
|-------|--------|
| Purpose | Baseline assessment of current AI governance maturity against all ISO 42001 requirements |
| Covers | All Clauses 4–10 and all 39 Annex A controls (128 requirements total) |
| Output | Maturity score, gap list, prioritised remediation plan |
| ISO 42001 Clause | Clause 4 (Context), Clause 6 (Planning) |
| Who completes it | AI Governance Lead / GRC Lead / Consultant |
| When to revisit | Before Stage 1 certification audit; annually as part of management review |

The gap assessment tells you which controls are already in place, which need work, and which are not started — so the implementation plan is based on evidence, not assumptions.

---

#### File 2 — IMPLEMENTATION-ROADMAP.md
**Use: Phase 1 — after the gap assessment, to structure the implementation**

| Field | Detail |
|-------|--------|
| Purpose | 12-month phased implementation plan with milestones, deliverables, and resource estimates |
| Covers | 4 phases: Foundations, Core AIMS, Operational Controls, Audit and Certification |
| Output | Project plan, responsibility assignments, milestone tracker |
| ISO 42001 Clause | All clauses |
| Who completes it | AI Governance Lead / Project Manager |
| When to revisit | Monthly to track progress; quarterly to adjust |

---

### PHASE 2 — GOVERNANCE FOUNDATIONS
*Clauses 5 and 6 | Top management commitment, scope, policy, and control selection*

---

#### File 3 — AIMS-POLICY-TEMPLATE.md
**Use: Phase 2 — first governance document to draft and get approved**

| Field | Detail |
|-------|--------|
| Purpose | AI Management System Policy — the primary governance document |
| Covers | Organisational AI commitments, ethical principles, roles, prohibited uses, scope, lifecycle requirements |
| Output | Approved, signed AI Policy ready for communication |
| ISO 42001 Clause | Clause 5.2 (AI Policy) |
| Annex A Controls | A.2.2 (AI Policy), A.2.3 (AI-Specific Policies) |
| Who completes it | AI Governance Lead; approved by CEO or Board |
| When to revisit | Annually; after scope changes or significant incidents |

The AI Policy is the instrument of top management commitment. Without it signed and in force, the AIMS is not established.

---

#### File 4 — STATEMENT-OF-APPLICABILITY.md
**Use: Phase 2 — after the gap assessment and policy, before risk treatment begins**

| Field | Detail |
|-------|--------|
| Purpose | Mandatory SoA — declares which of the 39 Annex A controls apply, why, and their implementation status |
| Covers | All 39 controls across Domains A.2–A.10; applicability, justification, status, and implementation reference |
| Output | Completed, approved SoA |
| ISO 42001 Clause | Clause 6.1.3 — MANDATORY |
| Annex A Controls | All 39 controls |
| Who completes it | AI Governance Lead / CISO / DPO |
| When to revisit | When scope changes; when new AI systems come into scope; annually |

The SoA is one of the most scrutinised documents in a certification audit. It determines which controls the organisation is committing to implement and must be completed before finalising risk treatment plans.

---

### PHASE 3 — RISK MANAGEMENT
*Clauses 6 and 8 | Identify, assess, and treat AI risks*

---

#### File 5 — AI-RISK-REGISTER.md
**Use: Phase 3 — begins concurrently with policy; maintained throughout the AIMS lifecycle**

| Field | Detail |
|-------|--------|
| Purpose | AI risk register with 44 pre-populated risks across 8 categories, scoring matrix, and risk treatment log |
| Covers | Model risks, data risks, operational risks, ethical and fairness risks, security risks, legal and regulatory risks, third-party risks, reputational risks |
| Output | Live risk register; risk treatment plans; residual risk records |
| ISO 42001 Clause | Clause 6.1 (Risk assessment), Clause 8.2 (Risk assessment execution), Clause 8.3 (Risk treatment) |
| Annex A Controls | A.5.2, A.5.4 |
| Who completes it | AI Risk Manager / AI Governance Lead |
| When to revisit | Quarterly; after every ASIA; after every significant incident; annually |

---

#### File 6 — AI-SYSTEM-IMPACT-ASSESSMENT.md
**Use: Phase 3 and ongoing — before every AI system deployment**

| Field | Detail |
|-------|--------|
| Purpose | 10-part AI System Impact Assessment (ASIA) template covering benefits, harms, fundamental rights, bias, privacy, safety, societal impacts, and human oversight |
| Covers | Pre-deployment impact assessment for each AI system in scope |
| Output | Completed ASIA per AI system; ASIA register |
| ISO 42001 Clause | Clause 8.4 — MANDATORY |
| Annex A Controls | A.5.2, A.5.3, A.5.4 |
| Who completes it | AI Risk Manager / Model Owner; reviewed by DPO; approved by AI Governance Lead |
| When to revisit | Before every deployment; after significant system changes; when monitoring reveals unexpected impacts |

The ASIA must be completed before deployment — not after. This is one of the most commonly cited nonconformities in ISO 42001 audits.

---

### PHASE 4 — OPERATIONAL CONTROLS
*Clause 8 | The procedures and processes that make governance operational*

---

#### File 7 — AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md
**Use: Phase 4 — implement before any new AI systems are built or deployed**

| Field | Detail |
|-------|--------|
| Purpose | End-to-end AI lifecycle governance procedure from design to decommissioning |
| Covers | Design governance gates, development controls, model documentation, bias evaluation, adversarial testing, pre-deployment testing, deployment authorisation, production monitoring, drift detection, decommissioning |
| Output | Controlled AI development and deployment procedure; governance gate records; model card template |
| ISO 42001 Clause | Clause 8.5 (AI system lifecycle) |
| Annex A Controls | A.6.1.1 through A.6.5.1 (all 12 lifecycle controls) |
| Who uses it | ML Engineers, Data Scientists, MLOps, Product Owners, AI Governance Lead |
| When to revisit | Annually; when new development methodologies are adopted; after lifecycle-related audit findings |

---

#### File 8 — AI-SUPPLIER-ASSESSMENT.md
**Use: Phase 4 — before adopting any third-party AI system, API, or model**

| Field | Detail |
|-------|--------|
| Purpose | Third-party AI due diligence template covering governance maturity, bias, security, privacy, regulatory compliance, and contract requirements |
| Covers | Pre-adoption risk assessment for third-party AI, supplier governance review, DPA requirements, contract clause requirements |
| Output | Completed supplier assessment per third-party AI; approval decision record |
| ISO 42001 Clause | Clause 8.1 (Operational planning and control) |
| Annex A Controls | A.10.2, A.10.3, A.10.4 |
| Who completes it | AI Risk Manager / Procurement / Legal / DPO |
| When to revisit | Before every new third-party AI adoption; annually for existing high-risk suppliers |

---

### PHASE 5 — PERFORMANCE EVALUATION
*Clause 9 | Monitor, measure, audit, and review*

---

#### File 9 — INTERNAL-AUDIT-PROCEDURE.md
**Use: Phase 5 — before Stage 2 certification audit; then on an ongoing annual cycle**

| Field | Detail |
|-------|--------|
| Purpose | Complete internal audit framework — audit programme, clause-by-clause and Annex A checklist, audit report template, corrective action tracking |
| Covers | All Clauses 4–10 and all 39 Annex A controls; audit planning, execution, and follow-up |
| Output | Internal audit programme; completed audit checklists; audit reports; corrective action register |
| ISO 42001 Clause | Clause 9.2 (Internal audit) — MANDATORY |
| Annex A Controls | All 39 controls |
| Who uses it | Internal auditors, AI Governance Lead, external consultants conducting readiness assessments |
| When to use | At least annually; before each certification audit; after major AIMS changes |

---

#### File 10 — MANAGEMENT-REVIEW-TEMPLATE.md
**Use: Phase 5 — annually minimum; after the internal audit cycle**

| Field | Detail |
|-------|--------|
| Purpose | Management review template with all 13 required inputs, KPI dashboard, risk review, incident review, and output decisions |
| Covers | All mandatory management review inputs per Clause 9.3; performance metrics; AIMS improvement decisions |
| Output | Completed management review record; AIMS improvement decisions; updated objectives |
| ISO 42001 Clause | Clause 9.3 (Management review) — MANDATORY |
| Annex A Controls | N/A (clause-level requirement) |
| Who completes it | Top management; facilitated by AI Governance Lead |
| When to use | At least annually; outputs feed into the next planning cycle |

---

### PHASE 6 — IMPROVEMENT
*Clause 10 | Nonconformity management, corrective action, and continual improvement*

---

#### File 11 — AI-INCIDENT-RESPONSE-PROCEDURE.md
**Use: Phase 6 — establish before any AI system goes into production; activated when incidents occur**

| Field | Detail |
|-------|--------|
| Purpose | 7-phase AI incident response lifecycle — detection, classification, containment, investigation, notification, remediation, and post-incident review |
| Covers | AI-specific incident types (bias, errors, security, performance, privacy), severity classification, escalation, regulatory notification, lessons learned |
| Output | Incident response procedure; incident log; post-incident review records; corrective action register |
| ISO 42001 Clause | Clause 10.2 (Nonconformity and corrective action) |
| Annex A Controls | A.8.5 (Incident communication), A.9.4 (Error handling), A.6.4.1 (Operation monitoring) |
| Who uses it | Operations, AI Governance Lead, CISO, DPO, Legal, Communications |
| When to revisit | After every AI incident; annually; when regulatory requirements change |

Clause 10 covers nonconformity, corrective action, and continual improvement. The incident response procedure is the primary operational mechanism for identifying nonconformities and driving corrective action in the AIMS.

---

### PHASE 7 — REFERENCE
*Supporting documents used across all phases*

---

#### File 12 — ANNEX-A-CONTROLS.md
**Use: Throughout — primary implementation and audit reference for all 39 Annex A controls**

| Field | Detail |
|-------|--------|
| Purpose | Control-by-control implementation, audit, and evidence guide for all 39 Annex A controls |
| Covers | All 39 controls: What It Means, Why It Matters, How to Implement, Documents to Prepare, How to Audit, Evidence Required, Common Gaps, Cross-References |
| Output | Implementation guidance per control; audit procedures; document master list; interview question bank |
| ISO 42001 Clause | Clause 6.1.3 and all Annex A domains |
| Annex A Controls | All 39 controls across A.2–A.10 |
| Who uses it | Implementers, internal auditors, GRC teams, certification consultants |
| When to use | Continuously from Phase 2 onwards; before every internal and external audit |

---

#### File 13 — CONTROLS-MAPPING.md
**Use: Throughout — cross-framework alignment and regulatory mapping**

| Field | Detail |
|-------|--------|
| Purpose | Cross-reference of all 39 Annex A controls mapped to EU AI Act articles, NIST AI RMF functions, and ISO 27001 controls |
| Covers | Full mapping: ISO 42001 Annex A to EU AI Act, NIST AI RMF 1.0, and ISO/IEC 27001:2022 |
| Output | Evidence reuse map; regulatory alignment documentation; multi-framework compliance planning |
| ISO 42001 Clause | Clause 6.1.3 |
| Annex A Controls | All 39 controls |
| Who uses it | GRC teams managing multiple frameworks, Legal and Compliance, certification preparation teams |
| When to use | During SoA completion (Phase 2), regulatory gap analysis, and multi-framework evidence mapping |

---

## Implementation Sequence — Summary

```
PHASE 1 — UNDERSTAND AND PLAN              (Clauses 4, 6)
├── 1.  GAP-ASSESSMENT.md                  Start here. Measure your baseline.
└── 2.  IMPLEMENTATION-ROADMAP.md          Build the 12-month plan.

PHASE 2 — GOVERNANCE FOUNDATIONS           (Clauses 5, 6)
├── 3.  AIMS-POLICY-TEMPLATE.md            Top management commitment. Signed policy.
└── 4.  STATEMENT-OF-APPLICABILITY.md      Declare which controls apply. MANDATORY.

PHASE 3 — RISK MANAGEMENT                  (Clauses 6, 8)
├── 5.  AI-RISK-REGISTER.md                Identify and treat AI risks.
└── 6.  AI-SYSTEM-IMPACT-ASSESSMENT.md     Assess each AI system before deployment. MANDATORY.

PHASE 4 — OPERATIONAL CONTROLS             (Clause 8)
├── 7.  AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md   Govern AI from design to decommissioning.
└── 8.  AI-SUPPLIER-ASSESSMENT.md          Assess third-party AI before adoption.

PHASE 5 — PERFORMANCE EVALUATION           (Clause 9)
├── 9.  INTERNAL-AUDIT-PROCEDURE.md        Audit your AIMS. MANDATORY.
└── 10. MANAGEMENT-REVIEW-TEMPLATE.md      Top management review. MANDATORY.

PHASE 6 — IMPROVEMENT                      (Clause 10)
└── 11. AI-INCIDENT-RESPONSE-PROCEDURE.md  Nonconformity, corrective action, lessons learned.

PHASE 7 — REFERENCE                        (Annex A / Cross-framework)
├── 12. ANNEX-A-CONTROLS.md               Control-by-control implementation and audit guide.
└── 13. CONTROLS-MAPPING.md               EU AI Act, NIST AI RMF, ISO 27001 cross-mapping.
```

---

## Mandatory Documents

ISO/IEC 42001:2023 requires the following documents as a minimum. All are covered in this toolkit.

| # | Document | Clause | File |
|---|----------|--------|------|
| 1 | AIMS Scope Statement | 4.3 | AIMS-POLICY-TEMPLATE.md |
| 2 | AI Policy | 5.2 | AIMS-POLICY-TEMPLATE.md |
| 3 | AI Risk Assessment Records | 6.1, 8.2 | AI-RISK-REGISTER.md |
| 4 | AI Risk Treatment Plans | 6.1, 8.3 | AI-RISK-REGISTER.md |
| 5 | Statement of Applicability | 6.1.3 | STATEMENT-OF-APPLICABILITY.md |
| 6 | AI Objectives Documentation | 6.2 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 7 | Evidence of Competence | 7.2 | ANNEX-A-CONTROLS.md (A.4.2) |
| 8 | AI System Impact Assessments | 8.4 | AI-SYSTEM-IMPACT-ASSESSMENT.md |
| 9 | AI Lifecycle Records | 8.5 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
| 10 | Monitoring and Measurement Results | 9.1 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 11 | Internal Audit Records | 9.2 | INTERNAL-AUDIT-PROCEDURE.md |
| 12 | Management Review Records | 9.3 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 13 | Nonconformity and Corrective Action Records | 10.2 | AI-INCIDENT-RESPONSE-PROCEDURE.md |

---

## Standard Structure Reference

| Clause | Title | Key Requirements |
|--------|-------|-----------------|
| 4 | Context of the Organisation | Define scope, identify interested parties, understand AI context |
| 5 | Leadership | AI Policy, top management commitment, roles and responsibilities |
| 6 | Planning | Risk assessment, risk treatment, Statement of Applicability, objectives |
| 7 | Support | Resources, competence, awareness, communication, documented information |
| 8 | Operation | Risk assessment execution, risk treatment, ASIA, AI lifecycle management |
| 9 | Performance Evaluation | Monitoring, internal audit, management review |
| 10 | Improvement | Nonconformity management, corrective action, continual improvement |
| Annex A | Controls | 39 controls across 9 domains (A.2–A.10) |

---

## Framework Alignment

| Framework | Alignment |
|-----------|-----------|
| EU AI Act (2024) | All 39 controls mapped to relevant articles — see CONTROLS-MAPPING.md |
| NIST AI RMF 1.0 | Controls mapped to GOVERN, MAP, MEASURE, MANAGE functions |
| ISO/IEC 27001:2022 | Controls integrated with information security management |
| GDPR / UK GDPR | Privacy requirements embedded throughout data controls (A.7) |

---

## Certification

### Certification Bodies
Accredited bodies offering ISO 42001 certification include: BSI Group, Bureau Veritas, DNV, SGS, TUV, LRQA, NQA.

### Typical Timeline

| Stage | Duration |
|-------|----------|
| Gap Assessment | 2–4 weeks |
| Implementation | 6–12 months |
| Stage 1 Audit (document review) | 1–2 days |
| Stage 2 Audit (effectiveness) | 2–5 days |
| Certification Decision | 2–4 weeks post Stage 2 |

---

## About

**Ankit Uniyal** — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group

ISO/IEC 42001:2023 Lead Auditor. GRC and information security management practitioner. Experience across healthcare, technology, and financial services.

Website: ankituniyalprofile.com

---

## Disclaimer

This toolkit is provided for guidance purposes only. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text for definitive requirements. Templates must be adapted to your organisational context before use. The standard must be purchased from ISO or your national standards body.

---

## License

MIT License — free to use, adapt, and distribute with attribution.
