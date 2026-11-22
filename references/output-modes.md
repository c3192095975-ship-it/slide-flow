# Output Modes

Output mode 是 PPT 任务的第一个硬分叉。它决定最终文件、生产引擎、QA 方式和可编辑性。

## 1. editable_pptx

适用：

- 学校/公司汇报；
- 需要后续修改；
- 答辩、项目评审、销售/客户材料；
- 要求原生文本、形状、表格、图表。

默认候选：

- `Presentations`（Spaces/PowerPoint/Google Slides）
- `academic-ppt-master`（论文转学术 deck）
- `slide-maker`
- `ppt-master`
- `pptx`
- `hands-on-deck`

选择规则：

- 目标是 Spaces、Google Slides 或官方 PowerPoint 文件读写：优先 `Presentations`；
- 需要从论文生成学术 PPTX：`academic-ppt-master`；
- 需要从零生成非学术原生 PPTX：`slide-maker` 或 `ppt-master` 二选一；
- 只做已有 PPTX 编辑/修复：`Presentations`、`hands-on-deck` 或 `pptx` 三选一；
- 不能把图片型页面当作可编辑 PPTX。

## 2. image_deck

适用：

- 高视觉冲击；
- 信息图/海报式页面；
- 社交平台；
- 用户明确接受图片型 PPT。

默认候选：

- `gpt-image2-ppt`
- `baoyu-slide-deck`
- `GordenImagePPTGen`

规则：

- 每页是图片；
- 文本可能不可编辑；
- 必须另行说明是否转换为可编辑版；
- 不能声称图片型页面是原生 PPTX 对象。

## 3. html_deck

适用：

- 网页演示、分享会、发布会；
- 需要 WebGL、交互或浏览器展示；
- 需要 HTML 单文件或站点部署。

默认候选：

- `html-ppt`
- `guizang-ppt-skill`
- `dashi-ppt`

规则：

- 先确定是否需要导出 PDF/PPTX；
- HTML 不是 PPTX；
- 若需要可编辑 PPTX，另走 `html-to-editable-pptx`，不能同轮由两个系统各自生产。

## 4. template_edit

适用：

- 已有大学/公司/实验室模板；
- 需要严格母版、字体、页眉页脚、品牌规范。

默认候选：

- `template-creator`
- `thesis-defense-pptx`
- `image-to-editable-ppt`
- `html-to-editable-pptx`

规则：

- 先做模板检查和 exemplar slide；
- 不擅自替换模板；
- 模板版式优先于通用视觉风格。

## 5. image_to_editable

适用：

- 图片 PPT、截图、扫描件还原为可编辑 PPTX。

默认候选：

- `GordenImage2PPTX`
- `image-to-editable-ppt`
- `nature-image2ppt`

规则：

- 区分背景图、框架图、图标和真实文本；
- 文字必须是真文本框才算可编辑；
- 还原后必须检查文本溢出、字体和对象层级。

## 6. univer_slides

适用：

- 目标是 `.univer` / Univer Slides；
- 需要 Univer CLI 的导入、导出、预览或编辑。

主候选：`univer-cli`。

规则：

- 不用于普通 PowerPoint PPTX；
- 不把 `.univer` 文件称为原生 `.pptx`；
- 需要 PPTX 时明确转换和验证。

## 7. hybrid_delivery

只有用户明确要求时使用。例如：

```text
图片型 PPT + 可编辑 PPTX
HTML deck + PDF
```

必须分别定义验收标准，不能让一个产物自动代表另一个产物合格。
