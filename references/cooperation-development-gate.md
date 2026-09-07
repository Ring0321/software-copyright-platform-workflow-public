# Cooperation Development Gate

Use this reference near the beginning of the workflow, after `code-source-strategy` and before drafting application information. The purpose is to decide whether the filing uses a cooperation-development agreement and to prevent the agreement, application fields, and rights-holder list from drifting apart.

## Gate question

Ask the user to confirm one of these choices:

1. `cooperation`: 合作开发，需要生成合作开发书。
2. `not-cooperation`: 非合作开发，不生成合作开发书.
3. `undecided`: 尚未确定，stop and wait before preparing formal materials.

Do not infer cooperation only because multiple people are listed. The user must confirm the development method.

## Required information when `cooperation`

Collect and confirm all of the following before generating the formal cooperation agreement:

- 合作开发人：all participant names, in the exact order to appear in the agreement and in the application rights-holder field.
- 身份证号：one ID number for each cooperation developer. Never invent or normalize missing ID numbers. If any ID number is missing, keep the field pending and stop before formal generation.
- 预计开发完成日期：the date to write in the agreement, formatted as `YYYY-MM-DD` in internal records and as `YYYY 年 M 月 D 日` in the agreement.
- 合作开发书签署日期：the date to write after `签订日期`, formatted as `YYYY-MM-DD` in internal records and as `YYYY 年 M 月 D 日` in the agreement.

Validation rule: the cooperation agreement signing date must be earlier than the expected development completion date. If the signing date is the same day as, or later than, the completion date, stop and ask the user to correct one of the dates.

## Consistency rules

- If `cooperation` is confirmed, set `开发方式：合作开发` in `申请表信息.md` and `申请表信息.txt`.
- The `著作权人` field must include the same cooperation developers in the same order as the agreement, unless the user explicitly explains a legally different ownership arrangement.
- The agreement's software full name and version must match the confirmed application fields and the manual/source-code headers.
- The agreement's expected development completion date must match the application `开发完成日期` unless the user explicitly says they are different and gives a reason. Record the reason in the audit report.
- Do not include personal ID numbers in the final chat summary unless the user asks. Store them only in the generated agreement/draft fields and local audit materials required for the filing workflow.

## Draft confirmation files

Before application-information drafting, generate these files in the isolated package:

- `草稿/合作开发确认.md`
- `草稿/合作开发确认.json`

Generate them for every run, including `not-cooperation`, so the decision is auditable. The files must record:

- `development_method_choice`: `cooperation`, `not-cooperation`, or `undecided`.
- `cooperation_developers`: ordered list of names and ID numbers when cooperation is confirmed; empty list when not cooperation.
- `expected_completion_date`: `YYYY-MM-DD` or pending.
- `agreement_signing_date`: `YYYY-MM-DD` or pending.
- `date_rule`: signing date must be earlier than expected completion date.
- `date_rule_status`: `pass`, `fail`, or `pending`.
- `application_field_effect`: how fields `开发方式`, `开发完成日期`, and `著作权人` should be filled.
- `pending_fields`: missing names, ID numbers, dates, or user decisions.

Do not proceed to formal agreement generation unless `date_rule_status` is `pass` and no required cooperation fields are pending.

## Cooperation agreement template

Use these bundled fixed template assets:

- `assets/fixed-submission-template/cooperation-agreement.docx`
- `assets/fixed-submission-template/cooperation-agreement.pdf`

Template characteristics inspected from the supplied agreement:

- Final filename pattern: `<软件全称>_合作开发.docx` and `<软件全称>_合作开发.pdf`.
- Page size: Letter portrait, about `21.59 × 27.94 cm`.
- Margins: top `2.2 cm`, bottom `2.0 cm`, left `2.3 cm`, right `2.3 cm`.
- Footer: `第 <页码> 页`; no header text.
- Title: centered `软件合作开发协议`, Songti, about 18 pt, bold.
- Body: Songti, about 12 pt, black text.
- Opening block: `合作全体人员：`, followed by one line per participant: `姓名：<姓名>  身份证号：<身份证号>`.
- Main clauses:
  1. `一、全体人员共同合作开发软件`
  2. `二、著作权归属`
  3. `三、权利约定`
  4. `四、其他约定`
- Signature block: centered `全体人员签字：`, followed by a two-column table `姓名 | 签字`, one row per cooperation developer.
- Ending date line: right-aligned `签订日期：YYYY 年 M 月 D 日`.

## Formal output behavior

- Generate the cooperation agreement only when `cooperation` is confirmed.
- Do not generate the agreement for `not-cooperation`; leave it out of the final bundle.
- If cooperation is confirmed but any required person/ID/date field is missing, produce drafts only and mark the formal agreement as pending.
- Export both DOCX and PDF for the final bundle and visually check every page because the agreement is short.
