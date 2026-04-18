# Legal and Regulatory Requirements Register
## ISO/IEC 42001:2023 | Clause 4.2

**Document ID:** AIMS-LEGAL-001
**Version:** 1.0
**Owner:** AI Governance Lead / Data Privacy Officer
**Date:** ___________________________
**Review Cycle:** Annual and upon regulatory change

---

## Purpose

This register identifies all legal, regulatory, contractual, and voluntary obligations that apply to the organisation's AI systems and AI Management System (AIMS). It feeds directly into risk assessments, control selection, and the Statement of Applicability.

Required by ISO/IEC 42001:2023 Clause 4.2 — Interested parties and their requirements.

---

## How to Use This Register

1. Review all entries at least annually and after any regulatory change
2. Mark new obligations as they are identified
3. Link each obligation to the controls or documents that address it
4. Use this register as input to the AI risk assessment (Clause 6.1.2)
5. Ensure the Statement of Applicability reflects all applicable obligations

---

## Section 1 — International AI Standards

| # | Obligation | Issuing Body | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|-------------|--------------|----------|--------------|-------|------------|
| 1.1 | ISO/IEC 42001:2023 — AI Management Systems | ISO/IEC | All in-scope AI systems | Yes — certification | Full AIMS implementation | AI Gov Lead | Annual |
| 1.2 | ISO/IEC 23894:2023 — AI Risk Management | ISO/IEC | Risk assessment process | Voluntary (best practice) | AI-RISK-ASSESSMENT-PROCESS.md | Risk Manager | Annual |
| 1.3 | ISO/IEC 25059 — Quality of AI systems | ISO/IEC | AI system performance | Voluntary | AI-PERFORMANCE-MONITORING-PLAN.md | AI Gov Lead | Annual |
| 1.4 | ISO/IEC TR 24368 — AI ethical concerns | ISO/IEC | Ethics framework | Voluntary | AI-ETHICS-FRAMEWORK.md | AI Gov Lead | Annual |

---

## Section 2 — EU and European Regulations

| # | Obligation | Regulation | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|-----------|--------------|----------|--------------|-------|------------|
| 2.1 | EU AI Act — Prohibited AI practices (Art. 5) | EU Regulation 2024/1689 | All AI systems | Yes — if EU nexus | AI-SYSTEM-IMPACT-ASSESSMENT.md, AI use policy | DPO / Legal | Annual |
| 2.2 | EU AI Act — High-risk AI requirements (Art. 9–15) | EU Regulation 2024/1689 | High-risk AI systems | Yes — if applicable | OPERATIONAL-CONTROLS-REGISTER.md, AI-MODEL-CARD-TEMPLATE.md | AI Gov Lead | Annual |
| 2.3 | EU AI Act — Transparency obligations (Art. 50) | EU Regulation 2024/1689 | AI interacting with individuals | Yes | AWARENESS-COMMUNICATION-PLAN.md | DPO | Annual |
| 2.4 | GDPR — Lawful basis for processing (Art. 6) | EU Regulation 2016/679 | AI using personal data | Yes | INTERESTED-PARTIES-REGISTER.md, Privacy notices | DPO | Annual |
| 2.5 | GDPR — Automated decision-making (Art. 22) | EU Regulation 2016/679 | AI making decisions about individuals | Yes | AI-SYSTEM-IMPACT-ASSESSMENT.md | DPO | Annual |
| 2.6 | GDPR — Data Protection Impact Assessment | EU Regulation 2016/679 | High-risk processing activities | Yes | AI-SYSTEM-IMPACT-ASSESSMENT.md | DPO | Per system |
| 2.7 | NIS2 Directive — Security of AI systems | EU Directive 2022/2555 | If organisation is OES/DSP | Yes — if applicable | OPERATIONAL-CONTROLS-REGISTER.md | CISO | Annual |

---

## Section 3 — UK Regulations (Post-Brexit)

| # | Obligation | Regulation | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|-----------|--------------|----------|--------------|-------|------------|
| 3.1 | UK GDPR — Data protection for AI | UK GDPR / DPA 2018 | AI using personal data (UK operations) | Yes | Same as GDPR controls | DPO | Annual |
| 3.2 | ICO AI guidance | ICO | AI processing personal data in UK | Yes — regulatory guidance | AI-SYSTEM-IMPACT-ASSESSMENT.md | DPO | Annual |
| 3.3 | UK AI Regulation (proposed) | UK Government | Future obligation — monitor | Pending | Track via regulatory horizon scan | AI Gov Lead | Quarterly |

---

## Section 4 — Sector-Specific Regulations

| # | Obligation | Regulation | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|-----------|--------------|----------|--------------|-------|------------|
| 4.1 | FCA AI guidance (financial services) | FCA / PRA | If financial services sector | Yes — if applicable | Risk controls, model governance | Risk Manager | Annual |
| 4.2 | MHRA AI as medical device | MHRA / MDR | If AI is medical device | Yes — if applicable | Regulatory classification review | Legal | Annual |
| 4.3 | Equality Act 2010 — AI and discrimination | UK Equality Act | AI affecting employment or services | Yes | AI-SYSTEM-IMPACT-ASSESSMENT.md | HR / Legal | Annual |
| 4.4 | [Sector Regulation] | [Body] | [AI use case] | [Y/N] | [Controls] | [Owner] | [Date] |

---

## Section 5 — US Regulations (if applicable)

| # | Obligation | Regulation | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|-----------|--------------|----------|--------------|-------|------------|
| 5.1 | NIST AI RMF 1.0 | NIST | AI risk management | Voluntary (federal context) | 11-CONTROLS-MAPPING.md | AI Gov Lead | Annual |
| 5.2 | Executive Order 14110 — Safe AI | US Executive Order | Federal AI use | Applicable if US federal | AI governance programme | AI Gov Lead | Annual |
| 5.3 | CCPA / CPRA — AI and personal data | California law | CA residents' data | Yes — if applicable | DPO controls | DPO | Annual |
| 5.4 | EEOC AI guidance — hiring AI | EEOC | HR / recruitment AI | Yes — if applicable | AI-SYSTEM-IMPACT-ASSESSMENT.md | HR / Legal | Annual |

---

## Section 6 — Contractual Obligations

| # | Obligation | Source | Applicability | Binding? | How Addressed | Owner | Next Review |
|---|-----------|--------|--------------|----------|--------------|-------|------------|
| 6.1 | AI provisions in customer contracts | Customer agreements | All customer-facing AI | Yes — contractual | AI-SUPPLIER-ASSESSMENT.md (mirror clauses) | Legal | Per contract |
| 6.2 | AI provisions in supplier contracts | Supplier agreements | Third-party AI use | Yes — contractual | AI-SUPPLIER-ASSESSMENT.md | Legal | Per contract |
| 6.3 | ISO 42001 certification requirements | Certification body | Full AIMS scope | Yes — certification | Full AIMS | AI Gov Lead | Annual |
| 6.4 | [Contract Name] | [Party] | [Scope] | Yes | [Controls] | [Owner] | [Date] |

---

## Section 7 — Voluntary Commitments

| # | Commitment | Source | Why Adopted | How Addressed | Owner | Next Review |
|---|-----------|--------|------------|--------------|-------|------------|
| 7.1 | EU AI Pact (voluntary) | European Commission | Proactive compliance ahead of EU AI Act | AI governance programme | AI Gov Lead | Annual |
| 7.2 | OECD AI Principles | OECD | Ethical AI alignment | AI-ETHICS-FRAMEWORK.md | AI Gov Lead | Annual |
| 7.3 | UNESCO AI Ethics Recommendation | UNESCO | Global ethical standard | AI-ETHICS-FRAMEWORK.md | AI Gov Lead | Annual |
| 7.4 | [Commitment Name] | [Source] | [Reason] | [Document] | [Owner] | [Date] |

---

## Regulatory Horizon Scanning

Track upcoming regulatory changes that may affect your AIMS obligations:

| Regulation | Status | Expected Date | Potential Impact | Action Required |
|-----------|--------|--------------|-----------------|----------------|
| EU AI Act — full application | Enacted | Aug 2026 (most provisions) | High — high-risk AI systems | Gap assessment against Title III requirements |
| UK AI Regulation Bill | Proposed | TBC | Medium | Monitor; update register when enacted |
| DORA (Digital Operational Resilience) | In force Jan 2025 | Active | Medium — if financial services | Review IT/AI resilience controls |
| [Regulation] | [Status] | [Date] | [Impact] | [Action] |

---

## Review and Approval

| Role | Name | Date | Sign-off |
|------|------|------|---------|
| DPO / Legal | | | |
| AI Governance Lead | | | |
| CEO / Top Management | | | |

---

## Review History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | | Initial issue | |
| | | | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 4.2 — Legal and Regulatory Requirements | See root README.md for full index*
