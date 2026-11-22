# Slide Flow 用户指南

## 1. 它解决什么问题

PPT skill 数量多，而且输出形态差异很大：

- 可编辑 PPTX；
- 图片型 PPT；
- HTML 演示；
- 模板套用；
- 图片还原为可编辑 PPTX。

直接让所有 PPT skill 自由触发的典型结果是：

- 两个总编排 skill 同时运行；
- 图片型和可编辑型产物互相冒充；
- 先做页面，再补故事；
- 模板被擅自替换；
- 渲染成功但没有检查溢出和对齐；
- 文件和源素材命名混乱。

Slide Flow 负责控制这些冲突。

## 2. 第一层：输出形态

必须先选：

```text
editable_pptx
image_deck
html_deck
template_edit
image_to_editable
hybrid_delivery
```

一次任务只能有一个主输出形态。

## 3. 第二层：Deck profile

常用：

- academic_talk
- thesis_defense
- pitch
- consulting
- training
- product_launch
- social_deck
- business_review
- template_deck

## 4. 第三层：Quality tier

- draft：结构和内容；
- presentation_ready：可以上台；
- executive_ready：高层/客户/答辩质量；
- publish_ready：可发布和归档。

提高 tier 只加深故事、证据、视觉和 QA，不自动加载更多 skill。

## 5. 阶段

```text
0 Brief
1 Story outline
2 Content and evidence
3 Visual direction
4 Exemplar + style contract
5 Slide production
6 Render
7 Visual QA
8 Editability / accessibility
9 Delivery
```

## 5.1 官方/插件 skill 优先级

- Spaces、PowerPoint、Google Slides：优先 `Presentations`。
- 模板复用：`template-creator` 作为 template owner。
- DOCX/PDF 视觉检查：`documents` / `pdf` 辅助。
- `.univer` 目标：`univer-cli`。
- 普通 PPTX 不使用 `univer-cli`，也不把图片型页面当可编辑 PPTX。

## 5.2 能力相关性过滤

能力发现将 skill 标记为：

- `ppt_core`：真正生产、编辑或转换 deck；
- `ppt_auxiliary`：模板、PDF/DOCX、A11y、视觉辅助；
- `not_ppt`：只是泛词或无关工具。

只有前两类进入 SlideFlow 候选。

## 5.3 科研 fallback

当 PPT skill 的产物在某个质量门失败时，不要整套重做。按失败原因选择一个科研 skill 补强：

| 失败类型 | fallback |
|---|---|
| 故事线 | `research-flow` LIGHT / `scientific-brainstorming` |
| 证据 | `nature-ref-verifier` / `peer-review` |
| 数据/真实图表 | `scientific-toolkit-skill` / `scipilot-figure-skill` |
| 框架图/机制图 | `academic-figure-skill` / `scientific-visualization` / `nature-figure` |
| 文案 | `scientific-writing` / `nature-polishing` |
| 论文转学术 deck | `academic-ppt-master` |

补强后回到 SlideFlow，只重跑受影响的 Gate。

## 5.4 Visual asset

推荐流程：

```text
message -> visual question -> SVG/real data -> inspect -> import PPT
-> convert to shapes (if available) -> verify editability -> place on slide
```

`paper-framework-figure-studio-pro`、`Skill-Research-Figure`、`happy-figure-skill` 等许可证不明的仓库只作为参考，不复制代码。

## 6. 质量门

- A：brief 和受众；
- B：故事线；
- C：证据和数据；
- D：视觉系统；
- E：版式和可读性；
- F：文件和可编辑性；
- G：人工确认。

## 7. 能力发现

```bash
python3 scripts/discover_slide_skills.py
```

输出 JSON 能力清单。它只读取 skill 元数据，不执行其他 skill。

## 8. 常见冲突

- 两个总编排 skill 同时运行；
- 图片型 PPT 和可编辑 PPTX 同时主控；
- 两套视觉系统同时修改同一套 deck；
- 两个 PPTX 编辑 skill 同时改同一个文件；
- 模板匹配和通用视觉风格同时决定版式；
- 生成成功但没有渲染验收。

## 9. 安全边界

- 不伪造数据、图表、引用、客户证言或品牌素材；
- 不把 PDF 当唯一可编辑源；
- 不把图片型页面称为可编辑 PPTX；
- 不自动安装或复制许可证不明的第三方 skill；
- 人类演讲者确认最终内容。
