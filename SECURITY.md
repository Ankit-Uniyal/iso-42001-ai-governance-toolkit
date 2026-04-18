# Security Policy

## Supported Versions

This is an open-source governance toolkit repository containing documentation templates only. There is no executable software with version-based security support.

| Resource Type | Security Support |
|--------------|-----------------|
| Markdown templates and guides | Maintained — issues welcomed |
| Python automation scripts (12-SCRIPTS/) | Actively maintained |

---

## Reporting a Vulnerability

If you discover a security issue in this repository — for example, a script that could be misused, a template containing incorrect security guidance, or any other concern — please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

### How to Report

Please report security vulnerabilities by emailing: **[your contact email]**

Include the following in your report:
- Description of the potential vulnerability
- File(s) affected
- Potential impact
- Suggested fix (if you have one)

### Response Timeline

- We will acknowledge receipt of your report within 5 business days
- We will assess and respond with our findings within 14 business days
- We will credit responsible disclosures in the CHANGELOG if you wish

---

## Security Considerations for Users of This Toolkit

If you are using this toolkit to implement an ISO/IEC 42001:2023 AIMS, note the following:

**Template Content:** All templates are examples only and must be reviewed by qualified AI governance and legal professionals before use in your organisation.

**Sensitive Data:** Do not store actual risk assessments, incident records, or confidential organisational information in public forks of this repository. All real AIMS documentation should be stored in your organisation's secure, access-controlled systems.

**Scripts:** The Python scripts in `12-SCRIPTS/` read CSV files and generate reports. Review all scripts before running them in your environment. No network calls are made and no data is transmitted externally.

**Credentials:** Never store API keys, passwords, or credentials in AIMS templates or documentation files.

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead*
