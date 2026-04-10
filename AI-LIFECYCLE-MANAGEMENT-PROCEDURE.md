# AI System Lifecycle Management Procedure
## ISO/IEC 42001:2023 — Clause 8.5 & Annex A Domain A.6 (Full Implementation Guide)

---

**Document ID:** AIMS-PROC-002
**Version:** 1.0
**Owner:** AI Development Lead / AI Governance Lead
**Classification:** Internal — Controlled Document

---

## 1. Purpose and Scope

This procedure defines the end-to-end lifecycle management process for AI systems within the AIMS scope. It covers all phases from conception to decommissioning, embedding responsible AI principles and governance requirements at each stage.

**This procedure implements:**
- ISO/IEC 42001:2023 Clause 8.5 (AI System Lifecycle)
- Annex A controls A.6.1.1 through A.6.5.1 (13 controls)

---

## 2. AI System Lifecycle Overview

```
[PHASE 1]        [PHASE 2]       [PHASE 3]       [PHASE 4]       [PHASE 5]
  Design   →   Development  →  Deployment  →   Operation   →  Decommission
    ↑              ↑                ↑               ↑               ↑
  A.6.1         A.6.2           A.6.3           A.6.4           A.6.5
```

Each phase has defined **Governance Gates** — approval checkpoints that must be passed before proceeding to the next phase.

---

## PHASE 1: AI SYSTEM DESIGN (Controls A.6.1.1, A.6.1.2)

### 1.1 Design Phase Initiation

**Trigger:** Business unit identifies need for AI system; receives approval to initiate AI project

**Required Inputs:**
- Business requirements document
- Preliminary budget approval
- Executive sponsor designated
- AI System Owner assigned

### 1.2 Responsible AI Design Requirements (A.6.1.1)

All AI system design specifications shall include the following responsible AI requirements:

#### 1.2.1 Fairness Requirements
```
Fairness Requirements Template:
- Target population: [Define who the AI system will affect]
- Protected attributes of concern: [List relevant protected characteristics]
- Fairness definition adopted: [Demographic parity / Equalized odds / Individual fairness / Counterfactual fairness]
- Acceptable performance disparity thresholds: [Define maximum acceptable gap]
- Bias testing approach: [Define testing methodology]
```

#### 1.2.2 Transparency and Explainability Requirements
```
Explainability Requirements Template:
- AI disclosure requirement: [Yes/No — how will users be informed?]
- Explainability level required: [Global / Local / Both]
- Explanation format: [Natural language / SHAP values / LIME / Other]
- Explanation audience: [End users / Affected individuals / Regulators / Internal]
- Right to explanation: [Define how individuals can request explanations]
```

#### 1.2.3 Human Oversight Requirements
```
Human Oversight Requirements Template:
- Oversight level: [Full automation / Human-in-loop / Human-on-loop / Human-in-command]
- Override mechanism: [Define how humans can override AI decisions]
- Escalation criteria: [Define when AI must defer to human judgment]
- Oversight competency: [Define required skills of oversight staff]
- Monitoring frequency: [Define how often humans review AI decisions]
```

#### 1.2.4 Privacy by Design Requirements
```
Privacy Requirements Template:
- Personal data types processed: [List data categories]
- Legal basis for processing: [Consent / Legitimate interest / Legal obligation / Other]
- Data minimization approach: [How will excess data be avoided?]
- Retention limits: [Define maximum retention periods]
- DPIA required: [Yes/No — if Yes, must be completed before development begins]
```

#### 1.2.5 Security Requirements
```
Security Requirements Template:
- Threat model completed: [Yes/No]
- Adversarial attack scenarios considered: [List]
- Authentication and access control requirements: [Define]
- Encryption requirements: [In transit / At rest / Both]
- Security testing requirements: [Penetration testing / Red team / Other]
```

### 1.3 AI System Design Documentation (A.6.1.2)

The following design documentation shall be produced:

| Document | Description | Required For |
|----------|-------------|-------------|
| AI System Design Specification | Architectural overview, model type, data flow, integration design | All AI systems |
| Data Flow Diagram | How data moves through the AI system | All AI systems processing data |
| Responsible AI Design Record | Documentation of responsible AI choices made in design | All AI systems |
| Threat Model | Security threats identified and mitigated in design | Medium and above risk tier |
| DPIA (if required) | Data Protection Impact Assessment | Systems processing personal data at scale |
| ASIA (AI System Impact Assessment) | Broader impact assessment | All Tier 1 and Tier 2 AI systems |

### 1.4 DESIGN GATE — Governance Approval Checklist

| Requirement | Status | Approver |
|------------|--------|---------|
| Business case approved | | |
| Responsible AI design requirements documented | | |
| Design documentation complete | | |
| Prohibited use check passed | | |
| EU AI Act classification completed | | |
| ASIA initiated or completed | | |
| DPIA initiated (if required) | | |
| AI Governance Committee notified | | |

**Design Gate Decision:** [ ] APPROVED to proceed to Development | [ ] CONDITIONAL | [ ] NOT APPROVED

---

## PHASE 2: AI SYSTEM DEVELOPMENT (Controls A.6.2.1 through A.6.2.8)

### 2.1 Development Process Requirements (A.6.2.1)

AI systems shall be developed following a controlled process including:

#### 2.1.1 Version Control
- All model code, training scripts, and configuration files must be under version control (Git or equivalent)
- Model weights and artifacts must be versioned and stored in a model registry
- Data preprocessing scripts must be versioned alongside model code
- Experiment tracking must record hyperparameters, data versions, and performance metrics

#### 2.1.2 Development Environment Controls
- Development, test/staging, and production environments must be segregated
- Access to production AI models restricted to authorized personnel
- Development credentials must not be used in production
- Infrastructure-as-code for AI environments must be version controlled

#### 2.1.3 Responsible AI Development Checkpoints

Developers must complete the following checkpoints during development:

**Checkpoint 1 — Data Readiness (before model training begins):**
- [ ] Training data quality assessment completed (A.7.2)
- [ ] Data provenance documented (A.7.3)
- [ ] Personal data legal basis confirmed (A.7.4)
- [ ] Bias assessment of training data completed (A.7.5)
- [ ] Data access controls implemented (A.7.6)

**Checkpoint 2 — Model Development (during training and tuning):**
- [ ] Model architecture appropriate for use case and explainability requirements
- [ ] Fairness constraints applied where required
- [ ] Regularization to prevent overfitting to sensitive attributes
- [ ] Experiment tracking active (hyperparameters, data versions, metrics)

**Checkpoint 3 — Validation (before deployment testing):**
- [ ] Bias evaluation completed across all relevant demographic groups (A.6.2.6)
- [ ] Adversarial testing completed (A.6.2.5)
- [ ] Performance testing in representative environment (A.6.2.8)
- [ ] Model card completed and reviewed (A.6.2.3)
- [ ] Security assessment completed

### 2.2 AI Model Card Template (A.6.2.3)

Every AI model must have a maintained model card:

```
MODEL CARD — [Model Name] v[Version]
Last Updated: [Date]
Owner: [Team/Person]

## Model Details
- Model type: [Architecture/algorithm]
- Training framework: [e.g., TensorFlow, PyTorch, scikit-learn]
- Model version: [Semantic version]
- License: [If applicable]

## Intended Use
- Primary intended uses: [Describe intended applications]
- Intended users: [Who should use this model]
- Out-of-scope uses: [Uses this model should NOT be applied to]

## Training Data
- Training dataset(s): [Name, version, source]
- Training data size: [Number of records/tokens]
- Data collection period: [Date range]
- Known data limitations: [Any known gaps or biases in training data]

## Evaluation Data
- Evaluation dataset(s): [Name, version, source]
- Evaluation metrics: [Define metrics used]

## Performance
| Metric | Overall | [Subgroup 1] | [Subgroup 2] | [Subgroup 3] |
|--------|---------|-------------|-------------|-------------|
| [Metric 1] | | | | |
| [Metric 2] | | | | |

## Fairness Analysis
- Protected attributes evaluated: [List]
| Attribute | Metric | Group A | Group B | Disparity | Acceptable? |
|-----------|--------|---------|---------|-----------|-------------|
| | | | | | |

## Known Limitations
- [List known limitations, failure modes, edge cases]

## Ethical Considerations
- [List ethical considerations addressed]
- [List residual ethical risks]

## Recommendations
- [Guidance for users on responsible use]
- [Monitoring recommendations]

## Caveats and Recommendations
```

### 2.3 Bias Evaluation Methodology (A.6.2.6)

**Step 1 — Define Fairness Metric:**
Select appropriate fairness metric based on use case:
| Metric | Definition | Best For |
|--------|-----------|---------|
| Demographic Parity | Equal positive prediction rates across groups | When equal opportunity is required |
| Equalized Odds | Equal TPR and FPR across groups | Classification tasks affecting protected groups |
| Predictive Parity | Equal precision across groups | Resource allocation decisions |
| Individual Fairness | Similar individuals receive similar outcomes | Cases where individual justice is paramount |
| Counterfactual Fairness | Outcome unchanged if individual were in different demographic group | High-stakes individual decisions |

**Step 2 — Identify Evaluation Groups:**
Identify protected characteristics and subgroups to test:
- Race/Ethnicity subgroups
- Gender (including non-binary if data available)
- Age groups (under 18, 18-30, 30-50, 50-65, 65+)
- Disability status (if available and relevant)
- Any other protected characteristics relevant to use case

**Step 3 — Calculate Fairness Metrics:**
For each protected attribute, calculate the selected fairness metric and compare across subgroups.

**Step 4 — Apply Fairness Thresholds:**
| Risk Tier | Maximum Acceptable Disparity |
|-----------|------------------------------|
| Tier 1 Critical | 5% maximum disparity |
| Tier 2 High | 10% maximum disparity |
| Tier 3 Medium | 15% maximum disparity |
| Tier 4 Low | 20% maximum disparity |

**Step 5 — Document and Remediate:**
If thresholds are exceeded:
- Investigate root cause (data bias, algorithmic bias, proxy variables)
- Apply appropriate mitigation (resampling, reweighting, adversarial debiasing, post-processing)
- Re-evaluate and document results
- If threshold cannot be met: escalate to AI Governance Committee before proceeding

### 2.4 Adversarial Testing Methodology (A.6.2.5)

**For all AI systems, test against relevant adversarial scenarios:**

| Attack Type | Description | Testing Method |
|-------------|-------------|---------------|
| Evasion Attack | Manipulated inputs designed to fool the model | Use adversarial example generation (FGSM, PGP, C&W) |
| Model Poisoning | Corrupted training data to manipulate model behavior | Test against known poisoned data samples |
| Prompt Injection (LLMs) | Malicious prompts designed to override system instructions | Red-team testing with injection payloads |
| Model Inversion | Attempting to extract training data from model outputs | Test with model inversion tools |
| Membership Inference | Determining if specific records were in training data | Apply membership inference attacks |
| Data Extraction (LLMs) | Extracting memorized training data | Systematic prompting to elicit training data |

**Adversarial Testing Report Template:**
```
Adversarial Testing Report — [Model Name] v[Version]
Date: [Date]
Tester: [Name]

Attack 1: [Attack Type]
- Tools used: [List]
- Test cases run: [Number]
- Successful attacks: [Number/Percentage]
- Severity: High/Medium/Low
- Mitigation applied: [Description]
- Post-mitigation test: Pass/Fail

[Repeat for each attack type]

Overall Adversarial Robustness: High/Medium/Low
Recommendation: Safe to Deploy / Deploy with Controls / Do Not Deploy
```

### 2.5 Testing in Representative Environments (A.6.2.8)

Before production deployment, AI systems must be tested in an environment that is representative of production:

**Representative Environment Requirements:**
- [ ] Data distribution matches production data distribution
- [ ] System load representative of expected production load
- [ ] All integrations and dependencies present
- [ ] Monitoring systems active and configured as they will be in production
- [ ] Human oversight mechanisms operational and tested
- [ ] No production data used unless DPIA-approved

**Acceptance Criteria for Representative Testing:**
| Criterion | Threshold | Result | Pass/Fail |
|-----------|----------|--------|-----------|
| Model performance vs. baseline | Within [X]% | | |
| Fairness metrics | Within policy thresholds | | |
| Latency (P95) | Under [X]ms | | |
| Error rate | Under [X]% | | |
| Human override rate | Under [X]% | | |
| Adversarial robustness | Pass | | |

---

## PHASE 3: AI SYSTEM DEPLOYMENT (Controls A.6.3.1, A.6.3.3)

### 3.1 Deployment Controls (A.6.3.1)

**Pre-Deployment Governance Gate:**

All of the following must be completed and approved before production deployment:

| Gate Requirement | Status | Owner | Evidence |
|-----------------|--------|-------|---------|
| All Checkpoint 1, 2, 3 items completed | | | |
| AI System Impact Assessment completed and approved | | | |
| Risk assessment updated and risks treated | | | |
| DPIA completed (if required) | | | |
| Model card complete and reviewed | | | |
| Adversarial testing passed | | | |
| Bias evaluation passed | | | |
| Representative environment testing passed | | | |
| Security assessment completed | | | |
| Human oversight mechanism tested and operational | | | |
| Monitoring and alerting configured | | | |
| Incident response contacts confirmed | | | |
| Rollback procedure documented and tested | | | |
| User disclosure implemented | | | |
| Legal and compliance review completed | | | |
| AI Governance Committee approval obtained | | | |

**Deployment Authorization Sign-off:**

| Role | Name | Approval | Date |
|------|------|---------|------|
| AI System Owner | | | |
| AI Governance Lead | | | |
| CISO | | | |
| DPO (if personal data) | | | |

### 3.2 Deployment Checklist (Operational Steps)

**Day of Deployment:**
- [ ] All governance gate requirements confirmed complete
- [ ] Deployment authorization confirmed
- [ ] Deployment window scheduled and communicated
- [ ] Rollback plan confirmed and accessible
- [ ] On-call contacts confirmed
- [ ] Monitoring dashboards active
- [ ] Deploy to production
- [ ] Smoke testing completed post-deployment
- [ ] Initial monitoring review (first 1 hour)
- [ ] Deployment record created

### 3.3 Human Oversight at Deployment (A.6.3.3)

**Human Oversight Handover Checklist:**
- [ ] Oversight staff trained on AI system capabilities and limitations
- [ ] Override mechanism demonstrated and confirmed operational
- [ ] Escalation procedure briefed to oversight staff
- [ ] Monitoring dashboard accessible to oversight staff
- [ ] First-day observation period defined (enhanced oversight for first 48 hours)

---

## PHASE 4: AI SYSTEM OPERATION AND MONITORING (Controls A.6.4.1, A.6.4.2)

### 4.1 AI Operation Monitoring Framework (A.6.4.1)

**Mandatory Monitoring Metrics:**

| Metric Category | Metric | Monitoring Frequency | Alert Threshold |
|----------------|--------|---------------------|-----------------|
| **Performance** | Accuracy / F1 score (vs. baseline) | Daily | > 5% degradation |
| **Performance** | Prediction confidence distribution | Daily | Significant shift |
| **Performance** | Error rate | Real-time | > threshold |
| **Performance** | Latency (P50, P95, P99) | Real-time | SLA breach |
| **Fairness** | Demographic parity by protected group | Weekly | > policy threshold |
| **Fairness** | Equalized odds by protected group | Weekly | > policy threshold |
| **Data** | Input data distribution | Daily | > 10% shift |
| **Data** | Feature drift (per key feature) | Daily | > 2 sigma shift |
| **Operations** | Human override rate | Daily | > baseline × 2 |
| **Operations** | User complaint / appeal rate | Daily | > baseline × 2 |
| **Security** | Adversarial input patterns | Real-time | Any detected |
| **Availability** | System uptime | Real-time | SLA breach |

### 4.2 Performance Drift Monitoring and Response (A.6.4.2)

**Drift Detection:**
| Drift Type | Detection Method | Threshold | Response |
|------------|----------------|---------|---------|
| Data Drift | Population Stability Index (PSI) | PSI > 0.2 (High drift) | Trigger model review |
| Concept Drift | Model performance degradation | > 5% accuracy drop | Initiate retraining assessment |
| Label Drift | Feedback loop analysis | Significant shift | Update training pipeline |
| Covariate Drift | Feature distribution monitoring | > 2 sigma shift | Investigate data source |

**Drift Response Process:**
1. Alert triggered by monitoring system
2. AI System Owner notified within 1 hour
3. Investigation: Is drift real or monitoring artifact?
4. If real drift confirmed:
   - Assess severity and business impact
   - Activate retraining or model adjustment if required
   - Consider temporary suspension if risk is high
   - Document in incident register
5. Post-drift review and AIMS documentation update

---

## PHASE 5: AI SYSTEM DECOMMISSIONING (Control A.6.5.1)

### 5.1 Decommissioning Process

**Trigger for Decommissioning:**
- System end-of-life decision by business owner
- Replacement by new AI system
- Regulatory prohibition
- Unacceptable ongoing risk

**Decommissioning Checklist:**

**30 Days Before Decommissioning:**
- [ ] Decommissioning decision formally approved
- [ ] Affected stakeholders identified and notified
- [ ] Dependent systems and integrations mapped
- [ ] Data retention/deletion requirements assessed
- [ ] Model artifact archiving requirements assessed
- [ ] Regulatory notification requirements assessed

**Decommissioning Day:**
- [ ] AI system disabled in production
- [ ] Fallback/manual processes activated
- [ ] API endpoints decommissioned or redirected
- [ ] Monitoring and alerting disabled

**Post-Decommissioning (within 30 days):**
- [ ] Training data: deleted or anonymized per retention schedule
- [ ] Model weights: archived securely or deleted per policy
- [ ] Model documentation archived for regulatory retention period
- [ ] Experiment tracking records archived
- [ ] AIMS register updated
- [ ] Risk register updated
- [ ] Incident register closed entries archived
- [ ] Decommissioning record created and signed off

---

## 3. AI System Register

Maintain a register of all AI systems within AIMS scope:

| System ID | AI System Name | Business Owner | AI Tier | EU AI Act Class | Lifecycle Phase | ASIA Ref | Risk Register Ref | Next Review | Status |
|-----------|---------------|---------------|---------|----------------|----------------|---------|------------------|------------|--------|
| AIMS-SYS-001 | | | | | | | | | Active |
| | | | | | | | | | |

---

## 4. Roles and Responsibilities

| Role | Responsibilities in Lifecycle |
|------|------------------------------|
| **AI System Owner** | Phase gates approval; ongoing oversight |
| **AI Developer** | Development checkpoints; documentation |
| **AI Governance Lead** | Governance gate review; policy compliance |
| **Data Scientist / ML Engineer** | Technical implementation; model validation |
| **Data Engineer** | Data quality; provenance documentation |
| **Security Engineer** | Threat modeling; adversarial testing |
| **DPO** | Privacy requirements; DPIA oversight |
| **Internal Audit** | Lifecycle compliance auditing |

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Implements ISO/IEC 42001:2023 Clause 8.5 and Annex A Domain A.6 controls A.6.1.1 through A.6.5.1*
