# Slide Flow

当前版本：`1.4.0`

Slide Flow 是一个独立的 PPT/演示文稿编排 skill。它不替代具体 PPT 制作工具，而是先选择输出形态，再按故事线、内容、视觉、生产、渲染、QA 和交付阶段选择唯一主技能，避免多个 PPT skill 互相抢任务。

## v1.4 更新重点

- 新增 Scientific SVG Generation：论文/参考图 → VisualSpec → 可编辑 SVG → PPT 对象。
- 新增 `check_svg.py`：检查 SVG 根节点、嵌入位图、文本、分组和单一路径。
- 新增 micro-task ownership：每个微任务最多一个主 skill + 两个辅助 skill。
- 新增 skill strength matrix：明确各 PPT skill 的 best_for 与 not_for。
- 新增 VisualSpec 的 vector/raster/editability/PPT conversion 字段。
- 强化参考图复刻边界：不得嵌入原图、位图冒充矢量或复制受保护作品。

## v1.3 更新重点

- 新增 Research Competition Profile 和 rubric-to-slide 映射。
- 新增 Scientific Visual Intelligence：按页面论点选择视觉类型，不强制每页有图。
- 新增 Evidence Registry：claim、来源、数据、页面和视觉可追踪。
- 新增 PDF Submission QA：authoring/delivery 分离，PDF 结构、页面和渲染检查。
- 新增 Design Reference Library 元数据与版权边界。
- 新增 capability verification：声明能力、smoke test 和 verified 区分。
- 新增 benchmark、human rubric 和 judge simulation 边界。
- 新增 `check_slide_plan.py` 和 `check_pdf.py`。
- 增加科研竞赛示例。

## v1.2 更新重点

- 新增 `visual_asset` 能力：论文框架图、机制图、流程图、TOC 和矢量图标。
- 新增科研 skill fallback：PPT 结果不满意时，按失败门只补强一个缺口，然后回到 SlideFlow。
- 新增 `paper_to_deck` 路径：论文 → story → 公式/图表/关键结果 → visual assets → editable PPTX。
- 新增 SVG-first 流程：概念图和机制图优先 SVG，导入 PPT 后验证“转换为形状”和可编辑性。
- 新增 Gate H：科研 fallback 和视觉资产保真。
- 扩展 GitHub 调研：academic-ppt-master、paper-framework-figure-studio-pro、Skill-Research-Figure、happy-figure-skill、schematic-figure、Paper-Comicizer。
- 保留 `Presentations`、`template-creator`、`documents`、`pdf`、`univer-cli` 的 v1.1 路由。

## v1.1 更新重点

- 接入官方 `Presentations` skill 作为 Spaces/PowerPoint/Google Slides 的首选。
- 接入 `template-creator` 作为模板复用辅助。
- 明确 `documents`、`pdf` 只做渲染/导出/验证辅助。
- `univer-cli` 只在 `.univer` / Univer Slides 目标下启用。
- 能力发现新增 `ppt_core` / `ppt_auxiliary` / `not_ppt` 相关性过滤，减少误报。

## 核心能力

- 输出形态分流：
  - `editable_pptx`
  - `image_deck`
  - `html_deck`
  - `template_edit`
  - `image_to_editable`
  - `hybrid_delivery`
- Deck profile：学术汇报、答辩、路演、咨询、培训、产品发布、社交图文、业务汇报、模板 deck。
- Quality tier：`draft`、`presentation_ready`、`executive_ready`、`publish_ready`。
- 每阶段一个主技能，最多一个不同职责的辅助技能。
- 先故事线，再生产页面。
- 生产后必须渲染和视觉 QA。
- 不把图片型 PPT 冒充可编辑 PPTX。
- 支持从现有 PPT skill 中发现能力，并整理为候选 stack。

## 安装

```bash
git clone https://github.com/c3192095975-ship-it/slide-flow.git slide-flow
mkdir -p ~/.codex/skills
cp -R slide-flow ~/.codex/skills/slide-flow
```

也可以把本目录直接复制到 `~/.codex/skills/slide-flow`。

## 使用

当任务涉及完整演示、PPTX/PPT、网页演示、图片型幻灯片、模板编辑或答辩 deck 时，先触发 `slide-flow`。

启动会显示：

```text
SlideFlow：模式=…；输出=…；profile=…；tier=…；阶段=…；主技能=…；辅助技能=…
```

## 阶段

```text
Brief -> Story -> Content/Evidence -> Visual Direction
-> Exemplar + Style Contract -> Production -> Render
-> Visual QA -> Editability/Accessibility -> Delivery
```

## 能力发现

```bash
python3 scripts/discover_slide_skills.py
```

脚本扫描当前已安装的 skill 元数据，识别：

- story_outline
- content_evidence
- visual_direction
- template_match
- image_generation
- slide_authoring
- pptx_editing
- html_deck
- render_qa
- accessibility
- delivery

## Scientific SVG generation

科研图和机制图使用：

```text
paper/data/reference
-> VisualSpec
-> SVG
-> check_svg.py
-> PowerPoint import
-> convert to shapes (when supported)
-> editability verification
-> slide placement
```

要求：

- 只用论文明确出现或可直接推导的信息；
- 箭头表达真实机制方向；
- 标签、单位和对象可追溯；
- 不把位图嵌入 SVG 冒充矢量；
- 不把所有内容合并成单一不可拆路径；
- 参考图只提取布局和设计规律；
- 生成后仍需人工核对科学逻辑。

## 微任务分工

每个微任务最多一个主 skill 和两个辅助 skill。总装配器负责统一风格、页面结构和最终导出。

## Research Competition

科研竞赛使用 `research_competition` profile：

- 问题与重要性；
- 现有方法与缺口；
- 创新点；
- 方法/技术路线；
- 实验设计与验证；
- 关键结果；
- 对比与可靠性；
- 应用价值；
- 局限与下一步。

如果用户提供官方规则，必须做 rubric-to-slide mapping；没有官方规则时只能使用通用检查并标注“非官方”。

## Evidence and PDF QA

- `slide-plan.json`：每页 takeaway、claim、evidence_ids 和 VisualSpec。
- `evidence-registry.json`：来源、数据、方法、限制和页面映射。
- `authoring_format` 与 `delivery_format` 分开。
- PPTX 不是 PDF 交付合格证明。
- `check_pdf.py` 检查结构、页数、页面尺寸、渲染和可检查的工具项。
- 工具不可用的检查标记 `not_checked`。

## 科研 fallback

科研 skill 只作为具体失败门的补强，不接管整个 deck：

- Gate B 故事线：`research-flow` LIGHT / `scientific-brainstorming`
- Gate C 证据：`nature-ref-verifier` / `peer-review`
- Gate C 数据/图表：`scientific-toolkit-skill` / `scipilot-figure-skill`
- Gate D 视觉资产：`academic-figure-skill` / `scientific-visualization` / `nature-figure`
- Gate E 文案：`scientific-writing` / `nature-polishing`
- Gate F 可编辑性：`hands-on-deck` / `pptx` / `image-to-editable-ppt`
- 论文整体转学术 deck：`academic-ppt-master`

补强后必须回到 SlideFlow，重新执行受影响门。

## 视觉资产与 SVG

- 真实数据图必须来自真实数据；
- 机制图、框架图和流程图优先 SVG；
- SVG 导入 PPT 后验证“转换为形状”和文字/对象可编辑；
- 生成图片只能作为概念或装饰，不能冒充数据图；
- 每个资产记录来源、许可证、vector/raster 和 editability。

## 官方/插件 PPT 能力

当前本机值得纳入 SlideFlow 的官方或插件能力：

| Skill | 角色 | 边界 |
|---|---|---|
| `Presentations` | 官方 presentation read/create/edit/export | Spaces、PowerPoint、Google Slides 首选 |
| `template-creator` | 可复用模板 | 只负责模板，不成为 deck 主生产器 |
| `documents` | DOCX/PDF 渲染和视觉 QA | 辅助 |
| `pdf` | PDF 检查和导出 | 辅助 |
| `univer-cli` | Univer Slides / `.univer` | 不用于普通 PPTX |
| `visualize` | 解释性视觉 | 不抢 PPT 版式主控 |

## GitHub PPT skill 扩充

已整理一份经过核验的 GitHub PPT/Agent Skills 参考：

- `references/github-ppt-skills.md`

其中包括：

- anthropics/skills
- hugohe3/ppt-master
- getsentry/skills
- claude-office-skills/skills
- openJiuwen-ai/jiuwenswarm
- daymade/claude-code-skills
- Community-Access/accessibility-agents
- alchaincyf/huashu-skills
- beita6969/ScienceClaw
- 以及其他可选参考

许可证不明的仓库只做参考，不自动复制其代码。

## 文档

- [用户指南](docs/user-guide.md)
- [架构说明](docs/architecture.md)
- [输出形态](references/output-modes.md)
- [Deck profiles](references/deck-profiles.md)
- [能力模型](references/capability-model.md)
- [质量门](references/quality-gates.md)
- [GitHub PPT skills](references/github-ppt-skills.md)

## 示例

见 `examples/research-competition/`。

## 测试

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT。见 [LICENSE](LICENSE)。
