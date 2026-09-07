# Application Fields And Bundle

## Application fields

Generate the initial application-information draft before rewriting the manual or building the code document. This preserves the original `software-copyright-materials` workflow. Read the base skill's `references/application_fields.md` as the authoritative detailed rule set.

Keep the following 25 fields in this exact order:

1. 软件全称。
2. 软件简称（可选）。
3. 版本号。
4. 软件分类（应用软件、嵌入式软件、中间件、系统软件或其他）。
5. 开发完成日期。
6. 开发方式（单独开发、合作开发、委托开发或下达任务开发）。
7. 软件说明（原创或修改）。
8. 发表状态（已发表或未发表）。
9. 首次发表日期（仅已发表时填写）。
10. 著作权人，包括国家、省市、主体类型、姓名、证件类型和证件号。
11. 权利范围（全部权利或部分权利）。
12. 权利取得方式（原始取得或继受取得）。
13. 开发的硬件环境（不超过 50 字符）。
14. 运行的硬件环境（不超过 50 字符）。
15. 开发该软件的操作系统（不超过 50 字符）。
16. 软件开发环境 / 开发工具（不超过 50 字符）。
17. 软件运行平台或操作系统（不超过 50 字符）。
18. 软件运行支撑环境或支持软件（不超过 50 字符）。
19. 编程语言（平台预设选项加自定义输入，自定义内容不超过 120 字符）。
20. 源程序量（纯数字，指登记软件全部源程序总行数）。
21. 开发目的（不超过 50 字符）。
22. 面向领域或行业（不超过 50 字符）。
23. 软件的主要功能（500 至 1300 字符）。
24. 软件的技术特点（平台标签加不超过 100 字符的文本描述）。
25. 页数（代码鉴别材料实际页数）。

Use `YYYY-MM-DD`. For unpublished software, keep first-publication date empty. Do not convert pending identity information into invented values. Hardware and operating-system fields require user confirmation. The source amount is not the number of displayed material lines and must not include inserted file markers.

Before finalizing fields 5, 6, and 10, read [cooperation-development-gate.md](cooperation-development-gate.md). If cooperation development is confirmed, field 6 must be `合作开发`, field 10 must follow the confirmed cooperation-developer order, and the application completion date must match the expected completion date used in the cooperation agreement unless the user explicitly records a reason. If cooperation development is not confirmed, do not generate a cooperation agreement.

The initial Markdown should be a complete platform-entry worksheet, not merely a prose summary. For each field include the confirmed value or a visible `待补充/待确认` status and, where useful, the project evidence or length check. The final TXT should contain clean field-value pairs suitable for platform entry and omit drafting commentary.

## Two-pass count handling

Use two passes for calculated code fields:

1. Initial application draft: write source amount and code pages as provisional or pending when final code selection is not complete.
2. Final application TXT: after source extraction, DOCX/PDF pagination, and audit, write the verified source-line count and actual PDF pages.

Do not alter already confirmed owner, date, environment, purpose, or publication fields during the second pass unless the user explicitly changes them.

## Consistency matrix

Verify the same values across:

- platform form/TXT;
- manual cover, header, body, and filename;
- source-code header and filename;
- cooperation agreement when `cooperation-development` confirms cooperation;
- final bundle audit report.

## Bundle rules

- Create a new dated bundle for each iteration.
- Keep `草稿`, `正式资料`, and `核检报告` separate.
- Keep PlantUML and screenshots outside `正式资料` unless the user explicitly wants them delivered.
- `正式资料` should contain only final Chinese-named artifacts.
- Remove `source_code_submit.docx`, temporary ASCII conversion copies, and old duplicate versions after validation.
- When copying to a delivery folder, verify the resolved destination and compare SHA-256 hashes when files are not locked.

## Completion status

Use one of these exact statuses:

- `DRAFT`: content or user fields remain unconfirmed.
- `DOCX_READY`: DOCX validated; PDF not yet verified.
- `PLATFORM_READY`: application fields, source fidelity, DOCX/PDF, page count, and visual checks all pass.
- `BLOCKED`: mandatory user data or external tooling prevents completion.
