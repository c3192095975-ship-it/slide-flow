---
name: slide-flow
description: Orchestrate presentation and slide-deck production without conflicting PPT skills. Use for creating, editing, converting, reviewing, or exporting decks, slides, PPT/PPTX, PowerPoint, Google Slides, HTML slides, image-based slides, or presentation narratives. Triage first; select output mode, deck profile, quality tier, and source mode; then build story, content, visual direction, production, render QA, accessibility, and delivery with one primary skill per stage. Prefer the official `Presentations` skill for Spaces/PowerPoint/Google Slides when available, `template-creator` for reusable templates, and `documents`/`pdf` only as verification or delivery support. Do not use for ordinary document writing or isolated image generation without a slide/deck context.
metadata:
  version: "1.1.0"
  short-description: Orchestrate PPT skills by output mode and stage
---

# Slide Flow v1.1

本 skill 是演示文稿任务的唯一编排入口。它不替代具体 PPT 制作 skill，而负责决定：输出形态、演示类型、质量标准、当前阶段、唯一主技能和渲染验收。

## 1. 强制规则

1. 实际 PPT 任务先进入 Slide Flow，再选择具体 PPT skill。
2. **先选输出形态**：可编辑 PPTX、图片型 PPT、HTML deck、模板编辑或图片还原。
3. 同一阶段只能有一个主技能。
4. 同一轮最多加载 3 个 skill，且不能有两个 skill 负责同一职责。
5. 先故事线，再视觉和生产；不能先做漂亮页面再补内容。
6. 可编辑 PPTX、图片型 PPT 和 HTML deck 不能互相冒充。
7. 每页只表达一个核心信息；标题应能单独讲出整套故事。
8. 生产后必须渲染或视觉检查；生成成功不等于版式合格。
9. 不伪造数据、图表、引用、品牌素材或模板要求。
10. 人类作者/演讲者确认最终内容和文件。
11. 不自动修改其他 skill 的源文件。
12. 可执行检查优先于模型自述；但视觉审美和最终演讲适配仍由人判断。
13. 原生演示文件优先考虑官方 `Presentations` skill；从零生成原生 PPTX 时再考虑 `slide-maker`、`ppt-master` 或 `pptx`。
14. `template-creator` 只负责模板能力，不自动成为 deck 主生产器；`documents`/`pdf` 只做渲染、导出或验证辅助。
15. `univer-cli` 只在目标是 `.univer` / Univer Slides 时启用，不能用来冒充 PowerPoint 原生 PPTX。

以下任务不进入 Slide Flow：普通文档写作、普通图片生成、单个图标或单张配图，没有幻灯片或演示语境的普通视觉任务。

## 2. 启动协议

1. **DETECT**：判断是否为真实 PPT/演示任务。
2. **TRIAGE**：选择 `BYPASS`、`LIGHT` 或 `FULL`。
3. **DISCOVER**：FULL 模式发现当前已安装的 PPT 能力；LIGHT 只确认一个主能力。
4. **OUTPUT MODE**：选择最终输出形态。
5. **DECK PROFILE**：选择学术、答辩、路演、咨询、培训、产品发布或社交 deck。
6. **QUALITY TIER**：选择 draft、presentation_ready、executive_ready 或 publish_ready。
7. **SOURCE MODE**：从主题、文档、论文、模板、URL、已有 PPTX、截图还是混合材料开始。
8. **PHASE**：锁定当前阶段和前置工件。
9. **RESOLVE**：解析一个主技能和一个可选辅助技能。
10. **EXECUTE**：只执行当前阶段。
11. **GATE**：执行故事、内容、视觉、渲染和技术检查。
12. **HANDOFF**：输出文件、状态、未解决问题和下一阶段。

开始时输出：

`SlideFlow：模式=…；输出=…；profile=…；tier=…；阶段=…；主技能=…；辅助技能=…`

## 3. 任务分级

### BYPASS

适用于：

- 只改一页文字；
- 只改颜色、字号或一处版式；
- 只提取 PPT 文本；
- 只生成一张不含演示逻辑的配图；
- 用户明确只做很小的单步操作。

行为：直接使用一个基础能力，不建立完整 deck 项目。

### LIGHT

适用于：

- 现有 PPTX 转 PDF；
- 单页重排；
- 单套模板套用；
- 图片 PPT 转可编辑 PPTX；
- 只做一次大纲或故事线；
- 只做一次视觉 QA。

行为：

- 一个主能力；
- 必要时一个辅助能力；
- 不建立完整页面生产流水线。

### FULL

适用于：

- 从主题/文档/论文生成完整 deck；
- 需要故事线、视觉系统和多页生产；
- 需要模板匹配和品牌一致性；
- 需要 PDF/HTML/PPTX 多格式交付；
- 需要渲染、视觉检查和可编辑性验收。

行为：

- 建立完整能力图；
- 锁定输出形态、profile、tier 和 source mode；
- 先故事线，再生产；
- 逐阶段渲染和 QA。

## 4. 输出形态

| 输出模式 | 适用 | 默认候选 |
|---|---|---|
| `editable_pptx` | 需要后续编辑、公司/学校汇报 | `Presentations`（Spaces/PPTX/Google Slides）、`slide-maker`、`pptx`、`hands-on-deck`、`ppt-master` |
| `image_deck` | 高视觉冲击、图片型 PPT、社交传播 | `gpt-image2-ppt`、`baoyu-slide-deck`、Gorden 系列 |
| `html_deck` | 网页演示、发布会、分享会 | `html-ppt`、`guizang-ppt-skill`、`dashi-ppt` |
| `template_edit` | 已有大学/公司模板 | `template-creator`、`thesis-defense-pptx`、`image-to-editable-ppt`、`html-to-editable-pptx` |
| `image_to_editable` | 截图或图片型 PPT 还原 | `GordenImage2PPTX`、`image-to-editable-ppt`、`nature-image2ppt` |
| `hybrid_delivery` | 明确要求图片版 + 可编辑版 | 只有用户明确要求时启用双交付 |

一次任务只能有一个主输出模式。  
`hybrid_delivery` 需明确两个产物和各自验收标准。

## 5. Deck profiles

| Profile | 用途 | 默认重点 |
|---|---|---|
| `academic_talk` | 组会、会议、论文汇报 | 研究问题、证据、图表、限制 |
| `thesis_defense` | 开题、预答辩、毕业答辩 | 贡献、方法、结果、创新、问答准备 |
| `pitch` | 融资、竞赛、路演 | 问题、方案、市场、证据、团队、行动 |
| `consulting` | 管理咨询、战略汇报 | 结论先行、结构化论证、行动建议 |
| `training` | 教学、培训、课程 | 学习目标、步骤、例子、练习 |
| `product_launch` | 产品发布、市场推广 | 用户价值、差异化、视觉锚点 |
| `social_deck` | 小红书/社交图文 | 封面钩子、信息节奏、可分享性 |
| `business_review` | 周报、月报、项目汇报 | 目标、进展、风险、决策请求 |
| `template_deck` | 指定模板/学校/公司格式 | 母版、版式、品牌和格式一致性 |

详细 profile 规则见 `references/deck-profiles.md`。

## 6. Quality tiers

| Tier | 目标 |
|---|---|
| `draft` | 先看结构和内容 |
| `presentation_ready` | 可以直接上台讲 |
| `executive_ready` | 高层/客户/答辩级质量 |
| `publish_ready` | 可发布、可分享、可归档 |

提高 tier 会加深故事、证据、视觉系统、渲染和 A11y 检查，不自动增加无关 skill。

## 7. 能力槽

| 能力槽 | 作用 | 默认候选 |
|---|---|---|
| `story_outline` | 故事线、大纲、章节和每页 message | `ppt-image-first`、`academic-pptx`、`slide-maker` |
| `content_evidence` | 资料、数据、引用和事实核验 | `agent-reach`、`nature-paper2ppt`、`academic-pptx` |
| `visual_direction` | 视觉概念、色板、字体、版式系统 | `slide-design`、`kami`、`jinba-consulting-pptx` |
| `template_match` | 模板识别、母版和版式约束 | `template-creator`、`thesis-defense-pptx`、`image-to-editable-ppt` |
| `image_generation` | 图片型页面或配图生成 | `gpt-image2-ppt`、`baoyu-slide-deck`、Gorden 系列 |
| `slide_authoring` | 页面设计、布局和完整 deck 生产 | `Presentations`、`slide-maker`、`ppt-master`、`ppt-agent-skill` |
| `pptx_editing` | PPTX 原生编辑、修复、合并 | `Presentations`、`hands-on-deck`、`pptx` |
| `html_deck` | HTML 演示和网页展示 | `html-ppt`、`guizang-ppt-skill`、`dashi-ppt` |
| `render_qa` | 渲染、截图、溢出、对齐、字体检查 | `Presentations`、`hands-on-deck`、`pptx`、`slide-maker`、`documents` |
| `accessibility` | 阅读顺序、对比度、替代文本 | `powerpoint-accessibility`、`documents` |
| `delivery` | 导出、打包、格式和版本 | `Presentations`、`pptx`、`documents`、`pdf` |

全部能力选择、外部 GitHub skill 和冲突规则见 `references/capability-model.md` 与 `references/github-ppt-skills.md`。

## 8. 阶段顺序

```text
0 Brief
-> 1 Story outline
-> 2 Content and evidence
-> 3 Visual direction
-> 4 Exemplar + style contract
-> 5 Slide production
-> 6 Render
-> 7 Visual QA
-> 8 Editability / accessibility
-> 9 Final delivery
```

强制依赖：

- 完整 deck 在 story outline 通过前不进入批量生产；
- 批量生产前先做一张 exemplar slide 和 style contract；
- 每页必须有一个明确 message；
- 图表只使用真实数据；
- 渲染后才做版面、溢出和对齐判断；
- 可编辑 PPTX 必须回到原生 PPTX 检查，不能用图片替代可编辑性；
- 最终交前做文件打开、字体、链接和版本检查。

## 8.1 Official and plugin skills

优先顺序：

1. 目标是 Spaces、Google Slides、PowerPoint 文件读写或官方演示工作流：优先 `Presentations`。
2. 已有参考 deck/截图，需要抽取或复用模板：`template-creator`。
3. 需要从内容从零生成原生 PPTX：`slide-maker`、`ppt-master` 或 `pptx`。
4. 需要修改已有 PPTX：`Presentations` 或 `hands-on-deck`/`pptx`，三选一。
5. 需要 DOCX/PDF 渲染检查：`documents` / `pdf`，只做辅助。
6. 目标是 `.univer` / Univer Slides：`univer-cli`，不得冒充 PowerPoint 原生文件。

插件的调用策略、依赖和可用性由 SlideFlow 的能力发现预检；不能因为已安装就自动变成主技能。

## 9. 冲突裁决

- `ppt-master`、`slide-maker`、`GordenSuperPPTSkill` 不能同时作为完整 deck 的总编排。
- `gpt-image2-ppt` 与 `baoyu-slide-deck` 不能同时生成同一套图片型 deck。
- `html-ppt`、`guizang-ppt-skill`、`dashi-ppt` 不能同时主控同一份 HTML deck。
- `hands-on-deck` 和 `pptx` 不能同时编辑同一个 `.pptx`。
- `Presentations` 与 `slide-maker`/`ppt-master` 不能同时成为同一 deck 的主生产器。
- `template-creator` 不能越过当前 template owner 自创一套视觉系统。
- `univer-cli` 不得用于普通 PPTX 任务，除非用户明确使用 Univer。
- 图片型 PPT 不能声称是原生可编辑 PPTX；只有经过转换和验证后才可以。
- `academic-pptx` 负责内容/结构时，不能再让另一套 deck 叙事同时主控。
- 模板匹配只由 template owner 负责；其他 skill 不能擅自换模板。
- 视觉方向只能有一个主 owner；配色/字体/导出工具只能辅助。

## 10. 质量门

### Gate A: Brief and audience

- 受众、场景、时长、目标行动/理解；
- 演示型还是阅读型；
- 页数/时间约束；
- 输出形态、模板和禁忌。

### Gate B: Story

- 一句话中心结论；
- 每页一个 message；
- 标题串联可讲出完整故事；
- 开场、论证、结论、行动清楚。

### Gate C: Evidence and data

- 数据和事实有来源；
- 图表使用真实数据；
- 引用、脚注和 source data 可追溯；
- 不把定性判断包装成统计结果；
- 不伪造用户、客户、市场和实验结果。

### Gate D: Visual system

- 色板、字体、网格、间距一致；
- 主视觉不是装饰噪声；
- 每页信息层级清楚；
- 图表可读且有解释；
- 品牌/模板约束被遵守。

### Gate E: Layout and legibility

- 无文字溢出、遮挡、裁切；
- 字号、对比度和行距适合现场/阅读；
- 图表标签可读；
- 页脚、页码、来源不冲突；
- 渲染后的实际页面通过视觉检查。

### Gate F: File and editability

- PPTX/PDF/HTML 可打开；
- 字体、图片、链接和媒体不缺失；
- 可编辑产物保留原生文本和对象；
- PDF 是交付副本，不是唯一源文件；
- 文件命名和版本清楚。

### Gate G: Human approval

- 演讲者读完整套 deck；
- 确认事实、品牌、模板、姓名和日期；
- 确认最终输出形态和提交格式；
- 批准交付。

详细规则见 `references/quality-gates.md`。

## 11. 交接

每阶段至少交接：

- 输出模式、profile、tier、source mode；
- 当前阶段和主/辅技能；
- story outline 和 style contract；
- 每页 message、source data 和素材；
- 渲染文件与 QA 结果；
- 未解决问题和下一阶段。

文件型项目读取 `references/handoff-schemas.md`。

## 12. 输出契约

开始：

```text
SlideFlow：模式=…；输出=…；profile=…；tier=…；阶段=…；主技能=…；辅助技能=…
```

阶段结束：

```text
SlideFlow gate：pass / fail / pending
工件：…
未解决：…
下一阶段：…
下一主技能：…
```

不要展示完整 skill 清单或内部推理；只展示当前决策和影响交付的问题。

## 13. 参考文件

- `references/output-modes.md`：输出形态和路由。
- `references/deck-profiles.md`：各类演示的内容结构。
- `references/capability-model.md`：能力槽、选择规则和冲突。
- `references/quality-gates.md`：Gate A-G。
- `references/handoff-schemas.md`：项目状态、页面计划、style contract 和 QA 模板。
- `references/github-ppt-skills.md`：经过核验的 GitHub PPT/Agent Skills 来源和适用边界。

只读取当前任务需要的参考文件。
