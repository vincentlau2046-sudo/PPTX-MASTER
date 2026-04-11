# Design Specification for OpenClaw Training PPT (smart_red Template)

## Global Design Context

**Template**: smart_red (Smart Red-Orange Business Style)
**Format**: 16:9 (1280×720)
**Total Pages**: 25 pages
**Style**: Modern, energetic, professional - suitable for technical training

---

## Template Overview

| Property | Description |
|----------|-------------|
| **Template Name** | smart_red (Smart Red-Orange Business Style) |
| **Use Cases** | Technical training, product introductions, solution presentations |
| **Design Tone** | Modern, energetic, professional, geometric |
| **Theme Mode** | Hybrid (dark/colorful cover + light content pages) |

---

## Color Scheme

### Primary Colors (from smart_red template)

| Role | Value | Usage |
|------|-------|-------|
| **Primary Red** | #DE3545 | Brand identity, title decoration, geometric cutouts |
| **Auxiliary Orange** | #F0964D | Geometric accents, gradient pairing |
| **Dark Background** | #333333 | Cover background, geometric cutouts, dark footer |

### Neutral Colors

| Role | Value | Usage |
|------|-------|-------|
| **Light Gray Background** | #F5F5F7 | Page background |
| **Border Gray** | #E0E0E0 | Section dividers, card borders |
| **Body Black** | #333333 | Titles and body text |
| **Description Gray** | #666666 | Subtitles, annotation text |
| **Pure White** | #FFFFFF | Card background |

---

## Typography System

**Font Stack**: `Arial, "Helvetica Neue", "Microsoft YaHei", sans-serif`

### Font Size Hierarchy

| Level | Usage | Size | Weight |
|-------|-------|------|--------|
| H1 | Cover main title | 60-80px | Bold |
| H2 | Page title | 32-40px | Bold |
| H3 | Subsection/Card title | 24-28px | Bold |
| P | Body content | 18-20px | Regular |
| Caption | Supplementary text | 14-16px | Regular |

---

## Core Design Principles

### Geometric Business Style

1. **Geometric Cutouts**: Cover, table of contents, and transition pages use large triangular cutout designs
2. **Red-Black Contrast**: Red primary color paired with dark gray blocks creates professional and impactful visual
3. **Card-Based Layout**: Content pages use white cards to hold content, with light gray backgrounds for depth
4. **Whitespace**: Maintain adequate whitespace to avoid information overload

### Advanced Refinement Features (v2.0)

1. **Multi-Layer Geometric Overlay**: Main triangles paired with semi-transparent smaller triangles
2. **Shadow Effects**: Text shadows, card shadows for 3D feel
3. **Dual-Line Decoration**: Decorative lines use dual-line styles (thick + thin)
4. **Subtle Glow**: Ultra-faint color glow behind content areas

---

## Page-by-Page Design

| Page | Content | Layout | Notes |
|------|---------|--------|-------|
| 1 | 封面页 | Cover (01_cover.svg) | 大标题 + 副标题 + 日期，红色几何装饰 |
| 2 | 目录 | TOC (02_toc.svg) | 5 个章节列表，圆形编号 |
| 3 | 1.1 OpenClaw 介绍 | Content (03_content.svg) | 核心价值 bullet points，白色卡片 |
| 4 | 1.2 技术架构 | Content | 架构图 + 组件表格 |
| 5 | 1.3 信息架构 | Content | 信息流向 + 数据类型 |
| 6 | 1.4 记忆架构 | Content | 三层记忆系统图 |
| 7 | 1.5 技能架构 | Content | 技能结构 + 文件树 |
| 8 | 1.6 SubAgent 架构 | Content | 表格 + 调用代码示例 |
| 9 | 1.7 Cron 任务原理 | Content | 调度机制 + JSON 配置 |
| 10 | 2.1 关键要素 | Content | 5 步骤 + 配置表格 |
| 11 | 2.2 实战案例 | Content | 执行流程图 |
| 12 | 2.3 执行数据与复盘 | Content | 数据表格 +3 个坑 |
| 13 | 3.1 技能开发要素 | Chapter (02_chapter.svg) | 技能开发流程 |
| 14 | 3.2 PPT-Master 案例 | Content | 核心工作流 |
| 15 | 3.3 5 大坑 | Content | 5 个坑列表 |
| 16 | 4.1 Multi-Agent 要素 | Chapter | 概念表格 + 能力映射 |
| 17 | 4.2 任务路由案例 | Content | YAML 配置示例 |
| 18 | 4.3 通信问题 | Content | 3 问题 + 解决方案 |
| 19 | 4.4 协同问题 | Content | 3 问题 + 解决方案 |
| 20 | 4.5 任务监控系统 | Content | 监控系统架构图 |
| 21 | 4.6 超时规则 | Content | 超时表格 |
| 22 | 4.7 开发检查清单 | Content | 3 阶段 checklist |
| 23 | 附录：命令速查 | Content | 命令代码块，灰色背景 |
| 24 | 故障排查流程 | Content | 流程图 |
| 25 | Q&A / 谢谢 | Ending (04_ending.svg) | 总结 + 联系方式 |

---

## Design Principles

1. **简洁优先**: 每页不超过 6 个 bullet points
2. **视觉层次**: 标题 > 副标题 > 正文 > 注释
3. **留白充足**: 页边距至少 60px (左右), 50px (上下)
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

---

## Template Reference

Template files located at:
`/home/Vincent/.openclaw/workspace/skills/ppt-master/templates/layouts/smart_red/`

- 01_cover.svg - Cover page template
- 02_toc.svg - Table of contents template
- 02_chapter.svg - Chapter transition template
- 03_content.svg - Content page template
- 04_ending.svg - Ending page template
