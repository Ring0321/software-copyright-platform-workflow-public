# Fixed Software Copyright Submission Template

Use this reference when `software-copyright-platform-workflow` prepares platform-ready software-copyright materials. The bundled template files live in `assets/fixed-submission-template/`:

- `manual.docx` and `manual.pdf`: software manual template.
- `source-code.docx` and `source-code.pdf`: source-code material template.
- `application-info.txt`: application-information TXT field-order template.
- `cooperation-agreement.docx` and `cooperation-agreement.pdf`: cooperation-development agreement template; read [cooperation-development-gate.md](cooperation-development-gate.md) before using it.

Original evidence inspected from `D:/芯珩科技/软著申报/陕北农特产品展销服务平台 V1.0/陕北农特产品展销服务平台 V1.0_最终提交材料/`:

- Manual DOCX SHA-256 prefix: `1b8322ee015d34b9`; manual PDF SHA-256 prefix: `47b0550aca380f32`; PDF pages: 43.
- Source-code DOCX SHA-256 prefix: `e7c8ae18cf474bbd`; source-code PDF SHA-256 prefix: `0f0413366b873a9a`; PDF pages: 60.
- Application TXT SHA-256 prefix: `892346be483361bd`; field lines: 25.
- Cooperation agreement DOCX SHA-256 prefix: `111111fc3f41ed88`; cooperation agreement PDF SHA-256 prefix: `5c49a55c7b63e65c`; PDF pages: 2.

## Authority boundary

- Treat these files as the fixed formatting and submission-shape authority.
- Exactness requirement: generate new materials by cloning the bundled template assets' formatting, not by approximating from the prose summary below. Preserve the same document family, page setup, margins, header/footer behavior, typography, heading hierarchy, field order, code line density, page-number style, table/figure positioning, and final filename pattern. The prose measurements below are a checklist for verification; when the prose and asset conflict, re-inspect the asset and follow the asset.
- Never copy the old software name, rights holders, product functions, domain facts, dates, hardware, code, screenshots, or business claims into a new project unless the user explicitly says the new project is the same software.
- The current project, user-confirmed fields, and verified source boundary remain the content authority.
- If a user supplies a newer replacement template, record the `template` gate and use the replacement only after explicit confirmation.

## Final bundle shape

Generate the final delivery folder with this file naming pattern:

- `<软件全称>_软件说明书.docx`
- `<软件全称>_软件说明书.pdf`
- `<软件全称>-源代码.docx`
- `<软件全称>-源代码.pdf`
- `<软件全称>-申请表信息.txt`
- `<软件全称>_合作开发.docx` and `<软件全称>_合作开发.pdf` only when cooperation development is confirmed.

Keep working drafts, temporary conversion files, JSON profiles, and audit reports outside the final delivery folder unless the user asks to include them.

## Application information TXT

Create a plain UTF-8 TXT file. Use exactly one `字段：值` line per field, no Markdown table, and preserve this order:

1. 软件全称
2. 软件简称
3. 版本号
4. 软件分类
5. 开发完成日期
6. 开发方式
7. 软件说明
8. 发表状态
9. 首次发表日期
10. 著作权人
11. 权利范围
12. 权利取得方式
13. 开发的硬件环境
14. 运行的硬件环境
15. 开发该软件的操作系统
16. 软件开发环境 / 开发工具
17. 该软件的运行平台 / 操作系统
18. 软件运行支撑环境 / 支持软件
19. 编程语言
20. 源程序量
21. 开发目的
22. 面向领域 / 行业
23. 软件的主要功能
24. 软件的技术特点
25. 页数

`源程序量` must be the verified source-line count used for the submitted code material, excluding inserted file-marker lines if they are not part of the original source. `页数` must match the final source-code PDF page count. If `发表状态` is `未发表`, leave `首次发表日期` blank unless the user gives a date.

## Software manual template

Page and header/footer:

- A4 portrait, about `21.0 × 29.7 cm`.
- Margins: top `2.2 cm`, bottom `2.0 cm`, left `2.5 cm`, right `2.2 cm`.
- Header distance and footer distance: about `1.2 cm`.
- Header text: `<软件全称> <版本号>`.
- Footer: `第 <页码> 页`.

Cover and text style:

- Cover page: centered software title/version, centered `软件说明书`, centered rights-holder line.
- Cover title and subtitle follow the template's large bold centered style, approximately 26 pt.
- Rights-holder line follows the template's centered Chinese body style, approximately 20 pt.
- Main body text uses continuous paragraphs, approximately 12 pt, first-line indent about `0.85 cm`.
- First-level headings use Chinese numerals such as `一、概述`, approximately 16 pt bold.
- Second-level headings use Arabic chapter numbering such as `1.1 系统背景`, approximately 14 pt bold.
- Third-level headings may be used sparingly for dense operation chapters, such as `6.11.1 查询商品`.
- Use black text. Do not add colored hyperlinks, process notes, or visible drafting instructions.

Required manual order:

1. Cover.
2. Directory / table of contents.
3. 一、概述
   - 1.1 系统背景
   - 1.2 系统价值
   - 1.3 适用范围
   - 1.4 术语定义
4. 二、软件概述
   - 软件名称和版本
   - 软件定位
   - 设计目标
   - 软件组成结构
   - 软件特点
5. 三、运行环境
   - 硬件环境
   - 软件环境
   - 目录环境
   - 运行边界
6. 四、总体架构
   - 架构设计原则
   - 系统总体架构
   - 数据流转关系
   - 前端页面架构
   - 后端与数据架构
7. 五、系统功能说明
   - Write one section per verified core user-facing or management function.
8. 六、系统操作说明
   - Start with 操作准备.
   - Then write operation sections in the real user-flow order.
   - Use third-level headings only when one operation module is too broad and the template benefits from internal steps.
9. 七、数据与输出说明
   - Cover important data categories, user-visible outputs, management outputs, storage/backup, interfaces or response states only when evidenced by the current project.
10. 八、安全与数据一致性说明
    - Cover authentication, input validation, transaction/data consistency, history snapshots, reference constraints, runtime boundaries, and other verified safeguards.
11. 九、异常处理与维护说明
    - Cover runtime, data loading, cart/order, login/session, management maintenance, backup, testing, and version maintenance issues that match the project.
12. 十、系统特点
    - Summarize concrete project-specific characteristics, not generic praise.
13. 十一、使用注意事项
    - Cover operational cautions that a real user/admin would need.
14. 十二、总结
    - Summarize actual software scope and boundary.

Tables and figures:

- The manual template is table-heavy in early explanatory chapters and uses figures in architecture, operation, data-relationship, and exception-flow sections.
- Use tables for scope/object/result, term definitions, software name/version, composition, environment, directory, architecture layers, page groups, and function/data mappings when applicable.
- Use figure captions in the form `图 X-X <标题>`.
- The inspected template contains architecture/data-flow/module figures, operation screenshots, a data relationship figure, and an exception recovery figure. Keep comparable figure positions when evidence exists.
- If real screenshots or diagrams are deferred, reserve a neutral figure area and formal caption, but do not write `截图占位`, `待插入`, `软著材料`, or other process language in the formal document.

Writing rules:

- Match the template's formal explanatory density: each subsection normally contains one to three specific paragraphs or a table plus explanatory text.
- Use current-project nouns, page names, routes, controls, inputs, validation, outputs, and exceptions.
- Do not write marketing slogans or vague claims such as “一站式、智能化、高效便捷” unless they are directly supported and necessary.
- Do not explain implementation internals in user-operation sections unless the template section is specifically about data, architecture, or consistency.

## Source-code material template

Page and header/footer:

- Letter portrait, about `21.59 × 27.94 cm`.
- Margins: top `2.54 cm`, bottom `2.54 cm`, left `1.91 cm`, right `1.91 cm`.
- Header distance and footer distance: about `2.0 cm`.
- Header text: `<软件全称> <版本号>`.
- Footer: `第 <页码> 页`.

Body style:

- No cover page, no table of contents, no tables, no screenshots.
- Black plain code text, approximately 9 pt, Times New Roman-compatible font.
- One visible line-number prefix per material line.
- Preserve natural blank lines from source.
- Add one language-valid file marker before each complete file, such as `// File: path`, `# File: path`, or `<!-- File: path -->`.
- Do not add syntax highlighting, hyperlinks, fake comments, artificial padding, or generated code.

Source page rule:

- The fixed template's final source material is one combined file named `<软件全称>-源代码.docx/pdf`.
- If the confirmed submitted source is under 60 pages, generate one complete source document ending naturally.
- If the confirmed submitted source reaches 60 pages or more, generate one 60-page source document by placing the first 30 pages and the last 30 pages into the same `-源代码` DOCX/PDF. Do not create two separate `前30页` and `后30页` files unless the user explicitly asks for that alternate package.
- Keep source order by confirmed product/module sequence and keep line numbering traceable to the assembled material.

Validation:

- Verify source-to-DOCX line equality from selected complete files.
- Verify final source PDF page count and record it into `申请表信息.txt` field 25.
- Verify the final source line count and record it into `申请表信息.txt` field 20.
- Visually check first page, page 30/31 boundary when 60 pages are generated, and last page.
