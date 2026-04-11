#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成英伟达 2026 财年财报深度分析 PPT 的 SVG 文件
共 14 页
"""

import os

PROJECT_DIR = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/nvidia_2026_financial_ppt169_20260410"
SVG_OUTPUT_DIR = os.path.join(PROJECT_DIR, "svg_output")

# 英伟达绿
NVIDIA_GREEN = "#76B900"
NVIDIA_GREEN_DARK = "#5FA000"
TECH_BLACK = "#1A1A1A"
DARK_GRAY = "#333333"
LIGHT_GRAY = "#F0F0F0"
WHITE = "#FFFFFF"
ACCENT_GREEN = "#5FA000"

def create_svg_header(title=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
    <defs>
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F8F9FA;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="greenGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{NVIDIA_GREEN};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{NVIDIA_GREEN_DARK};stop-opacity:1" />
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
    svg_content += f'''
    <!-- 页脚 -->
    <rect x="0" y="680" width="1280" height="40" fill="#F0F0F0" opacity="0.5"/>
    <text x="60" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999">
        英伟达 2026 财年财报深度分析
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
    <rect x="0" y="0" width="1280" height="200" fill="url(#greenGradient)"/>
    
    <!-- 主标题 -->
    <text x="640" y="100" font-family="Arial Black, Microsoft YaHei" font-size="44" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
        英伟达 2026 财年财报深度分析
    </text>
    
    <!-- 副标题 -->
    <text x="640" y="150" font-family="Arial, Microsoft YaHei" font-size="20" fill="#E0FFE0" text-anchor="middle">
        AI 算力时代的巅峰答卷 · 全年营收 2159 亿美元
    </text>
    
    <!-- 装饰线条 -->
    <rect x="440" y="220" width="400" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 信息卡片 -->
    <g filter="url(#shadow)">
        <rect x="340" y="300" width="600" height="120" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <text x="640" y="340" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
            财年周期：截至 2026 年 1 月 25 日
        </text>
        <text x="640" y="370" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
            全年营收：2159.38 亿美元（同比 +65.5%）
        </text>
        <text x="640" y="400" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
            净利润：1200.67 亿美元（同比 +64.8%）
        </text>
    </g>
    
    <!-- 底部装饰 -->
    <rect x="0" y="620" width="1280" height="100" fill="#F8F9FA"/>
    <text x="640" y="670" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999" text-anchor="middle">
        2026 年 4 月 · 内部汇报材料
    </text>
'''
    svg = create_svg_footer(svg, 1)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "01_cover.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_financial_overview():
    """第 2 页：核心财务指标概览"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        核心财务指标概览
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 表格标题 -->
    <rect x="60" y="130" width="1160" height="40" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="100" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">指标</text>
    <text x="300" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">2026 财年</text>
    <text x="500" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">2025 财年</text>
    <text x="700" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">同比变化</text>
    <text x="900" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">关键解读</text>
    
    <!-- 表格行 1 -->
    <rect x="60" y="170" width="1160" height="35" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="192" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">总营收</text>
    <text x="300" y="192" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">2159.38 亿</text>
    <text x="500" y="192" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">1304.97 亿</text>
    <text x="700" y="192" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+65.5%</text>
    <text x="900" y="192" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">连续两年高增长，规模突破 2000 亿</text>
    
    <!-- 表格行 2 -->
    <rect x="60" y="205" width="1160" height="35" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="227" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">GAAP 净利润</text>
    <text x="300" y="227" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">1200.67 亿</text>
    <text x="500" y="227" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">728.80 亿</text>
    <text x="700" y="227" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+64.8%</text>
    <text x="900" y="227" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">盈利规模翻倍，日均净赚 3.28 亿</text>
    
    <!-- 表格行 3 -->
    <rect x="60" y="240" width="1160" height="35" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="262" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">GAAP 毛利率</text>
    <text x="300" y="262" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">71.1%</text>
    <text x="500" y="262" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">69.7%</text>
    <text x="700" y="262" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+1.4pct</text>
    <text x="900" y="262" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">高端产品占比提升，规模效应强化</text>
    
    <!-- 表格行 4 -->
    <rect x="60" y="275" width="1160" height="35" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="297" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">经营现金流</text>
    <text x="300" y="297" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">1027.18 亿</text>
    <text x="500" y="297" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">640.89 亿</text>
    <text x="700" y="297" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+60.3%</text>
    <text x="900" y="297" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">现金流充沛，支撑研发与股东回报</text>
    
    <!-- 表格行 5 -->
    <rect x="60" y="310" width="1160" height="35" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="332" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">每股收益</text>
    <text x="300" y="332" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">4.93 美元</text>
    <text x="500" y="332" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">2.97 美元</text>
    <text x="700" y="332" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+66.0%</text>
    <text x="900" y="332" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">股东回报显著，业绩兑现度高</text>
    
    <!-- 表格行 6 -->
    <rect x="60" y="345" width="1160" height="35" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="367" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">资产负债率</text>
    <text x="300" y="367" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">23.9%</text>
    <text x="500" y="367" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">28.9%</text>
    <text x="700" y="367" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">-5.0pct</text>
    <text x="900" y="367" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">财务结构稳健，抗风险能力极强</text>
'''
    
    svg = create_svg_footer(svg, 2)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "02_financial_overview.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_performance_features():
    """第 3 页：整体业绩核心特征"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        整体业绩核心特征
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 特征卡片 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="8" height="220" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">增长质量双优</text>
        <text x="100" y="215" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 营收与净利润增速均超 65%</text>
        <text x="100" y="240" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 毛利率持续上行至 71.1%</text>
        <text x="100" y="265" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 费用增速远低于营收增速</text>
        <text x="100" y="290" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 运营效率大幅优化</text>
        <text x="580" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">1</text>
    </g>
    
    <!-- 特征卡片 2 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="8" height="220" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">结构高度集中</text>
        <text x="700" y="215" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 数据中心业务占总营收 89.7%</text>
        <text x="700" y="240" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 成为绝对核心增长引擎</text>
        <text x="700" y="265" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 其他业务协同增长</text>
        <text x="700" y="290" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 业务结构清晰聚焦</text>
        <text x="1180" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">2</text>
    </g>
    
    <!-- 特征卡片 3 -->
    <g filter="url(#shadow)">
        <rect x="60" y="400" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="400" width="8" height="220" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="440" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">现金流超级充沛</text>
        <text x="100" y="475" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 经营现金流破 1027 亿美元</text>
        <text x="100" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 自由现金流近 970 亿美元</text>
        <text x="100" y="525" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 现金储备超 625 亿美元</text>
        <text x="100" y="550" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 具备极强战略扩张能力</text>
        <text x="580" y="430" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">3</text>
    </g>
    
    <!-- 特征卡片 4 -->
    <g filter="url(#shadow)">
        <rect x="660" y="400" width="560" height="220" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="400" width="8" height="220" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="440" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">增长韧性强劲</text>
        <text x="700" y="475" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 全年四季度均环比正增长</text>
        <text x="700" y="500" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 无季度下滑记录</text>
        <text x="700" y="525" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• AI 需求转向稳健持续增长</text>
        <text x="700" y="550" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 业绩确定性极强</text>
        <text x="1180" y="430" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">4</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 3)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "03_performance_features.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_datacenter_business():
    """第 4 页：分领域业务 - 数据中心业务"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        数据中心业务 - 核心增长极
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 核心数据 -->
    <rect x="60" y="130" width="300" height="150" rx="8" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="210" y="175" font-family="Arial Black, Microsoft YaHei" font-size="42" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">1937.37 亿</text>
    <text x="210" y="205" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">全年收入 · 同比 +68.2%</text>
    <text x="210" y="230" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">占总营收 89.7%</text>
    
    <!-- Q4 数据 -->
    <rect x="400" y="130" width="300" height="150" rx="8" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="550" y="165" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">Q4 单季收入</text>
    <text x="550" y="200" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{DARK_GRAY}" text-anchor="middle">623.14 亿</text>
    <text x="550" y="230" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">同比 +75% · 环比 +22%</text>
    
    <!-- 产品结构 -->
    <rect x="740" y="130" width="480" height="150" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="780" y="160" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">产品结构</text>
    <rect x="780" y="180" width="400" height="30" rx="4" fill="#E8EAED"/>
    <rect x="780" y="180" width="267" height="30" rx="4" fill="{NVIDIA_GREEN}"/>
    <text x="980" y="200" font-family="Arial, Microsoft YaHei" font-size="12" fill="#FFFFFF" text-anchor="middle">GB 系统 2/3</text>
    <text x="780" y="230" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• Grace Blackwell 系统占数据中心营收 2/3</text>
    <text x="780" y="255" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 高端产品占比持续提升</text>
    
    <!-- 核心驱动 -->
    <text x="60" y="330" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">核心驱动因素</text>
    
    <!-- 驱动卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="360" width="280" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="90" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">Blackwell 架构</text>
        <text x="90" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">全面落地，支撑</text>
        <text x="90" y="445" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">全年核心增长</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="360" y="360" width="280" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="360" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="390" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">AI 推理需求</text>
        <text x="390" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">爆发式增长，</text>
        <text x="390" y="445" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">成为新增长点</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="660" y="360" width="280" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="690" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">云厂商采购</text>
        <text x="690" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">头部云厂商</text>
        <text x="690" y="445" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">集中采购放量</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="960" y="360" width="280" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="960" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="990" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">高速网络业务</text>
        <text x="990" y="420" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">爆发式增长，</text>
        <text x="990" y="445" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">贡献显著增量</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 4)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "04_datacenter_business.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_gaming_business():
    """第 5 页：分领域业务 - 游戏业务"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        游戏业务 - 稳健增长
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 核心数据 -->
    <rect x="60" y="130" width="300" height="150" rx="8" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="210" y="175" font-family="Arial Black, Microsoft YaHei" font-size="42" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">160.42 亿</text>
    <text x="210" y="205" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">全年收入 · 同比 +41.3%</text>
    <text x="210" y="230" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">占总营收 7.4%</text>
    
    <!-- 市场份额 -->
    <rect x="400" y="130" width="300" height="150" rx="8" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="550" y="165" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">AI PC 显卡市场份额</text>
    <text x="550" y="210" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">70%+</text>
    <text x="550" y="245" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">占据主导地位</text>
    
    <!-- 增长趋势图 -->
    <rect x="740" y="130" width="480" height="150" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="780" y="160" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">季度增长趋势</text>
    <!-- 简化的柱状图 -->
    <rect x="800" y="200" width="60" height="40" fill="{NVIDIA_GREEN}" opacity="0.6"/>
    <rect x="880" y="190" width="60" height="50" fill="{NVIDIA_GREEN}" opacity="0.7"/>
    <rect x="960" y="180" width="60" height="60" fill="{NVIDIA_GREEN}" opacity="0.8"/>
    <rect x="1040" y="170" width="60" height="70" fill="{NVIDIA_GREEN}"/>
    <text x="830" y="260" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666666" text-anchor="middle">Q1</text>
    <text x="910" y="260" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666666" text-anchor="middle">Q2</text>
    <text x="990" y="260" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666666" text-anchor="middle">Q3</text>
    <text x="1070" y="260" font-family="Arial, Microsoft YaHei" font-size="11" fill="#666666" text-anchor="middle">Q4</text>
    
    <!-- 核心驱动 -->
    <text x="60" y="330" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">核心驱动因素</text>
    
    <!-- 驱动卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="360" width="380" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="90" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">RTX 50 系列显卡发布</text>
        <text x="90" y="425" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">新一代游戏显卡上市，性能大幅提升，</text>
        <text x="90" y="450" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">带动游戏业务收入增长</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="480" y="360" width="380" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="480" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="510" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">AI PC 渗透率提升</text>
        <text x="510" y="425" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">AI PC 市场快速增长，英伟达占据</text>
        <text x="510" y="450" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">AI PC 显卡 70%+ 市场份额</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="900" y="360" width="380" height="140" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="900" y="360" width="6" height="140" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="930" y="395" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">游戏生态持续优化</text>
        <text x="930" y="425" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">DLSS 4.0、光线追踪等技术普及，</text>
        <text x="930" y="450" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">提升用户体验和购买意愿</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 5)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "05_gaming_business.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_other_business():
    """第 6 页：分领域业务 - 专业可视化/汽车/其他"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        其他业务板块 - 协同增长
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 专业可视化 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="360" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="8" height="200" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">专业可视化业务</text>
        <text x="100" y="220" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{NVIDIA_GREEN}">32.00 亿</text>
        <text x="100" y="250" font-family="Arial, Microsoft YaHei" font-size="14" fill="#5FA000">同比 +70.0% · 占总营收 1.5%</text>
        <text x="100" y="285" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• 工业元宇宙、AI 设计、数字孪生</text>
        <text x="100" y="305" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• RTX PRO 专业显卡需求爆发</text>
        <text x="380" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">高增长</text>
    </g>
    
    <!-- 汽车业务 -->
    <g filter="url(#shadow)">
        <rect x="460" y="140" width="360" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="460" y="140" width="8" height="200" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="500" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">汽车业务</text>
        <text x="500" y="220" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{NVIDIA_GREEN}">23.00 亿</text>
        <text x="500" y="250" font-family="Arial, Microsoft YaHei" font-size="14" fill="#5FA000">同比 +39.0% · 占总营收 1.1%</text>
        <text x="500" y="285" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• 自动驾驶平台量产落地</text>
        <text x="500" y="305" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• 车载 AI 算力需求提升</text>
        <text x="780" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">稳定增长</text>
    </g>
    
    <!-- OEM 及其他 -->
    <g filter="url(#shadow)">
        <rect x="860" y="140" width="360" height="200" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="860" y="140" width="8" height="200" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="900" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">OEM 及其他业务</text>
        <text x="900" y="220" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{NVIDIA_GREEN}">6.59 亿</text>
        <text x="900" y="250" font-family="Arial, Microsoft YaHei" font-size="14" fill="#5FA000">同比 +25.0% · 占总营收 0.3%</text>
        <text x="900" y="285" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• 边缘 AI、嵌入式计算</text>
        <text x="900" y="305" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666">• 工业解决方案</text>
        <text x="1180" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">补充</text>
    </g>
    
    <!-- 业务对比图 -->
    <text x="60" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">业务收入对比（单位：亿美元）</text>
    
    <!-- 柱状图 -->
    <rect x="100" y="440" width="200" height="150" fill="#F8F9FA" rx="4"/>
    <rect x="120" y="520" width="160" height="70" fill="{NVIDIA_GREEN}" opacity="0.6"/>
    <text x="200" y="510" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">32.00</text>
    <text x="200" y="610" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">专业可视化</text>
    
    <rect x="340" y="440" width="200" height="150" fill="#F8F9FA" rx="4"/>
    <rect x="360" y="540" width="160" height="50" fill="{NVIDIA_GREEN}" opacity="0.7"/>
    <text x="440" y="530" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">23.00</text>
    <text x="440" y="610" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">汽车</text>
    
    <rect x="580" y="440" width="200" height="150" fill="#F8F9FA" rx="4"/>
    <rect x="600" y="570" width="160" height="20" fill="{NVIDIA_GREEN}" opacity="0.8"/>
    <text x="680" y="560" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">6.59</text>
    <text x="680" y="610" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">其他</text>
'''
    
    svg = create_svg_footer(svg, 6)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "06_other_business.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_business_comparison():
    """第 7 页：业务结构对比表"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        业务结构对比表
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 表格标题 -->
    <rect x="60" y="130" width="1160" height="40" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="100" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">业务板块</text>
    <text x="300" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">2026 财年收入（亿）</text>
    <text x="550" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">同比增速</text>
    <text x="750" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">占总营收比</text>
    <text x="950" y="155" font-family="Arial, Microsoft YaHei" font-size="14" font-weight="bold" fill="{DARK_GRAY}">增长评级</text>
    
    <!-- 表格行 1 - 数据中心 -->
    <rect x="60" y="170" width="1160" height="50" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="195" font-family="Arial Black, Microsoft YaHei" font-size="15" font-weight="bold" fill="{TECH_BLACK}">数据中心</text>
    <text x="300" y="195" font-family="Arial Bold, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">1937.37</text>
    <text x="550" y="195" font-family="Arial, Microsoft YaHei" font-size="15" fill="#5FA000">+68.2%</text>
    <text x="750" y="195" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">89.7%</text>
    <text x="950" y="195" font-family="Arial Black, Microsoft YaHei" font-size="18" fill="#FFD700">★★★★★</text>
    
    <!-- 表格行 2 - 游戏 -->
    <rect x="60" y="220" width="1160" height="50" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="245" font-family="Arial, Microsoft YaHei" font-size="15" fill="{DARK_GRAY}">游戏</text>
    <text x="300" y="245" font-family="Arial Bold, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">160.42</text>
    <text x="550" y="245" font-family="Arial, Microsoft YaHei" font-size="15" fill="#5FA000">+41.3%</text>
    <text x="750" y="245" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">7.4%</text>
    <text x="950" y="245" font-family="Arial Black, Microsoft YaHei" font-size="18" fill="#C0C0C0">★★★★</text>
    
    <!-- 表格行 3 - 专业可视化 -->
    <rect x="60" y="270" width="1160" height="50" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="295" font-family="Arial, Microsoft YaHei" font-size="15" fill="{DARK_GRAY}">专业可视化</text>
    <text x="300" y="295" font-family="Arial Bold, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">32.00</text>
    <text x="550" y="295" font-family="Arial, Microsoft YaHei" font-size="15" fill="#5FA000">+70.0%</text>
    <text x="750" y="295" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">1.5%</text>
    <text x="950" y="295" font-family="Arial Black, Microsoft YaHei" font-size="18" fill="#FFD700">★★★★★</text>
    
    <!-- 表格行 4 - 汽车 -->
    <rect x="60" y="320" width="1160" height="50" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="345" font-family="Arial, Microsoft YaHei" font-size="15" fill="{DARK_GRAY}">汽车</text>
    <text x="300" y="345" font-family="Arial Bold, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">23.00</text>
    <text x="550" y="345" font-family="Arial, Microsoft YaHei" font-size="15" fill="#5FA000">+39.0%</text>
    <text x="750" y="345" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">1.1%</text>
    <text x="950" y="345" font-family="Arial Black, Microsoft YaHei" font-size="18" fill="#C0C0C0">★★★★</text>
    
    <!-- 表格行 5 - 其他 -->
    <rect x="60" y="370" width="1160" height="50" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="395" font-family="Arial, Microsoft YaHei" font-size="15" fill="{DARK_GRAY}">其他</text>
    <text x="300" y="395" font-family="Arial Bold, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">6.59</text>
    <text x="550" y="395" font-family="Arial, Microsoft YaHei" font-size="15" fill="#5FA000">+25.0%</text>
    <text x="750" y="395" font-family="Arial, Microsoft YaHei" font-size="15" fill="#666666">0.3%</text>
    <text x="950" y="395" font-family="Arial Black, Microsoft YaHei" font-size="18" fill="#CD7F32">★★★</text>
    
    <!-- 饼图 - 业务结构 -->
    <text x="60" y="470" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">收入结构分布</text>
    
    <!-- 简化的饼图 -->
    <circle cx="200" cy="550" r="80" fill="{NVIDIA_GREEN}" opacity="0.9"/>
    <circle cx="200" cy="550" r="80" fill="none" stroke="#FFFFFF" stroke-width="2"/>
    <path d="M 200 470 L 200 550 A 80 80 0 0 1 270 510 Z" fill="#FFFFFF" opacity="0.3"/>
    <text x="200" y="555" font-family="Arial, Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">数据中心 89.7%</text>
    
    <!-- 图例 -->
    <rect x="340" y="500" width="20" height="20" fill="{NVIDIA_GREEN}"/>
    <text x="370" y="515" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">数据中心 89.7%</text>
    
    <rect x="340" y="530" width="20" height="20" fill="{NVIDIA_GREEN}" opacity="0.7"/>
    <text x="370" y="545" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">游戏 7.4%</text>
    
    <rect x="500" y="500" width="20" height="20" fill="{NVIDIA_GREEN}" opacity="0.5"/>
    <text x="530" y="515" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">专业可视化 1.5%</text>
    
    <rect x="500" y="530" width="20" height="20" fill="{NVIDIA_GREEN}" opacity="0.3"/>
    <text x="530" y="545" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">汽车 1.1%</text>
    
    <rect x="660" y="500" width="20" height="20" fill="{NVIDIA_GREEN}" opacity="0.2"/>
    <text x="690" y="515" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">其他 0.3%</text>
'''
    
    svg = create_svg_footer(svg, 7)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "07_business_comparison.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_quarterly_data():
    """第 8 页：分季度财务数据"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        分季度财务数据
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 季度数据表格 -->
    <rect x="60" y="130" width="1160" height="220" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1" rx="8"/>
    
    <!-- 表格标题 -->
    <rect x="60" y="130" width="1160" height="35" fill="{NVIDIA_GREEN}" opacity="0.1" rx="8"/>
    <text x="100" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">季度</text>
    <text x="220" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">总营收（亿）</text>
    <text x="380" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">环比</text>
    <text x="500" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">同比</text>
    <text x="620" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">净利润（亿）</text>
    <text x="780" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">毛利率</text>
    <text x="920" y="153" font-family="Arial, Microsoft YaHei" font-size="13" font-weight="bold" fill="{DARK_GRAY}">数据中心收入（亿）</text>
    
    <!-- Q1 -->
    <rect x="60" y="165" width="1160" height="35" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">Q1</text>
    <text x="220" y="187" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">440.62</text>
    <text x="380" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">-</text>
    <text x="500" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+112%</text>
    <text x="620" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">187.75</text>
    <text x="780" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">70.1%</text>
    <text x="920" y="187" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">392.50</text>
    
    <!-- Q2 -->
    <rect x="60" y="200" width="1160" height="35" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">Q2</text>
    <text x="220" y="222" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">467.00</text>
    <text x="380" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+6%</text>
    <text x="500" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+56%</text>
    <text x="620" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">264.22</text>
    <text x="780" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">72.4%</text>
    <text x="920" y="222" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">418.00</text>
    
    <!-- Q3 -->
    <rect x="60" y="235" width="1160" height="35" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">Q3</text>
    <text x="220" y="257" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">570.06</text>
    <text x="380" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+22%</text>
    <text x="500" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+68%</text>
    <text x="620" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">319.10</text>
    <text x="780" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">73.4%</text>
    <text x="920" y="257" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">510.70</text>
    
    <!-- Q4 -->
    <rect x="60" y="270" width="1160" height="35" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="100" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="{DARK_GRAY}">Q4</text>
    <text x="220" y="292" font-family="Arial Bold, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">681.27</text>
    <text x="380" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+20%</text>
    <text x="500" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+73%</text>
    <text x="620" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">429.60</text>
    <text x="780" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">75.0%</text>
    <text x="920" y="292" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">623.14</text>
    
    <!-- 全年 -->
    <rect x="60" y="305" width="1160" height="45" fill="{NVIDIA_GREEN}" opacity="0.1" stroke="{NVIDIA_GREEN}" stroke-width="2"/>
    <text x="100" y="330" font-family="Arial Black, Microsoft YaHei" font-size="14" font-weight="bold" fill="{TECH_BLACK}">全年</text>
    <text x="220" y="330" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">2159.38</text>
    <text x="380" y="330" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">平均 +16%</text>
    <text x="500" y="330" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000">+65.5%</text>
    <text x="620" y="330" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{NVIDIA_GREEN}">1200.67</text>
    <text x="780" y="330" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">71.1%</text>
    <text x="920" y="330" font-family="Arial Black, Microsoft YaHei" font-size="14" font-weight="bold" fill="{NVIDIA_GREEN}">1937.37</text>
    
    <!-- 趋势图 -->
    <text x="60" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">季度营收趋势（单位：亿美元）</text>
    
    <!-- 折线图 -->
    <rect x="100" y="430" width="1080" height="200" fill="#F8F9FA" rx="8"/>
    <!-- 折线 -->
    <polyline points="150,550 400,520 650,420 900,350" fill="none" stroke="{NVIDIA_GREEN}" stroke-width="3"/>
    <!-- 数据点 -->
    <circle cx="150" cy="550" r="6" fill="{NVIDIA_GREEN}"/>
    <circle cx="400" cy="520" r="6" fill="{NVIDIA_GREEN}"/>
    <circle cx="650" cy="420" r="6" fill="{NVIDIA_GREEN}"/>
    <circle cx="900" cy="350" r="6" fill="{NVIDIA_GREEN}"/>
    <!-- 标签 -->
    <text x="150" y="580" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q1 440.62</text>
    <text x="400" y="580" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q2 467.00</text>
    <text x="650" y="580" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q3 570.06</text>
    <text x="900" y="580" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">Q4 681.27</text>
'''
    
    svg = create_svg_footer(svg, 8)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "08_quarterly_data.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_quarterly_features():
    """第 9 页：季度业绩核心特征"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        季度业绩核心特征
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 特征 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="160" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="8" height="160" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">增长逐季加速</text>
        <text x="100" y="215" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• Q2 短暂放缓后重回高增长轨道</text>
        <text x="100" y="240" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• Q3、Q4 环比增速分别达 22%、20%</text>
        <text x="100" y="265" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 同比增长持续保持 50%+ 高位</text>
        <text x="580" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">1</text>
    </g>
    
    <!-- 特征 2 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="160" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="8" height="160" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="180" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">盈利能力持续上行</text>
        <text x="700" y="215" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 毛利率逐季提升：70.1%→75.0%</text>
        <text x="700" y="240" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• Q4 单季毛利率创历史新高</text>
        <text x="700" y="265" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 高端产品占比提升驱动盈利改善</text>
        <text x="1180" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">2</text>
    </g>
    
    <!-- 特征 3 -->
    <g filter="url(#shadow)">
        <rect x="60" y="340" width="560" height="160" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="340" width="8" height="160" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="380" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">数据中心占比持续提高</text>
        <text x="100" y="415" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• Q1: 89.0% → Q4: 91.5%</text>
        <text x="100" y="440" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 业绩结构更集中、更稳定</text>
        <text x="100" y="465" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• AI 算力需求持续主导增长</text>
        <text x="580" y="370" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">3</text>
    </g>
    
    <!-- 特征 4 -->
    <g filter="url(#shadow)">
        <rect x="660" y="340" width="560" height="160" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="340" width="8" height="160" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="380" font-family="Arial Black, Microsoft YaHei" font-size="20" font-weight="bold" fill="{TECH_BLACK}">净利润增速超营收增速</text>
        <text x="700" y="415" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 规模效应持续释放</text>
        <text x="700" y="440" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• 费用控制得当，运营效率优化</text>
        <text x="700" y="465" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666">• Q4 单季净利润达 429.60 亿美元</text>
        <text x="1180" y="370" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">4</text>
    </g>
    
    <!-- 季度趋势总结 -->
    <rect x="60" y="540" width="1160" height="100" rx="8" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="640" y="580" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}" text-anchor="middle">季度趋势总结：增长加速 · 盈利提升 · 结构优化 · 韧性强劲</text>
    <text x="640" y="610" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">全年四个季度均实现环比正增长，无季度下滑，AI 需求从爆发式增长转向稳健持续增长</text>
'''
    
    svg = create_svg_footer(svg, 9)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "09_quarterly_features.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_strategy():
    """第 10 页：战略动作与财报协同"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        战略动作与财报协同
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 战略 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="8" height="180" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">技术产品迭代</text>
        <text x="100" y="215" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• Blackwell 架构全面落地，支撑全年核心增长</text>
        <text x="100" y="240" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• Rubin 推理平台发布，锁定 2027 财年增长</text>
        <text x="100" y="265" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 200 亿美元收购 Groq，强化推理竞争力</text>
        <text x="100" y="290" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 网络与存储产品爆发式增长</text>
        <text x="580" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">技术</text>
    </g>
    
    <!-- 战略 2 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="8" height="180" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">生态战略合作</text>
        <text x="700" y="215" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 与 Meta 达成多年千亿级战略合作</text>
        <text x="700" y="240" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 深度绑定 AWS、微软、谷歌、Oracle</text>
        <text x="700" y="265" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 生态投资超 700 亿美元</text>
        <text x="700" y="290" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 形成"投资 - 采购"闭环</text>
        <text x="1180" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">生态</text>
    </g>
    
    <!-- 战略 3 -->
    <g filter="url(#shadow)">
        <rect x="60" y="360" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="360" width="8" height="180" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">供应链与产能</text>
        <text x="100" y="435" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 锁定台积电 3nm/2nm 独家产能</text>
        <text x="100" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 供应链全球化布局，对冲地缘风险</text>
        <text x="100" y="485" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 提前备货，保障 2027 财年交付</text>
        <text x="100" y="510" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 产能保障支撑业绩持续增长</text>
        <text x="580" y="390" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">产能</text>
    </g>
    
    <!-- 战略 4 -->
    <g filter="url(#shadow)">
        <rect x="660" y="360" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="360" width="8" height="180" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">资本运作</text>
        <text x="700" y="435" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 全年分红 + 回购 410 亿美元</text>
        <text x="700" y="460" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 研发投入超 250 亿美元</text>
        <text x="700" y="485" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 保持技术领先地位</text>
        <text x="700" y="510" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 股东回报与长期发展并重</text>
        <text x="1180" y="390" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" opacity="0.1">资本</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 10)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "10_strategy.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_cashflow():
    """第 11 页：现金流与股东回报"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        现金流与股东回报
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 核心数据卡片 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="280" height="140" rx="12" fill="{NVIDIA_GREEN}" opacity="0.1"/>
        <text x="200" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">经营现金流</text>
        <text x="200" y="225" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">1027.18 亿</text>
        <text x="200" y="255" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">同比 +60.3%</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="380" y="140" width="280" height="140" rx="12" fill="{NVIDIA_GREEN}" opacity="0.1"/>
        <text x="520" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">自由现金流</text>
        <text x="520" y="225" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">970.00 亿</text>
        <text x="520" y="255" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">同比 +65.8%</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="700" y="140" width="280" height="140" rx="12" fill="{NVIDIA_GREEN}" opacity="0.1"/>
        <text x="840" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">现金及有价证券</text>
        <text x="840" y="225" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">625.56 亿</text>
        <text x="840" y="255" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">总资产 85.3% 增长</text>
    </g>
    
    <!-- 股东回报 -->
    <text x="60" y="340" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">股东回报（全年分红 + 回购）</text>
    
    <rect x="60" y="370" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    <text x="340" y="420" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">410 亿美元</text>
    <text x="340" y="460" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">占自由现金流 43%</text>
    <text x="340" y="490" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">持续高比例回报股东</text>
    
    <!-- 现金流用途 -->
    <text x="660" y="340" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">现金流用途分布</text>
    
    <rect x="660" y="370" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
    
    <!-- 用途条形图 -->
    <rect x="700" y="410" width="400" height="30" rx="4" fill="#F0F0F0"/>
    <rect x="700" y="410" width="172" height="30" rx="4" fill="{NVIDIA_GREEN}"/>
    <text x="680" y="430" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="end">股东回报 43%</text>
    
    <rect x="700" y="450" width="400" height="30" rx="4" fill="#F0F0F0"/>
    <rect x="700" y="450" width="100" height="30" rx="4" fill="{NVIDIA_GREEN}" opacity="0.8"/>
    <text x="680" y="470" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="end">研发投入 25%</text>
    
    <rect x="700" y="490" width="400" height="30" rx="4" fill="#F0F0F0"/>
    <rect x="700" y="490" width="80" height="30" rx="4" fill="{NVIDIA_GREEN}" opacity="0.6"/>
    <text x="680" y="510" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="end">资本开支 20%</text>
    
    <rect x="700" y="530" width="400" height="30" rx="4" fill="#F0F0F0"/>
    <rect x="700" y="530" width="48" height="30" rx="4" fill="{NVIDIA_GREEN}" opacity="0.4"/>
    <text x="680" y="550" font-family="Arial, Microsoft YaHei" font-size="12" fill="#666666" text-anchor="end">其他 12%</text>
'''
    
    svg = create_svg_footer(svg, 11)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "11_cashflow.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_future_outlook():
    """第 12 页：未来展望与增长驱动"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        未来展望与增长驱动
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 2027 财年 Q1 指引 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="360" height="140" rx="12" fill="{NVIDIA_GREEN}" opacity="0.1"/>
        <text x="240" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">2027 财年 Q1 指引</text>
        <text x="240" y="220" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">780 亿美元</text>
        <text x="240" y="250" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">同比 +85% · 毛利率 75%</text>
    </g>
    
    <!-- 2027 财年预测 -->
    <g filter="url(#shadow)">
        <rect x="460" y="140" width="360" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <text x="640" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">2027 财年总营收预测</text>
        <text x="640" y="220" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">3600-3800 亿</text>
        <text x="640" y="250" font-family="Arial, Microsoft YaHei" font-size="13" fill="#5FA000" text-anchor="middle">同比 +67%~76%</text>
    </g>
    
    <!-- 2028 财年预测 -->
    <g filter="url(#shadow)">
        <rect x="860" y="140" width="360" height="140" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <text x="1040" y="180" font-family="Arial, Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">2028 财年总营收预测</text>
        <text x="1040" y="220" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{NVIDIA_GREEN}" text-anchor="middle">5000-5300 亿</text>
        <text x="1040" y="250" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666" text-anchor="middle">持续高增长</text>
    </g>
    
    <!-- 核心驱动 -->
    <text x="60" y="340" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">核心增长驱动</text>
    
    <g filter="url(#shadow)">
        <rect x="60" y="370" width="560" height="150" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="370" width="8" height="150" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="410" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">Rubin 平台量产</text>
        <text x="100" y="440" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 下一代 AI 芯片平台</text>
        <text x="100" y="465" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 性能大幅提升，功耗优化</text>
        <text x="100" y="490" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 2027 财年开始贡献收入</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="660" y="370" width="560" height="150" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="370" width="8" height="150" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="410" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">AI 推理市场爆发</text>
        <text x="700" y="440" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 推理需求超过训练需求</text>
        <text x="700" y="465" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 边缘 AI、企业 AI 快速渗透</text>
        <text x="700" y="490" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 市场规模持续扩大</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="60" y="560" width="560" height="100" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="560" width="8" height="100" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="100" y="600" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">云厂商资本开支持续增长</text>
        <text x="100" y="630" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• AWS、微软、谷歌、Meta 持续加大 AI 投入</text>
        <text x="100" y="655" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 长期采购协议保障收入确定性</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="660" y="560" width="560" height="100" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="560" width="8" height="100" rx="4" fill="{NVIDIA_GREEN}"/>
        <text x="700" y="600" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">垂直行业深度渗透</text>
        <text x="700" y="630" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 医疗、制造、金融等行业 AI 化</text>
        <text x="700" y="655" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 从芯片供应商转向算力基础设施提供商</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 12)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "12_future_outlook.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_risks():
    """第 13 页：风险与挑战"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        风险与挑战
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 风险 1 -->
    <g filter="url(#shadow)">
        <rect x="60" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="140" width="8" height="180" rx="4" fill="#FF6B6B"/>
        <text x="100" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">行业竞争加剧</text>
        <text x="100" y="220" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• AMD MI300 系列竞争力增强</text>
        <text x="100" y="245" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 谷歌 TPU、英特尔 Gaudi 自研芯片</text>
        <text x="100" y="270" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 中国华为昇腾等国产替代加速</text>
        <text x="100" y="295" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 可能影响市场份额和定价能力</text>
        <text x="580" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#FF6B6B" opacity="0.1">竞争</text>
    </g>
    
    <!-- 风险 2 -->
    <g filter="url(#shadow)">
        <rect x="660" y="140" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="140" width="8" height="180" rx="4" fill="#FF6B6B"/>
        <text x="700" y="180" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">美国对华出口管制</text>
        <text x="700" y="220" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 持续限制高端 AI 芯片出口中国</text>
        <text x="700" y="245" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 影响中国区收入（历史占比 20-25%）</text>
        <text x="700" y="270" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 特供版芯片性能受限</text>
        <text x="700" y="295" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 政策不确定性持续存在</text>
        <text x="1180" y="170" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#FF6B6B" opacity="0.1">监管</text>
    </g>
    
    <!-- 风险 3 -->
    <g filter="url(#shadow)">
        <rect x="60" y="360" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="360" width="8" height="180" rx="4" fill="#FFA500"/>
        <text x="100" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">AI 需求波动</text>
        <text x="100" y="440" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• AI 投资热潮可能放缓</text>
        <text x="100" y="465" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 云厂商资本开支周期性波动</text>
        <text x="100" y="490" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 企业 AI 应用落地速度不确定</text>
        <text x="100" y="515" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 可能影响短期业绩增速</text>
        <text x="580" y="390" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#FFA500" opacity="0.1">需求</text>
    </g>
    
    <!-- 风险 4 -->
    <g filter="url(#shadow)">
        <rect x="660" y="360" width="560" height="180" rx="12" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="360" width="8" height="180" rx="4" fill="#FFA500"/>
        <text x="700" y="400" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">供应链与产能瓶颈</text>
        <text x="700" y="440" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 依赖台积电先进制程产能</text>
        <text x="700" y="465" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• CoWoS 封装产能紧张</text>
        <text x="700" y="490" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 地缘政治风险影响供应链稳定</text>
        <text x="700" y="515" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">• 可能制约交付能力</text>
        <text x="1180" y="390" font-family="Arial Black, Microsoft YaHei" font-size="48" font-weight="bold" fill="#FFA500" opacity="0.1">供应链</text>
    </g>
'''
    
    svg = create_svg_footer(svg, 13)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "13_risks.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def generate_summary():
    """第 14 页：总结"""
    svg = create_svg_header()
    
    svg += f'''
    <!-- 标题 -->
    <text x="60" y="80" font-family="Arial Black, Microsoft YaHei" font-size="32" font-weight="bold" fill="{TECH_BLACK}">
        总结：AI 算力王者
    </text>
    <rect x="60" y="95" width="120" height="4" rx="2" fill="{NVIDIA_GREEN}"/>
    
    <!-- 核心总结 -->
    <rect x="60" y="140" width="1160" height="200" rx="12" fill="{NVIDIA_GREEN}" opacity="0.1"/>
    <text x="640" y="190" font-family="Arial Black, Microsoft YaHei" font-size="24" font-weight="bold" fill="{TECH_BLACK}" text-anchor="middle">
        英伟达 2026 财年是 AI 算力时代的巅峰业绩年
    </text>
    <text x="640" y="230" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
        业绩、利润、毛利率全面创历史新高 · 数据中心业务形成绝对统治力
    </text>
    <text x="640" y="265" font-family="Arial, Microsoft YaHei" font-size="16" fill="#666666" text-anchor="middle">
        现金流充沛 · 增长韧性极强 · 行业龙头地位短期难以撼动
    </text>
    
    <!-- 关键要点 -->
    <text x="60" y="390" font-family="Arial Black, Microsoft YaHei" font-size="18" font-weight="bold" fill="{TECH_BLACK}">关键要点</text>
    
    <g filter="url(#shadow)">
        <rect x="60" y="420" width="560" height="120" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="60" y="420" width="6" height="120" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="90" y="455" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">短期展望</text>
        <text x="90" y="485" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">Rubin 平台将开启新一轮高增长</text>
        <text x="90" y="510" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">2027 财年 Q1 指引 780 亿美元（+85%）</text>
    </g>
    
    <g filter="url(#shadow)">
        <rect x="660" y="420" width="560" height="120" rx="8" fill="#FFFFFF" stroke="#E8EAED" stroke-width="1"/>
        <rect x="660" y="420" width="6" height="120" rx="3" fill="{NVIDIA_GREEN}"/>
        <text x="690" y="455" font-family="Arial Black, Microsoft YaHei" font-size="16" font-weight="bold" fill="{TECH_BLACK}">中长期定位</text>
        <text x="690" y="485" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">将成为全球 AI 算力核心基础设施提供商</text>
        <text x="690" y="510" font-family="Arial, Microsoft YaHei" font-size="13" fill="#666666">从芯片供应商转型为平台型公司</text>
    </g>
    
    <!-- 底部装饰 -->
    <rect x="60" y="580" width="1160" height="80" rx="8" fill="#F8F9FA" stroke="#E8EAED" stroke-width="1"/>
    <text x="640" y="620" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999" text-anchor="middle">
        虽然面临监管与竞争压力，但英伟达在 AI 算力领域的领导地位依然稳固
    </text>
    <text x="640" y="645" font-family="Arial, Microsoft YaHei" font-size="14" fill="#999999" text-anchor="middle">
        技术创新 + 生态优势 + 产能保障 = 持续增长的确定性
    </text>
'''
    
    svg = create_svg_footer(svg, 14)
    
    filepath = os.path.join(SVG_OUTPUT_DIR, "14_summary.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated: {filepath}")

def main():
    """生成所有 SVG 文件"""
    os.makedirs(SVG_OUTPUT_DIR, exist_ok=True)
    
    print("开始生成英伟达 2026 财年财报 PPT SVG 文件...")
    print(f"输出目录：{SVG_OUTPUT_DIR}")
    print()
    
    generate_cover()
    generate_financial_overview()
    generate_performance_features()
    generate_datacenter_business()
    generate_gaming_business()
    generate_other_business()
    generate_business_comparison()
    generate_quarterly_data()
    generate_quarterly_features()
    generate_strategy()
    generate_cashflow()
    generate_future_outlook()
    generate_risks()
    generate_summary()
    
    print()
    print("✅ 所有 SVG 文件生成完成！")
    print(f"共生成 14 个文件到：{SVG_OUTPUT_DIR}")

if __name__ == "__main__":
    main()
