# Annex B — AI Concepts and Their Application to ISO/IEC 42001
## ISO/IEC 42001:2023 | Informative Reference Guide

> **Note:** This document is an implementation reference guide. It is NOT a reproduction of the ISO/IEC 42001:2023 standard. Users must obtain a licensed copy of the standard from ISO (iso.org) for the full normative text.

---

## Purpose

ISO/IEC 42001:2023 Annex B provides guidance on how AI-specific concepts referenced in the standard should be understood and applied in an AIMS context. This document summarises those concepts and provides practical implementation notes to help practitioners apply them correctly.

---

## B.1 — AI Systems and Their Characteristics

### What is an AI System?
An AI system is a machine-based system that, for a given set of objectives, makes predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy.

Key characteristics relevant to AIMS:
- **Autonomy** — AI systems can act without constant human direction. The degree of autonomy varies from none (pure automation) to full (unsupervised decision-making).
- **Adaptivity** — Many AI systems learn from data and change their behaviour over time. This creates ongoing governance requirements that static software systems do not have.
- **Opacity** — Complex AI models (particularly deep learning) may not be fully explainable, creating transparency and accountability challenges.
- **Scale** — AI systems can affect large numbers of people simultaneously, amplifying both beneficial and harmful effects.

### AIMS Implication
The AIMS must account for the full lifecycle of AI systems — not just deployment, but design, development, monitoring, and decommissioning. See `AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md`.

---

## B.2 — Types of AI Systems Encountered in AIMS Scope

| AI System Type | Description | Typical AIMS Considerations |
|---------------|-------------|---------------------------|
| Machine Learning (supervised) | Learns from labelled training data to make predictions | Bias in training data; performance drift; fairness evaluation |
| Machine Learning (unsupervised) | Finds patterns in unlabelled data | Interpretability; validation of clustering quality |
| Reinforcement Learning | Learns by trial and error with rewards | Safety constraints; unexpected emergent behaviour |
| Large Language Models (LLMs) | Generates text, code, analysis from prompts | Hallucination risk; prompt injection; data leakage |
| Computer Vision | Interprets images and video | Bias across demographic groups; privacy (biometrics) |
| Recommender Systems | Suggests content, products, or actions | Filter bubbles; manipulation risk; transparency |
| Decision Support Systems | Assists human decision-makers | Over-reliance; automation bias; explainability |
| Autonomous Agents | Takes sequences of actions without human intervention | Scope containment; oversight mechanisms; fallback |

---

## B.3 — AI Risk Concepts

### Risk vs. Traditional IT Risk
AI risk is distinct from traditional IT risk in several important ways:

| Dimension | Traditional IT | AI-Specific |
|-----------|--------------|-------------|
| Failure mode | Deterministic — error or no error | Probabilistic — wrong with varying confidence |
| Validation | Test all paths to verify behaviour | Cannot test all possible inputs |
| Drift | Software doesn't change itself | AI models can degrade over time |
| Bias | Not inherent | Can encode and amplify societal biases |
| Explainability | Code logic is auditable | Neural network decisions may be opaque |
| Adversarial vulnerability | Patch-based security | Adversarial examples; prompt injection |

### Key AI Risk Concepts for AIMS

**Data Risk** — Risks arising from the data used to train, validate, and operate AI systems. Includes data quality, data bias, data provenance, and data protection.

**Model Risk** — Risks arising from the AI model itself. Includes model performance, model drift, model bias, model opacity, and adversarial vulnerability.

**Deployment Risk** — Risks arising from how AI systems are deployed and integrated. Includes integration failures, scaling issues, and inadequate human oversight.

**Operational Risk** — Risks arising during ongoing operation. Includes monitoring gaps, incident response failures, and supply chain risks.

**Societal Risk** — Broader risks to society from AI. Includes discrimination, surveillance, manipulation, and concentration of power.

---

## B.4 — AI Objectives and Their Relationship to AIMS Objectives

ISO/IEC 42001:2023 Clause 6.2 requires the organisation to establish AI objectives. Annex B provides guidance on how these relate to responsible AI principles.

### Recommended AI Objective Categories

| Objective Category | Example Objectives | Relevant Annex A Controls |
|------------------|------------------|--------------------------|
| Fairness | Reduce demographic disparity in AI outcomes to < 5% | A.4.7 |
| Transparency | 100% of AI systems have published model cards | A.4.8, A.9.2 |
| Accountability | 100% of AI systems have named owners | A.2.3, A.4.10 |
| Safety | Zero high-severity AI incidents per quarter | A.4.4, A.6.2.13 |
| Privacy | Zero GDPR violations related to AI | A.4.9 |
| Performance | All AI systems operating within 5% of baseline | A.4.3, A.6.2.10 |
| Regulatory | Full EU AI Act compliance before Aug 2026 | A.10.2 |

See `AI-OBJECTIVES-REGISTER.md` for the live objectives register.

---

## B.5 — Responsible AI Principles and Their Annex A Mapping

| Responsible AI Principle | Primary Annex A Domain | Key Controls |
|--------------------------|----------------------|-------------|
| Fairness / Non-discrimination | A.4 | A.4.7 |
| Transparency / Explainability | A.4, A.9 | A.4.8, A.9.2 |
| Accountability | A.2, A.4 | A.2.3, A.4.10 |
| Human oversight and control | A.3, A.6 | A.3.2, A.6.2.9 |
| Privacy | A.4 | A.4.9 |
| Safety | A.4, A.6 | A.4.4, A.6.2.13 |
| Security | A.4, A.6 | A.4.5 |
| Reliability / Robustness | A.4, A.6 | A.4.3, A.6.2.10 |
| Societal benefit | A.7 | A.7.2 |
| Environmental sustainability | A.7 | A.7.2 |

---

## B.6 — AI Lifecycle Phases

ISO/IEC 42001:2023 uses a consistent lifecycle model for AI systems. Understanding which phase an AI system is in determines which controls apply.

| Phase | Description | Key Controls | Key Documents |
|-------|-------------|-------------|--------------|
| Design | Define purpose, requirements, responsible AI design | A.6.1.2 | AI-SYSTEM-IMPACT-ASSESSMENT.md |
| Data | Collect, prepare, and govern training/operational data | A.6.2.2 | AI-RISK-REGISTER.md |
| Development | Build, train, validate AI model | A.6.2.4, A.6.2.5 | AI-DEPLOYMENT-CHECKLIST.md |
| Deployment | Release AI system to production | A.6.2.7, A.6.3 | AI-DEPLOYMENT-CHECKLIST.md |
| Operation | Monitor, maintain, update | A.6.2.8, A.6.2.10 | AI-PERFORMANCE-MONITORING-PLAN.md |
| Change | Modify the system materially | A.6.2.11 | AI-CHANGE-CONTROL-PROCEDURE.md |
| Decommission | Retire the AI system | A.6.2.12 | AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md |

---

## B.7 — AI System Classification for Risk-Based Controls

A risk-tiering approach helps apply proportionate controls. Recommended classification:

| Tier | Description | Examples | Controls Intensity |
|------|-------------|---------|-------------------|
| Tier 1 — Critical | High-risk AI; affects individuals' fundamental rights, safety, or significant decisions | Credit scoring, recruitment screening, medical AI | Full controls; highest oversight; quarterly monitoring |
| Tier 2 — High | Significant AI; material impact on individuals or operations | Customer service AI, fraud detection, HR analytics | Strong controls; regular monitoring; DPIA required |
| Tier 3 — Medium | Moderate AI; limited individual impact | Internal productivity tools, content moderation aids | Standard controls; annual monitoring |
| Tier 4 — Low | Minimal AI; no meaningful individual impact | Spam filters, autocomplete, search ranking (internal) | Basic controls; periodic review |

Note: EU AI Act classification (prohibited, high-risk, limited-risk, minimal-risk) must also be applied where EU nexus exists. See `LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md`.

---

## B.8 — Key AI Terminology Quick Reference

| Term | Definition | AIMS Relevance |
|------|-----------|---------------|
| Algorithm | Set of rules or instructions for solving a problem | Foundation of AI systems |
| Bias (AI) | Systematic errors in AI outputs due to flawed training data or model design | Fairness control A.4.7 |
| Concept drift | Change in the statistical relationship between input and output over time | Monitoring A.6.2.10 |
| Data drift | Change in the statistical distribution of input data over time | Monitoring A.6.2.10 |
| Explainability | Ability to explain an AI decision in understandable terms | Transparency A.4.8 |
| Feature | An input variable used by an AI model | Data governance A.6.2.2 |
| Hallucination | AI generating confident but incorrect outputs (especially LLMs) | Reliability A.4.3 |
| Human-in-the-loop | Human reviews and approves each AI decision | Human oversight A.3.2 |
| Model card | Documentation of an AI model's design, performance, and limitations | Documentation A.9.2 |
| Overfitting | Model performs well on training data but poorly on new data | Testing A.6.2.5 |
| Prompt injection | Malicious input designed to override AI system instructions | Security A.4.5 |
| Training data | Data used to train (build) an AI model | Data A.6.2.2 |
| Transfer learning | Using a pre-trained model as starting point for a new task | Acquisition A.6.2.3 |
| Zero-day (AI) | Novel attack or failure mode not yet known or defended against | Security A.4.5 |

---

## Obtaining the Full Standard

To access the complete normative text of ISO/IEC 42001:2023, including Annex B in full, purchase a licensed copy from:
- ISO Store: [iso.org/store](https://www.iso.org/store.html)
- BSI: [bsigroup.com](https://www.bsigroup.com)
- ANSI: [ansi.org](https://www.ansi.org)

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Annex B Reference Guide | See root README.md for full index*
