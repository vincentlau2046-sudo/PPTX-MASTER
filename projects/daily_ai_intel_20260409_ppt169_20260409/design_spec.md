# daily_ai_intel_20260409 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | daily_ai_intel_20260409 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 13 页 |
| **Design Style** | Top Consulting (战略咨询风格) |
| **Target Audience** | AI 从业者、投资人、企业决策者 |
| **Use Case** | 每日 AI 情报视频播报 PPT |
| **Created Date** | 2026-04-09 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px, 上下 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: Top Consulting (战略咨询)
- **Theme**: Light theme (浅色主题)
- **Tone**: 专业、科技感、数据驱动、结论优先

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 页面背景 |
| **Secondary bg** | `#F8F9FA` | 卡片背景、分区背景 |
| **Primary** | `#1565C0` | 标题装饰、关键信息、图标（科技蓝） |
| **Accent** | `#FF6B35` | 数据高亮、重点信息（活力橙） |
| **Secondary accent** | `#00BFA5` | 次要强调、增长指标（青绿色） |
| **Body text** | `#1A1A1A` | 正文文本 |
| **Secondary text** | `#666666` | 副标题、注释 |
| **Tertiary text** | `#999999` | 补充信息、页脚 |
| **Border/divider** | `#E0E0E0` | 卡片边框、分割线 |
| **Success** | `#2E7D32` | 正向指标（绿色） |
| **Warning** | `#C62828` | 风险指标（红色） |

---

## IV. Typography System

### Font Plan

**Recommended preset**: P1 (现代商务/科技)

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | 微软雅黑 | Arial | 黑体 |
| **Body** | 微软雅黑 | Calibri | 宋体 |
| **Code** | - | Consolas | Monaco |
| **Emphasis** | 黑体 | Arial Black | 微软雅黑 Bold |

**Font stack**: `"Microsoft YaHei", "微软雅黑", Arial, "Helvetica Neue", sans-serif`

### Font Size Hierarchy

**Baseline**: Body font size = 18px (内容密集)

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 3x | 54px | Bold |
| Chapter title | 2.2x | 40px | Bold |
| Content title | 1.7x | 31px | Bold |
| Subtitle | 1.3x | 23px | SemiBold |
| **Body content** | **1x** | **18px** | Regular |
| Annotation | 0.78x | 14px | Regular |
| Page number/date | 0.61x | 11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 60px - 页眉装饰条 + 章节标识
- **Content area**: 580px - 主要内容区
- **Footer area**: 80px - 页脚信息 + 页码

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | 封面、结束页、关键结论 |
| **Left-right split (5:5)** | 对比分析、双概念 |
| **Left-right split (4:6)** | 图文混排 |
| **Top-bottom split** | 流程、时间线 |
| **Three/four column cards** | 特性列表、多维度对比 |
| **Matrix grid** | 对比分析、分类 |

### Spacing Specification

| Element | Current Project |
| ------- | --------------- |
| Card gap | 24px |
| Content block gap | 32px |
| Card padding | 24px |
| Card border radius | 8px |
| Icon-text gap | 12px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/`
- **Style**: tabler-outline (线条风格，专业感)
- **Usage method**: Placeholder format `{{icon:tabler-outline/icon-name}}`

### Icon List

| Purpose | Icon Path |
| ------- | --------- |
| 算力/GPU | `{{icon:tabler-outline/cpu}}` |
| 模型/AI | `{{icon:tabler-outline/robot}}` |
| 应用/入口 | `{{icon:tabler-outline/app-window}}` |
| 政治/监管 | `{{icon:tabler-outline/scale}}` |
| 经济/资本 | `{{icon:tabler-outline/currency-dollar}}` |
| 公司/企业 | `{{icon:tabler-outline/building}}` |
| 投资/融资 | `{{icon:tabler-outline/trending-up}}` |
| 机会/风险 | `{{icon:tabler-outline/compass}}` |
| 信号/趋势 | `{{icon:tabler-outline/signal}}` |
| 洞察/行动 | `{{icon:tabler-outline/lightbulb}}` |

---

## VII. Chart Reference List

| Chart Type | Reference Template | Used In |
| ---------- | ------------------ | ------- |
| kpi_cards | `templates/charts/kpi_cards.svg` | Slide 02 (60 秒速览) |
| grouped_bar_chart | `templates/charts/grouped_bar_chart.svg` | Slide 04 (模型对比) |
| donut_chart | `templates/charts/donut_chart.svg` | Slide 08 (渗透率) |
| matrix_2x2 | `templates/charts/matrix_2x2.svg` | Slide 14 (机会雷达) |
| bullet_chart | `templates/charts/bullet_chart.svg` | Slide 17 (趋势评分) |

---

## VIII. Eight Confirmations

### 1. Canvas Format Confirmation
✅ **PPT 16:9 (1280×720)** - 标准演示文稿格式，适合视频生成

### 2. Page Count Confirmation
✅ **13 页** - 根据源文档内容自动分析

### 3. Key Information Confirmation
✅ **Target Audience**: AI 从业者、投资人、企业决策者
✅ **Use Case**: 每日 AI 情报视频播报

### 4. Style Objective Confirmation
✅ **Top Consulting (战略咨询风格)** - 数据驱动、结论优先、逻辑严谨

### 5. Color Scheme Confirmation
✅ **科技蓝主题** - Primary: #1565C0, Accent: #FF6B35, Secondary: #00BFA5

### 6. Icon Usage Confirmation
✅ **tabler-outline 线条风格** - 专业感强，适合商务场景

### 7. Typography Plan Confirmation
✅ **P1 现代商务字体** - 微软雅黑 + Arial, Body 18px

### 8. Image Usage Confirmation
✅ **简洁设计 + 图表为主** - 无需 AI 生成图片，使用图表和图标

---

## IX. Content Outline (每页布局规划)

### Slide 01 - AI 全球情报日报

- **Layout**: Full-screen gradient background + centered title
- **Title**: AI 全球情报日报

- **Content**: 2026-04-09; 第 109 期; 零壹情报...

### Slide 02 - ⚡ 60 秒速览

- **Layout**: KPI Cards (6 卡片网格)
- **Title**: ⚡ 60 秒速览
- **Chart**: kpi_cards
- **Content**: | 类别 | 热度 | 关键事件 | 影响等级 |; |------|------|----------|----------|; | 🔌 算力 | 🔥🔥🔥🔥🔥 | NVIDIA Rubin 正式发布，50 PFLOPS FP4 | 战略级 |...

### Slide 03 - 🚀 重磅头条

- **Layout**: Left-right split (4:6)
- **Title**: 🚀 重磅头条

- **Content**: **为什么重要**：NVIDIA 在 GTC 2026 正式揭晓 Rubin 平台，单芯片 50 petaflops FP4 推理性能，较 Blackwell 提升 2.5-5 倍。这不仅是数字游戏——它意味着训练 MoE 模型所需 GPU 数量减少 4 倍，推理 token 成本下降 10 倍。; **关键数据**：; - 50 PFLOPS FP4 推理 / 35 PFLOPS FP4 训练...

### Slide 04 - 📊 PESTEL 宏观分析

- **Layout**: Left-right split (4:6)
- **Title**: 📊 PESTEL 宏观分析

- **Content**: - EU AI Act 高风险条款 2026 年 8 月 2 日生效，违规罚款最高达全球营收 7%; - 中国网络安全法修订案 2026 年 1 月生效，强化 AI 风险评估和伦理治理; - 韩国 AI Basic Act 2026 年 1 月 22 日生效，成为全球第二部综合性 AI 法律...

### Slide 05 - 🏢 巨头动向

- **Layout**: Left-right split (4:6)
- **Title**: 🏢 巨头动向

- **Content**: | 公司 | 核心动作 | 战略意图 |; |------|----------|----------|; | **NVIDIA** | Rubin 发布，2026 产能 20-30 万片 | 巩固算力垄断，强化定价权 |...

### Slide 06 - 💰 资本风向

- **Layout**: Left-right split (4:6)
- **Title**: 💰 资本风向

- **Content**: | 公司 | 金额 | 估值 | 投资方 | 赛道 |; |------|------|------|--------|------|; | Anthropic | - | $3500 亿 | Sequoia | 大模型 |...

### Slide 07 - 🎯 机会雷达

- **Layout**: Matrix 2x2 grid
- **Title**: 🎯 机会雷达
- **Chart**: matrix_2x2
- **Content**: | 领域 | 时间窗口 | 机会点 |; |------|----------|--------|; | AI 合同审查（SMB） | 3-6 月 | $99-499/月，法律科技空白 |...

### Slide 08 - 🔍 信号与噪声

- **Layout**: Left-right split (4:6)
- **Title**: 🔍 信号与噪声

- **Content**: 1. **推理成本下降 10 倍**：NVIDIA Rubin + 模型优化双重驱动，AI 应用经济性拐点已至; 2. **Agent 生态标准化**：MCP + A2A 协议形成事实标准，多 Agent 协作进入生产阶段; 3. **中国 AI 应用爆发**：豆包破亿、千问 3000 万，AI 从"尝鲜"转向"日常"...

### Slide 09 - 💡 洞察与行动

- **Layout**: Left-right split (4:6)
- **Title**: 💡 洞察与行动

- **Content**: 1. **算力仍是王道，但生态决定胜负**：NVIDIA Rubin 性能无敌，但 Google 的 ADK + A2A 生态可能成为企业 Agent 首选。选边站队比单纯追求性能更重要。; 2. **中国 AI 应用进入"人口红利"期**：豆包破亿不是偶然——14 亿人口的数字化基础 + 大厂生态整合，中国可能率先出现 AI 原生超级应用。; 3. **2026 年是"AI ROI 元年"**：资本耐心耗尽，95% 试点失败倒逼企业从"做什么 AI"转向"AI 带来什么价值"。能证明 ROI 的团队将活下来。...

### Slide 10 - 📈 趋势评分

- **Layout**: Single column with icons
- **Title**: 📈 趋势评分
- **Chart**: bullet_chart
- **Content**: | 趋势 | 热度 (1-10) | 变化 | 持续性 | 行动建议 |; |------|-------------|------|--------|----------|; | 推理成本下降 | 9 | ↑↑ | 12 月+ | 加速应用部署 |...

### Slide 11 - 🔗 关键链接

- **Layout**: Left-right split (4:6)
- **Title**: 🔗 关键链接

- **Content**: 1. [NVIDIA Rubin 官方发布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); 2. [GPT-5.4 vs Claude 4.6 vs Gemini 3.1 对比](https://tech-insider.org/chatgpt-vs-claude-vs-deepseek-vs-gemini-2026/); 3. [2026 AI 年度策略：大厂链入口争夺战](https://pdf.dfcfw.com/pdf/H3_AP202512151801025472_1.pdf)...

### Slide 12 - 💎 情报金句

- **Layout**: Left-right split (4:6)
- **Title**: 💎 情报金句

- **Content**: **📊 本期情报来源**：Tavily 高级搜索（6 大领域 30+ 信源）+ 专业研报 + 官方公告; **🔍 分析框架**：PESTEL 宏观分析 + 信号噪声过滤 + 机会雷达; **⏰ 更新时间**：2026 年 4 月 9 日 12:00（Asia/Shanghai）...

### Slide 13 - 感谢收看

- **Layout**: Centered conclusion
- **Title**: 感谢收看

- **Content**: 零壹情报 · 用外星智慧，解人间难题...


---

## X. Speaker Notes Requirements

- **File naming**: 与 SVG 名称匹配，如 `01_cover.md`
- **Content**: 每页 150-350 字口语播报稿（封面页 100 字以内）
- **Style**: conversational, 适合视频配音

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`

---

## XIII. Next Steps

1. ✅ Design spec complete
2. **Next step**: Invoke **Executor** role to generate SVGs (根据上述每页布局规划)
3. After SVG generation: Generate speaker notes, post-process, export PPTX
