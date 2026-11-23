# PPT Skill Strength Matrix

目标：让每个 skill 只负责自己最擅长的微任务，最后由一个装配器统一合成。

| Skill | Best for | Not best for |
|---|---|---|
| `Presentations` | 官方演示文件读写、Spaces、PowerPoint、Google Slides | 深度科研叙事、原创视觉系统 |
| `academic-ppt-master` | 论文转学术 deck、公式/图表保留、学术模板 | 产品营销、社交图文 |
| `slide-maker` | 完整 deck 结构、页面生产、critique loop | 只改一个 PPTX 对象 |
| `ppt-master` | 原生 PPTX、模板、图表、完整页面生产 | 研究事实核验 |
| `slide-design` / `kami` | 视觉语言、字体、配色、版式系统 | 论文内容和引用核验 |
| `academic-figure-skill` | 论文框架图、机制图、TOC、SVG | 整份 deck 编排 |
| `scientific-visualization` | 数据图、色板、导出和可访问性 | 机制图叙事 |
| `gpt-image2-ppt` / `baoyu-slide-deck` | 图片型页面、视觉冲击、社交传播 | 原生可编辑 PPTX |
| `html-ppt` / `guizang-ppt-skill` / `dashi-ppt` | HTML deck、网页演示 | 原生 PPTX 文件 |
| `hands-on-deck` / `pptx` | 原生 PPTX 精确编辑、修复、合并 | 从零故事线和研究内容 |
| `template-creator` | 模板抽取、复用和品牌约束 | 整份 deck 主生产 |
| `documents` / `pdf` | DOCX/PDF 渲染、检查、导出 | 版式创意和叙事 |
| `research-flow` | 论文事实、证据、story outline 的受限 fallback | 直接接管 deck 生产 |

## Micro-task examples

- `paper_extraction`: `academic-ppt-master` / `academic-pptx`
- `story_outline`: `research-flow` LIGHT / `scientific-brainstorming`
- `visual_system`: `slide-design` / `kami`
- `mechanism_figure`: `academic-figure-skill`
- `data_chart`: `scientific-visualization` / `scipilot-figure-skill`
- `page_authoring`: `slide-maker` / `ppt-master` / `Presentations`
- `pptx_edit`: `hands-on-deck` / `pptx`
- `render_pdf_qa`: `documents` / `pdf`

每个微任务最多 1 个主技能 + 2 个辅助技能；总 skill 数不超过 3。
