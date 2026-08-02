# ISO 42001 INTERNAL AUDIT GUIDE
## The Complete, Step-by-Step Guide to Auditing an AI Management System
### So clear and simple, anyone can follow it — from first-timers to experienced auditors

---

> **What is this guide?**
> This guide walks you through everything you need to know and do to conduct a full internal audit of an organization's ISO/IEC 42001:2023 AI Management System (AIMS). It tells you exactly what to look at, what to ask, what to collect as evidence, and how to write up your findings. You do not need to be an AI expert. You need curiosity, a checklist, and this guide.

---

## PART 1 — UNDERSTANDING THE BASICS
### (Read this first. It takes 5 minutes and makes everything else make sense.)

---

### 1.1 — What Is ISO 42001?

ISO/IEC 42001:2023 is an international standard that tells organizations **how to responsibly manage AI systems**. Think of it like a rulebook for organizations that build or use AI. The rulebook covers things like:

- Making sure AI is fair and doesn't discriminate against people
- Making sure humans can always step in and override AI decisions
- Making sure the organization knows what AI systems it has and what they do
- Making sure AI data is handled safely and legally
- Making sure AI suppliers are trustworthy
- Making sure AI mistakes are caught and fixed quickly

When an organization says "we are ISO 42001 certified," it means an independent checker (a certification auditor) looked at their AI governance and agreed it meets the standard. But **before** the external checker comes, the organization must check itself. That self-check is called an **internal audit** — and that is what this guide is for.

---

### 1.2 — What Is an Internal Audit?

An **internal audit** is like a health check-up for the organization's AI governance. A doctor doesn't just ask "do you feel okay?" — they check your blood pressure, look at your test results, ask you questions, and compare everything against what a healthy person looks like. An internal audit works the same way:

1. **Look at documents** — Does the organization have the right policies and records?
2. **Talk to people** — Do employees actually know and follow those policies?
3. **Test the evidence** — Are the records real and up to date?
4. **Compare to the standard** — Does everything meet ISO 42001's requirements?
5. **Report findings** — Tell the organization what's working and what needs to be fixed.

---

### 1.3 — What Is the Auditor's Job?

As an auditor, your job is to be **objective, curious, and fair**. You are not there to catch people out or make anyone feel bad. You are there to find the truth about how the organization manages its AI systems, so it can improve.

**Golden rules for auditors:**
- Only report what you can prove — if you can't show evidence, it's not a finding
- Be curious — always ask "can you show me that?"
- Don't accept descriptions of what the process should be — ask for proof it actually happens
- Treat everyone with respect — you get better information that way
- Stay neutral — your job is to find facts, not to judge people

---

### 1.4 — The Structure of ISO 42001 (What You Are Auditing)

ISO 42001 has two main parts:

**Main Clauses (Clauses 4–10):** These are the core management system requirements — things like leadership commitment, planning, support, operation, evaluation, and improvement. Every organization must implement all of these.

**Annex A (Controls):** These are 38 specific controls organized into 9 domains. They cover everything from AI policies to data management to supplier oversight. Most organizations implement all 38, but they can document justified exclusions.

| Domain | What It Covers | Number of Controls |
|---|---|---|
| A.2 — Policies Related to AI | AI policy, alignment with other policies, policy review | 3 |
| A.3 — Internal Organisation | Roles, responsibilities, reporting of concerns | 2 |
| A.4 — Resources for AI Systems | Resource documentation, data, tooling, compute, people | 5 |
| A.5 — Assessing Impacts | Impact assessment process, documentation, individual and societal impacts | 4 |
| A.6 — AI System Life Cycle | Design, build, verify, deploy, operate, document, log | 9 |
| A.7 — Data for AI Systems | Development data, acquisition, quality, provenance, preparation | 5 |
| A.8 — Information for Interested Parties | User documentation, external reporting, incidents, disclosure | 4 |
| A.9 — Use of AI Systems | Responsible use processes, objectives, intended use | 3 |
| A.10 — Third-Party & Customer Relationships | Allocating responsibilities, suppliers, customers | 3 |

---

## PART 2 — PREPARING FOR THE AUDIT
### (Do all of this BEFORE the audit starts)

---

### 2.1 — Step 1: Understand What You Are Auditing

Before you audit anything, answer these questions:

**About the organization's AI:**
- [ ] What AI systems does the organization have? (Get a list — this is the AI System Inventory)
- [ ] What do those AI systems do? (e.g., credit scoring, hiring support, customer chatbot)
- [ ] Who are the people affected by those AI systems? (employees, customers, the public)
- [ ] What regulations apply? (EU AI Act? GDPR? Sector regulations?)

**About the AIMS scope:**
- [ ] What is officially in scope for the AIMS? (Check the Scope Statement document)
- [ ] Are there AI systems that should be in scope but are not? (A risk if scope is too narrow)

**Simple question to ask yourself:** *"If this AI system made a mistake that hurt someone, would I be surprised that it wasn't covered by the AIMS?"* If yes — it probably should be in scope.

---

### 2.2 — Step 2: Get the Audit Programme

Your organization should have an **Audit Programme** — a plan that says which parts of the AIMS will be audited, when, and by whom. Check:

- [ ] Does an Audit Programme exist?
- [ ] Is this audit on the programme?
- [ ] What is the scope of this specific audit? (All 38 controls? Just one domain?)
- [ ] How much time is allocated?

If there is no Audit Programme, that itself is a finding — ISO 42001 Clause 9.2 requires one.

---

### 2.3 — Step 3: Collect Documents in Advance

Before the audit, ask the organization to give you these documents. Read them before you arrive so you know what to expect:

| # | Document to Request | Why You Need It |
|---|---|---|
| 1 | AIMS Scope Statement | Tells you what's in and out of scope |
| 2 | AI Policy (top-level) | The foundational governance document |
| 3 | Statement of Applicability (SoA) | Shows which of the 38 controls apply and why |
| 4 | AI System Inventory / Register | List of all AI systems |
| 5 | AI Risk Register | Identified AI risks and their treatment |
| 6 | Previous audit reports | What was found before — has it been fixed? |
| 7 | Corrective action records | Evidence previous findings were resolved |
| 8 | Management review records | Evidence leadership is engaged |
| 9 | Training records | Evidence staff are trained |
| 10 | Organizational chart | Who is responsible for what |

**Tip:** If the organization can't provide a document, note it — you may have found a gap before the audit even starts.

---

### 2.4 — Step 4: Build Your Audit Plan

Create a simple Audit Plan document before you start. It should include:

```
AUDIT PLAN
-----------
Audit title:     ISO 42001 Internal Audit — [Year/Period]
Auditor(s):      [Your name(s)]
Auditee:         [Organization/department name]
Audit scope:     [Which clauses and Annex A domains are covered]
Audit dates:     [Date(s)]
Objectives:      Verify conformance with ISO 42001 requirements
                 Identify opportunities for improvement

Schedule:
  Day 1 Morning:   Opening meeting + document review
  Day 1 Afternoon: Interviews — AI Governance team
  Day 2 Morning:   Interviews — Technical team + Operations
  Day 2 Afternoon: Evidence testing + team debrief
  Day 3:           Report writing + closing meeting
```

---

### 2.5 — Step 5: Prepare Your Checklists

Use the checklists in Part 4 of this guide. Print them out or have them on a tablet. For each checklist item, you will mark:

- ✅ **Conforming** — requirement is met with evidence
- ❌ **Non-conforming** — requirement is not met (this is a finding)
- ⚠️ **Observation** — it's met but could be improved
- ➡️ **Not applicable** — doesn't apply (but document why)

---

## PART 3 — CONDUCTING THE AUDIT
### (The actual audit — follow these steps in order)

---

### 3.1 — PHASE 1: Opening Meeting

**Duration:** 30–45 minutes  
**Who attends:** You (auditor) + AI Governance Lead + any key managers

The opening meeting is your introduction. Keep it friendly and professional.

**What to say and do:**

1. **Introduce yourself** — "I'm [name], conducting the internal audit of the AIMS."

2. **Explain the purpose** — "The goal of this audit is to check whether the AIMS meets ISO 42001 requirements and to identify areas for improvement. This is not about blame — it's about finding facts."

3. **Explain the process** — "Over the next [X days], I will review documents, interview staff, and test evidence. At the end, I will share findings in a report."

4. **Confirm the scope** — "We agreed the scope is [list]. Is there anything that has changed?"

5. **Agree logistics** — Who is the main contact? Where will interviews take place? Who needs to be available when?

6. **Set the ground rules** — "Everything I find will be based on evidence. I will share findings before I finalize anything, so you can correct any misunderstandings."

7. **Ask for any updates** — "Is there anything that has changed recently in the AIMS that I should know about before I start?"

**Document:** Take notes of what was discussed. Record attendance.

---

### 3.2 — PHASE 2: Document Review

**Duration:** Half a day to a full day  
**Where:** Your desk / meeting room with the documents

Document review is where you read all the documents and ask: *"Does this document meet the requirement, or does it fall short?"*

**For each document, ask these five questions:**

1. **Does it exist?** If the standard requires a document and there isn't one — that's a gap.
2. **Is it approved?** The right person must have signed or approved it.
3. **Is it current?** When was it last reviewed? Is it out of date?
4. **Does it say the right things?** Does the content actually meet the requirement?
5. **Is it being used?** A policy no one follows is worse than no policy — it creates false confidence.

**Document Review Checklist:**

| Document | Exists? | Approved? | Current? | Content OK? | Notes |
|---|---|---|---|---|---|
| AI Policy | ☐ | ☐ | ☐ | ☐ | |
| AI-Specific Sub-Policies | ☐ | ☐ | ☐ | ☐ | |
| AIMS Scope Statement | ☐ | ☐ | ☐ | ☐ | |
| Statement of Applicability | ☐ | ☐ | ☐ | ☐ | |
| AI System Inventory | ☐ | ☐ | ☐ | ☐ | |
| AI Risk Register | ☐ | ☐ | ☐ | ☐ | |
| AI Governance RACI | ☐ | ☐ | ☐ | ☐ | |
| AI Competency Framework | ☐ | ☐ | ☐ | ☐ | |
| Training Records | ☐ | ☐ | ☐ | ☐ | |
| ASIA Template + Completed ASIAs | ☐ | ☐ | ☐ | ☐ | |
| Model Cards | ☐ | ☐ | ☐ | ☐ | |
| Bias Evaluation Reports | ☐ | ☐ | ☐ | ☐ | |
| Adversarial Test Results | ☐ | ☐ | ☐ | ☐ | |
| Deployment Authorization Records | ☐ | ☐ | ☐ | ☐ | |
| Override / Oversight Logs | ☐ | ☐ | ☐ | ☐ | |
| Monitoring Dashboards / Alert Logs | ☐ | ☐ | ☐ | ☐ | |
| Third-Party AI Inventory + Assessments | ☐ | ☐ | ☐ | ☐ | |
| Supplier Contracts (AI clauses) | ☐ | ☐ | ☐ | ☐ | |
| Incident Log | ☐ | ☐ | ☐ | ☐ | |
| Management Review Records | ☐ | ☐ | ☐ | ☐ | |

**Red flags to watch for during document review:**
- Documents dated before a major AI deployment but impact assessment dated after — impact assessment may have been written retrospectively
- All risk ratings in the risk register are "low" — may not be a genuine assessment
- Policy says "reviewed annually" but last review was 3 years ago
- Training records show 100% completion but no evidence of effectiveness testing
- Model cards exist but the "bias evaluation" section is blank or says "N/A" for all systems

---

### 3.3 — PHASE 3: Interviews

**Duration:** 30–60 minutes per interview  
**Who to interview:** See the list below

Interviews are where the audit comes to life. Documents tell you what the organization says it does. People tell you what actually happens. The gap between these two is where your most important findings live.

---

#### 3.3.1 — Interview Technique: The STAR-E Method

For every important topic, use the **STAR-E** method:

- **S — Show me:** "Can you show me where that document is / how that process works?"
- **T — Tell me:** "Tell me about the last time you did [process X]. Walk me through it."
- **A — Ask for evidence:** "Can you give me a copy of that record?"
- **R — Reality check:** Compare what they say to what the document says.
- **E — Explore the gap:** If the document and reality differ, explore why.

**The magic question: "Can you show me the last time you did that?"**
This single question reveals whether a process actually happens or only exists on paper.

---

#### 3.3.2 — Who to Interview and What to Ask

**INTERVIEW 1: AI Governance Lead / Chief AI Officer**
*(The person responsible for the whole AIMS)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "Walk me through the AI Policy — what does it commit the organization to?" | Can summarize key commitments without reading the document |
| 2 | "Which AI systems have you deployed in the last 12 months? For each one — was an impact assessment done?" | Can name systems and confirm ASIAs completed |
| 3 | "When did you last update the AI Risk Register? What triggered the update?" | Recent update, triggered by a change or review |
| 4 | "Has anyone ever tried to deploy an AI system and been told they couldn't because governance wasn't complete?" | Shows governance has real authority, not just advisory |
| 5 | "What was the most significant AI governance issue in the last 12 months? How was it handled?" | Demonstrates active governance, not just paperwork |
| 6 | "Who has the authority to stop an AI deployment on governance grounds? Has that ever happened?" | Clear answer, ideally with an example |
| 7 | "Tell me about your management review process — who attends, what is discussed, what decisions are made?" | Regular, attended by leadership, produces action items |
| 8 | "What new AI regulations have emerged in the last 6 months that affect your AIMS?" | Shows active regulatory monitoring |

---

**INTERVIEW 2: Technical Lead / ML Engineer**
*(The person who builds the AI systems)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "Walk me through how you develop a new AI model — from data to production." | Structured process with governance checkpoints |
| 2 | "Tell me about the last model you trained. What bias evaluation did you do? Show me the results." | Can produce bias evaluation report with disaggregated metrics |
| 3 | "If I asked you to use a new pre-trained model from Hugging Face right now, what would you have to do first?" | Knows the approval process — doesn't say "just download it" |
| 4 | "How do you version control your training data and model weights?" | Uses a versioning system, can trace model to training run |
| 5 | "Tell me about adversarial testing — what have you tested this system against?" | Can describe specific tests (prompt injection, adversarial examples) |
| 6 | "If your model starts drifting in production, how would you know? What would you do?" | Knows the monitoring setup, knows the retraining process |
| 7 | "Show me the model card for [specific AI system]." | Can pull up a completed model card with real data |
| 8 | "Who has access to your training data? Can anyone on the team access all of it?" | Knows access controls, applies least privilege |

---

**INTERVIEW 3: Operations / Business User of AI**
*(Someone who uses the AI system in their daily work)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "What AI systems do you use in your work? What do they do?" | Can describe clearly |
| 2 | "When an AI system gives you a recommendation, do you always follow it, or do you ever override it? Tell me about a time you overrode it." | Demonstrates real human oversight, not rubber-stamping |
| 3 | "Are there things you are NOT allowed to put into AI systems? What are they?" | Knows the acceptable use policy and data restrictions |
| 4 | "What would you do if you thought an AI system was giving wrong or unfair outputs?" | Has a clear escalation path |
| 5 | "How do you explain an AI decision to a customer if they ask why?" | Has an explanation mechanism they can use |
| 6 | "Have you been trained on AI governance or acceptable use policies? When? What did you learn?" | Can recall the training and its content |
| 7 | "Can you show me how you would override an AI recommendation right now?" | Can actually demonstrate it — not just describe it |

---

**INTERVIEW 4: HR / Learning & Development**
*(The people responsible for AI training and competencies)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "How do you identify what AI competencies staff need?" | Has a competency framework |
| 2 | "How do you know if training was effective — not just completed?" | Tests, assessments, or observed behavior — not just completion |
| 3 | "Has the AI training programme been updated in the last 12 months? What changed?" | Updated to reflect new regulations or technologies |
| 4 | "What happens if a staff member fails the AI governance training assessment?" | Has a process for retesting or remediation |
| 5 | "Who is responsible for AI governance training for new starters?" | Clear ownership, training in onboarding |

---

**INTERVIEW 5: Procurement / Legal**
*(The people who manage AI supplier contracts)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "When a business unit wants to use a new SaaS tool with AI features, what happens?" | Formal assessment process triggered |
| 2 | "Do your standard supplier contracts include AI governance clauses? Show me an example." | Can produce a contract with AI-specific terms |
| 3 | "Do you have Data Processing Agreements with all cloud AI providers? Can you show me the DPA for [specific provider]?" | Can produce the DPA promptly |
| 4 | "If a supplier's AI model exhibited bias that caused harm to our customers, what contractual recourse do we have?" | Can point to specific contract clauses |
| 5 | "Have you exercised audit rights over any AI supplier? What did you find?" | Shows active supplier management |

---

**INTERVIEW 6: CISO / Data Protection Officer**
*(Security and privacy for AI)*

| # | Question | What a good answer looks like |
|---|---|---|
| 1 | "Have you conducted DPIAs for all AI systems that process personal data? Show me one." | Can produce a completed DPIA |
| 2 | "What is the lawful basis for using personal data to train your AI models?" | Clear lawful basis, confirmed it covers training use |
| 3 | "If a customer submitted a data erasure request and their data was in an AI training set, what would happen?" | Has a defined process |
| 4 | "Who can access your AI training datasets? How is that access controlled and logged?" | Access control matrix, access logs retained |
| 5 | "Have you tested your AI systems for prompt injection or adversarial inputs?" | Can describe testing conducted |

---

### 3.4 — PHASE 4: Evidence Testing

This is the most important part of the audit. You are testing whether what you were told and shown in documents is actually real and actually happening.

**The core principle: Sample, don't assume.**

You cannot check everything. So you pick samples and test them. If 3 out of 3 samples are fine, you can have reasonable confidence. If 1 out of 3 is wrong, dig deeper.

---

#### 3.4.1 — Evidence Testing Checklist

**TEST 1: AI System Inventory Completeness**

Goal: Verify that all AI systems are on the inventory.

How to test:
1. Get the AI System Inventory.
2. Ask a cross-functional group (IT, business units, procurement) to name the AI tools their teams use.
3. Check each tool mentioned against the inventory.
4. Any tool not on the inventory = potential gap.

Result boxes:
- [ ] All mentioned AI systems are on the inventory (PASS)
- [ ] [Number] AI systems mentioned but not on inventory (FINDING)

---

**TEST 2: Impact Assessment Completeness and Timing**

Goal: Verify that ASIAs were done BEFORE deployment.

How to test:
1. Select 3 AI systems from the inventory.
2. For each: find the ASIA document (should be in the ASIA Register).
3. Check the ASIA date vs. the deployment date.
4. If ASIA date is AFTER deployment date — that's a non-conformity.
5. Read one ASIA in detail — is it substantive or just box-ticking?

Result boxes:
- [ ] ASIA exists for each sampled system (PASS/FINDING per system)
- [ ] ASIA date is BEFORE deployment date (PASS/FINDING per system)
- [ ] ASIA content is substantive, not just "low/low/low" (PASS/OBSERVATION)

---

**TEST 3: Bias Evaluation Quality**

Goal: Verify bias evaluation is real and disaggregated.

How to test:
1. Select 2 AI systems that make decisions affecting people.
2. Request the bias evaluation report for each.
3. Check: Does it show results broken down by demographic group (e.g., by gender, age, ethnicity)?
4. If it only shows an overall accuracy number — not disaggregated — that's a gap.
5. Check: Are fairness thresholds defined? Were they met?

Result boxes:
- [ ] Bias evaluation report exists (PASS/FINDING)
- [ ] Results are disaggregated by protected characteristic (PASS/FINDING)
- [ ] Thresholds defined and results within threshold (PASS/FINDING)

---

**TEST 4: Deployment Authorization Trail**

Goal: Verify no AI system was deployed without proper authorization.

How to test:
1. Select 3 recent AI deployments from the deployment log.
2. For each: find the deployment authorization record.
3. Check: Was the authorizer different from the developer? (Segregation of duties)
4. Check: Did authorization occur BEFORE deployment?
5. Check: Were all required governance steps completed before authorization?

Result boxes:
- [ ] Authorization record exists for each deployment (PASS/FINDING per system)
- [ ] Authorizer ≠ developer (PASS/FINDING)
- [ ] Authorization before deployment date (PASS/FINDING)

---

**TEST 5: Human Oversight Reality Check**

Goal: Verify human oversight is real, not rubber-stamping.

How to test:
1. Select 1 high-stakes AI system (e.g., one used in decisions about people).
2. Request the override log for the last 3 months.
3. Calculate the override rate (overrides ÷ total AI decisions).
4. If the override rate is 0% over thousands of decisions — that's suspicious. Is the AI really that perfect? Or are people not actually reviewing?
5. Ask an overseer to demonstrate the override process RIGHT NOW — can they do it?

Result boxes:
- [ ] Override log exists (PASS/FINDING)
- [ ] Override rate is plausible (PASS/OBSERVATION if too low)
- [ ] Overseer can demonstrate override process (PASS/FINDING)

---

**TEST 6: Training Record and Effectiveness**

Goal: Verify staff are trained AND that training worked.

How to test:
1. Pick 5 staff members from different departments.
2. Check their training records — have they completed AI governance training?
3. Ask each one a simple test question: "Can you put customer personal data into ChatGPT for work tasks?" (They should know the policy — probably no, or only under specific conditions.)
4. The gap between training records and actual knowledge is your finding.

Result boxes:
- [ ] Training records exist for sampled staff (PASS/FINDING)
- [ ] Staff can correctly answer policy questions (PASS/FINDING if knowledge gaps)

---

**TEST 7: Third-Party AI Inventory and Assessment**

Goal: Verify all third-party AI tools are inventoried and assessed.

How to test:
1. Ask 3 different business unit managers to list the AI tools their team uses (including SaaS with AI features).
2. Check each tool against the Third-Party AI Inventory.
3. For each tool on the inventory, check: is there an assessment record?
4. Check: did the assessment happen BEFORE adoption?
5. Check: is there a DPA for any that process personal data?

Result boxes:
- [ ] All mentioned third-party AI tools are on the inventory (PASS/FINDING)
- [ ] Assessment records exist for inventoried tools (PASS/FINDING)
- [ ] Assessments predate adoption (PASS/FINDING)
- [ ] DPAs exist for personal data processors (PASS/FINDING)

---

**TEST 8: Monitoring and Alerting**

Goal: Verify AI monitoring is real and being acted on.

How to test:
1. Select 1 high-risk AI system in production.
2. Ask to see the monitoring dashboard LIVE.
3. Ask: "What alerts have fired in the last 3 months? Show me the alert log."
4. For each alert in the log: was there a documented response?
5. Ask: "What would happen if this AI system suddenly started producing very different outputs? How would you know?"

Result boxes:
- [ ] Monitoring dashboard is live and current (PASS/FINDING)
- [ ] Alert log exists with responses documented (PASS/FINDING)
- [ ] Staff can articulate the response process (PASS/FINDING)

---

**TEST 9: Corrective Actions from Previous Audit**

Goal: Verify previous findings were actually fixed.

How to test:
1. Get the previous internal audit report.
2. List all findings (non-conformities and major observations).
3. For each finding: find the corrective action record.
4. Check: was a root cause identified?
5. Check: was a fix implemented? Can you verify it's actually been fixed?
6. Check: was effectiveness verified — i.e., did someone check the fix worked?

Result boxes:
- [ ] Corrective action record exists for each previous finding (PASS/FINDING)
- [ ] Root cause identified (PASS/OBSERVATION)
- [ ] Fix verified as effective (PASS/FINDING)

---

**TEST 10: Management Review**

Goal: Verify leadership is genuinely engaged in the AIMS.

How to test:
1. Request the management review records for the last 12 months.
2. Check: Who attended? (Must include top management — not just middle management)
3. Check: What inputs were considered? (ISO 42001 Clause 9.3 lists required inputs: audit results, incidents, risk, opportunities, regulatory changes, etc.)
4. Check: What decisions and actions came out of the review?
5. A management review that produced no action items is probably not a genuine review.

Result boxes:
- [ ] Management review records exist for last 12 months (PASS/FINDING)
- [ ] Top management attended (PASS/FINDING)
- [ ] Required inputs are covered in minutes (PASS/FINDING)
- [ ] Action items produced with owners and deadlines (PASS/OBSERVATION if none)

---

### 3.5 — PHASE 5: Closing Meeting

**Duration:** 45–60 minutes  
**Who attends:** You (auditor) + AI Governance Lead + relevant managers + top management representative

The closing meeting is where you share what you found. The key rule: **no surprises**. Every finding should have been informally previewed with the relevant manager before the closing meeting.

**Structure of the closing meeting:**

1. **Thank everyone** for their time and cooperation.

2. **Confirm the scope** — remind everyone what was audited and what was not.

3. **Share the summary** — overall impression: "The AIMS is broadly established / has significant gaps / shows good progress since the last audit."

4. **Present each finding** — for each finding:
   - State the requirement (what ISO 42001 says should exist)
   - State the evidence (or lack of it) that you found
   - State the classification (Major Non-Conformity, Minor Non-Conformity, or Observation)
   - Do NOT propose the solution — that's the organization's job

5. **Allow questions** — the auditee may challenge a finding. If they can provide evidence you missed, update your finding. If they just disagree, note it and stand your ground.

6. **Explain next steps** — Corrective action plan required by [date]. Follow-up audit scheduled for [date].

7. **Close the meeting** — thank everyone again.

---

## PART 4 — DOMAIN-BY-DOMAIN AUDIT CHECKLISTS
### (Use these during document review, interviews, and evidence testing)

---

These checklists cover all **38 Annex A controls of ISO/IEC 42001:2023**, in the order they appear in the standard. Control titles match the standard exactly, so a finding raised here maps straight onto the Statement of Applicability.

---

### CHECKLIST A.2 — POLICIES RELATED TO AI

**A.2.2 — AI Policy**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI Policy document exists | | |
| 2 | Approved/signed by top management | | |
| 3 | Dated within the last 12 months (or annual review evidenced) | | |
| 4 | Includes commitment to responsible AI | | |
| 5 | Includes scope statement covering all AIMS AI systems | | |
| 6 | References applicable regulations | | |
| 7 | Published and accessible to all staff | | |
| 8 | Evidence of communication to staff | | |
| 9 | Addresses generative AI and large language models | | |

**A.2.3 — Alignment with Other Organizational Policies**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Related policies identified (security, privacy, data, HR, procurement, quality) | | |
| 2 | AI Policy cross-references those policies rather than contradicting them | | |
| 3 | Conflicts between the AI Policy and other policies have been reconciled and recorded | | |
| 4 | Supporting AI policies exist where needed (acceptable use, prohibited use, human oversight) | | |
| 5 | Prohibited use list covers EU AI Act prohibited practices | | |
| 6 | All AI-related policies have named owners | | |
| 7 | Training on the policy set completed and recorded | | |

**A.2.4 — Review of the AI Policy**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Defined review interval for the AI Policy | | |
| 2 | Review triggers defined (regulatory change, incident, scope change, new AI system) | | |
| 3 | Evidence of at least one completed review | | |
| 4 | Regulatory monitoring feeds the review (watch list, alerts, consultation responses) | | |
| 5 | Review outcomes recorded, including a decision when no change is made | | |
| 6 | Policy version history maintained | | |

---

### CHECKLIST A.3 — INTERNAL ORGANIZATION

**A.3.2 — AI Roles and Responsibilities**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI Governance RACI Matrix exists | | |
| 2 | RACI covers all key AI governance activities (not just top-level) | | |
| 3 | All cells in RACI have named individuals (not just job titles) | | |
| 4 | AI System Owner assigned for EVERY AI system in inventory | | |
| 5 | Role profiles define competency requirements | | |
| 6 | Role assignments formally acknowledged by individuals | | |
| 7 | Conflicting duties separated: developer is not the deployment approver | | |
| 8 | Model trainer is not the bias evaluation approver | | |
| 9 | Where duties cannot be separated, compensating controls are documented | | |
| 10 | AI governance responsibilities are reflected in project governance gates | | |

**A.3.3 — Reporting of Concerns**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | A defined channel exists for raising concerns about AI systems | | |
| 2 | The channel is available to staff, contractors and third parties | | |
| 3 | Staff can describe how to raise a concern (test in interviews) | | |
| 4 | Confidentiality and non-retaliation are stated and understood | | |
| 5 | Concerns log maintained with outcomes and timescales | | |
| 6 | Concerns are triaged into the risk register or incident process where relevant | | |

---

### CHECKLIST A.4 — RESOURCES FOR AI SYSTEMS

**A.4.2 — Resource Documentation**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Resources needed across the AI life cycle are identified and documented | | |
| 2 | Documentation distinguishes data, tooling, compute and people | | |
| 3 | Resources are mapped to individual AI systems | | |
| 4 | Documentation is current — updated after the last significant change | | |

**A.4.3 — Data Resources**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Data resources used by each AI system are documented | | |
| 2 | Source, owner and permitted use recorded for each dataset | | |
| 3 | Training data encrypted at rest | | |
| 4 | Access to training data follows least privilege | | |
| 5 | Access logs retained and reviewed for AI training data | | |

**A.4.4 — Tooling Resources**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Approved AI tools and libraries list exists | | |
| 2 | Pre-trained model registry exists | | |
| 3 | Licence reviewed for each pre-trained model (AI training use confirmed) | | |
| 4 | Bias assessment conducted for each adopted pre-trained model | | |
| 5 | Approval record exists before any pre-trained model is used | | |
| 6 | No unapproved tools found in codebase (spot check) | | |

**A.4.5 — System and Computing Resources**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI infrastructure inventory exists (compute, storage, model registry) | | |
| 2 | Access controls applied to AI infrastructure | | |
| 3 | Model weights protected against tampering | | |
| 4 | Patching and vulnerability management applied to AI infrastructure | | |
| 5 | AI infrastructure included in the disaster recovery plan | | |
| 6 | Capacity is sufficient for the intended workload | | |

**A.4.6 — Human Resources**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI competency framework exists by role | | |
| 2 | Covers technical roles AND business/operational roles | | |
| 3 | Competency gap assessments conducted (within last 12 months) | | |
| 4 | Training programme designed to close identified gaps | | |
| 5 | Training completion records for all relevant staff | | |
| 6 | Training effectiveness evaluated (not just completion) | | |
| 7 | Training content updated for recent regulatory changes | | |

---

### CHECKLIST A.5 — ASSESSING IMPACTS OF AI SYSTEMS

**A.5.2 — AI System Impact Assessment Process**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | A documented AIA/ASIA process exists | | |
| 2 | Template covers individual, group and societal impacts | | |
| 3 | Triggers defined (new system, significant change, periodic review) | | |
| 4 | Roles for preparing, reviewing and approving assessments are defined | | |
| 5 | Process integrates with the AI risk assessment process | | |

**A.5.3 — Documentation of AI System Impact Assessments**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Impact assessment register exists | | |
| 2 | Every in-scope AI system has a completed assessment | | |
| 3 | Assessments are dated BEFORE the deployment date | | |
| 4 | Assessments are substantive — not all risks rated "low" | | |
| 5 | Results are retained per the records retention schedule | | |
| 6 | Results are available to the people who need them | | |
| 7 | Periodic reviews of assessments for operational systems evidenced | | |

**A.5.4 — Assessing AI System Impact on Individuals or Groups of Individuals**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Potential harms to individuals identified and rated for severity | | |
| 2 | Subgroup analysis performed for identifiable groups | | |
| 3 | Fundamental rights impact considered for high-risk AI | | |
| 4 | Findings have documented treatment decisions | | |
| 5 | Significant findings appear in the AI risk register | | |
| 6 | Deployment conditions arising from findings are enforced in production | | |
| 7 | Residual risk formally accepted by an authorised person | | |

**A.5.5 — Assessing Societal Impacts of AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Template includes a societal and environmental impact section | | |
| 2 | Societal sections of completed assessments are genuinely completed | | |
| 3 | Environmental impact assessed for large AI models | | |
| 4 | External perspectives sought for high-impact AI (ethics review, stakeholder engagement) | | |
| 5 | Corrective actions arising from societal findings are tracked to completion | | |

---

### CHECKLIST A.6 — AI SYSTEM LIFE CYCLE

**A.6.1.2 — Objectives for Responsible Development of AI System**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Responsible development objectives are documented | | |
| 2 | Objectives are specific and measurable (not vague) | | |
| 3 | Objectives name the demographic groups relevant to fairness | | |
| 4 | Objectives are derived from impact assessment findings | | |
| 5 | Objectives are communicated to development teams | | |

**A.6.1.3 — Processes for Responsible Design and Development of AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI development lifecycle procedure exists | | |
| 2 | Responsible AI checkpoints built into the development process | | |
| 3 | AI governance gates mapped to project phases | | |
| 4 | AI project register exists and is complete | | |
| 5 | Sample three AI projects — all governance gates completed? | | |
| 6 | Peer review conducted for model development | | |

**A.6.2.2 — AI System Requirements and Specification**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Requirements specification exists per AI system | | |
| 2 | Intended purpose and out-of-scope uses are stated | | |
| 3 | Responsible AI requirements (fairness, robustness, oversight) are included | | |
| 4 | Acceptance criteria are defined and testable | | |
| 5 | Requirements trace to impact assessment findings | | |

**A.6.2.3 — Documentation of AI System Design and Development**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Architecture documentation exists for all in-scope AI systems | | |
| 2 | Documentation is current — updated after the last system change | | |
| 3 | Design rationale documented (why decisions were made) | | |
| 4 | Dependencies (pre-trained models, third-party components) documented | | |
| 5 | Version control applied to training code, data and model weights | | |
| 6 | Experiment logs complete and enable reproduction | | |

**A.6.2.4 — AI System Verification and Validation**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Verification and validation plan exists per AI system | | |
| 2 | Fairness criteria defined (groups, metrics, thresholds) | | |
| 3 | Bias evaluation conducted before deployment, disaggregated by protected characteristic | | |
| 4 | Bias mitigation applied where thresholds exceeded | | |
| 5 | Adversarial and robustness testing performed; LLMs tested for prompt injection | | |
| 6 | Test data representativeness criteria defined and assessed | | |
| 7 | Test environment mirrors production infrastructure | | |
| 8 | Results compared against acceptance criteria and retained | | |
| 9 | Vulnerabilities and failures found are tracked to remediation | | |

**A.6.2.5 — AI System Deployment**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Deployment procedure exists with authorisation requirements | | |
| 2 | Deployment log maintained for all AI deployments | | |
| 3 | Authorisation records exist and predate deployment | | |
| 4 | Authoriser is not the developer (separation of duties check) | | |
| 5 | Rollback procedure exists and has been tested | | |
| 6 | Human oversight design verified as operational before go-live | | |
| 7 | Oversight personnel qualified before deployment | | |

**A.6.2.6 — AI System Operation and Monitoring**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Monitoring framework defines AI-specific metrics | | |
| 2 | Monitoring dashboards live and current | | |
| 3 | Alert thresholds configured for key metrics | | |
| 4 | Alert response log shows alerts are acted on | | |
| 5 | Drift detection configured with defined thresholds | | |
| 6 | Retraining decisions documented with rationale | | |
| 7 | Decommissioning procedure exists and has been followed for any retired systems | | |
| 8 | Data disposal evidence for retired systems; no orphaned AI data left behind | | |

**A.6.2.7 — AI System Technical Documentation**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Model card template exists | | |
| 2 | Model registry exists with all deployed models | | |
| 3 | Completed model card for every deployed model | | |
| 4 | Model cards include disaggregated performance metrics and known limitations | | |
| 5 | Model cards updated after each model change | | |
| 6 | Documentation is accessible to oversight personnel and, where relevant, to users | | |

**A.6.2.8 — AI System Recording of Event Logs**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Logging requirements defined per AI system | | |
| 2 | Logs capture inputs, outputs, model version and human overrides as appropriate | | |
| 3 | Log retention period defined and applied | | |
| 4 | Logs are protected against tampering and unauthorised access | | |
| 5 | Logs are sufficient to reconstruct a past decision during an investigation | | |

---

### CHECKLIST A.7 — DATA FOR AI SYSTEMS

**A.7.2 — Data for Development and Enhancement of AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Data requirements defined per AI system | | |
| 2 | AI data catalogue covers all training and evaluation datasets | | |
| 3 | Training, validation and test splits documented | | |
| 4 | Data used for enhancement and retraining is governed the same way | | |

**A.7.3 — Acquisition of Data**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Lawful basis confirmed for each AI personal data processing activity | | |
| 2 | Data licensing register confirms AI training use is permitted | | |
| 3 | Web-scraped data assessed for copyright and privacy | | |
| 4 | DPIAs conducted for high-risk AI personal data processing | | |
| 5 | DPAs in place for all cloud AI providers processing personal data | | |
| 6 | DPAs specifically address AI training use of customer data | | |
| 7 | Data subject rights procedure covers AI systems | | |

**A.7.4 — Quality of Data for AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI data quality standards defined with specific thresholds | | |
| 2 | Pre-training data quality assessments conducted | | |
| 3 | Representativeness included in the quality assessment | | |
| 4 | Production input data quality monitored | | |
| 5 | Data quality issue log maintained | | |

**A.7.5 — Data Provenance**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Data lineage documented from source to model | | |
| 2 | Origin and permitted use recorded for every dataset | | |
| 3 | Changes to source data are traceable | | |
| 4 | Provenance records are retained for the life of the model | | |

**A.7.6 — Data Preparation**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Data preparation steps (cleaning, labelling, augmentation) are documented | | |
| 2 | Labelling quality controls exist (guidelines, inter-annotator agreement) | | |
| 3 | Training data bias assessments conducted pre-training | | |
| 4 | Demographic representation and proxy variables assessed | | |
| 5 | Bias mitigation applied where assessment found issues, and effectiveness verified | | |

---

### CHECKLIST A.8 — INFORMATION FOR INTERESTED PARTIES OF AI SYSTEMS

**A.8.2 — System Documentation and Information for Users**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI capability sheets or product documentation exist | | |
| 2 | Documentation is accurate and not overstated | | |
| 3 | Known limitations documented and communicated | | |
| 4 | Marketing claims compared to verified performance metrics | | |
| 5 | Explainability requirements defined per AI system | | |
| 6 | Explanation mechanism implemented, functional and meaningful | | |
| 7 | Affected individuals can receive explanations on request | | |

**A.8.3 — External Reporting**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | External reporting obligations identified (regulators, authorities, customers) | | |
| 2 | AI regulatory watch list exists and covers the relevant authorities | | |
| 3 | Evidence of monitoring in the last three months | | |
| 4 | A route exists for external parties to report adverse impacts | | |
| 5 | Regulatory intelligence has fed into the AIMS management review | | |

**A.8.4 — Communication of Incidents**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI incident communication procedure exists | | |
| 2 | Communication templates prepared for different incident types | | |
| 3 | Notification timelines defined (regulatory, customer, public) | | |
| 4 | Escalation path and named approvers defined | | |
| 5 | Communication log for any past AI incidents | | |

**A.8.5 — Information for Interested Parties**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI disclosure policy exists | | |
| 2 | Users are told when they are interacting with AI | | |
| 3 | Disclosure is clear and prominent (not buried in terms and conditions) | | |
| 4 | Disclosure tested — is it actually visible to users? | | |
| 5 | Interested parties are identified and their information needs recorded | | |

---

### CHECKLIST A.9 — USE OF AI SYSTEMS

**A.9.2 — Processes for Responsible Use of AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Acceptable Use of AI Policy exists | | |
| 2 | Policy explicitly addresses external AI tools (approved and prohibited) | | |
| 3 | Approved external AI tools list exists and is current | | |
| 4 | Data restrictions for external AI tools are specified | | |
| 5 | Staff have acknowledged the policy | | |
| 6 | Policy enforced — violations are logged and acted on | | |
| 7 | Error handling design covers hard AND soft failures | | |
| 8 | Confidence thresholds and output validation implemented | | |
| 9 | Error logs include soft failures and are reviewed regularly | | |
| 10 | Human fallback procedure exists for high-stakes AI | | |

**A.9.3 — Objectives for Responsible Use of AI Systems**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Objectives for responsible use are documented | | |
| 2 | Objectives cover human oversight expectations | | |
| 3 | Objectives are measurable and owned | | |
| 4 | Progress against objectives is reported to management review | | |

**A.9.4 — Intended Use of the AI System**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Intended use is documented for each AI system in operation | | |
| 2 | Actual use in production matches the documented intended use | | |
| 3 | Controls prevent or detect out-of-scope use | | |
| 4 | Human oversight policy defines which AI requires oversight | | |
| 5 | Override logs maintained and the override rate is plausible | | |
| 6 | Overseers are qualified (training and domain knowledge) | | |
| 7 | Anti-automation-bias design evidence exists | | |

---

### CHECKLIST A.10 — THIRD-PARTY AND CUSTOMER RELATIONSHIPS

**A.10.2 — Allocating Responsibilities**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | Third-party AI inventory exists | | |
| 2 | All third-party AI tools inventoried (including SaaS with embedded AI features) | | |
| 3 | Responsibilities allocated across the AI value chain and recorded | | |
| 4 | Risk-based assessment depth applied | | |
| 5 | Assessment records cover technical, bias, security, privacy and regulatory aspects | | |
| 6 | Assessments predate adoption and approval records exist for high-risk third-party AI | | |
| 7 | Periodic reassessment schedule exists and is followed | | |

**A.10.3 — Suppliers**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI standard contract clauses library exists | | |
| 2 | Performance SLAs in AI supplier contracts | | |
| 3 | Data handling obligations in contracts | | |
| 4 | AI incident notification obligation in contracts | | |
| 5 | Audit rights in high-risk supplier contracts | | |
| 6 | Regulatory compliance obligation in contracts | | |
| 7 | DPAs in place for all AI suppliers processing personal data | | |
| 8 | Ongoing supplier monitoring evidenced, not just onboarding checks | | |

**A.10.4 — Customers**

| # | What to Check | Status | Evidence / Notes |
|---|---|---|---|
| 1 | AI-enabled product/service register exists | | |
| 2 | Customer AI governance requirements tracked | | |
| 3 | Customer-facing AI documentation available (model cards, capability sheets) | | |
| 4 | Customer audit response procedure exists | | |
| 5 | Customer contract AI obligations are being met | | |

---

## PART 5 — CLASSIFYING YOUR FINDINGS
### (How to decide how serious each finding is)

---

### 5.1 — Finding Classification Guide

When you find something wrong, you need to decide how serious it is. ISO 42001 audits use four levels:

---

**🔴 MAJOR NON-CONFORMITY**

*What it means:* A serious failure that could mean the whole AIMS isn't working. The organization is likely to fail certification if this isn't fixed.

*Think of it like:* A hospital that has no patient safety policy at all — not just a slightly outdated one.

*When to use it:*
- A required process, document, or control is completely absent
- A control exists on paper but has never been implemented in practice
- A previous major finding was not corrected
- The same minor non-conformity has been found in multiple areas showing a systematic failure
- A legal or regulatory breach has resulted

*Examples:*
- No AI System Impact Assessment has EVER been conducted for ANY AI system
- AI systems are deployed without any authorization process
- Zero evidence of human oversight — override rate is 0% across all high-stakes AI for 12 months
- No management review has occurred in the last 12 months

---

**🟡 MINOR NON-CONFORMITY**

*What it means:* A real gap or failure but in an isolated area. The overall system is working but this specific control is not fully implemented.

*Think of it like:* A hospital that has a patient safety policy but one department hasn't communicated it to new staff.

*When to use it:*
- A document exists but is missing a required element
- A process is defined but not always followed (isolated instances)
- A record exists but is incomplete
- A control is implemented but not documented

*Examples:*
- ASIA template exists but the societal impact section is blank for 2 out of 5 systems
- Bias evaluation was conducted but results are not disaggregated by protected characteristic
- Third-party AI inventory exists but one cloud AI API in use is not on it
- Override logs exist but override rate is suspiciously low (0% for 3 months) for one specific system

---

**🔵 OBSERVATION / OPPORTUNITY FOR IMPROVEMENT**

*What it means:* Not a failure — the requirement is met — but you can see a way to make it better.

*Think of it like:* A hospital that has a patient safety policy but it's written in very complex language that's hard for nurses to understand.

*When to use it:*
- The requirement is technically met but the implementation is weak
- A trend that could become a non-conformity if not addressed
- A best practice that would improve effectiveness
- Something working well that could be extended elsewhere

*Examples:*
- Bias evaluation is conducted but only annually — more frequent evaluation would be better given the model's use case
- Acceptable use policy is comprehensive but employee quiz scores suggest some staff are not retaining the key rules
- Management review occurs but action items are not always assigned owners and deadlines

---

**✅ CONFORMING (POSITIVE FINDING)**

Don't forget to record the good things! Positive findings show what's working and what the organization should keep doing.

*Examples:*
- Bias evaluation reports are comprehensive, with disaggregated results across all relevant demographic groups, and clear evidence of mitigation where thresholds were exceeded
- The override log shows a realistic and well-documented override rate with full rationale for each override
- Third-party AI assessments are thorough and consistently completed before adoption

---

### 5.2 — How to Write a Finding

A good finding has four parts, sometimes called a **PFAS**:

| Part | What it is | Example |
|---|---|---|
| **P** — Problem | What is wrong? | "No bias evaluation has been conducted for the loan scoring AI system." |
| **F** — Finding Evidence | What evidence shows the problem? | "The model card for LOAN-AI-001 shows the bias evaluation section as 'pending'. The ML Engineer confirmed during interview that bias evaluation has not been scheduled." |
| **A** — Applicable Requirement | Which requirement is not met? | "ISO 42001 Annex A, Control A.6.2.6 requires documented bias evaluation before deployment." |
| **S** — Significance | How serious is it? | "Classified as Major Non-Conformity. The system is deployed in production making decisions that affect loan applicants. Undetected bias could result in discriminatory outcomes for protected groups." |

**Full example finding:**

> **Finding #3 — Major Non-Conformity — A.6.2.6 Bias Evaluation**
>
> **Problem:** No bias evaluation has been conducted for the loan scoring AI system (LOAN-AI-001).
>
> **Evidence:** The model card for LOAN-AI-001 shows the bias evaluation section marked as "pending." Interview with the ML Engineer on 12 April 2026 confirmed that bias evaluation has not been scheduled or conducted. The ASIA for LOAN-AI-001 identifies gender and ethnicity as relevant demographic characteristics for fairness assessment but documents no corresponding evaluation.
>
> **Requirement:** ISO 42001:2023 Annex A, Control A.6.2.6 requires the organization to conduct documented bias evaluation using appropriate fairness metrics and disaggregated analysis across relevant demographic groups before deployment.
>
> **Significance:** Major Non-Conformity. LOAN-AI-001 is deployed in production making credit scoring decisions affecting thousands of customers. The absence of any bias evaluation means potential discriminatory outcomes for protected groups cannot be detected or mitigated. This also likely constitutes a breach of EU AI Act requirements for high-risk AI systems.

---

## PART 6 — WRITING THE AUDIT REPORT

---

### 6.1 — Audit Report Template

Use this template to write your audit report. Fill in every section.

---

```
═══════════════════════════════════════════════════════════════
         ISO 42001 INTERNAL AUDIT REPORT
═══════════════════════════════════════════════════════════════

AUDIT REFERENCE:     IA-[YEAR]-[NUMBER]  (e.g., IA-2026-003)
REPORT DATE:         [DD Month YYYY]
AUDIT PERIOD:        [From date] to [To date]

AUDITOR(S):          [Name(s), role(s)]
LEAD AUDITOR:        [Name]
AUDITEE:             [Organization / Department name]
AUDIT SPONSOR:       [Name of senior manager who commissioned the audit]

AUDIT SCOPE:
[Describe exactly what was audited — which clauses, which Annex A domains,
which AI systems, which departments. Be specific.]

AUDIT OBJECTIVES:
1. Verify conformance with ISO/IEC 42001:2023 requirements within scope
2. Assess effectiveness of the AIMS in achieving its intended outcomes
3. Identify opportunities for improvement
4. Verify closure of previous audit findings

DOCUMENTS REVIEWED:
[List all documents reviewed, including version/date]

PEOPLE INTERVIEWED:
[List all people interviewed, with their role]

═══════════════════════════════════════════════════════════════
SECTION 1 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════

OVERALL ASSESSMENT:
[One paragraph. Overall maturity of the AIMS. Is it broadly effective?
Are there significant gaps? Has it improved since the last audit?
Be honest and balanced.]

FINDING SUMMARY:
  Major Non-Conformities:         [Number]
  Minor Non-Conformities:         [Number]
  Observations:                   [Number]
  Positive Findings:              [Number]

PREVIOUS FINDINGS STATUS:
  Total previous findings:        [Number]
  Closed (verified effective):    [Number]
  Partially addressed:            [Number]
  Not addressed (repeat finding): [Number]

═══════════════════════════════════════════════════════════════
SECTION 2 — DETAILED FINDINGS
═══════════════════════════════════════════════════════════════

[Repeat this block for each finding, in order of severity]

───────────────────────────────────────────────────────────────
FINDING #[Number]
Classification:    [🔴 MAJOR | 🟡 MINOR | 🔵 OBSERVATION | ✅ POSITIVE]
Control Reference: [e.g., A.6.2.6 | Clause 9.2 | etc.]
───────────────────────────────────────────────────────────────

PROBLEM STATEMENT:
[One sentence describing what is wrong or what was done well]

EVIDENCE:
[Specific evidence — document names, interview quotes, test results.
Do not write vague descriptions. Quote the document, name the interviewee,
show the date. Evidence must be verifiable.]

APPLICABLE REQUIREMENT:
[Quote or paraphrase the exact ISO 42001 requirement that is (not) met.
Include clause or control reference.]

SIGNIFICANCE / IMPACT:
[Why does this matter? What harm could result if not fixed?
What benefit does the positive finding create?]

ROOT CAUSE (for non-conformities):
[What caused this gap? Process failure? Resource constraint?
Awareness gap? Design oversight? Identifying root cause helps the
organization fix it properly.]

REQUIRED ACTION:
[For non-conformities: The organization must address this by [date].
A corrective action plan is required.
For positive findings: No action required — maintain this practice.]

───────────────────────────────────────────────────────────────

[... repeat for each finding ...]

═══════════════════════════════════════════════════════════════
SECTION 3 — CORRECTIVE ACTION REQUIREMENTS
═══════════════════════════════════════════════════════════════

The auditee must respond to this report with a corrective action plan
within [14/30] days of report issuance, covering:

For each Major Non-Conformity:
  a) Root cause analysis
  b) Immediate containment action (if applicable)
  c) Corrective action to prevent recurrence
  d) Owner and target completion date
  e) Evidence that will demonstrate closure

For each Minor Non-Conformity:
  a) Corrective action description
  b) Owner and target completion date
  c) Evidence that will demonstrate closure

═══════════════════════════════════════════════════════════════
SECTION 4 — NEXT STEPS
═══════════════════════════════════════════════════════════════

CORRECTIVE ACTION PLAN DUE:     [Date — typically 14-30 days from report]
FOLLOW-UP AUDIT DATE:           [Date — typically 30-90 days for Major NCs]
NEXT SCHEDULED INTERNAL AUDIT:  [Date from Audit Programme]

═══════════════════════════════════════════════════════════════
SIGNATURES
═══════════════════════════════════════════════════════════════

Lead Auditor:   ___________________________  Date: ______________
                [Name]

AI Governance   ___________________________  Date: ______________
Lead:           [Name]

Top Management  ___________________________  Date: ______________
Representative: [Name]
```

---

## PART 7 — AFTER THE AUDIT
### (What happens next — and what you need to follow up)

---

### 7.1 — Corrective Action Follow-Up

After the audit, the organization must produce a **Corrective Action Plan (CAP)**. Your job as auditor is to:

1. **Review the CAP** — Is the root cause correctly identified? Is the proposed fix sufficient?
2. **Approve or challenge** — If the fix doesn't address the root cause, send it back.
3. **Verify closure** — When the organization says a finding is fixed, check the evidence.

**Evidence of closure must be real:**
- "We created a policy" — show me the signed, dated policy.
- "We trained staff" — show me the training records AND a test of knowledge retention.
- "We conducted the bias evaluation" — show me the completed report with disaggregated results.

**Do not close a finding based on intent or plans — only on demonstrated evidence.**

---

### 7.2 — Audit Programme Update

After the audit:
- [ ] Update the Audit Programme with outcomes
- [ ] Schedule follow-up audit for major non-conformities
- [ ] Adjust future audit scope based on findings (higher-risk areas need more audit attention)
- [ ] Feed lessons learned into the AIMS management review

---

### 7.3 — Metrics to Track Year-on-Year

Track these numbers across audit cycles to show AIMS maturity improvement:

| Metric | Year 1 | Year 2 | Year 3 | Target |
|---|---|---|---|---|
| Major Non-Conformities | | | | 0 |
| Minor Non-Conformities | | | | <3 |
| Controls fully conforming | | | | 38/38 |
| % AI systems with completed ASIA | | | | 100% |
| % AI systems with bias evaluation | | | | 100% |
| % staff trained in AI governance | | | | 100% |
| % third-party AI with assessment | | | | 100% |
| Override rate (plausible range) | | | | >0% |
| Findings closed within target date | | | | 100% |

---

## PART 8 — QUICK REFERENCE CARD
### (Print this out and keep it with you during the audit)

---

```
┌─────────────────────────────────────────────────────────────┐
│          ISO 42001 AUDIT — QUICK REFERENCE CARD             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  THE AUDITOR'S GOLDEN RULES                                 │
│  ✦ Only report what you can prove                           │
│  ✦ Always ask "Can you show me that?"                       │
│  ✦ Compare what people say to what documents say            │
│  ✦ Check dates — before or after deployment?                │
│  ✦ No surprises — share findings before closing meeting     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  THE MAGIC TEST QUESTIONS                                   │
│  1. "Show me the last time you did that."                   │
│  2. "Can you show me the evidence?"                         │
│  3. "Was this done BEFORE the AI was deployed?"             │
│  4. "Who is accountable if this AI causes harm?"            │
│  5. "Can you override the AI right now? Show me how."       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TOP 10 GAPS FOUND IN EVERY AUDIT                           │
│  1. Impact assessments done AFTER deployment                │
│  2. Bias evaluation without disaggregated results           │
│  3. Override rate of 0% — rubber-stamping                   │
│  4. 3rd party AI tools not inventoried                      │
│  5. No DPAs for cloud AI processing personal data           │
│  6. Training recorded as complete but staff don't know      │
│     the policies                                            │
│  7. Acceptable use policy doesn't address ChatGPT/LLMs      │
│  8. Pre-trained models used without license review          │
│  9. Management review with no action items produced         │
│  10. Previous audit findings still not closed               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FINDING CLASSIFICATION                                     │
│  🔴 MAJOR  — Completely absent or systemic failure          │
│  🟡 MINOR  — Partial or isolated failure                    │
│  🔵 OBS    — Met but could be better                        │
│  ✅ POS    — Working well — note it and praise it           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FINDING FORMAT (PFAS)                                      │
│  P — Problem (what is wrong)                                │
│  F — Finding Evidence (specific proof)                      │
│  A — Applicable Requirement (which clause/control)          │
│  S — Significance (why it matters)                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## PART 9 — GLOSSARY
### (Plain-English definitions of terms used in this guide)

---

| Term | Plain English Meaning |
|---|---|
| **AIMS** | AI Management System — the whole set of policies, processes, and controls an organization uses to govern its AI responsibly |
| **Annex A** | The list of 38 specific controls in ISO 42001 that organizations should implement |
| **ASIA** | AI System Impact Assessment — a structured analysis of what harm an AI system could cause, done before deployment |
| **Audit** | A systematic check to verify whether the AIMS works as it should |
| **Auditor** | The person conducting the audit — that's you! |
| **Auditee** | The organization (or team) being audited |
| **Bias** | When an AI system treats different groups of people unfairly — for example, making better predictions for men than for women |
| **Conforming** | Meeting the requirement — the organization is doing what ISO 42001 says it should |
| **Control** | A specific action or safeguard that reduces a risk |
| **Corrective Action** | The fix put in place after a non-conformity is found |
| **Data Provenance** | Knowing exactly where data came from and whether the organization has the right to use it |
| **Deployment** | When an AI system is put into real use (goes from testing to production) |
| **Drift** | When an AI model's performance gets worse over time because the world changes but the model doesn't |
| **DPIA** | Data Protection Impact Assessment — a privacy risk analysis required when AI processes sensitive personal data |
| **Evidence** | Proof that something happened — a document, a record, a screenshot, a log file |
| **Finding** | Something the auditor discovered during the audit — can be positive or negative |
| **Major Non-Conformity** | A serious failure — the organization is significantly not meeting a requirement |
| **Minor Non-Conformity** | A smaller failure — a requirement is partially not met in an isolated area |
| **Model Card** | A document describing what an AI model does, how well it performs, and its known limitations |
| **Non-Conformity** | A failure to meet a requirement of ISO 42001 |
| **Observation** | A finding that the requirement is met but could be done better |
| **Override** | When a human reviewer decides NOT to follow the AI's recommendation |
| **Pre-trained Model** | An AI model built by someone else (e.g., from Hugging Face) that you download and use rather than train yourself |
| **Prompt Injection** | An attack where someone tricks a language model by embedding instructions in the input text |
| **RACI** | Responsible, Accountable, Consulted, Informed — a way of documenting who is responsible for what |
| **SoD** | Segregation of Duties — making sure the same person doesn't both build and approve their own AI system |
| **Statement of Applicability** | A document listing which of the 38 controls apply to the organization and why |
| **Third-Party AI** | AI systems or services built by someone else that the organization buys or uses |

---

## DOCUMENT CONTROL

| Field | Value |
|---|---|
| Document ID | AIMS-AUDIT-GUIDE-001 |
| Document Title | ISO 42001 Internal Audit Guide — Complete End-to-End |
| Version | 1.0 |
| Author | Ankit Uniyal — ISO 42001 Lead Auditor |
| Review Cycle | Annual |
| Next Review Date | April 2027 |
| Standard Reference | ISO/IEC 42001:2023 |
| Related Documents | INTERNAL-AUDIT-PROCEDURE.md, ../10-ANNEX-A-CONTROLS.md, ../01-GAP-ASSESSMENT.md |

---

**DISCLAIMER:** This guide is provided for educational and practical guidance purposes only. It does not constitute legal, regulatory, or professional advice. Always refer to the official ISO/IEC 42001:2023 standard text for definitive normative requirements. Organizations seeking ISO 42001 certification should engage a qualified implementation consultant and accredited certification body.

---

*Maintained by Ankit Uniyal — ISO 42001 Lead Auditor | GRC Lead, PureHealth Group*
*Part of the ISO 42001 AI Governance Toolkit: github.com/Ankit-Uniyal/iso-42001-ai-governance-toolkit*
*MIT License — Free to use, adapt, and distribute with attribution*
