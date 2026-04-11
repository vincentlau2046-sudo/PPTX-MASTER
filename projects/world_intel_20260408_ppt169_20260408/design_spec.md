# world_intel_20260408 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | world_intel_20260408 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 8 |
| **Design Style** | Professional Business Dark |
| **Target Audience** | 政府/企业决策者、国际事务关注者 |
| **Use Case** | 国际形势日报视频演示 |
| **Created Date** | 2026-04-08 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 60px, top/bottom 50px |
| **Content Area** | 1160×620 (60px margins) |

---

## III. Visual Theme

### Theme Style

- **Style**: Professional Business Dark
- **Theme**: Dark theme
- **Tone**: Professional, serious, authoritative, data-driven

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#0a1628` | Deep navy background |
| **Secondary bg** | `#1a2744` | Card background, section background |
| **Primary** | `#3b82f6` | Title decorations, key sections, icons (bright blue) |
| **Accent** | `#60a5fa` | Data highlights, key information (lighter blue) |
| **Secondary accent** | `#1e40af` | Gradient transitions (darker blue) |
| **Body text** | `#e5e7eb` | Main body text (light gray) |
| **Secondary text** | `#9ca3af` | Captions, annotations (medium gray) |
| **Tertiary text** | `#6b7280` | Supplementary info, footers (darker gray) |
| **Border/divider** | `#374151` | Card borders, divider lines |
| **Success** | `#10b981` | Positive indicators (green) |
| **Warning** | `#ef4444` | Risk markers (red) |
| **Caution** | `#f59e0b` | Caution markers (amber) |

### Gradient Scheme

```xml
<!-- Title gradient -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#3b82f6"/>
  <stop offset="100%" stop-color="#1e40af"/>
</linearGradient>

<!-- Background decorative gradient -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.1"/>
  <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Recommended preset**: P1 (Modern business/tech)

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | Microsoft YaHei Bold | Segoe UI Bold | Arial Bold |
| **Body** | Microsoft YaHei | Segoe UI | Arial |
| **Code** | - | Consolas | Monaco |
| **Emphasis** | Microsoft YaHei Bold | Segoe UI Bold | Arial Bold |

**Font stack**: `"Microsoft YaHei", "Segoe UI", Arial, sans-serif`

### Font Size Hierarchy

**Baseline**: Body font size = 20px (balanced content density)

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 3x | 60px | Bold |
| Chapter title | 2.2x | 44px | Bold |
| Content title | 1.8x | 36px | Bold |
| Subtitle | 1.4x | 28px | SemiBold |
| **Body content** | **1x** | **20px** | Regular |
| Annotation | 0.8x | 16px | Regular |
| Page number/date | 0.6x | 12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 60px - Title and date
- **Content area**: 560px - Main content
- **Footer area**: 50px - Page number and source

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | Covers, conclusions |
| **Left-right split (5:5)** | Comparisons, dual concepts |
| **Top-bottom split** | Processes, timelines |
| **Three/four column cards** | News items, briefs |
| **Matrix grid** | Data tables, market data |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Content block gap | 32px |
| Card padding | 24px |
| Card border radius | 12px |
| Icon-text gap | 12px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| News/Headline | `{{icon:communication/newspaper}}` | 2, 3 |
| Location/Region | `{{icon:maps/globe}}` | 4 |
| Market/Finance | `{{icon:finance/chart-line}}` | 5 |
| Brief/Quick | `{{icon:communication/lightning}}` | 6 |
| Forecast | `{{icon:weather/cloud-sun}}` | 7 |
| Warning/Risk | `{{icon:alert/triangle}}` | 2, 3 |

---

## VII. Chart Reference List

| Chart Type | Reference Template | Used In |
| ---------- | ------------------ | ------- |
| data_table | `templates/charts/data_table.svg` | Slide 5 |
| comparison_table | `templates/charts/comparison_table.svg` | Slide 4, 7 |
| info_cards | `templates/charts/info_cards.svg` | Slide 6 |

---

## VIII. Image Resource List

No AI images required. All content is text and data-based.

---

## IX. Content Outline

### Slide 01 - Cover

- **Layout**: Full-screen dark background + centered title
- **Title**: 国际形势日报
- **Subtitle**: 2026 年 4 月 8 日（周三）
- **Info**: AI 自动生成 | 每日更新

### Slide 02 - 头条深度：美伊停火谈判

- **Layout**: Left title + right content
- **Title**: 美伊停火谈判陷入僵局
- **Content**: 
  - 霍尔木兹海峡关闭现状
  - 特朗普最后期限
  - 风险信号：高危
- **Visual**: Warning indicator (red)

### Slide 03 - 头条深度：俄乌能源互袭

- **Layout**: Left title + right content
- **Title**: 俄乌能源设施互袭升级
- **Content**:
  - 双方互相袭击能源设施
  - 谈判暂停状态
  - 风险信号：中危
- **Visual**: Caution indicator (amber)

### Slide 04 - 区域要闻

- **Layout**: Three-column cards
- **Title**: 区域要闻
- **Content**:
  - 亚太：台海/朝鲜半岛/南海
  - 欧洲：能源危机/欧盟政策
  - 中东/美洲：伊朗局势/OPEC+
- **Visual**: Risk level indicators

### Slide 05 - 全球市场

- **Layout**: Data table
- **Title**: 全球市场数据
- **Content**:
  - 油价：布伦特$109.30, WTI$103.20
  - 金价：$4,774.65/盎司
  - 美股：标普 6,616.85
  - 汇率：美元/人民币 6.8609

### Slide 06 - 简讯速读

- **Layout**: Bullet list with icons
- **Title**: 简讯速读
- **Content**: 8 条一句话新闻
- **Visual**: Lightning icons for each item

### Slide 07 - 今日看点

- **Layout**: Forecast table
- **Title**: 今日看点（4 月 9 日预判）
- **Content**:
  - 美伊最后期限截止 ⭐⭐⭐⭐⭐
  - 美国 3 月 CPI 数据 ⭐⭐⭐⭐
  - OPEC+ 增产实施 ⭐⭐⭐

### Slide 08 - 封底

- **Layout**: Centered
- **Title**: 感谢观看
- **Subtitle**: 明日同一时间更新
- **Info**: 数据来源：公开新闻报道 | 仅供参考

---

## X. Speaker Notes Requirements

Generate corresponding speaker note files for each page, saved to the `notes/` directory:

- **File naming**: Match SVG names, e.g., `01_cover.md`
- **Content includes**: Script key points, timing cues, transition phrases

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

- [x] Content fits page capacity
- [x] Layout mode selected correctly
- [x] Colors used semantically

### Post-generation

- [ ] viewBox = `0 0 1280 720`
- [ ] No `<foreignObject>` elements
- [ ] All text readable (>=14px)
- [ ] Content within safe area
- [ ] All elements aligned to grid
- [ ] Same elements maintain consistent style
- [ ] Colors conform to spec
- [ ] CRAP four-principle check passed

---

## XIII. Next Steps

1. ✅ Design spec complete
2. **Next step**: Invoke **Executor** role to generate SVGs
