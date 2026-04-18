# AI Risk Assessment Process
## ISO/IEC 42001:2023 | Clause 6.1.2 — Documented Process

**Document ID:** AIMS-RISKPROC-001
**Version:** 1.0
**Owner:** Risk Manager / AI Governance Lead
**Approved by:** ___________________________
**Date:** ___________________________
**Review Cycle:** Annual or upon significant change to AI systems or risk environment

---

## 1. Purpose

This document defines the process for identifying, analysing, and evaluating risks and opportunities associated with the organisation's AI systems and the AIMS itself. It satisfies the requirement in ISO/IEC 42001:2023, Clause 6.1.2 for a documented AI risk assessment process.

---

## 2. Scope

This process applies to:
- All AI systems within the AIMS scope (as defined in AIMS-SCOPE-001)
- - The AIMS processes themselves
  - - Risks arising from AI supply chain and third-party AI components
   
    - ---

    ## 3. Definitions

    | Term | Definition |
    |------|-----------|
    | Risk | Effect of uncertainty on objectives — can be positive (opportunity) or negative |
    | AI Risk | A risk that arises from, or is amplified by, the use of AI systems |
    | Likelihood | Probability that the risk event will occur (1–5 scale) |
    | Impact | Magnitude of consequences if the risk event occurs (1–5 scale) |
    | Risk Score | Likelihood x Impact |
    | Risk Owner | Person accountable for monitoring and treating a specific risk |
    | Residual Risk | Risk remaining after treatment controls are applied |

    ---

    ## 4. Risk Assessment Frequency

    | Trigger | Assessment Required |
    |---------|-------------------|
    | New AI system proposed | Full risk assessment before design approval |
    | Significant change to existing AI system | Reassessment of affected risk areas |
    | New regulation or legal requirement | Review of affected risks |
    | AI incident or near-miss | Reassessment of related risks |
    | Annual AIMS review cycle | Full risk register review |
    | Management Review request | Ad hoc review as directed |

    ---

    ## 5. Risk Assessment Process Steps

    ### Step 1 — Identify Risks

    For each in-scope AI system and AIMS process, identify risks across the following categories:

    | Category | Examples |
    |----------|---------|
    | Accuracy / Performance | Model drift, incorrect predictions, poor calibration |
    | Bias and Fairness | Discriminatory outputs against protected groups |
    | Privacy | Unauthorised use of personal data in training or inference |
    | Security | Adversarial attacks, model inversion, data poisoning, prompt injection |
    | Transparency | Inability to explain AI decisions to affected individuals |
    | Accountability | No clear owner when something goes wrong |
    | Legal / Regulatory | Non-compliance with EU AI Act, GDPR, sector-specific rules |
    | Operational | System failure, third-party AI vendor dependency |
    | Societal | Automation of harmful decisions, reputational harm |
    | Supplier / Third-party | AI vendor risk, data quality from external sources |

    **Methods for risk identification:**
    - Review of AI Systems Inventory
    - - Workshops with AI System Owners and developers
      - - Review of regulatory requirements and industry incidents
        - - Results of previous audits and assessments
         
          - ### Step 2 — Analyse Risks
         
          - For each identified risk, assess:
         
          - **Likelihood Scale**
          - | Score | Description |
          - |-------|-------------|
          - | 1 | Rare — Unlikely to occur; no known precedent |
          - | 2 | Unlikely — Could occur but not expected |
          - | 3 | Possible — May occur in some circumstances |
          - | 4 | Likely — Will probably occur; has occurred before |
          - | 5 | Almost Certain — Expected to occur in most circumstances |
         
          - **Impact Scale**
          - | Score | Description |
          - |-------|-------------|
          - | 1 | Negligible — Minimal impact; easily recovered |
          - | 2 | Minor — Limited impact; manageable with existing resources |
          - | 3 | Moderate — Noticeable impact; requires management attention |
          - | 4 | Major — Significant harm; potential regulatory action or reputational damage |
          - | 5 | Severe — Critical harm to individuals, major legal/regulatory consequence, or reputational crisis |
         
          - **Risk Score = Likelihood x Impact**
         
          - ### Step 3 — Evaluate Risks
         
          - **Risk Appetite Matrix**
         
          - | Score | Level | Response Required |
          - |-------|-------|------------------|
          - | 1–4 | Low | Accept — monitor at standard frequency |
          - | 5–9 | Medium | Treat or accept with monitoring; review quarterly |
          - | 10–14 | High | Treatment required; review monthly |
          - | 15–25 | Critical | Immediate treatment required; escalate to management |
         
          - ### Step 4 — Document Results
         
          - All risk assessments must be documented in the AI Risk Register (AI-RISK-REGISTER.md). Each entry must include:
          - - Risk ID, AI System, Risk Description, Category
            - - Likelihood score, Impact score, Risk Score
              - - Risk Owner
                - - Existing controls
                  - - Treatment decision
                    - - Residual risk score
                     
                      - ### Step 5 — Risk Treatment
                     
                      - For risks requiring treatment (score >= 10), complete a Risk Treatment Plan (RISK-TREATMENT-PLAN.md) specifying:
                      - - Selected treatment option: Avoid / Reduce / Transfer / Accept
                        - - Specific controls to implement (referencing Annex A controls)
                          - - Residual risk after treatment
                            - - Owner, deadline, and evidence of implementation
                             
                              - ### Step 6 — Statement of Applicability
                             
                              - Following risk treatment, produce and maintain the Statement of Applicability (STATEMENT-OF-APPLICABILITY.md) listing all Annex A controls with applicability decisions and justifications.
                             
                              - ---

                              ## 6. Roles and Responsibilities

                              | Role | Responsibility |
                              |------|---------------|
                              | Risk Manager | Leads risk assessment process; maintains Risk Register |
                              | AI System Owner | Provides system-specific risk information; owns assigned risks |
                              | AI Governance Lead | Reviews and approves risk assessments |
                              | DPO | Assesses privacy-related AI risks |
                              | Internal Auditor | Audits risk assessment process (Clause 9.2) |
                              | Top Management | Approves risk appetite; reviews risk status at management review |

                              ---

                              ## 7. Records

                              | Record | Retained In | Retention Period |
                              |--------|------------|-----------------|
                              | AI Risk Register | 05-CLAUSE6-PLANNING/AI-RISK-REGISTER.md | Minimum 3 years |
                              | Risk Treatment Plan | 05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md | Minimum 3 years |
                              | Statement of Applicability | 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md | Duration of AIMS + 3 years |
                              | Risk assessment working notes | AI Governance Lead | Minimum 1 year |

                              ---

                              ## 8. Review History

                              | Version | Date | Changes | Approved By |
                              |---------|------|---------|-------------|
                              | 1.0 | | Initial issue | |

                              ---

                              *ISO/IEC 42001:2023 AI Governance Toolkit | Clause 6.1.2 | See root README.md for full index*
