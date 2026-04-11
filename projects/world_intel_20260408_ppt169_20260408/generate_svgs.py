#!/usr/bin/env python3
"""Generate SVG slides for world_intel_20260408 project."""

import os
from datetime import datetime

PROJECT_DIR = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/world_intel_20260408_ppt169_20260408"
SVG_OUTPUT = os.path.join(PROJECT_DIR, "svg_output")
SVG_FINAL = os.path.join(PROJECT_DIR, "svg_final")

os.makedirs(SVG_OUTPUT, exist_ok=True)
os.makedirs(SVG_FINAL, exist_ok=True)

# Color scheme
BG_COLOR = "#0a1628"
CARD_BG = "#1a2744"
PRIMARY = "#3b82f6"
ACCENT = "#60a5fa"
TEXT_PRIMARY = "#e5e7eb"
TEXT_SECONDARY = "#9ca3af"
WARNING = "#ef4444"
CAUTION = "#f59e0b"
SUCCESS = "#10b981"

def create_svg(filename, content):
    """Create an SVG file."""
    svg_path = os.path.join(SVG_OUTPUT, filename)
    with open(svg_path, 'w') as f:
        f.write(content)
    
    # Copy to final
    final_path = os.path.join(SVG_FINAL, filename)
    with open(final_path, 'w') as f:
        f.write(content)
    
    print(f"  ✓ {filename}")

# Slide 1: Cover
slide1 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  <rect x="0" y="0" width="1280" height="720" fill="url(#bgDecor)"/>
  
  <defs>
    <radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
      <stop offset="0%" stop-color="{PRIMARY}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{PRIMARY}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PRIMARY}"/>
      <stop offset="100%" stop-color="#1e40af"/>
    </linearGradient>
  </defs>
  
  <!-- Title -->
  <text x="640" y="280" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="60" font-weight="bold" fill="url(#titleGradient)">国际形势日报</text>
  
  <!-- Date -->
  <text x="640" y="360" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="32" fill="{TEXT_PRIMARY}">2026 年 4 月 8 日（周三）</text>
  
  <!-- Footer -->
  <text x="640" y="650" text-anchor="middle" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">AI 自动生成 | 每日更新</text>
</svg>'''
create_svg("01_cover.svg", slide1)

# Slide 2: Headline 1 - US-Iran
slide2 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">头条深度</text>
  
  <!-- Risk indicator -->
  <rect x="1000" y="60" width="200" height="40" fill="{WARNING}" rx="8"/>
  <text x="1100" y="88" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FFFFFF">🔴 高危</text>
  
  <!-- Content -->
  <text x="100" y="170" font-family="Microsoft YaHei, Arial" font-size="32" font-weight="bold" fill="{TEXT_PRIMARY}">美伊停火谈判陷入僵局</text>
  <text x="100" y="220" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_SECONDARY}">霍尔木兹海峡持续关闭</text>
  
  <!-- Key points -->
  <rect x="100" y="260" width="1080" height="320" fill="{CARD_BG}" rx="12"/>
  
  <text x="140" y="310" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 特朗普设定 4 月 7 日晚 8 时为最后期限</text>
  <text x="140" y="350" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 要求伊朗重新开放霍尔木兹海峡</text>
  <text x="140" y="390" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 海峡关闭导致全球每日减少 1200-1500 万桶石油供应</text>
  <text x="140" y="430" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 伊朗已发射约 500 枚导弹袭击以色列</text>
  <text x="140" y="470" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 若谈判破裂，美国可能打击伊朗民用基础设施</text>
  
  <!-- Source -->
  <text x="100" y="650" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">来源：新华网 | 俄罗斯卫星通讯社</text>
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">2 / 8</text>
</svg>'''
create_svg("02_headline_us_iran.svg", slide2)

# Slide 3: Headline 2 - Russia-Ukraine
slide3 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">头条深度</text>
  
  <!-- Risk indicator -->
  <rect x="1000" y="60" width="200" height="40" fill="{CAUTION}" rx="8"/>
  <text x="1100" y="88" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FFFFFF">🟡 中危</text>
  
  <!-- Content -->
  <text x="100" y="170" font-family="Microsoft YaHei, Arial" font-size="32" font-weight="bold" fill="{TEXT_PRIMARY}">俄乌能源设施互袭升级</text>
  <text x="100" y="220" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_SECONDARY}">谈判处于暂停状态</text>
  
  <!-- Key points -->
  <rect x="100" y="260" width="1080" height="320" fill="{CARD_BG}" rx="12"/>
  
  <text x="140" y="310" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 俄对乌克兰敖德萨发动大规模无人机袭击</text>
  <text x="140" y="350" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 乌反击袭击俄罗斯新罗西斯克港石油设施</text>
  <text x="140" y="390" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 俄罗斯境内约 50 万户家庭遭遇停电</text>
  <text x="140" y="430" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 乌称自 1 月底以来收复 480 平方公里领土</text>
  <text x="140" y="470" font-family="Microsoft YaHei, Arial" font-size="20" fill="{TEXT_PRIMARY}">• 三方谈判暂停，双边接触仍在继续</text>
  
  <!-- Source -->
  <text x="100" y="650" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">来源：网易</text>
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">3 / 8</text>
</svg>'''
create_svg("03_headline_russia_ukraine.svg", slide3)

# Slide 4: Regional News
slide4 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">区域要闻</text>
  
  <!-- Three columns -->
  <!-- Asia Pacific -->
  <rect x="60" y="140" width="360" height="440" fill="{CARD_BG}" rx="12"/>
  <text x="240" y="180" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="24" font-weight="bold" fill="{PRIMARY}">🌏 亚太</text>
  <text x="80" y="220" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 台海：两岸关系持续冰封</text>
  <text x="80" y="250" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 朝鲜：战术突击手定位</text>
  <text x="80" y="280" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 日韩：重启海上联合演习</text>
  <text x="80" y="310" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 南海：无人集群跨域协同演习</text>
  
  <!-- Europe -->
  <rect x="460" y="140" width="360" height="440" fill="{CARD_BG}" rx="12"/>
  <text x="640" y="180" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="24" font-weight="bold" fill="{PRIMARY}">🇪🇺 欧洲</text>
  <text x="480" y="220" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 能源危机：或演变为财政危机</text>
  <text x="480" y="250" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 欧盟政策：70% 欧洲制造遇阻</text>
  <text x="480" y="280" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 左翼力量：经济困境中复兴</text>
  
  <!-- Middle East/Americas -->
  <rect x="860" y="140" width="360" height="440" fill="{CARD_BG}" rx="12"/>
  <text x="1040" y="180" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="24" font-weight="bold" fill="{PRIMARY}">🌎 中东/美洲</text>
  <text x="880" y="220" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 伊朗：加大反击力度</text>
  <text x="880" y="250" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• 美国：特朗普对协议不乐观</text>
  <text x="880" y="280" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">• OPEC+: 4 月起日增 20.6 万桶</text>
  
  <!-- Footer -->
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">4 / 8</text>
</svg>'''
create_svg("04_regional_news.svg", slide4)

# Slide 5: Global Market
slide5 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">全球市场</text>
  
  <!-- Data table -->
  <rect x="100" y="140" width="1080" height="480" fill="{CARD_BG}" rx="12"/>
  
  <!-- Header row -->
  <rect x="100" y="140" width="1080" height="50" fill="#253559" rx="12"/>
  <text x="200" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">类别</text>
  <text x="450" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">指标</text>
  <text x="750" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">价格</text>
  <text x="1000" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">涨跌</text>
  
  <!-- Data rows -->
  <text x="200" y="230" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">油价</text>
  <text x="450" y="230" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">布伦特原油</text>
  <text x="750" y="230" font-family="Arial" font-size="18" fill="{SUCCESS}">$109.30/桶</text>
  <text x="1000" y="230" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">-0.46%</text>
  
  <text x="450" y="265" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">WTI 原油</text>
  <text x="750" y="265" font-family="Arial" font-size="18" fill="{SUCCESS}">$103.20/桶</text>
  <text x="1000" y="265" font-family="Arial" font-size="18" fill="{WARNING}">-8.67%</text>
  
  <text x="200" y="315" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">金价</text>
  <text x="450" y="315" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">现货黄金</text>
  <text x="750" y="315" font-family="Arial" font-size="18" fill="{SUCCESS}">$4,774.65/盎司</text>
  <text x="1000" y="315" font-family="Arial" font-size="18" fill="{SUCCESS}">+1.46%</text>
  
  <text x="200" y="365" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">美股</text>
  <text x="450" y="365" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">标普 500</text>
  <text x="750" y="365" font-family="Arial" font-size="18" fill="{TEXT_PRIMARY}">6,616.85</text>
  <text x="1000" y="365" font-family="Arial" font-size="18" fill="{SUCCESS}">+0.08%</text>
  
  <text x="450" y="400" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">纳斯达克</text>
  <text x="750" y="400" font-family="Arial" font-size="18" fill="{TEXT_PRIMARY}">22,017.85</text>
  <text x="1000" y="400" font-family="Arial" font-size="18" fill="{SUCCESS}">+0.10%</text>
  
  <text x="200" y="450" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">汇率</text>
  <text x="450" y="450" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">美元/人民币</text>
  <text x="750" y="450" font-family="Arial" font-size="18" fill="{TEXT_PRIMARY}">6.8609</text>
  <text x="1000" y="450" font-family="Arial" font-size="18" fill="{TEXT_SECONDARY}">—</text>
  
  <!-- Footer -->
  <text x="100" y="650" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">数据来源：网易财经 | Mitrade</text>
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">5 / 8</text>
</svg>'''
create_svg("05_global_market.svg", slide5)

# Slide 6: News Briefs
slide6 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">简讯速读</text>
  
  <!-- News items -->
  <rect x="100" y="140" width="1080" height="480" fill="{CARD_BG}" rx="12"/>
  
  <text x="140" y="190" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 巴基斯坦拟定停火框架方案，拟先实现立即停火</text>
  <text x="140" y="225" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 伊朗称美以袭击造成超 10.5 万处民用设施受损</text>
  <text x="140" y="260" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 乌克兰对俄罗斯列宁格勒州石油设施发动袭击</text>
  <text x="140" y="295" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 俄罗斯防空系统 24 小时内击落 148 架无人机</text>
  <text x="140" y="330" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 欧盟要求成员国限制能源补贴防止金融危机</text>
  <text x="140" y="365" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 中国央行连续 17 个月增持黄金</text>
  <text x="140" y="400" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 日韩时隔九年重启海上搜救联合演习</text>
  <text x="140" y="435" font-family="Microsoft YaHei, Arial" font-size="18" fill="{TEXT_PRIMARY}">⚡ 美国 3 月 CPI 数据今日公布</text>
  
  <!-- Footer -->
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">6 / 8</text>
</svg>'''
create_svg("06_news_briefs.svg", slide6)

# Slide 7: Today's Highlights
slide7 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  
  <!-- Header -->
  <rect x="60" y="50" width="1160" height="60" fill="{CARD_BG}" rx="12"/>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}">今日看点</text>
  <text x="100" y="90" font-family="Microsoft YaHei, Arial" font-size="36" font-weight="bold" fill="{PRIMARY}" x="300">（4 月 9 日预判）</text>
  
  <!-- Forecast table -->
  <rect x="100" y="140" width="1080" height="480" fill="{CARD_BG}" rx="12"/>
  
  <!-- Header -->
  <rect x="100" y="140" width="1080" height="50" fill="#253559" rx="12"/>
  <text x="150" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">事件</text>
  <text x="550" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">时间</text>
  <text x="800" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">重要性</text>
  <text x="1000" y="175" font-family="Arial" font-size="18" font-weight="bold" fill="{TEXT_PRIMARY}">预期影响</text>
  
  <!-- Rows -->
  <text x="150" y="230" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">美伊最后期限截止</text>
  <text x="550" y="230" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">4 月 7 日 20 时</text>
  <text x="800" y="230" font-family="Arial" font-size="16" fill="{WARNING}">⭐⭐⭐⭐⭐</text>
  <text x="1000" y="230" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_SECONDARY}">油价或突破$120</text>
  
  <text x="150" y="275" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">美国 3 月 CPI 数据</text>
  <text x="550" y="275" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">20:30</text>
  <text x="800" y="275" font-family="Arial" font-size="16" fill="{ACCENT}">⭐⭐⭐⭐</text>
  <text x="1000" y="275" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_SECONDARY}">影响美联储预期</text>
  
  <text x="150" y="320" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">OPEC+ 增产实施</text>
  <text x="550" y="320" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">4 月起</text>
  <text x="800" y="320" font-family="Arial" font-size="16" fill="{ACCENT}">⭐⭐⭐</text>
  <text x="1000" y="320" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_SECONDARY}">实际供应难增加</text>
  
  <text x="150" y="365" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_PRIMARY}">俄乌谈判进展</text>
  <text x="550" y="365" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">待定</text>
  <text x="800" y="365" font-family="Arial" font-size="16" fill="{ACCENT}">⭐⭐⭐</text>
  <text x="1000" y="365" font-family="Microsoft YaHei, Arial" font-size="16" fill="{TEXT_SECONDARY}">双边接触继续</text>
  
  <!-- Footer -->
  <text x="1200" y="650" text-anchor="end" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">7 / 8</text>
</svg>'''
create_svg("07_todays_highlights.svg", slide7)

# Slide 8: Back Cover
slide8 = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="{BG_COLOR}"/>
  <rect x="0" y="0" width="1280" height="720" fill="url(#bgDecor)"/>
  
  <defs>
    <radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
      <stop offset="0%" stop-color="{PRIMARY}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{PRIMARY}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  
  <!-- Main text -->
  <text x="640" y="280" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="48" font-weight="bold" fill="{TEXT_PRIMARY}">感谢观看</text>
  
  <text x="640" y="360" text-anchor="middle" font-family="Microsoft YaHei, Arial" font-size="28" fill="{TEXT_SECONDARY}">明日同一时间更新</text>
  
  <!-- Footer -->
  <text x="640" y="600" text-anchor="middle" font-family="Arial" font-size="16" fill="{TEXT_SECONDARY}">数据来源：公开新闻报道 | 仅供参考，不构成投资建议</text>
  <text x="640" y="650" text-anchor="middle" font-family="Arial" font-size="14" fill="{TEXT_SECONDARY}">AI 自动生成 | 2026-04-08</text>
</svg>'''
create_svg("08_back_cover.svg", slide8)

print(f"\n✅ 已生成 8 个 SVG 文件到 {SVG_OUTPUT}")
print(f"✅ 已复制到 {SVG_FINAL}")
