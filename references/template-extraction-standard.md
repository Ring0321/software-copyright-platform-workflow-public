# Template Extraction Standard

## Source priority

Use the user's files in this order:

1. editable DOCX template;
2. matching PDF for visual confirmation;
3. screenshots for isolated visual details.

When DOCX and PDF differ, ask which is authoritative before formal generation.

## Template profile

Create one JSON profile per template containing:

- source path, size, hash, paragraph/table/section counts;
- section page dimensions, orientation, margins, header/footer distances;
- header/footer text and alignment;
- style IDs and names used by the document;
- font name, size, bold/italic, and color;
- paragraph alignment, first-line indent, left/right indent, spacing, and line spacing;
- table styles, dimensions, column widths, cell shading, borders, and margins;
- page-break and section-break locations;
- figure/caption paragraphs and image dimensions;
- code-line format when the document is a source template.

Use `scripts/inspect_docx_template.py` for deterministic properties, then add visual observations after rendering.

## Reproduction rules

- Create a new output document; never rewrite the user's original template.
- Copy measured layout properties rather than approximating them.
- Reuse style hierarchy and numbering.
- Replace old software name/version in headers, cover, captions, and filenames.
- Keep body text black unless the template intentionally uses colored headings.
- Preserve table geometry and caption placement.
- Match paragraph density; do not create sparse pages that merely imitate chapter names.

## Visual verification

Render at least:

- cover or first page;
- first normal body page;
- a heading transition page;
- a table-heavy page;
- a figure-heavy page;
- middle page;
- final page.

Compare margins, header baseline, title position, body line length, table width, caption spacing, and page balance.
