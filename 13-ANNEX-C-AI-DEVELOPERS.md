# Annex C — Guidance for Organisations Developing AI for Other Organisations
## ISO/IEC 42001:2023 | Informative Reference Guide

> **Note:** This document is an implementation reference guide based on ISO/IEC 42001:2023 Annex C concepts. It is NOT a reproduction of the standard. Users must obtain a licensed copy from ISO (iso.org) for the full normative text.
>
> ---
>
> ## Purpose
>
> ISO/IEC 42001:2023 Annex C provides specific guidance for organisations that **develop AI systems for use by other organisations** — i.e., AI developers, AI product companies, AI-as-a-Service providers, and managed AI service providers. This document summarises those concepts and provides practical implementation templates for the developer-side AIMS.
>
> This applies to your organisation if you:
> - Build AI models or AI systems that other organisations purchase or licence
> - - Provide AI APIs, AI platforms, or AI SaaS products to customers
>   - - Develop custom AI solutions deployed in customer environments
>     - - Supply pre-trained models, datasets, or AI components to other organisations
>      
>       - ---
>
> ## C.1 — The AI Developer's Unique AIMS Position
>
> Organisations that develop AI for others occupy a unique position in the AI supply chain. They are simultaneously:
> - **An AI system operator** within their own AIMS scope
> - - **An AI system supplier** to their customer's AIMS
>  
>   - This creates dual responsibilities that must both be reflected in the AIMS.
>  
>   - ### Developer vs. Deployer Responsibilities
>  
>   - | Responsibility | AI Developer | AI Deployer (Customer) | Shared |
>   - |---------------|-------------|----------------------|--------|
>   - | Training data quality and bias | Primary | — | — |
>   - | Model design and architecture | Primary | — | — |
>   - | Model performance documentation | Primary | — | — |
>   - | Intended use definition | Primary | Confirms fit | Both define |
>   - | Fairness evaluation | Primary | Validate for context | Both |
>   - | Security of the model | Primary | Security of deployment | Both |
>   - | Human oversight mechanism | Design | Implement | Both |
>   - | Data used in deployment | — | Primary | — |
>   - | Monitoring in production | Design monitoring | Operate monitoring | Both |
>   - | Incident response | Model defects | Deployment incidents | Both |
>   - | User disclosure | Design disclosure | Implement disclosure | Both |
>
>   - ---
>
> ## C.2 — Developer-Specific AIMS Requirements
>
> ### C.2.1 — Customer-Facing AI Documentation
>
> AI developers must provide customers with sufficient documentation to enable them to implement and operate the AI system responsibly. This is a core requirement of Annex C.
>
> **Minimum documentation to provide to each customer:**
>
> | Document | Contents | Who Prepares | Timing |
> |---------|---------|-------------|--------|
> | AI System Model Card | Architecture, training data, performance metrics, limitations, fairness evaluation | Developer | At delivery |
> | Intended Use Statement | Authorised uses; explicitly prohibited uses; conditions for safe use | Developer | At delivery |
> | AI System Integration Guide | How to deploy, configure, and integrate the AI system | Developer | At delivery |
> | Security Advisory | Known vulnerabilities, security considerations, hardening guidance | Developer | At delivery + updates |
> | Fairness Assessment Report | Fairness metrics by demographic group; methodology; thresholds | Developer | At delivery + updates |
> | Monitoring Guidance | What to monitor; recommended alert thresholds; drift detection | Developer | At delivery |
> | Incident Reporting Process | How to report AI system defects back to the developer | Developer | At delivery |
> | Model Update Notifications | Process for notifying customers of material model changes | Developer | Ongoing |
>
> See `AI-MODEL-CARD-TEMPLATE.md` for the standard model card format.
>
> ---
>
> ### C.2.2 — Contractual Requirements for AI Developers
>
> Developer contracts with customers (and with their own AI sub-suppliers) must include appropriate AI governance clauses. See `AI-SUPPLIER-CONTRACT-CLAUSES.md` for standard contract clauses.
>
> Key contractual provisions AI developers must address:
>
> **Provisions to include in customer contracts:**
> - Warranty of fitness for intended use
> - - Limitations on liability for out-of-scope uses
>   - - Notification obligations for material model changes
>     - - Data processing terms (if model processes customer data)
>       - - Audit rights for regulatory compliance verification
>         - - Incident notification and cooperation obligations
>           - - IP and licensing terms for model weights and outputs
>            
>             - **Provisions to require from AI sub-suppliers (data providers, foundational model vendors, etc.):**
>             - - Data provenance and licensing warranties
>               - - Bias and fairness certifications (where available)
>                 - - Security and vulnerability disclosure obligations
>                   - - Notification of material changes to foundational models
>                     - - Right to audit sub-supplier AI governance practices
>                      
>                       - ---
>
> ### C.2.3 — Training Data Governance for Developers
>
> AI developers have primary responsibility for the governance of training data. Auditors will scrutinise this area closely.
>
> **Training Data Governance Requirements:**
>
> | Area | Requirement | Evidence Required |
> |------|------------|------------------|
> | Data provenance | Document source and licensing of all training data | Data provenance register |
> | Data quality | Assess and document data quality before training | Data quality assessment report |
> | Bias assessment | Assess training data for demographic bias | Bias assessment report |
> | Personal data | Identify and document any personal data in training sets | DPIA or equivalent |
> | Data retention | Define retention periods for training data | Records retention schedule |
> | Data security | Secure training data against unauthorised access | Access control records |
> | Third-party data | Comply with licensing and IP terms for all third-party data | Licence register |
>
> ---
>
> ### C.2.4 — Responsible AI by Design
>
> AI developers are responsible for embedding responsible AI requirements at the design stage — before any code is written.
>
> **Design Stage Checklist for AI Developers:**
>
> | Checkpoint | Requirement | ISO/IEC 42001 Ref |
> |-----------|------------|------------------|
> | Intended use defined | Clear statement of intended and prohibited uses | A.4.2 |
> | Fairness requirements | Fairness constraints defined before training | A.4.7 |
> | Explainability approach | Explainability method selected and documented | A.4.8 |
> | Human oversight mechanism | Designed into system architecture | A.3.2 |
> | Privacy by design | Personal data minimised; retention limits built in | A.4.9 |
> | Security by design | Threat model completed; adversarial defences designed in | A.4.5 |
> | AI Act classification | EU AI Act risk classification completed | A.10.2 |
> | DPIA trigger assessment | Determined whether DPIA is required | A.4.9 |
>
> ---
>
> ## C.3 — AI Supplier Risk Register (Developer Perspective)
>
> As an AI developer, you are both a **supplier** to your customers and a **customer** of your own AI sub-suppliers (data providers, foundational model vendors, cloud AI services). Maintain a supplier risk register covering both directions.
>
> See `AI-SUPPLIER-RISK-REGISTER.md` for the register template.
>
> **Supplier risk categories specific to AI developers:**
>
> | Risk Category | Description | Mitigation |
> |--------------|-------------|-----------|
> | Foundational model changes | Vendor updates foundational model without notice, changing behaviour | Contractual notification requirements; version pinning |
> | Data licensing | Training data licence revoked or changed retroactively | Licence audits; IP warranties from data providers |
> | Sub-processor risk | Cloud AI services process personal data in non-compliant jurisdictions | DPA agreements; adequacy assessments |
> | Open-source model risk | Open-source foundational model contains hidden vulnerabilities or biases | Security scanning; bias evaluation; licence compliance |
> | API discontinuation | Third-party AI API discontinued, breaking dependent products | Dependency risk assessment; fallback planning |
>
> ---
>
> ## C.4 — Developer AIMS Scope Considerations
>
> When determining AIMS scope as an AI developer, consider:
>
> 1. **Which AI products are in scope?** List all AI systems/products you develop for customers
> 2. 2. **Which development activities are in scope?** Training, fine-tuning, testing, deployment pipelines
>    3. 3. **Which customers are in scope?** Consider risk-tiering customers by the criticality of their AI use
>       4. 4. **What AI sub-suppliers are in scope?** Data providers, foundational model vendors, cloud AI platforms
>          5. 5. **What development environments are in scope?** Training infrastructure, CI/CD pipelines, model registries
>            
>             6. ---
>            
>             7. ## C.5 — Developer-Specific Documents Checklist
>            
>             8. | # | Document | Purpose | Where |
> |---|---------|---------|-------|
> | 1 | AI Product Model Cards | Per-product documentation for customers | AI-MODEL-CARD-TEMPLATE.md |
> | 2 | Training Data Provenance Register | Source and licensing of all training data | AI-RISK-REGISTER.md (data risks) |
> | 3 | Fairness Assessment Reports | Per-product fairness evaluation by demographic group | AI-SYSTEM-IMPACT-ASSESSMENT.md |
> | 4 | Intended Use Statements | Authorised and prohibited uses per AI product | AI-MODEL-CARD-TEMPLATE.md |
> | 5 | Customer AI Documentation Pack | All documentation provided to customers at delivery | AI-DEPLOYMENT-CHECKLIST.md |
> | 6 | Developer Supplier Risk Register | Sub-supplier AI governance risks | AI-SUPPLIER-RISK-REGISTER.md |
> | 7 | AI Developer Contract Clauses | Standard governance clauses for customer contracts | AI-SUPPLIER-CONTRACT-CLAUSES.md |
>
> ---
>
> ## C.6 — Regulatory Considerations for AI Developers
>
> ### EU AI Act — Developer-Specific Obligations
>
> Under the EU AI Act, AI developers (called "providers" in the Act) have specific obligations for high-risk AI systems:
>
> | Obligation | Details |
> |-----------|---------|
> | Risk management system | Implement and maintain a risk management system throughout the lifecycle |
> | Data governance | Ensure training data is relevant, representative, and free from errors |
> | Technical documentation | Maintain comprehensive technical documentation before placing on market |
> | Logging and traceability | AI systems must enable monitoring through automatic logging |
> | Transparency to deployers | Provide sufficient information to deployers to use system responsibly |
> | Human oversight | Design systems to enable human oversight by deployers |
> | Accuracy and robustness | Achieve appropriate levels of accuracy and robustness |
> | Conformity assessment | Complete conformity assessment before placing high-risk AI on market |
> | CE marking | Affix CE marking for qualifying high-risk AI systems |
> | Post-market monitoring | Implement proactive post-market monitoring plan |
>
> Note: These  obligations apply when your AI system has an EU nexus. See `LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md`.
>
> ---
>
> *ISO/IEC 42001:2023 AI Governance Toolkit | Annex C Reference Guide — AI Developers | See root README.md for full index*
