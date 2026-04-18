# Changelog

All notable changes to the ISO/IEC 42001 AI Governance Toolkit are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to semantic-style versioning for its toolkit releases.

---

## [Unreleased]

### Added
- `LICENSE` — MIT License
- - `.gitignore` — standard Python, OS, and secrets exclusions
  - - `CONTRIBUTING.md` — contribution guidelines, ground rules, and PR process
    - - `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
      - - `CHANGELOG.md` — this file
       
        - ### Planned (next releases)
        - - Clause 4 templates: Scope Statement, Interested Parties Register, AI System Inventory
          - - Clause 5 templates: Roles & Responsibilities (RACI), Management Commitment Record
            - - Clause 6 templates: AI Objectives & KPI Tracker, Risk Treatment Plan, Change Planning, Opportunities Register
              - - Clause 7 templates: Competence Matrix, Training Plan & Log, Communication Plan, Document Control Procedure, Evidence Register
                - - Clause 8 procedures: Data Management, Model Development & Validation, Deployment/Release, Decommissioning, Human Oversight, Transparency & System Information
                  - - Clause 9 templates: KPI Monitoring Dashboard, Audit Program & Plan, Audit Checklist
                    - - Clause 10 templates: Nonconformity & Corrective Action Log, Continual Improvement Register
                      - - Annex coverage: Annex B implementation guidance, Annex C AI objectives, Annex D sector applications
                        - - Regulatory crosswalks: EU AI Act, NIST AI RMF, ISO 27001 / 27701 / 23894
                          - - Additional scripts: SoA completeness checker, risk register validator, evidence index generator, AI inventory validator
                           
                            - ---

                            ## [1.0.0] — 2026-04-10

                            ### Added
                            - Initial release of the ISO/IEC 42001:2023 AI Governance Toolkit
                            - - Root documents: `00-README.md`, `01-GAP-ASSESSMENT.md`, `02-IMPLEMENTATION-ROADMAP.md`, `10-ANNEX-A-CONTROLS.md`, `11-CONTROLS-MAPPING.md`
                              - - Clause 4 — Context of the Organisation: implementation guide
                                - - Clause 5 — Leadership: implementation guide and AIMS Policy template
                                  - - Clause 6 — Planning: implementation guide, AI Risk Register, Statement of Applicability
                                    - - Clause 7 — Support: implementation guide
                                      - - Clause 8 — Operation: implementation guide, AI Lifecycle Management procedure, AI Supplier Assessment, AI System Impact Assessment
                                        - - Clause 9 — Performance Evaluation: implementation guide, Internal Audit procedure, ISO 42001 Internal Audit Guide, Management Review template
                                          - - Clause 10 — Improvement: implementation guide, AI Incident Response procedure
                                            - - Scripts folder with `ai_assessment_checker.py` and sample inventory CSV
                                             
                                              - ---

                                              ## Versioning

                                              - MAJOR: breaking structural changes to the toolkit (e.g., file reorganisation, removal of templates)
                                              - - MINOR: new templates, procedures, or scripts
                                                - - PATCH: clarifications, typo fixes, small corrections
                                                  - 
