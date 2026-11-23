# Scientific SVG Generation

## Purpose

将论文事实、数据或用户提供的参考图转换成可在 PowerPoint 中继续编辑的科研视觉资产。

## Source modes

- `paper`: 只使用论文明确出现或能直接推导的信息。
- `data`: 使用真实数据生成图表或示意图。
- `user_asset`: 使用用户提供的原始图、实验图或项目素材。
- `reference`: 只提取布局、比例、层级、配色和图标语义，不复制受保护作品。
- `concept`: 明确标注为概念示意，不能冒充实验观察。

## VisualSpec additions

```json
{
  "visual_id": "V01",
  "micro_task_id": "M03",
  "source_type": "paper",
  "source_location": "paper.pdf#section-2",
  "visual_type": "mechanism",
  "conceptual": true,
  "vector_required": true,
  "raster_embedded": false,
  "editable_text_required": true,
  "ppt_conversion_required": true,
  "validation_status": "pending"
}
```

## Generation rules

1. 先提取事实、机制、数据、标签和边界。
2. 写出箭头的语义：激活、抑制、转化、运输、时序或包含关系。
3. 生成 SVG 前先确定分组和图层。
4. 文字尽量保持 `<text>`，不要转成路径。
5. 不使用 `<image>` 嵌入原 PNG/JPG 冒充矢量。
6. 不把所有内容合并成一条 path。
7. 概念图必须标注 conceptual。
8. 真实数据图必须有 source data。
9. 参考图只提取设计规律，不复制受版权保护的作品。

## SVG structure

推荐：

```xml
<svg ...>
  <g id="background">...</g>
  <g id="connectors">...</g>
  <g id="nodes">...</g>
  <g id="labels"><text>...</text></g>
</svg>
```

## PPT integration

1. 导入 SVG；
2. 如 PowerPoint 支持，执行“转换为形状”；
3. 检查文本框、线条、箭头和图标是否独立可编辑；
4. 检查字体替换、文字裁切和缩放；
5. 失败时保留 SVG 源文件，不宣称已可编辑。

## Automated check

```bash
python3 scripts/check_svg.py --svg asset.svg --spec visual-spec.json
```

脚本只检查结构性事实：是否 SVG、是否嵌入位图、是否有文本/分组、是否单一路径。科学含义仍需人工核对。
