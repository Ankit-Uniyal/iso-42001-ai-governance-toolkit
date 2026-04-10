# AI Risk Register Template — ISO/IEC 42001:2023

**Organization:** ___________________________
**AI System / Scope:** ___________________________
**Risk Owner:** ___________________________
**Last Updated:** ___________________________
**Review Frequency:** Quarterly

> This risk register template is aligned with ISO/IEC 42001:2023 Clause 6.1 (AI Risk Assessment) and Annex C (Guidance on AI Risk Management).

---

## Risk Scoring Methodology

### Likelihood Scale

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Rare | May occur only in exceptional circumstances (less than once in 5 years) |
| 2 | Unlikely | Could occur at some time (once in 2-5 years) |
| 3 | Possible | Might occur at some time (once per year) |
| 4 | Likely | Will probably occur in most circumstances (monthly) |
| 5 | Almost Certain | Is expected to occur in most circumstances (weekly or more) |

### Consequence Scale

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Insignificant | Minimal impact — no meaningful harm to individuals or organization |
| 2 | Minor | Limited impact — minor inconvenience, easily remediated |
| 3 | Moderate | Significant impact — affects operations, moderate regulatory exposure |
| 4 | Major | Serious impact — significant harm to individuals, major regulatory action |
| 5 | Catastrophic | Critical impact — severe harm, fundamental breach of trust, organizational threat |

### Risk Rating Matrix

| Likelihood / Consequence | 1 Insignificant | 2 Minor | 3 Moderate | 4 Major | 5 Catastrophic |
|--------------------------|----------------|---------|------------|---------|----------------|
| 5 Almost Certain | Medium (5) | High (10) | Critical (15) | Critical (20) | Critical (25) |
| 4 Likely | Low (4) | Medium (8) | High (12) | Critical (16) | Critical (20) |
| 3 Possible | Low (3) | Medium (6) | Medium (9) | High (12) | Critical (15) |
| 2 Unlikely | Low (2) | Low (4) | Medium (6) | Medium (8) | High (10) |
| 1 Rare | Low (1) | Low (2) | Low (3) | Low (4) | Medium (5) |

### Risk Appetite Thresholds

| Rating | Score | Action Required |
|--------|-------|----------------|
| **Critical** | 15-25 | Immediate treatment required — escalate to executive leadership |
| **High** | 10-12 | Treatment plan required within 30 days |
| **Medium** | 5-9 | Treatment plan required within 90 days |
| **Low** | 1-4 | Monitor and review at next scheduled assessment |

---

## Risk Treatment Options

| Option | Description | When to Use |
|--------|-------------|-------------|
| **Mitigate** | Implement controls to reduce likelihood or consequence | Most AI risks — preferred option |
| **Accept** | Accept the risk within the defined risk appetite | Low/Medium risks where treatment cost exceeds benefit |
| **Transfer** | Transfer risk to third party (insurance, contract) | Residual risks after mitigation |
| **Avoid** | Cease the activity that creates the risk | Critical risks that cannot be adequately mitigated |

---

## AI Risk Register

### Category 1: Bias and Fairness Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| BIAS-001 | AI model produces discriminatory outcomes against protected characteristics (age, gender, race, disability) | | | | | | | | | | | |
| BIAS-002 | Training data contains historical bias that perpetuates inequitable outcomes | | | | | | | | | | | |
| BIAS-003 | Proxy variables used in model inadvertently encode protected characteristics | | | | | | | | | | | |
| BIAS-004 | AI system performance varies significantly across demographic groups | | | | | | | | | | | |
| BIAS-005 | Lack of representation in training data for minority groups | | | | | | | | | | | |

### Category 2: Transparency and Explainability Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| TRANS-001 | Inability to explain AI decisions to affected individuals or regulators | | | | | | | | | | | |
| TRANS-002 | Black-box model used in high-stakes decisions without explainability mechanisms | | | | | | | | | | | |
| TRANS-003 | Users unaware they are interacting with an AI system | | | | | | | | | | | |
| TRANS-004 | AI system documentation insufficient for regulatory audit | | | | | | | | | | | |
| TRANS-005 | Model documentation (model card) not maintained or outdated | | | | | | | | | | | |

### Category 3: Data Quality and Privacy Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| DATA-001 | Personal data used for AI training without appropriate consent or legal basis | | | | | | | | | | | |
| DATA-002 | AI model memorizes and reproduces training data containing personal information | | | | | | | | | | | |
| DATA-003 | Poor data quality leads to unreliable AI outputs | | | | | | | | | | | |
| DATA-004 | Training data provenance not documented — cannot verify data lineage | | | | | | | | | | | |
| DATA-005 | Data used for AI training violates third-party IP rights or licensing terms | | | | | | | | | | | |
| DATA-006 | Cross-border data transfer for AI training violates data sovereignty requirements | | | | | | | | | | | |

### Category 4: Security Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| SEC-001 | Adversarial attacks causing AI model to produce malicious or incorrect outputs | | | | | | | | | | | |
| SEC-002 | Model poisoning — malicious manipulation of AI training data | | | | | | | | | | | |
| SEC-003 | Prompt injection attacks against LLM-based AI systems | | | | | | | | | | | |
| SEC-004 | Model inversion attacks — extracting training data from AI model | | | | | | | | | | | |
| SEC-005 | Unauthorized access to AI model weights or training data | | | | | | | | | | | |
| SEC-006 | AI system used as vector for social engineering or fraud | | | | | | | | | | | |
| SEC-007 | Membership inference attacks — determining if specific data was used in training | | | | | | | | | | | |

### Category 5: Operational Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| OPS-001 | AI model performance degrades over time due to data drift | | | | | | | | | | | |
| OPS-002 | AI system failure in production causes business process disruption | | | | | | | | | | | |
| OPS-003 | Overreliance on AI — humans fail to exercise judgment when AI is wrong | | | | | | | | | | | |
| OPS-004 | AI system deployed without adequate testing or validation | | | | | | | | | | | |
| OPS-005 | Inadequate monitoring — AI performance issues not detected promptly | | | | | | | | | | | |
| OPS-006 | No rollback or fallback procedure when AI system fails | | | | | | | | | | | |

### Category 6: Regulatory and Compliance Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| REG-001 | High-risk AI system deployed without required EU AI Act conformity assessment | | | | | | | | | | | |
| REG-002 | AI system in prohibited use category under EU AI Act continues operation | | | | | | | | | | | |
| REG-003 | AI system used in GDPR-regulated decisions violates right to explanation | | | | | | | | | | | |
| REG-004 | Sector-specific AI regulations (healthcare, financial services) not identified or addressed | | | | | | | | | | | |
| REG-005 | AI governance documentation insufficient for regulatory inspection | | | | | | | | | | | |

### Category 7: Third-Party and Supply Chain AI Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| TPRM-001 | Third-party AI vendor suffers security incident compromising AI system | | | | | | | | | | | |
| TPRM-002 | AI API provider changes model behavior without notification | | | | | | | | | | | |
| TPRM-003 | Open-source AI model contains vulnerabilities or hidden biases | | | | | | | | | | | |
| TPRM-004 | Vendor AI system processes personal data in violation of DPA agreements | | | | | | | | | | | |
| TPRM-005 | Dependency on single AI vendor creates operational concentration risk | | | | | | | | | | | |

### Category 8: Reputational and Societal Risks

| Risk ID | Risk Description | AI System | Likelihood | Consequence | Risk Score | Rating | Risk Owner | Treatment Option | Controls | Target Date | Residual Risk | Status |
|---------|-----------------|-----------|------------|-------------|------------|--------|------------|-----------------|----------|-------------|--------------|--------|
| REP-001 | AI system produces harmful, offensive, or factually incorrect outputs (hallucinations) | | | | | | | | | | | |
| REP-002 | AI system disproportionately impacts vulnerable populations | | | | | | | | | | | |
| REP-003 | Public backlash from AI-related incident damages organizational reputation | | | | | | | | | | | |
| REP-004 | AI used for manipulation, disinformation, or deepfake generation | | | | | | | | | | | |
| REP-005 | Environmental impact of AI compute (carbon footprint) attracts negative attention | | | | | | | | | | | |

---

## Risk Register Summary Dashboard

### Risk Distribution by Category

| Category | Total Risks | Critical | High | Medium | Low | Open | Closed |
|----------|-------------|----------|------|--------|-----|------|--------|
| Bias and Fairness | 5 | | | | | | |
| Transparency | 5 | | | | | | |
| Data and Privacy | 6 | | | | | | |
| Security | 7 | | | | | | |
| Operational | 6 | | | | | | |
| Regulatory | 5 | | | | | | |
| Third-Party | 5 | | | | | | |
| Reputational | 5 | | | | | | |
| **TOTAL** | **44** | | | | | | |

### Top 10 Risks (Prioritized)

| Priority | Risk ID | Risk Description | Rating | Owner | Due Date |
|----------|---------|-----------------|--------|-------|----------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

---

## Risk Treatment Log

| Risk ID | Treatment Action | Control Implemented | Implementation Date | Effectiveness Review Date | Residual Risk After Treatment | Approved By |
|---------|-----------------|---------------------|--------------------|--------------------------|-----------------------------|-------------|
| | | | | | | |

---

## Risk Register Review History

| Review Date | Reviewer | Changes Made | Next Review Date |
|-------------|---------|-------------|-----------------|
| | | | |

---

*This risk register template is aligned with ISO/IEC 42001:2023 Annex C and Clause 6.1.*
*Maintained by [Ankit Uniyal](https://github.com/Ankit-Uniyal) — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
