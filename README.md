# 🤖 ISO/IEC 42001:2023 AI Governance Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ISO Standard](https://img.shields.io/badge/Standard-ISO%2FIEC%2042001%3A2023-blue)](https://www.iso.org/standard/81230.html)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Ankit%20Uniyal-green)](https://github.com/Ankit-Uniyal)

> *"AI is not just a technology decision — it's a governance imperative."*

**The most comprehensive open-source ISO/IEC 42001:2023 AI Governance Toolkit available.** Built by an ISO 42001 Lead Auditor for GRC professionals, AI governance practitioners, compliance leads, and organizations seeking certification.

This toolkit covers all 10 clauses, all 39 Annex A controls across 9 control domains, and every mandatory document required by the standard.

---

## 📋 How to Use This Toolkit

The files in this toolkit are designed to be used **in sequence**, following the ISO/IEC 42001:2023 implementation lifecycle. The order below mirrors the standard's clause structure and the recommended implementation journey — from understanding your context, through building your AIMS, to operating and auditing it.

> **Start here if you are new:** Read the [Implementation Roadmap](IMPLEMENTATION-ROADMAP.md) first to understand the 12-month journey, then work through each phase in order.

---

## 🗂️ Files in Correct Implementation Order

---

### PHASE 1 — UNDERSTAND & PLAN
*ISO 42001 Clauses 4 & 6 | Before you build anything, understand where you are and what you need*

---

#### 📁 File 1 — GAP-ASSESSMENT.md
**Use: Immediately — before any implementation begins**

| Field | Detail |
|-------|--------|
| **Purpose** | Baseline assessment of your current AI governance maturity against all ISO 42001 requirements |
| **Covers** | All Clauses 4–10 + all 39 Annex A controls across 9 domains (128 requirements total) |
| **Output** | Maturity score, gap list, prioritized remediation plan |
| **ISO 42001 Clause** | Clause 4 (Context), Clause 6 (Planning) |
| **Who completes it** | AI Governance Lead / GRC Lead / Consultant |
| **When to revisit** | Before Stage 1 certification audit; annually as part of management review |

**Why first:** You cannot plan what you have not measured. The gap assessment tells you which controls you already have in place, which need work, and which are not yet started — so you build an implementation plan based on facts, not assumptions.

---

#### 📁 File 2 — IMPLEMENTATION-ROADMAP.md
**Use: Phase 1 — after the gap assessment, to plan your implementation journey**

| Field | Detail |
|-------|--------|
| **Purpose** | 12-month phased implementation plan with milestones, deliverables, and resource estimates |
| **Covers** | 4 phases: Foundations → Core AIMS → Operational Controls → Audit & Certification |
| **Output** | Project plan, responsibility assignments, milestone tracker |
| **ISO 42001 Clause** | All clauses — cross-cutting planning document |
| **Who completes it** | AI Governance Lead / Project Manager |
| **When to revisit** | Monthly to track progress; quarterly to adjust plan |

**Why second:** The gap assessment tells you *what* to do. The roadmap tells you *how* and *when*. This is your project management tool for the entire implementation.

---

### PHASE 2 — ESTABLISH GOVERNANCE FOUNDATIONS
*ISO 42001 Clauses 4, 5 & 6 | Define scope, set policy, assign accountability*

---

#### 📁 File 3 — AIMS-POLICY-TEMPLATE.md
**Use: Phase 2 — first governance document to draft and get approved**

| Field | Detail |
|-------|--------|
| **Purpose** | Complete AI Management System Policy — the flagship governance document |
| **Covers** | Organizational AI commitment, ethical principles, roles, prohibited uses, scope, lifecycle requirements |
| **Output** | Approved, signed AI Policy ready for communication |
| **ISO 42001 Clause** | Clause 5.2 (AI Policy) |
| **Annex A Controls** | A.2.2 (AI Policy), A.2.3 (AI-Specific Policies) |
| **Who completes it** | AI Governance Lead; approved by CEO/Board |
| **When to revisit** | Annually; after scope changes or significant incidents |

**Why third:** The AI Policy is the instrument of top management commitment. Without it signed and communicated, you cannot claim your AIMS is established. Every other document flows from this policy.

---

#### 📁 File 4 — STATEMENT-OF-APPLICABILITY.md
**Use: Phase 2 — after the gap assessment and policy, before risk treatment**

| Field | Detail |
|-------|--------|
| **Purpose** | Mandatory SoA document — declares which of the 39 Annex A controls apply, why, and their implementation status |
| **Covers** | All 39 controls across Domains A.2–A.10; applicability, justification, status, and implementation reference |
| **Output** | Completed, approved SoA — a mandatory certification document |
| **ISO 42001 Clause** | Clause 6.1.3 (Statement of Applicability) — **MANDATORY** |
| **Annex A Controls** | All 39 controls |
| **Who completes it** | AI Governance Lead / CISO / DPO |
| **When to revisit** | When scope changes; when new AI systems come in scope; annually |

**Why fourth:** The SoA is one of the most scrutinized documents in a certification audit. It must be completed before you finalize risk treatment, because it determines *which* controls you are committing to implement.

---

#### 📁 File 5 — ANNEX-A-CONTROLS.md
**Use: Phase 2 onwards — the implementation reference for every Annex A control**

| Field | Detail |
|-------|--------|
| **Purpose** | Control-by-control implementation, audit, and evidence guide for all 39 Annex A controls |
| **Covers** | All 39 controls: What It Means · Why It Matters · How to Implement · Documents to Prepare · How to Audit · Evidence Required · Common Gaps · Cross-References (EU AI Act, NIST AI RMF, ISO 27001) |
| **Output** | Implementation guidance; audit checklist; document master list; interview question bank |
| **ISO 42001 Clause** | Clause 6.1.3 + all Annex A domains |
| **Annex A Controls** | All 39 controls across A.2–A.10 |
| **Who uses it** | Implementers (how-to guidance) · Auditors (audit procedures) · GRC teams (evidence checklists) |
| **When to revisit** | Continuously during implementation; before internal/external audits |

**Why fifth:** Once you know which controls apply (SoA), this document tells you *exactly* how to implement each one, what documents to create, and how they will be audited. It is the operational instruction manual for the entire Annex A.

---

### PHASE 3 — RISK MANAGEMENT
*ISO 42001 Clauses 6 & 8 | Identify, assess, and treat AI risks*

---

#### 📁 File 6 — AI-RISK-REGISTER.md
**Use: Phase 3 — concurrent with policy establishment, maintained throughout AIMS lifecycle**

| Field | Detail |
|-------|--------|
| **Purpose** | AI risk register with 44 pre-populated risks across 8 categories, scoring matrix, and risk treatment log |
| **Covers** | Model risks · Data risks · Operational risks · Ethical/fairness risks · Security risks · Legal/regulatory risks · Third-party risks · Reputational risks |
| **Output** | Live risk register; risk treatment plans; residual risk records |
| **ISO 42001 Clause** | Clause 6.1 (Risk assessment), Clause 8.2 (Risk assessment execution), Clause 8.3 (Risk treatment) |
| **Annex A Controls** | A.5.2 (ASIA), A.5.4 (Use of assessment results) |
| **Who completes it** | AI Risk Manager / AI Governance Lead |
| **When to revisit** | Quarterly; after every ASIA; after every significant incident; annually |

**Why sixth:** Risk assessment drives risk treatment, which drives control selection. The risk register is the living backbone of your AIMS — every ASIA finding, every incident, every audit finding should flow back into it.

---

#### 📁 File 7 — AI-SYSTEM-IMPACT-ASSESSMENT.md
**Use: Phase 3 & ongoing — before every AI system deployment**

| Field | Detail |
|-------|--------|
| **Purpose** | 10-part AI System Impact Assessment (ASIA) template covering benefits, harms, fundamental rights, bias, privacy, safety, societal impacts, and human oversight |
| **Covers** | Pre-deployment impact assessment for each AI system in scope |
| **Output** | Completed ASIA per AI system; ASIA register |
| **ISO 42001 Clause** | Clause 8.4 (AI system impact assessment) — **MANDATORY** |
| **Annex A Controls** | A.5.2 (ASIA), A.5.3 (Societal/ethical impact), A.5.4 (Use of results) |
| **Who completes it** | AI Risk Manager / Model Owner; reviewed by DPO; approved by AI Governance Lead |
| **When to revisit** | Before every deployment; after significant system changes; when monitoring reveals unexpected impacts |

**Why seventh:** The ASIA is the central operational control linking risk assessment to deployment decisions. It must be completed *before* deployment — not after. This is one of the most commonly cited nonconformities in ISO 42001 audits.

---

### PHASE 4 — BUILD OPERATIONAL CONTROLS
*ISO 42001 Clause 8 | The procedures and processes that make governance real*

---

#### 📁 File 8 — AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md
**Use: Phase 4 — implement before any new AI systems are built or deployed**

| Field | Detail |
|-------|--------|
| **Purpose** | End-to-end AI lifecycle governance procedure from design to decommissioning |
| **Covers** | Design governance gates · Development controls · Model documentation (model cards) · Bias evaluation · Adversarial testing · Pre-deployment testing · Deployment authorization · Production monitoring · Drift detection · Decommissioning |
| **Output** | Controlled AI development and deployment procedure; governance gate records; model card template |
| **ISO 42001 Clause** | Clause 8.5 (AI system lifecycle) |
| **Annex A Controls** | A.6.1.1 – A.6.5.1 (all 12 lifecycle controls) |
| **Who uses it** | AI/ML Engineers · Data Scientists · MLOps · Product Owners · AI Governance Lead |
| **When to revisit** | Annually; when new AI development methodologies are adopted; after lifecycle-related audit findings |

**Why eighth:** The lifecycle procedure embeds governance into the work of building AI. Without it, developers make ad hoc decisions at every stage. With it, responsible AI is the process, not an afterthought.

---

#### 📁 File 9 — AI-INCIDENT-RESPONSE-PROCEDURE.md
**Use: Phase 4 — establish before any AI system goes into production**

| Field | Detail |
|-------|--------|
| **Purpose** | 7-phase AI incident response lifecycle — detection, classification, containment, investigation, notification, remediation, and post-incident review |
| **Covers** | AI-specific incident types (bias, errors, security, performance, privacy) · Severity classification · Escalation · Regulatory notification · Lessons learned |
| **Output** | Incident response procedure; incident log; post-incident review records |
| **ISO 42001 Clause** | Clause 10.2 (Nonconformity and corrective action) |
| **Annex A Controls** | A.8.5 (Incident communication), A.9.4 (Error handling), A.6.4.1 (Operation monitoring) |
| **Who uses it** | Operations · AI Governance Lead · CISO · DPO · Legal · Communications |
| **When to revisit** | After every AI incident; annually; when regulatory requirements change |

**Why ninth:** You need incident response *before* an incident happens. AI incidents behave differently from IT incidents — this procedure is purpose-built for AI-specific failure modes including silent failures, bias events, and hallucination incidents.

---

#### 📁 File 10 — AI-SUPPLIER-ASSESSMENT.md
**Use: Phase 4 — before adopting any third-party AI system, API, or model**

| Field | Detail |
|-------|--------|
| **Purpose** | Third-party AI due diligence template covering governance maturity, bias, security, privacy, regulatory compliance, and contract requirements |
| **Covers** | Pre-adoption risk assessment for third-party AI · Supplier governance review · DPA requirements · Contract clause requirements |
| **Output** | Completed supplier assessment per third-party AI; approval decision record |
| **ISO 42001 Clause** | Clause 8.1 (Operational planning and control) |
| **Annex A Controls** | A.10.2 (Third-party AI risk assessment), A.10.3 (AI supplier contracts), A.10.4 (Customer AI governance) |
| **Who completes it** | AI Risk Manager / Procurement / Legal / DPO |
| **When to revisit** | Before every new third-party AI adoption; annually for existing high-risk suppliers |

**Why tenth:** Most organizations use far more third-party AI than they build. Every SaaS product with AI, every cloud AI API, every adopted open-source model needs assessment before use. This template makes that process consistent and auditable.

---

### PHASE 5 — MONITOR & MEASURE
*ISO 42001 Clause 9 | Internal controls for performance evaluation*

---

#### 📁 File 11 — INTERNAL-AUDIT-PROCEDURE.md
**Use: Phase 5 — before Stage 2 certification audit; then on an ongoing annual cycle**

| Field | Detail |
|-------|--------|
| **Purpose** | Complete internal audit framework — audit program, clause-by-clause and Annex A checklist, audit report template, and corrective action tracking |
| **Covers** | All Clauses 4–10 + all 39 Annex A controls; audit planning, execution, and follow-up |
| **Output** | Internal audit program; completed audit checklists; audit reports; corrective action register |
| **ISO 42001 Clause** | Clause 9.2 (Internal audit) — **MANDATORY** |
| **Annex A Controls** | All 39 controls |
| **Who uses it** | Internal auditors · AI Governance Lead · External consultants conducting readiness assessments |
| **When to use** | At least annually; before each certification audit; after major AIMS changes |

**Why eleventh:** Internal audits are mandatory under Clause 9.2. They are also your rehearsal for the certification audit. Running a rigorous internal audit using this procedure — and referencing ANNEX-A-CONTROLS.md for the detailed audit tests — will surface gaps before the certification body does.

---

#### 📁 File 12 — MANAGEMENT-REVIEW-TEMPLATE.md
**Use: Phase 5 — annually (minimum); linked to the audit and risk review cycle**

| Field | Detail |
|-------|--------|
| **Purpose** | Full management review template with all 13 required inputs, KPI dashboard, risk review, incident review, and output decisions |
| **Covers** | All mandatory management review inputs per Clause 9.3; AI performance metrics; AIMS improvement decisions |
| **Output** | Completed management review record; AIMS improvement decisions; updated objectives |
| **ISO 42001 Clause** | Clause 9.3 (Management review) — **MANDATORY** |
| **Annex A Controls** | N/A (clause-level requirement) |
| **Who completes it** | Top management; facilitated by AI Governance Lead |
| **When to use** | At least annually; output feeds into next cycle's planning |

**Why twelfth:** Management review is mandatory and is one of the first things a certification auditor will check. It is also the governing body meeting where the AIMS is reviewed, objectives are reset, and continual improvement decisions are made — the steering wheel of the AIMS.

---

### PHASE 6 — REFERENCE & CROSS-FRAMEWORK ALIGNMENT
*Supporting documents used throughout the lifecycle*

---

#### 📁 File 13 — CONTROLS-MAPPING.md
**Use: Throughout — whenever cross-framework alignment is needed**

| Field | Detail |
|-------|--------|
| **Purpose** | Cross-reference of all 39 Annex A controls mapped to EU AI Act articles, NIST AI RMF functions, and ISO 27001 controls |
| **Covers** | Full mapping of ISO 42001 Annex A ↔ EU AI Act ↔ NIST AI RMF 1.0 ↔ ISO/IEC 27001:2022 |
| **Output** | Evidence reuse map; regulatory alignment documentation; multi-framework compliance planning |
| **ISO 42001 Clause** | Clause 6.1.3 (Controls mapping) |
| **Annex A Controls** | All 39 controls |
| **Who uses it** | GRC teams managing multiple frameworks · Legal/Compliance · Certification preparation teams · Organizations subject to EU AI Act |
| **When to use** | During SoA completion · During regulatory gap analysis · When mapping evidence to multiple frameworks |

**Why thirteenth:** Most organizations subject to ISO 42001 are also navigating the EU AI Act, NIST AI RMF, or ISO 27001. This mapping eliminates duplicated effort — evidence gathered for one framework often satisfies another. It is also essential for demonstrating regulatory alignment to auditors and customers.

---

#### 📁 File 14 — ANNEX-A-CONTROLS.md *(also listed in Phase 2)*
> *Already referenced in Phase 2 (File 5). This document is a continuous reference used in every phase.*

---

## 🗺️ Implementation Sequence — Visual Summary

```
PHASE 1 — UNDERSTAND & PLAN
├── 1. GAP-ASSESSMENT.md              ← Start here. Measure your baseline.
└── 2. IMPLEMENTATION-ROADMAP.md      ← Plan your 12-month journey.

PHASE 2 — GOVERNANCE FOUNDATIONS
├── 3. AIMS-POLICY-TEMPLATE.md        ← Get top management commitment signed.
├── 4. STATEMENT-OF-APPLICABILITY.md  ← Declare which controls apply (MANDATORY).
└── 5. ANNEX-A-CONTROLS.md            ← How to implement every control (reference throughout).

PHASE 3 — RISK MANAGEMENT
├── 6. AI-RISK-REGISTER.md            ← Identify and treat AI risks.
└── 7. AI-SYSTEM-IMPACT-ASSESSMENT.md ← Assess each AI system before deployment (MANDATORY).

PHASE 4 — OPERATIONAL CONTROLS
├── 8. AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md  ← Govern AI from design to retirement.
├── 9. AI-INCIDENT-RESPONSE-PROCEDURE.md     ← Respond to AI failures and incidents.
└── 10. AI-SUPPLIER-ASSESSMENT.md            ← Assess third-party AI before adoption.

PHASE 5 — MONITOR & MEASURE
├── 11. INTERNAL-AUDIT-PROCEDURE.md   ← Audit your AIMS (MANDATORY).
└── 12. MANAGEMENT-REVIEW-TEMPLATE.md ← Top management review (MANDATORY).

PHASE 6 — REFERENCE
└── 13. CONTROLS-MAPPING.md           ← Cross-map to EU AI Act, NIST, ISO 27001.
```

---

## 📌 Mandatory Documents Checklist

ISO/IEC 42001:2023 requires the following documents as a minimum. All are covered in this toolkit.

| # | Document | Clause | File in This Toolkit |
|---|----------|--------|---------------------|
| 1 | AIMS Scope Statement | 4.3 | Included in AIMS-POLICY-TEMPLATE.md |
| 2 | AI Policy | 5.2 | AIMS-POLICY-TEMPLATE.md |
| 3 | AI Risk Assessment Records | 6.1, 8.2 | AI-RISK-REGISTER.md |
| 4 | AI Risk Treatment Plans | 6.1, 8.3 | AI-RISK-REGISTER.md |
| 5 | AI Objectives Documentation | 6.2 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 6 | **Statement of Applicability** ⚠️ | 6.1.3 | STATEMENT-OF-APPLICABILITY.md |
| 7 | Evidence of Competence | 7.2 | Covered in ANNEX-A-CONTROLS.md (A.4.2) |
| 8 | **AI System Impact Assessments** ⚠️ | 8.4 | AI-SYSTEM-IMPACT-ASSESSMENT.md |
| 9 | AI Lifecycle Records | 8.5 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |
| 10 | Monitoring and Measurement Results | 9.1 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 11 | **Internal Audit Records** ⚠️ | 9.2 | INTERNAL-AUDIT-PROCEDURE.md |
| 12 | **Management Review Records** ⚠️ | 9.3 | MANAGEMENT-REVIEW-TEMPLATE.md |
| 13 | Nonconformity and Corrective Action Records | 10.2 | AI-INCIDENT-RESPONSE-PROCEDURE.md |

> ⚠️ These four documents are the most scrutinized in certification audits. Do not proceed to Stage 2 without them complete and approved.

---

## 🔗 Framework Alignment

| Framework | Alignment |
|-----------|-----------|
| EU AI Act (2024) | All 39 controls mapped to relevant EU AI Act articles — see CONTROLS-MAPPING.md |
| NIST AI RMF 1.0 | Controls mapped to GOVERN, MAP, MEASURE, MANAGE functions |
| ISO/IEC 27001:2022 | Controls integrated with information security management |
| GDPR / UK GDPR | Privacy requirements embedded throughout data controls (A.7) |
| OECD AI Principles | Ethical AI principles aligned with A.2 and A.9 controls |

---

## 📖 ISO/IEC 42001:2023 Standard Structure

| Clause | Title | Key Requirements |
|--------|-------|-----------------|
| 4 | Context of the Organization | Define scope, identify interested parties, understand AI context |
| 5 | Leadership | AI Policy, top management commitment, roles and responsibilities |
| 6 | Planning | AI risk assessment, risk treatment, Statement of Applicability, AI objectives |
| 7 | Support | Resources, competence, awareness, communication, documented information |
| 8 | Operation | Risk assessment execution, risk treatment, ASIA, AI lifecycle management |
| 9 | Performance Evaluation | Monitoring, internal audit, management review |
| 10 | Improvement | Nonconformity management, corrective action, continual improvement |
| Annex A | Controls | 39 controls across 9 domains — see ANNEX-A-CONTROLS.md and STATEMENT-OF-APPLICABILITY.md |

---

## 🚀 Quick Start by Role

### For Organizations Starting ISO 42001 Implementation
1. **Read** [IMPLEMENTATION-ROADMAP.md](IMPLEMENTATION-ROADMAP.md) — understand the 12-month journey
2. **Measure** using [GAP-ASSESSMENT.md](GAP-ASSESSMENT.md) — know your baseline
3. **Commit** top management using [AIMS-POLICY-TEMPLATE.md](AIMS-POLICY-TEMPLATE.md)
4. **Declare** your controls using [STATEMENT-OF-APPLICABILITY.md](STATEMENT-OF-APPLICABILITY.md)
5. **Implement** each control using [ANNEX-A-CONTROLS.md](ANNEX-A-CONTROLS.md)
6. **Manage risks** using [AI-RISK-REGISTER.md](AI-RISK-REGISTER.md)
7. **Assess systems** using [AI-SYSTEM-IMPACT-ASSESSMENT.md](AI-SYSTEM-IMPACT-ASSESSMENT.md)

### For GRC Professionals Auditing AI Governance
1. **Reference** [ANNEX-A-CONTROLS.md](ANNEX-A-CONTROLS.md) for control-by-control audit procedures and interview questions
2. **Execute** audits using [INTERNAL-AUDIT-PROCEDURE.md](INTERNAL-AUDIT-PROCEDURE.md)
3. **Verify** coverage using [GAP-ASSESSMENT.md](GAP-ASSESSMENT.md)
4. **Map** findings to frameworks using [CONTROLS-MAPPING.md](CONTROLS-MAPPING.md)

### For AI Teams Building Responsible AI
1. **Follow** [AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md](AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md) for governance-embedded development
2. **Complete** [AI-SYSTEM-IMPACT-ASSESSMENT.md](AI-SYSTEM-IMPACT-ASSESSMENT.md) before every deployment
3. **Reference** [ANNEX-A-CONTROLS.md](ANNEX-A-CONTROLS.md) for data, bias, testing, and monitoring requirements

### For Organizations Managing Third-Party AI
1. **Assess** every third-party AI using [AI-SUPPLIER-ASSESSMENT.md](AI-SUPPLIER-ASSESSMENT.md)
2. **Reference** A.10 controls in [ANNEX-A-CONTROLS.md](ANNEX-A-CONTROLS.md) for contract and customer requirements
3. **Map** supplier obligations using [CONTROLS-MAPPING.md](CONTROLS-MAPPING.md)

---

## 🏆 Certification Journey

### Certification Bodies (ISO 42001)
Accredited CBs offering ISO 42001 certification include:
**BSI Group | Bureau Veritas | DNV | SGS | TÜV | LRQA | NQA**

### Timeline to Certification
| Stage | Activity | Typical Duration |
|-------|----------|-----------------|
| Gap Assessment | Using GAP-ASSESSMENT.md | 2–4 weeks |
| Implementation | Using the full toolkit in sequence | 6–12 months |
| Stage 1 Audit | Document review by certification body | 1–2 days |
| Stage 2 Audit | Effectiveness audit by certification body | 2–5 days |
| Certification Decision | CB review and decision | 2–4 weeks post Stage 2 |

---

## 👤 About the Author

**Ankit Uniyal** — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group

🌐 [ankituniyalprofile.com](https://ankituniyalprofile.com)

- ISO/IEC 42001:2023 Lead Auditor
- Certified Practitioner in AI governance, GRC, and information security management
- Experience across healthcare, technology, and financial services

---

## ⚠️ Disclaimer

This toolkit is provided for guidance purposes only. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text for definitive requirements. Organizations should seek qualified professional advice for their specific implementation context. Templates must be adapted to your organizational context before use. The ISO/IEC 42001:2023 standard must be purchased from ISO or your national standards body.

---

## 📄 License

MIT License — free to use, adapt, and distribute with attribution.

If this toolkit helps your AI governance work, please ⭐ **star the repository** and share with the GRC and AI governance community.
