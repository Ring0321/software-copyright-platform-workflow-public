---
name: software-copyright-platform-workflow
description: Create and strictly audit Chinese software-copyright documents from a user-confirmed code-source strategy, cooperation-development decision, the user's fixed PDF/DOCX/TXT template, and a real verified project source boundary. Use for choosing whether to write new code, rewrite code, or read an existing project before soft-copyright planning; deciding whether the filing is cooperation development; collecting cooperation developers, ID numbers, expected completion date, and agreement signing date; fixed-template extraction; template-matched software manuals; application-information TXT files; cooperation agreement DOCX/PDF; source-code selection and formatting; first/second registration separation; platform-ready DOCX/PDF bundles; and final document consistency checks.
---

# Software Copyright Platform Workflow

Create platform-ready software-copyright documents by first recording how the registered code will be produced or supplied, confirming whether the filing uses cooperation development, preserving the base skill's complete application-information workflow, then reproducing the user's fixed manual/code/agreement PDF or DOCX template and extracting verified real source code.

## Public edition note

This public repository intentionally does not ship real filing templates, personal identity data, customer project materials, or prior registration documents. Add your own private template files locally under `assets/fixed-submission-template/` before formal generation, and keep those files out of public commits.

## Scope boundary

- During the formal material workflow, never develop, complete, refactor, rename, or modify project source code.
- Never create code merely to reach a page target.
- If the user chooses to write new code or rewrite code, record that decision and stop the material workflow until a separate, explicitly authorized development task has produced verified source code.
- Read an existing or newly produced project only to understand the software and extract existing source.
- If source defects, unused modules, inconsistent names, or missing functionality are found, report them and stop for user direction.
- Create or edit only application drafts, TXT, DOCX, PDF, diagrams, screenshots, manifests, and audit reports.

## Required base skills

1. Read `C:/Users/Ring/.codex/skills/software-copyright-materials/SKILL.md` and reuse its environment checks, confirmation gates, and scripts.
2. Read the `docx` skill for Word inspection/generation and the `pdf` skill for PDF rendering/visual checks.
3. Do not overwrite the installed `software-copyright-materials` skill or the user's earlier registration materials.
4. If the base skill is missing, stop and request installation before formal generation.
5. Use the base `confirm_stage.py` for its supported gates. Use [scripts/record_gate.py](scripts/record_gate.py) only for this skill's additional `code-source-strategy`, `cooperation-development`, `registration-scope`, `template`, and `final-submission` gates.

## Core rules

- The user must choose the code-source strategy before application drafting, template writing, or code selection begins.
- The user must confirm whether the filing is cooperation development before application drafting. If cooperation development is confirmed, collect cooperation developer names, ID numbers, expected completion date, and agreement signing date before formal generation.
- The local fixed template in `assets/fixed-submission-template/` is the default formatting and submission-shape authority after the user supplies it. Read [references/fixed-shaanbei-submission-template.md](references/fixed-shaanbei-submission-template.md) before drafting or formatting formal materials.
- Formal DOCX/PDF/TXT outputs must match the selected local template formatting exactly in structure, page setup, naming pattern, header/footer behavior, title hierarchy, body style, table/figure placement, code pagination, and field order. Treat prose summaries of the template as navigation aids only; the actual user-supplied local template files are authoritative. If exact template cloning cannot be achieved or verified, stop and report the mismatch instead of delivering an approximate file.
- Treat the user's fixed PDF/DOCX template as already selected only when it exists in the local template folder or is supplied in the current task; do not substitute another template unless the user explicitly replaces it.
- The current project and confirmed application fields are the content authority.
- Reuse layout, hierarchy, density, tables, captions, headers, and fonts; never copy the earlier software's technical content as current content.
- Keep each registration and each formal iteration in a separate dated folder.
- Use only complete, real source files selected from the confirmed project boundary.
- If the registered program is under 60 pages, submit the complete selected program. Do not pad it to 60 pages.
- If it reaches 60 pages or more, arrange the confirmed complete-file sequence first, then prepare continuous first 30 and last 30 pages.
- Use 50 material lines per code page. The final page ends naturally.
- Use language-valid file markers, such as `# File:` for Python.
- Formal documents must not contain drafting instructions, “soft-copyright material”, “screenshot placeholder”, “submit later”, or other process narration.
- Do not claim functionality that cannot be traced to the existing project or user-supplied evidence.

## Workflow

### 1. Create an isolated work package

Create a new dated directory with separate areas for drafts, formal files, template profiles, diagrams/screenshots, and audit reports. Never mix it with the prior registration.

```text
<software-slug>_软著材料_<YYYYMMDD>/
├── 草稿/
├── 模板规格/
├── PlantUML/
├── 截图/
├── 正式资料/
└── 核检报告/
```

### 2. Confirm the code-source strategy

Before analyzing business content or drafting application information, ask the user to choose and confirm one of these strategies:

1. `new-code`: 自主编写代码. The registered software does not yet have a usable source boundary. Record the gate, stop this material workflow, and request a separate development brief before creating or editing code. Resume this workflow only after the new code exists, runs or is otherwise verified, and the user confirms it is the registered project.
2. `rewrite-code`: 重新编写代码. Existing code is not the filing boundary. Record the gate, stop this material workflow, and request an explicit rewrite scope before modifying code. Do not use the old code as registration evidence unless the user later confirms a mixed or inherited boundary.
3. `existing-project`: 读取已有项目代码进行软著预案和材料编写. Record the gate and continue with the selected project as the content authority.

Do not infer a default strategy. If the user has already said “按现有项目做”, “读取当前项目”, or equivalent in the same task, record `existing-project` with that wording as the confirmation.

Record this gate with:

```bash
python3 scripts/record_gate.py \
  --workdir <software-slug>_软著材料_<YYYYMMDD> \
  --stage code-source-strategy \
  --note "<用户确认的新建/重写/读取已有项目策略>"
```

### 3. Confirm cooperation development

Read [references/cooperation-development-gate.md](references/cooperation-development-gate.md). Ask whether the filing is `cooperation`, `not-cooperation`, or `undecided`.

If `cooperation`, collect and confirm:

- cooperation developer names in final rights-holder order;
- ID number for each cooperation developer;
- expected development completion date;
- cooperation agreement signing date.

The signing date must be earlier than the expected development completion date. If the date rule fails or any required person/ID/date field is missing, stop before formal generation. When cooperation is confirmed, keep `开发方式：合作开发`, `著作权人`, agreement signer list, completion date, and signing date consistent across drafts, application TXT, and the cooperation agreement.

Always write `草稿/合作开发确认.md` and `草稿/合作开发确认.json` before drafting application information. These files must show whether the filing is cooperation development, the required cooperation fields when applicable, pending items, and whether the signing-date-before-completion-date rule passes.

Record this gate with:

```bash
python3 scripts/record_gate.py \
  --workdir <software-slug>_软著材料_<YYYYMMDD> \
  --stage cooperation-development \
  --note "<用户确认的是否合作开发、合作人、日期和缺失字段情况>"
```

### 4. Confirm the registration boundary

Identify whether the work is a new independent registration or a real version upgrade. For a second registration, compare software name, purpose, architecture, core modules, workflow, outputs, and source boundary with the first registration.

Use the first registration only as a formatting reference unless the user explicitly confirms shared content. Record the `registration-scope` gate.

### 5. Complete the original application-information workflow first

Preserve the beginning of the base `software-copyright-materials` workflow without replacing it:

1. check the document-generation environment;
2. confirm the project root;
3. analyze the project and prepare business understanding;
4. confirm software name, short name, version, category, dates, development method, publication status, rights holders, rights scope, hardware/software environment, programming language, purpose, domain, main functions, and technical characteristics;
5. generate `草稿/申请表信息.md` and record the base `application-fields` gate.

Read the base skill's `references/application_fields.md` and [references/application-and-bundle.md](references/application-and-bundle.md). Preserve all 25 fields, their order, choice sets, character limits, confirmation requirements, and consistency rules. Do not reduce the application-information draft to a short summary table.

If cooperation development is confirmed, `开发方式` must be `合作开发`, the rights-holder order must match the cooperation agreement signer order, and the application completion date must match the confirmed expected completion date unless the user explicitly records a reason.

At this first stage, source amount and code pages may be marked “待最终代码材料核定”. Do not reuse counts from an earlier registration. After the code document is finalized, update only those calculated fields and generate the final `申请表信息.txt`.

The application-information stage is mandatory even when the user only asks to rewrite the manual or code material.

### 6. Extract the fixed supplied PDF/DOCX template

Use the local fixed PDF/DOCX template as the default formatting authority. Read [references/fixed-shaanbei-submission-template.md](references/fixed-shaanbei-submission-template.md) and use the private template assets in `assets/fixed-submission-template/` once the user supplies them. Use DOCX assets for editable style extraction and PDF assets for visual verification. Do not search for, invent, or choose a different template.

If the fixed template assets are missing or unreadable, stop and ask the user to provide them again before writing manual/code content. Once available, inspect them before writing content. Extract and save a template profile covering:

- page size, orientation, margins, and section breaks;
- header/footer text, distance, alignment, and page numbers;
- cover arrangement and title positions;
- heading numbering, fonts, sizes, color, spacing, and outline levels;
- body font, indentation, alignment, line spacing, and paragraph spacing;
- table borders, widths, shading, fonts, and cell margins;
- figure dimensions, captions, and surrounding spacing;
- code line-number format, font, line spacing, and lines per page.

Run [scripts/inspect_docx_template.py](scripts/inspect_docx_template.py) for DOCX templates, then visually inspect representative PDF pages. For PDF-only templates, create the template profile from visual inspection and any extractable page/font/table evidence. Save the resulting JSON in `模板规格/`.

Read [references/template-extraction-standard.md](references/template-extraction-standard.md).

### 7. Draft the manual from current evidence

Read the current project, existing user descriptions, screenshots, and confirmed application fields. Rewrite every chapter for the current software while following the extracted template structure.

- Match the template's chapter depth and paragraph density.
- Use formal software-manual language.
- Describe actual inputs, operations, decisions, outputs, and exceptions.
- Keep screenshots or diagrams in the same positions and proportions as the template.
- When real screenshots are deferred, use neutral figure space and formal captions without visible drafting instructions.
- Use PlantUML only when the template contains architecture or flow diagrams; size it for the template page.

Read [references/manual-template-standard.md](references/manual-template-standard.md). Record the `markdown` and `screenshot-method` gates before formal generation.

### 8. Select existing source code

Generate a complete source inventory. Classify files as:

- registered product runtime source;
- genuine public extension or operational interface;
- tests/examples/docs;
- application/manual/material-generation helpers;
- research/review-only code;
- generated output, cache, or dependency.

Select only the first two categories. Do not modify a file to make it look more relevant. For every selected file, record the path, line count, hash, and selection reason.

Perform a read-only import/call audit when applicable. Unreachable code is a warning, not an automatic deletion. Ask the user whether it is a shipped public interface or outside the registered software boundary. Never edit the source to resolve the warning.

Read [references/code-extraction-format.md](references/code-extraction-format.md). Record the `code-selection` gate.

### 9. Build the code document in the supplied format

1. Copy each confirmed source file from first line to last line.
2. Preserve all existing source lines, including natural blank lines.
3. Add one language-valid file marker before each file.
4. Order files by the confirmed product/module sequence.
5. Number material lines continuously.
6. Place exactly 50 material lines on each full page.
7. Apply the code template's page, header, footer, font, and spacing properties.
8. Keep body text black; do not add syntax highlighting or hyperlinks.
9. Let the final page end naturally; do not add fake comments or blank lines.

For under-60-page material, generate one complete `<软件全称>-源代码.docx/pdf` ending naturally. For 60 pages or more, generate one combined 60-page `<软件全称>-源代码.docx/pdf` by placing the first 30 pages and last 30 pages into the same document. Do not produce separate `前30页` and `后30页` files unless the user explicitly asks for that alternate package.

Use [scripts/audit_source_submission.py](scripts/audit_source_submission.py) to verify the resulting Python source DOCX. The script is read-only with respect to project source.

### 10. Validate formal documents

Run separate checks for:

- template fidelity;
- software name/version consistency;
- source-to-DOCX line equality;
- source counts and page counts;
- old software name and process-language removal;
- DOCX OpenXML integrity;
- PDF export and actual pages;
- first, middle, figure/table-heavy, boundary, and last-page visual rendering.

Do not mark a file ready when only file existence has been checked.

### 11. Produce the final bundle

Generate only the documents required by the user, normally following the fixed submission template:

- `<软件全称>-申请表信息.txt`;
- `<软件全称>_软件说明书.docx`;
- `<软件全称>_软件说明书.pdf`;
- `<软件全称>-源代码.docx`;
- `<软件全称>-源代码.pdf`;
- `<软件全称>_合作开发.docx` and `<软件全称>_合作开发.pdf` when `cooperation` is confirmed;
- template profile JSON;
- code selection/extraction manifest;
- document and source audit reports.

Keep temporary English filenames, conversion copies, old versions, and generated working files outside `正式资料/`. Copy verified formal artifacts to the requested delivery folder and compare hashes when files are not locked.

### 12. Final gate

Before recording `final-submission`, verify:

- one software name and version everywhere;
- owner order matches the cooperation agreement;
- cooperation agreement signing date is earlier than the expected/application completion date;
- application source amount equals actual source lines, excluding file markers;
- code page count equals the final PDF;
- manual layout matches the supplied template;
- formal documents contain no process narration;
- prior-registration files are not mixed into the current bundle.

Then return to the initial application-information draft, replace its provisional source amount and page count with the final verified values, and generate the final application TXT.

## Completion report

Report exact output paths, template used, documents generated, source file/line/page counts, visual pages checked, and pending user fields. State limitations explicitly. Never claim source code was fixed or developed by this skill.
