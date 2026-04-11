# Huawei Technologies (华为技术有限公司) - Design Specification v2.0

> Suitable for Huawei's enterprise work reports, solution showcases, annual reports, product launches, strategic planning, high-end client communication and similar scenarios.

---

## I. Template Overview

| Property          | Description                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Template Name** | 华为技术有限公司                                                                                                                     |
| **Use Cases**     | Enterprise work reports, solution showcases, annual reports, product promotion, strategic planning, B2B client communication |
| **Design Tone**   | Minimalist tech, professional & rigorous, global business style, high-end industrial sense, modern technology                |
| **Theme Mode**    | Light theme (subtle tech textured background + Huawei red/tech gray refined accents)                                         |

---

## II. Canvas Specification

| Property         | Value                                |
| ---------------- | ------------------------------------ |
| **Format**       | Standard 16:9                        |
| **Dimensions**   | 1280 × 720 px                        |
| **viewBox**      | `0 0 1280 720`                       |
| **Safe Margins** | 40px (left/right), 35px (top/bottom) |
| **Safe Area**    | x: 40-1240, y: 70-665                |
| **Grid Base**    | 40px                                 |

---

## III. Color Scheme

### Core Colors

| Role                 | Color Value | Notes                                                                                |
| -------------------- | ----------- | ------------------------------------------------------------------------------------ |
| **Huawei Red**       | `#E60012`   | Brand primary color, used for accents, title bars, key highlights, brand identifiers |
| **Deep Tech Gray**   | `#191919`   | Primary text color, title text, deep background for chapter pages                    |
| **Medium Tech Gray** | `#595959`   | Secondary body text, auxiliary information                                           |
| **Light Tech Gray**  | `#F5F5F5`   | Page base background, card backgrounds, decorative areas                             |
| **Background White** | `#FFFFFF`   | Core content card backgrounds, highlight areas                                       |
| **Warm Gray Accent** | `#F8F8F8`   | Bottom decorative bars, secondary card backgrounds                                   |
| **Tech Blue Accent** | `#0052CC`   | Link text, data chart highlights, auxiliary accent color                             |

### Safe Area Anchor Points (Minimalist Tech Decoration)

```xml
<!-- Four-corner anchor points (replacing legacy card borders) -->

<path d="M40 140 L50 140 M40 140 L40 150" stroke="#E60012" stroke-width="1" stroke-opacity="0.5" />
<path d="M1240 140 L1230 140 M1240 140 L1240 150" stroke="#E60012" stroke-width="1" stroke-opacity="0.5" />
<path d="M40 650 L50 650 M40 650 L40 640" stroke="#191919" stroke-width="1" stroke-opacity="0.3" />
<path d="M1240 650 L1230 650 M1240 650 L1240 640" stroke="#191919" stroke-width="1" stroke-opacity="0.3" />
```
