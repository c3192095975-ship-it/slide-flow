---
name: slide-flow
description: Orchestrate presentation and slide-deck production without conflicting PPT skills. Use for creating, editing, converting, reviewing, or exporting decks, slides, PPT/PPTX, PowerPoint, Google Slides, HTML slides, image-based slides, or presentation narratives. Triage first; select output mode, deck profile, quality tier, and source mode; then build story, content, visual direction, production, render QA, accessibility, and delivery with one primary skill per stage. Prefer the official `Presentations` skill for Spaces/PowerPoint/Google Slides when available, `template-creator` for reusable templates, and `documents`/`pdf` only as verification or delivery support. Support scoped research-skill fallback, research-competition profiles, scientific visual intelligence, scientific SVG assets, evidence registries, PDF submission QA, design references, and micro-task skill specialization. Do not use for ordinary document writing or isolated image generation without a slide/deck context.
metadata:
  version: "1.4.0"
  short-description: Orchestrate PPT skills by output mode and stage
---

# Slide Flow v1.4

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
16. 科研 skill 只能作为具体失败门的补强，不得直接接管整个 deck；补强完成后必须回到 SlideFlow。
17. 科研 fallback 必须使用受限范围（例如 research-flow LIGHT），并记录 trigger、scope、return_to、失效工件和重跑检查。
18. 真实数据图优先由科研绘图/数据分析能力生成；概念图、框架图和机制图优先使用可编辑 SVG。
19. SVG 导入 PowerPoint 后，只有实际完成“转换为形状”并验证对象可编辑，才能称为可编辑 PPTX。
20. `academic-ppt-master` 可作为论文转学术 deck 的替代主生产器，但不能与 `Presentations`、`slide-maker` 或 `ppt-master` 同时主控。
21. 每个重要页面必须有 takeaway/claim，且重要 claim 必须能映射到 evidence registry。
22. 每个科研视觉必须有 VisualSpec；真实数据图只能使用真实数据，概念图必须标注为示意。
23. `authoring_format` 与 `delivery_format` 分离；PPTX 生成成功不等于 PDF 交付合格。
24. 比赛规则只能来自用户提供的官方文件；缺失时使用通用检查并标明“非官方”。
25. PDF 交付必须检查页数、页面尺寸、渲染、文本/图片完整性和源文件一致性；工具缺失时标记 `not_checked`。
26. 设计参考只提取结构和表达规律，不复制受版权保护的整页作品。
27. Benchmark、Judge Simulation 和内部评分只作为辅助，不得冒充官方成绩或评委结论。
28. 科研 SVG 必须来自论文/数据/用户材料或明确标记的参考图；不得把位图嵌入冒充矢量，不得用单一不可拆路径冒充可编辑对象。
29. 科研图生成后必须检查机制方向、标签、单位、箭头语义、对象分组、文本可编辑性和 PPT 转换结果。
30. 每个微任务只能有一个主技能，最多两个辅助技能，总 skill 数不超过 3；微任务输出回到总装配器，不直接重写整套 deck。
31. 设计参考和参考图只用于提取布局与表达规律；未获授权不得复制受版权保护的整张科研图或作品。

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
| `editable_pptx` | 需要后续编辑、公司/学校汇报 | `Presentations`、`academic-ppt-master`、`slide-maker`、`pptx`、`hands-on-deck`、`ppt-master` |
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
| `research_competition` | 科研创新/学生项目竞赛 | 问题、创新、方法、验证、价值、限制、rubric 映射 |
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
| `visual_asset` | 论文框架图、机制图、流程图、TOC、矢量图标 | `academic-figure-skill`、`scientific-visualization`、`nature-figure`、`schematic-figure`、科研绘图 fallback |

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
-> 2 Content and evidence registry
-> 2.5 Evidence / rubric validation
-> 3 Visual direction
-> 3.5 VisualSpec / visual asset preparation
-> 4 Exemplar + style contract
-> 5 Slide production
-> 6 Render
-> 7 Visual QA
-> 8 Editability / accessibility
-> 8.5 PDF delivery QA
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

## 7.1 Authoring and delivery formats

每个完整任务必须记录：

```yaml
authoring_format: editable_pptx | html_deck | image_deck | univer
delivery_format: pdf | pptx | html | png_zip
```

规则：

- 可编辑源文件和最终交付物分开验收；
- PPTX 成功生成不代表 PDF 合格；
- PDF 必须实际检查页数、页面尺寸、渲染和源文件一致性；
- 工具不可用时标记 `not_checked`，不能默认通过。

## 7.2 Evidence, rubric and VisualSpec

核心工件：

- `evidence-registry.json`：claim、来源、数据、限制、状态、相关页面/视觉；
- `slide-plan.json`：每页 title、takeaway、claim、evidence_ids、visual_type、visual_spec_id；
- `visual-specs.json`：视觉类型、目的、数据源、标签、单位、输出格式和可编辑性；
- `rubric-map.yaml`：比赛/课程/投稿评分维度到页面的映射，仅使用提供的官方规则。

可使用：

```bash
python3 scripts/check_slide_plan.py --plan slide-plan.json --evidence evidence-registry.json
```

科研竞赛、学术汇报和 PDF 交付的具体规范见对应 references。

## 7.3 Micro-task ownership

PPT skill 不需要负责整份 deck。先将工作拆成微任务：

```yaml
micro_task_id: M03
slide_id: S05
task_type: mechanism_figure
primary_skill: academic-figure-skill
auxiliary_skills:
  - scientific-visualization
output_contract:
  format: svg
  editable: true
return_to: slide-flow
```

规则：

- 一个微任务一个主技能；
- 最多两个辅助技能，总 skill 数不超过 3；
- 微任务只交付中间工件；
- 总装配器负责页面风格、布局和最终合并；
- 同一页面对象不能由两个微任务同时写；
- 失败时只回到对应微任务修复。

强项与禁区见 `references/skill-strength-matrix.md`。

## 7.4 Scientific SVG assets

科研视觉资产统一走：

```text
paper/data/reference
-> VisualSpec
-> SVG structure
-> deterministic checks
-> PPT import
-> convert to shapes (when supported)
-> editability verification
-> slide placement
```

要求：

- 机制/概念图优先 SVG；
- 真实数据图优先真实数据生成；
- 不嵌入原始位图冒充矢量；
- 不只生成一条不可拆路径；
- 标签、箭头和方向必须与论文/数据一致；
- 概念图标注 conceptual；
- 参考图只提取设计规律，不复制受保护作品；
- 输出后运行 `scripts/check_svg.py`。

详细协议见 `references/scientific-svg-generation.md`。

## 8.1 Official and plugin skills

优先顺序：

1. 目标是 Spaces、Google Slides、PowerPoint 文件读写或官方演示工作流：优先 `Presentations`。
2. 已有参考 deck/截图，需要抽取或复用模板：`template-creator`。
3. 需要从内容从零生成原生 PPTX：`slide-maker`、`ppt-master` 或 `pptx`。
4. 需要修改已有 PPTX：`Presentations` 或 `hands-on-deck`/`pptx`，三选一。
5. 需要 DOCX/PDF 渲染检查：`documents` / `pdf`，只做辅助。
6. 目标是 `.univer` / Univer Slides：`univer-cli`，不得冒充 PowerPoint 原生文件。

插件的调用策略、依赖和可用性由 SlideFlow 的能力发现预检；不能因为已安装就自动变成主技能。

## 8.2 Research fallback

科研 skill 只用于补强具体缺口：

| PPT 失败门 | 允许的 fallback | 返回位置 |
|---|---|---|
| Gate B 故事线浅 | `research-flow` LIGHT / `scientific-brainstorming` | story outline |
| Gate C 证据不足 | `nature-ref-verifier` / `peer-review` | content/evidence |
| Gate C 数据/图表不可靠 | `scientific-toolkit-skill` / `scipilot-figure-skill` | visual asset / content |
| Gate D 视觉资产不足 | `academic-figure-skill` / `scientific-visualization` / `nature-figure` | visual asset |
| Gate E 文案空泛 | `scientific-writing` / `nature-polishing` | draft |
| Gate F 可编辑性失败 | `hands-on-deck` / `pptx` / `image-to-editable-ppt` | production |
| 学术 deck 核心转换失败 | `academic-ppt-master`（仅在未启用其他主生产器时） | production |

fallback 规则：

- 只补一个缺口，不接管整套 deck；
- `research-flow` 只能以 LIGHT 或受限子任务使用；
- 返回 SlideFlow 后重新执行受影响门；
- 不得同时让 PPT 主生产器和科研总流程各自生产一套页面；
- 许可证不明的科研图仓库只参考，不复制代码。

## 8.3 Paper-to-deck method

论文转 deck 使用固定路径：

```text
论文
-> 中心贡献/问题/方法/实验/结论/限制
-> story outline
-> 保留的公式、图表、关键结果
-> visual direction
-> visual asset preparation
-> exemplar + style contract
-> slide production
-> render
-> visual QA
-> editability/accessibility
-> delivery
```

适用：

- `academic_talk`
- `thesis_defense`
- `grant_briefing`
- `lab_meeting`

默认候选：

- `academic-ppt-master`
- `academic-pptx`
- `nature-paper2ppt`
- `ppt-master`
- `Presentations`

优先保留论文原图、表格、公式和 source data；不能把论文仅压缩成 bullet 摘要。

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
### Gate H: Research fallback and visual asset fidelity

- 科研 fallback 必须有 trigger、scope、return_to、失效工件和重跑检查；
- 科研图、SVG 和生成资产必须有来源、数据/提示词记录、许可证、矢量/栅格类型和可编辑性状态；
- 真实数据图不能用图片模型伪造；
- SVG 转 PPT 后必须实际验证文字和对象可编辑；
- 不允许科研 fallback 另起一套 deck 叙事。
- 科研 SVG 不使用 `<image>` 或 base64 位图冒充矢量；
- SVG 至少包含可编辑文本和基本分组；
- 参考图复刻不得直接嵌入原图或复制受保护作品。


- 演讲者读完整套 deck；
- 确认事实、品牌、模板、姓名和日期；
- 确认最终输出形态和提交格式；
- 批准交付。

详细规则见 `references/quality-gates.md`。

### Gate I: Evidence, rubric and VisualSpec

- 重要页面有 takeaway/claim；
- claim 能映射到 evidence registry；
- 数据图有真实数据源；
- 概念图明确标记 conceptual；
- research competition 有 rubric-to-slide mapping 或明确缺少官方规则；
- VisualSpec 有 purpose、labels/units、output format 和 editability。

### Gate J: PDF delivery QA

- authoring_format 与 delivery_format 明确；
- PDF 可打开；
- 页数、页面尺寸和顺序正确；
- 无空白页、明显裁切、遮挡或溢出；
- 字体/文字/图片/图表可读；
- 源文件与 PDF 一致；
- 工具缺失时记录 `not_checked`，不能伪报通过。

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
- `references/research-competition-profile.md`：科研竞赛 Profile 和 rubric 映射。
- `references/scientific-visual-intelligence.md`：视觉类型、VisualSpec 和科研视觉决策。
- `references/evidence-registry.md`：证据、claim、数据和页面/视觉映射。
- `references/pdf-submission-qa.md`：PPTX 到 PDF 的交付检查。
- `references/design-reference-library.md`：设计参考元数据和版权边界。
- `references/benchmark-and-judge.md`：基准任务、评分 rubric 和评委模拟边界。
- `references/capability-verification.md`：声明能力与验证能力的区分。
- `references/scientific-svg-generation.md`：论文/参考图 → 可编辑 SVG 的生成和验证协议。
- `references/skill-strength-matrix.md`：PPT skill 的 best_for / not_for 和微任务分工。
- `scripts/check_slide_plan.py`：检查 SlidePlan、证据引用和 VisualSpec。
- `scripts/check_pdf.py`：检查 PDF 结构、页面和渲染。
- `scripts/check_svg.py`：检查 SVG 是否为矢量、是否嵌入位图、文本/分组和基础可编辑性。

只读取当前任务需要的参考文件。
