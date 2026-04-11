# PPT 生成执行指南

## 项目信息
- 项目名称：openclaw_training_ppt169_20260408
- 源文件：sources/training_content.md (15KB, 25 页内容)
- 设计规范：design_spec.md (亮色商务主题)

## 执行步骤

### 1. 确认源文件已就绪
```bash
ls -lh sources/training_content.md
# 应该显示约 15KB
```

### 2. 创建设计规范（已完成）
design_spec.md 已创建，包含：
- 亮色主题配色（白色背景，蓝色主色调 #2563EB）
- 25 页页面设计规划
- 布局和图表规范

### 3. 生成 SVG 页面
使用 AI Agent 逐页生成 SVG，参考 design_spec.md 中的 Page-by-Page Design 表格。

### 4. 导出 PPTX
```bash
python3 /home/Vincent/.openclaw/workspace/skills/ppt-master/scripts/svg_to_pptx.py /home/Vincent/.openclaw/workspace/skills/ppt-master/projects/openclaw_training_ppt169_20260408 -s final
```

## 输出路径
PPTX 应保存到：
/home/Vincent/.openclaw/workspace/WORK/course-development/Openclaw 使用体验/OpenClaw 培训材料.pptx
