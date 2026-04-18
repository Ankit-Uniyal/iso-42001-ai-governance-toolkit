# AI Model Card / AI System Card
## ISO/IEC 42001:2023 | Clause 8.1 / Annex A.6.2.3 — Template

**Document ID:** AIMS-MODELCARD-[SystemID]
**AI System Name:** ___________________________
**System ID:** ___________________________
**Version:** ___________________________
**Owner:** ___________________________
**Date Created:** ___________________________
**Last Updated:** ___________________________
**Classification:** Internal

---

## 1. System Overview

| Field | Details |
|-------|---------|
| System Name | |
| System ID | |
| Version | |
| AI Type | e.g., ML classification / NLP / generative AI / recommendation engine |
| Primary Use Case | What this system is designed to do |
| Business Function | Department / process supported |
| Deployment Status | Live / Pilot / Development / Decommissioned |
| System Owner | Named individual accountable for this system |
| Technical Lead | Named individual responsible for technical operation |

---

## 2. Model Details

| Field | Details |
|-------|---------|
| Model Architecture | e.g., XGBoost / BERT / GPT-based / CNN / custom |
| Training Framework | e.g., TensorFlow / PyTorch / scikit-learn |
| Model Version | |
| Training Date | |
| Last Retrained | |
| Retraining Schedule | e.g., quarterly / triggered by drift detection |
| Model Repository | Location of model artefacts |

---

## 3. Intended Use

**Primary Intended Use:** [Describe the specific, intended use case]

**Intended Users:** [Describe who is intended to use or be affected by this system]

**Out-of-Scope Uses:** [Explicitly document uses the model should NOT be used for]

---

## 4. Training Data

| Field | Details |
|-------|---------|
| Data Sources | |
| Data Volume | |
| Data Collection Period | |
| Data Provenance | How and where data was sourced |
| Legal Basis for Use | e.g., Consent / Legitimate interest / Contract |
| Personal Data Used | Yes / No — if Yes, describe |
| Data Quality Assessment | Pass / Pass with conditions / Fail |
| Bias Review Completed | Yes / No — summary of findings |

---

## 5. Performance Metrics

| Metric | Value | Measured On | Date |
|--------|-------|-------------|------|
| Accuracy | | | |
| Precision | | | |
| Recall / Sensitivity | | | |
| F1 Score | | | |
| [Custom metric] | | | |

**Minimum acceptable performance threshold:** ___________________________

---

## 6. Bias and Fairness Evaluation

| Protected Characteristic | Group | Metric | Value | Threshold | Pass/Fail |
|--------------------------|-------|--------|-------|-----------|-----------|
| Gender | Male | | | | |
| Gender | Female | | | | |
| Age | Under 30 | | | | |
| Age | Over 65 | | | | |
| Ethnicity | [Group] | | | | |

**Fairness Methodology:** [Describe approach — e.g., disparate impact analysis]
**Known Limitations / Residual Bias:** [Describe any known fairness limitations]

---

## 7. Explainability

| Question | Answer |
|---------|--------|
| Is the model explainable? | Yes / No / Partially |
| Explainability method | e.g., SHAP values / LIME / decision rules |
| Can decisions be explained to affected individuals? | Yes / No / With limitations |
| Explainability tool | |

---

## 8. Human Oversight

| Decision Type | Human Oversight Required | Oversight Mechanism | Escalation Path |
|--------------|------------------------|---------------------|----------------|
| High-stakes decisions | Yes | | |
| Standard decisions | No / Audit sample | | |

---

## 9. Monitoring

| Metric | Frequency | Alert Threshold | Owner |
|--------|-----------|----------------|-------|
| Model accuracy | | | |
| Fairness metrics | | | |
| Data drift | | | |
| Error rates | | | |

---

## 10. Testing History

| Date | Test Type | Results Summary | Outcome |
|------|---------|----------------|---------|
| | Bias evaluation | | Pass / Fail |
| | Performance testing | | Pass / Fail |
| | Adversarial testing | | Pass / Fail |
| | Security testing | | Pass / Fail |
| | UAT | | Pass / Fail |

---

## 11. Related Documents

| Document | Reference |
|---------|---------|
| AI System Impact Assessment | |
| Risk Register entry | |
| Deployment Checklist | |

---

## 12. Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | | Initial model card | |

---

*ISO/IEC 42001:2023 AI Governance Toolkit | Clause 8.1 / A.6.2.3 | See root README.md for full index*
