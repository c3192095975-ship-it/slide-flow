# Slide Flow

当前版本：`1.1.0`

Slide Flow 是一个独立的 PPT/演示文稿编排 skill。它不替代具体 PPT 制作工具，而是先选择输出形态，再按故事线、内容、视觉、生产、渲染、QA 和交付阶段选择唯一主技能，避免多个 PPT skill 互相抢任务。

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

## 测试

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT。见 [LICENSE](LICENSE)。
