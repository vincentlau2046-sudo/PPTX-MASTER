# AI 每日洞察报告 2026-04-10 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | AI 每日洞察报告 2026-04-10 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 10 页 |
| **Design Style** | 华为商务风格 |
| **Target Audience** | AI 行业从业者、技术决策者、投资人 |
| **Use Case** | 每日 AI 情报简报、内部参考 |
| **Created Date** | 2026-04-10 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 上下左右各 60px |
| **Content Area** | 1160×600 (60px 边距内) |

---

## III. Visual Theme

### Theme Style

- **Style**: 华为商务风格
- **Theme**: Light theme (浅色主题)
- **Tone**: 专业、简洁、科技感、严谨

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 页面背景 |
| **Secondary bg** | `#F8F9FA` | 卡片背景、区块背景 |
| **Primary** | `#CF002E` | 华为红 - 标题装饰、关键信息、图标 |
| **Accent** | `#0066CC` | 科技蓝 - 数据图表、链接 |
| **Secondary accent** | `#333333` | 深灰 - 次要强调 |
| **Body text** | `#333333` | 正文文字 |
| **Secondary text** | `#666666` | 辅助文字、图例 |
| **Tertiary text** | `#999999` | 注释、页脚 |
| **Border/divider** | `#E5E5E5` | 卡片边框、分隔线 |
| **Success** | `#00AA55` | 正向指标 |
| **Warning** | `#FF8800` | 关注点提示 |

### Gradient Scheme

```xml
<!-- 华为红渐变 (标题/背景装饰) -->
<linearGradient id="huaweiRedGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#CF002E"/>
  <stop offset="100%" stop-color="#8B0020"/>
</linearGradient>

<!-- 背景装饰渐变 -->
<radialGradient id="bgDecor" cx="90%" cy="10%" r="40%">
  <stop offset="0%" stop-color="#CF002E" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#CF002E" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Recommended preset**: P1 (现代商务/科技风格)

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | 微软雅黑 Bold | Arial Bold | 黑体 |
| **Body** | 微软雅黑 Regular | Arial Regular | 宋体 |
| **Code** | - | Consolas | Monaco |
| **Emphasis** | 微软雅黑 Bold | Arial Bold | 黑体 |

**Font stack**: `"Microsoft YaHei", "微软雅黑", Arial, sans-serif`

### Font Size Hierarchy

**Baseline**: Body font size = 20px (内容密度适中)

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 3x | 60px | Bold |
| Chapter title | 2.25x | 45px | Bold |
| Content title | 1.75x | 35px | Bold |
| Subtitle | 1.4x | 28px | SemiBold |
| **Body content** | **1x** | **20px** | Regular |
| Annotation | 0.8x | 16px | Regular |
| Page number/date | 0.65x | 13px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 80px - 页面标题 + 华为红装饰条
- **Content area**: 560px - 主要内容区
- **Footer area**: 80px - 页码、日期、信息来源

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | 封面页、核心摘要、结论页 |
| **Left-right split (5:5)** | 中美厂商对比、数据对比 |
| **Left-right split (4:6)** | 图文混排 |
| **Top-bottom split** | 时间线、流程展示 |
| **Three-column cards** | 多维度动态列表 |
| **Matrix grid** | 趋势预判表格 |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Content block gap | 32px |
| Card padding | 24px |
| Card border radius | 8px |
| Icon-text gap | 12px |
| Single-row card height | 260px |
| Double-row card height | 120px each |
| Three-column card width | 360px each |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/`
- **Usage method**: Placeholder format `{{icon:category/icon-name}}`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 大模型 | `{{icon:tech/brain}}` | Slide 03-04 |
| 中国厂商 | `{{icon:business/china}}` | Slide 05 |
| 美国厂商 | `{{icon:business/usa}}` | Slide 06 |
| 政策监管 | `{{icon:interface/shield}}` | Slide 07 |
| 趋势洞察 | `{{icon:tech/trending-up}}` | Slide 08-09 |
| 信息来源 | `{{icon:interface/link}}` | Slide 10 |

---

## VII. Chart Reference List

| Chart Type | Reference Template | Used In |
| ---------- | ------------------ | ------- |
| grouped_bar_chart | `templates/charts/grouped_bar_chart.svg` | Slide 03 (模型对比) |
| line_chart | `templates/charts/line_chart.svg` | Slide 09 (趋势预测) |
| stat_card | `templates/charts/stat_card.svg` | Slide 02 (核心指标) |

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Status | Generation Description |
| -------- | --------- | ----- | ------- | ---- | ------ | --------------------- |
| cover_bg.png | 1280×720 | 16:9 | 封面背景 | Background | Placeholder | 华为红渐变科技背景，右下角留白 |

---

## IX. Content Outline

### Part 1: 核心内容

#### Slide 01 - Cover

- **Layout**: 全 bleed 华为红渐变背景 + 居中标题
- **Title**: AI 每日洞察报告
- **Subtitle**: 2026 年 4 月 10 日
- **Info**: 零壹情报 | 全球 AI 前沿动态·中美厂商进展·商业化落地
- **Visual**: 华为红渐变背景，科技感装饰元素

#### Slide 02 - 核心摘要（30 秒速览）

- **Layout**: 三栏卡片布局
- **Title**: 核心摘要
- **Content**:
  - 卡片 1: 智谱 GLM-5.1 发布（8 小时持续工作）
  - 卡片 2: Kimi K2.5 登顶全球榜单
  - 卡片 3: 中国 AGI 通用智能体突破
- **Key conclusion**: 2026 年 Q2 开源模型已具备与闭源模型正面竞争能力

#### Slide 03 - 大模型动态（一）：智谱 GLM-5.1

- **Layout**: 左文右图（6:4）
- **Title**: 智谱 GLM-5.1 发布
- **Content**:
  - 全球首个支持 8 小时持续工作的开源模型
  - SWE-bench Pro 超越 Claude Opus 4.6
  - 8 小时构建 Linux 桌面（1200 余步操作）
  - 向量数据库优化吞吐提升 6.9 倍
  - 价格调整：提价 10%
- **Chart**: 模型性能对比柱状图

#### Slide 04 - 大模型动态（二）：Kimi K2.5 & Qwen3.5

- **Layout**: 双栏对比
- **Title**: Kimi K2.5 & 阿里 Qwen3.5
- **Content (左)**:
  - Kimi K2.5 发布 24 小时登顶 LMarena 开源模型首位
  - 可自主调度 100 个专业背景分身
  - 并行处理高达 1500 个步骤
  - Kilo Code 宣布成为默认模型
- **Content (右)**:
  - Qwen3.5-397B-A17B 混合专家架构
  - 总参数 3970 亿，激活仅 170 亿
  - 支持文本、图像和视频输入

#### Slide 05 - 中国厂商 AI 动态

- **Layout**: 三栏卡片
- **Title**: 中国厂商动态
- **Content**:
  - 卡片 1: 阿里云 CodingPlan（四大开源模型自由切换）
  - 卡片 2: MiniMax M2.5 登顶 OpenRouter 调用量榜首（3.07T tokens）
  - 卡片 3: 腾讯混元 2Bit 量化端侧大模型（生成速度提升 2-3 倍）

#### Slide 06 - 美国厂商 AI 动态

- **Layout**: 双栏布局
- **Title**: 美国厂商动态
- **Content (左)**:
  - OpenAI、Google 员工支持 Anthropic 在国防部诉讼中
  - 30+ 名员工提交法庭之友简报
  - 反映 AI 行业对军事应用的伦理担忧
- **Content (右)**:
  - Google DeepMind 发布 Genie 3 世界模型
  - 用户可生成世界模拟并实时交互
  - 社交媒体引发热议

#### Slide 07 - AI 政策与监管

- **Layout**: 单栏 + 时间线
- **Title**: AI 政策与监管
- **Content**:
  - 欧盟 AI 法案生效一周年
  - 2026 年 8 月大部分条款适用
  - 全球首部全面规范 AI 技术的综合性立法
  - 欧盟发布《通用人工智能行为准则》
- **Visual**: 时间线展示（2024.08 生效 → 2026.08 适用）

#### Slide 08 - 趋势洞察（一）：开源模型崛起

- **Layout**: 左文右图
- **Title**: 趋势一：开源模型能力追平闭源
- **Content**:
  - Kimi K2.5、GLM-5.1 等接近或超越 Claude、GPT
  - 智谱逆势提价 10%，从"低价获客"转向"价值定价"
  - 中小企业：可更低成本获得顶尖模型能力
  - 从业者：多模型路由能力成为核心竞争力
- **Chart**: 开源 vs 闭源模型性能对比趋势图

#### Slide 09 - 趋势洞察（二）：智能体长程任务

- **Layout**: 左文右图
- **Title**: 趋势二：智能体长程任务成为新战场
- **Content**:
  - GLM-5.1 实现 8 小时持续工作（1200 步复杂操作）
  - MiniMax M2.5 带动 100K-1M 长文本调用需求
  - 中小企业：可部署 7×24 小时自治智能体
  - 从业者：需掌握智能体编排、长程任务分解技能
- **Chart**: Agent 工作流调用量增长趋势线

#### Slide 10 - 信息来源

- **Layout**: 表格布局
- **Title**: 信息来源
- **Content**:
  - 表格列示：来源 | 可信度 | 链接数
  - IT 之家、21 经济网、WIRED、澎湃新闻等
  - 所有来源可信度⭐⭐⭐⭐⭐
- **Footer**: © 2026 零壹情报 | 每日更新

---

## X. Speaker Notes Requirements

为每页生成对应的演讲者备注，保存到 `notes/` 目录：

- **File naming**: 与 SVG 名称匹配，如 `01_cover.md`
- **Content includes**: 演讲要点、时间提示、过渡语句
- **Style**: 简洁口语化，每页备注 50-100 字

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`, `marker`/`marker-end`
7. Arrows use `<polygon>` triangles instead of `<marker>`

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set on each child element individually
- Image transparency uses overlay mask layer (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only; external CSS and `@font-face` FORBIDDEN

---

## XII. Design Checklist

### Pre-generation

- [x] Content fits page capacity (10 页，每页 3-5 个要点)
- [x] Layout mode selected correctly
- [x] Colors used semantically (华为红主色)

### Post-generation

- [ ] viewBox = `0 0 1280 720`
- [ ] No `<foreignObject>` elements
- [ ] All text readable (>=14px)
- [ ] Content within safe area (60px 边距)
- [ ] All elements aligned to grid
- [ ] Same elements maintain consistent style
- [ ] Colors conform to spec
- [ ] CRAP four-principle check passed

---

## XIII. Next Steps

1. ✅ Design spec complete
2. **Next step**: Invoke **Executor** role to generate SVGs (no AI images needed, use placeholder for cover background)

---

## Eight Confirmations（八项确认）

### 1. 画布格式确认 ✅
- [x] 16:9 比例 (1280×720)
- [x] 适合投影仪和屏幕演示

### 2. 色彩方案确认 ✅
- [x] 华为红 (#CF002E) 为主色
- [x] 深灰/白色为辅色
- [x] 色彩对比度符合无障碍标准

### 3. 字体选择确认 ✅
- [x] 无衬线字体（微软雅黑/Arial）
- [x] 字号层次清晰（60→45→35→20→16）
- [x] 中英文字体协调

### 4. 布局结构确认 ✅
- [x] 12 列网格系统
- [x] 安全边距 60px
- [x] 页面类型：封面/单栏/双栏/三栏

### 5. 图表类型确认 ✅
- [x] 柱状图：模型性能对比
- [x] 折线图：趋势展示
- [x] 数据卡片：核心指标
- [x] 表格：信息来源

### 6. 视觉风格确认 ✅
- [x] 简洁商务风格
- [x] 科技感元素（渐变、阴影）
- [x] 专业严谨对齐

### 7. 内容层次确认 ✅
- [x] 标题层级清晰（H1/H2/H3）
- [x] 重点信息突出（华为红/大字号）
- [x] 辅助信息降级（灰色/小字）

### 8. 输出格式确认 ✅
- [x] SVG 矢量图形
- [x] 可编辑 PPTX 导出
- [x] 兼容 Office 2016+

---

**设计规范版本**: v1.0  
**创建日期**: 2026-04-10  
**适用项目**: ai_daily_brief_20260410  
**状态**: 等待用户确认后进入 Executor 阶段
