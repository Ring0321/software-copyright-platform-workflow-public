# Workflow Gates

## Gate sequence

Use the base skill `confirm_stage.py` for its supported gates and keep a timestamped confirmation record. Use this skill's `scripts/record_gate.py` for the additional gates named below.

1. `environment`: DOCX/PDF tooling and fallback choice.
2. `code-source-strategy` (additional): user chooses `new-code`, `rewrite-code`, or `existing-project` before soft-copyright drafting begins.
3. `cooperation-development` (additional): user confirms whether the filing is cooperation development; if yes, collect cooperation developers, ID numbers, expected completion date, and agreement signing date.
4. `project`: exact registered project root after the chosen code-source strategy has a verified source boundary.
5. `registration-scope` (additional): independent software versus actual upgrade.
6. `business`: product purpose, users, workflow, and technical boundary.
7. `application-fields`: the complete initial application-information draft, including explicit pending identity data and provisional code counts.
8. `template` (additional): bundled fixed PDF/DOCX/TXT template in `assets/fixed-submission-template/`, or a user-confirmed newer replacement, and whether layout cloning is approved.
9. `code-selection`: complete-file whitelist, exclusions, and read-only unreachable-module classification.
10. `screenshot-method`: real screenshots, desktop capture, browser capture, user-supplied, or skip.
11. `markdown`: manual and application drafts approved for formal generation.
12. `final-submission` (additional): final DOCX/PDF/TXT inventory, verified code counts, updated application TXT, cooperation agreement when applicable, and delivery folder.

## Stop conditions

Stop and request user confirmation when:

- the project root is ambiguous;
- the user has not confirmed whether the code will be newly written, rewritten, or read from an existing project;
- the user chooses `new-code` or `rewrite-code` and no separate development/rewrite scope has been confirmed;
- the user has not confirmed whether the filing is cooperation development;
- cooperation development is confirmed but any cooperation developer name, ID number, expected completion date, or agreement signing date is missing;
- the cooperation agreement signing date is not earlier than the expected completion date;
- software name/version or registration type is ambiguous;
- an old registration may be too similar;
- owner/date/environment data is incomplete;
- selected code contains unreferenced or development-only modules;
- screenshot handling is undecided;
- the bundled fixed template is missing, a replacement template is ambiguous, or the template and current content conflict;
- formal files are about to overwrite an earlier package;
- destination files are locked and cannot be hash-verified.

## Second-registration difference matrix

Create a table with these rows:

- software full name and short name;
- registration version;
- primary purpose;
- user-facing entry point;
- runtime architecture;
- core modules;
- authorization/processing workflow;
- outputs and storage;
- operation manual chapters;
- source-code overlap and independent code;
- evidence supporting independent registration.

Do not rely on naming changes alone. Require functional and source-level evidence.
