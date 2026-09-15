# Manual And Template Standard

## Template extraction

Inspect the supplied reference DOCX rather than approximating it. Record:

- page dimensions and margins;
- header/footer distances and text;
- title hierarchy, numbering, colors, and fonts;
- body font, first-line indent, line spacing, and paragraph spacing;
- table widths, borders, shading, and cell margins;
- caption style and figure placement;
- section breaks, page breaks, and total page density.

Generate a new DOCX from those measured properties. Do not edit the previous registration in place.

## Direct-submission language

Formal manuals describe the product, not the writing process. Ban phrases such as:

- “本说明书中凡涉及正式软件名称”；
- “正式提交前”；
- “软著材料” or “申请表字段”；
- “截图预留” or “请在此处插入”；
- “审核员” or “后续替换”；
- absolute production-security guarantees unsupported by evidence.

Replace them with normal product descriptions, figure titles, and tested operational boundaries.

## Manual structure

Follow the supplied template's actual chapter count, numbering hierarchy, and order. Do not force a universal chapter list onto the document.

Map every template chapter to current-project evidence before drafting. If a template chapter has no current-project counterpart, ask the user whether to omit, rename, or replace it. If the current software requires an additional chapter, add it only after user confirmation and format it with the nearest matching template style.

Write each subsection with project-specific behavior, inputs, decisions, outputs, and failure handling. Do not create many headings with one-sentence bodies merely to imitate the template's table of contents.

The final software manual PDF must be at least 40 pages. This is a content requirement, not a layout trick. If the generated PDF is shorter, return to the Markdown draft and expand genuine project content: role permissions, entry paths, preconditions, field and button meanings, status definitions, step-by-step user actions, validation rules, exception handling, system feedback, downstream workflow effects, maintenance operations, reports, and screenshots. Do not use blank pages, duplicated paragraphs, enlarged spacing, oversized screenshots, or invented functionality to reach 40 pages.

Every operation chapter must be written so a first-time business user can reproduce the workflow. For each page or workflow, cover:

- applicable role and permission boundary;
- where the page is entered from;
- prerequisites such as account, material, payment status, task status, or configuration state;
- visible fields, buttons, tabs, filters, lists, status labels, and result areas;
- each user action in order, including what to click, fill, select, confirm, save, submit, review, download, or archive;
- field constraints, permission limits, state limits, and common validation prompts;
- success feedback, failure feedback, exception handling, and how to recover;
- the result's downstream effect on review, rectification, signing, reporting, archiving, or audit trail.

## Tables

Manual tables must be black three-line tables unless the user-confirmed template explicitly requires a different style:

- top border across the table;
- bottom border below the header row;
- bottom border across the table;
- no background fill;
- no vertical borders;
- no internal horizontal borders between body rows.

Use three-line tables for related documents, system requirements, field definitions, button meanings, status meanings, permission matrices, exception handling, report outputs, and glossary entries. If a generator cannot produce three-line tables, stop and report the limitation instead of delivering grid tables.

## Figures and screenshots

- Use PlantUML for architecture, module relations, authorization events, exception handling, and file structures.
- Keep diagrams vertical or moderately wide for portrait Word pages.
- Store `.puml` source beside rendered images.
- Use real screenshots for operational chapters when possible.
- If screenshots are deferred, keep neutral blank figure space and a formal caption; do not display drafting instructions.

## Validation

- Search banned phrases in DOCX XML and extracted PDF text.
- Confirm the old software name never appears as the current product.
- Confirm the final manual PDF has at least 40 pages and that pages contain genuine content rather than blanks, duplicated filler, or inflated screenshots.
- Render representative table pages and confirm tables use black three-line formatting.
- Render first, middle, figure-heavy, table-heavy, and last pages.
- Verify no text overlaps, orphan captions, empty oversized boxes, colored body text, or broken headers.
