# ANNEX A CONTROLS — ISO/IEC 42001:2023
## Complete Implementation, Audit & Evidence Guide — All 38 Controls

---

## DOMAIN A.2 — POLICIES RELATED TO AI
*3 Controls | Establishing, aligning and maintaining the AI governance policy framework*

---

### A.2.2 — AI Policy

**Control Statement:** Top management shall establish, document, approve, communicate, and periodically review an AI policy that sets the organization's direction for responsible AI management.

---

#### What It Means

A.2.2 is the foundational governance document of the entire AIMS. The AI Policy is the top-level statement of management intent — analogous to an Information Security Policy under ISO 27001. It must be authorized at the highest appropriate level, communicated to all relevant parties, and reviewed regularly.

#### Why It Matters

Without a board- or senior-management-approved AI Policy, the entire AIMS lacks authority. Auditors will immediately question any AI governance framework that has not been formally endorsed at the top of the organization. The policy also creates accountability: employees and contractors understand what the organization expects of them regarding AI.

#### How to Implement

- **Secure top management sign-off** — The policy must be approved by the CEO, CTO, board, or equivalent authority. Document who signed it and when.
- **Cover all required elements** — The policy must address: organizational commitment to responsible AI; alignment with the organization's purpose and strategic direction; a framework for setting AI objectives; a commitment to satisfy applicable requirements (regulatory, legal, ethical); a commitment to continual improvement of the AIMS.
- **Communicate it** — Publish the policy on the intranet, include it in onboarding, and communicate it to relevant external parties.
- **Maintain and review** — Establish a regular review cycle (minimum annual) and update when organizational context or regulatory requirements change.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Policy (AIMS-POL-001) | Top-level AI governance policy signed by senior management | CEO / CTO / Board |
| Policy Communication Records | Evidence that the policy has been communicated to all relevant personnel | HR / Communications |
| Policy Review Records | Documented evidence of periodic management review and re-approval | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify the policy exists and is formally approved (signed, dated)
- Check policy content covers all required elements listed above
- Confirm version control — is it the current version? When was it last reviewed?
- Verify it has been communicated — intranet record, email distribution, onboarding inclusion

**Personnel Interviews:**
- Ask a random employee: "Have you seen the AI Policy? What does it say about your responsibilities?"
- Ask the AI Governance Lead: "When was this policy last reviewed? What triggered the review?"

**Evidence Required**
- Signed and dated AI Policy (current version)
- Version history showing prior versions and change rationale
- Communication records (intranet publication, email distribution)
- Management review and approval records

**Common Gaps Found in Audits**
- Policy exists but was never formally signed by senior management
- Policy content is generic and does not reflect the organization's specific AI context
- Policy was written at AIMS implementation and never reviewed or updated
- Policy is not communicated — staff unaware it exists

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management), Art. 26 (Deployer obligations) |
| NIST AI RMF | GOVERN 1.1, GOVERN 1.2 |
| ISO 27001:2022 | A.5.1 (Policies for information security) |

---

### A.2.3 — Alignment with Other Organizational Policies

**Control Statement:** The organization shall identify where the AI policy interacts with other organizational policies and ensure that those policies are aligned and mutually consistent.

---

#### What It Means

The AI policy does not operate in isolation. AI activity touches information security, privacy and data protection, data governance, quality management, procurement, HR and health and safety. A.2.3 requires the organization to identify every existing policy that AI activity intersects with, and to reconcile them so they do not contradict one another or leave gaps.

#### Why It Matters

Conflicting policies create both audit findings and genuine operational risk. If the AI policy permits the use of production data for model training while the data protection policy forbids it, staff receive contradictory instructions and the organization cannot demonstrate control. Auditors routinely test policy alignment because it reveals whether AI governance has been genuinely integrated into the management system or simply bolted on.

#### How to Implement

- **Map the policy landscape** — Produce an inventory of all policies that AI touches: information security, privacy, data governance, acceptable use, procurement, change management, HR and code of conduct.
- **Perform a conflict analysis** — Review each policy against the AI policy and record any contradictions, overlaps, or gaps in coverage.
- **Amend the related policies** — Update the affected policies so AI obligations are reflected consistently, rather than duplicating AI rules in multiple places.
- **Assign clear ownership at the boundaries** — Where two policies overlap, name which policy takes precedence and who arbitrates disputes.
- **Synchronize review cycles** — Align review dates so related policies are revised together and do not drift apart over time.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Policy Interaction Map | Matrix showing the AI policy against all intersecting organizational policies | AI Governance Lead |
| Policy Alignment Review Record | Documented analysis of conflicts, gaps and resolutions | AI Governance Lead / Compliance |
| Updated Related Policies | Revised versions of policies amended to reflect AI obligations | Individual policy owners |

#### How to Audit

**Document Review:**
- Verify a policy interaction map or equivalent analysis exists and is current
- Sample two or three related policies and check they do not contradict the AI policy
- Confirm amendments to related policies were formally approved and version controlled
- Check that review cycles across related policies are coordinated

**Personnel Interviews:**
- Ask the AI Governance Lead: "Which other policies does the AI policy interact with, and how were conflicts resolved?"
- Ask a policy owner such as the CISO or DPO: "Was your policy reviewed when the AI policy was introduced?"

**Evidence Required**
- Policy interaction map or cross-policy analysis
- Records of the alignment review and decisions taken
- Version history of amended policies showing AI-related changes
- Coordinated policy review schedule

**Common Gaps Found in Audits**
- AI policy written in isolation by a single team with no reference to existing policies
- Direct contradictions between the AI policy and the data protection or security policy
- Related policies never updated after the AIMS was implemented
- No named owner for resolving conflicts where two policies overlap

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 17 (Quality management system) |
| NIST AI RMF | GOVERN 1.1, GOVERN 2.1 |
| ISO 27001:2022 | A.5.1 (Policies for information security) |

---

### A.2.4 — Review of the AI Policy

**Control Statement:** The AI policy shall be reviewed at planned intervals, and additionally whenever significant changes occur, to ensure its continuing suitability, adequacy and effectiveness.

---

#### What It Means

A.2.4 makes policy review an explicit, auditable obligation rather than an assumption. The AI policy must be re-examined on a defined schedule and also triggered by events: new regulation, a material change in how the organization uses AI, an AI incident, a merger, or the adoption of a new class of technology such as generative AI or autonomous agents.

#### Why It Matters

AI is one of the fastest-moving risk domains in the organization. A policy written before a major regulatory or technological shift becomes actively misleading, giving staff false assurance that they are compliant. This is among the most frequently raised nonconformities in AIMS audits, because organizations write a strong policy during certification preparation and then never revisit it.

#### How to Implement

- **Define the review interval** — Set a minimum frequency, typically annual, and record it in the policy itself.
- **Define the trigger events** — Specify what forces an off-cycle review: regulatory change, significant AI incident, new high-risk AI system, change of scope, adoption of a new AI capability, or findings from audits.
- **Assign the reviewer and the approver** — Name who conducts the review and who has authority to re-approve the policy.
- **Record the outcome even when nothing changes** — A review that concludes no amendment is required is still a review and must be evidenced.
- **Feed the review into management review** — Link the policy review to the Clause 9.3 management review so top management formally considers its continued suitability.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Policy Review Procedure | Defines review frequency, triggers, roles and approval route | AI Governance Lead |
| AI Policy Review Record | Dated record of each review, findings and decisions | AI Governance Lead |
| Policy Version History | Change log showing revisions, rationale and re-approval | Document Controller |
| Management Review Minutes | Evidence that top management considered the AI policy | Top Management |

#### How to Audit

**Document Review:**
- Confirm the policy states its review interval and that the interval has been honoured
- Check review records exist for each cycle, including reviews concluding no change was needed
- Verify off-cycle reviews were triggered by relevant events such as new regulation or incidents
- Confirm re-approval was given by an appropriate authority and the version history is complete

**Personnel Interviews:**
- Ask the AI Governance Lead: "When was the policy last reviewed, what prompted it, and what changed?"
- Ask top management: "How does the AI policy reach you for review, and what did you challenge?"

**Evidence Required**
- Dated and signed policy review records
- Version history with change rationale and approver
- Evidence of event-triggered reviews
- Management review minutes referencing the AI policy

**Common Gaps Found in Audits**
- Policy has a stated annual review cycle that has demonstrably lapsed
- No record kept when a review concludes that no change is required
- Reviews are administrative re-dating exercises with no substantive challenge
- Major regulatory or technology changes did not trigger a review

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 17 (Quality management system); Art. 9 (Risk management as a continuous process) |
| NIST AI RMF | GOVERN 1.1, GOVERN 1.2, MANAGE 4.1 |
| ISO 27001:2022 | A.5.1 (Policies reviewed at planned intervals) |

---

## DOMAIN A.3 — INTERNAL ORGANIZATION
*2 Controls | Establishing accountability structures and safe escalation routes for AI*

---

### A.3.2 — AI Roles and Responsibilities

**Control Statement:** The organization shall define, assign, and communicate AI governance roles and responsibilities, ensuring accountability for AI risk management, ethical AI, and AIMS implementation is clearly allocated at appropriate levels.

---

#### What It Means

A.3.2 requires that the organization structures its human governance infrastructure for AI — defining who is responsible for what, at every level from the board to the ML engineer. Without clear role definition, accountability falls into gaps and governance decisions are made inconsistently or not at all.

#### Why It Matters

AI governance failures frequently occur not because policies don't exist, but because no one is clearly accountable for implementing them. Role clarity is especially important for: AI deployment decisions (who can approve going to production?); AI incident response (who leads it?); ethics review (who performs it and with what authority?); board-level AI oversight (does it exist?).

#### How to Implement

- **Define the AI governance structure** — Establish an AI Governance Committee or equivalent body with executive sponsorship. Define its mandate, membership, and decision-making authority.
- **Assign AI-specific roles** — Including: AI Governance Lead (overall AIMS accountability); AI Risk Manager; Model Owners (per-system accountability); Data Governance Lead; Privacy/DPO; Internal Audit (AI-specific capability).
- **Create a RACI matrix** — Roles vs. key AI governance activities (impact assessment, model approval, incident response, audit). Assign: Responsible, Accountable, Consulted, Informed.
- **Define role profiles** — For each governance role: responsibilities; required competencies; authority limits; escalation paths.
- **Communicate assignments** — Individuals must know what they are responsible for.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Governance Structure Document | Describes governance bodies, mandates, membership, and authority | AI Governance Lead |
| AI Governance RACI Matrix | Maps governance roles to key activities with R/A/C/I assignments | AI Governance Lead |
| Role Profiles for AI Governance Roles | Detailed descriptions of responsibilities, competencies, and authority | HR / AI Governance Lead |
| AI Governance Committee Terms of Reference | Charter for the AI Governance Committee | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify governance structure documentation exists with executive-level sponsorship
- Check RACI matrix covers all key AI governance activities
- Confirm role profiles exist for all defined AI governance roles

**Audit Testing:**
- Trace an AI deployment: who approved it? Did they have the authority? Is approval documented?

**Evidence Required**
- AI governance structure document
- RACI matrix (current, covers all live AI systems and key activities)
- Role profiles for key AI governance roles
- AI Governance Committee meeting minutes

**Common Gaps Found in Audits**
- RACI matrix incomplete for incident response and ethics review
- "AI Governance Lead" is a title without a defined mandate or authority limits
- Model Owners don't know they are model owners or what their responsibilities are
- No board-level AI oversight role

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 26 (Deployer obligations); Art. 9 (Risk management) |
| NIST AI RMF | GOVERN 2.1, GOVERN 2.2 |
| ISO 27001:2022 | A.5.2 (Information security roles and responsibilities) |

---

### A.3.3 — Reporting of Concerns

**Control Statement:** The organization shall provide a mechanism through which personnel and other interested parties can report concerns about the organization's AI systems, in a manner that is accessible and protects the person raising the concern.

---

#### What It Means

A.3.3 requires a defined, usable route for raising worries about AI — covering safety, fairness, bias, misuse, unlawful or unethical behaviour, or an AI system simply not performing as claimed. It applies to internal staff and, where relevant, to external parties such as contractors, users and affected individuals. Critically, the mechanism must protect the reporter, which in practice means offering confidentiality or anonymity and guaranteeing freedom from retaliation.

#### Why It Matters

The people closest to an AI system are usually the first to notice that something is wrong, but they will only speak up if it is safe and straightforward to do so. Many of the most damaging publicly reported AI failures were foreseen internally by engineers or domain experts whose concerns had no route upward, were dismissed, or carried a career cost. A functioning reporting channel converts scattered private doubts into early, actionable governance signal, and it is increasingly expected by regulators as evidence of a genuine speak-up culture.

#### How to Implement

- **Provide a clearly identified channel** — This can extend an existing whistleblowing or ethics hotline, but AI concerns must be an explicitly named category so people recognise it applies to them.
- **Allow confidential and anonymous reporting** — Give reporters a genuine choice, and make sure anonymous reports are still triaged seriously.
- **Guarantee non-retaliation** — State the protection explicitly in policy, and make clear that it covers concerns raised in good faith even if they turn out to be unfounded.
- **Define triage, ownership and timescales** — Specify who receives reports, how they are assessed for severity, target response times, and the escalation path to the AI governance function or board.
- **Route serious concerns into the risk and incident processes** — Concerns that indicate real harm should feed the AI risk register and the incident response procedure rather than being handled informally.
- **Close the loop with the reporter** — Tell the reporter what happened, so far as confidentiality permits, or the channel will fall into disuse.
- **Publicise it and keep records** — Cover it in onboarding and AI training, and retain records of every concern, its assessment and its outcome.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Concern Reporting Procedure | Defines channels, triage, timescales, escalation and protections | AI Governance Lead / Compliance |
| Non-Retaliation Statement | Formal protection for those raising concerns in good faith | HR / Legal |
| AI Concerns Register | Log of concerns raised, assessment, actions and outcomes | AI Governance Lead |
| Awareness and Training Material | Evidence that staff are told the channel exists and how to use it | HR / Communications |

#### How to Audit

**Document Review:**
- Verify a documented reporting procedure exists and explicitly covers AI-related concerns
- Confirm anonymous or confidential routes are available and functioning
- Check the non-retaliation commitment is formally documented
- Inspect the concerns register: were reports triaged, actioned and closed within defined timescales?
- Confirm serious concerns were escalated into the risk register or incident process

**Personnel Interviews:**
- Ask a sample of staff: "If you thought one of our AI systems was producing unfair or unsafe results, what would you do?"
- Ask the AI Governance Lead: "How many AI concerns were raised in the last 12 months and what happened to them?"
- Ask HR: "What protection does someone have if they raise a concern that turns out to be wrong?"

**Evidence Required**
- Documented AI concern reporting procedure
- Records of concerns raised, with triage and resolution history
- Non-retaliation policy statement
- Communication and training records showing staff awareness
- Escalation records where concerns fed the risk or incident process

**Common Gaps Found in Audits**
- A general whistleblowing line exists but AI is never mentioned, so staff do not realise it applies
- No anonymous option, so reporters must expose themselves to raise a concern
- Zero concerns ever recorded, which usually signals distrust rather than an absence of issues
- Concerns are received but there is no register, triage criteria or defined response time
- Reporters are never told the outcome, so confidence in the channel erodes

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 26 (Deployer obligations); Art. 73 (Reporting of serious incidents); Whistleblower protection under Directive (EU) 2019/1937 |
| NIST AI RMF | GOVERN 4.1, GOVERN 4.2, GOVERN 4.3 |
| ISO 27001:2022 | A.6.8 (Information security event reporting) |

---

## DOMAIN A.4 — RESOURCES FOR AI SYSTEMS
*5 Controls | Identifying and managing the data, tooling, computing and human resources that AI systems depend on*

---

### A.4.2 — Resource Documentation

**Control Statement:** The organization shall identify and document the resources required for each stage of the AI system life cycle, so that the resources necessary to develop, deploy, operate and maintain AI systems responsibly are known and planned.

---

#### What It Means

A.4.2 is the umbrella control for the whole of Domain A.4. It requires the organization to write down, per AI system and per life cycle stage, what resources it depends on. Those resources fall into four categories that the remaining controls in this domain expand upon: data (A.4.3), tooling (A.4.4), systems and computing (A.4.5), and human resources (A.4.6). The intent is that resource needs are deliberately identified rather than discovered when something fails.

#### Why It Matters

Undocumented resource dependencies are a common root cause of AI failures. If nobody has recorded that a model depends on a particular third-party API, a specific data feed, or one engineer's undocumented knowledge, the organization cannot assess concentration risk, plan continuity, or budget realistically. Auditors use this control to test whether AI is being run as a managed capability or as a collection of undocumented projects.

#### How to Implement

- **Document resources per AI system** — For each system in the AI inventory, record the data, tools, infrastructure and people it depends on across its life cycle.
- **Cover every life cycle stage** — Requirements, design, development, verification, deployment, operation, monitoring and retirement each have distinct resource needs.
- **Identify single points of failure** — Flag dependencies on one vendor, one dataset or one individual, and record the mitigation.
- **Link to budget and capacity planning** — Resource documentation should feed the AIMS resource plan and the annual planning cycle.
- **Keep it current** — Update the documentation when systems change, and review it as part of the change control process.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AIMS Resource Plan | Consolidated view of human, financial, data and infrastructure resources for the AIMS | AI Governance Lead |
| AI System Resource Register | Per-system record of data, tooling, compute and people dependencies | AI System Owners |
| Dependency and Continuity Analysis | Identification of single points of failure and mitigations | AI Governance Lead / IT |

#### How to Audit

**Document Review:**
- Confirm resource documentation exists and covers all systems in the AI inventory
- Check that all four resource types are addressed: data, tooling, compute, people
- Verify the documentation spans the full life cycle, not just development
- Confirm it is version controlled and has been updated as systems changed

**Personnel Interviews:**
- Ask an AI System Owner: "What does this system depend on to keep running, and where is that written down?"
- Ask the AI Governance Lead: "How do resource needs for AI feed into your planning and budget cycle?"

**Evidence Required**
- Documented resource register covering in-scope AI systems
- Evidence of linkage to budgeting and capacity planning
- Change records showing resource documentation is maintained
- Dependency analysis identifying critical resources

**Common Gaps Found in Audits**
- Resources documented for development only, with operations and monitoring ignored
- No record of third-party dependencies such as model APIs or data feeds
- Documentation created once at certification and never updated
- Key person dependencies well known informally but never formally recorded

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 17 (Quality management system); Art. 11 (Technical documentation) |
| NIST AI RMF | GOVERN 1.2, MAP 1.1, MAP 3.1 |
| ISO 27001:2022 | A.5.9 (Inventory of associated assets) |

---

### A.4.3 — Data Resources

**Control Statement:** The organization shall document and manage the data resources used for its AI systems, including their origin, intended purpose, and the requirements they must satisfy.

---

#### What It Means

A.4.3 treats data as a governed resource of the AI system rather than as raw material. It requires the organization to know which datasets underpin each AI system, where they came from, what they may legitimately be used for, and what quality and legal constraints attach to them. It is the resource-planning counterpart to the deeper data controls in Domain A.7.

#### Why It Matters

Data is the most common source of AI risk. Models trained on data the organization had no right to use create legal exposure; models trained on unrepresentative data create discriminatory outcomes; models fed by a data pipeline nobody owns fail silently when that pipeline changes. Documenting data resources is the precondition for controlling any of these risks.

#### How to Implement

- **Maintain a data inventory per AI system** — Record each dataset used for training, tuning, testing and operation.
- **Record origin and lawful basis** — Capture where data came from, the licence or contractual terms, and the lawful basis for processing personal data.
- **Record intended and prohibited uses** — State explicitly what the dataset may and may not be used for, so it is not silently repurposed.
- **Define quality requirements** — Specify accuracy, completeness, timeliness and representativeness expectations appropriate to the system risk level.
- **Assign data ownership** — Name an accountable owner for each significant dataset.
- **Review on change** — Reassess when a data source, supplier or purpose changes.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Data Inventory | Register of datasets per AI system with origin, purpose and owner | Chief Data Officer / AI System Owners |
| Data Licensing and Lawful Basis Record | Licences, contracts and lawful basis for each dataset | Legal / DPO |
| Data Quality Requirements | Defined quality thresholds per dataset and system risk level | Data Governance Lead |

#### How to Audit

**Document Review:**
- Verify a data inventory exists and reconciles to the AI systems inventory
- Sample datasets and confirm origin, licence and lawful basis are recorded
- Check that intended and prohibited uses are stated
- Confirm data quality requirements are defined and monitored

**Personnel Interviews:**
- Ask a data scientist: "Where did the training data for this model come from and what are you permitted to use it for?"
- Ask the DPO: "How do you assure the lawful basis for personal data used in AI training?"

**Evidence Required**
- AI data inventory mapped to AI systems
- Licence, contract or consent records for datasets
- Documented data quality requirements
- Review records where data sources changed

**Common Gaps Found in Audits**
- Training data provenance unknown, particularly for scraped or vendor-supplied datasets
- Data acquired for one purpose reused for model training with no reassessment
- No named owner for critical datasets
- Quality requirements stated as aspirations with no measurement

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance) |
| NIST AI RMF | MAP 2.3, MEASURE 2.2 |
| ISO 27001:2022 | A.5.9 (Inventory of assets); A.5.34 (Privacy and protection of PII) |

---

### A.4.4 — Tooling Resources

**Control Statement:** The organization shall document and manage the tooling resources used for its AI systems, including development frameworks, libraries, pre-trained models and MLOps platforms, together with their approval, versioning and vulnerability management.

---

#### What It Means

A.4.4 requires the organization to know and govern the tooling its AI systems depend on, and to manage the supply chain risk those tools carry: the open-source ML frameworks (TensorFlow, PyTorch, scikit-learn), pre-trained models (from Hugging Face, model providers, etc.), data science notebooks (Jupyter), and MLOps tools (MLflow, Kubeflow, etc.). Each component carries security vulnerabilities and governance risks.

#### Why It Matters

The AI tool ecosystem contains significant supply chain risk: open-source ML libraries with known CVEs in active use; pre-trained models from public repositories that may contain backdoors, biases, or license restrictions; notebooks with hard-coded credentials; third-party ML tools with excessive data exfiltration.

#### How to Implement

- **Create an approved AI tools and libraries list** — Register of approved ML frameworks, libraries, and tools with approved versions.
- **Implement tool approval process** — New tools require security assessment before use in development or production.
- **Software Composition Analysis (SCA)** — Automated scanning of AI project dependencies for known vulnerabilities. Integrate into CI/CD pipeline.
- **Pre-trained model governance** — For each pre-trained model: document source and version; review license terms for AI training use; assess for known vulnerabilities and bias concerns; maintain in a controlled model registry.
- **Notebook security** — Prevent hard-coded credentials in notebooks. Use secrets management. Review notebooks in code review.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Approved AI Tools and Libraries List | Register of approved ML frameworks, libraries, and tools | CISO / AI Governance Lead |
| Pre-trained Model Registry | Register of all pre-trained models with source, version, license, and security assessment | AI Governance Lead / ML Lead |
| Tool Approval Process | Process for requesting and approving new AI development tools | CISO |
| SCA Scan Results | Automated dependency vulnerability scan results | DevOps / CISO |
| License Compliance Register | AI training license compliance status for pre-trained models and datasets | Legal / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify approved tools list exists and is current
- Check pre-trained model registry — are all in-use models listed with source and license?
- Review SCA scan results — are there unresolved high/critical CVEs?

**Evidence Required**
- Approved AI tools and libraries list
- Pre-trained model registry
- SCA scan results and remediation records

**Common Gaps Found in Audits**
- No approved tools list — developers use whatever libraries they prefer
- Pre-trained models from Hugging Face adopted without any security or license review
- SCA scanning in place for application code but not applied to ML dependencies
- Hard-coded API keys found in notebooks committed to version control

#### Cross-References

| Framework | Reference |
|---|---|
| NIST AI RMF | MAP 5.1, MANAGE 2.2 |
| ISO 27001:2022 | A.8.30 (Outsourced development); A.8.8 (Management of technical vulnerabilities) |

### A.4.5 — System and Computing Resources

**Control Statement:** The organization shall document and manage the system and computing resources required by its AI systems, including compute, storage, networking and development environments, applying protection and capacity management proportionate to the risk of the AI system.

---

#### What It Means

A.4.5 ensures that the technical infrastructure underlying AI systems is appropriately secured and maintained. AI infrastructure has unique security considerations: training data repositories containing sensitive or personal data; GPU compute environments; model artifact storage; MLOps pipelines; production inference infrastructure.

#### Why It Matters

AI infrastructure security failures can lead to: training data exfiltration (personal or proprietary data); model theft or tampering (adversarial modification of model weights); poisoning attacks through compromised training pipelines; unauthorized access to AI production systems leading to manipulation of outputs.

#### How to Implement

- **Create an AI infrastructure inventory** — All infrastructure components supporting AI: cloud GPU instances, training clusters, data lakes, model registries, MLOps platforms, inference endpoints.
- **Apply security standards** — Access controls, encryption at rest and in transit, network segmentation, vulnerability management, and patching.
- **Secure MLOps pipelines** — Treat the training pipeline as a critical system: version control, integrity verification, access controls on pipeline configuration.
- **Protect model artifacts** — Model weights are intellectual property and security-sensitive. Apply access controls, integrity verification, and audit logging.
- **Maintain and patch** — AI infrastructure requires active patching. Define patching cadence and track compliance.
- **Disaster recovery** — For critical AI services, ensure infrastructure is covered by DR plans with defined RTO/RPO.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Infrastructure Inventory | Complete list of AI infrastructure components with classification | CISO / DevOps |
| AI Infrastructure Security Standards | Security requirements applicable to AI infrastructure | CISO |
| AI Infrastructure Access Control Matrix | Who can access what AI infrastructure, with what privilege | CISO / DevOps |
| Patching and Maintenance Records | Evidence of vulnerability management and patching | DevOps |
| AI Infrastructure DR Plan | Disaster recovery provisions for critical AI infrastructure | CISO / DevOps |

#### How to Audit

**Document Review:**
- Verify AI infrastructure inventory exists and is complete
- Check access controls are configured for least privilege
- Review patching records — are AI infrastructure components patched to current standards?

**Evidence Required**
- AI infrastructure inventory
- Access control configuration records
- Patching and vulnerability management records
- DR plan coverage for AI infrastructure

**Common Gaps Found in Audits**
- Training data stored in unsecured S3 buckets or file shares
- Model registry lacks access controls — any developer can overwrite production models
- MLOps pipeline configuration not in version control and not access-controlled
- AI infrastructure excluded from standard vulnerability management processes

#### Cross-References

| Framework | Reference |
|---|---|
| NIST AI RMF | MANAGE 2.2, MAP 5.2 |
| ISO 27001:2022 | A.8.1 (User endpoint devices); A.8.9 (Configuration management) |

---

### A.4.6 — Human Resources

**Control Statement:** The organization shall document and manage the human resources required for its AI systems, including the roles, competences, training and awareness needed to develop, deploy, operate and oversee AI responsibly.

---

#### What It Means

A.4.6 addresses the human capability dimension of AI governance. AI systems require people who understand not just the technical aspects — but also the ethical, legal, and governance dimensions. This control requires systematic assessment of competence gaps and closing them through training and hiring.

#### Why It Matters

Competence gaps are one of the most common root causes of AI governance failures: ML engineers who can train excellent models but don't understand bias evaluation methodology; product managers who approve AI deployments without understanding risk implications; executives who set AI strategy without understanding AI limitations; human reviewers who oversee AI decisions without domain expertise.

#### How to Implement

- **Define required AI competencies** — By role: what does an ML Engineer, Data Scientist, Product Manager, AI Risk Manager, AI Auditor need to know?
- **Conduct competency gap assessments** — Assess current staff against required competencies. Identify gaps.
- **Design training programs** — Role-appropriate training covering: AI concepts and limitations; responsible AI principles; bias and fairness; regulatory requirements (EU AI Act, sector-specific); governance procedures.
- **Evaluate training effectiveness** — Don't just track completion rates. Assess whether training has changed behavior and built genuine capability.
- **Address gaps through hiring and external expertise** — Training alone cannot close all gaps. For specialist roles, consider external recruitment or advisory engagement.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Competency Framework | Required competencies by role for all AI-related positions | HR / AI Governance Lead |
| AI Competency Gap Assessment Records | Documented assessments of individuals against required competencies | HR |
| AI Training Curriculum | Role-appropriate training modules covering all required competency areas | HR / AI Governance Lead |
| Training Completion Records | Evidence of training completion per individual | HR |
| Training Effectiveness Review | Assessment of whether training has achieved competence outcomes | HR / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify a competency framework exists and covers all AI-related roles
- Check gap assessments are current (within last 12 months or when roles change)
- Confirm training records are maintained and complete
- Review training effectiveness evaluation — is it substantive or just completion tracking?

**Personnel Interviews:**
- Ask an ML Engineer: "What training have you had on bias evaluation and fairness? Describe the methodology you use."
- Ask HR: "What AI governance training is required for employees who use AI tools in their work?"

**Evidence Required**
- AI competency framework
- Current competency gap assessments
- Training completion records
- Training effectiveness assessment records

**Common Gaps Found in Audits**
- Competency framework covers technical roles but not governance roles (AI Risk Manager, AI Auditor)
- Gap assessments conducted at onboarding but never updated when roles change
- Training is generic AI awareness and does not address role-specific competencies
- No training effectiveness evaluation — completion = competence assumed

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 26 (Deployer obligations — AI literacy); Art. 4 (AI literacy) |
| NIST AI RMF | GOVERN 2.2, GOVERN 4.1 |
| ISO 27001:2022 | A.6.3 (Information security awareness, education and training) |

---

## DOMAIN A.5 — ASSESSING IMPACTS OF AI SYSTEMS
*4 Controls | Assessing and documenting the impacts of AI on individuals, groups and society*

---

### A.5.2 — AI System Impact Assessment Process

**Control Statement:** The organization shall conduct documented AI System Impact Assessments (ASIAs) for AI systems before deployment and at significant change points, covering potential harms, benefits, ethical implications, and societal impacts.

---

#### What It Means

The ASIA is one of the most important controls in ISO 42001. It requires a structured pre-deployment assessment of every AI system to identify potential harms before they occur. It is the AI equivalent of a Privacy Impact Assessment — but broader, covering harm, ethics, fairness, and societal impact.

#### Why It Matters

AI systems can cause harms not anticipated by their designers: discriminatory outputs affecting protected groups; privacy violations through inference; safety failures in high-stakes contexts; erosion of human autonomy. The ASIA is designed to surface these risks before deployment — when they can still be mitigated.

#### How to Implement

- **Define the ASIA process** — When it is required (all AI systems above a defined risk threshold); who conducts it; who reviews and approves it; how findings are acted upon.
- **Develop an ASIA template** covering: AI system description and purpose; intended beneficiaries; deployment context; risk tier classification; potential harms analysis (by harm type and affected party); benefits assessment; fairness and bias assessment; privacy implications; human oversight adequacy; risk treatment decisions.
- **Conduct the ASIA before deployment** — Must be completed and approved BEFORE a system is approved for production. Post-hoc assessments do not satisfy this control.
- **Act on findings** — ASIAs that identify risks must result in documented risk treatment decisions.
- **Maintain ASIA register** — A register of all completed ASIAs linked to the AI systems they cover.
- **Re-assess at significant change** — Trigger a new ASIA or update when: the system's purpose changes; new data is used; deployment context changes; significant model retraining occurs.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| ASIA Template | Standardized template for conducting AI System Impact Assessments | AI Governance Lead |
| Completed ASIAs | One per AI system, completed before deployment | AI Risk Manager / Model Owner |
| ASIA Register | Register of all completed ASIAs with system, date, outcome, and review date | AI Governance Lead |
| ASIA Review and Approval Records | Evidence of independent review and approval of completed ASIAs | AI Governance Lead / Ethics Committee |

#### How to Audit

**Document Review:**
- Verify ASIA template exists and covers all required domains
- Check ASIA register — is every live AI system covered by a completed ASIA?
- **Critical test:** Compare ASIA completion date to deployment date. Was the ASIA completed BEFORE deployment?

**Personnel Interviews:**
- Ask the AI Risk Manager: "Walk me through the ASIA process. Who initiates it? Who reviews findings? What authority does the reviewer have to halt a deployment?"
- Ask a Model Owner: "What harms were identified in the ASIA for this system? What was done about them?"

**Evidence Required**
- ASIA template
- Completed ASIA for each live AI system
- ASIA register
- Evidence that ASIA completion predates deployment (timestamped documents)
- Evidence that ASIA findings drove risk treatment actions

**Common Gaps Found in Audits**
- ASIA template exists but ASIAs have not been completed for all live AI systems
- ASIAs completed after deployment — governance retrospective rather than prospective
- ASIA harm analysis section is cursory — "no significant harms identified" with no substantive analysis
- ASIA findings not linked to risk register or action plans

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management system for high-risk AI) |
| NIST AI RMF | MAP 1.1, MAP 5.1, MAP 5.2 |
| ISO 27001:2022 | A.5.12 (Classification of information) |

---

### A.5.3 — Documentation of AI System Impact Assessments

**Control Statement:** The organization shall document the results of its AI system impact assessments and retain those records for a defined period, making them available to relevant interested parties where appropriate.

---

#### What It Means

A.5.2 defines the process; A.5.3 governs its output. Every impact assessment must produce a durable, retrievable record that shows what was assessed, who was involved, what impacts were identified, what decisions followed and what mitigations were committed. The record must be retained and, where there is a legal or contractual duty, made available to regulators, customers or affected parties.

#### Why It Matters

An impact assessment that leaves no record is worthless in an audit or an investigation. When an AI system causes harm, the first question asked by a regulator, a court or a customer is what the organization knew and when it knew it. Well-kept impact assessment records are the organization's primary evidence of due diligence; missing or retrospectively created records are treated as an aggravating factor.

#### How to Implement

- **Standardize the record format** — Use a consistent template so every assessment captures scope, methodology, participants, identified impacts, severity, mitigations, residual risk and approval.
- **Record the decision and the approver** — Note explicitly who accepted the residual impact and on what authority.
- **Version the assessments** — Reassessments should build on prior versions so the history of the system's risk profile is visible.
- **Set a retention period** — Define how long assessments are kept, aligned to the operational life of the system plus any statutory limitation period.
- **Control access and disclosure** — Define who may see assessments internally, and the process for releasing them to regulators, customers or the public.
- **Link records to the AI inventory** — Each system in the inventory should point to its current impact assessment.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI System Impact Assessment Template | Standard format ensuring consistent, complete records | AI Governance Lead |
| Completed Impact Assessment Records | Per-system assessment records with approvals | AI System Owners |
| Records Retention Schedule | Retention periods for impact assessments and supporting evidence | Compliance / Records Manager |
| Disclosure Procedure | Process for providing assessments to regulators or customers | Legal / AI Governance Lead |

#### How to Audit

**Document Review:**
- Confirm a standard template is in use and completed consistently across systems
- Sample AI systems from the inventory and verify a current, approved assessment exists for each
- Check that approvals name an individual with appropriate authority
- Verify retention periods are defined and being honoured
- Confirm reassessments are versioned rather than overwriting prior records

**Personnel Interviews:**
- Ask the AI Governance Lead: "Show me the impact assessment for this system and its approval history."
- Ask Legal: "If a regulator requested our impact assessments tomorrow, how would you produce them?"

**Evidence Required**
- Completed, approved and dated impact assessment records
- Retention schedule covering impact assessments
- Version history showing reassessment over time
- Records of any external disclosure

**Common Gaps Found in Audits**
- Assessments performed in workshops but never written up
- Records held in personal drives or chat threads rather than a controlled repository
- No approver recorded, so accountability for accepting residual impact is unclear
- Reassessments overwrite the original, destroying the audit trail
- No retention period defined, so records are deleted or kept indefinitely without basis

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 27 (Fundamental rights impact assessment); Art. 11 and Annex IV (Technical documentation); Art. 18 (Documentation keeping) |
| NIST AI RMF | MAP 5.1, MAP 5.2, GOVERN 1.4 |
| ISO 27001:2022 | A.5.33 (Protection of records); A.5.37 (Documented operating procedures) |

---

### A.5.4 — Assessing AI System Impact on Individuals or Groups of Individuals

**Control Statement:** The organization shall assess and document the potential impacts of its AI systems on individuals and on groups of individuals throughout the system life cycle.

---

#### What It Means

A.5.4 narrows the impact assessment to the people on the receiving end of an AI decision. It requires the organization to work out who is affected, how they could be harmed, and how severely — covering not just the direct user but anyone subject to or affected by the system's output. It explicitly extends to groups, because harms such as discrimination often appear only when outcomes are examined across a protected characteristic rather than case by case.

#### Why It Matters

Individual and group harm is the risk that regulators, courts and the public care about most. AI systems have denied people credit, filtered them out of hiring processes, mispriced their insurance and misidentified them to law enforcement. These harms are rarely visible in aggregate accuracy metrics: a model can be 95 percent accurate overall and still fail systematically for one subgroup. A.5.4 forces that analysis to happen deliberately and before deployment rather than after a complaint.

#### How to Implement

- **Identify all affected parties** — Distinguish users, decision subjects, bystanders and vulnerable groups. The decision subject is frequently not the user.
- **Categorize potential harms** — Consider physical safety, psychological harm, financial loss, discrimination, loss of opportunity, privacy intrusion, loss of autonomy and loss of access to essential services.
- **Assess by subgroup, not just in aggregate** — Analyse outcomes across relevant characteristics such as age, sex, ethnicity, disability and socioeconomic status, within what the law permits.
- **Rate severity, likelihood and reversibility** — An irreversible harm to a small group can outweigh a minor harm to many, and should be scored accordingly.
- **Give particular weight to vulnerable groups** — Children, elderly people, people with disabilities and people in precarious circumstances warrant heightened scrutiny.
- **Involve affected people where practicable** — Consultation, user research or representative panels produce harms that internal teams miss.
- **Define mitigations and residual impact** — Record what will be done, who owns it, and what impact remains after mitigation.
- **Reassess on change** — Repeat when the model, data, population or deployment context changes.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Individual and Group Impact Assessment | Per-system analysis of affected parties, harms, severity and mitigations | AI System Owner / AI Governance Lead |
| Affected Parties Register | Identification of users, decision subjects and vulnerable groups per system | AI Governance Lead |
| Subgroup Outcome Analysis | Evidence of performance and outcome testing across relevant subgroups | Data Science / ML Engineering |
| Stakeholder Consultation Records | Evidence of engagement with or research into affected populations | Product / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify assessments identify decision subjects and not only direct users
- Confirm harm categories extend beyond privacy and security to fairness, autonomy and access
- Check for evidence of subgroup analysis rather than aggregate metrics alone
- Confirm vulnerable groups were explicitly considered
- Verify mitigations have named owners and that residual impact was formally accepted
- Check reassessment occurred after significant model or context changes

**Personnel Interviews:**
- Ask the AI System Owner: "Who is affected by this system's decisions, and what is the worst outcome for them?"
- Ask a data scientist: "How does this model perform for the groups most likely to be disadvantaged by it?"
- Ask the AI Governance Lead: "How did you involve or represent affected people in this assessment?"

**Evidence Required**
- Completed impact assessments covering individuals and groups
- Subgroup performance and outcome testing results
- Records of vulnerable group consideration
- Mitigation plans with owners and residual impact sign-off
- Consultation or user research evidence where applicable

**Common Gaps Found in Audits**
- Assessment considers the customer using the system but ignores the person the system decides about
- Harm analysis limited to data protection, omitting discrimination and loss of opportunity
- Only aggregate accuracy reported, with no subgroup breakdown
- Vulnerable groups not identified at all
- Assessment completed once before launch and never repeated after retraining
- Mitigations listed with no owner, deadline or verification that they were implemented

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 27 (Fundamental rights impact assessment); Art. 9 (Risk management); Art. 5 (Prohibited practices); Art. 14 (Human oversight) |
| NIST AI RMF | MAP 1.1, MAP 3.3, MAP 5.1, MEASURE 2.11 |
| ISO 27001:2022 | A.5.34 (Privacy and protection of PII) |

---

### A.5.5 — Assessing Societal Impacts of AI Systems

**Control Statement:** The organization shall assess and address the broader societal and ethical implications of its AI systems, including impacts on communities, institutions, human autonomy, and social cohesion beyond direct individual harms.

---

#### What It Means

A.5.5 extends impact assessment beyond direct individual harm to consider macro-level societal and ethical implications: systemic effects at population scale; environmental impact of large AI model training; impacts on human autonomy and agency; effects on labor markets and employment; concentration of power implications.

#### Why It Matters

Individual-level harm assessments can miss systemic harms. A system that causes a small individual impact multiplied across millions of users can have profound societal effects. AI systems that individually seem low-risk can collectively reshape labor markets, democratic processes, or social trust in institutions.

#### How to Implement

- **Extend the ASIA societal section** — Include specific analysis of: scale effects; effects on labor and employment; environmental impact (compute carbon footprint for large models); effects on human autonomy; third-party and community impacts; potential for misuse at scale.
- **Ethics review** — For high-risk AI, conduct an independent ethics review that specifically examines societal implications.
- **Environmental assessment for large models** — Large language models and foundation models require specific assessment of training and inference carbon footprint.
- **Stakeholder engagement** — Consider engaging affected communities or their representatives in impact assessment where feasible.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| ASIA Societal Impact Section | Template section covering societal and ethical implications | AI Governance Lead |
| Ethics Review Records | Independent ethics review findings for high-risk AI systems | AI Governance Lead / Ethics Committee |
| Environmental Impact Assessment | Carbon and energy impact assessment for large AI models | AI Governance Lead / Sustainability Lead |
| Stakeholder Engagement Records | Evidence of engagement with affected communities where conducted | AI Governance Lead |

#### How to Audit

**Document Review:**
- Review the societal section of completed ASIAs — is it substantive or marked "N/A"?
- Check whether environmental impact has been assessed for any large AI models in use
- Review ethics review records for high-risk AI systems

**Evidence Required**
- Completed societal impact sections in ASIAs
- Ethics review records
- Environmental impact assessments (for large models)

**Common Gaps Found in Audits**
- Societal impact section of ASIA is blank or marked N/A for systems with significant scale
- No environmental impact assessment for large language models
- Ethics review covers data privacy but does not extend to broader societal dimensions

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Recital 27 (Societal impacts) |
| NIST AI RMF | MAP 1.5, MAP 1.6 |

---

## DOMAIN A.6 — AI SYSTEM LIFE CYCLE
*9 Controls | Governing responsible design, development, verification, deployment and operation of AI systems*

---

### A.6.1.2 — Objectives for Responsible Development of AI Systems

**Control Statement:** The organization shall identify and document the objectives that guide the responsible development of its AI systems, and ensure those objectives are taken into account across the development life cycle.

---

#### What It Means

A.6.1.2 requires management to state, up front, what responsible development actually means for this organization. These objectives translate the abstract commitments in the AI policy — fairness, safety, transparency, accountability, privacy, robustness, environmental impact — into named goals that development teams are expected to design towards and be measured against.

#### Why It Matters

Without stated objectives, responsible AI collapses into individual judgement. Two teams in the same organization will make opposite trade-offs between accuracy and explainability, or between speed and safety testing, and neither can be said to be wrong. Documented objectives give designers a reference point, give reviewers a basis for challenge, and give auditors something concrete to test development decisions against.

#### How to Implement

- **Derive objectives from the AI policy and ethics framework** — They should be a direct, traceable expression of stated organizational commitments, not a separate list.
- **Make them specific enough to design against** — "Be fair" is not an objective; "no material disparity in approval rates across protected groups beyond a defined threshold" is.
- **Cover the recognised responsible-AI dimensions** — Typically fairness, safety, security, robustness, transparency and explainability, privacy, human oversight, accountability, and increasingly environmental footprint.
- **Set them proportionate to risk** — A high-risk system affecting access to credit or employment warrants tighter objectives than an internal productivity tool.
- **Assign ownership and measures** — Each objective needs an owner and a way of telling whether it was met.
- **Communicate them to development teams** — Objectives that live only in a governance document have no effect on what gets built.
- **Review them** — Reassess as regulation, technology and organizational risk appetite change.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Responsible AI Development Objectives | Documented objectives with measures, owners and risk-based tiering | AI Governance Lead |
| AI Ethics Framework | Principles from which the objectives are derived | AI Governance Lead / Ethics Committee |
| AI Objectives Register | Objectives, KPIs, targets and achievement tracking | AI Governance Lead |
| Design Review Records | Evidence that objectives were considered at design checkpoints | AI System Owners |

#### How to Audit

**Document Review:**
- Verify documented responsible development objectives exist and trace back to the AI policy
- Check objectives are specific and measurable rather than aspirational statements
- Confirm they are tiered according to system risk
- Inspect design and gate review records for evidence the objectives were actually applied
- Confirm objectives have owners and are reviewed periodically

**Personnel Interviews:**
- Ask a developer or ML engineer: "What responsible AI objectives apply to the system you are building, and how do you know you met them?"
- Ask the AI Governance Lead: "How do these objectives change the design of a high-risk system compared with a low-risk one?"

**Evidence Required**
- Documented and approved responsible development objectives
- Traceability from the AI policy and ethics framework to the objectives
- Design review or gate records referencing the objectives
- Measurement results against objective targets
- Review records showing objectives are kept current

**Common Gaps Found in Audits**
- Objectives exist only as ethical principles with no measurable expression
- Development teams are unaware the objectives exist
- The same objectives applied identically to trivial and high-risk systems
- No evidence that objectives influenced any actual design decision
- Objectives never reviewed after major regulatory or technology change

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management system); Art. 17 (Quality management system) |
| NIST AI RMF | GOVERN 1.1, GOVERN 3.2, MAP 1.4 |
| ISO 27001:2022 | Clause 6.2 (Information security objectives) |

---

### A.6.1.3 — Processes for Responsible AI System Design and Development

**Control Statement:** The organization shall define and implement documented processes for the responsible design and development of AI systems, covering the activities, checkpoints and approvals that apply across the development life cycle.

---

#### What It Means

A.6.1.3 requires that AI development follows a structured, repeatable process — not an ad hoc, individual-driven activity. This includes version control for all model artifacts, code review checkpoints, and documented development practices that ensure responsible AI considerations are embedded throughout development, not just at the end.

#### Why It Matters

Uncontrolled AI development produces systems that are difficult to reproduce, audit, or investigate when something goes wrong. Version control of model artifacts (not just code) is still an immature practice in many organizations — making it impossible to reproduce a training run, understand what changed between model versions, or roll back to a prior version.

#### How to Implement

- **Define an AI Development Lifecycle (ADLC) procedure** — Stages, activities, responsible parties, and outputs for each stage of AI development.
- **Version control for all artifacts** — Code, configuration, training data references, model weights, and experiment records must all be version-controlled.
- **Checkpoint reviews** — Define mandatory technical review checkpoints: data validation checkpoint; model development review; pre-evaluation review; pre-deployment review.
- **Reproducibility** — Ensure a training run can be reproduced: fixed random seeds; versioned training data references; versioned code and configuration.
- **Experiment tracking** — Track all experiments: parameters, metrics, training data version, model version.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Development Lifecycle Procedure | Defined ADLC stages, activities, and review checkpoints | AI Governance Lead / ML Lead |
| Version Control Configuration | Configuration of version control for model artifacts | DevOps / ML Lead |
| Code Review Records | Documentation of technical review checkpoints | ML Lead |
| Experiment Tracking Records | Records of all model training experiments | ML Engineer |

#### How to Audit

**Document Review:**
- Verify ADLC procedure exists and is followed
- Check version control is in use for model artifacts (not just code)

**Audit Testing:**
- Ask: "Can you reproduce the last training run for this model?" Have them demonstrate.
- Check experiment tracking records for a live model — can you see the history of model versions?

**Evidence Required**
- ADLC procedure document
- Version control repository showing model artifacts
- Experiment tracking records
- Code/model review records

**Common Gaps Found in Audits**
- Version control applied to code but not to model weights, training data references, or configuration
- No experiment tracking — model history cannot be reconstructed
- Checkpoint reviews defined on paper but not consistently conducted

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 17 (Quality management) |
| NIST AI RMF | MAP 2.2, MANAGE 1.2 |

---

### A.6.2.2 — AI System Requirements and Specification

**Control Statement:** The organization shall specify and document the requirements for each AI system, including its intended purpose, functional and performance requirements, and the responsible-AI requirements it must satisfy.

---

#### What It Means

A.6.2.2 requires that responsible AI principles are translated into concrete, measurable design requirements before development begins — not as an afterthought. Just as software engineering defines functional requirements before coding, AI governance requires responsible AI requirements to be defined at the design stage.

#### Why It Matters

AI systems designed without explicit fairness, transparency, and safety requirements tend to optimize for performance metrics alone, at the expense of responsible AI properties. By the time bias or explainability gaps are discovered post-deployment, remediation is expensive and harm may already have occurred.

#### How to Implement

- **Develop a Responsible AI Requirements Template** — Define required responsible AI considerations for every AI system: fairness criteria (which protected attributes must be evaluated?); explainability requirements (what level of explanation is needed for this use case?); privacy requirements (data minimization, purpose limitation); safety requirements (what failure modes must be mitigated?); security requirements (adversarial robustness requirements).
- **Make requirements specific and measurable** — "AI must be fair" is not a requirement. "The false positive rate must not differ by more than 5% between protected groups" is a requirement.
- **Require sign-off before development begins** — The requirements document must be approved before the development sprint begins.
- **Link to evaluation criteria** — Design requirements must be traceable to the evaluation and testing phase (A.6.2.6, A.6.2.8).

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Responsible AI Requirements Template | Standardized template for defining responsible AI requirements per system | AI Governance Lead |
| AI System Requirements Specifications | Completed responsible AI requirements for each AI system | Model Owner / AI Governance Lead |
| Requirements Approval Records | Evidence of approval of requirements before development | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify requirements template exists and covers all responsible AI dimensions
- Check requirements specifications exist for all live AI systems
- Confirm requirements were approved before development (date check)
- Verify fairness requirements are specific and measurable — not generic statements

**Evidence Required**
- Responsible AI requirements template
- Completed AI system requirements specifications
- Approval records predating development start

**Common Gaps Found in Audits**
- Requirements template addresses functional requirements but not responsible AI properties
- Fairness requirements are generic ("AI will be fair") not measurable
- Requirements defined after development begins — not influencing design
- Requirements not linked to evaluation criteria — no way to verify they are met

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 13 (Transparency and provision of information) |
| NIST AI RMF | MAP 1.1, MAP 2.1 |

---

### A.6.2.3 — Documentation of AI System Design and Development

**Control Statement:** The organization shall document the design and development of each AI system, including the design decisions taken, the rationale for them, and the alternatives considered.

---

#### What It Means

A.6.2.3 requires that AI systems are documented in sufficient technical detail to enable independent understanding, evaluation, and audit. Without design documentation, the only person who understands how an AI system works is the person who built it — creating a single point of failure and making governance, maintenance, and audit impossible.

#### How to Implement

- **Create architecture documentation** — System architecture diagrams showing all components, data flows, integration points, and external dependencies.
- **Model design documentation** — For each model: the problem it solves; the modeling approach chosen and rationale; input features and their sources; output format; training approach; key design decisions and rationale.
- **Maintain as the system evolves** — Documentation must be updated when the system changes significantly.
- **Version control documentation** — Store in version control linked to the model version it describes.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI System Architecture Document | Architecture diagrams and component descriptions | ML Engineer / Software Architect |
| Model Design Document | Detailed description of model design, decisions, and rationale | ML Engineer / Model Owner |
| Data Flow Diagrams | Diagrams showing all data inputs, processing, and outputs | ML Engineer |

#### How to Audit

**Document Review:**
- Verify architecture document exists for each AI system
- Check documentation is current — updated after last significant system change
- Confirm data flows are documented — can you trace personal data through the system?

**Evidence Required**
- AI system architecture documents (version-controlled)
- Model design documents
- Data flow diagrams
- Evidence of documentation updates following system changes

**Common Gaps Found in Audits**
- Architecture documented at implementation and never updated after significant changes
- Data flows not documented — cannot trace what data the AI processes
- Design rationale missing — documentation describes what was built but not why

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 11 (Technical documentation for high-risk AI) |
| NIST AI RMF | MAP 1.1, MAP 2.2 |
| ISO 27001:2022 | A.8.9 (Configuration management) |

---

### A.6.2.4 — AI System Verification and Validation

**Control Statement:** The organization shall define and apply verification and validation measures for its AI systems, and retain evidence that those measures were carried out and their acceptance criteria met before the system is released.

---

#### What It Means

Verification asks whether the system was built correctly against its specification; validation asks whether the resulting system actually performs as intended in its real operating context. For AI this goes well beyond conventional software testing: it must cover statistical performance, behaviour across subgroups, robustness under adversarial and out-of-distribution conditions, and behaviour in an environment that genuinely represents production.

#### Why It Matters

AI systems fail in ways that traditional test suites do not detect. A model can pass every unit test while being systematically less accurate for one demographic, collapsing under slightly shifted input distributions, or being trivially manipulated through crafted inputs. Verification and validation evidence is also the artefact regulators ask for first, and it is the organization's principal defence in demonstrating that a failure was not foreseeable and unaddressed.

#### How to Implement

- **Define acceptance criteria before testing** — Set the thresholds the system must meet in advance, so results cannot be rationalised after the fact.
- **Test in representative environments** — Validate against data and conditions that reflect the real deployment population, including the edge cases and rare segments that development datasets typically under-represent.
- **Evaluate for bias across subgroups** — Measure performance and outcomes separately for relevant groups rather than relying on aggregate metrics, and record the fairness metric chosen and why.
- **Conduct adversarial and robustness testing** — Probe for prompt injection, evasion, data poisoning, model extraction and membership inference as applicable to the system type, and test behaviour under distribution shift and degraded inputs.
- **Test the human oversight path** — Verify that reviewers can actually understand, question and override the system's output in practice, not just in principle.
- **Keep validation independent** — The person who built the model should not be the sole party attesting that it passed.
- **Record results and the release decision** — Retain the evidence, the residual issues accepted, and who authorised release.
- **Re-run on material change** — Retraining, a new data source or a new deployment context invalidates prior results.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Verification and Validation Plan | Scope, methods, acceptance criteria and responsibilities per system | AI System Owner / QA |
| Test and Evaluation Results | Performance, subgroup, robustness and adversarial testing evidence | Data Science / ML Engineering |
| Bias Evaluation Report | Subgroup outcome analysis, chosen fairness metrics and mitigations | Data Science / AI Governance Lead |
| Release Approval Record | Documented decision to release, residual issues and approver | AI System Owner / Governance Board |

#### How to Audit

**Document Review:**
- Confirm acceptance criteria were defined before testing and were met, or that deviations were formally accepted
- Verify subgroup and bias evaluation was performed, not just aggregate accuracy
- Check adversarial and robustness testing appropriate to the system type was carried out
- Confirm the test environment and data genuinely represent production conditions
- Verify independence between the build team and the validation sign-off
- Check that retraining or significant change triggered revalidation

**Personnel Interviews:**
- Ask an ML engineer: "What were the pass criteria for this model, and were any missed?"
- Ask the validator: "What would have caused you to block this release?"
- Ask the AI System Owner: "When this model was last retrained, what testing was repeated?"

**Evidence Required**
- Verification and validation plan with pre-defined acceptance criteria
- Test results including subgroup and robustness evidence
- Bias evaluation report with methodology stated
- Release approval records naming the approver
- Revalidation records following material changes

**Common Gaps Found in Audits**
- Only aggregate accuracy reported, with no subgroup breakdown
- Acceptance thresholds set after seeing the results
- Testing performed on a clean development dataset that does not reflect production
- No adversarial or robustness testing for systems clearly exposed to manipulation
- The model developer is also the sole approver of the release
- Model retrained repeatedly with validation performed only for the original version

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 15 (Accuracy, robustness and cybersecurity); Art. 10 (Data governance) |
| NIST AI RMF | MEASURE 2.1, MEASURE 2.5, MEASURE 2.7, MEASURE 2.11 |
| ISO 27001:2022 | A.8.29 (Security testing in development and acceptance) |

---

### A.6.2.5 — AI System Deployment

**Control Statement:** The organization shall define and apply a documented process for deploying AI systems into operational use, including the approval criteria, release conditions, human oversight arrangements and rollback provisions that must be satisfied before and during deployment.

---

#### What It Means

A.6.2.5 requires that deploying an AI system to production is a controlled, authorized, and reversible action. Production deployment should require formal authorization, should follow a documented procedure, and should be designed so that a failed deployment can be quickly reversed.

#### Why It Matters

Uncontrolled AI deployment leads to: unauthorized AI systems in production (governance bypassed); AI systems deployed without completing required assessments; deployment failures with no rollback capability, causing extended outages; no record of what was deployed, when, and by whom.

#### How to Implement

- **Define a deployment authorization process** — Who must approve production deployment? What conditions must be met (ASIA complete, bias evaluation passed, deployment checklist signed)? Document authorization in a deployment request/approval record.
- **Staged rollout** — For high-risk AI: pilot deployment to a subset of users; monitor for unexpected behavior; extend rollout only if pilot performance is acceptable.
- **Rollback capability** — Design deployments so they can be reversed. Maintain the previous model version in the model registry. Test rollback procedure regularly.
- **Post-deployment validation** — After deployment, validate that the system is behaving as expected in production before full rollout.
- **Deployment record** — Maintain a record of every deployment: what was deployed, version, date, deployer, authorizer.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Deployment Procedure | Documented procedure for deploying AI systems to production | AI Governance Lead / DevOps |
| Deployment Authorization Records | Formal approval records for each production deployment | AI Governance Lead |
| Deployment Checklist | Pre-deployment checklist of required conditions | AI Governance Lead |
| Rollback Procedure | Documented procedure for rolling back an AI deployment | DevOps |
| Rollback Test Records | Evidence that rollback has been tested | DevOps |

#### How to Audit

**Document Review:**
- Verify deployment procedure exists
- Check deployment authorization records — were all recent deployments formally authorized?
- Confirm rollback procedure exists and has been tested

**Audit Testing:**
- Select last 5 production deployments. For each: was it authorized? By whom? Was the deployment checklist completed? Is there a deployment record?

**Evidence Required**
- AI deployment procedure
- Deployment authorization records (pre-deployment, not post-hoc)
- Deployment checklist completion records
- Rollback procedure and test evidence

**Common Gaps Found in Audits**
- Deployment authorization is informal — no documented approval record
- Rollback procedure exists but has never been tested
- Deployment checklist items not completed before deployment
- No deployment record — cannot determine what is in production or when it was deployed

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 26 (Deployer obligations) |
| NIST AI RMF | MANAGE 1.1, MANAGE 3.1 |
| ISO 27001:2022 | A.8.32 (Change management) |

---

### A.6.2.6 — AI System Operation and Monitoring

**Control Statement:** The organization shall operate and monitor its AI systems in accordance with defined arrangements, covering ongoing performance, drift, incidents and the eventual retirement of the system.

---

#### What It Means

A.6.2.6 requires ongoing monitoring of AI systems in production. Unlike traditional software where failures are typically binary (working or not), AI failures are often gradual and soft: model performance slowly degrades; data quality issues accumulate; bias increases over time; security incidents affect AI outputs. Monitoring must be designed to detect these AI-specific failure modes.

#### Why It Matters

Without monitoring, AI systems that are degrading go undetected until a visible failure occurs — by which time significant harm may have already been done at scale. AI systems can fail silently: still producing outputs, but outputs that are increasingly wrong, biased, or harmful.

#### How to Implement

- **Define monitoring requirements per AI system** — What metrics must be monitored? At what frequency? What are the alert thresholds? Who receives alerts?
- **Technical monitoring** — Implement dashboards and alerts for: prediction confidence distributions; output distributions (detecting distributional shift); input data quality; latency and throughput; error rates.
- **Operational monitoring** — Track: human override rates; user feedback/complaints; downstream outcomes where trackable.
- **Alert management** — Define what happens when an alert fires: who investigates? What is the escalation path? What is the response SLA?
- **Regular monitoring review** — Periodic review of monitoring data by the model owner and AI governance team.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Monitoring Framework | Defined monitoring requirements per AI system | AI Governance Lead / ML Lead |
| Monitoring Dashboard Configuration | Technical configuration of monitoring dashboards | DevOps / ML Engineer |
| Alert Configuration Records | Alert thresholds and escalation paths | DevOps / AI Governance Lead |
| Monitoring Review Records | Evidence of periodic monitoring data review | Model Owner / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify monitoring framework exists and covers all production AI systems
- Check alert configuration — are alerts defined and operational?
- Review monitoring review records — are they being conducted?

**Audit Testing:**
- Pull up the monitoring dashboard for a production AI system. Are there any unresolved alerts? Who received them? What was done?

**Evidence Required**
- AI monitoring framework
- Monitoring dashboard and alert configuration
- Monitoring review records

**Common Gaps Found in Audits**
- Monitoring limited to infrastructure (server uptime) — no AI-specific metrics
- Alerts configured but no one reviews them
- Monitoring review records do not exist or are superficial

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 72 (Post-market monitoring for high-risk AI) |
| NIST AI RMF | MANAGE 2.4, MEASURE 2.7 |
| ISO 27001:2022 | A.8.16 (Monitoring activities) |

---

### A.6.2.7 — AI System Technical Documentation

**Control Statement:** The organization shall produce and maintain technical documentation for each AI system, sufficient to enable interested parties to understand how the system works, how it was built and evaluated, and the limits of its intended use.

---

#### What It Means

A.6.2.7 requires that every AI model has a standardized documentation artifact — commonly called a "model card" — that provides a transparent, accessible account of what the model does, how well it does it, where it fails, and who should and should not use it. Model cards originated at Google and have become a de facto standard for AI model documentation.

#### Why It Matters

Without model documentation: business users don't understand the model's limitations; governance personnel cannot assess whether the model is being used within its validated scope; auditors cannot determine if the model meets fairness requirements; downstream users inherit undisclosed risks.

#### How to Implement

- **Develop a model card template** — Standardized structure covering: model description and purpose; intended use cases and out-of-scope uses; training data summary; performance metrics overall and disaggregated by relevant subgroups; fairness evaluation results; known limitations and failure modes; environmental impact (training energy/CO2); caveats and recommendations.
- **Populate model cards at deployment** — Model cards must be complete before a model is deployed to production.
- **Maintain a model registry** — All production models listed with links to their model cards.
- **Update on retraining** — When a model is significantly retrained, update the model card.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Model Card Template | Standardized template for model documentation | AI Governance Lead / ML Lead |
| Completed Model Cards | One per model in the model registry | ML Engineer / Model Owner |
| Model Registry | Register of all production AI models with version, status, and model card link | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify model card template exists
- Check model registry — is every production model listed?
- Review a sample of model cards — are performance metrics disaggregated by relevant subgroups?
- Check subgroup fairness metrics are populated — not blank or "not evaluated"

**Evidence Required**
- Model card template
- Completed model cards for all production models
- Model registry

**Common Gaps Found in Audits**
- Model cards exist but subgroup fairness metrics are blank
- Model registry is incomplete — some production models not listed
- Model cards not updated after significant retraining
- Model cards exist for some systems but not all

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 11 (Technical documentation); Art. 13 (Transparency) |
| NIST AI RMF | MAP 1.1, GOVERN 1.5 |

---

### A.6.2.8 — AI System Recording of Event Logs

**Control Statement:** The organization shall determine which events its AI systems record, and shall implement and maintain logging that is sufficient to support traceability, investigation and oversight throughout the system life cycle.

---

#### What It Means

A.6.2.8 requires deliberate decisions about what an AI system records while it runs. Logging must be adequate to reconstruct, after the event, what the system did and on what basis: which model version produced an output, what inputs it received, what confidence it reported, whether a human reviewed or overrode it, and what changed in the system's configuration. Retention must be long enough to be useful to investigators and regulators.

#### Why It Matters

When an AI system produces a harmful or disputed outcome, the organization must be able to explain that specific decision, sometimes years later. Without adequate logs it cannot investigate an incident, cannot respond to an individual exercising a right to explanation or contest, cannot prove that human oversight actually occurred, and cannot detect drift or misuse. Insufficient logging is one of the most consequential and least reversible AI governance failures, because the evidence simply does not exist after the fact.

#### How to Implement

- **Define the events to log per system** — Typically inputs and outputs or their references, model and configuration version, timestamp, confidence or score, the decision taken, and the identity of any human reviewer.
- **Log human oversight actions explicitly** — Record when a human reviewed, approved, modified or overrode an output, so oversight can be evidenced rather than asserted.
- **Log model and configuration changes** — Deployments, retraining, threshold changes and feature updates must be traceable to a time and an authoriser.
- **Set risk-based retention periods** — Align retention to the operational life of the system and any statutory limitation or regulatory requirement, and document the basis.
- **Protect log integrity** — Restrict who can alter or delete logs, and apply tamper-evidence for high-risk systems.
- **Reconcile logging with data protection** — Apply minimisation, pseudonymisation or referencing so that logging does not itself become an unlawful accumulation of personal data.
- **Make logs usable** — Ensure logs can actually be queried to reconstruct an individual decision, not merely stored.
- **Monitor and alert** — Feed logs into monitoring so anomalies, drift and misuse are detected rather than merely recorded.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Logging Standard | Defines events to be logged per system risk tier, formats and retention | AI Governance Lead / IT |
| Log Retention Schedule | Retention periods with legal and operational justification | Compliance / Records Manager |
| Log Access Control Record | Who may read, alter or delete AI logs and how integrity is assured | CISO |
| Traceability Test Evidence | Demonstration that an individual decision can be reconstructed from logs | AI System Owner |

#### How to Audit

**Document Review:**
- Confirm a logging standard exists and specifies events per system or risk tier
- Verify model version and configuration changes are captured
- Check that human oversight actions are logged
- Confirm retention periods are defined, justified and enforced
- Verify log integrity protection and restricted deletion rights
- Confirm logging has been assessed against data protection obligations

**Personnel Interviews:**
- Ask the AI System Owner: "Pick a decision this system made three months ago and reconstruct it for me."
- Ask the CISO: "Who can delete or alter these logs, and how would you know if they had?"
- Ask the DPO: "What personal data ends up in these logs and on what basis is it retained?"

**Evidence Required**
- Documented logging standard and retention schedule
- Sample logs demonstrating decision-level traceability
- Evidence of logged human oversight actions
- Access control and integrity protection configuration
- Records of log review or monitoring alerts

**Common Gaps Found in Audits**
- Only errors and system health are logged, with no record of decisions made
- Model version not recorded, so outputs cannot be attributed to a specific model
- Human review claimed but never logged, so oversight cannot be evidenced
- Logs retained for a short operational period well below the time limit for challenge
- Logs writable or deletable by the same team that operates the model
- Logs technically retained but impossible to query for an individual case

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 12 (Record-keeping and automatic logging); Art. 19 (Automatically generated logs); Art. 26 (Deployer log retention) |
| NIST AI RMF | MEASURE 1.1, MEASURE 2.4, MANAGE 4.1 |
| ISO 27001:2022 | A.8.15 (Logging); A.8.16 (Monitoring activities); A.8.17 (Clock synchronization) |

---

## DOMAIN A.7 — DATA FOR AI SYSTEMS
*5 Controls | Governing the data AI systems are built on, from acquisition through preparation*

---

### A.7.2 — Data for Development and Enhancement of AI Systems

**Control Statement:** The organization shall define and document the data required to develop and enhance its AI systems, including the types, sources and volumes of data needed and the constraints on their use.

---

#### What It Means

A.7.2 is the entry control for Domain A.7. It requires a deliberate, documented answer to a basic question: what data does this AI system need in order to be built, trained, tuned and subsequently improved, and on what terms may that data be used. It covers training, validation and test data, fine-tuning and reinforcement data, and any data used later to enhance a system already in production.

#### Why It Matters

Most serious AI failures trace back to a data decision made early and never examined. Teams frequently use whatever data is convenient, then discover after deployment that it was unrepresentative, unlawfully obtained, or contractually barred from that use. Defining data requirements before collection makes those constraints visible while they can still be acted upon, and gives the organization a defensible account of why it holds the data it holds.

#### How to Implement

- **Specify data requirements per system** — Record the data types, sources, volumes, coverage and refresh frequency the system needs, tied to its intended purpose.
- **Define representativeness expectations** — State which populations and conditions the data must cover so the system performs adequately for everyone it will affect.
- **Record permitted and prohibited uses** — Capture licence terms, contractual restrictions, consent scope and lawful basis, and state explicitly what the data may not be used for.
- **Separate development, validation and test data** — Define how data is partitioned and prevent leakage between the sets.
- **Plan for enhancement data** — Decide in advance whether production data, user feedback or human labelling may be fed back into the system, and under what safeguards.
- **Assess synthetic data explicitly** — Where synthetic data is used, document why, how it was generated and how its fidelity was checked.
- **Review when purpose changes** — A change of purpose requires a fresh assessment of whether the existing data may still lawfully and appropriately be used.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Data Requirements Specification | Per-system definition of data types, sources, volumes and coverage | AI System Owner / Data Science |
| Permitted Use Record | Licence, contract, consent scope and lawful basis per dataset | Legal / DPO |
| Data Partitioning Standard | Rules for separating training, validation and test data | Data Science Lead |
| Enhancement Data Procedure | Rules for reusing production or feedback data to improve systems | AI Governance Lead |

#### How to Audit

**Document Review:**
- Confirm data requirements are documented per AI system and tied to intended purpose
- Verify representativeness expectations are stated, not assumed
- Check permitted and prohibited uses are recorded for each dataset
- Confirm training, validation and test data separation is defined and enforced
- Verify any use of production data for enhancement is authorised and safeguarded

**Personnel Interviews:**
- Ask a data scientist: "What data does this system need, and who decided that?"
- Ask Legal or the DPO: "What are we permitted to do with this dataset, and what are we not?"
- Ask the AI System Owner: "Is production data fed back into this model, and who approved that?"

**Evidence Required**
- Documented data requirements per system
- Licence, contract or consent evidence for each data source
- Data partitioning configuration or procedure
- Approvals for use of production or feedback data in enhancement
- Reassessment records where system purpose changed

**Common Gaps Found in Audits**
- Data requirements never documented, with datasets chosen opportunistically
- Representativeness assumed rather than specified or verified
- Data collected for one purpose reused for training with no legal review
- Test data contaminated with training data, inflating reported performance
- Production data quietly recycled into retraining without authorisation or safeguards

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance) |
| NIST AI RMF | MAP 2.3, MEASURE 2.2 |
| ISO 27001:2022 | A.5.9 (Inventory of assets); A.5.34 (Privacy and protection of PII) |

---

### A.7.3 — Acquisition of Data

**Control Statement:** The organization shall determine and document how data for its AI systems is acquired, ensuring that acquisition is lawful, authorised, and consistent with the terms under which the data was made available.

---

#### What It Means

A.7.3 governs the act of obtaining data, whatever the route: collected directly from users, generated internally, purchased from a broker, licensed from a vendor, scraped from public sources, obtained through a partnership, or produced synthetically. Each route carries different legal, ethical and security conditions, and the organization must be able to show that those conditions were identified and satisfied at the point of acquisition, and that access to the acquired data is properly controlled thereafter.

#### Why It Matters

Acquisition is where the organization's legal exposure is created, and it is largely irreversible. A model trained on improperly acquired data may have to be retrained or withdrawn entirely, and regulators have ordered exactly that. Web-scraped and broker-sourced datasets are the highest-risk category because their lawful basis is frequently untested and their contents unverified. Acquisition is also a security boundary: externally sourced data is an established vector for poisoning attacks.

#### How to Implement

- **Define approved acquisition routes** — State which sources are permitted, which require review, and which are prohibited outright.
- **Establish lawful basis before acquiring** — Confirm consent, contract, legitimate interest or another basis for personal data, and record the assessment.
- **Verify licence and terms compliance** — Check that the source's terms actually permit AI training, which many expressly do not.
- **Apply heightened scrutiny to scraped and brokered data** — Require documented legal review before any such dataset is used.
- **Screen acquired data for integrity and safety** — Check for poisoning, embedded malicious content, unexpected personal data and prohibited content before ingestion.
- **Apply access controls from the point of acquisition** — Restrict who can read, copy, export or delete acquired datasets, applying least privilege and logging access to sensitive data.
- **Apply data minimisation** — Acquire only what the documented requirements justify.
- **Record the acquisition** — Log source, date, terms, approver and the checks performed, so provenance under A.7.5 can be established.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Data Acquisition Procedure | Approved routes, review gates and prohibitions | Data Governance Lead |
| Data Source Approval Records | Per-source legal, ethical and security review and sign-off | Legal / DPO / CISO |
| Data Access Control Matrix | Who may access each dataset, at what privilege level | CISO / Data Owners |
| Acquisition Log | Record of datasets acquired with source, terms, date and approver | Data Governance Lead |

#### How to Audit

**Document Review:**
- Confirm an acquisition procedure exists and defines permitted and prohibited sources
- Sample datasets and verify lawful basis and licence terms were assessed before acquisition
- Check that scraped or purchased datasets received documented legal review
- Verify integrity and safety screening was applied to externally sourced data
- Confirm access controls and logging are applied to sensitive datasets
- Check that acquisition records are complete enough to support provenance claims

**Personnel Interviews:**
- Ask a data engineer: "Where did this dataset come from and what approval did it go through?"
- Ask Legal: "Do the source's terms permit using this data to train a model?"
- Ask the CISO: "Who can access the training data, and how is that access monitored?"

**Evidence Required**
- Documented acquisition procedure and approval gates
- Per-source legal and lawful basis assessments
- Licence agreements or terms evidencing permitted AI use
- Integrity and safety screening results
- Access control configuration and access logs
- Acquisition log entries with approver and date

**Common Gaps Found in Audits**
- Scraped data used for training with no assessment of the source's terms
- Vendor datasets accepted on the vendor's assurance with no independent verification
- No screening of external data for poisoning or unexpected personal data
- Training data accessible to the entire engineering organization
- Acquisition undocumented, making provenance impossible to reconstruct
- Data acquired far beyond the documented requirement, with no minimisation

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance); Art. 53 (GPAI training data transparency) |
| NIST AI RMF | MAP 2.3, MEASURE 2.2, MANAGE 2.2 |
| ISO 27001:2022 | A.5.15 (Access control); A.5.34 (Privacy and protection of PII); A.8.12 (Data leakage prevention) |

---

### A.7.4 — Quality of Data for AI Systems

**Control Statement:** The organization shall define and apply requirements for the quality of data used in its AI systems, and verify that the data meets those requirements before and during use.

---

#### What It Means

A.7.4 recognizes that AI system quality is fundamentally dependent on data quality: "garbage in, garbage out" applies with particular force to AI. This control requires that data quality requirements are defined before training (not just assumed), measured, and verified before data is used for AI development.

#### Why It Matters

Poor data quality in AI training produces unreliable, biased, or dangerous AI outputs: missing data that causes the model to learn from unrepresentative samples; mislabeled training data that causes the model to learn incorrect patterns; biased data that encodes historical discrimination; inconsistent data that reduces model reliability.

#### How to Implement

- **Define data quality dimensions relevant to AI** — Accuracy (labels are correct); Completeness (no critical missing values); Consistency (no contradictory records); Representativeness (data covers the population the model will serve); Timeliness (data is current and reflects the operational environment); Volume (sufficient data for each subgroup being modeled).
- **Set measurable quality thresholds** — Define specific, measurable thresholds for each dimension. "Data must be complete" is not a standard. "Missing values must not exceed 2% for any feature used in the model" is a standard.
- **Conduct pre-training data quality assessment** — Before training a model, assess training data against defined quality standards. Document results.
- **Implement ongoing data quality monitoring** — For AI systems that continuously receive new data, monitor data quality in production.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Data Quality Standards | Defined data quality dimensions and measurable thresholds for AI data | Chief Data Officer / AI Governance Lead |
| Data Quality Assessment Records | Results of data quality assessment per dataset per AI system | ML Engineer / Data Engineer |
| Data Quality Monitoring Configuration | Configuration of ongoing data quality monitoring | Data Engineer / DevOps |

#### How to Audit

**Document Review:**
- Verify data quality standards exist and are measurable (not generic)
- Check data quality assessment records exist for training datasets

**Personnel Interviews:**
- Ask: "How did you verify that training data for this model meets your quality standards? Show me the assessment."

**Evidence Required**
- Data quality standards with specific thresholds
- Data quality assessment results for AI training datasets

**Common Gaps Found in Audits**
- Data quality standards exist for operational databases but not specifically for AI training data
- Quality thresholds are vague — no measurable criteria
- No data quality assessment conducted before training

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance for high-risk AI) |
| NIST AI RMF | MAP 2.3, MEASURE 2.5 |

---

### A.7.5 — Data Provenance

**Control Statement:** The organization shall record and maintain the provenance of data used in its AI systems, so that the origin, chain of custody and permitted uses of that data can be established throughout its life cycle.

---

#### What It Means

A.7.5 requires that organizations know exactly where their AI training data comes from, what transformations it has undergone, and what rights exist to use it. Data provenance is the documented history of data from its origin to its use in AI training. This is essential for: reproducing training runs; investigating model behavior; verifying licensing compliance; responding to GDPR subject access requests; regulatory audit.

#### Why It Matters

Data provenance gaps create serious risks: using data for AI training without the right to do so (copyright or contractual violation); being unable to reproduce a training run when investigating a model failure; being unable to delete an individual's data when required (GDPR right to erasure); discovered use of data obtained unethically (web scraping, unauthorized collection).

#### How to Implement

- **Document data sources for each training dataset** — For every dataset used for AI training: source (internal system, public dataset, purchased, web scraped, synthetic); collection method; collection date; geographic scope; processing and transformation history.
- **Maintain a data lineage record** — Show the transformations applied to data from source to training-ready form.
- **Maintain a data licensing register** — For each external dataset: what license applies? Does the license permit use for AI training? Is commercial use permitted? Is attribution required?
- **Enable reproducibility** — Version training datasets. Store data manifests (lists of data files and versions used for each training run).

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Data Catalog | Catalog of all datasets used for AI training, validation, and testing | Chief Data Officer / ML Lead |
| Data Lineage Documentation | Lineage records showing data transformations from source to training-ready | Data Engineer |
| Data Licensing Register | License terms and compliance status for all external AI training datasets | Legal / Chief Data Officer |
| Training Data Manifests | Version-specific records of data files and versions used for each model training run | ML Engineer |

#### How to Audit

**Document Review:**
- Verify data catalog exists and covers all AI training datasets
- Check data lineage — can you trace data from source to trained model?
- Review licensing register — is licensing confirmed for AI training use?

**Personnel Interviews:**
- Ask: "Can you reproduce the training run for this model? What data was used? Can you show me the manifest?"
- Ask Legal: "Do we have the right to use this external dataset for AI training? Is it in the licensing register?"

**Evidence Required**
- AI data catalog
- Data lineage records
- Data licensing register (with AI training use confirmation)
- Training data manifests

**Common Gaps Found in Audits**
- Training data sources not documented — only the ML engineer knows where data came from
- External datasets used for AI training without confirming the license permits AI training use
- No training data manifests — training runs cannot be reproduced
- Web-scraped data used for AI training without assessment of copyright and terms of service compliance

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance — provenance) |
| NIST AI RMF | MAP 2.3 |

---

### A.7.6 — Data Preparation

**Control Statement:** The organization shall define and document how data is prepared for use in its AI systems, including cleaning, transformation, labelling, feature engineering and the treatment of bias introduced or corrected during preparation.

---

#### What It Means

A.7.6 addresses bias at the data level — distinct from model-level bias evaluation (A.6.2.6). Data-level bias assessment examines whether training data itself contains historical bias, underrepresentation, or skewed labeling that will be learned by the model. Data-level mitigation (resampling, reweighting, relabeling) is often more effective than post-hoc model-level correction.

#### Why It Matters

Historical data frequently encodes historical discrimination: historical hiring data reflects past discriminatory hiring practices; historical lending data reflects redlining and discriminatory lending; historical criminal justice data reflects differential enforcement. Training AI models on this data without bias assessment perpetuates and potentially amplifies historical discrimination at scale.

#### How to Implement

- **Conduct training data bias assessment** — Before training: analyze the distribution of protected attributes in training data; analyze label rates and outcomes by protected group; identify potential proxy variables for protected attributes; assess annotation bias (were labels applied consistently across groups?).
- **Implement data-level mitigations where bias is found** — Options include: resampling (oversampling underrepresented groups); reweighting (adjusting instance weights); relabeling (correcting mislabeled instances); synthetic data augmentation for underrepresented groups; collection of additional representative data.
- **Document mitigation decisions** — What bias was found? What mitigation was applied? Why? What was the effect?
- **Link to model-level bias evaluation** — Data-level bias assessment should inform model-level fairness evaluation criteria (A.6.2.6).

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Training Data Bias Assessment Reports | Results of bias assessment for AI training datasets | ML Engineer / AI Risk Manager |
| Data Bias Mitigation Records | Documented mitigation decisions and implementations | ML Engineer |
| Annotation Bias Assessment | Assessment of label quality and consistency across demographic groups | ML Engineer / Data Annotation Lead |

#### How to Audit

**Document Review:**
- Verify training data bias assessment was conducted before model training (date check)
- Check assessment covers relevant protected attributes
- Review mitigation records where bias was found

**Evidence Required**
- Training data bias assessment reports (per dataset, per AI system)
- Bias mitigation records
- Evidence mitigation was implemented before training

**Common Gaps Found in Audits**
- No data-level bias assessment — bias evaluation happens only at model level
- Assessment limited to checking representation counts — does not analyze label rates by group
- Bias found in training data but no mitigation implemented

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data governance — bias testing) |
| NIST AI RMF | MAP 5.1, MAP 5.2 |

---

## DOMAIN A.8 — INFORMATION FOR INTERESTED PARTIES OF AI SYSTEMS
*4 Controls | Ensuring users, authorities and affected parties receive the information they need*

---

### A.8.2 — System Documentation and Information for Users

**Control Statement:** The organization shall provide users of its AI systems with documentation and information sufficient to understand the system’s capabilities, limitations, intended purpose and appropriate use, including how its outputs should be interpreted.

---

#### What It Means

A.8.2 requires honesty and accuracy in how the organization communicates about its AI systems. This applies to: marketing materials; sales claims; product documentation; internal communications about AI performance; reporting to boards and regulators. AI capabilities must not be overstated, and limitations must not be concealed.

#### Why It Matters

AI capability overclaiming causes real harm: business users make decisions based on inflated performance expectations; procurement decisions are made on the basis of false claims; individuals are affected by AI systems they believed were more accurate than they are; regulators make compliance assessments based on misleading information.

#### How to Implement

- **Maintain verified AI capability sheets** — For each AI system: what does it do? What does it not do? What are its known limitations and failure modes? What performance has been verified in testing?
- **Ensure marketing claims are verified** — Any public claim about AI performance must be verifiable against actual test results. Marketing team must consult AI governance before making performance claims.
- **Produce AI performance fact sheets** — Standardized documents showing actual verified performance metrics for each AI system, available for customers and regulators.
- **Internal capability communication** — Ensure internal stakeholders (product teams, sales, executives) have accurate information about AI system capabilities and limitations.

- **Explain the system in terms the user can act on** — Describe, at a level appropriate to the audience, what drives the system's outputs, what an output does and does not mean, and what the user should do when they disagree with it. Technical interpretability artefacts such as feature attributions support this but are not a substitute for a usable explanation.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Capability and Limitation Sheets | Accurate description of what each AI system does and does not do | AI Governance Lead / Product Owner |
| AI Performance Fact Sheets | Verified performance metrics for each AI system | AI Governance Lead / ML Lead |
| Marketing Claim Review Records | Evidence that marketing claims have been reviewed against actual capabilities | AI Governance Lead / Marketing |

#### How to Audit

**Document Review:**
- Verify capability sheets exist for all AI systems
- Compare marketing claims to actual performance metrics — are they consistent?
- Check performance fact sheets reflect actual test results

**Evidence Required**
- AI capability and limitation documentation
- Performance fact sheets with verified metrics
- Marketing review records

**Common Gaps Found in Audits**
- Marketing materials claim AI accuracy exceeding measured test performance
- No capability limitation documentation — users don't know what the AI can't do
- Performance claims not verified against actual measurements

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 13 (Transparency and provision of information to deployers) |
| NIST AI RMF | GOVERN 1.5, MAP 1.1 |

---

### A.8.3 — External Reporting

**Control Statement:** The organization shall determine its external reporting obligations in relation to its AI systems and shall provide the required reports to the relevant authorities and other external parties within the applicable timescales.

---

#### What It Means

A.8.3 covers the reports the organization owes to the outside world, as distinct from the information it gives to users under A.8.2. This includes registration and conformity submissions to regulators, serious incident notifications, responses to supervisory requests, disclosures to customers under contract, and any transparency reporting the organization has committed to voluntarily. The control requires these obligations to be identified in advance and discharged reliably, rather than discovered under pressure.

#### Why It Matters

External reporting obligations for AI carry hard deadlines and personal and corporate liability. Under the EU AI Act, serious incidents must be reported to authorities within defined and short periods, and providers of high-risk systems have registration duties before placing systems on the market. Organizations that have not mapped these obligations in advance routinely miss them, and a missed statutory notification is treated far more seriously than the underlying incident.

#### How to Implement

- **Map every reporting obligation** — Work through applicable regulation, sector rules and contracts, and record what must be reported, to whom, in what format and by when.
- **Determine the organization's role** — Obligations differ sharply depending on whether the organization is a provider, deployer, importer or distributor of a given system.
- **Assign named accountability** — Each obligation needs an owner and a deputy, because deadlines do not pause for absence.
- **Pre-build the reporting artefacts** — Prepare templates and identify the data that will be needed, so a report can be assembled quickly under time pressure.
- **Define the trigger and escalation path** — Specify what threshold turns an internal incident into a reportable event and who makes that determination.
- **Rehearse it** — Test the reporting path in incident exercises, including the decision to notify.
- **Keep records of what was reported** — Retain submissions, timestamps and correspondence as evidence of compliance.
- **Monitor for change** — AI regulation is moving quickly, so the obligations register needs periodic review.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| External Reporting Obligations Register | All AI reporting duties with recipient, trigger, deadline, format and owner | Compliance / Legal |
| Regulatory Reporting Procedure | How reports are prepared, approved and submitted | Compliance |
| Report Templates | Pre-prepared formats for incident and conformity reporting | Compliance / AI Governance Lead |
| Submitted Reports Archive | Copies of reports with submission evidence and correspondence | Compliance |

#### How to Audit

**Document Review:**
- Verify a register of external reporting obligations exists and reflects current applicable regulation
- Confirm the organization's role per AI system has been determined, since obligations flow from it
- Check each obligation has a named owner and defined deadline
- Confirm reporting triggers and escalation thresholds are documented
- Inspect the archive of submitted reports and check timeliness against deadlines
- Confirm the register has been reviewed as regulation changed

**Personnel Interviews:**
- Ask Compliance: "Which AI reporting obligations apply to us, and what is the shortest deadline among them?"
- Ask the AI Governance Lead: "Who decides whether an incident is reportable, and how quickly?"
- Ask the obligation owner: "Walk me through the last report you submitted."

**Evidence Required**
- External reporting obligations register
- Documented reporting procedure and escalation criteria
- Evidence of reports actually submitted, with dates
- Correspondence with authorities or customers
- Review records showing the register is kept current

**Common Gaps Found in Audits**
- No register of obligations, so duties are identified only when an incident occurs
- Provider versus deployer role never determined, leaving obligations unassigned
- Reporting deadlines unknown to the people who would need to meet them
- No defined threshold for what constitutes a reportable serious incident
- Reporting path never tested, so first use is during a live incident
- No archive of what was reported, making compliance unprovable

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 73 (Reporting of serious incidents); Art. 49 and Art. 71 (Registration in the EU database); Art. 62 (Reporting by deployers); Art. 21 (Cooperation with authorities) |
| NIST AI RMF | GOVERN 4.3, MANAGE 4.1, MANAGE 4.3 |
| ISO 27001:2022 | A.5.5 (Contact with authorities); A.5.31 (Legal, statutory and contractual requirements) |

---

### A.8.4 — Communication of Incidents

**Control Statement:** The organization shall define and apply arrangements for communicating AI system incidents to the interested parties who need to know, within the timescales required by regulation, contract and its own policy.

---

#### What It Means

A.8.4 requires that when an AI system fails, causes harm, or is involved in a significant incident, the organization communicates appropriately. This includes: internal incident communication (to management, board); regulatory notification (to data protection authority, sector regulator, EU AI Office for high-risk AI); individual notification (to affected individuals); public communication (where incident is of public significance).

#### Why It Matters

Inadequate incident communication: delays remediation because relevant parties are not informed; leads to regulatory penalties for failure to notify within required timeframes; erodes trust through perceived concealment; deprives affected individuals of the ability to protect themselves.

#### How to Implement

- **Define AI incident categories** — What constitutes a notifiable AI incident? Types: algorithmic bias causing discrimination; AI decision causing significant individual harm; AI security breach; AI system producing systematically incorrect outputs with significant effect.
- **Define notification requirements per incident category** — Who must be notified? Within what timeframe? With what information? GDPR: 72 hours for personal data breach; EU AI Act: timeline for serious incidents involving high-risk AI.
- **Develop incident communication templates** — Pre-approved templates for: regulatory notification; individual notification; internal escalation; public statement.
- **Maintain a communication log** — Record all notifications made, to whom, when, and content.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Incident Communication Policy | Defines notification requirements by incident type and affected party | AI Governance Lead / Legal |
| AI Incident Communication Templates | Pre-approved templates for regulatory, individual, and internal notifications | Legal / AI Governance Lead |
| Incident Communication Log | Record of all notifications made in connection with AI incidents | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify AI incident communication policy exists and covers all relevant notification types
- Check communication templates are available and pre-approved
- Review incident communication log for any incidents that have occurred

**Personnel Interviews:**
- Ask: "If this AI system produced discriminatory outputs affecting 1,000 customers tomorrow, who would you notify? Within what timeframe? What would you tell them?"

**Evidence Required**
- AI incident communication policy
- Communication templates
- Incident communication log (if incidents have occurred)

**Common Gaps Found in Audits**
- Incident communication policy covers IT incidents but not AI-specific incident types
- No individual notification process — affected individuals not informed of AI incidents affecting them
- Regulatory notification timelines not defined for AI incidents
- No communication templates — response improvised under pressure during incidents

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 73 (Reporting of serious incidents for high-risk AI) |
| NIST AI RMF | MANAGE 3.1, GOVERN 6.2 |
| ISO 27001:2022 | A.5.26 (Response to information security incidents) |

### A.8.5 — Information for Interested Parties

**Control Statement:** The organization shall determine what information about its AI systems needs to be made available to interested parties, including disclosure that a person is interacting with or subject to an AI system, and shall provide that information in an accessible form.

---

#### What It Means

A.8.5 requires that AI is not used to deceive users into thinking they are interacting with a human or with a more capable system than actually exists. This includes: disclosure when chatbots or virtual agents are AI (not humans); disclosure when AI is making or significantly influencing decisions that affect users; disclosure when content is AI-generated.

#### Why It Matters

Undisclosed AI use erodes trust, undermines informed consent, and in some jurisdictions violates legal requirements. Users who don't know they are interacting with AI cannot: make informed decisions about sharing personal information; seek human assistance where needed; exercise their right to challenge automated decisions; understand the limitations of the system they are interacting with.

#### How to Implement

- **Define disclosure requirements per AI system** — What must be disclosed? To whom? When? How (in-interface, in terms of service, on request)?
- **Implement disclosures in user interface** — At the point of interaction: "You are chatting with an AI assistant." "This recommendation is generated by AI." "This decision was made with AI assistance — you have the right to request human review."
- **Test disclosure prominence** — Disclosures should be clear and prominent, not buried in terms of service.
- **Maintain compliance with regulatory disclosure requirements** — EU AI Act requires disclosure when AI systems interact with natural persons; GDPR Art. 13/14 requires information about automated decision-making.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Disclosure Policy | Policy defining disclosure requirements for each AI system | AI Governance Lead / Legal |
| UI/UX Disclosure Evidence | Screenshots or records of AI disclosures in user interfaces | Product Owner |
| Regulatory Compliance Assessment | Assessment of disclosure compliance against applicable regulations | Legal / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify disclosure policy exists
- Review UI/UX evidence — are disclosures present, clear, and prominent?

**Behavioral Testing:**
- Interact with the AI system as a user would. Is it clear you are interacting with AI? Is the disclosure prominent?

**Evidence Required**
- AI disclosure policy
- UI/UX evidence of disclosures (screenshots, recordings)
- Regulatory compliance assessment

**Common Gaps Found in Audits**
- Chatbots do not disclose they are AI — can be mistaken for human agents
- AI disclosure buried in terms of service — not visible during interaction
- AI-generated content not labeled as such
- No disclosure of automated decision-making — individuals unaware AI made or influenced a decision affecting them

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 50 (Transparency obligations for certain AI systems) |
| NIST AI RMF | GOVERN 1.5, MAP 1.1 |

---

## DOMAIN A.9 — USE OF AI SYSTEMS
*3 Controls | Governing how AI systems are actually used in operational contexts*

---

### A.9.2 — Processes for Responsible Use of AI Systems

**Control Statement:** The organization shall define and implement processes for the responsible use of its AI systems, covering permitted and prohibited use, the human oversight that applies, and how erroneous or contested outputs are handled.

---

#### What It Means

A.9.2 addresses operational use of AI — both organizational AI systems and employee use of external AI tools. It requires a clear policy that employees, contractors, and users can understand and follow, covering what they may and may not do with AI.

#### Why It Matters

Without acceptable use policies, employees make their own judgments about what AI use is appropriate — with highly variable and sometimes harmful results: employees sharing confidential data with public AI services; AI used for prohibited purposes; AI outputs used without appropriate human review in high-stakes decisions; IP-protected code generated by AI creating license complications.

#### How to Implement

1. **Map AI use cases by category** — Permitted without restriction; Permitted with conditions (e.g., human review required); Requires approval; Prohibited.
2. **Address employee use of external AI tools** — This is the highest-gap area. Explicitly address: Which external AI tools (ChatGPT, Copilot, Claude, etc.) are permitted; What data categories may and may not be entered; What AI-generated output may be used for; IP considerations.
3. **Address organizational AI system use** — Use cases within and outside validated scope; Requirements for human review; Escalation procedures; Recording requirements for AI-assisted decisions.
4. **Communicate and enforce policy** — Training, intranet publication, and acknowledgment. Technical controls where feasible (block access to prohibited AI services).
5. **Update regularly** — As new AI tools proliferate, update the approved list and conditions.

- **Define the human oversight that applies** — State which decisions require human review, at what level, and what authority the reviewer has to question, modify or override an output. Oversight must be genuine: reviewers need the time, information, competence and standing to disagree, otherwise it becomes rubber-stamping.
- **Define how errors and contested outputs are handled** — Provide a route for users and affected people to flag an incorrect output, specify who investigates, how corrections are made, and how systemic errors are escalated into the incident and risk processes.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| Acceptable Use of AI Policy | Comprehensive policy covering organizational and employee AI use | AI Governance Lead / CISO |
| AI Use Case Register | Register of approved AI use cases with conditions | AI Governance Lead |
| External AI Tools Approved List | List of approved external AI tools and conditions of use | CISO / AI Governance Lead |
| Acceptable Use Training Materials | Training on AI acceptable use for all relevant staff | HR / AI Governance Lead |
| Acceptable Use Acknowledgment Record | Evidence employees have read and acknowledged the policy | HR |
| Policy Violation Log | Record of identified acceptable use policy violations | CISO / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify acceptable use policy exists and explicitly addresses external AI tool use
- Check the approved external AI tools list — is it current?
- Confirm training and acknowledgment records are maintained

**Personnel Interviews:**
- Ask an employee: "Are you allowed to use ChatGPT for work? What data can you put into it?"
- Ask a manager: "If an employee used an unauthorized AI tool and shared confidential data, what would happen?"

**Audit Testing:**
- Survey 5 staff on AI tool use policies — test training effectiveness
- Check network monitoring for access to external AI services

#### Evidence Required

- Acceptable Use of AI policy (current version)
- Approved external AI tools list
- Employee training completion records
- Policy acknowledgment records
- Policy violation log

#### Common Gaps Found in Audits

- Policy exists but was written before generative AI proliferated — does not address LLM tools
- No approved external AI tools list — employees use whatever they wish
- No prohibition on entering confidential data into public AI services
- Policy not enforced — violations known to occur but not addressed

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 26 (Deployer obligations — staff instructions) |
| NIST AI RMF | GOVERN 1.2, GOVERN 6.1 |
| ISO 27001:2022 | A.5.1 (Policies for information security) |

---

### A.9.3 — Objectives for Responsible Use of AI Systems

**Control Statement:** The organization shall identify and document the objectives that govern the responsible use of its AI systems, and shall take those objectives into account when deploying and operating them.

---

#### What It Means

Where A.6.1.2 sets objectives for building AI responsibly, A.9.3 sets them for using it. The organization must state what it is trying to achieve, and what it will not accept, when AI is put to work: the outcomes it expects, the limits it places on reliance, the level of human involvement it requires, and the effects on staff, customers and affected parties that it considers unacceptable.

#### Why It Matters

Organizations routinely deploy AI with an implicit objective, usually efficiency, and no stated counterweight. The result is predictable: reliance grows beyond what the system can support, human review is quietly reduced to meet throughput targets, and quality or fairness degrades without anyone having decided to accept that. Documented use objectives make the trade-off explicit and reviewable, and give staff a legitimate basis to push back when operational pressure conflicts with responsible use.

#### How to Implement

- **State what the organization is optimising for** — Efficiency, consistency, accuracy, accessibility, cost, and where those goals conflict, which one yields.
- **State the limits on reliance** — Define the decisions the organization will not delegate to an AI system regardless of measured performance.
- **Set objectives for human involvement** — Express the intended level of human review in terms that cannot be silently eroded by throughput targets.
- **Include objectives for affected people** — Fair outcomes, ability to contest, availability of a human alternative, and clarity about when AI is involved.
- **Consider the effect on staff** — Deskilling, workload, monitoring and job design are legitimate objectives of responsible use.
- **Make them measurable and assign owners** — Each objective needs a measure, a target and someone accountable.
- **Align them with the AI objectives register** — Use objectives should sit alongside the AIMS objectives set under Clause 6.2 rather than in a separate silo.
- **Review them against reality** — Compare intended use objectives with what monitoring shows is actually happening.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Responsible Use Objectives | Documented objectives for AI use with measures, targets and owners | AI Governance Lead |
| AI Objectives Register | Consolidated AIMS objectives including use objectives | AI Governance Lead |
| Deployment Approval Records | Evidence that use objectives were considered before go-live | AI System Owner |
| Performance Review Reports | Measurement of actual use against stated objectives | AI Governance Lead |

#### How to Audit

**Document Review:**
- Confirm responsible use objectives are documented and distinct from development objectives
- Check objectives are measurable and have named owners
- Verify limits on reliance and required human involvement are explicitly stated
- Confirm objectives address affected people and staff, not only efficiency
- Compare stated objectives against monitoring data to see whether practice matches intent

**Personnel Interviews:**
- Ask the AI System Owner: "What is this system supposed to achieve, and what would count as using it irresponsibly?"
- Ask an operational user: "Have review expectations changed since launch, and who authorised that?"
- Ask the AI Governance Lead: "How do you know the intended level of human involvement is still happening?"

**Evidence Required**
- Documented responsible use objectives with measures and owners
- Deployment records showing objectives were considered
- Monitoring evidence comparing actual use against objectives
- Records of decisions to change reliance or oversight levels
- Review records showing objectives are kept current

**Common Gaps Found in Audits**
- Only efficiency and cost objectives exist, with no counterbalancing limits
- Objectives for use are conflated with objectives for development
- Required human review level stated in policy but contradicted by operational targets
- No measurement of whether use objectives are actually being met
- Objectives never revisited after the system's role expanded

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 26 (Deployer obligations); Art. 14 (Human oversight) |
| NIST AI RMF | GOVERN 1.1, GOVERN 5.1, MANAGE 1.1 |
| ISO 27001:2022 | Clause 6.2 (Objectives and planning to achieve them) |

---

### A.9.4 — Intended Use of the AI System

**Control Statement:** The organization shall ensure that its AI systems are used in accordance with their intended purpose and documented conditions of use, including any limitations specified by the provider of the system.

---

#### What It Means

A.9.4 requires that AI systems are actually used for what they were built, validated and approved for. Every AI system has a defined intended purpose and a set of conditions under which its performance was established: a population, a data distribution, an operating environment, and stated limitations. Using it outside those boundaries invalidates its testing, and the organization must have controls that detect and prevent that drift.

#### Why It Matters

Use outside intended purpose is one of the most common and least detected AI failures, because nothing breaks visibly. A model validated for one customer segment gets applied to another; a triage tool built to prioritise becomes the de facto decision-maker; a system approved for internal drafting ends up producing customer-facing output. The system keeps returning confident results, and its validation evidence no longer means anything. This is also where liability shifts decisively: a deployer that uses a system outside the provider's stated conditions generally assumes the provider's responsibilities.

#### How to Implement

- **Document intended purpose per system** — Record what the system is for, the population and conditions it was validated against, and the outputs it is authorised to produce.
- **Document the limitations explicitly** — Capture what the system must not be used for, including provider-stated restrictions, and make this visible to users rather than buried in technical documentation.
- **Communicate boundaries to users** — Present the constraints at the point of use, not only in onboarding material.
- **Control access by use case** — Where feasible, enforce boundaries technically through configuration, input validation or access restrictions rather than relying on user discipline.
- **Monitor for out-of-scope use** — Track input distributions, request patterns and output uses to detect creeping expansion of the system's role.
- **Require change approval for new uses** — Treat a new use case as a change requiring reassessment, revalidation and re-approval, not as business as usual.
- **Respect provider conditions for third-party systems** — Record the provider's stated intended use and limitations, and verify the organization's deployment stays within them.
- **Reassess periodically** — Confirm at defined intervals that actual use still matches documented intended use.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Intended Use Statement | Per-system purpose, validated conditions, authorised outputs and limitations | AI System Owner |
| AI Model Card | Documentation including intended use and out-of-scope uses | AI System Owner / Data Science |
| Provider Documentation Record | Third-party provider's stated intended use and restrictions | Procurement / AI System Owner |
| Use Monitoring Reports | Evidence of monitoring for out-of-scope or expanded use | AI Governance Lead |
| Change Approval Records | Approvals for new use cases with revalidation evidence | Change Authority |

#### How to Audit

**Document Review:**
- Confirm each AI system has a documented intended purpose and stated limitations
- Verify limitations are communicated to users at the point of use
- Check whether actual observed use matches the documented intended use
- Confirm new use cases went through change control and revalidation
- For third-party systems, verify provider conditions are recorded and respected
- Check monitoring exists for out-of-scope use

**Personnel Interviews:**
- Ask a user: "What is this system not supposed to be used for?"
- Ask the AI System Owner: "Has anyone started using this system for something new since launch?"
- Ask Procurement: "What did the vendor say this product must not be used for?"

**Evidence Required**
- Documented intended use statements and model cards
- Evidence that limitations are surfaced to users
- Monitoring reports covering actual usage patterns
- Change approvals and revalidation records for new use cases
- Provider documentation for third-party systems

**Common Gaps Found in Audits**
- Intended use documented internally but never communicated to the people using the system
- System quietly applied to a population it was never validated for
- Advisory output treated as a decision in practice, with no reassessment
- No monitoring capable of detecting scope creep
- Third-party system used in ways the vendor's terms expressly exclude
- New use cases added without revalidation or approval

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 26 (Deployer obligations, use in accordance with instructions); Art. 25 (Responsibilities along the value chain); Art. 13 (Instructions for use) |
| NIST AI RMF | MAP 1.1, MAP 3.4, MANAGE 1.2 |
| ISO 27001:2022 | A.5.10 (Acceptable use of information and other associated assets) |

---

## DOMAIN A.10 — THIRD-PARTY AND CUSTOMER RELATIONSHIPS
*3 Controls | Managing responsibilities across the AI value chain, suppliers and customers*

---

### A.10.2 — Allocating Responsibilities

**Control Statement:** The organization shall allocate responsibilities for its AI systems across the parties involved in the AI value chain, and shall document that allocation so that each party understands what it is accountable for.

---

#### What It Means

Modern AI systems are rarely built and run by one organization. A typical deployment involves a foundation model provider, a platform or cloud host, an integrator, the deploying organization and sometimes a downstream customer. A.10.2 requires the organization to work out, and write down, who is responsible for what across that chain: data, testing, monitoring, incident handling, transparency and regulatory duties. It is the control that prevents responsibility falling into the gaps between organizations.

#### Why It Matters

Unallocated responsibility is where AI governance fails most reliably. Each party assumes another is monitoring for bias, testing for robustness or handling incident notification, and none is. Regulators have made clear that a deployer cannot discharge its obligations simply by pointing at a vendor, and the EU AI Act sets out explicit rules on how responsibility shifts along the value chain, including circumstances in which a deployer becomes a provider. Establishing this allocation before deployment is far cheaper than establishing it during an incident.

#### How to Implement

- **Map the value chain per AI system** — Identify every party that contributes to or relies on the system, including sub-processors and model providers behind an integrator.
- **Determine each party's regulatory role** — Establish who is provider, deployer, importer or distributor, since obligations follow from that classification and can change if the system is substantially modified or rebranded.
- **Allocate responsibility by activity** — Work through data quality, testing, bias evaluation, security, monitoring, human oversight, logging, incident response, user information and regulatory reporting, and name the responsible party for each.
- **Record it contractually** — Reflect the allocation in contracts and data processing agreements rather than leaving it as a shared assumption.
- **Identify and close the gaps** — Explicitly look for activities nobody has taken responsibility for, which is the point of the exercise.
- **Retain accountability internally** — Responsibility can be delegated to a supplier, but the organization remains accountable to its own regulators and customers; name the internal owner for each outsourced activity.
- **Reassess on change** — Fine-tuning a third-party model, rebranding it or changing its purpose can move the organization's role and obligations.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Value Chain Map | Per-system map of all parties and their contributions | AI Governance Lead |
| Responsibility Allocation Matrix | Activity-by-activity RACI across internal and external parties | AI Governance Lead / Legal |
| Regulatory Role Determination | Documented assessment of provider or deployer status per system | Legal / Compliance |
| Contracts and Data Processing Agreements | Contractual reflection of the agreed allocation | Legal / Procurement |

#### How to Audit

**Document Review:**
- Confirm a value chain map exists for significant AI systems
- Verify the organization's regulatory role has been determined and justified per system
- Check the responsibility matrix covers the full set of governance activities
- Confirm the allocation is reflected in contracts, not just internal documents
- Look for activities with no named responsible party
- Verify roles were reassessed where systems were fine-tuned, rebranded or repurposed

**Personnel Interviews:**
- Ask the AI Governance Lead: "For this system, who monitors for bias in production, and where is that agreed?"
- Ask Legal: "Are we a provider or a deployer for this system, and what changed that determination?"
- Ask the AI System Owner: "Which governance activities do you rely on the vendor to perform?"

**Evidence Required**
- Value chain maps and responsibility allocation matrices
- Documented regulatory role determinations
- Contracts and DPAs reflecting allocated responsibilities
- Internal ownership records for outsourced activities
- Reassessment records following material changes

**Common Gaps Found in Audits**
- Responsibility assumed to sit with the vendor but never agreed or documented
- Provider versus deployer status never assessed, so obligations are unknown
- Bias monitoring, logging or incident notification allocated to nobody
- Fine-tuning a third-party model without recognising the change in regulatory role
- Allocation documented internally but absent from the actual contract

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 25 (Responsibilities along the AI value chain); Art. 26 (Deployer obligations); Art. 16 (Provider obligations) |
| NIST AI RMF | GOVERN 2.1, GOVERN 6.1, GOVERN 6.2, MAP 4.1 |
| ISO 27001:2022 | A.5.19 (Information security in supplier relationships); A.5.2 (Roles and responsibilities) |

---

### A.10.3 — Suppliers

**Control Statement:** The organization shall establish and apply a process for managing suppliers of AI systems, components and services, covering the assessment of supplier risk, the contractual terms agreed, and the ongoing monitoring of supplier performance against those terms.

---

#### What It Means

Before adopting an AI system, API, or service from a third party — whether a vendor AI product, a cloud AI service, an open-source model, or an embedded AI component — the organization must systematically assess the risks. A.10.3 requires this to be documented, structured, and proportionate to the risk level of the third-party AI.

#### Why It Matters

Most organizations today use more third-party AI than they build themselves. Every cloud AI service, every SaaS product with AI features, every pre-trained model adopted from Hugging Face is a third-party AI in scope for A.10.3. These systems carry inherited risks: bias baked into training data the organization never saw; security vulnerabilities in the model or API; regulatory non-compliance in the supplier's practices; data handling practices that conflict with privacy obligations. Governance of third-party AI is one of the most significant gaps in most organizations' AI risk management.

#### How to Implement

1. **Create a third-party AI inventory** — List every third-party AI system in use or under evaluation: vendor AI products (SaaS with AI features); cloud AI APIs (OpenAI, Azure AI, Google AI, AWS AI services); open-source models adopted from repositories; AI components embedded in other procured software.
2. **Define risk classification criteria** — Classify third-party AI by risk level based on: What decisions does it influence? Does it process personal data? What is the scale of use? Is it used in high-stakes contexts? Higher risk = deeper assessment required.
3. **Conduct structured assessments** — For each third-party AI (depth proportionate to risk): Technical performance: Has the supplier provided validated performance metrics? Are they verified for your use case and data? Bias and fairness: What bias evaluation has the supplier conducted? What protected attributes were assessed? What are known limitations? Security: What security certifications does the supplier hold? How is the model/API secured? What are the data handling practices? Privacy: Where is data processed? What data is retained? Is there a DPA available? Regulatory compliance: Is the supplier compliant with EU AI Act where applicable? What is their regulatory status for your jurisdiction? Supplier governance: Does the supplier have an AI governance framework? Are they ISO 42001 certified or working toward it?
4. **Document assessment findings** — Use a standardized assessment template. Record findings, risk ratings, and treatment decisions.
5. **Approval gate** — Third-party AI above a defined risk threshold requires formal approval before adoption.
6. **Ongoing review** — Reassess periodically (annually minimum) and on significant changes.

- **Translate assessment findings into contract terms** — Agree AI-specific clauses covering permitted use of the organization's data (including whether it may be used for the supplier's model training), performance and accuracy commitments, bias testing and reporting obligations, security requirements, audit and evidence rights, incident notification timescales, change notification for model updates, subcontractor and sub-processor disclosure, liability and indemnity, and exit and transition provisions.
- **Monitor suppliers against the terms agreed** — Reassess at a frequency proportionate to risk, track performance and incidents, and require notice of material model changes rather than discovering them through degraded output.
- **Plan for exit** — Record how the organization would migrate away from the supplier, what happens to its data, and what continuity arrangements apply if the service is withdrawn.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| AI Supplier Contract Clauses | Standard AI governance clauses for inclusion in supplier agreements | Legal / Procurement |
| Supplier Monitoring and Review Records | Ongoing performance, incident and change tracking per supplier | Procurement / AI System Owner |
| Exit and Transition Plan | Migration, data return and continuity arrangements per critical supplier | Procurement / IT |
| Third-Party AI Inventory | Complete register of all third-party AI in use or evaluation | AI Governance Lead / Procurement |
| Third-Party AI Risk Assessment Template | Standardized assessment covering all required domains | AI Risk Manager |
| Completed Third-Party AI Assessments | One per third-party AI system assessed, with risk ratings | AI Risk Manager |
| Third-Party AI Approval Register | Record of approval decisions for third-party AI adoption | AI Governance Lead |
| Third-Party AI Risk Register | Live register of risks associated with adopted third-party AI | AI Risk Manager |
| Third-Party AI Review Schedule | Scheduled periodic reassessment dates per third-party AI | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify a third-party AI inventory exists and is complete
- Check assessments exist for all adopted third-party AI
- Confirm approval records predate adoption (not post-hoc)
- Verify periodic reassessments are scheduled and occurring

**Personnel Interviews:**
- Ask Procurement: "When a business unit wants to adopt a new SaaS tool with AI features, what assessment process is triggered?"
- Ask the AI Risk Manager: "What was the highest-risk third-party AI you've assessed? What were the key findings?"
- Ask Legal: "Do you have DPAs with all your cloud AI providers? Can you show me the one for [specific service]?"

**Audit Testing:**
- Select 3 adopted third-party AI systems. For each: verify assessment exists; check assessment was completed before adoption; confirm approval was granted; verify DPA is in place where personal data is processed.
- Identify one high-risk third-party AI (e.g., LLM used for customer-facing application). Review the depth of assessment — does it cover bias, security, privacy, and regulatory compliance substantively?
- Check if any business units are using AI tools that are not on the inventory.

#### Evidence Required

- Third-party AI inventory (complete and current)
- Completed assessment records for all third-party AI above risk threshold
- Approval records predating adoption
- DPAs for third-party AI processing personal data
- Periodic reassessment records

#### Common Gaps Found in Audits

- No inventory of third-party AI — business units adopt AI tools without central visibility
- SaaS products with embedded AI features treated as standard software procurements with no AI-specific assessment
- Open-source models (from Hugging Face, GitHub, etc.) adopted with no assessment whatsoever
- Assessments conducted but DPA never obtained for cloud AI services processing personal data
- Cloud AI provider's terms-of-service allow training on customer data — not identified in assessment
- No reassessment process — assessments conducted at adoption and never revisited

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 25 (Obligations of distributors/importers); Art. 28 (Third-party obligations) |
| NIST AI RMF | MAP 5.1, MAP 5.2 |
| ISO 27001:2022 | A.5.19 (Information security in supplier relationships) |

---

### A.10.4 — Customers

**Control Statement:** The organization shall determine and document its responsibilities towards customers to whom it provides AI systems or AI-based services, including the information, support and contractual commitments those customers require.

---

#### What It Means

A.10.4 applies to organizations that supply AI to others — as AI providers, not just deployers. If your product or service includes AI components, your customers may have governance requirements you must meet: transparency about AI use in your product; documentation of AI system performance and limitations; compliance with customer's own AI governance framework; cooperation with customer audits.

#### Why It Matters

As AI governance matures, sophisticated customers — particularly in regulated sectors — are increasingly demanding AI governance assurances from their suppliers. Enterprise customers may require ISO 42001 certification from AI vendors, just as they require ISO 27001 for information security. Being unable to meet customer AI governance requirements is a competitive disadvantage and, in some procurement contexts, a disqualifying criterion. This control ensures the organization is proactively prepared.

#### How to Implement

1. **Identify AI-enabled products and services** — Inventory all products or services you provide that include AI components.
2. **Understand customer AI governance requirements** — Survey existing customer contracts for AI-related obligations. Proactively engage key customers to understand emerging requirements. Monitor regulatory developments that affect customer obligations (e.g., EU AI Act downstream obligations).
3. **Map customer requirements to internal controls** — For each customer AI requirement, identify the internal control or documentation that satisfies it. Gap analysis: what is required that you cannot currently provide?
4. **Develop customer-facing AI documentation** — Model cards for AI components in your products; AI capability and limitation documentation; Performance reports with disaggregated metrics; Compliance documentation (e.g., EU AI Act conformity assessment, ISO 42001 certificate).
5. **Contractual obligations** — Ensure your customer contracts reflect your AI governance obligations. Align with what you commit to in AI supplier contracts (A.10.3) — what you require of suppliers, you should also be prepared to provide to customers.
6. **Customer audit support** — Define a process for responding to customer audit requests related to AI governance. Designate a contact and process.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| AI-Enabled Product/Service Register | List of all products/services with AI components | Product Management / AI Governance Lead |
| Customer AI Governance Requirements Register | Tracked customer AI requirements by customer/contract | AI Governance Lead / Account Management |
| Customer-Facing AI Documentation Pack | Model cards, capability sheets, compliance docs for customer distribution | AI Governance Lead / Product Owner |
| Customer AI Governance Gap Analysis | Gap analysis between customer requirements and current capability | AI Risk Manager |
| Customer Audit Response Procedure | Process for handling customer AI governance audit requests | AI Governance Lead |
| AI Regulatory Conformity Documentation | Evidence pack for regulatory requirements (EU AI Act, etc.) for customer use | Legal / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify an inventory of AI-enabled products/services exists
- Check customer AI requirements are tracked and mapped to internal controls
- Confirm customer-facing AI documentation is available and current

**Personnel Interviews:**
- Ask Account Management: "Have any customers asked us about our AI governance practices? How did we respond?"
- Ask the AI Governance Lead: "If a customer asked to audit our AI governance tomorrow, what would you give them? Is that ready?"
- Ask Product Management: "Are our AI product components documented in a way we can share with customers?"

**Audit Testing:**
- Select a key customer contract — does it contain AI governance obligations? Are those obligations currently being met?
- Request the customer-facing AI documentation pack for a product — is it complete, current, and genuinely useful?

#### Evidence Required

- AI-enabled product/service register
- Customer AI requirements tracker
- Customer-facing AI documentation packs (model cards, capability sheets, compliance docs)
- Customer contract AI obligation review records
- Customer audit response records (if any audits conducted)

#### Common Gaps Found in Audits

- Organization does not know which of its products contain AI components — no inventory
- Customer contracts contain AI governance obligations the organization is not currently meeting
- No customer-facing AI documentation available — customers asking for it receive nothing
- EU AI Act obligations as a provider not understood or addressed
- When customers request AI governance audits, there is no process — handled entirely ad hoc

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 16 (Provider obligations); Art. 25 (Distributor obligations); Art. 28 (Deployer as provider) |
| NIST AI RMF | GOVERN 1.7, GOVERN 6.2 |
| ISO 27001:2022 | A.5.20 (Supplier agreements); A.5.21 (Supply chain security) |

---

## MASTER SUMMARY — ALL 38 ANNEX A CONTROLS AT A GLANCE

| Control | Title | Domain | Key Document(s) | Key Audit Test |
|---------|-------|--------|-----------------|----------------|
| A.2.2 | AI Policy | Policies related to AI | AI Policy (AIMS-POL-001) | Check signature, date and communication evidence |
| A.2.3 | Alignment with Other Organizational Policies | Policies related to AI | Policy Interaction Map; Amended Policies | Sample related policies for contradictions with the AI policy |
| A.2.4 | Review of the AI Policy | Policies related to AI | Policy Review Records; Version History | Confirm the stated review interval has actually been honoured |
| A.3.2 | AI Roles and Responsibilities | Internal organization | RACI Matrix; Role Profiles | Trace a deployment — who approved it? |
| A.3.3 | Reporting of Concerns | Internal organization | AI Concern Reporting Procedure; Concerns Register | Ask staff how they would raise a concern; check the register |
| A.4.2 | Resource Documentation | Resources for AI systems | AIMS Resource Plan; AI System Resource Register | Sample a system — are all four resource types documented? |
| A.4.3 | Data Resources | Resources for AI systems | AI Data Inventory; Lawful Basis Record | Check dataset origin, licence and permitted use are recorded |
| A.4.4 | Tooling Resources | Resources for AI systems | Approved Tooling Register; SBOM | Verify approval and vulnerability management for ML tooling |
| A.4.5 | System and Computing Resources | Resources for AI systems | Infrastructure Register; Capacity Plan | Check environment segregation and access to training compute |
| A.4.6 | Human Resources | Resources for AI systems | Competence Matrix; Training Plan and Records | Sample a role — is the required competence evidenced? |
| A.5.2 | AI System Impact Assessment Process | Assessing impacts of AI systems | AI System Impact Assessment Procedure | Confirm the process defines triggers, method and approval |
| A.5.3 | Documentation of AI System Impact Assessments | Assessing impacts of AI systems | Completed Assessments; Retention Schedule | Sample the AI inventory — does each system have a current record? |
| A.5.4 | Assessing AI System Impact on Individuals or Groups | Assessing impacts of AI systems | Individual and Group Impact Assessment | Check subgroup analysis exists, not just aggregate accuracy |
| A.5.5 | Assessing Societal Impacts of AI Systems | Assessing impacts of AI systems | Societal Impact Assessment | Verify societal and environmental effects were considered |
| A.6.1.2 | Objectives for Responsible Development of AI Systems | AI system life cycle | Responsible AI Development Objectives | Are objectives measurable and known to developers? |
| A.6.1.3 | Processes for Responsible AI System Design and Development | AI system life cycle | AI Lifecycle Management Procedure | Sample a project — were all gates completed and evidenced? |
| A.6.2.2 | AI System Requirements and Specification | AI system life cycle | AI Requirements Specification | Trace a responsible-AI requirement into the built system |
| A.6.2.3 | Documentation of AI System Design and Development | AI system life cycle | Design Documentation; Decision Log | Check design rationale and alternatives are recorded |
| A.6.2.4 | AI System Verification and Validation | AI system life cycle | V and V Plan; Test and Bias Evaluation Results | Were acceptance criteria set before testing and met? |
| A.6.2.5 | AI System Deployment | AI system life cycle | Deployment Checklist; Release Approval | Verify rollback exists and approval was independent |
| A.6.2.6 | AI System Operation and Monitoring | AI system life cycle | Performance Monitoring Plan; Drift Reports | Check drift thresholds are defined and alerts are acted on |
| A.6.2.7 | AI System Technical Documentation | AI system life cycle | AI Model Card; Technical Documentation | Is documentation current for the deployed model version? |
| A.6.2.8 | AI System Recording of Event Logs | AI system life cycle | Logging Standard; Log Retention Schedule | Reconstruct a past decision from logs alone |
| A.7.2 | Data for Development and Enhancement of AI Systems | Data for AI systems | AI Data Requirements Specification | Are data requirements tied to intended purpose? |
| A.7.3 | Acquisition of Data | Data for AI systems | Data Acquisition Procedure; Source Approvals | Check lawful basis and licence terms were assessed pre-acquisition |
| A.7.4 | Quality of Data for AI Systems | Data for AI systems | Data Quality Requirements and Reports | Are quality thresholds defined and measured, not aspirational? |
| A.7.5 | Data Provenance | Data for AI systems | Data Provenance Records; Lineage Diagrams | Trace a training dataset back to its original source |
| A.7.6 | Data Preparation | Data for AI systems | Data Preparation Procedure; Labelling Standards | Check preparation and bias treatment steps are documented |
| A.8.2 | System Documentation and Information for Users | Information for interested parties | User Documentation; Model Card | Can a user state the system limitations from what they were given? |
| A.8.3 | External Reporting | Information for interested parties | External Reporting Obligations Register | Does the register reflect current regulation and named owners? |
| A.8.4 | Communication of Incidents | Information for interested parties | AI Incident Response Procedure | Check notification timescales against regulatory deadlines |
| A.8.5 | Information for Interested Parties | Information for interested parties | AI Disclosure Standard; Transparency Notices | Verify people are told when they interact with or are assessed by AI |
| A.9.2 | Processes for Responsible Use of AI Systems | Use of AI systems | Acceptable Use Policy; Human Oversight Policy | Is oversight genuine, or rubber-stamping under time pressure? |
| A.9.3 | Objectives for Responsible Use of AI Systems | Use of AI systems | Responsible Use Objectives; AI Objectives Register | Do objectives balance efficiency with limits on reliance? |
| A.9.4 | Intended Use of the AI System | Use of AI systems | Intended Use Statement; Model Card | Does observed use still match the documented intended purpose? |
| A.10.2 | Allocating Responsibilities | Third-party and customer relationships | Value Chain Map; Responsibility Matrix | Find an activity nobody has taken responsibility for |
| A.10.3 | Suppliers | Third-party and customer relationships | Supplier Assessments; AI Contract Clauses | Check audit rights and model-change notification are contracted |
| A.10.4 | Customers | Third-party and customer relationships | Customer AI Governance Pack; Contracts | Verify customers receive the information they need to comply |

---

## MASTER DOCUMENT CHECKLIST

Use this checklist to track documentation completeness across all 38 Annex A controls.

### Policies Related to AI (A.2)
- [ ] AI Policy (AIMS-POL-001) — A.2.2
- [ ] Policy Communication Records — A.2.2
- [ ] Policy Interaction Map (AI policy vs related policies) — A.2.3
- [ ] Amended Related Policies (security, privacy, data, HR, procurement) — A.2.3
- [ ] AI Policy Review Procedure and Review Records — A.2.4
- [ ] AI Policy Version History and Re-approval Records — A.2.4

### Internal Organization (A.3)
- [ ] AI Governance RACI Matrix and Role Profiles — A.3.2
- [ ] AI System Ownership Register — A.3.2
- [ ] AI Concern Reporting Procedure — A.3.3
- [ ] Non-Retaliation Statement — A.3.3
- [ ] AI Concerns Register and Outcome Records — A.3.3

### Resources for AI Systems (A.4)
- [ ] AIMS Resource Plan — A.4.2
- [ ] AI System Resource Register and Dependency Analysis — A.4.2
- [ ] AI Data Inventory — A.4.3
- [ ] Data Licensing and Lawful Basis Records — A.4.3
- [ ] Approved AI Tools and Libraries List — A.4.4
- [ ] Pre-trained Model Registry and Vulnerability Records — A.4.4
- [ ] AI Infrastructure Inventory and Security Standards — A.4.5
- [ ] Compute Capacity and Environment Controls — A.4.5
- [ ] AI Competency Framework and Gap Assessments — A.4.6
- [ ] Training Plan, Records and Effectiveness Reviews — A.4.6

### Assessing Impacts of AI Systems (A.5)
- [ ] AI System Impact Assessment Procedure — A.5.2
- [ ] Impact Assessment Trigger Criteria — A.5.2
- [ ] Impact Assessment Template — A.5.3
- [ ] Completed Impact Assessment Records per AI System — A.5.3
- [ ] Impact Assessment Retention Schedule — A.5.3
- [ ] Individual and Group Impact Assessments — A.5.4
- [ ] Subgroup Outcome Analysis and Vulnerable Group Records — A.5.4
- [ ] Societal Impact Assessments — A.5.5
- [ ] Environmental Impact Assessments for Large Models — A.5.5

### AI System Life Cycle (A.6)
- [ ] Responsible AI Development Objectives — A.6.1.2
- [ ] AI Objectives Register and Design Review Records — A.6.1.2
- [ ] AI Lifecycle Management Procedure — A.6.1.3
- [ ] Development Checkpoint and Code Review Records — A.6.1.3
- [ ] AI System Requirements Specifications — A.6.2.2
- [ ] Responsible AI Requirements Template — A.6.2.2
- [ ] AI System Architecture and Design Documents — A.6.2.3
- [ ] Design Decision and Rationale Log — A.6.2.3
- [ ] Verification and Validation Plan — A.6.2.4
- [ ] Test, Bias Evaluation and Adversarial Testing Results — A.6.2.4
- [ ] Release Approval Records — A.6.2.4
- [ ] AI Deployment Procedure and Checklist — A.6.2.5
- [ ] Deployment Authorization and Rollback Records — A.6.2.5
- [ ] AI Monitoring Framework and Dashboards — A.6.2.6
- [ ] Drift Detection Configuration and Retraining Decisions — A.6.2.6
- [ ] AI Decommissioning Procedure and Records — A.6.2.6
- [ ] Model Card Template and Completed Model Cards — A.6.2.7
- [ ] Model Registry and Technical Documentation — A.6.2.7
- [ ] AI Logging Standard and Retention Schedule — A.6.2.8
- [ ] Log Access Control and Traceability Evidence — A.6.2.8

### Data for AI Systems (A.7)
- [ ] AI Data Requirements Specification — A.7.2
- [ ] Data Partitioning Standard and Enhancement Data Procedure — A.7.2
- [ ] Data Acquisition Procedure and Source Approval Records — A.7.3
- [ ] AI Data Access Control Matrix and Review Records — A.7.3
- [ ] DPIAs, Lawful Basis Register and DPAs for AI Processing — A.7.3
- [ ] AI Data Quality Standards and Assessment Records — A.7.4
- [ ] AI Data Catalog and Lineage Documentation — A.7.5
- [ ] Data Licensing and Provenance Register — A.7.5
- [ ] Data Preparation and Labelling Procedures — A.7.6
- [ ] Training Data Bias Assessment Reports — A.7.6

### Information for Interested Parties (A.8)
- [ ] AI Capability and Limitation Sheets — A.8.2
- [ ] User Documentation and Explainability Material — A.8.2
- [ ] External Reporting Obligations Register — A.8.3
- [ ] Regulatory Reporting Procedure and Submitted Reports Archive — A.8.3
- [ ] AI Incident Communication Policy and Templates — A.8.4
- [ ] Incident Notification Records — A.8.4
- [ ] AI Disclosure Policy and UI/UX Evidence — A.8.5
- [ ] Transparency Notices for Interested Parties — A.8.5

### Use of AI Systems (A.9)
- [ ] Acceptable Use of AI Policy — A.9.2
- [ ] Approved External AI Tools List — A.9.2
- [ ] Human Oversight Policy and Procedures — A.9.2
- [ ] AI Error Handling and Contest Procedure — A.9.2
- [ ] Responsible Use Objectives and Measures — A.9.3
- [ ] Use Performance Review Reports — A.9.3
- [ ] Intended Use Statements per AI System — A.9.4
- [ ] Use Monitoring Reports and Change Approvals — A.9.4

### Third-Party and Customer Relationships (A.10)
- [ ] AI Value Chain Map — A.10.2
- [ ] Responsibility Allocation Matrix and Regulatory Role Determination — A.10.2
- [ ] Third-Party AI Inventory and Risk Assessments — A.10.3
- [ ] AI Supplier Contract Clauses and Signed Agreements — A.10.3
- [ ] Supplier Monitoring, Review and Exit Plans — A.10.3
- [ ] Customer AI Governance and Support Documentation — A.10.4
- [ ] Customer Information and Contractual Commitments — A.10.4

---

## AUDIT INTERVIEW QUESTION BANK

A consolidated list of the most impactful audit questions across all 38 controls. Use these in Stage 1 (document review) and Stage 2 (effectiveness audit) interviews.

**Opening Questions (to any interviewee):**
1. "Describe your role in AI governance. What are you personally responsible for?"
2. "What AI systems does your team develop, deploy, or use?"
3. "What would you do if you identified an AI system behaving in a way that might cause harm?"

**Policy & Governance:**
4. "What does the AI Policy say about your responsibilities? When did you last read it?"
5. "Are there AI use cases that are explicitly prohibited in your organization? Name three."
6. "Who has the authority to stop an AI project on governance grounds? Has that ever happened?"

**Impact Assessment:**
7. "Was an ASIA conducted for [specific AI system]? What were the key findings? What changed as a result?"
8. "How do you identify potential harms from AI systems before they're deployed?"

**Lifecycle:**
9. "Walk me through your AI development process from the point you have a clean dataset to the point the model is in production."
10. "What bias evaluation did you conduct for this model? Show me the results disaggregated by demographic group."
11. "When was this model last retrained? Why? Was drift detected? Show me the records."
12. "If this AI model started producing clearly wrong outputs right now, what would happen? Walk me through it step by step."

**Data:**
13. "Where did the training data for this model come from? Do you have the right to use it for AI training?"
14. "How do you know your training data is representative of the population the model will serve?"
15. "If a data subject requests erasure and their data was used to train this model, what happens?"

**Transparency & Oversight:**
16. "Show me the explanation a user would receive if this AI made a decision affecting them."
17. "When did you last override an AI recommendation? Why? How did you do it?"
18. "What is your AI override rate? Is that plausible given the AI's known error rate?"

**Third-Party AI:**
19. "List all the third-party AI services your team uses. Are they all on the approved list?"
20. "What data do you send to [cloud AI service]? Have you reviewed their data handling terms? Is there a DPA?"

---

## DOCUMENT VERSION CONTROL AND MAINTENANCE

| Field | Value |
|-------|-------|
| Document ID | AIMS-ANNEXA-001 |
| Document Title | Annex A Controls — ISO 42001:2023 Implementation, Audit & Evidence Guide |
| Version | 1.0 |
| Author | Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group |
| Review Cycle | Annual (minimum) |
| Next Review Date | April 2027 |
| Standard Reference | ISO/IEC 42001:2023 Annex A |
| Related Documents | STATEMENT-OF-APPLICABILITY.md, GAP-ASSESSMENT.md, AI-RISK-REGISTER.md, AI-SYSTEM-IMPACT-ASSESSMENT.md, INTERNAL-AUDIT-PROCEDURE.md, AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md, CONTROLS-MAPPING.md |

### Review Triggers

This document must be reviewed and updated when:
- A new version of ISO/IEC 42001 is published
- Significant new regulatory requirements emerge (EU AI Act guidance, national AI regulations)
- AIMS scope changes and new control domains become relevant
- An internal audit or certification audit identifies gaps in the guidance
- Major AI incidents reveal control weaknesses not addressed in this guide
- Annually as part of the AIMS management review cycle

### Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Ankit Uniyal | Initial release — all 38 Annex A controls |

---

## DISCLAIMER

This guide is provided for educational and practical guidance purposes only. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text (available from ISO or your national standards body) for definitive normative requirements.

All templates and guidance must be adapted to your specific organizational context, sector, jurisdiction, and AI risk profile. Organizations seeking ISO 42001 certification should engage a qualified implementation consultant and accredited certification body.

The author has made every effort to ensure accuracy at the time of writing, but this guidance may not reflect the latest regulatory developments. Always verify current regulatory requirements with qualified legal counsel.

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Part of the ISO 42001 AI Governance Toolkit: github.com/Ankit-Uniyal/iso-42001-ai-governance-toolkit*
*MIT License — Free to use, adapt, and distribute with attribution*
