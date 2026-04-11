#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成百度智能云 2025 年财报分析 PPT 的 SVG 文件
共 14 页
"""

import os

PROJECT_DIR = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/baidu_cloud_2025_financial_ppt169_20260410"
SVG_OUTPUT_DIR = os.path.join(PROJECT_DIR, "svg_output")

# 百度蓝
BAIDU_BLUE = "#2932E1"
BAIDU_BLUE_LIGHT = "#5C67FF"
DARK_GRAY = "#333333"
LIGHT_GRAY = "#F5F5F5"
WHITE = "#FFFFFF"
ACCENT_BLUE = "#0066FF"

def create_svg_header(title=""):
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
    
    <!-- 背景 -->
    <rect width="1280" height="720" fill="url(#bgGradient)"/>
'''

def create_svg_footer(svg_content, page_num, total_pages=14):
    # 添加页脚
    svg_content += f'''
    <!-- 页脚 -->
    <rect x="0" y="680" width="1280" height="40" fill="#F5F5F5" opacity="0.5"/>
    <text x="60" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999">
        百度智能云 2025 年财报分析
    </text>
    <text x="1220" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999" text-anchor="end">
        {page_num} / {total_pages}
    </text>
    
</svg>'''
    return svg_content

def generate_cover():
    """第 1 页：封面"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题区域 -->
    <rect x="0" y="0" width="1280" height="200" fill="url(#blueGradient)"/>
    
    <!-- 主标题 -->
    <text x="640" y="120" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
        百度智能云 2025 年财报分析
    </text>
    
    <!-- 副标题 -->
    <text x="640" y="170" font-family="Arial, Microsoft YaHei" font-size="20" fill="#E0E0FF" text-anchor="middle">
        AI 云兑现元年 · 全栈能力规模化落地
    </text>
    
    <!-- 装饰线条 -->
    <rect x="440" y="220" width="400" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 信息卡片 -->
    <g filter="url(#shadow)">
        <rect x="340" y="320" width="600" height="80" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <text x="640" y="355" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
            数据基准：百度集团 2026 年 2 月 26 日发布 2025 年 Q4 及全年财报
        </text>
        <text x="640" y="380" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
            财年周期：2025 年 1 月 1 日 — 2025 年 12 月 31 日（自然年）
        </text>
    </g>
    
    <!-- 底部装饰 -->
    <rect x="0" y="620" width="1280" height="100" fill="#F8F9FA"/>
    <text x="640" y="670" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999" text-anchor="middle">
        2026 年 4 月 · 内部汇报材料
    </text>
'''
    return create_svg_footer(svg, 1)

def generate_data_baseline():
    """第 2 页：数据基准与财年周期"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        数据基准与财年周期
    </text>
    <rect x="60" y="95" width="200" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 内容区域 - 两个卡片 -->
    
    <!-- 卡片 1：数据基准 -->
    <g filter="url(#shadow)">
        <rect x="60" y="150" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="150" width="8" height="220" rx="4" fill="{BAIDU_BLUE}"/>
        
        <text x="100" y="190" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{DARK_GRAY}">
            📊 数据基准
        </text>
        
        <text x="100" y="230" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan x="100" dy="0">• 百度集团 2026 年 2 月 26 日发布</tspan>
            <tspan x="100" dy="30">• 2025 年 Q4 及全年财报</tspan>
            <tspan x="100" dy="30">• 电话会官方披露内容</tspan>
            <tspan x="100" dy="30">• 官方投资者关系材料</tspan>
        </text>
    </g>
    
    <!-- 卡片 2：财年周期 -->
    <g filter="url(#shadow)">
        <rect x="660" y="150" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="150" width="8" height="220" rx="4" fill="{BAIDU_BLUE_LIGHT}"/>
        
        <text x="700" y="190" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{DARK_GRAY}">
            📅 财年周期
        </text>
        
        <text x="700" y="240" font-family="Arial, Microsoft YaHei" font-size="16" fill="#555555">
            <tspan x="700" dy="0">2025 年 1 月 1 日</tspan>
            <tspan x="900" dy="0" font-weight="bold" fill="{BAIDU_BLUE}"> —→ </tspan>
            <tspan x="980" dy="0">2025 年 12 月 31 日</tspan>
        </text>
        
        <rect x="700" y="260" width="480" height="60" rx="8" fill="#F5F5F5"/>
        <text x="940" y="295" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            百度采用自然年财年
        </text>
    </g>
    
    <!-- 底部说明 -->
    <g filter="url(#shadow)">
        <rect x="60" y="420" width="1160" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <text x="100" y="460" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{DARK_GRAY}">
            💡 关键说明
        </text>
        <text x="100" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan x="100" dy="0">• 所有财务数据均来自百度集团官方财报，单位为亿元人民币</tspan>
            <tspan x="100" dy="28">• 同比增长率基于 2024 年同期数据计算</tspan>
            <tspan x="100" dy="28">• 市场份额数据来自第三方研究机构（IDC、Canalys 等）</tspan>
            <tspan x="100" dy="28">• 部分季度数据为基于全年数据的合理估算</tspan>
        </text>
    </g>
'''
    return create_svg_footer(svg, 2)

def generate_core_metrics():
    """第 3 页：整体业绩概览 - 核心财务指标（表格）"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        整体业绩概览 · 核心财务指标
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 表格标题行 -->
    <rect x="60" y="140" width="1160" height="50" fill="{BAIDU_BLUE}" rx="8"/>
    <text x="180" y="172" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF">指标</text>
    <text x="420" y="172" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF">2025 全年</text>
    <text x="620" y="172" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF">2024 全年</text>
    <text x="820" y="172" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF">同比变化</text>
    <text x="1020" y="172" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF">关键说明</text>
    
    <!-- 表格数据行 1 -->
    <rect x="60" y="190" width="1160" height="55" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="215" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">百度智能云总收入</text>
    <text x="420" y="220" font-family="Arial Black, Microsoft YaHei" font-size="24" font-weight="bold" fill="{BAIDU_BLUE}">300</text>
    <text x="620" y="220" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666">223.9</text>
    <text x="820" y="220" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#27AE60">+34%</text>
    <text x="1020" y="220" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">首次突破 300 亿</text>
    
    <!-- 表格数据行 2 -->
    <rect x="60" y="245" width="1160" height="55" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="270" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">— 智能云基础设施</text>
    <text x="420" y="275" font-family="Arial, Microsoft YaHei" font-size="20" font-weight="bold" fill="{DARK_GRAY}">198</text>
    <text x="620" y="275" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">148</text>
    <text x="820" y="275" font-family="Arial, Microsoft YaHei" font-size="18" font-weight="bold" fill="#27AE60">+34%</text>
    <text x="1020" y="275" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">AI 算力/存储/网络</text>
    
    <!-- 表格数据行 3 -->
    <rect x="60" y="300" width="1160" height="55" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="325" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">— AI 应用与服务</text>
    <text x="420" y="330" font-family="Arial, Microsoft YaHei" font-size="20" font-weight="bold" fill="{DARK_GRAY}">102</text>
    <text x="620" y="330" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">75.9</text>
    <text x="820" y="330" font-family="Arial, Microsoft YaHei" font-size="18" font-weight="bold" fill="#27AE60">+34%</text>
    <text x="1020" y="330" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">MaaS、大模型</text>
    
    <!-- 表格数据行 4 -->
    <rect x="60" y="355" width="1160" height="55" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="380" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">AI 高性能计算订阅 (Q4)</text>
    <text x="420" y="385" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999">—</text>
    <text x="620" y="385" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999">—</text>
    <text x="820" y="385" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#27AE60">+143%</text>
    <text x="1020" y="380" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">增速逐季加快</text>
    
    <!-- 表格数据行 5 -->
    <rect x="60" y="410" width="1160" height="55" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="435" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">大模型中标项目/金额</text>
    <text x="420" y="440" font-family="Arial, Microsoft YaHei" font-size="16" font-weight="bold" fill="{DARK_GRAY}">109 个 / 9 亿</text>
    <text x="620" y="440" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999">—</text>
    <text x="820" y="440" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12">双第一</text>
    <text x="1020" y="440" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">连续两年行业第一</text>
    
    <!-- 表格数据行 6 -->
    <rect x="60" y="465" width="1160" height="55" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="180" y="490" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">AI 云全栈市占率</text>
    <text x="420" y="495" font-family="Arial Black, Microsoft YaHei" font-size="24" font-weight="bold" fill="{BAIDU_BLUE}">40.2%</text>
    <text x="620" y="495" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999">—</text>
    <text x="820" y="495" font-family="Arial, Microsoft YaHei" font-size="18" font-weight="bold" fill="#27AE60">领跑</text>
    <text x="1020" y="495" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">中国 AI 市场份额首位</text>
    
    <!-- 底部备注 -->
    <text x="60" y="560" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999">
        注：所有金额单位为亿元人民币；市占率数据来自中国 AI 云全栈服务市场
    </text>
'''
    return create_svg_footer(svg, 3)

def generate_overview_features():
    """第 4 页：整体业绩概览 - 整体特征"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        整体业绩概览 · 整体特征
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 4 个特征卡片 2x2 布局 -->
    
    <!-- 卡片 1：增长韧性强 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="240" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="560" height="60" rx="12" fill="#FEF9E7"/>
        <text x="340" y="175" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#F39C12" text-anchor="middle">
            📈 增长韧性强
        </text>
        <text x="100" y="230" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan x="100" dy="0">在百度总营收同比 -3%</tspan>
            <tspan x="100" dy="30">（1291 亿元）背景下</tspan>
        </text>
        <text x="340" y="300" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#27AE60" text-anchor="middle">
            +34%
        </text>
        <text x="340" y="335" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666" text-anchor="middle">
            智能云逆势高增
        </text>
    </g>
    
    <!-- 卡片 2：AI 算力爆发 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="240" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="560" height="60" rx="12" fill="#E8F6F3"/>
        <text x="940" y="175" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            ⚡ AI 算力爆发
        </text>
        <text x="700" y="230" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan x="700" dy="0">AI 高性能计算订阅</tspan>
            <tspan x="700" dy="30">Q4 同比增速</tspan>
        </text>
        <text x="940" y="300" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            +143%
        </text>
        <text x="940" y="335" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666" text-anchor="middle">
            核心增长极
        </text>
    </g>
    
    <!-- 卡片 3：全栈壁垒 -->
    <g filter="url(#shadow)">
        <rect x="60" y="420" width="560" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="420" width="560" height="60" rx="12" fill="#EBF5FB"/>
        <text x="340" y="455" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🏗️ 全栈壁垒
        </text>
        <text x="340" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            昆仑芯 → 天池智算 → 千帆 MaaS → 文心大模型 → 行业 Agent
        </text>
        <text x="340" y="540" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            完整闭环落地
        </text>
        <text x="340" y="580" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            自研芯片 | 智算平台 | 模型服务 | 大模型 | 智能体应用
        </text>
    </g>
    
    <!-- 卡片 4：盈利阶段 -->
    <g filter="url(#shadow)">
        <rect x="660" y="420" width="560" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="420" width="560" height="60" rx="12" fill="#FDEDEC"/>
        <text x="940" y="455" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            💰 盈利阶段
        </text>
        <text x="700" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan x="940" dy="0" text-anchor="middle">2025 年仍处高投入期</tspan>
            <tspan x="940" dy="28" text-anchor="middle">整体未盈利</tspan>
        </text>
        <text x="940" y="560" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            AI 算力 / 高毛利 MaaS 利润率持续改善
        </text>
    </g>
'''
    return create_svg_footer(svg, 4)

def generate_quarterly_data():
    """第 5 页：分季度表现 - 季度核心数据（表格 + 趋势图）"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        分季度表现 · 季度核心数据
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 左侧：表格 -->
    <rect x="60" y="130" width="600" height="320" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1" rx="8" filter="url(#shadow)"/>
    
    <!-- 表格标题行 -->
    <rect x="60" y="130" width="600" height="45" fill="{BAIDU_BLUE}" rx="8"/>
    <rect x="60" y="165" width="600" height="10" fill="{BAIDU_BLUE}"/>
    <text x="100" y="160" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="#FFFFFF">季度</text>
    <text x="230" y="160" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="#FFFFFF">智能云收入</text>
    <text x="360" y="160" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="#FFFFFF">同比</text>
    <text x="480" y="160" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="#FFFFFF">AI 算力订阅同比</text>
    
    <!-- 表格数据行 -->
    quarters = [
        ("Q1", "~65", "+28%", "+95%", "#FFFFFF"),
        ("Q2", "~70", "+31%", "+112%", "#F8F9FA"),
        ("Q3", "~77", "+32%", "+128%", "#FFFFFF"),
        ("Q4", "88", "+41%", "+143%", "#FEF9E7"),
    ]
    
    y = 185
    for i, (q, revenue, growth, ai_growth, bg) in enumerate(quarters):
        rect_y = y + i * 65
        svg = svg + f'<rect x="60" y="{rect_y}" width="600" height="65" fill="{bg}" stroke="#E8EAED" stroke-width="1"/>\n'
        svg = svg + f'<text x="100" y="{rect_y + 40}" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{DARK_GRAY}">{q}</text>\n'
        svg = svg + f'<text x="230" y="{rect_y + 40}" font-family="Arial, Microsoft YaHei" font-size="18" font-weight="bold" fill="{DARK_GRAY}">{revenue}</text>\n'
        color = "#27AE60" if q == "Q4" else "#555555"
        svg = svg + f'<text x="360" y="{rect_y + 40}" font-family="Arial, Microsoft YaHei" font-size="18" font-weight="bold" fill="{color}">{growth}</text>\n'
        svg = svg + f'<text x="480" y="{rect_y + 40}" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666">{ai_growth}</text>\n'
    
    <!-- 全年汇总 -->
    <rect x="60" y="445" width="600" height="60" fill="#E8F6F3" stroke="#1ABC9C" stroke-width="2" rx="8"/>
    <text x="100" y="475" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#1ABC9C">全年</text>
    <text x="230" y="480" font-family="Arial Black, Microsoft YaHei" font-size="24" font-weight="bold" fill="{BAIDU_BLUE}">300</text>
    <text x="360" y="480" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#27AE60">+34%</text>
    <text x="480" y="480" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">首次破 300 亿</text>
    
    <!-- 右侧：趋势图 -->
    <rect x="700" y="130" width="520" height="375" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1" rx="8" filter="url(#shadow)"/>
    <text x="960" y="165" font-family="Arial, Microsoft YaHei" font-size="16" font-weight="bold" fill="{DARK_GRAY}" text-anchor="middle">季度收入趋势（亿元）</text>
    
    <!-- 简易柱状图 -->
    <rect x="760" y="200" width="80" height="180" fill="#5C67FF" opacity="0.6" rx="4"/>
    <text x="800" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q1</text>
    <text x="800" y="210" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">65</text>
    
    <rect x="860" y="200" width="80" height="200" fill="#5C67FF" opacity="0.7" rx="4"/>
    <text x="900" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q2</text>
    <text x="900" y="210" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">70</text>
    
    <rect x="960" y="200" width="80" height="220" fill="#5C67FF" opacity="0.8" rx="4"/>
    <text x="1000" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q3</text>
    <text x="1000" y="210" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">77</text>
    
    <rect x="1060" y="200" width="80" height="260" fill="{BAIDU_BLUE}" rx="4"/>
    <text x="1100" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q4</text>
    <text x="1100" y="210" font-family="Arial Black, Microsoft YaHei" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">88</text>
    
    <!-- Y 轴标签 -->
    <text x="740" y="395" font-family="Arial, Microsoft YaHei" font-size="11" fill="#999999" text-anchor="end">0</text>
    <text x="740" y="300" font-family="Arial, Microsoft YaHei" font-size="11" fill="#999999" text-anchor="end">50</text>
    <text x="740" y="205" font-family="Arial, Microsoft YaHei" font-size="11" fill="#999999" text-anchor="end">100</text>
    
    <!-- 趋势线 -->
    <polyline points="800,290 900,270 1000,250 1100,200" fill="none" stroke="#E74C3C" stroke-width="3" stroke-dasharray="5,5"/>
    <circle cx="800" cy="290" r="4" fill="#E74C3C"/>
    <circle cx="900" cy="270" r="4" fill="#E74C3C"/>
    <circle cx="1000" cy="250" r="4" fill="#E74C3C"/>
    <circle cx="1100" cy="200" r="4" fill="#E74C3C"/>
'''
    return create_svg_footer(svg, 5)

def generate_quarterly_trend():
    """第 6 页：分季度表现 - 季度趋势分析"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        分季度表现 · 季度趋势分析
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 三个趋势点 -->
    
    <!-- 趋势 1：增速逐季抬升 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="1160" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="1160" height="50" rx="12" fill="#FEF9E7"/>
        <text x="90" y="175" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12">
            1️⃣ 增速逐季抬升
        </text>
        <text x="90" y="220" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan>Q1(28%) → Q2(31%) → Q3(32%) → Q4(41%)，AI 需求</tspan>
            <tspan font-weight="bold" fill="{BAIDU_BLUE}">加速释放</tspan>
        </text>
        <!-- 增速可视化 -->
        <rect x="800" y="160" width="80" height="100" fill="#F7DC6F" rx="4"/>
        <text x="840" y="215" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">28%</text>
        <text x="840" y="245" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666" text-anchor="middle">Q1</text>
        
        <rect x="890" y="160" width="80" height="110" fill="#F5B041" rx="4"/>
        <text x="930" y="215" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">31%</text>
        <text x="930" y="245" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666" text-anchor="middle">Q2</text>
        
        <rect x="940" y="160" width="80" height="115" fill="#F39C12" rx="4"/>
        <text x="980" y="215" font-family="Arial, Microsoft YaHei" font-size="12" fill="#333" text-anchor="middle">32%</text>
        <text x="980" y="245" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666" text-anchor="middle">Q3</text>
        
        <rect x="990" y="160" width="80" height="140" fill="#E67E22" rx="4"/>
        <text x="1030" y="215" font-family="Arial Black, Microsoft YaHei" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">41%</text>
        <text x="1030" y="245" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666" text-anchor="middle">Q4</text>
    </g>
    
    <!-- 趋势 2：Q4 拐点 -->
    <g filter="url(#shadow)">
        <rect x="60" y="310" width="1160" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="310" width="1160" height="50" rx="12" fill="#E8F6F3"/>
        <text x="90" y="345" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#1ABC9C">
            2️⃣ Q4 拐点
        </text>
        <text x="90" y="390" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan>单季收入</tspan>
            <tspan font-weight="bold" fill="{BAIDU_BLUE}" font-size="18">88 亿</tspan>
            <tspan>（占全年 29%），算力订阅</tspan>
            <tspan font-weight="bold" fill="#E74C3C" font-size="18">+143%</tspan>
            <tspan>增速，企业从</tspan>
            <tspan font-weight="bold" fill="{BAIDU_BLUE}">试点 → 规模化采购</tspan>
        </text>
    </g>
    
    <!-- 趋势 3：结构优化 -->
    <g filter="url(#shadow)">
        <rect x="60" y="480" width="1160" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="480" width="1160" height="50" rx="12" fill="#EBF5FB"/>
        <text x="90" y="515" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{BAIDU_BLUE}">
            3️⃣ 结构优化
        </text>
        <text x="90" y="560" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
            <tspan>高毛利</tspan>
            <tspan font-weight="bold" fill="{BAIDU_BLUE}">MaaS/模型服务</tspan>
            <tspan>占比从 2024 年</tspan>
            <tspan font-weight="bold" font-size="18">13%</tspan>
            <tspan> → 2025 年</tspan>
            <tspan font-weight="bold" font-size="18">22%</tspan>
            <tspan>，拉动整体毛利率提升</tspan>
        </text>
        <!-- 占比可视化 -->
        <rect x="900" y="510" width="200" height="20" fill="#E8EAED" rx="10"/>
        <rect x="900" y="510" width="104" height="20" fill="{BAIDU_BLUE}" rx="10"/>
        <text x="1010" y="525" font-family="Arial, Microsoft YaHei" font-size="12" fill="#FFFFFF" text-anchor="middle">2024: 13%</text>
        
        <rect x="900" y="540" width="200" height="20" fill="#E8EAED" rx="10"/>
        <rect x="900" y="540" width="169" height="20" fill="{BAIDU_BLUE_LIGHT}" rx="10"/>
        <text x="1010" y="555" font-family="Arial, Microsoft YaHei" font-size="12" fill="#FFFFFF" text-anchor="middle">2025: 22%</text>
    </g>
'''
    return create_svg_footer(svg, 6)

def generate_infrastructure():
    """第 7 页：业务结构 - 智能云基础设施（198 亿）"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        业务结构 · 智能云基础设施
    </text>
    <rect x="60" y="95" width="320" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 收入数字 -->
    <text x="1100" y="90" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="end">
        198 亿
    </text>
    <text x="1100" y="115" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="end">
        同比 +34%
    </text>
    
    <!-- 构成说明 -->
    <rect x="60" y="140" width="560" height="100" fill="#F5F5F5" rx="8"/>
    <text x="100" y="175" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
        <tspan font-weight="bold">构成：</tspan>AI 算力（GPU/昆仑芯）、存储、网络、私有云/混合云
    </text>
    <text x="100" y="210" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">
        核心主力业务，占智能云总收入 66%
    </text>
    
    <!-- 四个核心驱动 -->
    
    <!-- 驱动 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="270" width="280" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="270" width="280" height="50" rx="12" fill="#FEF9E7"/>
        <text x="200" y="303" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#F39C12" text-anchor="middle">
            🚀 大模型训练爆发
        </text>
        <text x="80" y="345" font-family="Arial, Microsoft YaHei" font-size="13" fill="#555555">
            <tspan x="80" dy="0">服务字节、快手、</tspan>
            <tspan x="80" dy="22">智谱 AI、MiniMax 等</tspan>
            <tspan x="80" dy="22">头部客户</tspan>
        </text>
        <text x="200" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#E67E22" text-anchor="middle" font-weight="bold">
            万卡级集群订单大增
        </text>
    </g>
    
    <!-- 驱动 2 -->
    <g filter="url(#shadow)">
        <rect x="360" y="270" width="280" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="360" y="270" width="280" height="50" rx="12" fill="#E8F6F3"/>
        <text x="500" y="303" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            💎 昆仑芯规模化
        </text>
        <text x="380" y="345" font-family="Arial, Microsoft YaHei" font-size="13" fill="#555555">
            <tspan x="380" dy="0">全年交付</tspan>
            <tspan font-weight="bold" font-size="16" fill="{BAIDU_BLUE}">超 30 万片</tspan>
        </text>
        <text x="500" y="400" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            <tspan x="500" dy="0">70% 外部客户</tspan>
            <tspan x="500" dy="22" font-weight="bold" fill="#27AE60">成本下降 25%+</tspan>
        </text>
    </g>
    
    <!-- 驱动 3 -->
    <g filter="url(#shadow)">
        <rect x="660" y="270" width="280" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="270" width="280" height="50" rx="12" fill="#EBF5FB"/>
        <text x="800" y="303" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🏦 政企/金融刚需
        </text>
        <text x="680" y="345" font-family="Arial, Microsoft YaHei" font-size="13" fill="#555555">
            <tspan x="800" dy="0" text-anchor="middle">80% 央企</tspan>
            <tspan x="800" dy="22" text-anchor="middle">100% 系统重要性银行</tspan>
        </text>
        <text x="800" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            金融 AI 云市占率
            <tspan font-weight="bold" fill="{BAIDU_BLUE}" font-size="16">38%</tspan>
        </text>
    </g>
    
    <!-- 驱动 4 -->
    <g filter="url(#shadow)">
        <rect x="960" y="270" width="260" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="960" y="270" width="260" height="50" rx="12" fill="#FDEDEC"/>
        <text x="1090" y="303" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            ⚡ 天池超节点
        </text>
        <text x="980" y="345" font-family="Arial, Microsoft YaHei" font-size="13" fill="#555555">
            <tspan x="1090" dy="0" text-anchor="middle">512 卡集群落地</tspan>
            <tspan x="1090" dy="22" text-anchor="middle">支持万亿参数训练</tspan>
        </text>
        <text x="1090" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#C0392B" text-anchor="middle" font-weight="bold">
            单价提升 30%+
        </text>
    </g>
'''
    return create_svg_footer(svg, 7)

def generate_ai_services():
    """第 8 页：业务结构 - AI 应用与服务（102 亿）"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        业务结构 · AI 应用与服务
    </text>
    <rect x="60" y="95" width="300" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 收入数字 -->
    <text x="1100" y="90" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="end">
        102 亿
    </text>
    <text x="1100" y="115" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="end">
        同比 +34%
    </text>
    
    <!-- 构成说明 -->
    <rect x="60" y="140" width="560" height="100" fill="#F5F5F5" rx="8"/>
    <text x="100" y="175" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555">
        <tspan font-weight="bold">构成：</tspan>千帆 MaaS、文心大模型服务、行业 AI 解决方案、智能体、数字人
    </text>
    <text x="100" y="210" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">
        高毛利业务，占智能云总收入 34%
    </text>
    
    <!-- 四个核心驱动 -->
    
    <!-- 驱动 1：千帆 MaaS -->
    <g filter="url(#shadow)">
        <rect x="60" y="270" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="270" width="560" height="50" rx="12" fill="#EBF5FB"/>
        <text x="340" y="303" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🌊 千帆 MaaS 平台
        </text>
        <text x="340" y="345" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            模型训练 / 微调 / 推理 / Agent 开发一体化
        </text>
        <text x="340" y="390" font-family="Arial Black, Microsoft YaHei" font-size="28" font-weight="bold" fill="#27AE60" text-anchor="middle">
            Token 消耗月增 50%+
        </text>
        <text x="340" y="425" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            一站式模型服务，降低企业 AI 使用门槛
        </text>
    </g>
    
    <!-- 驱动 2：文心大模型 -->
    <g filter="url(#shadow)">
        <rect x="660" y="270" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="270" width="560" height="50" rx="12" fill="#FEF9E7"/>
        <text x="940" y="303" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12" text-anchor="middle">
            🧠 文心大模型 4.0
        </text>
        <text x="940" y="345" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            2025 年迭代至 4.0 版本
        </text>
        <text x="940" y="390" font-family="Arial Black, Microsoft YaHei" font-size="28" font-weight="bold" fill="#E67E22" text-anchor="middle">
            企业付费调用量季度翻倍
        </text>
        <text x="940" y="425" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            全模态、长文本、工具调用、智能体能力
        </text>
    </g>
    
    <!-- 驱动 3：行业 AI 落地 -->
    <g filter="url(#shadow)">
        <rect x="60" y="480" width="560" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="480" width="560" height="50" rx="12" fill="#E8F6F3"/>
        <text x="340" y="513" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            🏭 行业 AI 落地
        </text>
        <text x="340" y="560" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            金融风控 | 智能制造 | 自动驾驶云 | 电网智能调度
        </text>
        <text x="340" y="595" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            规模化交付，垂直行业深度渗透
        </text>
    </g>
    
    <!-- 驱动 4：超级智能体 -->
    <g filter="url(#shadow)">
        <rect x="660" y="480" width="560" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="480" width="560" height="50" rx="12" fill="#FDEDEC"/>
        <text x="940" y="513" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            🤖 超级智能体
        </text>
        <text x="940" y="560" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            "百度伐谋"获 2000+ 企业试用
        </text>
        <text x="940" y="595" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">
            "曦灵"数字人商业化落地
        </text>
    </g>
'''
    return create_svg_footer(svg, 8)

def generate_market_share():
    """第 9 页：客户与市场地位"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        客户与市场地位
    </text>
    <rect x="60" y="95" width="240" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 左侧：客户结构饼图 -->
    <rect x="60" y="140" width="560" height="380" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1" rx="12" filter="url(#shadow)"/>
    <text x="340" y="180" font-family="Arial, Microsoft YaHei" font-size="16" font-weight="bold" fill="{DARK_GRAY}" text-anchor="middle">
        客户结构
    </text>
    
    <!-- 简易饼图 -->
    <circle cx="260" cy="320" r="120" fill="#FFFFFF" stroke="#E8EAED" stroke-width="2"/>
    <!-- 互联网 35% -->
    <path d="M 260 200 A 120 120 0 0 1 370 270 L 260 320 Z" fill="{BAIDU_BLUE}"/>
    <!-- 金融 22% -->
    <path d="M 370 270 A 120 120 0 0 1 340 400 L 260 320 Z" fill="#5C67FF"/>
    <!-- 制造 18% -->
    <path d="M 340 400 A 120 120 0 0 1 180 400 L 260 320 Z" fill="#3498DB"/>
    <!-- 政企 15% -->
    <path d="M 180 400 A 120 120 0 0 1 150 270 L 260 320 Z" fill="#2ECC71"/>
    <!-- 其他 10% -->
    <path d="M 150 270 A 120 120 0 0 1 260 200 L 260 320 Z" fill="#F39C12"/>
    
    <!-- 图例 -->
    <text x="420" y="240" font-family="Arial, Microsoft YaHei" font-size="13" fill="#555555">
        <tspan x="420" dy="0">■ 互联网 35%</tspan>
        <tspan x="420" dy="25">■ 金融 22%</tspan>
        <tspan x="420" dy="25">■ 制造 18%</tspan>
        <tspan x="420" dy="25">■ 政企 15%</tspan>
        <tspan x="420" dy="25">■ 其他 10%</tspan>
    </text>
    
    <!-- 右侧：市场份额和中标表现 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="560" height="50" rx="12" fill="{BAIDU_BLUE}"/>
        <text x="940" y="173" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
            🏆 市场份额
        </text>
        
        <text x="940" y="230" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            中国 AI 云全栈服务
        </text>
        <text x="940" y="270" font-family="Arial Black, Microsoft YaHei" font-size="56" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            40.2%
        </text>
        <text x="940" y="300" font-family="Arial, Microsoft YaHei" font-size="14" fill="#27AE60" text-anchor="middle" font-weight="bold">
            行业第一 · 领跑市场
        </text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="660" y="340" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="340" width="560" height="50" rx="12" fill="#FEF9E7"/>
        <text x="940" y="373" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12" text-anchor="middle">
            📋 中标表现
        </text>
        
        <text x="940" y="430" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            2025 年大模型项目
        </text>
        <text x="940" y="470" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="#E67E22" text-anchor="middle">
            109 个 / 9 亿元
        </text>
        <text x="940" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#27AE60" text-anchor="middle" font-weight="bold">
            连续两年 项目数/金额双第一
        </text>
    </g>
'''
    return create_svg_footer(svg, 9)

def generate_kunlun_chip():
    """第 10 页：关键战略 - 昆仑芯 AI 芯片"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        关键战略 · 昆仑芯 AI 芯片
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 主卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="1160" height="120" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="1160" height="60" rx="12" fill="{BAIDU_BLUE}"/>
        <text x="120" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">
            💡 核心动作
        </text>
        <text x="640" y="180" font-family="Arial, Microsoft YaHei" font-size="16" fill="#E0E0FF" text-anchor="middle">
            二代昆仑芯（P800）量产，覆盖训练 / 微调 / 推理全栈
        </text>
    </g>
    
    <!-- 三个财报影响 -->
    
    <!-- 影响 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="290" width="360" height="50" rx="12" fill="#FEF9E7"/>
        <text x="240" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#F39C12" text-anchor="middle">
            📈 新增长曲线
        </text>
        <text x="240" y="380" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            超 50 亿元
        </text>
        <text x="240" y="420" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            芯片相关收入
        </text>
        <text x="240" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            成为独立增长引擎
        </text>
    </g>
    
    <!-- 影响 2 -->
    <g filter="url(#shadow)">
        <rect x="440" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="440" y="290" width="360" height="50" rx="12" fill="#E8F6F3"/>
        <text x="620" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            💰 成本优化
        </text>
        <text x="620" y="380" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="#27AE60" text-anchor="middle">
            -25%~-30%
        </text>
        <text x="620" y="420" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            云基础设施成本下降
        </text>
        <text x="620" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            毛利率改善 +3~+5pct
        </text>
    </g>
    
    <!-- 影响 3 -->
    <g filter="url(#shadow)">
        <rect x="820" y="290" width="400" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="820" y="290" width="400" height="50" rx="12" fill="#EBF5FB"/>
        <text x="1020" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🛡️ 国产替代壁垒
        </text>
        <text x="1020" y="380" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            强化自主可控能力
        </text>
        <text x="1020" y="420" font-family="Arial Black, Microsoft YaHei" font-size="28" font-weight="bold" fill="#27AE60" text-anchor="middle">
            政企订单 +40%
        </text>
        <text x="1020" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            国产芯片首选供应商
        </text>
    </g>
    
    <!-- 底部总结 -->
    <rect x="60" y="540" width="1160" height="80" fill="#F8F9FA" rx="8"/>
    <text x="640" y="575" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
        昆仑芯规模化商用是百度智能云 2025 年核心竞争力之一，实现成本优化与收入增长双赢
    </text>
    <text x="640" y="600" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
        自研芯片战略 | 全栈覆盖 | 外部客户占比 70% | 成本下降 25%+
    </text>
'''
    return create_svg_footer(svg, 10)

def generate_qianfan_maas():
    """第 11 页：关键战略 - 千帆 MaaS 平台"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        关键战略 · 千帆 MaaS 平台
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 主卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="1160" height="120" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="1160" height="60" rx="12" fill="{BAIDU_BLUE}"/>
        <text x="120" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">
            💡 核心动作
        </text>
        <text x="640" y="180" font-family="Arial, Microsoft YaHei" font-size="16" fill="#E0E0FF" text-anchor="middle">
            一站式模型商店、行业大模型定制、智能体开发工具链
        </text>
    </g>
    
    <!-- 三个财报影响 -->
    
    <!-- 影响 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="290" width="360" height="50" rx="12" fill="#FEF9E7"/>
        <text x="240" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#F39C12" text-anchor="middle">
            📈 收入高增
        </text>
        <text x="240" y="380" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="#E67E22" text-anchor="middle">
            +225%
        </text>
        <text x="240" y="420" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            MaaS 收入增长
        </text>
        <text x="240" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            占比升至 22%
        </text>
    </g>
    
    <!-- 影响 2 -->
    <g filter="url(#shadow)">
        <rect x="440" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="440" y="290" width="360" height="50" rx="12" fill="#E8F6F3"/>
        <text x="620" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            💎 高毛利拉动
        </text>
        <text x="620" y="380" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="#27AE60" text-anchor="middle">
            65%~70%
        </text>
        <text x="620" y="420" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            MaaS 毛利率
        </text>
        <text x="620" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            拉动整体盈利改善
        </text>
    </g>
    
    <!-- 影响 3 -->
    <g filter="url(#shadow)">
        <rect x="820" y="290" width="400" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="820" y="290" width="400" height="50" rx="12" fill="#EBF5FB"/>
        <text x="1020" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            👥 客户粘性提升
        </text>
        <text x="1020" y="370" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            <tspan x="1020" dy="0">客户 LTV</tspan>
            <tspan font-weight="bold" fill="#27AE60" font-size="20"> +60%</tspan>
            <tspan x="1020" dy="30">| 流失率</tspan>
            <tspan font-weight="bold" fill="#E74C3C" font-size="20"> -15%</tspan>
        </text>
        <text x="1020" y="440" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            外部收入占比 90%+
        </text>
        <text x="1020" y="470" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            平台化效应显著
        </text>
    </g>
    
    <!-- 底部总结 -->
    <rect x="60" y="540" width="1160" height="80" fill="#F8F9FA" rx="8"/>
    <text x="640" y="575" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
        千帆 MaaS 平台是百度智能云商业化成功的核心引擎，实现收入、毛利、客户粘性三重提升
    </text>
    <text x="640" y="600" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
        模型商店 | 行业定制 | 智能体工具链 | Token 消耗月增 50%+
    </text>
'''
    return create_svg_footer(svg, 11)

def generate_ernie_model():
    """第 12 页：关键战略 - 文心大模型 4.0"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        关键战略 · 文心大模型 4.0
    </text>
    <rect x="60" y="95" width="280" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 主卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="1160" height="120" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="1160" height="60" rx="12" fill="{BAIDU_BLUE}"/>
        <text x="120" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">
            💡 核心动作
        </text>
        <text x="640" y="180" font-family="Arial, Microsoft YaHei" font-size="16" fill="#E0E0FF" text-anchor="middle">
            全模态、长文本、工具调用、智能体能力全面开放
        </text>
    </g>
    
    <!-- 三个财报影响 -->
    
    <!-- 影响 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="290" width="360" height="50" rx="12" fill="#FEF9E7"/>
        <text x="240" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#F39C12" text-anchor="middle">
            📈 收入带动
        </text>
        <text x="240" y="380" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="#E67E22" text-anchor="middle">
            +200%
        </text>
        <text x="240" y="420" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            MaaS/API 收入增长
        </text>
        <text x="240" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            成为核心竞争力
        </text>
    </g>
    
    <!-- 影响 2 -->
    <g filter="url(#shadow)">
        <rect x="440" y="290" width="360" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="440" y="290" width="360" height="50" rx="12" fill="#E8F6F3"/>
        <text x="620" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            🔄 能力升级
        </text>
        <text x="620" y="370" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            <tspan x="620" dy="0">全模态理解</tspan>
            <tspan x="620" dy="28">长文本处理</tspan>
            <tspan x="620" dy="28">工具调用</tspan>
            <tspan x="620" dy="28">智能体编排</tspan>
        </text>
        <text x="620" y="470" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            企业级能力全面开放
        </text>
    </g>
    
    <!-- 影响 3 -->
    <g filter="url(#shadow)">
        <rect x="820" y="290" width="400" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="820" y="290" width="400" height="50" rx="12" fill="#EBF5FB"/>
        <text x="1020" y="323" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🌐 生态协同
        </text>
        <text x="1020" y="370" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555" text-anchor="middle">
            <tspan x="1020" dy="0">与搜索、网盘、文库协同</tspan>
        </text>
        <text x="1020" y="420" font-family="Arial Black, Microsoft YaHei" font-size="24" font-weight="bold" fill="#27AE60" text-anchor="middle">
            C 端 + B 端 闭环形成
        </text>
        <text x="1020" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            全场景覆盖
        </text>
    </g>
    
    <!-- 底部总结 -->
    <rect x="60" y="540" width="1160" height="80" fill="#F8F9FA" rx="8"/>
    <text x="640" y="575" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
        文心大模型 4.0 是百度 AI 技术实力的集中体现，驱动 MaaS 收入增长，构建 C 端+B 端生态闭环
    </text>
    <text x="640" y="600" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
        全模态 | 长文本 | 工具调用 | 智能体 | 生态协同
    </text>
'''
    return create_svg_footer(svg, 12)

def generate_risks():
    """第 13 页：核心风险与挑战"""
    svg = create_svg_header()
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{DARK_GRAY}">
        核心风险与挑战
    </text>
    <rect x="60" y="95" width="240" height="4" rx="2" fill="{BAIDU_BLUE}"/>
    
    <!-- 四个风险卡片 -->
    
    <!-- 风险 1：竞争加剧 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="560" height="50" rx="12" fill="#FDEDEC"/>
        <text x="340" y="173" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            ⚠️ 行业竞争加剧
        </text>
        <text x="100" y="220" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan>• 阿里云、华为云、腾讯云持续加大 AI 投入</tspan>
            <tspan x="100" dy="28">• 价格战压力可能影响利润率</tspan>
            <tspan x="100" dy="28">• 需要持续保持技术领先优势</tspan>
        </text>
    </g>
    
    <!-- 风险 2：资本开支 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="560" height="50" rx="12" fill="#FEF9E7"/>
        <text x="940" y="173" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12" text-anchor="middle">
            💸 高资本开支压力
        </text>
        <text x="700" y="220" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan>• 2025 年智算投入 250~280 亿元</tspan>
            <tspan x="700" dy="28">• 昆仑芯研发 + 产能扩张持续投入</tspan>
            <tspan x="700" dy="28">• 短期盈利承压，需平衡投入与回报</tspan>
        </text>
    </g>
    
    <!-- 风险 3：技术迭代 -->
    <g filter="url(#shadow)">
        <rect x="60" y="350" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="350" width="560" height="50" rx="12" fill="#F5EEF8"/>
        <text x="340" y="383" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#9B59B6" text-anchor="middle">
            🔄 技术迭代风险
        </text>
        <text x="100" y="430" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan>• 大模型技术快速演进，需持续研发投入</tspan>
            <tspan x="100" dy="28">• 国际头部模型（GPT-5 等）可能形成代差</tspan>
            <tspan x="100" dy="28">• 人才竞争激烈，核心技术人员流失风险</tspan>
        </text>
    </g>
    
    <!-- 风险 4：宏观环境 -->
    <g filter="url(#shadow)">
        <rect x="660" y="350" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="350" width="560" height="50" rx="12" fill="#EBF5FB"/>
        <text x="940" y="383" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            🌍 宏观经济环境
        </text>
        <text x="700" y="430" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
            <tspan>• 企业 IT 预算可能受经济波动影响</tspan>
            <tspan x="700" dy="28">• AI 项目 ROI 验证周期较长</tspan>
            <tspan x="700" dy="28">• 政企客户决策周期长、回款慢</tspan>
        </text>
    </g>
    
    <!-- 底部应对策略 -->
    <rect x="60" y="560" width="1160" height="80" fill="#E8F6F3" rx="8"/>
    <text x="100" y="595" font-family="Arial Black, Microsoft YaHei" font-size="15" font-weight="bold" fill="#1ABC9C">
        💡 应对策略：
    </text>
    <text x="220" y="595" font-family="Arial, Microsoft YaHei" font-size="14" fill="#555555">
        持续技术创新 · 优化成本结构 · 深化行业落地 · 加强生态合作
    </text>
'''
    return create_svg_footer(svg, 13)

def generate_summary():
    """第 14 页：总结：AI 云兑现元年"""
    svg = create_svg_header()
    svg += f'''
    <!-- 背景装饰 -->
    <rect x="0" y="0" width="1280" height="200" fill="url(#blueGradient)"/>
    
    <!-- 标题 -->
    <text x="640" y="100" font-family="Arial Black, Microsoft YaHei" font-size="40" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
        总结：AI 云兑现元年
    </text>
    <text x="640" y="150" font-family="Arial, Microsoft YaHei" font-size="18" fill="#E0E0FF" text-anchor="middle">
        百度智能云 2025 年核心洞察
    </text>
    
    <!-- 四个关键结论 -->
    
    <!-- 结论 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="230" width="560" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="230" width="560" height="60" rx="12" fill="#FEF9E7"/>
        <text x="340" y="268" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#F39C12" text-anchor="middle">
            ✅ 高增长验证
        </text>
        <text x="340" y="320" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            总收入 300 亿，同比 +34%
        </text>
        <text x="340" y="355" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            在百度整体 -3% 背景下逆势高增
        </text>
        <text x="340" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            AI 成为核心增长引擎
        </text>
    </g>
    
    <!-- 结论 2 -->
    <g filter="url(#shadow)">
        <rect x="660" y="230" width="560" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="230" width="560" height="60" rx="12" fill="#E8F6F3"/>
        <text x="940" y="268" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#1ABC9C" text-anchor="middle">
            ✅ 全栈壁垒形成
        </text>
        <text x="940" y="320" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            昆仑芯 → 天池 → 千帆 → 文心 → Agent
        </text>
        <text x="940" y="355" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            完整技术闭环落地
        </text>
        <text x="940" y="395" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            自研芯片 + 平台化双轮驱动
        </text>
    </g>
    
    <!-- 结论 3 -->
    <g filter="url(#shadow)">
        <rect x="60" y="460" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="460" width="560" height="60" rx="12" fill="#EBF5FB"/>
        <text x="340" y="498" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{BAIDU_BLUE}" text-anchor="middle">
            ✅ 市场地位稳固
        </text>
        <text x="340" y="550" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            AI 云全栈市占率 40.2% 行业第一
        </text>
        <text x="340" y="585" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            大模型中标 109 个/9 亿 双第一
        </text>
        <text x="340" y="620" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            政企/金融深度渗透
        </text>
    </g>
    
    <!-- 结论 4 -->
    <g filter="url(#shadow)">
        <rect x="660" y="460" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="460" width="560" height="60" rx="12" fill="#FDEDEC"/>
        <text x="940" y="498" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="#E74C3C" text-anchor="middle">
            ⚠️ 投入期持续
        </text>
        <text x="940" y="550" font-family="Arial, Microsoft YaHei" font-size="15" fill="#555555" text-anchor="middle">
            2025 年仍处高投入期，整体未盈利
        </text>
        <text x="940" y="585" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">
            AI 算力/高毛利 MaaS 利润率改善
        </text>
        <text x="940" y="620" font-family="Arial, Microsoft YaHei" font-size="13" fill="#999999" text-anchor="middle">
            平衡投入与回报是关键
        </text>
    </g>
'''
    return create_svg_footer(svg, 14)

# 生成所有 SVG 文件
slides = [
    ("01_cover.svg", generate_cover),
    ("02_data_baseline.svg", generate_data_baseline),
    ("03_core_metrics.svg", generate_core_metrics),
    ("04_overview_features.svg", generate_overview_features),
    ("05_quarterly_data.svg", generate_quarterly_data),
    ("06_quarterly_trend.svg", generate_quarterly_trend),
    ("07_infrastructure.svg", generate_infrastructure),
    ("08_ai_services.svg", generate_ai_services),
    ("09_market_share.svg", generate_market_share),
    ("10_kunlun_chip.svg", generate_kunlun_chip),
    ("11_qianfan_maas.svg", generate_qianfan_maas),
    ("12_ernie_model.svg", generate_ernie_model),
    ("13_risks.svg", generate_risks),
    ("14_summary.svg", generate_summary),
]

os.makedirs(SVG_OUTPUT_DIR, exist_ok=True)

for filename, generator in slides:
    filepath = os.path.join(SVG_OUTPUT_DIR, filename)
    svg_content = generator()
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"✅ 已生成：{filename}")

print(f"\n🎉 完成！共生成 {len(slides)} 页 SVG 文件")
print(f"输出目录：{SVG_OUTPUT_DIR}")
