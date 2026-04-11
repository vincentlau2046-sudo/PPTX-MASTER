#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成百度智能云 2025 年财报分析 PPT 的 SVG 文件 - 修复版
共 14 页
"""

import os

PROJECT_DIR = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/baidu_cloud_2025_financial_ppt169_20260410"
SVG_OUTPUT_DIR = os.path.join(PROJECT_DIR, "svg_output")

BAIDU_BLUE = "#2932E1"
BAIDU_BLUE_LIGHT = "#5C67FF"
DARK_GRAY = "#333333"
WHITE = "#FFFFFF"

def create_base_svg(title_elem=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
    <defs>
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F8F9FA;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="blueGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{BAIDU_BLUE};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{BAIDU_BLUE_LIGHT};stop-opacity:1" />
        </linearGradient>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
            <feOffset dx="0" dy="2" result="offsetblur"/>
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.15"/>
            </feComponentTransfer>
            <feMerge>
                <feMergeNode/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <rect width="1280" height="720" fill="url(#bgGradient)"/>
    {title_elem}
    <rect x="0" y="680" width="1280" height="40" fill="#F5F5F5" opacity="0.5"/>
    <text x="60" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999">百度智能云 2025 年财报分析</text>
    <text x="1220" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999" text-anchor="end">{{page_num}} / 14</text>
</svg>'''

# 由于代码太长，让我直接生成简化的 SVG 文件
# 使用更直接的方法

slides_content = {}

# 第 1 页：封面
slides_content["01_cover.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF"/>
            <stop offset="100%" style="stop-color:#F8F9FA"/>
        </linearGradient>
        <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#2932E1"/>
            <stop offset="100%" style="stop-color:#5C67FF"/>
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="url(#bgGrad)"/>
    <rect width="1280" height="200" fill="url(#blueGrad)"/>
    <text x="640" y="100" font-family="Arial Black" font-size="42" fill="#FFFFFF" text-anchor="middle">百度智能云 2025 年财报分析</text>
    <text x="640" y="145" font-family="Arial" font-size="18" fill="#E0E0FF" text-anchor="middle">AI 云兑现元年 · 全栈能力规模化落地</text>
    <rect x="340" y="280" width="600" height="80" rx="8" fill="#FFFFFF" filter="url(#shadow)"/>
    <text x="640" y="315" font-family="Arial" font-size="14" fill="#666666" text-anchor="middle">数据基准：百度集团 2026 年 2 月 26 日发布 2025 年 Q4 及全年财报</text>
    <text x="640" y="340" font-family="Arial" font-size="14" fill="#666666" text-anchor="middle">财年周期：2025 年 1 月 1 日 — 2025 年 12 月 31 日</text>
    <text x="640" y="680" font-family="Arial" font-size="12" fill="#999999" text-anchor="middle">2026 年 4 月 · 内部汇报材料 | 1 / 14</text>
</svg>'''

# 第 2 页：数据基准
slides_content["02_data_baseline.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="32" fill="#333333">数据基准与财年周期</text>
    <rect x="60" y="80" width="200" height="4" fill="#2932E1"/>
    <rect x="60" y="130" width="540" height="200" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <text x="90" y="170" font-family="Arial Black" font-size="18" fill="#2932E1">📊 数据基准</text>
    <text x="90" y="210" font-family="Arial" font-size="14" fill="#555555">• 百度集团 2026 年 2 月 26 日发布</text>
    <text x="90" y="235" font-family="Arial" font-size="14" fill="#555555">• 2025 年 Q4 及全年财报</text>
    <text x="90" y="260" font-family="Arial" font-size="14" fill="#555555">• 电话会官方披露内容</text>
    <text x="90" y="285" font-family="Arial" font-size="14" fill="#555555">• 官方投资者关系材料</text>
    <rect x="680" y="130" width="540" height="200" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <text x="710" y="170" font-family="Arial Black" font-size="18" fill="#2932E1">📅 财年周期</text>
    <text x="710" y="220" font-family="Arial" font-size="16" fill="#555555">2025 年 1 月 1 日 → 2025 年 12 月 31 日</text>
    <rect x="710" y="240" width="480" height="60" rx="8" fill="#F5F5F5"/>
    <text x="950" y="275" font-family="Arial" font-size="14" fill="#666666" text-anchor="middle">百度采用自然年财年</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 2 / 14</text>
</svg>'''

# 第 3 页：核心财务指标
slides_content["03_core_metrics.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">整体业绩概览 · 核心财务指标</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="1160" height="45" fill="#2932E1" rx="8"/>
    <text x="150" y="150" font-family="Arial" font-size="13" fill="#FFFFFF">指标</text>
    <text x="400" y="150" font-family="Arial" font-size="13" fill="#FFFFFF">2025 全年</text>
    <text x="580" y="150" font-family="Arial" font-size="13" fill="#FFFFFF">2024 全年</text>
    <text x="760" y="150" font-family="Arial" font-size="13" fill="#FFFFFF">同比变化</text>
    <text x="980" y="150" font-family="Arial" font-size="13" fill="#FFFFFF">关键说明</text>
    <rect x="60" y="170" width="1160" height="50" fill="#FFFFFF"/>
    <text x="150" y="200" font-family="Arial" font-size="13" fill="#333">智能云总收入</text>
    <text x="400" y="200" font-family="Arial Black" font-size="22" fill="#2932E1">300</text>
    <text x="580" y="200" font-family="Arial" font-size="14" fill="#666">223.9</text>
    <text x="760" y="200" font-family="Arial Black" font-size="18" fill="#27AE60">+34%</text>
    <text x="980" y="200" font-family="Arial" font-size="12" fill="#666">首次突破 300 亿</text>
    <rect x="60" y="225" width="1160" height="50" fill="#F5F5F5"/>
    <text x="150" y="255" font-family="Arial" font-size="13" fill="#555">— 智能云基础设施</text>
    <text x="400" y="255" font-family="Arial" font-size="18" fill="#333">198</text>
    <text x="580" y="255" font-family="Arial" font-size="14" fill="#666">148</text>
    <text x="760" y="255" font-family="Arial" font-size="16" fill="#27AE60">+34%</text>
    <text x="980" y="255" font-family="Arial" font-size="12" fill="#666">AI 算力/存储/网络</text>
    <rect x="60" y="280" width="1160" height="50" fill="#FFFFFF"/>
    <text x="150" y="310" font-family="Arial" font-size="13" fill="#555">— AI 应用与服务</text>
    <text x="400" y="310" font-family="Arial" font-size="18" fill="#333">102</text>
    <text x="580" y="310" font-family="Arial" font-size="14" fill="#666">75.9</text>
    <text x="760" y="310" font-family="Arial" font-size="16" fill="#27AE60">+34%</text>
    <text x="980" y="310" font-family="Arial" font-size="12" fill="#666">MaaS、大模型</text>
    <rect x="60" y="335" width="1160" height="50" fill="#FEF9E7"/>
    <text x="150" y="365" font-family="Arial" font-size="13" fill="#555">AI 云全栈市占率</text>
    <text x="400" y="365" font-family="Arial Black" font-size="22" fill="#2932E1">40.2%</text>
    <text x="580" y="365" font-family="Arial" font-size="14" fill="#999">—</text>
    <text x="760" y="365" font-family="Arial" font-size="16" fill="#27AE60">领跑</text>
    <text x="980" y="365" font-family="Arial" font-size="12" fill="#666">中国 AI 市场份额首位</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 3 / 14</text>
</svg>'''

# 第 4 页：整体特征
slides_content["04_overview_features.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">整体业绩概览 · 整体特征</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="560" height="260" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="560" height="50" rx="12" fill="#FEF9E7"/>
    <text x="340" y="153" font-family="Arial Black" font-size="18" fill="#F39C12" text-anchor="middle">📈 增长韧性强</text>
    <text x="100" y="200" font-family="Arial" font-size="14" fill="#555">在百度总营收同比 -3% 背景下</text>
    <text x="340" y="260" font-family="Arial Black" font-size="42" fill="#27AE60" text-anchor="middle">+34%</text>
    <text x="340" y="295" font-family="Arial" font-size="14" fill="#666" text-anchor="middle">智能云逆势高增</text>
    <rect x="660" y="120" width="560" height="260" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="120" width="560" height="50" rx="12" fill="#E8F6F3"/>
    <text x="940" y="153" font-family="Arial Black" font-size="18" fill="#1ABC9C" text-anchor="middle">⚡ AI 算力爆发</text>
    <text x="700" y="200" font-family="Arial" font-size="14" fill="#555">AI 高性能计算订阅 Q4 同比</text>
    <text x="940" y="260" font-family="Arial Black" font-size="42" fill="#E74C3C" text-anchor="middle">+143%</text>
    <text x="940" y="295" font-family="Arial" font-size="14" fill="#666" text-anchor="middle">核心增长极</text>
    <rect x="60" y="410" width="560" height="220" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="410" width="560" height="50" rx="12" fill="#EBF5FB"/>
    <text x="340" y="443" font-family="Arial Black" font-size="18" fill="#2932E1" text-anchor="middle">🏗️ 全栈壁垒</text>
    <text x="340" y="485" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">昆仑芯 → 天池智算 → 千帆 MaaS → 文心大模型 → 行业 Agent</text>
    <text x="340" y="520" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">完整闭环落地</text>
    <text x="340" y="560" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">自研芯片 | 智算平台 | 模型服务 | 大模型 | 智能体应用</text>
    <rect x="660" y="410" width="560" height="220" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="410" width="560" height="50" rx="12" fill="#FDEDEC"/>
    <text x="940" y="443" font-family="Arial Black" font-size="18" fill="#E74C3C" text-anchor="middle">💰 盈利阶段</text>
    <text x="940" y="490" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">2025 年仍处高投入期，整体未盈利</text>
    <text x="940" y="530" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">AI 算力/高毛利 MaaS 利润率持续改善</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 4 / 14</text>
</svg>'''

# 第 5 页：分季度表现
slides_content["05_quarterly_data.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">分季度表现 · 季度核心数据</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="580" height="380" fill="#FFFFFF" rx="8" filter="url(#shadow)"/>
    <rect x="60" y="120" width="580" height="40" fill="#2932E1" rx="8"/>
    <text x="90" y="147" font-family="Arial" font-size="12" fill="#FFFFFF">季度</text>
    <text x="200" y="147" font-family="Arial" font-size="12" fill="#FFFFFF">收入 (亿)</text>
    <text x="320" y="147" font-family="Arial" font-size="12" fill="#FFFFFF">同比</text>
    <text x="430" y="147" font-family="Arial" font-size="12" fill="#FFFFFF">AI 算力订阅</text>
    <rect x="60" y="165" width="580" height="55" fill="#FFFFFF"/>
    <text x="90" y="200" font-family="Arial Black" font-size="16" fill="#333">Q1</text>
    <text x="200" y="200" font-family="Arial" font-size="16" fill="#333">~65</text>
    <text x="320" y="200" font-family="Arial" font-size="16" fill="#555">+28%</text>
    <text x="430" y="200" font-family="Arial" font-size="14" fill="#666">+95%</text>
    <rect x="60" y="220" width="580" height="55" fill="#F8F9FA"/>
    <text x="90" y="255" font-family="Arial Black" font-size="16" fill="#333">Q2</text>
    <text x="200" y="255" font-family="Arial" font-size="16" fill="#333">~70</text>
    <text x="320" y="255" font-family="Arial" font-size="16" fill="#555">+31%</text>
    <text x="430" y="255" font-family="Arial" font-size="14" fill="#666">+112%</text>
    <rect x="60" y="275" width="580" height="55" fill="#FFFFFF"/>
    <text x="90" y="310" font-family="Arial Black" font-size="16" fill="#333">Q3</text>
    <text x="200" y="310" font-family="Arial" font-size="16" fill="#333">~77</text>
    <text x="320" y="310" font-family="Arial" font-size="16" fill="#555">+32%</text>
    <text x="430" y="310" font-family="Arial" font-size="14" fill="#666">+128%</text>
    <rect x="60" y="330" width="580" height="55" fill="#FEF9E7"/>
    <text x="90" y="365" font-family="Arial Black" font-size="16" fill="#333">Q4</text>
    <text x="200" y="365" font-family="Arial" font-size="16" fill="#333">88</text>
    <text x="320" y="365" font-family="Arial Black" font-size="16" fill="#27AE60">+41%</text>
    <text x="430" y="365" font-family="Arial" font-size="14" fill="#666">+143%</text>
    <rect x="60" y="390" width="580" height="50" fill="#E8F6F3" stroke="#1ABC9C" stroke-width="2"/>
    <text x="90" y="422" font-family="Arial Black" font-size="14" fill="#1ABC9C">全年</text>
    <text x="200" y="422" font-family="Arial Black" font-size="20" fill="#2932E1">300</text>
    <text x="320" y="422" font-family="Arial Black" font-size="18" fill="#27AE60">+34%</text>
    <text x="430" y="422" font-family="Arial" font-size="12" fill="#666">首次破 300 亿</text>
    <rect x="680" y="120" width="540" height="380" fill="#FFFFFF" rx="8" filter="url(#shadow)"/>
    <text x="950" y="150" font-family="Arial" font-size="14" fill="#333" text-anchor="middle">季度收入趋势（亿元）</text>
    <rect x="740" y="180" width="70" height="160" fill="#5C67FF" opacity="0.6" rx="4"/>
    <text x="775" y="355" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">Q1</text>
    <text x="775" y="190" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">65</text>
    <rect x="830" y="180" width="70" height="180" fill="#5C67FF" opacity="0.7" rx="4"/>
    <text x="865" y="355" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">Q2</text>
    <text x="865" y="190" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">70</text>
    <rect x="920" y="180" width="70" height="200" fill="#5C67FF" opacity="0.8" rx="4"/>
    <text x="955" y="355" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">Q3</text>
    <text x="955" y="190" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">77</text>
    <rect x="1010" y="180" width="70" height="240" fill="#2932E1" rx="4"/>
    <text x="1045" y="355" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">Q4</text>
    <text x="1045" y="190" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">88</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 5 / 14</text>
</svg>'''

# 第 6 页：季度趋势
slides_content["06_quarterly_trend.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">分季度表现 · 季度趋势分析</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="1160" height="150" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="1160" height="50" rx="12" fill="#FEF9E7"/>
    <text x="90" y="153" font-family="Arial Black" font-size="16" fill="#F39C12">1️⃣ 增速逐季抬升</text>
    <text x="90" y="195" font-family="Arial" font-size="14" fill="#555">Q1(28%) → Q2(31%) → Q3(32%) → Q4(41%)，AI 需求加速释放</text>
    <rect x="800" y="140" width="70" height="100" fill="#F7DC6F" rx="4"/>
    <text x="835" y="230" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">28%</text>
    <text x="835" y="250" font-family="Arial" font-size="10" fill="#666" text-anchor="middle">Q1</text>
    <rect x="880" y="140" width="70" height="110" fill="#F5B041" rx="4"/>
    <text x="915" y="230" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">31%</text>
    <text x="915" y="250" font-family="Arial" font-size="10" fill="#666" text-anchor="middle">Q2</text>
    <rect x="960" y="140" width="70" height="115" fill="#F39C12" rx="4"/>
    <text x="995" y="230" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">32%</text>
    <text x="995" y="250" font-family="Arial" font-size="10" fill="#666" text-anchor="middle">Q3</text>
    <rect x="1040" y="140" width="70" height="135" fill="#E67E22" rx="4"/>
    <text x="1075" y="230" font-family="Arial" font-size="11" fill="#333" text-anchor="middle">41%</text>
    <text x="1075" y="250" font-family="Arial" font-size="10" fill="#666" text-anchor="middle">Q4</text>
    <rect x="60" y="295" width="1160" height="150" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="295" width="1160" height="50" rx="12" fill="#E8F6F3"/>
    <text x="90" y="328" font-family="Arial Black" font-size="16" fill="#1ABC9C">2️⃣ Q4 拐点</text>
    <text x="90" y="370" font-family="Arial" font-size="14" fill="#555">单季收入<tspan fill="#2932E1" font-weight="bold" font-size="16">88 亿</tspan>（占全年 29%），算力订阅<tspan fill="#E74C3C" font-weight="bold" font-size="16">+143%</tspan>增速，企业从试点 → 规模化采购</text>
    <rect x="60" y="470" width="1160" height="150" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="470" width="1160" height="50" rx="12" fill="#EBF5FB"/>
    <text x="90" y="503" font-family="Arial Black" font-size="16" fill="#2932E1">3️⃣ 结构优化</text>
    <text x="90" y="545" font-family="Arial" font-size="14" fill="#555">高毛利 MaaS/模型服务占比从 2024 年<tspan font-weight="bold" font-size="16">13%</tspan> → 2025 年<tspan font-weight="bold" font-size="16">22%</tspan>，拉动整体毛利率提升</text>
    <rect x="900" y="515" width="180" height="18" fill="#E8EAED" rx="9"/>
    <rect x="900" y="515" width="117" height="18" fill="#2932E1" rx="9"/>
    <text x="990" y="528" font-family="Arial" font-size="10" fill="#FFFFFF" text-anchor="middle">2024: 13%</text>
    <rect x="900" y="545" width="180" height="18" fill="#E8EAED" rx="9"/>
    <rect x="900" y="545" width="162" height="18" fill="#5C67FF" rx="9"/>
    <text x="990" y="558" font-family="Arial" font-size="10" fill="#FFFFFF" text-anchor="middle">2025: 22%</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 6 / 14</text>
</svg>'''

# 第 7 页：智能云基础设施
slides_content["07_infrastructure.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">业务结构 · 智能云基础设施</text>
    <rect x="60" y="80" width="320" height="4" fill="#2932E1"/>
    <text x="1100" y="80" font-family="Arial Black" font-size="42" fill="#2932E1" text-anchor="end">198 亿</text>
    <text x="1100" y="105" font-family="Arial" font-size="13" fill="#666" text-anchor="end">同比 +34%</text>
    <rect x="60" y="130" width="560" height="90" fill="#F5F5F5" rx="8"/>
    <text x="100" y="165" font-family="Arial" font-size="13" fill="#555"><tspan font-weight="bold">构成：</tspan>AI 算力（GPU/昆仑芯）、存储、网络、私有云/混合云</text>
    <text x="100" y="195" font-family="Arial" font-size="12" fill="#666">核心主力业务，占智能云总收入 66%</text>
    <rect x="60" y="250" width="280" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="250" width="280" height="45" rx="12" fill="#FEF9E7"/>
    <text x="200" y="280" font-family="Arial Black" font-size="14" fill="#F39C12" text-anchor="middle">🚀 大模型训练爆发</text>
    <text x="80" y="320" font-family="Arial" font-size="12" fill="#555">服务字节、快手、</text>
    <text x="80" y="340" font-family="Arial" font-size="12" fill="#555">智谱 AI、MiniMax 等</text>
    <text x="200" y="380" font-family="Arial" font-size="12" fill="#E67E22" text-anchor="middle" font-weight="bold">万卡级集群订单大增</text>
    <text x="80" y="415" font-family="Arial" font-size="11" fill="#999">头部客户需求旺盛</text>
    <rect x="360" y="250" width="280" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="360" y="250" width="280" height="45" rx="12" fill="#E8F6F3"/>
    <text x="500" y="280" font-family="Arial Black" font-size="14" fill="#1ABC9C" text-anchor="middle">💎 昆仑芯规模化</text>
    <text x="380" y="320" font-family="Arial" font-size="12" fill="#555">全年交付<tspan fill="#2932E1" font-weight="bold">超 30 万片</tspan></text>
    <text x="500" y="360" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">70% 外部客户</text>
    <text x="500" y="385" font-family="Arial" font-size="12" fill="#27AE60" text-anchor="middle" font-weight="bold">成本下降 25%+</text>
    <text x="500" y="415" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">自研芯片成本优势</text>
    <rect x="660" y="250" width="280" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="250" width="280" height="45" rx="12" fill="#EBF5FB"/>
    <text x="800" y="280" font-family="Arial Black" font-size="14" fill="#2932E1" text-anchor="middle">🏦 政企/金融刚需</text>
    <text x="800" y="320" font-family="Arial" font-size="12" fill="#555" text-anchor="middle">80% 央企</text>
    <text x="800" y="345" font-family="Arial" font-size="12" fill="#555" text-anchor="middle">100% 系统重要性银行</text>
    <text x="800" y="385" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">金融 AI 云市占率</text>
    <text x="800" y="405" font-family="Arial Black" font-size="18" fill="#2932E1" text-anchor="middle">38%</text>
    <text x="800" y="430" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">深度渗透</text>
    <rect x="960" y="250" width="280" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="960" y="250" width="280" height="45" rx="12" fill="#FDEDEC"/>
    <text x="1100" y="280" font-family="Arial Black" font-size="14" fill="#E74C3C" text-anchor="middle">⚡ 天池超节点</text>
    <text x="980" y="320" font-family="Arial" font-size="12" fill="#555" text-anchor="middle">512 卡集群落地</text>
    <text x="1100" y="350" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">支持万亿参数训练</text>
    <text x="1100" y="390" font-family="Arial" font-size="12" fill="#C0392B" text-anchor="middle" font-weight="bold">单价提升 30%+</text>
    <text x="1100" y="420" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">高端算力溢价</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 7 / 14</text>
</svg>'''

# 第 8 页：AI 应用与服务
slides_content["08_ai_services.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">业务结构 · AI 应用与服务</text>
    <rect x="60" y="80" width="300" height="4" fill="#2932E1"/>
    <text x="1100" y="80" font-family="Arial Black" font-size="42" fill="#2932E1" text-anchor="end">102 亿</text>
    <text x="1100" y="105" font-family="Arial" font-size="13" fill="#666" text-anchor="end">同比 +34%</text>
    <rect x="60" y="130" width="560" height="90" fill="#F5F5F5" rx="8"/>
    <text x="100" y="165" font-family="Arial" font-size="13" fill="#555"><tspan font-weight="bold">构成：</tspan>千帆 MaaS、文心大模型服务、行业 AI 解决方案、智能体、数字人</text>
    <text x="100" y="195" font-family="Arial" font-size="12" fill="#666">高毛利业务，占智能云总收入 34%</text>
    <rect x="60" y="250" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="250" width="560" height="45" rx="12" fill="#EBF5FB"/>
    <text x="340" y="280" font-family="Arial Black" font-size="16" fill="#2932E1" text-anchor="middle">🌊 千帆 MaaS 平台</text>
    <text x="340" y="315" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">模型训练/微调/推理/Agent 开发一体化</text>
    <text x="340" y="360" font-family="Arial Black" font-size="24" fill="#27AE60" text-anchor="middle">Token 消耗月增 50%+</text>
    <text x="340" y="395" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">一站式模型服务，降低企业 AI 使用门槛</text>
    <text x="340" y="425" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">平台化效应显著</text>
    <rect x="660" y="250" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="250" width="560" height="45" rx="12" fill="#FEF9E7"/>
    <text x="940" y="280" font-family="Arial Black" font-size="16" fill="#F39C12" text-anchor="middle">🧠 文心大模型 4.0</text>
    <text x="940" y="315" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">2025 年迭代至 4.0 版本</text>
    <text x="940" y="360" font-family="Arial Black" font-size="20" fill="#E67E22" text-anchor="middle">企业付费调用量季度翻倍</text>
    <text x="940" y="395" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">全模态、长文本、工具调用、智能体能力</text>
    <text x="940" y="425" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">技术领先优势</text>
    <rect x="60" y="470" width="560" height="150" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="470" width="560" height="45" rx="12" fill="#E8F6F3"/>
    <text x="340" y="500" font-family="Arial Black" font-size="16" fill="#1ABC9C" text-anchor="middle">🏭 行业 AI 落地</text>
    <text x="340" y="540" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">金融风控 | 智能制造 | 自动驾驶云 | 电网智能调度</text>
    <text x="340" y="575" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">规模化交付，垂直行业深度渗透</text>
    <text x="340" y="605" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">行业 Know-how 积累</text>
    <rect x="660" y="470" width="560" height="150" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="470" width="560" height="45" rx="12" fill="#FDEDEC"/>
    <text x="940" y="500" font-family="Arial Black" font-size="16" fill="#E74C3C" text-anchor="middle">🤖 超级智能体</text>
    <text x="940" y="540" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">"百度伐谋"获 2000+ 企业试用</text>
    <text x="940" y="575" font-family="Arial" font-size="12" fill="#666" text-anchor="middle">"曦灵"数字人商业化落地</text>
    <text x="940" y="605" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">Agent 生态布局</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 8 / 14</text>
</svg>'''

# 第 9 页：客户与市场地位
slides_content["09_market_share.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">客户与市场地位</text>
    <rect x="60" y="80" width="240" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="560" height="400" fill="#FFFFFF" rx="12" filter="url(#shadow)"/>
    <text x="340" y="160" font-family="Arial" font-size="16" fill="#333" text-anchor="middle" font-weight="bold">客户结构</text>
    <circle cx="240" cy="320" r="110" fill="#FFFFFF" stroke="#E8EAED" stroke-width="2"/>
    <path d="M 240 210 A 110 110 0 0 1 340 275 L 240 320 Z" fill="#2932E1"/>
    <path d="M 340 275 A 110 110 0 0 1 315 390 L 240 320 Z" fill="#5C67FF"/>
    <path d="M 315 390 A 110 110 0 0 1 165 390 L 240 320 Z" fill="#3498DB"/>
    <path d="M 165 390 A 110 110 0 0 1 135 275 L 240 320 Z" fill="#2ECC71"/>
    <path d="M 135 275 A 110 110 0 0 1 240 210 L 240 320 Z" fill="#F39C12"/>
    <text x="420" y="230" font-family="Arial" font-size="12" fill="#555">■ 互联网 35%</text>
    <text x="420" y="255" font-family="Arial" font-size="12" fill="#555">■ 金融 22%</text>
    <text x="420" y="280" font-family="Arial" font-size="12" fill="#555">■ 制造 18%</text>
    <text x="420" y="305" font-family="Arial" font-size="12" fill="#555">■ 政企 15%</text>
    <text x="420" y="330" font-family="Arial" font-size="12" fill="#555">■ 其他 10%</text>
    <rect x="660" y="120" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="120" width="560" height="50" rx="12" fill="#2932E1"/>
    <text x="940" y="153" font-family="Arial Black" font-size="16" fill="#FFFFFF" text-anchor="middle">🏆 市场份额</text>
    <text x="940" y="210" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">中国 AI 云全栈服务</text>
    <text x="940" y="255" font-family="Arial Black" font-size="52" fill="#2932E1" text-anchor="middle">40.2%</text>
    <text x="940" y="290" font-family="Arial" font-size="13" fill="#27AE60" text-anchor="middle" font-weight="bold">行业第一 · 领跑市场</text>
    <rect x="660" y="330" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="330" width="560" height="50" rx="12" fill="#FEF9E7"/>
    <text x="940" y="363" font-family="Arial Black" font-size="16" fill="#F39C12" text-anchor="middle">📋 中标表现</text>
    <text x="940" y="420" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">2025 年大模型项目</text>
    <text x="940" y="465" font-family="Arial Black" font-size="32" fill="#E67E22" text-anchor="middle">109 个 / 9 亿元</text>
    <text x="940" y="500" font-family="Arial" font-size="13" fill="#27AE60" text-anchor="middle" font-weight="bold">连续两年 项目数/金额双第一</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 9 / 14</text>
</svg>'''

# 第 10 页：昆仑芯
slides_content["10_kunlun_chip.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">关键战略 · 昆仑芯 AI 芯片</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="1160" height="110" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="1160" height="55" rx="12" fill="#2932E1"/>
    <text x="110" y="158" font-family="Arial Black" font-size="18" fill="#FFFFFF">💡 核心动作</text>
    <text x="640" y="158" font-family="Arial" font-size="15" fill="#E0E0FF" text-anchor="middle">二代昆仑芯（P800）量产，覆盖训练/微调/推理全栈</text>
    <rect x="60" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="265" width="360" height="50" rx="12" fill="#FEF9E7"/>
    <text x="240" y="298" font-family="Arial Black" font-size="15" fill="#F39C12" text-anchor="middle">📈 新增长曲线</text>
    <text x="240" y="360" font-family="Arial Black" font-size="36" fill="#2932E1" text-anchor="middle">超 50 亿元</text>
    <text x="240" y="400" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">芯片相关收入</text>
    <text x="240" y="435" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">成为独立增长引擎</text>
    <text x="240" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">商业化成功</text>
    <rect x="440" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="440" y="265" width="360" height="50" rx="12" fill="#E8F6F3"/>
    <text x="620" y="298" font-family="Arial Black" font-size="15" fill="#1ABC9C" text-anchor="middle">💰 成本优化</text>
    <text x="620" y="360" font-family="Arial Black" font-size="32" fill="#27AE60" text-anchor="middle">-25%~-30%</text>
    <text x="620" y="400" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">云基础设施成本下降</text>
    <text x="620" y="435" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">毛利率改善 +3~+5pct</text>
    <text x="620" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">自研替代优势</text>
    <rect x="820" y="265" width="400" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="820" y="265" width="400" height="50" rx="12" fill="#EBF5FB"/>
    <text x="1020" y="298" font-family="Arial Black" font-size="15" fill="#2932E1" text-anchor="middle">🛡️ 国产替代壁垒</text>
    <text x="1020" y="350" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">强化自主可控能力</text>
    <text x="1020" y="395" font-family="Arial Black" font-size="28" fill="#27AE60" text-anchor="middle">政企订单 +40%</text>
    <text x="1020" y="435" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">国产芯片首选供应商</text>
    <text x="1020" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">政策红利 + 技术实力</text>
    <rect x="60" y="525" width="1160" height="75" fill="#F5F5F5" rx="8"/>
    <text x="640" y="560" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">昆仑芯规模化商用是百度智能云 2025 年核心竞争力之一，实现成本优化与收入增长双赢</text>
    <text x="640" y="585" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">自研芯片战略 | 全栈覆盖 | 外部客户占比 70% | 成本下降 25%+</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 10 / 14</text>
</svg>'''

# 第 11 页：千帆 MaaS
slides_content["11_qianfan_maas.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">关键战略 · 千帆 MaaS 平台</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="1160" height="110" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="1160" height="55" rx="12" fill="#2932E1"/>
    <text x="110" y="158" font-family="Arial Black" font-size="18" fill="#FFFFFF">💡 核心动作</text>
    <text x="640" y="158" font-family="Arial" font-size="15" fill="#E0E0FF" text-anchor="middle">一站式模型商店、行业大模型定制、智能体开发工具链</text>
    <rect x="60" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="265" width="360" height="50" rx="12" fill="#FEF9E7"/>
    <text x="240" y="298" font-family="Arial Black" font-size="15" fill="#F39C12" text-anchor="middle">📈 收入高增</text>
    <text x="240" y="360" font-family="Arial Black" font-size="36" fill="#E67E22" text-anchor="middle">+225%</text>
    <text x="240" y="400" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">MaaS 收入增长</text>
    <text x="240" y="435" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">占比升至 22%</text>
    <text x="240" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">平台化效应</text>
    <rect x="440" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="440" y="265" width="360" height="50" rx="12" fill="#E8F6F3"/>
    <text x="620" y="298" font-family="Arial Black" font-size="15" fill="#1ABC9C" text-anchor="middle">💎 高毛利拉动</text>
    <text x="620" y="360" font-family="Arial Black" font-size="32" fill="#27AE60" text-anchor="middle">65%~70%</text>
    <text x="620" y="400" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">MaaS 毛利率</text>
    <text x="620" y="435" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">拉动整体盈利改善</text>
    <text x="620" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">高附加值服务</text>
    <rect x="820" y="265" width="400" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="820" y="265" width="400" height="50" rx="12" fill="#EBF5FB"/>
    <text x="1020" y="298" font-family="Arial Black" font-size="15" fill="#2932E1" text-anchor="middle">👥 客户粘性提升</text>
    <text x="1020" y="345" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">客户 LTV <tspan fill="#27AE60" font-weight="bold" font-size="18">+60%</tspan> | 流失率 <tspan fill="#E74C3C" font-weight="bold" font-size="18">-15%</tspan></text>
    <text x="1020" y="395" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">外部收入占比 90%+</text>
    <text x="1020" y="430" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">平台化效应显著</text>
    <text x="1020" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">生态锁定效应</text>
    <rect x="60" y="525" width="1160" height="75" fill="#F5F5F5" rx="8"/>
    <text x="640" y="560" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">千帆 MaaS 平台是百度智能云商业化成功的核心引擎，实现收入、毛利、客户粘性三重提升</text>
    <text x="640" y="585" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">模型商店 | 行业定制 | 智能体工具链 | Token 消耗月增 50%+</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 11 / 14</text>
</svg>'''

# 第 12 页：文心大模型
slides_content["12_ernie_model.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">关键战略 · 文心大模型 4.0</text>
    <rect x="60" y="80" width="280" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="1160" height="110" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="1160" height="55" rx="12" fill="#2932E1"/>
    <text x="110" y="158" font-family="Arial Black" font-size="18" fill="#FFFFFF">💡 核心动作</text>
    <text x="640" y="158" font-family="Arial" font-size="15" fill="#E0E0FF" text-anchor="middle">全模态、长文本、工具调用、智能体能力全面开放</text>
    <rect x="60" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="265" width="360" height="50" rx="12" fill="#FEF9E7"/>
    <text x="240" y="298" font-family="Arial Black" font-size="15" fill="#F39C12" text-anchor="middle">📈 收入带动</text>
    <text x="240" y="360" font-family="Arial Black" font-size="36" fill="#E67E22" text-anchor="middle">+200%</text>
    <text x="240" y="400" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">MaaS/API 收入增长</text>
    <text x="240" y="435" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">成为核心竞争力</text>
    <text x="240" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">技术变现能力</text>
    <rect x="440" y="265" width="360" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="440" y="265" width="360" height="50" rx="12" fill="#E8F6F3"/>
    <text x="620" y="298" font-family="Arial Black" font-size="15" fill="#1ABC9C" text-anchor="middle">🔄 能力升级</text>
    <text x="620" y="340" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">全模态理解</text>
    <text x="620" y="365" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">长文本处理</text>
    <text x="620" y="390" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">工具调用</text>
    <text x="620" y="415" font-family="Arial" font-size="13" fill="#555" text-anchor="middle">智能体编排</text>
    <text x="620" y="450" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">企业级能力全面开放</text>
    <text x="620" y="475" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">技术领先</text>
    <rect x="820" y="265" width="400" height="230" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="820" y="265" width="400" height="50" rx="12" fill="#EBF5FB"/>
    <text x="1020" y="298" font-family="Arial Black" font-size="15" fill="#2932E1" text-anchor="middle">🌐 生态协同</text>
    <text x="1020" y="350" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">与搜索、网盘、文库协同</text>
    <text x="1020" y="395" font-family="Arial Black" font-size="22" fill="#27AE60" text-anchor="middle">C 端 + B 端 闭环形成</text>
    <text x="1020" y="435" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">全场景覆盖</text>
    <text x="1020" y="465" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">生态优势</text>
    <rect x="60" y="525" width="1160" height="75" fill="#F5F5F5" rx="8"/>
    <text x="640" y="560" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">文心大模型 4.0 是百度 AI 技术实力的集中体现，驱动 MaaS 收入增长，构建 C 端+B 端生态闭环</text>
    <text x="640" y="585" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">全模态 | 长文本 | 工具调用 | 智能体 | 生态协同</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 12 / 14</text>
</svg>'''

# 第 13 页：风险与挑战
slides_content["13_risks.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <text x="60" y="70" font-family="Arial Black" font-size="28" fill="#333333">核心风险与挑战</text>
    <rect x="60" y="80" width="240" height="4" fill="#2932E1"/>
    <rect x="60" y="120" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="120" width="560" height="50" rx="12" fill="#FDEDEC"/>
    <text x="340" y="153" font-family="Arial Black" font-size="16" fill="#E74C3C" text-anchor="middle">⚠️ 行业竞争加剧</text>
    <text x="100" y="195" font-family="Arial" font-size="13" fill="#555">• 阿里云、华为云、腾讯云持续加大 AI 投入</text>
    <text x="100" y="220" font-family="Arial" font-size="13" fill="#555">• 价格战压力可能影响利润率</text>
    <text x="100" y="245" font-family="Arial" font-size="13" fill="#555">• 需要持续保持技术领先优势</text>
    <text x="340" y="285" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">竞争格局</text>
    <rect x="660" y="120" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="120" width="560" height="50" rx="12" fill="#FEF9E7"/>
    <text x="940" y="153" font-family="Arial Black" font-size="16" fill="#F39C12" text-anchor="middle">💸 高资本开支压力</text>
    <text x="700" y="195" font-family="Arial" font-size="13" fill="#555">• 2025 年智算投入 250~280 亿元</text>
    <text x="700" y="220" font-family="Arial" font-size="13" fill="#555">• 昆仑芯研发 + 产能扩张持续投入</text>
    <text x="700" y="245" font-family="Arial" font-size="13" fill="#555">• 短期盈利承压，需平衡投入与回报</text>
    <text x="940" y="285" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">投入压力</text>
    <rect x="60" y="335" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="335" width="560" height="50" rx="12" fill="#F5EEF8"/>
    <text x="340" y="368" font-family="Arial Black" font-size="16" fill="#9B59B6" text-anchor="middle">🔄 技术迭代风险</text>
    <text x="100" y="410" font-family="Arial" font-size="13" fill="#555">• 大模型技术快速演进，需持续研发投入</text>
    <text x="100" y="435" font-family="Arial" font-size="13" fill="#555">• 国际头部模型（GPT-5 等）可能形成代差</text>
    <text x="100" y="460" font-family="Arial" font-size="13" fill="#555">• 人才竞争激烈，核心技术人员流失风险</text>
    <text x="340" y="500" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">技术风险</text>
    <rect x="660" y="335" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="335" width="560" height="50" rx="12" fill="#EBF5FB"/>
    <text x="940" y="368" font-family="Arial Black" font-size="16" fill="#2932E1" text-anchor="middle">🌍 宏观经济环境</text>
    <text x="700" y="410" font-family="Arial" font-size="13" fill="#555">• 企业 IT 预算可能受经济波动影响</text>
    <text x="700" y="435" font-family="Arial" font-size="13" fill="#555">• AI 项目 ROI 验证周期较长</text>
    <text x="700" y="460" font-family="Arial" font-size="13" fill="#555">• 政企客户决策周期长、回款慢</text>
    <text x="940" y="500" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">宏观风险</text>
    <rect x="60" y="550" width="1160" height="70" fill="#E8F6F3" rx="8"/>
    <text x="90" y="580" font-family="Arial Black" font-size="14" fill="#1ABC9C">💡 应对策略：</text>
    <text x="210" y="580" font-family="Arial" font-size="13" fill="#555">持续技术创新 · 优化成本结构 · 深化行业落地 · 加强生态合作</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 13 / 14</text>
</svg>'''

# 第 14 页：总结
slides_content["14_summary.svg"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <defs>
        <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#2932E1"/>
            <stop offset="100%" style="stop-color:#5C67FF"/>
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="#F8F9FA"/>
    <rect width="1280" height="180" fill="url(#blueGrad)"/>
    <text x="640" y="80" font-family="Arial Black" font-size="36" fill="#FFFFFF" text-anchor="middle">总结：AI 云兑现元年</text>
    <text x="640" y="125" font-family="Arial" font-size="16" fill="#E0E0FF" text-anchor="middle">百度智能云 2025 年核心洞察</text>
    <rect x="60" y="200" width="560" height="210" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="200" width="560" height="55" rx="12" fill="#FEF9E7"/>
    <text x="340" y="235" font-family="Arial Black" font-size="16" fill="#F39C12" text-anchor="middle">✅ 高增长验证</text>
    <text x="340" y="280" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">总收入 300 亿，同比 +34%</text>
    <text x="340" y="315" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">在百度整体 -3% 背景下逆势高增</text>
    <text x="340" y="355" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">AI 成为核心增长引擎</text>
    <text x="340" y="385" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">增长质量</text>
    <rect x="660" y="200" width="560" height="210" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="200" width="560" height="55" rx="12" fill="#E8F6F3"/>
    <text x="940" y="235" font-family="Arial Black" font-size="16" fill="#1ABC9C" text-anchor="middle">✅ 全栈壁垒形成</text>
    <text x="940" y="280" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">昆仑芯 → 天池 → 千帆 → 文心 → Agent</text>
    <text x="940" y="315" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">完整技术闭环落地</text>
    <text x="940" y="355" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">自研芯片 + 平台化双轮驱动</text>
    <text x="940" y="385" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">技术壁垒</text>
    <rect x="60" y="435" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="60" y="435" width="560" height="55" rx="12" fill="#EBF5FB"/>
    <text x="340" y="470" font-family="Arial Black" font-size="16" fill="#2932E1" text-anchor="middle">✅ 市场地位稳固</text>
    <text x="340" y="515" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">AI 云全栈市占率 40.2% 行业第一</text>
    <text x="340" y="550" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">大模型中标 109 个/9 亿 双第一</text>
    <text x="340" y="585" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">政企/金融深度渗透</text>
    <text x="340" y="610" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">市场地位</text>
    <rect x="660" y="435" width="560" height="190" rx="12" fill="#FFFFFF" filter="url(#shadow)"/>
    <rect x="660" y="435" width="560" height="55" rx="12" fill="#FDEDEC"/>
    <text x="940" y="470" font-family="Arial Black" font-size="16" fill="#E74C3C" text-anchor="middle">⚠️ 投入期持续</text>
    <text x="940" y="515" font-family="Arial" font-size="14" fill="#555" text-anchor="middle">2025 年仍处高投入期，整体未盈利</text>
    <text x="940" y="550" font-family="Arial" font-size="13" fill="#666" text-anchor="middle">AI 算力/高毛利 MaaS 利润率改善</text>
    <text x="940" y="585" font-family="Arial" font-size="12" fill="#999" text-anchor="middle">平衡投入与回报是关键</text>
    <text x="940" y="610" font-family="Arial" font-size="11" fill="#999" text-anchor="middle">盈利挑战</text>
    <text x="60" y="680" font-family="Arial" font-size="12" fill="#999999">百度智能云 2025 年财报分析 | 14 / 14</text>
</svg>'''

# 生成所有文件
os.makedirs(SVG_OUTPUT_DIR, exist_ok=True)

for filename, content in slides_content.items():
    filepath = os.path.join(SVG_OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已生成：{filename}")

print(f"\n🎉 完成！共生成 {len(slides_content)} 页 SVG 文件")
print(f"输出目录：{SVG_OUTPUT_DIR}")
