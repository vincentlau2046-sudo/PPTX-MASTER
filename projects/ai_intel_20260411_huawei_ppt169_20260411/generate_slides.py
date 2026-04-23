#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 AI 情报日报 2026-04-11 的 SVG 文件
共 18 页，使用华为技术模板
"""

import os
import re

PROJECT_DIR = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/ai_intel_20260411_huawei_ppt169_20260411"
SOURCES_DIR = os.path.join(PROJECT_DIR, "sources")
SVG_OUTPUT_DIR = os.path.join(PROJECT_DIR, "svg_output")
SVG_FINAL_DIR = os.path.join(PROJECT_DIR, "svg_final")

# 华为红
HUAWEI_RED = "#E60012"
TECH_BLACK = "#191919"
MEDIUM_GRAY = "#595959"
LIGHT_GRAY = "#F5F5F5"
WHITE = "#FFFFFF"

def create_svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
    <defs>
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F8F9FA;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="url(#bgGradient)"/>
'''

def create_svg_footer(svg_content, page_num, total_pages=18):
    svg_content += f'''
    <rect x="0" y="680" width="1280" height="40" fill="#F0F0F0" opacity="0.5"/>
    <text x="60" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999">
        AI 每日洞察报告 | 2026-04-11
    </text>
    <text x="1220" y="705" font-family="Arial, Microsoft YaHei" font-size="12" fill="#999999" text-anchor="end">
        {page_num} / {total_pages}
    </text>
</svg>'''
    return svg_content

def parse_md_content(md_file):
    """解析 MD 文件，提取每页内容"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按 ## 分割章节
    sections = re.split(r'\n##\s+', content)
    pages = []
    
    for section in sections:
        if section.strip():
            lines = section.strip().split('\n')
            title = lines[0].strip() if lines else ""
            body = '\n'.join(lines[1:]) if len(lines) > 1 else ""
            pages.append({'title': title, 'body': body})
    
    return pages

def generate_cover(page_data):
    """第 1 页：封面"""
    svg = create_svg_header()
    svg += f'''
    <rect x="0" y="0" width="1280" height="200" fill="url(#linearGradient)"/>
    <rect x="0" y="0" width="1280" height="200" fill="{HUAWEI_RED}" opacity="0.9"/>
    
    <text x="640" y="90" font-family="Arial Black, Microsoft YaHei" font-size="40" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
        AI 每日洞察报告
    </text>
    
    <text x="640" y="140" font-family="Arial, Microsoft YaHei" font-size="20" fill="#FFE0E0" text-anchor="middle">
        2026 年 4 月 11 日 | 全球 AI 前沿动态
    </text>
    
    <rect x="440" y="220" width="400" height="4" rx="2" fill="{HUAWEI_RED}"/>
    
    <text x="640" y="300" font-family="Arial, Microsoft YaHei" font-size="24" fill="{TECH_BLACK}" text-anchor="middle">
        大模型竞赛 · AI 监管框架 · 多模态突破
    </text>
    
    <text x="640" y="350" font-family="Arial, Microsoft YaHei" font-size="16" fill="{MEDIUM_GRAY}" text-anchor="middle">
        零壹情报每日更新
    </text>
'''
    return create_svg_footer(svg, 1)

def generate_content_page(page_num, page_data, total_pages=18):
    """生成内容页"""
    svg = create_svg_header()
    
    # 页眉
    svg += f'''
    <rect x="0" y="0" width="1280" height="60" fill="#F8F9FA"/>
    <rect x="0" y="55" width="1280" height="5" fill="{HUAWEI_RED}"/>
    <text x="60" y="38" font-family="Arial, Microsoft YaHei" font-size="18" fill="{TECH_BLACK}" font-weight="bold">
        {page_data['title'][:50]}
    </text>
'''
    
    # 内容区域
    body_lines = page_data['body'].split('\n')[:8]  # 限制行数
    y_pos = 120
    
    for line in body_lines:
        line = line.strip()
        if line and not line.startswith('**要点**') and not line.startswith('**时长**'):
            # 清理 markdown
            line = re.sub(r'\*\*|\*|`', '', line)
            line = re.sub(r'^[①②③④⑤].*$', '', line)
            
            if line.strip():
                svg += f'''
    <text x="60" y="{y_pos}" font-family="Arial, Microsoft YaHei" font-size="16" fill="{MEDIUM_GRAY}">
        {line[:80]}
    </text>
'''
                y_pos += 35
    
    return create_svg_footer(svg, page_num, total_pages)

def generate_ending():
    """第 18 页：结束页"""
    svg = create_svg_header()
    svg += f'''
    <text x="640" y="300" font-family="Arial Black, Microsoft YaHei" font-size="36" font-weight="bold" fill="{TECH_BLACK}" text-anchor="middle">
        感谢聆听
    </text>
    
    <text x="640" y="350" font-family="Arial, Microsoft YaHei" font-size="18" fill="{MEDIUM_GRAY}" text-anchor="middle">
        明日更新：2026 年 4 月 12 日上午 7 点
    </text>
    
    <rect x="440" y="400" width="400" height="4" rx="2" fill="{HUAWEI_RED}"/>
'''
    return create_svg_footer(svg, 18)

def main():
    os.makedirs(SVG_OUTPUT_DIR, exist_ok=True)
    os.makedirs(SVG_FINAL_DIR, exist_ok=True)
    
    md_file = os.path.join(SOURCES_DIR, "daily_ai_intel_2026-04-11.md")
    pages = parse_md_content(md_file)
    
    print(f"解析到 {len(pages)} 个章节")
    
    for i, page in enumerate(pages):
        if i == 0:
            svg_content = generate_cover(page)
        elif i == len(pages) - 1:
            svg_content = generate_ending()
        else:
            svg_content = generate_content_page(i + 1, page)
        
        # 保存到 svg_output
        output_file = os.path.join(SVG_OUTPUT_DIR, f"{i+1:02d}_page.svg")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        # 复制到 svg_final
        final_file = os.path.join(SVG_FINAL_DIR, f"{i+1:02d}_page.svg")
        with open(final_file, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✓ 生成第 {i+1} 页：{output_file}")
    
    print(f"\n✅ 完成！共生成 {len(pages)} 页 SVG")

if __name__ == "__main__":
    main()
