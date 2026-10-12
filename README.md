# Tender Pilot — isolated local MVP

A new project, independent of `tender-pilot-approved`. No deployment or paid infrastructure. Local demonstration authentication, not production authentication. All sample data is synthetic.

## Install and run

Requirements: Node.js 24+, Python 3, Poppler `pdftotext`. The application has no npm dependencies. DOCX extraction uses Python's standard library. Test PDF/DOCX generation additionally requires python-docx and reportlab.

```bash
cd tender-pilot-one-shot
npm install --ignore-scripts
npm start
```

Open http://localhost:3000. The server binds loopback only. SQLite and uploaded files persist in `data/`. To install extraction/test prerequisites on Ubuntu:

```bash
sudo apt-get install poppler-utils python3-venv
python3 -m venv .venv
. .venv/bin/activate
python -m pip install python-docx reportlab
npm test
```

## Complete walkthrough

1. Choose **Explore synthetic demo**. This creates an isolated demonstration account and seeds a fictional company, tender, ten source-backed suggestions and two evidence files. One requirement is accepted/complete with accepted evidence; remaining items need attention.
2. Choose Companies to edit the synthetic profile, or New company to create your own fictional company. Choose Tenders to create a workspace. Company and tender selectors keep the workspace scoped.
3. Upload a TXT, text-based PDF or DOCX in Documents. View the actual extracted text; download the original. Corrupt and image-only documents fail visibly. Maximum file size: 5 MB.
4. Run **DEMO ANALYSIS**. Deterministic rules propose requirements from lines containing requirement signals; each quotation is checked against the extracted text. This is not live AI and may miss requirements.
5. In Requirements, edit descriptions, accept or reject suggestions, select progress and save notes. Add manual requirements when needed.
6. In Evidence, upload company documents. Mark them reviewed or accepted as a human reviewer. Link the evidence in Requirements, save the review and return to Dashboard.
7. Dashboard updates from saved data. Progress counts accepted, completed requirements over all non-rejected requirements. Missing accepted evidence is a conservative flag on every accepted requirement; evidence applicability has not been modeled separately.
8. Open Report to review saved tender/company details, requirements, source references, gaps and warnings. Print / Save as PDF uses the browser print dialog.
9. Reset synthetic demo clears only the current demonstration account's records and reseeds it. Ordinary local accounts cannot reset this way. Sign out and register another account to exercise isolation.

## Live AI

Set OPENAI_API_KEY in the server process environment without putting it in a file or source. The UI then offers an explicit billable live-analysis action using gpt-4.1-mini. One call per click, no automatic retries; quotes not found in the source are discarded. Input is limited to the first 40,000 extracted characters, output to 2,500 tokens and 100 proposals. Truncated output can fail visibly. Live requests were **not tested**, and no provider requests were made during this build. There is no credit ledger or spend ceiling; production needs these before live use.

## Validation results

`npm test`: 1 integrated workflow test passed, 0 failures. Covers registration/login/logout, protected access, company/tender persistence, actual TXT/PDF/DOCX extraction, invalid file rejection, quote validation, duplicate analysis avoidance, review/evidence updates, cross-company evidence rejection, cross-account isolation and persistence after database reopen. JavaScript syntax checks pass. HTML route returns HTTP 200.

Browser automation was unavailable under the supported managed preview workflow. The interface, interactive journey and print layout have **not** been browser-tested. No screenshots were captured. The test validates server operations, not browser rendering.

## Working / partial / missing

Implemented: responsive landing/workspace interface; local registration/login/logout; owner-scoped SQLite records; company creation/editing; tender creation/switching; file upload/extraction/download; deterministic analysis; live AI integration (untested); source-validated suggestions; requirement review/manual entry; evidence upload/review/acceptance/delete; associations; data-derived progress; print-friendly report; resettable synthetic demonstration.

Partial: deterministic analysis has limited recall; source locations are extracted line numbers, not original PDF page numbers; AI analyzes only a bounded excerpt; browser PDF export requires user printing; no confidence scoring beyond human review state; risks surface as requirement categories and general report warnings rather than a comprehensive risk model.

Missing production capabilities: hardened identity/HTTPS and secure cookies; account recovery and email verification; durable hosted storage and backups; malware scanning; OCR; audit trails; reviewer roles; billing and AI cost controls; retention/privacy policy implementation; concurrency/load testing; production deployment; a verified browser acceptance run. These are launch blockers. Do not use this local MVP as a production service or as a compliance certificate.
