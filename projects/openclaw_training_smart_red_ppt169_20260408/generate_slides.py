#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 读取模板文件
def read_template(template_name):
    template_path = f"/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/openclaw_training_smart_red_ppt169_20260408/templates/{template_name}"
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

# 读取培训内容
def read_content():
    content_path = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/openclaw_training_smart_red_ppt169_20260408/sources/training_content.md"
    with open(content_path, 'r', encoding='utf-8') as f:
        return f.read()

# 提取特定章节的内容
def extract_section(content, section_title):
    # 找到章节开始
    start_pattern = f"## {section_title}"
    start_idx = content.find(start_pattern)
    if start_idx == -1:
        return ""
    
    # 找到下一个章节开始或文件结束
    next_section_patterns = ["## ", "### ", "---", "## Q&A", "## 谢谢！"]
    end_idx = len(content)
    
    for pattern in next_section_patterns:
        next_idx = content.find(pattern, start_idx + len(start_pattern))
        if next_idx != -1 and next_idx < end_idx:
            end_idx = next_idx
    
    return content[start_idx:end_idx].strip()

# 生成封面页
def generate_cover():
    template = read_template("01_cover.svg")
    template = template.replace("{{TITLE}}", "OpenClaw 内部培训材料")
    template = template.replace("{{SUBTITLE}}", "从原理到实践，掌握 AI Agent 操作系统")
    template = template.replace("{{AUTHOR}}", "Vincent")
    template = template.replace("{{DATE}}", "2026 年 4 月 9 日")
    return template

# 生成目录页
def generate_toc():
    template = read_template("02_toc.svg")
    # 替换 TOC 内容
    toc_content = """<text x="100" y="150" font-family="'Microsoft YaHei', 'SimHei', sans-serif" font-size="28" fill="#333333">1. 原理篇：OpenClaw 技术基础</text>
<text x="100" y="200" font-family="'Microsoft YaHei', 'SimHei', sans-serif" font-size="28" fill="#333333">2. 实践篇 1：第一个 Cron 定时任务</text>
<text x="100" y="250" font-family="'Microsoft YaHei', 'SimHei', sans-serif" font-size="28" fill="#333333">3. 实践篇 2：第一个技能开发</text>
<text x="100" y="300" font-family="'Microsoft YaHei', 'SimHei', sans-serif" font-size="28" fill="#333333">4. 实践篇 3：Multi-Agent 体系开发</text>
<text x="100" y="350" font-family="'Microsoft YaHei', 'SimHei', sans-serif" font-size="28" fill="#333333">5. Q&A 与实战演示</text>"""
    
    # 在模板中找到合适的位置插入内容
    content_area_start = template.find('<g transform="translate(')
    if content_area_start != -1:
        # 找到 content area 的结束标签
        content_area_end = template.find('</g>', content_area_start)
        if content_area_end != -1:
            before = template[:content_area_start]
            after = template[content_area_end:]
            new_content = '<g transform="translate(100, 100)">\n' + toc_content + '\n</g>'
            return before + new_content + after
    
    return template

# 生成章节页
def generate_chapter(title):
    template = read_template("02_chapter.svg")
    # 替换章节标题
    template = re.sub(r'<text[^>]*>{{CHAPTER_TITLE}}</text>', 
                     f'<text x="100" y="200" font-family="\'Microsoft YaHei\', \'SimHei\', sans-serif" font-size="40" fill="#DE3545" font-weight="bold">{title}</text>', 
                     template)
    return template

# 生成内容页
def generate_content(title, content_text):
    template = read_template("03_content.svg")
    
    # 处理内容文本，限制在6个bullet points以内
    lines = content_text.split('\n')
    bullet_points = []
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            bullet_points.append(line.strip()[2:].strip())
            if len(bullet_points) >= 6:
                break
    
    # 构建内容
    content_lines = [f'<text x="50" y="{150 + i*40}" font-family="\'Microsoft YaHei\', \'SimHei\', sans-serif" font-size="20" fill="#333333">• {point}</text>' 
                    for i, point in enumerate(bullet_points)]
    
    content_xml = '\n'.join(content_lines)
    
    # 替换标题和内容
    template = re.sub(r'<text[^>]*>{{PAGE_TITLE}}</text>', 
                     f'<text x="50" y="80" font-family="\'Microsoft YaHei\', \'SimHei\', sans-serif" font-size="32" font-weight="bold" fill="#333333">{title}</text>', 
                     template)
    
    # 插入内容
    content_area_start = template.find('<!-- Content Area -->')
    if content_area_start != -1:
        insert_pos = content_area_start + len('<!-- Content Area -->')
        template = template[:insert_pos] + '\n' + content_xml + template[insert_pos:]
    
    return template

# 主函数
def main():
    output_dir = "/home/Vincent/.openclaw/workspace/skills/ppt-master/projects/openclaw_training_smart_red_ppt169_20260408/svg_final"
    os.makedirs(output_dir, exist_ok=True)
    
    content = read_content()
    
    # 生成25页
    slides = []
    
    # 1. 封面
    slides.append(("01_cover.svg", generate_cover()))
    
    # 2. 目录
    slides.append(("02_toc.svg", generate_toc()))
    
    # 3. 1.1 OpenClaw 介绍
    section_1_1 = extract_section(content, "1.1 OpenClaw 介绍")
    slides.append(("03_content.svg", generate_content("1.1 OpenClaw 介绍", section_1_1)))
    
    # 4. 1.2 技术架构
    section_1_2 = extract_section(content, "1.2 技术架构")
    slides.append(("04_content.svg", generate_content("1.2 技术架构", section_1_2)))
    
    # 5. 1.3 信息架构
    section_1_3 = extract_section(content, "1.3 信息架构")
    slides.append(("05_content.svg", generate_content("1.3 信息架构", section_1_3)))
    
    # 6. 1.4 记忆架构
    section_1_4 = extract_section(content, "1.4 记忆架构")
    slides.append(("06_content.svg", generate_content("1.4 记忆架构", section_1_4)))
    
    # 7. 1.5 技能架构
    section_1_5 = extract_section(content, "1.5 技能架构")
    slides.append(("07_content.svg", generate_content("1.5 技能架构", section_1_5)))
    
    # 8. 1.6 SubAgent 架构
    section_1_6 = extract_section(content, "1.6 SubAgent 架构")
    slides.append(("08_content.svg", generate_content("1.6 SubAgent 架构", section_1_6)))
    
    # 9. 1.7 Cron 任务原理
    section_1_7 = extract_section(content, "1.7 Cron 任务原理")
    slides.append(("09_content.svg", generate_content("1.7 Cron 任务原理", section_1_7)))
    
    # 10. 2.1 第一个 Cron 任务：关键要素
    section_2_1 = extract_section(content, "2.1 第一个 Cron 任务：关键要素")
    slides.append(("10_content.svg", generate_content("2.1 第一个 Cron 任务：关键要素", section_2_1)))
    
    # 11. 2.2 实战案例：国际形势日报
    section_2_2 = extract_section(content, "2.2 实战案例：国际形势日报")
    slides.append(("11_content.svg", generate_content("2.2 实战案例：国际形势日报", section_2_2)))
    
    # 12. 2.3 执行数据与复盘
    section_2_3 = extract_section(content, "2.3 执行数据与复盘")
    slides.append(("12_content.svg", generate_content("2.3 执行数据与复盘", section_2_3)))
    
    # 13. 章节页 - 3.1 第一个技能开发：关键要素
    slides.append(("13_chapter.svg", generate_chapter("第一个技能开发")))
    
    # 14. 3.1 第一个技能开发：关键要素
    section_3_1 = extract_section(content, "3.1 第一个技能开发：关键要素")
    slides.append(("14_content.svg", generate_content("3.1 第一个技能开发：关键要素", section_3_1)))
    
    # 15. 3.2 实战案例：PPT-Master 技能
    section_3_2 = extract_section(content, "3.2 实战案例：PPT-Master 技能")
    slides.append(("15_content.svg", generate_content("3.2 实战案例：PPT-Master 技能", section_3_2)))
    
    # 16. 3.3 技能开发 5 大坑
    section_3_3 = extract_section(content, "3.3 技能开发 5 大坑")
    slides.append(("16_content.svg", generate_content("3.3 技能开发 5 大坑", section_3_3)))
    
    # 17. 章节页 - 4.1 Multi-Agent 关键要素
    slides.append(("17_chapter.svg", generate_chapter("Multi-Agent 体系开发")))
    
    # 18. 4.1 Multi-Agent 关键要素
    section_4_1 = extract_section(content, "4.1 Multi-Agent 关键要素")
    slides.append(("18_content.svg", generate_content("4.1 Multi-Agent 关键要素", section_4_1)))
    
    # 19. 4.2 实战案例：任务路由
    section_4_2 = extract_section(content, "4.2 实战案例：任务路由")
    slides.append(("19_content.svg", generate_content("4.2 实战案例：任务路由", section_4_2)))
    
    # 20. 4.3 通信问题与解决方案
    section_4_3 = extract_section(content, "4.3 通信问题与解决方案")
    slides.append(("20_content.svg", generate_content("4.3 通信问题与解决方案", section_4_3)))
    
    # 21. 4.4 协同问题与解决方案
    section_4_4 = extract_section(content, "4.4 协同问题与解决方案")
    slides.append(("21_content.svg", generate_content("4.4 协同问题与解决方案", section_4_4)))
    
    # 22. 4.5 任务监控系统
    section_4_5 = extract_section(content, "4.5 任务监控系统")
    slides.append(("22_content.svg", generate_content("4.5 任务监控系统", section_4_5)))
    
    # 23. 4.6 超时规则
    section_4_6 = extract_section(content, "4.6 超时规则")
    slides.append(("23_content.svg", generate_content("4.6 超时规则", section_4_6)))
    
    # 24. 4.7 Multi-Agent 开发检查清单
    section_4_7 = extract_section(content, "4.7 Multi-Agent 开发检查清单")
    slides.append(("24_content.svg", generate_content("4.7 Multi-Agent 开发检查清单", section_4_7)))
    
    # 25. 结束页
    template = read_template("04_ending.svg")
    template = template.replace("{{THANKS_TEXT}}", "谢谢！")
    template = template.replace("{{CONTACT_INFO}}", "演讲者：Vincent\n日期：2026 年 4 月 9 日\n版本：v1.0")
    slides.append(("25_ending.svg", template))
    
    # 保存所有幻灯片
    for i, (filename, content) in enumerate(slides, 1):
        filepath = os.path.join(output_dir, f"{str(i).zfill(2)}_{filename.split('_')[1]}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated slide {i}: {filepath}")

if __name__ == "__main__":
    main()