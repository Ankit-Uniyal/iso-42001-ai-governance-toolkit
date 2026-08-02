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

## DOMAIN A.6 — AI LIFECYCLE
*10 Controls | Governing AI from design through decommissioning*

---

### A.6.1.1 — AI Design Requirements

**Control Statement:** The organization shall define and document responsible AI design requirements for AI systems, covering fairness, transparency, explainability, privacy, safety, and security, before development begins.

---

#### What It Means

A.6.1.1 requires that responsible AI principles are translated into concrete, measurable design requirements before development begins — not as an afterthought. Just as software engineering defines functional requirements before coding, AI governance requires responsible AI requirements to be defined at the design stage.

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

### A.6.1.2 — AI Design Documentation

**Control Statement:** The organization shall create and maintain design documentation for AI systems, including system architecture, data flows, model design decisions, and rationale, sufficient to enable understanding, evaluation, and audit of the AI system.

---

#### What It Means

A.6.1.2 requires that AI systems are documented in sufficient technical detail to enable independent understanding, evaluation, and audit. Without design documentation, the only person who understands how an AI system works is the person who built it — creating a single point of failure and making governance, maintenance, and audit impossible.

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

### A.6.2.1 — AI Development Process

**Control Statement:** The organization shall implement a defined, controlled, and auditable AI development process that incorporates responsible AI practices, version control, documentation, and review checkpoints throughout development.

---

#### What It Means

A.6.2.1 requires that AI development follows a structured, repeatable process — not an ad hoc, individual-driven activity. This includes version control for all model artifacts, code review checkpoints, and documented development practices that ensure responsible AI considerations are embedded throughout development, not just at the end.

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

### A.6.2.3 — Model Documentation (Model Cards)

**Control Statement:** The organization shall create and maintain model documentation (model cards or equivalent) for AI models, covering model purpose, performance metrics, limitations, bias evaluation results, and intended and prohibited use cases.

---

#### What It Means

A.6.2.3 requires that every AI model has a standardized documentation artifact — commonly called a "model card" — that provides a transparent, accessible account of what the model does, how well it does it, where it fails, and who should and should not use it. Model cards originated at Google and have become a de facto standard for AI model documentation.

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

### A.6.2.5 — Adversarial Testing

**Control Statement:** The organization shall conduct adversarial testing of AI systems to identify vulnerabilities to adversarial inputs, prompt injection, data poisoning, model evasion, and other attacks relevant to the AI system's threat model.

---

#### What It Means

A.6.2.5 requires that AI systems are tested against adversarial attacks — deliberate attempts to manipulate, deceive, or exploit the AI system. Unlike functional testing, adversarial testing requires a "red team" mindset: actively trying to break the system rather than verify it works under normal conditions.

#### Why It Matters

AI systems face unique attack vectors: adversarial examples (inputs crafted to fool the model); prompt injection (for LLM-based systems); model inversion (reconstructing training data from model outputs); data poisoning (corrupting training data to manipulate model behavior); model evasion (evading classification by AI security tools). Without adversarial testing, these vulnerabilities are discovered in production by attackers rather than in testing by security teams.

#### How to Implement

- **Define the threat model for each AI system** — What adversarial attacks are plausible given the system's context? Who would benefit from attacking it? What is the impact of a successful attack?
- **Conduct adversarial testing per threat model** — For each relevant attack type: define test scenarios; execute tests; document findings.
- **LLM-specific testing** — For any generative AI or LLM: prompt injection testing; jailbreaking attempts; harmful output elicitation; indirect prompt injection (from documents/web content processed by the LLM).
- **Red team exercises** — For high-risk AI, conduct structured red team exercises with dedicated attackers.
- **Document results and remediation** — All adversarial test findings must be documented. Critical findings must be remediated before deployment.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Threat Model | Threat model per AI system identifying relevant adversarial attack types | CISO / AI Governance Lead |
| Adversarial Test Plan | Test plan per AI system covering relevant attack types | CISO / ML Security Engineer |
| Adversarial Test Results | Documented results of adversarial testing | CISO / ML Security Engineer |
| Red Team Exercise Records | Records of red team exercises for high-risk AI systems | CISO |

#### How to Audit

**Document Review:**
- Verify threat model exists for each high-risk AI system
- Check adversarial test plans and results exist
- For LLM systems: confirm prompt injection testing has been conducted

**Personnel Interviews:**
- Ask: "What adversarial attacks have you tested this AI system against? Show me the results."

**Evidence Required**
- AI threat models
- Adversarial test plans and results
- Evidence of remediation for critical findings

**Common Gaps Found in Audits**
- No adversarial testing conducted — only functional testing
- LLM systems deployed without prompt injection testing
- Adversarial testing conducted by the development team rather than an independent red team
- Findings documented but remediation not tracked

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 15 (Accuracy, robustness, cybersecurity) |
| NIST AI RMF | MANAGE 2.2, MAP 5.1 |
| ISO 27001:2022 | A.8.8 (Management of technical vulnerabilities) |

---

### A.6.2.6 — Bias Evaluation

**Control Statement:** The organization shall conduct systematic bias evaluation of AI systems against defined fairness criteria before deployment and periodically during operation, with results documented and used to inform risk treatment decisions.

---

#### What It Means

A.6.2.6 requires systematic, documented evaluation of AI model bias against defined fairness criteria. Bias evaluation must be: conducted before deployment (prospective); repeated periodically in production (operational); disaggregated by relevant protected attributes; measured against defined fairness thresholds; and used to make go/no-go decisions.

#### Why It Matters

AI bias causes real harm: discriminatory employment decisions; unfair credit assessments; differential quality of medical AI recommendations; biased law enforcement predictions. Bias evaluation is the mechanism by which organizations detect and address unfair AI behavior before it causes harm at scale.

#### How to Implement

- **Define fairness criteria per AI system** — Based on the use case and applicable law: which protected attributes are relevant (race, gender, age, disability, etc.)? Which fairness metrics are appropriate (demographic parity, equalized odds, calibration)? What are the acceptable thresholds?
- **Conduct bias evaluation using representative datasets** — Ensure evaluation datasets are sufficiently large and representative for each subgroup being assessed.
- **Disaggregate all performance metrics** — Report accuracy, precision, recall, false positive rate, and false negative rate separately for each protected group.
- **Apply defined thresholds** — Does the model meet the defined fairness thresholds? If not, the model should not be deployed until bias is addressed.
- **Document methodology and results** — Full bias evaluation report with methodology, datasets used, metrics, and findings.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Fairness Criteria and Thresholds | Defined fairness metrics and acceptable thresholds per AI system | AI Governance Lead / ML Lead |
| Bias Evaluation Methodology | Documented methodology for bias evaluation | ML Engineer / AI Risk Manager |
| Bias Evaluation Reports | Results of bias evaluation per AI system, with disaggregated metrics | ML Engineer |
| Bias Remediation Records | Actions taken to address identified bias | ML Engineer / Model Owner |

#### How to Audit

**Document Review:**
- Verify fairness criteria and thresholds are defined for each AI system
- Check bias evaluation reports exist and contain disaggregated metrics by protected attribute
- Confirm evaluation datasets were representative for each subgroup

**Audit Testing:**
- Select a live AI system. Review its bias evaluation report. Are metrics disaggregated by relevant protected attributes? Did the system pass defined fairness thresholds?

**Evidence Required**
- Fairness criteria and threshold definitions
- Bias evaluation reports with disaggregated metrics
- Bias remediation records (where bias was found)
- Evidence fairness thresholds were met before deployment

**Common Gaps Found in Audits**
- Overall accuracy reported but no disaggregation by protected group
- Fairness thresholds not defined — no basis for a pass/fail determination
- Evaluation datasets too small for meaningful subgroup analysis
- Bias evaluation conducted but findings did not delay deployment

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data and data governance); Art. 9 (Risk management) |
| NIST AI RMF | MAP 5.1, MAP 5.2, MEASURE 2.5 |

---

### A.6.2.8 — Testing in Representative Environments

**Control Statement:** The organization shall test AI systems in environments and with data that are representative of the actual operational deployment context before deployment to production.

---

#### What It Means

A.6.2.8 requires that testing is conducted in conditions that reflect reality: using data representative of the production population; in an environment that reflects production infrastructure; under realistic operating conditions (load, data quality, edge cases). Testing in unrepresentative environments produces unreliable assurance that the system will behave as expected in production.

#### Why It Matters

AI systems frequently perform well in test environments and poorly in production because: test data does not reflect the diversity and quality of production data; test environment does not replicate production infrastructure; edge cases in production were not anticipated in testing; the model was optimized for the test distribution, not the production distribution.

#### How to Implement

- **Define "representative" for each AI system** — What is the production data distribution? What are the edge cases and challenging inputs? What infrastructure characteristics must the test environment replicate?
- **Use production-representative test data** — Avoid using only "clean" test data. Include realistic noise, missing values, distribution shifts, and rare cases.
- **Test with protected group representation** — Ensure test data is representative for all protected groups relevant to fairness evaluation.
- **Staging environment** — Maintain a staging environment that replicates production infrastructure for pre-deployment testing.
- **Load and performance testing** — Test under realistic load conditions.
- **Document test environment and data** — Record what data was used for testing and how the test environment compares to production.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Test Environment Specification | Description of test environment and how it reflects production | ML Engineer / DevOps |
| Test Data Specification | Description of test datasets including representativeness assessment | ML Engineer |
| Test Plans and Results | Documented test plans and results for each AI system | ML Engineer / QA |
| Test Environment vs Production Comparison | Analysis of differences between test and production environments | ML Engineer / DevOps |

#### How to Audit

**Document Review:**
- Verify test data documentation includes representativeness assessment
- Check test environment specification — how closely does it replicate production?

**Personnel Interviews:**
- Ask: "How do you know your test data is representative of the population your model will serve in production?"

**Evidence Required**
- Test data specification with representativeness evidence
- Test environment documentation
- Test results

**Common Gaps Found in Audits**
- Test data is a clean, curated dataset that does not reflect production data quality
- Test environment does not replicate production — different infrastructure, data volumes
- No analysis of whether test data is representative for relevant protected groups

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management); Art. 10 (Data and data governance) |
| NIST AI RMF | MEASURE 2.5, MANAGE 1.2 |

---

### A.6.3.1 — AI Deployment Controls

**Control Statement:** The organization shall implement controls for the deployment of AI systems to production, including deployment authorization, staged rollout, rollback capability, and post-deployment validation.

---

#### What It Means

A.6.3.1 requires that deploying an AI system to production is a controlled, authorized, and reversible action. Production deployment should require formal authorization, should follow a documented procedure, and should be designed so that a failed deployment can be quickly reversed.

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

### A.6.3.3 — Human Oversight at Deployment

**Control Statement:** The organization shall verify that human oversight mechanisms are operational and effective before deploying AI systems to production, and shall document this verification.

---

#### What It Means

A.6.3.3 is the deployment-stage verification that human oversight (designed in A.6.1.1 and governed operationally by A.9.3) is actually working. Before go-live, the organization must verify: the override mechanism works technically; overseers are trained and ready; the oversight process has been rehearsed; logging of override decisions is functional.

#### Why It Matters

Human oversight mechanisms that exist on paper but fail in practice are a critical governance gap. The time to discover that the override button is broken or that no one knows how to use it is not when a harmful AI output needs to be stopped. A.6.3.3 requires pre-deployment verification that oversight is operational.

#### How to Implement

- **Human oversight verification checklist** — Verify before deployment: override mechanism tested and confirmed working; oversight personnel identified and trained; oversight process rehearsed with realistic scenarios; override logging confirmed operational; escalation path confirmed.
- **Live test of override** — Demonstrate that the override mechanism works by actually exercising it in the staging environment.
- **Overseer readiness confirmation** — Confirm that designated oversight personnel are available and prepared for go-live.
- **Document verification** — Create an oversight verification record as part of the deployment package.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Human Oversight Verification Checklist | Pre-deployment checklist for verifying oversight is operational | AI Governance Lead |
| Oversight Verification Record | Completed verification record per deployment | AI Governance Lead / Model Owner |
| Overseer Training Records | Evidence that oversight personnel are trained for this specific system | HR / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify oversight verification records exist for recent deployments
- Check overseer training records are current

**Audit Testing:**
- For a live AI system: demonstrate that the override mechanism works. Can an overseer actually override an AI recommendation right now?

**Evidence Required**
- Oversight verification records (pre-deployment)
- Overseer training records
- Evidence of override mechanism testing

**Common Gaps Found in Audits**
- No pre-deployment oversight verification — oversight assumed to work without testing
- Override mechanism exists in design but has never been tested
- Oversight personnel identified but not trained for this specific AI system

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 14 (Human oversight for high-risk AI) |
| NIST AI RMF | MANAGE 1.3, GOVERN 6.2 |

---

### A.6.4.1 — AI Operation Monitoring

**Control Statement:** The organization shall implement and maintain monitoring of AI systems in operation to detect performance degradation, unexpected behavior, data quality issues, and security incidents affecting AI systems.

---

#### What It Means

A.6.4.1 requires ongoing monitoring of AI systems in production. Unlike traditional software where failures are typically binary (working or not), AI failures are often gradual and soft: model performance slowly degrades; data quality issues accumulate; bias increases over time; security incidents affect AI outputs. Monitoring must be designed to detect these AI-specific failure modes.

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

### A.6.4.2 — Performance Drift Monitoring

**Control Statement:** The organization shall monitor AI systems for performance drift, data drift, and concept drift, and shall define and implement processes to detect, investigate, and respond to drift that affects AI system performance or fairness.

---

#### What It Means

A.6.4.2 specifically addresses drift — one of the most important operational AI risks. AI models are trained on historical data, but the world changes: the statistical properties of input data change (data drift); the relationship between inputs and outputs changes (concept drift); model performance on production data degrades (performance drift). Without monitoring for drift, organizations discover problems only after significant degradation has occurred.

#### Why It Matters

Drift is pervasive in production AI: a hiring AI trained on historical data becomes less accurate as the job market changes; a fraud detection AI trained on historical fraud patterns becomes less effective as fraud tactics evolve; a medical AI trained on historical patient populations becomes less accurate as patient demographics shift.

#### How to Implement

- **Implement statistical drift detection** — Monitor for changes in: input data distributions (feature drift); prediction output distributions; model performance metrics (if ground truth is available); fairness metrics by subgroup.
- **Define drift detection methods** — Population Stability Index (PSI), Kolmogorov-Smirnov test, Jensen-Shannon divergence, or other appropriate statistical methods per feature type.
- **Set drift alert thresholds** — Define what level of drift triggers an alert requiring investigation.
- **Define response procedures** — When drift is detected: investigate root cause; assess impact on model performance and fairness; determine whether retraining or recalibration is required.
- **Document retraining decisions** — All retraining decisions must be documented: what drift was detected; what investigation was conducted; why retraining was decided; the retraining approach.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Drift Detection Configuration | Technical configuration of drift monitoring per AI system | ML Engineer / DevOps |
| Drift Monitoring Reports | Regular reports on drift metrics and status | ML Engineer / Model Owner |
| Retraining Decision Records | Documented decisions to retrain, with rationale | Model Owner / AI Governance Lead |
| Model Retraining Records | Evidence of model retraining including data version, parameters, evaluation results | ML Engineer |

#### How to Audit

**Document Review:**
- Verify drift detection is configured for each production AI system
- Check drift monitoring reports — is drift being tracked and reviewed?
- Review retraining records — are retraining decisions documented with rationale?

**Personnel Interviews:**
- Ask: "When was this model last retrained? Why? What drift was detected? Show me the records."

**Evidence Required**
- Drift detection configuration evidence
- Drift monitoring reports
- Retraining decision records

**Common Gaps Found in Audits**
- No drift monitoring in place — model is never retrained unless it visibly fails
- Drift monitoring configured for input features but not for fairness metrics by subgroup
- Retraining occurs informally with no documented decision rationale

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 72 (Post-market monitoring); Art. 9 (Risk management) |
| NIST AI RMF | MANAGE 2.4, MEASURE 2.7 |

---

### A.6.5.1 — AI Decommissioning

**Control Statement:** The organization shall implement controlled processes for decommissioning AI systems, including proper data disposal, documentation archival, stakeholder notification, and transition planning.

---

#### What It Means

A.6.5.1 requires that AI systems are decommissioned in a controlled manner when they reach end-of-life. Decommissioning includes: turning off the AI system; properly disposing of training data and model artifacts in accordance with data retention policies; archiving documentation; notifying affected stakeholders; and ensuring any dependent processes are transitioned.

#### Why It Matters

Uncontrolled AI decommissioning leads to: training data (including personal data) remaining on servers indefinitely after the AI system it supported has been discontinued; model artifacts accessible to unauthorized parties long after decommissioning; stakeholders (including individuals affected by the AI) not notified of changes; no record of when an AI system was shut down and why.

#### How to Implement

- **Define an AI decommissioning procedure** — Steps required to decommission an AI system: decision and authorization; stakeholder notification; data disposal (aligned with retention policy and GDPR right to erasure); model artifact disposal or archival; documentation archival; transition of dependent processes; decommissioning record.
- **Data disposal** — Training data and personal data processed by the AI must be disposed of in accordance with data retention schedules and GDPR obligations.
- **Model artifact disposal** — Model weights and artifacts should be deleted (or archived in controlled storage) according to a defined retention schedule.
- **Documentation archival** — ASIA, model cards, and other governance documentation should be archived for audit purposes for a defined retention period.
- **Maintain a decommissioning register** — Record all decommissioned AI systems with dates and disposal evidence.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Decommissioning Procedure | Documented procedure for controlled AI system decommissioning | AI Governance Lead / DevOps |
| Decommissioning Authorization Records | Formal authorization of decommissioning decisions | AI Governance Lead |
| Data Deletion Certificates | Evidence of data disposal for training and operational data | DevOps / DPO |
| Decommissioning Register | Register of all decommissioned AI systems | AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify decommissioning procedure exists
- Check decommissioning register — are all discontinued AI systems recorded?
- Review data deletion certificates for decommissioned systems

**Audit Testing:**
- Identify any AI systems known to have been discontinued. Is data from those systems still on servers?

**Evidence Required**
- Decommissioning procedure
- Decommissioning register
- Data deletion certificates for decommissioned systems

**Common Gaps Found in Audits**
- No decommissioning procedure — AI systems are "switched off" informally
- Training data from decommissioned AI systems remains on servers with no deletion record
- No decommissioning register — no record of which AI systems have been discontinued

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 9 (Risk management throughout lifecycle) |
| NIST AI RMF | MANAGE 4.1 |
| ISO 27001:2022 | A.8.10 (Information deletion) |

## DOMAIN A.7 — DATA FOR AI
*5 Controls | Governing data quality, provenance, privacy, and access for AI systems*

---

### A.7.2 — AI Data Quality

**Control Statement:** The organization shall define, implement, and verify data quality requirements for AI training, validation, and testing data, including accuracy, completeness, consistency, and representativeness standards appropriate to the AI system's purpose and risk level.

---

#### What It Means

A.7.2 recognizes that AI system quality is fundamentally dependent on data quality: "garbage in, garbage out" applies with particular force to AI. This control requires that data quality requirements are defined before training (not just assumed), measured, and verified before data is used for AI development.

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

### A.7.3 — Data Provenance

**Control Statement:** The organization shall establish and maintain documentation of the provenance, lineage, and licensing of data used for AI training, validation, and testing, sufficient to enable reproducibility, audit, and compliance verification.

---

#### What It Means

A.7.3 requires that organizations know exactly where their AI training data comes from, what transformations it has undergone, and what rights exist to use it. Data provenance is the documented history of data from its origin to its use in AI training. This is essential for: reproducing training runs; investigating model behavior; verifying licensing compliance; responding to GDPR subject access requests; regulatory audit.

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

### A.7.4 — Data Privacy for AI

**Control Statement:** The organization shall identify, assess, and address privacy risks associated with personal data used in AI systems, including for training, validation, testing, and operation, in compliance with applicable data protection requirements.

---

#### What It Means

A.7.4 applies data protection requirements specifically to AI use of personal data — which has unique characteristics: personal data embedded in training data persists in the model itself; AI systems can infer sensitive attributes from non-sensitive data; AI systems can reconstruct personal data from model outputs (model inversion). Standard GDPR compliance processes may not capture these AI-specific privacy risks.

#### Why It Matters

Using personal data in AI without appropriate legal basis, privacy assessment, and safeguards exposes organizations to: regulatory enforcement action (GDPR fines); reputational damage; inability to fulfill data subject rights (erasure, access) for data used in AI training; processing personal data in ways data subjects did not anticipate or consent to.

#### How to Implement

- **Conduct DPIAs for AI systems processing personal data** — Every AI system processing personal data requires a Data Protection Impact Assessment (DPIA) covering AI-specific risks: inference risks; profiling; automated decision-making; model inversion risk.
- **Establish lawful basis for each AI processing activity** — Training on personal data, validation, operational inference, and output processing may each require separate lawful basis analysis.
- **Address GDPR automated decision-making** — For AI that makes solely automated decisions with significant effects on individuals: ensure compliance with GDPR Art. 22; implement right to human review; provide meaningful information about the logic.
- **Data minimization for AI training** — Use the minimum personal data necessary for the purpose. Consider synthetic data or anonymization where possible.
- **Data Processing Agreements (DPAs)** — For cloud AI APIs that process personal data, ensure DPAs are in place.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| DPIAs for AI Systems | Data Protection Impact Assessments for each AI system processing personal data | DPO / AI Governance Lead |
| Lawful Basis Register for AI Processing | Documented lawful basis for each AI processing activity | DPO / Legal |
| GDPR Art. 22 Compliance Assessment | Assessment of automated decision-making compliance for relevant AI systems | DPO / Legal |
| DPAs for Cloud AI Services | Data Processing Agreements with cloud AI providers processing personal data | Legal / DPO |

#### How to Audit

**Document Review:**
- Verify DPIAs exist for all AI systems processing personal data
- Check lawful basis is documented for all AI processing activities
- Confirm DPAs are in place for cloud AI services processing personal data

**Personnel Interviews:**
- Ask the DPO: "If a data subject requests erasure and their data was used to train one of our AI models, what happens?"
- Ask Legal: "Do we have DPAs with all cloud AI services that process personal data for us?"

**Evidence Required**
- DPIAs for AI systems (covering AI-specific privacy risks)
- Lawful basis register
- DPAs for cloud AI services

**Common Gaps Found in Audits**
- DPIAs conducted using standard template that does not address AI-specific risks (inference, model inversion)
- Personal data used for AI training without documented lawful basis
- Cloud AI APIs processing personal data without DPAs in place
- Right to erasure for AI training data not addressed — technically complex challenge unresolved

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data governance); Art. 26 (Deployer obligations) |
| NIST AI RMF | MAP 1.6, GOVERN 1.6 |
| ISO 27001:2022 | A.5.34 (Privacy and protection of PII) |

---

### A.7.5 — Bias Mitigation in Data

**Control Statement:** The organization shall assess AI training, validation, and testing data for bias affecting protected groups and implement appropriate data-level bias mitigation measures prior to model training.

---

#### What It Means

A.7.5 addresses bias at the data level — distinct from model-level bias evaluation (A.6.2.6). Data-level bias assessment examines whether training data itself contains historical bias, underrepresentation, or skewed labeling that will be learned by the model. Data-level mitigation (resampling, reweighting, relabeling) is often more effective than post-hoc model-level correction.

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

### A.7.6 — Data Access Controls

**Control Statement:** The organization shall implement access controls for AI training data, validation data, test data, and production inference data, applying least-privilege principles and maintaining access logs sufficient for audit.

---

#### What It Means

A.7.6 applies information security access control principles specifically to AI-related data. AI data environments have specific access control requirements: training data (often large, sensitive, and accessed by ML engineers); validation and test data (must be protected from contamination and information leakage); production inference data (may contain personal data requiring access restriction); output data (AI predictions and decisions, potentially sensitive).

#### Why It Matters

Inadequate access controls on AI data lead to: unauthorized access to personal data used in AI training; training data contamination (if test data is accessible during training, test results are unreliable); intellectual property loss through model theft; insider threats (employees extracting sensitive training data).

#### How to Implement

- **Create an AI data access control matrix** — For each AI data category and each role, define: read access; write access; delete access; export access. Apply least privilege.
- **Implement access controls technically** — Storage-level access controls (S3 bucket policies, database permissions, file system ACLs). Identity-based access controls linked to organizational identity management.
- **Separate training/validation/test data stores** — Prevent test data contamination. Separate access for data used in different ML pipeline stages.
- **Access logging** — Log all access to AI data. Retain logs for audit purposes.
- **Periodic access reviews** — Review access rights periodically (minimum annually) and revoke when no longer needed.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| AI Data Access Control Matrix | Defined access rights by role for each AI data category | CISO / Chief Data Officer |
| Access Control Configuration Records | Technical evidence of access control implementation | DevOps / CISO |
| AI Data Access Logs | Audit logs of access to AI training and production data | DevOps |
| Access Review Records | Periodic review of access rights with revocation evidence | CISO / Chief Data Officer |

#### How to Audit

**Document Review:**
- Verify access control matrix exists for AI data
- Check access controls are technically implemented (not just documented)
- Confirm access logs are retained

**Technical Review:**
- Review access control configuration for AI data stores
- Check audit log retention period

**Evidence Required**
- AI data access control matrix
- Access control configuration evidence
- Access logs (sample)
- Periodic access review records

**Common Gaps Found in Audits**
- Training data accessible to all members of the AI team — no least privilege
- No separation between training, validation, and test data stores
- Access logs not retained — cannot reconstruct who accessed data
- Access rights never reviewed — departed employees retain access

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 10 (Data governance); Art. 9 (Risk management) |
| NIST AI RMF | MAP 2.3, GOVERN 1.6 |
| ISO 27001:2022 | A.5.15 (Access control); A.5.18 (Access rights) |

## DOMAIN A.8 — INFORMATION FOR INTERESTED PARTIES
*4 Controls | Ensuring transparency, explainability, and communication about AI*

---

### A.8.2 — AI Capability Information

**Control Statement:** The organization shall provide accurate, clear, and non-misleading information about the capabilities, performance, and limitations of its AI systems to relevant interested parties.

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

### A.8.3 — AI Explainability

**Control Statement:** The organization shall implement explainability mechanisms appropriate to the AI system's risk level and use case, enabling affected individuals and relevant stakeholders to understand AI-driven decisions or recommendations to the degree necessary.

---

#### What It Means

A.8.3 requires that AI decisions can be explained — particularly when those decisions affect individuals. The required level of explainability depends on the use case: a low-risk content recommendation may require minimal explanation; an employment or credit decision may require a full explanation of the factors that drove the outcome. This control requires organizations to design explainability into AI systems, not to add it as an afterthought.

#### Why It Matters

Without explainability: individuals affected by AI decisions cannot understand or challenge them; human reviewers cannot meaningfully evaluate AI recommendations; regulators cannot assess compliance; systemic bias is harder to detect and address. GDPR Article 22 requires meaningful information about automated decision-making logic for individuals.

#### How to Implement

- **Define explainability requirements per AI system** — Based on: risk level (higher risk = higher explainability requirement); regulatory requirements (GDPR Art. 22 for automated decisions); operational need (human reviewers need to understand AI recommendations to exercise meaningful oversight).
- **Implement appropriate explainability techniques** — Options: feature importance (SHAP, LIME); counterfactual explanations ("if X had been different, the outcome would have been Y"); example-based explanations; rule extraction. Choose technique appropriate to the use case and audience.
- **Design explanations for the intended audience** — Explanations for data scientists, for human reviewers, and for affected individuals are different. Design accordingly.
- **Ensure explanations are actionable** — Explanations that tell someone their application was rejected because "features contributed negatively" are not actionable. Explanations must enable the individual to understand what to do differently.

#### Documents to Prepare

| Document | Description | Owner |
|---|---|---|
| Explainability Requirements per AI System | Defined explainability requirements based on risk and regulatory obligations | AI Governance Lead |
| Explainability Design Documentation | Technical design of explainability mechanisms per AI system | ML Engineer |
| Individual Explanation Examples | Examples of the explanations provided to affected individuals | AI Governance Lead / Product Owner |

#### How to Audit

**Document Review:**
- Verify explainability requirements are defined per AI system
- Review individual explanation examples — are they meaningful and actionable?

**Behavioral Testing:**
- Ask to see the explanation a user would receive if this AI system made a decision affecting them.
- Is the explanation meaningful? Can the individual understand what factors drove the decision and what to do differently?

**Evidence Required**
- Explainability requirements documentation
- Explainability design documentation
- Sample individual explanations

**Common Gaps Found in Audits**
- Explainability not designed into the system — added post-hoc with limited capability
- Explanations provided in technical terms not comprehensible to affected individuals
- Explainability exists for data scientists but not for affected individuals
- Explanations describe what the AI did but are not actionable — individual cannot understand what to do differently

#### Cross-References

| Framework | Reference |
|---|---|
| EU AI Act | Art. 13 (Transparency); Art. 86 (Right to explanation) |
| NIST AI RMF | MAP 1.1, MEASURE 2.6 |

---

### A.8.4 — AI Disclosure to Users

**Control Statement:** The organization shall ensure that users interacting with AI systems are appropriately informed that they are interacting with AI, and shall provide relevant information about the AI system's nature, capabilities, and limitations.

---

#### What It Means

A.8.4 requires that AI is not used to deceive users into thinking they are interacting with a human or with a more capable system than actually exists. This includes: disclosure when chatbots or virtual agents are AI (not humans); disclosure when AI is making or significantly influencing decisions that affect users; disclosure when content is AI-generated.

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

### A.8.5 — AI Incident Communication

**Control Statement:** The organization shall establish and implement processes for timely and appropriate communication with affected individuals, regulators, and other relevant parties when AI-related incidents occur.

---

#### What It Means

A.8.5 requires that when an AI system fails, causes harm, or is involved in a significant incident, the organization communicates appropriately. This includes: internal incident communication (to management, board); regulatory notification (to data protection authority, sector regulator, EU AI Office for high-risk AI); individual notification (to affected individuals); public communication (where incident is of public significance).

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

## DOMAIN A.9 — USE OF AI SYSTEMS
*3 Controls | Governing how AI is used in operational contexts*

---

### A.9.2 — Acceptable Use of AI

**Control Statement:** The organization shall define, document, communicate, and enforce acceptable use policies for AI systems, covering permitted and prohibited uses, responsible use guidance, and consequences for policy violations.

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

### A.9.3 — Human Oversight

**Control Statement:** The organization shall implement effective human oversight mechanisms for AI systems used in high-stakes decisions, ensuring humans have the ability to understand, review, override, and suspend AI outputs, and that oversight personnel are appropriately qualified.

---

#### What It Means

A.9.3 is the operational human oversight control — applying in live production operations. It requires that qualified people are actively and meaningfully reviewing AI decisions, overrides are being exercised appropriately, and humans are not simply rubber-stamping AI outputs.

#### Why It Matters

Automation bias — the tendency to over-trust automated systems — is well-documented and dangerous. In high-stakes AI applications (medical diagnosis, credit decisioning, criminal justice, hiring), the consequence of blind AI acceptance can be serious and irreversible harm.

#### How to Implement

1. **Define "high-stakes" for your context** — Criteria: Impact on fundamental rights; Irreversibility; Severity of potential harm; Regulatory requirement. Examples: automated employment decisions; credit/loan decisions; medical treatment recommendations; law enforcement decisions.
2. **Design meaningful oversight** — Informed (overseers see what they need); Timely (can operate at the speed of decisions); Empowered (can override without friction); Proportionate to risk level.
3. **Prevent automation bias** — Present AI recommendation with uncertainty; Show supporting evidence; Require active human judgment rather than passive confirmation.
4. **Qualify overseers** — Overseers must have domain knowledge and AI literacy to meaningfully evaluate AI outputs.
5. **Monitor oversight quality** — Track override rates; investigate suspiciously low override rates; conduct periodic oversight quality audits.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| Human Oversight Policy | Defines which AI decisions require oversight and at what level | AI Governance Lead |
| AI Human Oversight Procedure | Operational procedure for oversight personnel | Operations / AI Governance Lead |
| Overseer Qualification Requirements | Required qualifications and competencies for each oversight role | HR / AI Governance Lead |
| Override Log | Record of human overrides and their basis | Operations |
| Oversight Quality Audit Reports | Periodic audits of oversight effectiveness | AI Governance Lead / Internal Audit |
| Automation Bias Risk Assessment | Assessment of automation bias risk and design mitigations | UX Lead / AI Governance Lead |

#### How to Audit

**Document Review:**
- Verify oversight policy identifies all high-stakes AI decisions requiring oversight
- Check override logs — are overrides occurring at plausible rates?

**Behavioral Testing:**
- Observe oversight personnel: Do they actively consider AI recommendations or passively approve?
- Present an overseer with a clearly wrong AI recommendation: Do they catch it? Can they override?

**Interview Questions:**
- Ask an overseer: "When did you last override an AI recommendation? Why? What happened next?"
- Ask a manager: "What is your AI override rate? Is that what you'd expect?"
- "Can you show me a case where a human reviewer changed an AI decision?"

**Audit Testing:**
- Review override logs for 3 months. Calculate override rate. Is it plausible?
- Check overseer training records and qualification verification.

#### Evidence Required

- Human oversight policy
- Override logs with rates and documented reasons
- Overseer qualification records
- Anti-automation-bias design evidence
- Oversight quality audit reports

#### Common Gaps Found in Audits

- Zero override rate over 6 months for high-volume AI — clear rubber-stamping
- Overseers lack domain knowledge to evaluate AI recommendations
- Override mechanism requires 3 approvals and IT tickets — never used in practice
- High-stakes AI decisions list is 18 months out of date — missing new AI deployments

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 14 (Human oversight for high-risk AI) |
| NIST AI RMF | MANAGE 1.3, GOVERN 6.2 |
| ISO 27001:2022 | A.8.15 (Logging) |

---

### A.9.4 — AI Error Handling

**Control Statement:** The organization shall define and implement processes to detect, handle, log, and respond to AI system errors, failures, unexpected behaviors, and outputs that fall outside expected parameters.

---

#### What It Means

AI systems fail differently from traditional software — they do not "crash" clearly; they produce wrong outputs confidently. A.9.4 requires error handling specifically designed for AI: detecting when AI output is outside expected bounds, handling gracefully, logging for investigation, and triggering appropriate response.

#### Why It Matters

Silent AI failures — where the system produces output without raising a technical error — are a unique AI risk. A classifier returning 50% confidence raises no system alert but is providing unreliable output. A generative AI that hallucinates raises no error. AI error handling must catch "soft failures" that traditional monitoring misses.

#### How to Implement

1. **Define AI error categories** — Hard failures (crashes, timeouts); Soft failures (below-threshold confidence, out-of-distribution outputs); Behavioral anomalies (sudden output distribution shifts, unusual inputs).
2. **Implement confidence-based handling** — Define minimum confidence thresholds; below threshold: route to human review, decline to respond, or return "uncertain" response.
3. **Implement output validation** — Validate AI outputs against expected ranges and constraints before acting on them.
4. **Comprehensive error logging** — Log all errors (hard and soft) with: triggering input; AI output; error type and confidence; timestamp; system context.
5. **Error response procedures** — Define what happens at each error category level: immediate response; root cause investigation; escalation to incident response.
6. **Human fallback** — For high-stakes AI, define a human fallback for when AI is unavailable or unreliable.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| AI Error Handling Design | Technical design for error detection and handling per system | ML Engineer / Software Architect |
| AI Error Classification Scheme | Categories of AI errors and handling procedures | AI Governance Lead / ML Engineer |
| AI Error Log | Technical log of AI errors in production (hard and soft) | DevOps / ML Engineer |
| Error Response Procedure | Operational procedure for responding to AI errors | Operations / AI Governance Lead |
| Human Fallback Procedure | Documented fallback for when AI is unavailable or unreliable | Operations |
| Error Trend Analysis Reports | Regular review of AI error patterns | AI Governance Lead / Model Owner |

#### How to Audit

**Document Review:**
- Verify error handling design covers both hard and soft failures
- Check error logs are generated, retained, and reviewed
- Confirm human fallback procedures exist for high-stakes AI systems

**Technical Review:**
- Review AI system code for confidence threshold implementation
- Check output validation configuration
- Review error log completeness and retention period

**Interview Questions:**
- "What happens if this AI returns a recommendation with very low confidence? How is that handled?"
- "Show me the error log for this AI. How often are errors occurring? How are they investigated?"
- "If this AI system went down completely right now, what would operations do?"

**Audit Testing:**
- Test AI system with boundary inputs: Does it handle them gracefully? Does it log the error?
- Request error log for past month: Are errors being reviewed?

#### Evidence Required

- AI error handling design documentation
- Error logs for production AI systems
- Confidence threshold configuration evidence
- Error investigation records
- Human fallback procedure documentation

#### Common Gaps Found in Audits

- Error handling limited to server errors — soft failures not logged or handled
- No confidence thresholds — AI always responds with same authority regardless of actual confidence
- Error logs retained for 7 days — insufficient for investigation
- No human fallback for high-stakes AI — "call IT" is not an adequate procedure
- Errors logged but never reviewed — no trend analysis

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 9 (Risk management — error detection); Art. 15 (Accuracy, robustness) |
| NIST AI RMF | MANAGE 2.2, MANAGE 3.2 |
| ISO 27001:2022 | A.8.16 (Monitoring activities) |

---

## DOMAIN A.10 — THIRD-PARTY AND CUSTOMER AI
*3 Controls | Managing AI risk across the supply chain and customer relationships*

---

### A.10.2 — Third-Party AI Risk Assessment

**Control Statement:** The organization shall conduct documented risk assessments of third-party AI systems, APIs, models, and services before adoption, covering technical performance, bias, security, privacy, regulatory compliance, and supplier governance maturity.

---

#### What It Means

Before adopting an AI system, API, or service from a third party — whether a vendor AI product, a cloud AI service, an open-source model, or an embedded AI component — the organization must systematically assess the risks. A.10.2 requires this to be documented, structured, and proportionate to the risk level of the third-party AI.

#### Why It Matters

Most organizations today use more third-party AI than they build themselves. Every cloud AI service, every SaaS product with AI features, every pre-trained model adopted from Hugging Face is a third-party AI in scope for A.10.2. These systems carry inherited risks: bias baked into training data the organization never saw; security vulnerabilities in the model or API; regulatory non-compliance in the supplier's practices; data handling practices that conflict with privacy obligations. Governance of third-party AI is one of the most significant gaps in most organizations' AI risk management.

#### How to Implement

1. **Create a third-party AI inventory** — List every third-party AI system in use or under evaluation: vendor AI products (SaaS with AI features); cloud AI APIs (OpenAI, Azure AI, Google AI, AWS AI services); open-source models adopted from repositories; AI components embedded in other procured software.
2. **Define risk classification criteria** — Classify third-party AI by risk level based on: What decisions does it influence? Does it process personal data? What is the scale of use? Is it used in high-stakes contexts? Higher risk = deeper assessment required.
3. **Conduct structured assessments** — For each third-party AI (depth proportionate to risk): Technical performance: Has the supplier provided validated performance metrics? Are they verified for your use case and data? Bias and fairness: What bias evaluation has the supplier conducted? What protected attributes were assessed? What are known limitations? Security: What security certifications does the supplier hold? How is the model/API secured? What are the data handling practices? Privacy: Where is data processed? What data is retained? Is there a DPA available? Regulatory compliance: Is the supplier compliant with EU AI Act where applicable? What is their regulatory status for your jurisdiction? Supplier governance: Does the supplier have an AI governance framework? Are they ISO 42001 certified or working toward it?
4. **Document assessment findings** — Use a standardized assessment template. Record findings, risk ratings, and treatment decisions.
5. **Approval gate** — Third-party AI above a defined risk threshold requires formal approval before adoption.
6. **Ongoing review** — Reassess periodically (annually minimum) and on significant changes.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
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

### A.10.3 — AI Supplier Contracts

**Control Statement:** The organization shall ensure that contracts with AI suppliers include appropriate AI governance, responsible AI, transparency, compliance, and notification obligations, including the right to audit and requirements for incident notification.

---

#### What It Means

A risk assessment alone is not sufficient — the organization must contractually bind AI suppliers to governance obligations. A.10.3 requires that AI-specific terms are included in supplier contracts: performance obligations, ethical AI commitments, incident notification requirements, audit rights, data handling obligations, and regulatory compliance obligations.

#### Why It Matters

Without contractual protections, organizations have no recourse when a third-party AI system causes harm. If the supplier's model exhibits bias that causes discrimination in your deployment, if they suffer a security breach affecting your data, if their model degrades significantly — you need contractual levers to demand remedy, access information, and exit if necessary. Generic commercial contracts do not address AI-specific risks.

#### How to Implement

1. **Develop an AI supplier contract standard clauses library** — A set of required contractual provisions for AI supplier agreements. Engage legal and AI governance to develop these.
2. **Define required clauses by risk tier** — Higher-risk AI suppliers require more comprehensive contractual protections. Minimum clauses for all AI suppliers: Performance obligations and SLAs; Data handling obligations (DPA where required); Incident notification obligations (including AI-specific incidents); Right to request information about AI system changes; Liability for AI-related harms.
3. **Enhanced clauses for high-risk AI suppliers** — Additionally: Audit rights (right to review supplier's AI governance practices); Bias and fairness obligations (supplier must disclose bias evaluation results; must notify of significant bias findings); Regulatory compliance obligations (must comply with applicable AI regulations; must notify of regulatory investigations); Change notification (must notify of significant changes to AI model, training data, or system architecture); Exit obligations (data return/deletion; cooperation with transition).
4. **Integrate into procurement process** — AI-specific contract terms must be reviewed and agreed before any high-risk AI supplier contract is executed.
5. **Review existing contracts** — For existing AI supplier relationships, identify gaps against the standard clauses library and seek to amend or negotiate at renewal.
6. **Maintain contract register** — Track AI supplier contracts, key terms, expiry dates, and review schedule.

#### Documents to Prepare

| Document | Description | Owner |
|----------|-------------|-------|
| AI Supplier Standard Contract Clauses | Library of required AI-specific contractual provisions by risk tier | Legal / AI Governance Lead |
| AI Supplier Contract Register | Register of all AI supplier contracts with key terms and dates | Legal / Procurement |
| AI Supplier Contract Review Records | Evidence of legal and AI governance review of supplier contracts | Legal |
| Contract Gap Analysis for Existing Suppliers | Assessment of existing contracts against required AI clauses | Legal / AI Risk Manager |
| DPA Register | Register of Data Processing Agreements with AI suppliers | DPO / Legal |

#### How to Audit

**Document Review:**
- Verify AI standard contract clauses library exists and covers all required areas
- Review sample AI supplier contracts against the standard — are required clauses present?
- Check DPA register — are DPAs in place for all AI suppliers processing personal data?

**Personnel Interviews:**
- Ask Legal: "When we procure an AI service, what AI-specific terms do we require in the contract? Show me a recent example."
- Ask Procurement: "Has our standard supplier contract been updated to include AI governance clauses?"
- Ask the AI Governance Lead: "Do you have audit rights over your AI suppliers? Have you exercised them?"

**Audit Testing:**
- Select 3 AI supplier contracts. Check for presence of: performance SLAs; data handling obligations; AI incident notification obligation; right to information on AI system changes; audit rights (for high-risk suppliers); regulatory compliance obligations.
- For one key AI supplier, verify DPA is executed and covers the specific AI processing activities.

#### Evidence Required

- AI supplier standard contract clauses document
- Sample AI supplier contracts with required clauses highlighted
- DPAs for AI suppliers processing personal data
- Contract gap analysis for existing suppliers
- AI supplier contract register

#### Common Gaps Found in Audits

- No AI-specific contract clauses — standard commercial terms only
- Data Processing Agreements in place but do not specifically address AI model training use of data
- No incident notification obligation — organization would not be informed if supplier's AI suffered a security breach or produced systematic bias
- No audit rights — no mechanism to verify supplier's AI governance practices
- Existing high-risk AI supplier contracts have no AI-specific protections — not remediated

#### Cross-References

| Framework | Reference |
|-----------|-----------|
| EU AI Act | Art. 25 (Distributor obligations); Art. 28 (AI system providers and deployers) |
| NIST AI RMF | MAP 5.2, GOVERN 6.1 |
| ISO 27001:2022 | A.5.20 (Addressing security within supplier agreements) |

---

### A.10.4 — Customer AI Governance

**Control Statement:** Where the organization provides AI-enabled products or services to customers, it shall identify and meet applicable customer AI governance, transparency, explainability, and compliance requirements.

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

## MASTER SUMMARY — ALL 39 ANNEX A CONTROLS AT A GLANCE

| Control | Title | Domain | Key Document(s) | Key Audit Test |
|---------|-------|--------|-----------------|----------------|
| A.2.2 | AI Policy | Policies | AI Policy (AIMS-POL-001) | Check signature, date, communication evidence |
| A.2.3 | AI-Specific Policies | Policies | Prohibited Use Policy; Acceptable Use Policy | Verify GenAI tool use is explicitly addressed |
| A.3.2 | AI Governance Roles | Organisation | RACI Matrix; Role Profiles | Trace a deployment — who approved it? |
| A.3.3 | Segregation of Duties | Organisation | SoD Policy; Access Control Matrix | Developer ≠ deployment approver: verify in system |
| A.3.4 | Contact with AI Authorities | Organisation | Regulatory Watch List; Engagement Log | Evidence of regulatory intelligence feeding AIMS |
| A.3.6 | AI in Project Management | Organisation | AI Project Governance Framework | Sample 3 AI projects — all governance gates completed? |
| A.4.2 | AI Competencies | Resources | Competency Framework; Training Records | Gap assessments current; training effectiveness evaluated |
| A.4.3 | AI Infrastructure Security | Resources | Infrastructure Inventory; DR Plan | Access controls and patching for AI infrastructure |
| A.4.4 | AI Tool Security | Resources | Approved Tools List; SCA Reports | Any unapproved tools or unassessed pre-trained models? |
| A.5.2 | AI System Impact Assessment | Impact | ASIA Template; ASIA Register | ASIA completed BEFORE deployment — check dates |
| A.5.3 | Societal & Ethical Impact | Impact | ASIA Societal Section; Ethics Review | Societal section substantive, not blank or N/A |
| A.5.4 | Use of Assessment Results | Impact | ASIA-to-Risk Register Mapping | Trace ASIA finding → risk register → implemented control |
| A.6.1.1 | AI Design Requirements | Lifecycle | AI Requirements Spec | Fairness requirements specific and measurable? |
| A.6.1.2 | AI Design Documentation | Lifecycle | Architecture Doc; Model Design Doc | Updated after last system change? |
| A.6.2.1 | AI Development Process | Lifecycle | ADLC Procedure; Code Review Records | Version control in use for model artifacts? |
| A.6.2.3 | Model Documentation (Model Cards) | Lifecycle | Model Card Template; Model Registry | Subgroup fairness metrics populated in model cards? |
| A.6.2.5 | Adversarial Testing | Lifecycle | Adversarial Test Plan; Test Results | LLM prompt injection tested? Red team results? |
| A.6.2.6 | Bias Evaluation | Lifecycle | Bias Eval Reports; Fairness Thresholds | Disaggregated metrics by protected attribute — passed threshold? |
| A.6.2.8 | Testing in Representative Environments | Lifecycle | Test Plan; Test Results | Production-representative data used for testing? |
| A.6.3.1 | AI Deployment Controls | Lifecycle | Deployment Auth Records; Rollback Procedure | Authorization pre-deployment; rollback tested? |
| A.6.3.3 | Human Oversight at Deployment | Lifecycle | Oversight Verification Record | Demonstrate override works — live test |
| A.6.4.1 | AI Operation Monitoring | Lifecycle | Monitoring Dashboard; Alert Config | Unresolved alerts? Who reviews and how often? |
| A.6.4.2 | Performance Drift Monitoring | Lifecycle | Drift Detection Config; Retraining Records | Drift monitoring active; retraining decisions documented |
| A.6.5.1 | AI Decommissioning | Lifecycle | Decommissioning Procedure; Data Deletion Records | Any "switched-off" AI with data still on servers? |
| A.7.2 | AI Data Quality | Data | Data Quality Standards; Assessment Records | Specific, measurable quality thresholds defined and met |
| A.7.3 | Data Provenance | Data | Data Catalog; Lineage Docs; Licensing Register | Can you reproduce a training run? License for AI training confirmed? |
| A.7.4 | Data Privacy for AI | Data | DPIAs; Lawful Basis Register; DPAs | DPIAs for all AI with personal data; DPA for cloud AI APIs |
| A.7.5 | Bias Mitigation in Data | Data | Training Data Bias Assessment; Mitigation Records | Training data bias assessed before model training? |
| A.7.6 | Data Access Controls | Data | AI Data Access Matrix; Access Review Records | Least privilege applied; access reviewed; logs retained |
| A.8.2 | AI Capability Information | Information | Capability Sheets; Performance Fact Sheets | Marketing claims match verified performance metrics? |
| A.8.3 | AI Explainability | Information | Explainability Requirements; Explanation Design | Affected individuals receive meaningful, actionable explanations |
| A.8.4 | AI Disclosure to Users | Information | Disclosure Policy; UI/UX Evidence | Users told they are interacting with AI — clear and prominent? |
| A.8.5 | AI Incident Communication | Information | Incident Comm Policy; Templates; Comm Log | Notifiable AI incidents — communication timelines met? |
| A.9.2 | Acceptable Use of AI | Use | Acceptable Use Policy; Approved Tools List | GenAI tools addressed; employees aware and signed off |
| A.9.3 | Human Oversight | Use | Oversight Policy; Override Log | Override rate plausible? Overseers qualified? |
| A.9.4 | AI Error Handling | Use | Error Handling Design; Error Log; Fallback Procedure | Soft failures logged? Confidence thresholds configured? |
| A.10.2 | Third-Party AI Risk Assessment | Third Party | 3P AI Inventory; Assessment Records; Approval Register | All third-party AI inventoried; assessments pre-adoption |
| A.10.3 | AI Supplier Contracts | Third Party | Standard AI Contract Clauses; DPA Register | AI clauses in supplier contracts; audit rights; incident notification |
| A.10.4 | Customer AI Governance | Third Party | Customer-Facing AI Docs; Requirements Register | Customer obligations met; audit requests can be supported |

---

## MASTER DOCUMENT CHECKLIST

Use this checklist to track documentation completeness across all 39 Annex A controls.

### Governance & Policy Documents
- [ ] AI Policy (AIMS-POL-001) — A.2.2
- [ ] AI-Specific Sub-Policies (Prohibited Use, Acceptable Use, Human Oversight, Ethics, Data Governance) — A.2.3
- [ ] AI Governance RACI Matrix and Role Profiles — A.3.2
- [ ] AI SoD Policy and Access Control Matrix — A.3.3
- [ ] Regulatory Watch List and Engagement Log — A.3.4
- [ ] AI Project Governance Framework — A.3.6

### Resources & Competence Documents
- [ ] AI Competency Framework and Gap Assessments — A.4.2
- [ ] Training Records and Effectiveness Reviews — A.4.2
- [ ] AI Infrastructure Inventory and Security Standards — A.4.3
- [ ] Approved AI Tools and Libraries List — A.4.4
- [ ] Pre-trained Model Registry — A.4.4

### Impact Assessment Documents
- [ ] ASIA Template — A.5.2
- [ ] Completed ASIAs per AI System — A.5.2
- [ ] ASIA Register — A.5.2
- [ ] Environmental Impact Assessments for Large Models — A.5.3
- [ ] ASIA-to-Risk Register Mapping — A.5.4

### AI Lifecycle Documents
- [ ] Responsible AI Requirements Template — A.6.1.1
- [ ] AI System Requirements Specifications — A.6.1.1
- [ ] AI System Architecture Documents — A.6.1.2
- [ ] Model Design Documents — A.6.1.2
- [ ] AI Development Lifecycle Procedure — A.6.2.1
- [ ] Code Review and Checkpoint Records — A.6.2.1
- [ ] Model Card Template and Completed Model Cards — A.6.2.3
- [ ] Model Registry — A.6.2.3
- [ ] Adversarial Testing Plans and Results — A.6.2.5
- [ ] Bias Evaluation Methodology and Reports — A.6.2.6
- [ ] Fairness Criteria per AI System — A.6.2.6
- [ ] Test Environment Standards and Test Results — A.6.2.8
- [ ] AI Deployment Procedure — A.6.3.1
- [ ] Deployment Authorization Records — A.6.3.1
- [ ] Rollback Procedures (tested) — A.6.3.1
- [ ] Human Oversight Design Documents — A.6.3.3
- [ ] Oversight Verification Records — A.6.3.3
- [ ] AI Monitoring Framework and Dashboards — A.6.4.1
- [ ] Drift Detection Configuration and Reports — A.6.4.2
- [ ] Retraining Decision Records — A.6.4.2
- [ ] AI Decommissioning Procedure and Records — A.6.5.1

### Data Documents
- [ ] AI Data Quality Standards and Assessment Records — A.7.2
- [ ] AI Data Catalog and Lineage Documentation — A.7.3
- [ ] Data Licensing Register — A.7.3
- [ ] DPIAs for AI Systems — A.7.4
- [ ] Lawful Basis Register for AI Processing — A.7.4
- [ ] DPAs for Cloud AI Services — A.7.4
- [ ] Training Data Bias Assessment Reports — A.7.5
- [ ] AI Data Access Control Matrix and Review Records — A.7.6

### Information & Transparency Documents
- [ ] AI Capability and Limitation Sheets — A.8.2
- [ ] Explainability Requirements and Design Documentation — A.8.3
- [ ] AI Disclosure Policy and UI/UX Evidence — A.8.4
- [ ] AI Incident Communication Policy and Templates — A.8.5

### Use & Oversight Documents
- [ ] Acceptable Use of AI Policy — A.9.2
- [ ] Approved External AI Tools List — A.9.2
- [ ] Human Oversight Policy and Procedures — A.9.3
- [ ] Override Logs and Quality Audit Reports — A.9.3
- [ ] AI Error Handling Design and Error Logs — A.9.4
- [ ] Human Fallback Procedures — A.9.4

### Third-Party & Customer Documents
- [ ] Third-Party AI Inventory — A.10.2
- [ ] Third-Party AI Assessment Records — A.10.2
- [ ] AI Supplier Standard Contract Clauses — A.10.3
- [ ] AI Supplier Contract Register — A.10.3
- [ ] Customer-Facing AI Documentation Pack — A.10.4
- [ ] Customer AI Governance Requirements Register — A.10.4

---

## AUDIT INTERVIEW QUESTION BANK

A consolidated list of the most impactful audit questions across all 39 controls. Use these in Stage 1 (document review) and Stage 2 (effectiveness audit) interviews.

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
| 1.0 | April 2026 | Ankit Uniyal | Initial release — all 39 Annex A controls |

---

## DISCLAIMER

This guide is provided for educational and practical guidance purposes only. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text (available from ISO or your national standards body) for definitive normative requirements.

All templates and guidance must be adapted to your specific organizational context, sector, jurisdiction, and AI risk profile. Organizations seeking ISO 42001 certification should engage a qualified implementation consultant and accredited certification body.

The author has made every effort to ensure accuracy at the time of writing, but this guidance may not reflect the latest regulatory developments. Always verify current regulatory requirements with qualified legal counsel.

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Part of the ISO 42001 AI Governance Toolkit: github.com/Ankit-Uniyal/iso-42001-ai-governance-toolkit*
*MIT License — Free to use, adapt, and distribute with attribution*
