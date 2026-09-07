# Code Extraction And Format Standard

## Read-only requirement

This workflow never edits project source. It may read, hash, parse, import, compile-check, and compare source. When a problem is found, write it to the audit report and wait for the user.

## Selection categories

| Category | Default action |
| --- | --- |
| Registered product runtime source | Include |
| Genuine shipped public extension/API | Include after user confirmation |
| Operational CLI/report/export interface | Include when documented and usable |
| Tests, fixtures, demos, examples | Exclude |
| Documentation/build/material-generation scripts | Exclude |
| Application-form or manual helpers | Exclude |
| Research, paper, review, benchmark-only code | Exclude |
| Generated output, caches, dependencies | Exclude |

## Complete-file extraction

- Extract every selected file from line 1 through its final line.
- Preserve blank lines and comments already in the source.
- Do not extract only “lines 90–98” or other arbitrary fragments.
- Add one file marker before each file using a valid comment for that language.
- For Python use `# File: relative/path.py`; never use `// File:`.
- Place package initializers next to their substantive modules, not together on a filler page.

## Ordering

Prefer an order that helps a reviewer follow the software:

1. package entry and shared models;
2. schemas/configuration;
3. core business processing;
4. policy/security/validation;
5. adapters and controlled execution;
6. storage/audit/output;
7. user-facing or command entry.

Use the user's template order when it is explicitly required and technically coherent.

## Pagination

- Count one source or file-marker line as one material line.
- Use 50 material lines per full page.
- Keep continuous line numbers across file boundaries.
- Allow only the last page to contain fewer than 50 lines.
- If total material is under 60 pages, submit it completely.
- If total material reaches 60 pages, prepare continuous first 30 and last 30 pages from the confirmed sequence.
- Do not pad with comments, blank lines, helpers, tests, or examples.

## Code template format

Extract these properties from the supplied code template:

- paper size, margins, and orientation;
- header software name/version position and font;
- footer and page-number style;
- line-number width and separator spacing;
- code font family, size, color, and line spacing;
- paragraph spacing before/after;
- page-break method;
- visible line density and long-line wrapping behavior.

Keep all code text black. Do not add syntax colors, hyperlink styles, explanatory boxes, or a cover page unless the supplied template has them.

## Counts

Report separately:

- source file count;
- source line count, excluding added file markers;
- file-marker count;
- material line count;
- calculated and actual PDF pages.

The application form uses source line count, not material line count.

## Audit results

Check:

- all markers are unique;
- all selected paths resolve inside the project;
- DOCX payload equals the real files line for line;
- line numbers are continuous;
- no old software name or material-generation text remains;
- no wrong-language marker is used;
- calculated pages equal PDF pages;
- first, middle, file-boundary, and final pages render correctly.

Import/call analysis is advisory only. It helps classify public extensions versus isolated code. It must never modify the project.
