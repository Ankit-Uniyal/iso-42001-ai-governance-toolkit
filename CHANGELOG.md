# Changelog

All notable changes to the ISO/IEC 42001 AI Governance Toolkit are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project uses semantic-style versioning for its toolkit releases.

---

## [1.2.0] — 2026-08-02

### Fixed
- Rebuilt the Annex A audit checklists in `08-CLAUSE9-PERFORMANCE/ISO42001-INTERNAL-AUDIT-GUIDE.md` against the correct 38 controls. The guide previously claimed 39 controls with an incorrect per-domain breakdown and used control identifiers that do not exist in the standard.
- Corrected the Annex A control audit checklist in `08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROCEDURE.md`.
- Mapped `07-CLAUSE8-OPERATION/AI-LIFECYCLE-MANAGEMENT-PROCEDURE.md` onto the real Annex A.6 structure (A.6.1.2 to A.6.2.8, nine controls) and removed references to a non-existent Clause 8.5.
- Corrected control references in `07-CLAUSE8-OPERATION/OPERATIONAL-CONTROLS-REGISTER.md`, `07-CLAUSE8-OPERATION/AI-SUPPLIER-CONTRACT-CLAUSES.md`, `09-CLAUSE10-IMPROVEMENT/AI-INCIDENT-RESPONSE-PROCEDURE.md` and `02-IMPLEMENTATION-ROADMAP.md`.
- Removed invented Clause 8.5 and 8.6 sections from `01-GAP-ASSESSMENT.md`, added the missing 6.3 Planning of Changes section, and reconciled the scoring summary with the actual checklist (124 items).
- Corrected the Clause 8 subclause titles in `07-CLAUSE8-OPERATION/README.md` and the 10.1 / 10.2 order in `09-CLAUSE10-IMPROVEMENT/README.md`.
- Rewrote `00-README.md` for the current folder layout; all eleven of its relative links were broken.
- Fixed broken template paths and clause references in `14-WORKED-EXAMPLE/`.
- Repaired markdown corruption (runaway blockquotes, doubled bullets, doubled list numbers) in the Clause 4 and Clause 5 folder READMEs, `13-ANNEX-C-AI-DEVELOPERS.md`, `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and this changelog.
- Reframed `12-ANNEX-B-AI-CONCEPTS.md` and `13-ANNEX-C-AI-DEVELOPERS.md` as supplementary guides. Annex B of the standard is implementation guidance for the Annex A controls and Annex C is potential AI-related organisational objectives and risk sources.
- Repaired `.github/workflows/ai-assessment-check.yml`, which had invalid YAML indentation and had never run successfully.
- Fixed `15-SCRIPTS/ai_assessment_checker.py`: default paths pointed at a non-existent `scripts/` directory and the report directory was never created.
- Replaced the placeholder contact address in `SECURITY.md`.

- Restored the YAML front matter in `.github/ISSUE_TEMPLATE/bug-report.md`, which had the file path pasted onto the opening delimiter and so was not recognised as an issue template.
- Corrected the ISO reference example in `.github/ISSUE_TEMPLATE/feature-request.md` (Clause 8.4, not 8.2, for impact assessment; A.7.5 is Data provenance).
- Removed stray em dashes that sat in front of the H1 heading in five templates, so the titles render as headings again.
- Swapped the clause references in `09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md` (now 10.1) and `09-CLAUSE10-IMPROVEMENT/NCR-REGISTER.md` (now 10.2).
- Renumbered the Clause 8 audit checklist rows in `08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROCEDURE.md` from the non-existent 8.5.x to 8.1.x.
- Repointed `07-CLAUSE8-OPERATION/AI-SUPPLIER-RISK-REGISTER.md` at Clause 8.1 / A.10.3 and `14-WORKED-EXAMPLE/NFS-AI-SYSTEM-MODEL-CARD.md` at Clause 8.1 / A.6.2.3.
- Closed the code fences on the diagrams in `03-CLAUSE4-CONTEXT/AIMS-PROCESS-MAP.md`, `03-CLAUSE4-CONTEXT/README.md` and `14-WORKED-EXAMPLE/NFS-AIMS-SCOPE-STATEMENT.md`; runaway indentation had swallowed the rest of each document.
- Rebuilt the corrupted list numbering in `08-CLAUSE9-PERFORMANCE/INDIVIDUAL-AUDIT-PLAN-TEMPLATE.md`.
- Escaped a stray pipe that split the version control table in `10-ANNEX-A-CONTROLS.md`.
- Added hard line breaks to the document metadata block in 48 files so Document ID, Version, Owner and Review Cycle no longer run together into one paragraph.
- Described Annex C accurately in `05-CLAUSE6-PLANNING/AI-RISK-REGISTER.md` and matched four Annex A control titles in `15-SCRIPTS/aims_soa_tracker.py` to the wording of the standard.
### Added
- Missing folder README entries for `LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md`, `AI-ETHICS-FRAMEWORK.md` and `AI-SUPPLIER-CONTRACT-CLAUSES.md`.
- Documentation for `aims_soa_tracker.py` in `15-SCRIPTS/README.md`.

### Changed
- Refreshed `15-SCRIPTS/sample_ai_systems.csv` so the sample inventory still demonstrates compliant, due-soon, overdue and missing-date outcomes.
- Renamed the scripts folder from `12-SCRIPTS/` to `15-SCRIPTS/` so it no longer shares the `12-` prefix with `12-ANNEX-B-AI-CONCEPTS.md`. All references, including the GitHub Actions workflow and `.gitignore`, were updated with it.

---

## [1.1.0] — 2026-08-02

### Fixed
- Rebuilt `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md`, `10-ANNEX-A-CONTROLS.md`, `11-CONTROLS-MAPPING.md` and `15-SCRIPTS/aims_soa_tracker.py` against the correct ISO/IEC 42001:2023 Annex A structure of 38 controls across nine domains.

---

## [1.0.0] — 2026-04-10

### Added
- Initial release of the ISO/IEC 42001:2023 AI Governance Toolkit.
- Root documents: `00-README.md`, `01-GAP-ASSESSMENT.md`, `02-IMPLEMENTATION-ROADMAP.md`, `10-ANNEX-A-CONTROLS.md`, `11-CONTROLS-MAPPING.md`.
- Clause 4 — Context of the organisation: implementation guide and registers.
- Clause 5 — Leadership: implementation guide, AIMS policy template, ethics framework, RACI.
- Clause 6 — Planning: implementation guide, AI risk register, Statement of Applicability, objectives register.
- Clause 7 — Support: implementation guide, resource plan, competence matrix, training plan, document control.
- Clause 8 — Operation: implementation guide, lifecycle procedure, supplier assessment, impact assessment.
- Clause 9 — Performance evaluation: implementation guide, internal audit procedure and guide, management review template.
- Clause 10 — Improvement: implementation guide, NCR register, incident response procedure.
- Scripts folder with `ai_assessment_checker.py`, `aims_soa_tracker.py` and a sample inventory CSV.
- Worked example folder for the fictional Nexus Financial Services.
- Repository hygiene: `LICENSE`, `.gitignore`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue templates.

---

## Versioning

- **MAJOR** — breaking structural changes to the toolkit, such as file reorganisation or removal of templates.
- **MINOR** — new templates, procedures or scripts.
- **PATCH** — clarifications, typo fixes and small corrections.
