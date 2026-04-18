# AI Supplier Contract Clauses Template
## ISO/IEC 42001:2023 | Clause 8.4 / Annex A.2.5 / A.8.2

**Document ID:** AIMS-CONTRACT-001
**Version:** 1.0
**Owner:** Legal / AI Governance Lead
**Date:** ___________________________
**Review Cycle:** Annual

> **Legal Disclaimer:** These clauses are template starting points developed by an ISO 42001 Lead Auditor. They are NOT legal advice. All contractual provisions must be reviewed and approved by qualified legal counsel before use in actual contracts. Requirements vary by jurisdiction and sector.

---

## Purpose

This document provides standard AI governance clauses for inclusion in contracts with AI suppliers, AI vendors, and third parties that develop, supply, or operate AI systems on behalf of the organisation. It implements:
- ISO/IEC 42001:2023 Annex A.2.5 — Addressing AI considerations in contracts
- ISO/IEC 42001:2023 Annex A.8.2 — Supplier relationships for AI systems
- ISO/IEC 42001:2023 Clause 8.4 — Externally provided processes, products and services

---

## How to Use This Document

1. Select the relevant clauses for each supplier relationship based on the nature of the AI service
2. Adapt the clauses to the specific contract type and jurisdiction
3. Have all clauses reviewed by legal counsel before inclusion in contracts
4. Ensure clauses are proportionate to the AI risk tier of the supplier
5. Track which clauses are included in each supplier contract in `AI-SUPPLIER-RISK-REGISTER.md`

---

## Section A — Core AI Governance Clauses (Include in ALL AI supplier contracts)

### A.1 — AI System Identification and Documentation

**Clause A.1.1 — AI System Disclosure**
The Supplier shall, at contract commencement and upon any material change, provide the Customer with a written description of all AI systems, AI models, and AI-enabled features used in the provision of the Services, including: (a) the purpose of each AI system; (b) the type  of AI technology; (c) training data used; (d) known limitations; (e) EU AI Act risk class.

**Clause A.1.2 — Model Cards:** Supplier shall provide a model card for each AI system making decisions affecting individuals, updated within 30 days of material change.

---

## Section A — Core Clauses (ALL AI supplier contracts)

**A.2 — Fairness:** Supplier shall conduct fairness evaluations before deployment and notify Customer within 5 days of detecting material bias. Remediation plan within 15 days; implemented within 60 days.

**A.3 — Transparency:** Where AI interacts with end users, Supplier shall provide disclosure mechanisms. AI systems making decisions about individuals must support explanation on request.

**A.4 — Human Oversight:** Supplier shall ensure AI systems include a mechanism enabling Customer to override, suspend, or switch off AI decision-making.

**A.5 — Security:** Supplier shall implement AI-specific security measures including adversarial testing. Notify Customer within 48 hours of discovering any AI vulnerability.

**A.6 — Performance:** Supplier shall monitor for drift and notify Customer within 5 days of detecting performance degradation below agreed thresholds.

**A.7 — Incidents:** Supplier shall notify Customer of AI incidents within 24 hours and cooperate in investigation, remediation, and regulatory notification.

**A.8 — Change Management:** Supplier shall provide 30 days notice of material AI system changes. Customer may refuse changes that materially adversely affect Services.

---

## Section B — Data Protection (Where AI processes personal data)

**B.1 — Data Processing Agreement:** Processing of personal data in AI systems governed by DPA at Schedule [X].

**B.2 — Training Data:** Supplier shall not use Customer data for AI training without prior written consent.

**B.3 — Automated Decisions:** Supplier shall ensure compliance with GDPR Art. 22 and provide tools to fulfil data subject rights obligations.

---

## Section C — EU AI Act (High-risk AI systems)

**C.1 — Compliance Warranty:** Supplier warrants that high-risk AI systems have completed conformity assessment, technical documentation is maintained, and post-market monitoring is in place.

**C.2 — Audit Rights:** Customer may audit AI governance compliance on 30 days notice.

**C.3 — ISO 42001 [Optional]:** Supplier shall maintain ISO/IEC 42001:2023 certification throughout the term.

---

## Section D — Liability (Adapt with legal counsel)

**D.1 — AI Indemnity:** Supplier indemnifies Customer against losses from unlawfully discriminatory AI outputs, undisclosed security vulnerabilities, and material breach of documentation obligations.

**D.2 — Liability Cap:** Total liability not to exceed [AMOUNT]. Excludes death/personal injury, fraud, and non-excludable statutory liability.

---

## Supplier Risk Classification Schedule

| AI System | Risk Tier | EU AI Act Class | Applicable Sections |
|-----------|-----------|----------------|-------------------|
| [System 1] | Tier 1 | High-risk | A + B + C |
| [System 2] | Tier 2 | Limited-risk | A + B (if personal data) |
| [System 3] | Tier 3 | Minimal-risk | A (core) |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 8.4 / A.2.5 / A.8.2 — AI Supplier Contract Clauses | See root README.md for full index*
