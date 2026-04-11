# OpenClaw 培训 PPT - 设计规范（smart_red 模板）

## 项目信息
- **项目名称**: openclaw_training_smart_red
- **源文件**: training_content.md (25 页内容)
- **模板**: smart_red (红黑商务风格)
- **画布**: 16:9 (1280×720)

---

## Eight Confirmations（八项确认）

### 1. 项目基本信息
- **项目名称**: openclaw_training_smart_red_ppt169_20260408
- **输出格式**: PPTX 16:9
- **总页数**: 25 页
- **模板风格**: smart_red (红黑商务)

**确认**: ✅

---

### 2. 源文件内容
**输入文件**: training_content.md
**内容结构**:
- 封面页 (1 页)
- 目录页 (1 页)
- 原理篇 (7 页): OpenClaw 技术基础
- 实践篇 1 (3 页): Cron 定时任务
- 实践篇 2 (3 页): 技能开发
- 实践篇 3 (7 页): Multi-Agent 体系
- 附录 (2 页): 命令速查 + 故障排查
- 封底页 (1 页)

**确认**: ✅

---

### 3. 设计模板选择
**模板**: smart_red
**模板特点**:
- 主色调：红色 #DE3545
- 辅助色：橙色 #F0964D
- 背景：浅灰 #F5F5F7
- 风格：几何商务，红黑对比
- 适用场景：技术培训、产品介绍

**确认**: ✅

---

### 4. 页面布局规划

| 页码 | 页面类型 | 内容 | 使用模板 |
|------|----------|------|----------|
| 1 | Cover | 封面：标题 + 副标题 + 日期 | 01_cover.svg |
| 2 | TOC | 目录：5 个章节 | 02_toc.svg |
| 3 | Chapter | 第 1 章：原理篇 | 02_chapter.svg |
| 4-10 | Content | 1.1-1.7 技术基础内容 | 03_content.svg |
| 11 | Chapter | 第 2 章：实践篇 1 | 02_chapter.svg |
| 12-14 | Content | Cron 任务实战 | 03_content.svg |
| 15 | Chapter | 第 3 章：实践篇 2 | 02_chapter.svg |
| 16-18 | Content | 技能开发实战 | 03_content.svg |
| 19 | Chapter | 第 4 章：实践篇 3 | 02_chapter.svg |
| 20-26 | Content | Multi-Agent 体系 | 03_content.svg |
| 27 | Content | 附录：命令速查 | 03_content.svg |
| 28 | Content | 故障排查流程 | 03_content.svg |
| 29 | Ending | 封底：Q&A + 谢谢 | 04_ending.svg |

**确认**: ✅

---

### 5. 配色方案

**主色调**:
- Primary Red: #DE3545 (标题、强调)
- Auxiliary Orange: #F0964D (装饰、渐变)
- Dark Gray: #333333 (文字、几何块)

**背景色**:
- Light Gray: #F5F5F7 (页面背景)
- White: #FFFFFF (卡片背景)

**文字色**:
- Body Black: #333333 (正文)
- Description Gray: #666666 (副标题)

**确认**: ✅

---

### 6. 字体规范

**中文字体**:
- 标题：Microsoft YaHei Bold (思源黑体 Bold)
- 正文：Microsoft YaHei Regular

**英文字体**:
- Arial, Helvetica Neue

**字号**:
- 封面标题：72px
- 页面标题：40px
- 正文：20px
- 注释：16px

**确认**: ✅

---

### 7. 图表和视觉元素

**图表类型**:
- 架构图：使用 03_content 模板，白色卡片承载
- 流程图：使用几何箭头 + 圆角矩形
- 表格：红黑配色，表头红色背景
- 代码块：灰色背景 #E0E0E0，等宽字体

**图标**:
- 使用 Tabler Icons (outline 风格)
- 颜色：Primary Red 或 Description Gray

**确认**: ✅

---

### 8. 导出设置

**PPTX 格式**:
- 原生可编辑形状（非图片）
- 兼容 Office 2016+
- 包含 PNG 后备（复杂 SVG）

**分辨率**:
- 1280×720 (16:9)
- 96 DPI

**输出路径**:
`/home/Vincent/.openclaw/workspace/WORK/course-development/Openclaw 使用体验/OpenClaw 培训材料_smart_red.pptx`

**确认**: ✅

---

## 执行流程

1. ✅ 项目初始化（已完成）
2. ✅ 源文件导入（已完成）
3. ✅ 设计规范确认（Eight Confirmations - 待用户确认）
4. ⏳ SVG 生成（逐页生成，25 页）
5. ⏳ 质量检查
6. ⏳ PPTX 导出（原生 + 兼容双格式）
7. ⏳ 交付

---

**请确认以上 Eight Confirmations 内容，确认后我将开始生成 SVG 页面。**

确认方式：回复"确认"或"✅"
