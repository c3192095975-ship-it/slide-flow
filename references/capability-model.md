# SlideFlow Capability Model

## 1. 能力槽

| 能力槽 | 职责 | 强信号 | 默认候选 |
|---|---|---|---|
| `story_outline` | 故事线、大纲、章节、每页 message | outline, story, narrative, deck plan | `ppt-image-first`、`academic-pptx`、`slide-maker` |
| `content_evidence` | 资料、数据、引用、事实核验 | research, data, citation, evidence | `agent-reach`、`nature-paper2ppt`、`academic-pptx` |
| `visual_direction` | 视觉风格、色板、字体、网格 | visual, design system, brand, art direction | `slide-design`、`kami`、`jinba-consulting-pptx` |
| `template_match` | 模板、母版和版式约束 | template, master, brand template | `template-creator`、`thesis-defense-pptx`、`image-to-editable-ppt` |
| `image_generation` | 图片型页面和配图生成 | image generation, gpt-image, image deck | `gpt-image2-ppt`、`baoyu-slide-deck`、Gorden 系列 |
| `slide_authoring` | 页面设计和完整 deck 生产 | deck, slides, pptx generation | `Presentations`、`slide-maker`、`ppt-master`、`ppt-agent-skill` |
| `pptx_editing` | 原生 PPTX 编辑、修复、合并 | edit pptx, patch deck, merge slides | `Presentations`、`hands-on-deck`、`pptx` |
| `html_deck` | HTML 演示和网页展示 | html, reveal, slidev, web deck | `html-ppt`、`guizang-ppt-skill`、`dashi-ppt` |
| `render_qa` | 渲染、截图、溢出、对齐、字体检查 | render, screenshot, overflow, visual QA | `Presentations`、`hands-on-deck`、`pptx`、`slide-maker`、`documents` |
| `accessibility` | 阅读顺序、对比度、替代文本 | accessibility, WCAG, alt text | `powerpoint-accessibility`、`documents` |
| `delivery` | 导出、打包、格式和版本 | export, pdf, pptx, package | `Presentations`、`pptx`、`documents`、`pdf` |
| `orchestration` | 多阶段总流程 | workflow, orchestrator | `slide-flow` 自身；不要同时加载多个总控 |

## 2. 选择顺序

1. 用户明确指定的 skill；
2. 输出模式匹配；
3. deck profile 匹配；
4. 当前阶段能力匹配；
5. 需要原生可编辑性时优先原生 PPTX 能力；
6. 需要图片型页面时优先图片生成能力；
7. 有渲染/视觉检查器时优先；
8. 有模板约束时模板 owner 优先；
9. 同名 skill 按项目级 > 用户级 > 插件级；
10. 无法决定时停在当前阶段，只问一个关键问题。

## 3. 同轮限制

- 一个主技能；
- 最多一个不同职责的辅助技能；
- 最多一个输出适配器；
- 同轮最多 3 个 skill；
- 不能同时加载两个总编排器；
- 不能同时生成两套视觉系统；
- 不能同时编辑同一份 PPTX；
- 不能同时生产图片型和可编辑型页面，除非明确双交付。

## 4. 能力降级

| 缺失能力 | 降级 |
|---|---|
| story outline | 使用内置 story brief 模板 |
| content/evidence | 使用用户材料和来源表 |
| visual direction | 使用最小品牌系统/单色网格 |
| template match | 使用通用模板并明确说明 |
| image generation | 使用真实图片/图标/图形，不伪造图片 |
| slide authoring | 生成 Markdown/HTML 大纲 |
| pptx editing | 生成结构化 patch 或 Markdown，不宣称改过 PPTX |
| html deck | 生成静态 Markdown/PDF |
| render QA | 至少输出页面计划和人工检查清单 |
| accessibility | 人工检查对比度、阅读顺序和替代文本 |
| delivery | 输出可打开的最简格式并说明限制 |

## 5. 外部 GitHub skill

见 `github-ppt-skills.md`。只把有明确许可和适用边界的仓库列为可选；不自动复制许可证不明的仓库内容。

## 6. PPT relevance filter

能力发现必须区分三类：

- `ppt_core`：名称/description 明确包含 slide、deck、presentation、PowerPoint、PPTX、Google Slides、HTML slides、幻灯片、演示文稿、答辩、汇报模板等强信号；
- `ppt_auxiliary`：不生产 deck，但提供模板、PDF/DOCX 渲染、A11y、导出或图片能力；
- `not_ppt`：只是包含 visual、delivery、template、data 等泛词。

只有 `ppt_core` 和 `ppt_auxiliary` 进入 SlideFlow 候选。

## 7. Official/plugin priority

- `Presentations`：Spaces、PowerPoint、Google Slides 和官方演示文件工作流的首选。
- `template-creator`：模板抽取/复用，不自动成为 deck 主生产器。
- `documents` / `pdf`：渲染、导出、格式验证辅助。
- `univer-cli`：只在 `.univer` / Univer Slides 目标下使用。
- `visualize`：解释性视觉辅助，不自动担任 PPT 版式主控。
