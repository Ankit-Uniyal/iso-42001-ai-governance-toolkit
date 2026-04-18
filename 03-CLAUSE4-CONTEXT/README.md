# Clause 4 — Context of the Organisation
## ISO/IEC 42001:2023 | Implementation Guide

> **Purpose:** Establish the foundation of your AIMS by understanding your organisation's environment, stakeholders, scope, and processes.
>
> ---
>
> ## 📁 Files in This Folder — Read in This Order
>
> | # | File | What It Is | ISO Ref |
> |---|------|-----------|---------|
> | 1 | [CONTEXT-REGISTER.md](CONTEXT-REGISTER.md) | Internal & external issues register (PESTLE) | 4.1 |
> | 2 | [AI-SYSTEMS-INVENTORY.md](AI-SYSTEMS-INVENTORY.md) | Register of all AI systems in scope | 4.1 |
> | 3 | [INTERESTED-PARTIES-REGISTER.md](INTERESTED-PARTIES-REGISTER.md) | Stakeholder needs & binding requirements | 4.2 |
> | 4 | [AIMS-SCOPE-STATEMENT.md](AIMS-SCOPE-STATEMENT.md) | Formal AIMS scope definition | 4.3 |
> | 5 | [AIMS-PROCESS-MAP.md](AIMS-PROCESS-MAP.md) | All AIMS processes, owners & connections | 4.4 |
>
> > **Start here → CONTEXT-REGISTER.md → AI-SYSTEMS-INVENTORY.md → INTERESTED-PARTIES-REGISTER.md → AIMS-SCOPE-STATEMENT.md → AIMS-PROCESS-MAP.md**
> >
> > ---
> >
> > ## 4.1 — Understanding the Organisation and Its Context
> >
> > ### What it requires
> > Identify all internal and external issues relevant to your purpose that affect your ability to achieve AIMS intended outcomes.
> >
> > ### Internal Issues to Identify
> > | Issue Area | Examples |
> > |-----------|----------|
> > | AI Strategy | Business goals for AI, board-level AI ambitions |
> > | Existing AI Systems | Current AI tools, models, products in use |
> > | Governance | Policies, ethics committees, decision-making structures |
> > | People and Culture | AI literacy, risk appetite, accountability culture |
> > | Technical Capability | Data quality, infrastructure, MLOps maturity |
> > | Ethics and Values | Fairness commitments, transparency policies |
> >
> > ### External Issues to Identify
> > | Issue Area | Examples |
> > |-----------|----------|
> > | Regulation | EU AI Act, GDPR, sector-specific AI rules |
> > | Standards | ISO 42001, ISO 27001, NIST AI RMF |
> > | Market | Customer AI expectations, competitor practices |
> > | Technology | Vendor dependencies, open-source risks |
> > | Society | Public trust in AI, bias concerns, media scrutiny |
> >
> > ### Implementation Steps
> > 1. Run a PESTLE analysis focused on AI — document each factor
> > 2. 2. Conduct an internal AI capability review — systems, people, processes
> >    3. 3. Populate the **Context Register** (template: `CONTEXT-REGISTER.md`)
> >       4. 4. Get sign-off from senior management
> >          5. 5. Schedule annual review and trigger-based updates
> >            
> >             6. ### Documents Required
> >             7. - Context of the Organisation Register (internal + external issues, rated by relevance)
> >                - - AI Systems Inventory (all AI systems: name, purpose, owner, risk level, status)
> >                  - - PESTLE Analysis Worksheet
> >                   
> >                    - ---
> >
> > ## 4.2 — Understanding Needs and Expectations of Interested Parties
> >
> > ### What it requires
> > Identify who has a stake in your AI systems, what they need, and which of those needs become binding requirements for your AIMS.
> >
> > ### Interested Parties Register Template
> > | Stakeholder | What They Need | Binding? | How Addressed |
> > |-------------|---------------|----------|---------------|
> > | Employees | Safe AI tools, transparency, no unjust automation | Yes — labour law | AI use policy, training |
> > | Customers / End Users | Fair decisions, explainability, data privacy | Yes — GDPR, contract | Privacy notices, explanations |
> > | Regulators | Compliance with AI laws, audit trails | Yes — legal | Compliance controls, records |
> > | AI Vendors / Suppliers | Clear requirements, IP protection | Yes — contract | Supplier agreements |
> > | Investors / Board | Risk management, reputational protection | Yes — fiduciary | AIMS reports, board updates |
> > | General Public / Society | Non-discriminatory AI, societal benefit | Ethical | Ethics framework, bias testing |
> > | Certification Body | Conformity with ISO 42001 | Yes — certification | Full AIMS implementation |
> >
> > ### Implementation Steps
> > 1. Brainstorm all stakeholder groups using the table above as a starting point
> > 2. 2. For each group, document: who they are, what they need, legal or contractual basis
> >    3. 3. Classify requirements as mandatory or best practice
> >       4. 4. Feed mandatory requirements into your AIMS controls and policies
> >          5. 5. Review when stakeholder landscape changes
> >            
> >             6. ### Documents Required
> >             7. - Interested Parties Register
> >                - - Legal and Regulatory Requirements Register
> >                 
> >                  - ---
> >
> > ## 4.3 — Determining the Scope of the AIMS
> >
> > ### What it requires
> > Define the exact boundaries of your AI Management System — what AI systems, organisational units, functions, and activities are included.
> >
> > ### Scope Statement Template
> > ```
> > AIMS Scope Statement — [Organisation Name]
> >
> > [Organisation Name] operates an AI Management System in accordance with ISO/IEC 42001:2023,
> > covering the design, development, deployment, monitoring, and decommissioning of AI systems
> > used in the following business functions:
> >   - [Function 1, e.g., Customer Service Automation]
> >   - [Function 2, e.g., Credit Risk Scoring]
> >   - [Function 3, e.g., HR Candidate Screening]
> >
> > Organisational units in scope: [list teams/departments]
> > Physical locations in scope: [offices, data centres, remote]
> > Exclusions: [List any AI systems NOT in scope and the reason why]
> >
> > Approved by: [Name, Title] | Date: [Date] | Version: 1.0
> > ```
> >
> > ### How to Determine Scope
> > 1. List every AI system in your AI Systems Inventory
> > 2. 2. Decide which systems are high enough risk to include
> >    3. 3. Consider starting with a pilot scope (1–2 AI systems) then expanding
> >       4. 4. Align scope with 4.1 context and 4.2 stakeholder findings
> >          5. 5. Document exclusions with clear justification
> >             6. 6. Get formal approval from top management
> >               
> >                7. ### Common Mistakes to Avoid
> >                8. - Scope too vague — be specific about which AI systems are included
> >                   - - Scope not approved — needs top management sign-off
> >                     - - Scope inconsistent with context — should flow logically from 4.1 and 4.2
> >                       - - Exclusions not justified — auditors will challenge them
> >                        
> >                         - ### Documents Required
> >                         - - AIMS Scope Statement (formal document, management approved)
> >                           - - Scope Exclusion Justification Log
> >                            
> >                             - ---
> >
> > ## 4.4 — The AI Management System
> >
> > ### What it requires
> > Establish, implement, maintain, and continually improve an AIMS — including all processes needed to meet the standard's requirements.
> >
> > ### What This Means in Practice
> > - Every process must have: owner, inputs, outputs, controls, and records
> > - - Processes must be documented at the level needed to ensure consistency
> >   - - Processes must connect to each other (risk feeds operations; audits feed improvement)
> >     - - The system must be reviewed and improved continuously, not set up once and forgotten
> >      
> >       - ### AIMS High-Level Process Flow
> >       - ```
> >         Clause 4 (Context) ──► Clause 5 (Leadership) ──► Clause 6 (Planning)
> >                                                                   │
> >                                                                   ▼
> >         Clause 10 (Improvement) ◄── Clause 9 (Performance) ◄── Clause 7 (Support)
> >                                                                   │
> >                                                                   ▼
> >                                                           Clause 8 (Operations)
> >         ```
> >
> > ### Documents Required
> > - AIMS Process Map (visual or table showing all processes, owners, and connections)
> > - - Master Document List (all policies, procedures, templates, records)
> >  
> >   - ---
> >
> > ## Clause 4 — Complete Documents Checklist
> >
> > | # | Document | ISO Ref | File |
> > |---|----------|---------|------|
> > | 1 | Context of the Organisation Register | 4.1 | [CONTEXT-REGISTER.md](CONTEXT-REGISTER.md) |
> > | 2 | AI Systems Inventory | 4.1 | [AI-SYSTEMS-INVENTORY.md](AI-SYSTEMS-INVENTORY.md) |
> > | 3 | PESTLE Analysis Worksheet | 4.1 | Embedded in CONTEXT-REGISTER.md |
> > | 4 | Interested Parties Register | 4.2 | [INTERESTED-PARTIES-REGISTER.md](INTERESTED-PARTIES-REGISTER.md) |
> > | 5 | Legal and Regulatory Requirements Register | 4.2 | Embedded in INTERESTED-PARTIES-REGISTER.md |
> > | 6 | AIMS Scope Statement | 4.3 | [AIMS-SCOPE-STATEMENT.md](AIMS-SCOPE-STATEMENT.md) |
> > | 7 | Scope Exclusion Justification Log | 4.3 | Embedded in AIMS-SCOPE-STATEMENT.md |
> > | 8 | AIMS Process Map | 4.4 | [AIMS-PROCESS-MAP.md](AIMS-PROCESS-MAP.md) |
> > | 9 | Master Document List | 4.4 | See `06-CLAUSE7-SUPPORT/MASTER-DOCUMENT-LIST.md` |
> >
> > ---
> >
> > ## What Auditors Check in Clause 4
> > - Is the context analysis documented and up to date?
> > - - Are interested parties listed with specific, traceable requirements?
> >   - - Is the scope precise — naming actual AI systems and functions?
> >     - - Is there a management-approved scope document with a signature and date?
> >       - - Does the AIMS cover all in-scope systems and activities?
> >         - - Is there evidence the organisation reviews context periodically?
> >          
> >           - ---
> >
> > *ISO/IEC 42001:2023 AI Governance Toolkit | Clause 4 of 10 | See root [README.md](../README.md) for full index*
