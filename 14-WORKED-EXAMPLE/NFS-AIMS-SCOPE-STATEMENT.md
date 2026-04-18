# AIMS Scope Statement — Worked Example

## ISO/IEC 42001:2023 | Clause 4.3 | FICTIONAL REFERENCE ONLY

**Document ID:** NFS-AIMS-SCOPE-001
**Version:** 1.2 | **Owner:** Chief Risk Officer | **Date:** 14 March 2025 | **Review Cycle:** Annual

> **FICTIONAL EXAMPLE:** This document is a completed worked example for the fictional organisation Nexus Financial Services Ltd. It is for educational reference only and does not represent any real organisation, product, or compliance status.

---

## 1. Organisation Overview

**Organisation Name:** Nexus Financial Services Ltd (NFS)
**Registered Address:** 12 Exchange Square, Manchester, M2 7BL, United Kingdom
**Company Number:** 04782193
**FCA Reference:** 789234
**Industry:** Retail banking and consumer lending
**Size:** Approximately 3,200 employees across 14 UK branch locations

NFS provides personal loans, mortgages, credit cards, and current accounts to approximately 860,000 retail customers across the United Kingdom. NFS operates as both a data controller and data processor under UK GDPR and is authorised and regulated by the Financial Conduct Authority (FCA).

---

## 2. AIMS Scope Statement

The scope of NFS's AI Management System (AIMS) is:

> **"The development, deployment, operation, monitoring, and continual improvement of the CreditIQ v2.1 automated credit scoring and loan decisioning system, including all supporting data pipelines, model governance processes, and human review mechanisms, as operated by the Retail Credit Risk division of Nexus Financial Services Ltd from its Manchester headquarters."**

This scope is bounded to CreditIQ v2.1 as the primary in-scope AI system for the initial AIMS certification. Expansion to additional AI systems (fraud detection, customer service chatbot) is planned for Phase 2 (Q4 2026).

---

## 3. In-Scope AI Systems

| AI System | Version | Purpose | Risk Tier | Deployment Model |
|---|---|---|---|---|
| CreditIQ | v2.1 | Automated credit scoring and loan approval/rejection decisions for personal loans up to £50,000 | High Risk (EU AI Act Annex III) | On-premise (NFS data centre, Manchester) |

---

## 4. In-Scope Organisational Units

| Unit | Role in AIMS |
|---|---|
| Retail Credit Risk Division | AI system owner and primary operator |
| Data Science & AI Team (8 FTE) | Model development, retraining, performance monitoring |
| IT Operations | Infrastructure, security, deployment pipeline |
| Legal & Compliance | Regulatory oversight, FCA reporting, GDPR compliance |
| Internal Audit | Independent AIMS audit (annual) |
| Human Review Panel | Mandatory human oversight for declined/borderline cases |

**Out of Scope (explicitly excluded):**
- FraudGuard v3.0 (fraud detection AI) — planned for Phase 2
- Aria chatbot (customer service) — not yet assessed
- Third-party scoring systems used by mortgage partners
- Manual underwriting processes not involving AI

---

## 5. Internal and External Context

### 5.1 Internal Context

| Factor | Description |
|---|---|
| Strategic objective | Increase personal loan approval speed from 48 hours to under 4 hours while maintaining credit quality |
| Risk appetite | Low tolerance for model bias; medium tolerance for model performance degradation |
| Existing governance | ISO 27001:2022 certified (cert. no. IS-88234); DORA compliance project underway |
| Organisational culture | Risk-aware; board-level AI ethics committee established Q1 2024 |
| Constraints | Legacy core banking system (Temenos T24) limits real-time data feeds; model retraining cycle is quarterly |

### 5.2 External Context

| Factor | Description |
|---|---|
| Regulatory | FCA Consumer Duty (effective Jul 2023); UK GDPR Article 22 (automated decisions); EU AI Act (high-risk, cross-border product sales) |
| Competitive | Three major UK banks have deployed similar AI scoring systems; speed-to-decision is a key differentiator |
| Technology | Increasing availability of open-source LLM tools creates new risk vectors for future AI systems |
| Societal | Growing public concern about algorithmic bias in financial services following FCA Fairness in Finance report (2024) |
| Economic | Cost-of-living crisis increases default risk in training data; model may underperform in novel economic conditions |

---

## 6. Interested Parties

| Interested Party | Interest / Expectation | Relevance to AIMS |
|---|---|---|
| FCA (regulator) | Fair outcomes for consumers; explainability of automated decisions; Consumer Duty compliance | Mandatory — regulatory oversight |
| UK ICO | GDPR Art.22 compliance; data minimisation; right to explanation | Mandatory — data protection |
| Retail customers | Fair credit decisions; right to human review; transparent criteria | Mandatory — direct impact |
| NFS Board of Directors | Risk management; reputational protection; competitive advantage | Mandatory — governance oversight |
| NFS AI Ethics Committee | Ethical deployment; bias monitoring; alignment with NFS AI Principles | Internal governance |
| Data Science Team | Clear model governance; defined retraining triggers; tooling support | Internal operators |
| Credit Risk Officers | Reliable system output; clear escalation paths; model explainability | Internal users |
| Cloud/infrastructure suppliers | Security requirements; uptime SLAs; data residency | Supply chain |
| External auditors (BSI) | Evidence of AIMS implementation; documented controls; audit trail | Certification body |

---

## 7. Scope Boundaries and Interfaces

### 7.1 System Boundaries

```
[Customer Application] --> [NFS Loan Portal] --> [CreditIQ v2.1 API]
                                                        |
                                                                                      +-------------------------+-------------------------+
                                                                                                                    |                         |                         |
                                                                                                                                        [Credit Bureau Feed]    [Internal Transaction Data]    [Fraud Score Feed]
                                                                                                                                                            (Experian, Equifax)      (NFS Core Banking T24)        (FraudGuard v3.0)
                                                                                                                                                                                          |                         |                         |
                                                                                                                                                                                                                        +-------------------------+-------------------------+
                                                                                                                                                                                                                                                                                |
                                                                                                                                                                                                                                                                                                                              [Decision Output]
                                                                                                                                                                                                                                                                                                                                                                                      |
                                                                                                                                                                                                                                                                                                                                                                                                                    +-------------------------+-------------------------+
                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                   |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      [Approved: Automated]                            [Declined/Borderline:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          (score >= 720)                                    Human Review Panel]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ```
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ### 7.2 Interfaces with Other Management Systems
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Interface | System | Integration Point |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |---|---|---|
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Information security | ISO 27001 ISMS | Shared risk register; model data classified under IS asset register |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Data protection | UK GDPR programme | DPIA for CreditIQ maintained by DPO; shared with AIMS |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Business continuity | BCP/DR plan | CreditIQ failover procedure documented in BCP |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Operational risk | FCA ICARA process | AI risk included in ICARA operational risk assessment |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ---
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ## 8. Exclusions and Justifications
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Exclusion | Justification |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |---|---|
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Clause 8.6 (AI system acquisition) | NFS develops CreditIQ in-house; no third-party AI model acquisition in scope |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | FraudGuard v3.0 | Separate risk profile; Phase 2 AIMS expansion planned Q4 2026 |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mortgage AI tools (third-party) | Operated by partner organisations; NFS is data processor only; separate DPA in place |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ---
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ## 9. Scope Approval
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Role | Name | Signature | Date |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |---|---|---|---|
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Chief Risk Officer | Sarah Mitchell | *[signed]* | 14 March 2025 |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Chief Executive Officer | James Okafor | *[signed]* | 17 March 2025 |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Head of AI Governance | Priya Sharma | *[signed]* | 14 March 2025 |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | External AIMS Consultant | Dr. Wei Chen (BSI) | *[signed]* | 20 March 2025 |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ---
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ## Review History
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Version | Date | Changes | Approved By |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |---|---|---|---|
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.0 | 02 Sep 2024 | Initial scope drafted | S. Mitchell |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.1 | 10 Jan 2025 | Added EU AI Act external context; updated interested parties | P. Sharma |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.2 | 14 Mar 2025 | Scope boundary diagram added; exclusions formalised | S. Mitchell |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ---
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          *ISO/IEC 42001:2023 AI Governance Toolkit | Worked Example — Clause 4.3 | See root README.md for full index*
