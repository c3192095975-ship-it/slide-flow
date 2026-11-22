# Slide Flow 架构

## 1. 分层

```text
任务识别
-> 分级
-> 输出形态
-> deck profile
-> quality tier
-> source mode
-> 能力图
-> 阶段主技能
-> 渲染与 QA
-> 交付
```

## 2. 为什么先选输出形态

PPTX、图片型页面和 HTML 是不同产物。如果先选 skill，容易出现：

- 用图片生成 skill 做需要编辑的 PPTX；
- 用 HTML 生成器做需要 PPTX 模板的答辩；
- 两个生产引擎同时控制同一份 deck。

## 3. 能力槽

```text
story_outline
content_evidence
visual_direction
template_match
image_generation
slide_authoring
pptx_editing
html_deck
render_qa
accessibility
delivery
orchestration
```

一个阶段一个主能力，最多一个辅助能力。

## 4. 单一主技能

- `ppt-master`、`slide-maker`、`GordenSuperPPTSkill` 不能同时总控；
- 图片型和可编辑型不能同时作为主产物；
- `hands-on-deck` 和 `pptx` 不能同时编辑同一个 PPTX；
- 模板 owner 和视觉 owner 不能互相覆盖。

## 5. 质量门

Gate A-G 覆盖受众、故事、内容、视觉、版式、文件、可编辑性和人工确认。

## 6.2 Fallback layer

```text
PPT primary skill
-> Gate failure
-> select one research fallback
-> produce one repaired artifact
-> return to SlideFlow
-> rerun affected gate
```

科研 fallback 不重新定义 deck，不另起一套页面生产。它只补 story、evidence、visual asset、writing 或 editability。

## 6.1 插件感知

SlideFlow 同时扫描本地 skill 和可选插件缓存：

- `Presentations`：官方演示工作流；
- `template-creator`：模板能力；
- `documents` / `pdf`：渲染和导出辅助；
- `univer-cli`：Univer 文件。

插件能力必须通过 relevance filter，不能因为已安装就自动成为主技能。

## 6. 外部技能

GitHub PPT skill 只作为候选能力，不越过 Slide Flow 成为总流程。许可证不明或 AGPL 的仓库只作参考。
