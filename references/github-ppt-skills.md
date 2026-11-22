# GitHub PPT / Agent Skills Research

Last verified: 2026-11-22.

Additional verified sources:

这些仓库用于扩充 SlideFlow 的能力候选。不是全部建议安装；许可证和运行环境需在使用前确认。

## High-value references

| Repository | License | Useful capability | Suggested role |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | No detected SPDX license | Official Agent Skills examples and PPTX references | Reference / manual install only |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | MIT | Native PPTX generation, shapes, transitions, charts, templates | `slide_authoring` / `editable_pptx` |
| [getsentry/skills](https://github.com/getsentry/skills) | Apache-2.0 | Presentation builder with React/Vite/Recharts and data-aware slide rules | `html_deck` / data presentation |
| [claude-office-skills/skills](https://github.com/claude-office-skills/skills) | MIT | ai-slides, dev-slides, html-slides, md-slides, pptx-manipulation | `pptx_editing`, `html_deck`, `slide_authoring` |
| [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | Apache-2.0 | deck planning, slide design, charts, themes/masters | `story_outline`, `visual_direction`, `template_match` |
| [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) | MIT | slides-creator | `slide_authoring` |
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | MIT | PowerPoint accessibility review | `accessibility` |
| [alchaincyf/huashu-skills](https://github.com/alchaincyf/huashu-skills) | MIT | huashu slides and Chinese content workflows | `slide_authoring` / social |
| [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | MIT | scientific pptx generation and official deck patterns | academic/scientific |
| [GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills) | No detected SPDX license | image PPT generation + editable conversion | reference only |
| [OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck) | AGPL-3.0 | frontend slides and PPTX skills | reference only unless AGPL accepted |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | Check repository | baoyu-slide-deck image deck generation | image_deck |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | Check repository | editorial/Swiss HTML deck | html_deck |
| [luwill/research-skills](https://github.com/luwill/research-skills) | No detected SPDX license | scholar-slides academic presentation | reference / academic_talk |

## Integration rules

1. 不把第三方 skill 的代码直接复制进 SlideFlow，除非许可证明确允许。
2. 发现仓库不等于已安装；只在用户安装或明确允许后调用。
3. 外部 GitHub skill 只能占一个能力槽，不能越过 SlideFlow 成为总编排。
4. 外部 skill 的模板、字体、图片和 API 依赖必须单独验收。
5. 许可证不明或 AGPL 的仓库只做参考，不自动整合代码。
6. 安装后可用 `scripts/discover_slide_skills.py` 做本地能力发现。

## Official/plugin skills found locally

These are not GitHub repositories; they are installed runtime/plugin skills and should be included in the local capability map:

| Skill | Role | Boundary |
|---|---|---|
| `Presentations` | official presentation read/create/edit/export | prefer for Spaces/PowerPoint/Google Slides |
| `template-creator` | reusable template creation | template owner only; not deck producer |
| `documents` | DOCX/PDF render and visual QA | auxiliary only |
| `pdf` | PDF render/inspect | auxiliary only |
| `univer-cli` | Univer files/slides | only for `.univer` targets |
| `visualize` | explanatory visuals | auxiliary visual only |

## Additional research/deck sources

| Repository | License | Use |
|---|---|---|
| [M1n-n9/academic-ppt-master](https://github.com/M1n-n9/academic-ppt-master) | MIT | paper to editable academic PPTX; strong academic_talk/thesis_defense candidate |
| [c-narcissus/paper-framework-figure-studio-pro](https://github.com/c-narcissus/paper-framework-figure-studio-pro) | No detected SPDX | framework/method overview figures; reference only |
| [chingswy/Skill-Research-Figure](https://github.com/chingswy/Skill-Research-Figure) | No detected SPDX | TikZ/hand-drawn SVG figures; reference only |
| [BAIKEMARK/happy-figure-skill](https://github.com/BAIKEMARK/happy-figure-skill) | NOASSERTION | structured scientific figure prompts; reference only |
| [lgwrightlab/schematic-figure](https://github.com/lgwrightlab/schematic-figure) | MIT | publication-quality vector schematics |
| [redreamality/Paper-Comicizer](https://github.com/redreamality/Paper-Comicizer) | No detected SPDX | paper-to-comic communication; social/科普 branch only |

Research figure repositories should enter `visual_asset`, never `slide_authoring`, unless they actually produce complete decks.
