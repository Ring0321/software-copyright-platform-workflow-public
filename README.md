# Software Copyright Platform Workflow

> 面向中国软件著作权材料准备的 Codex 技能：从代码边界确认、合作开发日期校验、模板化文档生成，到最终提交包核检的一整套安全工作流。  
> A safety-first Codex skill for Chinese software copyright filing materials.

![Status](https://img.shields.io/badge/status-public%20safe%20edition-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Safety](https://img.shields.io/badge/safety-no%20private%20templates%20bundled-orange)

很多软著材料不是“写不出来”，而是输在细节：申请表源程序量对不上、合作协议日期反了、旧项目名称残留、源码里混入配置文件、说明书像宣传稿、最终包看起来齐全但内部互相矛盾。

`software-copyright-platform-workflow` 解决的就是这些麻烦。它把软著材料准备变成一个可记录、可复核、可追溯的流程，让 AI 不能随便编、不能跳过门禁、不能把私密信息带进提交包。

本仓库是“开源安全版”：包含工作流规则、参考标准和辅助脚本；不包含真实身份证号、客户项目、签字文件或私有 DOCX/PDF 模板。

## 项目亮点

- **门禁式流程**：先确认代码来源、合作开发、登记边界、模板来源，再进入正式材料生成。
- **真实源码边界**：只从已确认项目中抽取真实源文件，不为凑页数编造代码。
- **合作开发校验**：统一著作权人顺序、身份证字段、开发完成日期和协议签订日期。
- **固定模板复刻**：以用户提供的 DOCX/PDF/TXT 模板为格式权威，避免随手套版。
- **源码提交规则**：排除依赖、缓存、构建产物、测试、文档和私有配置；记录路径、行数、哈希和选择理由。
- **最终一致性核检**：检查软件名、版本号、源程序量、页数、旧名称残留、过程性措辞和包内文件齐套性。
- **隐私优先**：开源版不携带真实模板；本地私有模板默认被 `.gitignore` 排除。

## 适合谁

- 经常为项目、比赛、课程、企业系统准备软著材料的人；
- 想让 Codex/Agent 帮忙写软著，但担心它瞎编字段或混入敏感信息的人；
- 需要批量整理申请表、说明书、源码材料、合作开发协议的人；
- 希望把软著材料准备流程标准化、可复查、可交接的团队。

## 仓库结构

```text
.
├── SKILL.md                         # Codex 技能主规则
├── agents/
│   └── openai.yaml                  # Agent 元数据
├── assets/
│   └── fixed-submission-template/   # 本地私有模板目录，真实模板不随仓库公开
├── references/                      # 字段、模板、源码、合作开发等参考规则
├── scripts/                         # 门禁记录与模板/源码检查脚本
├── README.md
├── LICENSE
└── .gitignore
```

## 它会生成什么

每个软件建议使用独立日期目录，避免混入旧材料：

```text
<软件slug>_软著材料_<YYYYMMDD>/
├── 草稿/
├── 模板规格/
├── PlantUML/
├── 截图/
├── 正式资料/
└── 核检报告/
```

常见正式资料包括：

- `<软件全称>-申请表信息.txt`
- `<软件全称>_软件说明书.docx`
- `<软件全称>_软件说明书.pdf`
- `<软件全称>-源代码.docx`
- `<软件全称>-源代码.pdf`
- `<软件全称>_合作开发.docx`
- `<软件全称>_合作开发.pdf`

## 快速开始

克隆仓库：

```bash
git clone https://github.com/Ring0321/software-copyright-platform-workflow-public.git
cd software-copyright-platform-workflow-public
```

复制到 Codex 技能目录：

```bash
mkdir -p ~/.codex/skills/software-copyright-platform-workflow
cp -R ./* ~/.codex/skills/software-copyright-platform-workflow/
```

在本地加入你自己的私有模板：

```text
assets/fixed-submission-template/
├── application-info.txt
├── manual.docx
├── manual.pdf
├── source-code.docx
├── source-code.pdf
├── cooperation-agreement.docx
└── cooperation-agreement.pdf
```

这些真实模板会被 `.gitignore` 排除。不要把包含个人身份信息、签名、客户名称、旧软件名称或平台专用内容的模板提交到公开仓库。

## 推荐工作流

### 1. 确认代码来源

必须先确认本次软著使用哪一种代码来源：

- `new-code`：自主编写代码；
- `rewrite-code`：重新编写代码；
- `existing-project`：读取已有项目代码。

如果选择新写或重写，材料流程会停止，直到真实代码已经产生并通过确认。

### 2. 确认是否合作开发

如果是合作开发，需要确认：

- 合作开发人姓名与最终著作权人顺序；
- 每位合作开发人的证件号码字段；
- 预计/实际开发完成日期；
- 合作开发协议签订日期；
- 协议签订日期必须早于开发完成日期。

### 3. 确认登记边界

区分：

- 首次独立登记；
- 版本升级登记；
- 继承或混合代码边界。

旧登记材料只能作为格式参考，不能自动成为当前软件内容来源。

### 4. 编写申请表信息

保留申请表字段顺序和字段口径。源程序量、源码页数等计算字段，应在源码材料最终生成后回填。

### 5. 提取模板规格

从用户本地私有模板中提取：

- 页面尺寸、方向、页边距；
- 页眉、页脚、页码；
- 标题层级、字体、字号、间距；
- 表格边框、底纹、列宽；
- 图片位置和图题；
- 源码页每页行数、字体和分页规则。

### 6. 抽取源码

只选择：

- 产品运行源码；
- 真实对外交付接口或运维入口。

排除：

- `node_modules/`、`dist/`、`build/`、缓存；
- 测试、示例、说明文档；
- 环境变量、私有配置、密钥文件；
- 材料生成脚本和无关研究代码。

### 7. 生成正式材料

生成申请表 TXT、说明书 DOCX/PDF、源码 DOCX/PDF，以及合作开发协议 DOCX/PDF。

### 8. 最终核检

正式交付前至少检查：

- 软件名称和版本号是否全包一致；
- 著作权人顺序是否和合作协议一致；
- 协议签订日期是否早于开发完成日期；
- 申请表源程序量是否等于实际源码行数；
- 申请表页数是否等于源码 PDF 页数；
- 说明书是否残留旧项目名或“待插入”等过程性文字；
- 源码材料是否含配置凭据、冲突标记或不合法文件标记；
- 当前登记材料是否混入旧登记文件。

## 设计原则

这个技能有点“保守”，但这是故意的：

- 不修改项目源码；
- 不替用户编造身份字段；
- 不为了凑满 60 页制造假代码；
- 不把旧软著内容当作新项目事实；
- 不把私有模板、身份证号、签名文件放进开源仓库；
- 不用“看起来差不多”替代模板复核；
- 不把 AI 输出当最终法律判断。

如果一个字段缺失，它会标记为待确认；如果一个模板无法复刻，它会报告差异；如果源码里有风险，它会停下来提醒。慢一点，但更稳。

## 脚本说明

### `scripts/record_gate.py`

记录工作流关键门禁，例如：

- `code-source-strategy`
- `cooperation-development`
- `registration-scope`
- `template`
- `final-submission`

### `scripts/inspect_docx_template.py`

检查 DOCX 模板结构，包括页面、段落、表格、页眉、页脚和样式。

### `scripts/audit_source_submission.py`

核查源码提交材料是否符合已选源文件、行数和格式规则。

## 开源版限制

克隆本仓库后不能直接当成完整提交工厂使用，因为真实 DOCX/PDF 模板被刻意移除了。正式生成前，请先在本地加入你自己的模板，并确认模板不包含不应公开的信息。

如果你需要携带真实模板、签名文件或客户材料，请保留在私有仓库或本地目录中。

## Roadmap

- [ ] 增加脱敏版 DOCX/PDF 示例模板；
- [ ] 增加跨平台安装脚本；
- [ ] 增加更细的最终核检报告；
- [ ] 增加可选的运行截图采集流程；
- [ ] 增加 CI 检查 references 和 helper scripts。

## License

MIT License. 你可以自由使用、修改和分发本工作流，但需要自行保护私有模板、身份字段和客户项目内容。
