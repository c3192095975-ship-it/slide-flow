# Slide Quality Gates

## Gate A: Brief and audience

检查：

- 受众和场景；
- 演示型/阅读型；
- 时长、页数和目标行动；
- 输出形态、模板和品牌禁区；
- 是否需要讲稿/备注。

## Gate B: Story

检查：

- 一句话中心结论；
- 每页一个 message；
- 标题串联能讲出完整故事；
- 开场、论证、结论、行动的顺序；
- 页面是否服务于一个明确决策或理解目标。

## Gate C: Evidence and data

检查：

- 每个事实、数字和引用有来源；
- 图表使用真实数据；
- 不把定性判断伪装成统计；
- 不虚构市场、客户、实验结果或用户证言；
- 图注、来源和单位清楚。

## Gate D: Visual system

检查：

- 色板、字体、网格和间距一致；
- 主视觉服务信息，不是装饰噪声；
- 每页有明确视觉层级；
- 图表和 icon 语义一致；
- 模板/品牌规范被遵守。

## Gate E: Layout and legibility

检查：

- 无文字溢出、遮挡、裁切；
- 字号、对比度和行距适合观看距离；
- 图表标签可读；
- 页脚、页码、来源不冲突；
- 实际渲染页面通过视觉检查。

## Gate F: File and editability

检查：

- PPTX/PDF/HTML 能打开；
- 字体、图片、链接和媒体存在；
- 可编辑文件保留原生文本和对象；
- PDF 不是唯一源文件；
- 文件名、版本和导出格式正确。

## Gate G: Human approval

检查：

- 演讲者完整阅读；
- 事实、品牌、姓名、日期和模板确认；
- 最终输出形态和提交方式确认；
- 批准交付。

## Failure handling

1. 定位失败门和具体页面。
2. 只修复受影响页面/阶段。
3. 重新渲染并复查同一门。
4. 默认最多两轮。
5. 第三轮需要新素材、模板变化、用户明确要求或新风险。
6. 不能靠换一个 PPT skill 绕过失败门。

## Gate H: Research fallback and visual asset fidelity

检查：

- 科研 fallback 是否有明确 trigger、scope、return_to、失效工件和重跑门；
- 是否只补强一个缺口，而不是重新生产整套 deck；
- 科研图是否有 source/data/prompt、许可证和矢量/栅格记录；
- 真实数据图是否来自真实数据；
- SVG 导入 PPT 后是否实际验证了文字和对象可编辑；
- `check_svg.py` 是否通过，且无 `<image>`/base64 位图伪装矢量；
- 图片模型生成的概念图是否被错误当作数据图或可编辑矢量。

通过条件：fallback 工件能被当前 deck 消费，可追溯，且没有悄悄替换原有视觉/叙事系统。

## Gate I: Evidence, rubric and VisualSpec

- every key slide has a claim;
- claim maps to evidence registry;
- data chart has real source data;
- conceptual visual is labelled conceptual;
- research competition has rubric mapping or an explicit missing-rules state;
- VisualSpec has purpose, labels/units, output format and editability.

## Gate J: PDF delivery QA

- authoring and delivery formats are explicit;
- PDF opens;
- page count, size and order are correct;
- no blank, clipped, overlapped or overflowing pages;
- text/images/charts are readable;
- source and PDF are in sync;
- unavailable checks are `not_checked`, never pass.
