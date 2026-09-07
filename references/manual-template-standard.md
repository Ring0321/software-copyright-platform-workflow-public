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

## Figures and screenshots

- Use PlantUML for architecture, module relations, authorization events, exception handling, and file structures.
- Keep diagrams vertical or moderately wide for portrait Word pages.
- Store `.puml` source beside rendered images.
- Use real screenshots for operational chapters when possible.
- If screenshots are deferred, keep neutral blank figure space and a formal caption; do not display drafting instructions.

## Validation

- Search banned phrases in DOCX XML and extracted PDF text.
- Confirm the old software name never appears as the current product.
- Render first, middle, figure-heavy, table-heavy, and last pages.
- Verify no text overlaps, orphan captions, empty oversized boxes, colored body text, or broken headers.
