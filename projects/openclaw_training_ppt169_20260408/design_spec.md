# Design Specification for OpenClaw Training PPT

## Global Design Context

**Theme**: Bright Professional (亮色商务主题)
**Format**: 16:9 (1280×720)
**Total Pages**: 25 pages
**Style**: Clean, modern, professional training deck

---

## Color Palette

**Primary Colors**
- Primary Blue: #2563EB (标题、重点强调)
- Primary Dark: #1E40AF (副标题、边框)

**Secondary Colors**
- Accent Green: #10B981 (成功、完成状态)
- Accent Orange: #F59E0B (警告、注意)
- Accent Red: #EF4444 (错误、高危)

**Background Colors**
- Background White: #FFFFFF (主背景)
- Background Light: #F8FAFC (次要背景、卡片)
- Background Gray: #E2E8F0 (分隔线、边框)

**Text Colors**
- Text Primary: #1E293B (主标题、正文)
- Text Secondary: #64748B (副标题、注释)
- Text Muted: #94A3B8 (辅助信息)

---

## Typography

**Chinese Fonts**
- Headings: 思源黑体 Bold (Noto Sans SC Bold)
- Body: 思源黑体 Regular (Noto Sans SC Regular)
- Code: JetBrains Mono / Fira Code

**Font Sizes**
- Title: 36-44pt
- Subtitle: 24-28pt
- Body: 18-20pt
- Caption: 14-16pt

---

## Layout Templates

**Cover Page (封面页)**
- Layout: Center-aligned title with subtitle
- Background: White with subtle gradient
- Elements: Title, subtitle, date, presenter

**Content Page (内容页)**
- Layout: Title top, content below
- Background: White
- Elements: Section title, bullet points, icons

**Two Column (双栏布局)**
- Layout: Title top, two columns below
- Use: Comparison tables, side-by-side content

**Full Width Chart (全宽图表)**
- Layout: Title top, full-width chart
- Use: Architecture diagrams, flowcharts

**Quote Page (引用页)**
- Layout: Centered quote with accent background
- Use: Key takeaways, important notes

---

## Visual Elements

**Icons**
- Style: Tabler Icons (outline)
- Color: Primary Blue or Text Secondary
- Size: 24×24 for bullet points, 48×48 for section headers

**Charts**
- Bar charts: Primary Blue gradient
- Line charts: Primary Blue + Accent Green
- Pie charts: Multi-color (Blue, Green, Orange, Gray)

**Tables**
- Header: Primary Blue background, white text
- Rows: Alternating white and light gray
- Borders: Light gray (#E2E8F0)

**Code Blocks**
- Background: #F1F5F9 (light gray)
- Border: Left border 4px Primary Blue
- Font: JetBrains Mono 16pt

---

## Page-by-Page Design

| Page | Content | Layout | Notes |
|------|---------|--------|-------|
| 1 | 封面页 | Cover | 大标题 + 副标题 + 日期 |
| 2 | 目录 | Content | 5 个章节列表 |
| 3 | 1.1 OpenClaw 介绍 | Content | 核心价值 bullet points |
| 4 | 1.2 技术架构 | Full Width | 架构图 + 组件表格 |
| 5 | 1.3 信息架构 | Two Column | 信息流向 + 数据类型 |
| 6 | 1.4 记忆架构 | Full Width | 三层记忆系统图 |
| 7 | 1.5 技能架构 | Two Column | 技能结构 + 文件树 |
| 8 | 1.6 SubAgent 架构 | Content | 表格 + 调用代码示例 |
| 9 | 1.7 Cron 任务原理 | Two Column | 调度机制 + JSON 配置 |
| 10 | 2.1 关键要素 | Content | 5 步骤 + 配置表格 |
| 11 | 2.2 实战案例 | Full Width | 执行流程图 |
| 12 | 2.3 执行数据与复盘 | Two Column | 数据表格 +3 个坑 |
| 13 | 3.1 技能开发要素 | Content | 流程图 + 文件结构 |
| 14 | 3.2 PPT-Master 案例 | Full Width | 核心工作流 |
| 15 | 3.3 5 大坑 | Content | 5 个坑列表 |
| 16 | 4.1 Multi-Agent 要素 | Content | 概念表格 + 能力映射 |
| 17 | 4.2 任务路由案例 | Content | YAML 配置示例 |
| 18 | 4.3 通信问题 | Content | 3 问题 + 解决方案 |
| 19 | 4.4 协同问题 | Content | 3 问题 + 解决方案 |
| 20 | 4.5 任务监控系统 | Full Width | 监控系统架构图 |
| 21 | 4.6 超时规则 | Content | 超时表格 |
| 22 | 4.7 开发检查清单 | Content | 3 阶段 checklist |
| 23 | 附录：命令速查 | Two Column | 命令代码块 |
| 24 | 故障排查流程 | Full Width | 流程图 |
| 25 | Q&A / 谢谢 | Cover | 总结 + 联系方式 |

---

## Design Principles

1. **简洁优先**: 每页不超过 6 个 bullet points
2. **视觉层次**: 标题 > 副标题 > 正文 > 注释
3. **留白充足**: 页边距至少 48px
4. **对比度**: 文字与背景对比度≥4.5:1
5. **一致性**: 相同元素使用相同样式

---

## Export Settings

**PPTX Format**
- Native editable shapes (not images)
- Compatible with Office 2016+
- Include PNG fallback for complex SVG

**Resolution**
- 1280×720 (16:9)
- 96 DPI
