# OpenClaw 内部培训材料

**培训日期**: 2026 年 4 月 9 日  
**培训对象**: 部门内部技术团队  
**培训目标**: 掌握 OpenClaw 核心架构原理，具备独立开发 Cron 任务、技能和 Multi-Agent 体系的能力

---

## 目录

1. [原理篇：OpenClaw 技术基础](#1-原理篇 openclaw 技术基础)
   - 1.1 OpenClaw 介绍
   - 1.2 技术架构
   - 1.3 信息架构
   - 1.4 记忆架构
   - 1.5 技能架构
   - 1.6 SubAgent 架构
   - 1.7 Cron 任务（HeartBeat）原理

2. [实践篇：第一个 OpenClaw 定时任务](#2-实践篇第一个 openclaw 定时任务)
   - 2.1 关键要素
   - 2.2 实战案例：国际形势日报 Cron
   - 2.3 复盘与避坑指南

3. [实践篇：第一个 OpenClaw 技能开发](#3-实践篇第一个 openclaw 技能开发)
   - 3.1 关键要素
   - 3.2 实战案例：PPT-Master 技能
   - 3.3 常见坑与避坑方案

4. [实践篇：Multi-Agent 体系开发](#4-实践篇 multi-agent 体系开发)
   - 4.1 关键要素
   - 4.2 实战案例：当前 Multi-Agent 体系
   - 4.3 通信问题与解决方案
   - 4.4 协同问题与解决方案
   - 4.5 任务监控问题与解决方案

---

## 1. 原理篇：OpenClaw 技术基础

### 1.1 OpenClaw 介绍

**OpenClaw 是什么？**

OpenClaw 是一个 AI Agent 操作系统，提供：
- **会话管理**: 主会话、子会话、隔离会话
- **任务调度**: Cron 定时任务、Heartbeat 心跳机制
- **技能系统**: 可扩展的技能开发和执行框架
- **Multi-Agent**: 多 Agent 协同工作体系
- **记忆系统**: 短期记忆、长期记忆、自我改进记忆

**核心价值**:
- 让 AI 从"聊天机器人"变成"自主执行者"
- 支持复杂任务的自动化和持续化
- 提供企业级任务监控和质量保障

---

### 1.2 技术架构

```
┌─────────────────────────────────────────────────────────┐
│                    OpenClaw Gateway                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Session    │  │    Cron     │  │   Skills    │     │
│  │  Manager    │  │  Scheduler  │  │   Engine    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Memory    │  │   Multi-    │  │   Tools     │     │
│  │   System    │  │   Agent     │  │   Proxy     │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼───────┐  ┌────────▼────────┐  ┌──────▼──────┐
│  Main Agent   │  │  Sub Agents     │  │  External   │
│  (主会话)      │  │  (子会话)        │  │  Tools      │
└───────────────┘  └─────────────────┘  └─────────────┘
```

**核心组件**:

| 组件 | 职责 | 关键配置 |
|------|------|----------|
| Gateway | 核心服务，管理所有组件 | `~/.openclaw/openclaw.json` |
| Session Manager | 会话生命周期管理 | `sessions_spawn`, `sessions_list` |
| Cron Scheduler | 定时任务调度 | `cron add/update/run` |
| Skills Engine | 技能加载和执行 | `skills/<skill-name>/SKILL.md` |
| Memory System | 记忆存储和检索 | `MEMORY.md`, `memory/`, `~/self-improving/` |
| Tools Proxy | 工具调用代理 | `exec`, `message`, `web_search` 等 |

---

### 1.3 信息架构

**OpenClaw 信息流向**:

```
用户输入 → Gateway → Agent → Tools → 外部系统
                                    ↓
                              结果返回 → Agent → Gateway → 用户输出
```

**关键信息类型**:

1. **用户消息**: 通过 channel 插件接收（微信、飞书、Discord 等）
2. **系统事件**: Cron 触发、Heartbeat、内部通知
3. **工具调用**: Agent 调用外部 API、执行命令、读写文件
4. **会话状态**: 任务进度、子 Agent 状态、错误信息

**数据持久化**:

| 数据类型 | 存储位置 | 用途 |
|----------|----------|------|
| 会话历史 | Gateway 内存 + 数据库 | 对话上下文 |
| 长期记忆 | `MEMORY.md` | 用户偏好、重要事件 |
| 每日日志 | `memory/YYYY-MM-DD.md` | 原始执行记录 |
| 自我改进 | `~/self-improving/` | 执行优化规则 |
| 任务状态 | `shared/task_status.md` | Multi-Agent 任务跟踪 |

---

### 1.4 记忆架构

**三层记忆系统**:

```
┌─────────────────────────────────────────┐
│         短期记忆 (Session Context)       │
│  - 当前会话消息历史                       │
│  - 工具调用结果                          │
│  - 临时变量                              │
└─────────────────────────────────────────┘
              ↓ 定期提炼
┌─────────────────────────────────────────┐
│         长期记忆 (MEMORY.md)             │
│  - 用户背景和偏好                        │
│  - 重要决策和事件                        │
│  - 项目上下文                            │
└─────────────────────────────────────────┘
              ↓ 经验固化
┌─────────────────────────────────────────┐
│      自我改进记忆 (~/self-improving/)    │
│  - 执行优化规则 (memory.md)              │
│  - 领域专用知识 (domains/)               │
│  - 项目特定配置 (projects/)              │
│  - 错误和修正 (corrections.md)           │
└─────────────────────────────────────────┘
```

**记忆使用规范**:

```markdown
# 每次会话启动时（主会话）
1. 读取 SOUL.md（人格定义）
2. 读取 USER.md（用户信息）
3. 读取 MEMORY.md（长期记忆）
4. 扫描最近 2 天的 memory/YYYY-MM-DD.md
5. 读取 ~/self-improving/memory.md 和相关的 domains/*.md

# 写入规则
- 事实性事件 → memory/YYYY-MM-DD.md
- 重要决策/洞察 → MEMORY.md
- 执行优化规则 → ~/self-improving/memory.md
- 领域特定知识 → ~/self-improving/domains/<domain>.md
- 用户纠正 → ~/self-improving/corrections.md（立即写入）
```

---

### 1.5 技能架构

**技能定义**:

技能是 OpenClaw 的可扩展功能模块，包含：
- `SKILL.md`: 技能描述、触发规则、执行流程
- `scripts/`: 执行脚本（Shell、Python、Node.js 等）
- `references/`: 参考文档和模板
- `output/`: 技能输出目录（可选）

**技能结构示例**（以 ppt-master 为例）:

```
skills/ppt-master/
├── SKILL.md              # 技能定义（16KB，含完整工作流）
├── scripts/              # 执行脚本
│   ├── project_manager.py    # 项目管理
│   ├── svg_to_pptx.py        # PPTX 导出
│   ├── pdf_to_md.py          # PDF 转换
│   └── README.md             # 脚本说明
├── templates/            # 模板库
│   ├── layouts/              # 页面布局模板
│   ├── charts/               # 图表模板
│   └── icons/                # 图标库
├── workflows/            # 独立工作流
│   └── create-template.md
└── projects/             # 项目输出（运行时生成）
```

**技能触发机制**:

```yaml
# SKILL.md 头部定义
---
name: ppt-master
description: >
  AI-driven multi-format SVG content generation system.
  Use when user asks to "create PPT", "make presentation",
  "生成 PPT", "做 PPT", "制作演示文稿".
---
```

**触发关键词匹配**:
- 精确匹配：技能名称、别名
- 语义匹配：描述中的动词短语
- 上下文匹配：当前任务类型

---

### 1.6 SubAgent 架构

**SubAgent 类型**:

| 类型 | runtime | 用途 | 会话模式 |
|------|---------|------|----------|
| subagent | `subagent` | 通用子任务 | run（单次）/ session（持久） |
| acp | `acp` | ACP  harness 集成 | thread（线程绑定） |

**SubAgent 调用方式**:

```javascript
// 主 Agent 调用子 Agent
sessions_spawn(
  runtime = "subagent",
  agent_id = "tech_analyst",
  task = "【任务 ID: 20260408001】深度分析中国 MaaS 市场",
  mode = "run",  // 或 "session"
  timeoutSeconds = 1800
)
```

**SubAgent 工作空间**:

```
/home/Vincent/.openclaw/
├── workspace/                    # 主工作空间
├── workspace-AI-INTEL/           # ai_intel 专属空间
├── workspace-TECH-ANALYST/       # tech_analyst 专属空间
├── workspace-CONTENT-CREATOR/    # content_creator 专属空间
└── workspace-WORK-PRESENT-OUTPUT/ # work_present_output 专属空间
```

**关键原则**:
1. 子 Agent 继承父工作空间目录
2. 每个 Agent 有独立的工作空间
3. 通过 `task_status.md` 跟踪状态
4. 主 Agent 负责协调和结果汇总

---

### 1.7 Cron 任务（HeartBeat）原理

**Cron 调度机制**:

```
┌─────────────────────────────────────────┐
│         Cron Scheduler                   │
│  ┌─────────────────────────────────┐    │
│  │  Job Queue (13 个任务)            │    │
│  │  - 国际形势日报 (工作日 8:00)     │    │
│  │  - 国际形势日报 PPT+ 视频 (8:30)   │    │
│  │  - 国际形势周报 (周六 10:00)      │    │
│  │  - AI 情报日报 (每天 6:40)        │    │
│  │  - 质量监控日报 (每天 21:00)      │    │
│  │  - ...                           │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
              ↓ 定时触发
┌─────────────────────────────────────────┐
│         Session Target                   │
│  - main: 主会话（systemEvent）          │
│  - isolated: 隔离会话（agentTurn）      │
│  - session:ai_intel: 专属会话           │
└─────────────────────────────────────────┘
```

**Cron Job 结构**:

```json
{
  "id": "a556ee2b-4531-4dad-9d92-5fc754a1d944",
  "name": "国际形势日报（工作日 5 分钟快读）",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * 1-5",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "生成今日国际形势日报...",
    "timeoutSeconds": 1800
  },
  "delivery": {
    "mode": "announce",
    "channel": "feishu",
    "to": "ou_01c7bc2227dc9960a4388a1db7e86ddc"
  }
}
```

**HeartBeat 机制**:

- **定义**: 定期唤醒主 Agent 检查系统状态
- **频率**: 默认每 5 分钟（可配置）
- **用途**: 
  - 检查邮件、日历、通知
  - 执行周期性巡检
  - 触发后台任务

**HeartBeat vs Cron**:

| 特性 | HeartBeat | Cron |
|------|-----------|------|
| 触发方式 | 固定间隔（如 5 分钟） | Cron 表达式（精确时间） |
| 执行会话 | 主会话 | 可选主会话/隔离会话 |
| 用途 | 系统巡检、批量检查 | 定时任务、日报周报 |
| 配置复杂度 | 低 | 中 |

---

## 2. 实践篇：第一个 OpenClaw 定时任务

### 2.1 关键要素

**创建 Cron 任务的 5 个步骤**:

1. **明确任务目标**: 要做什么？输出什么？
2. **设计执行流程**: Agent 需要执行哪些步骤？
3. **配置 Cron Job**: 时间、会话、payload、delivery
4. **测试验证**: 手动触发测试
5. **监控优化**: 观察执行情况，调整参数

**关键配置项**:

| 配置项 | 说明 | 示例 |
|--------|------|------|
| `schedule.kind` | 调度类型 | `cron` / `every` / `at` |
| `schedule.expr` | Cron 表达式 | `0 8 * * 1-5` |
| `sessionTarget` | 执行会话 | `isolated` / `main` / `session:xxx` |
| `payload.kind` | 负载类型 | `agentTurn` / `systemEvent` |
| `payload.message` | 执行指令 | 详细的任务描述 |
| `delivery.mode` | 交付方式 | `announce` / `webhook` / `none` |
| `timeoutSeconds` | 超时时间 | `1800` (30 分钟) |

---

### 2.2 实战案例：国际形势日报 Cron

**任务背景**:
- 需求：每天早上 8 点获取国际形势 5 分钟快读
- 内容：中东局势、俄乌冲突、中美关系、全球市场
- 输出：飞书推送 + Markdown 文档

**Cron 配置**（已部署）:

```json
{
  "id": "a556ee2b-4531-4dad-9d92-5fc754a1d944",
  "name": "国际形势日报（工作日 5 分钟快读）",
  "description": "周一至周五早上 8:00 生成国际形势 5 分钟快读简报并推送到飞书",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * 1-5",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "生成今日国际形势日报（工作日 5 分钟快读版），严格按照以下模板：\n\n【模板结构】\n1. 【头条・深度解析】（1-2 条，事件 + 影响 + 风险）\n2. 【区域要闻】\n   - 亚太（3-4 条）\n   - 欧洲（2-3 条）\n   - 中东/美洲（2-3 条）\n3. 【全球市场】（表格格式）\n4. 【简讯速读】（5-8 条，一句话）\n5. 【今日看点】（明日预判表格）\n\n【搜索要求】\n使用 Tavily 搜索 7 个主题...\n\n【输出】\n1. 保存到 /home/Vincent/.openclaw/workspace/wechat_articles/world_intel_brief/daily_brief_YYYY-MM-DD.md\n2. 发送飞书通知",
    "timeoutSeconds": 1800
  },
  "delivery": {
    "mode": "announce",
    "channel": "feishu",
    "to": "ou_01c7bc2227dc9960a4388a1db7e86ddc"
  }
}
```

**执行流程**:

```
[08:00] Cron 触发
    ↓
[08:00] isolated session 启动
    ↓
[08:00] Agent 执行：
    1. Tavily 搜索 7 个主题（中东、俄乌、中美、油价等）
    2. 整理新闻（每条 3-5 条结果）
    3. 生成 Markdown（1500-2000 字）
    4. 保存到指定路径
    5. 发送飞书通知
    ↓
[08:02] 任务完成（耗时约 2 分钟）
    ↓
[08:02] 飞书推送：
    🌍 国际形势日报 | 2026-04-09
    - 美伊停火谈判僵局
    - 俄乌能源互袭升级
    - 亚太军事联动
    ⏱️ 阅读耗时：约 5 分钟
```

**输出示例**（2026-04-08）:

```markdown
# 🌍 国际形势日报 | 2026 年 4 月 8 日（周三）

**阅读耗时**: 约 5 分钟 | **字数**: 约 1800 字

---

## 一、【头条・深度解析】

### 1. 美伊停火谈判陷入僵局，霍尔木兹海峡持续关闭 🔴

**事件**: 美国和伊朗在巴基斯坦、埃及、土耳其斡旋下讨论 45 天停火协议，但双方立场"差距过大，难以缩小"。

**影响**: 
- 霍尔木兹海峡自 2 月底关闭，全球每日减少约 1200-1500 万桶石油供应
- OPEC+ 虽同意 4 月起每日增产 20.6 万桶，但实际无法实施

**风险信号**: 🔴 **高危**

---

## 二、【区域要闻】
...
```

---

### 2.3 复盘与避坑指南

**实际执行数据**（2026-04-08 测试）:

| 指标 | 数值 |
|------|------|
| 启动时间 | 19:02 |
| 完成时间 | 19:04 |
| 总耗时 | 124 秒 |
| 输出字数 | 1800 字 |
| 搜索主题 | 7 个 |
| 飞书推送 | ✅ 成功 |

**遇到的坑**:

#### 坑 1: 输出目录不一致
- **问题**: 最初配置输出到 `WORK/wechat_articles/`，后来改为 `wechat_articles/`
- **影响**: Cron 任务读取路径错误，找不到输入文件
- **解决**: 统一修改所有 Cron 任务的输出路径配置
- **教训**: 路径配置要集中管理，避免硬编码

#### 坑 2: 搜索超时
- **问题**: Tavily 搜索 7 个主题，偶尔超时
- **影响**: 任务失败，无输出
- **解决**: 
  - 增加 timeout 到 1800 秒
  - 搜索并行化（同时发起 7 个搜索请求）
- **教训**: 外部 API 调用要设置合理的超时和重试

#### 坑 3: 飞书推送失败
- **问题**: 某些时段飞书 API 返回 401 错误
- **影响**: 任务成功但用户未收到通知
- **解决**: 
  - 检查飞书 token 有效期
  - 添加失败重试逻辑
- **教训**: 推送失败要有降级方案（如邮件备用）

**最佳实践**:

1. **路径配置集中化**:
   ```bash
   # 在 openclaw.json 中定义全局路径
   {
     "workspace": {
       "output": "/home/Vincent/.openclaw/workspace/wechat_articles"
     }
   }
   ```

2. **错误处理标准化**:
   ```javascript
   // Cron payload 中包含错误处理指令
   "payload": {
     "message": "... 如果文件不存在，输出错误信息并退出 ...",
     "timeoutSeconds": 1800
   }
   ```

3. **监控和日志**:
   ```bash
   # 查看 Cron 执行历史
   cron runs --jobId <job_id>
   
   # 查看任务状态
   cat /home/Vincent/.openclaw/workspace/shared/task_status.md
   ```

---

## 3. 实践篇：第一个 OpenClaw 技能开发

### 3.1 关键要素

**技能开发流程**:

```
1. 需求分析 → 2. 设计结构 → 3. 编写代码 → 4. 测试验证 → 5. 文档编写 → 6. 发布部署
```

**技能文件结构**:

```
skills/<skill-name>/
├── SKILL.md              # 必须：技能定义
├── scripts/              # 必须：执行脚本
│   └── <script>.py/.sh/.js
├── references/           # 可选：参考文档
├── templates/            # 可选：模板文件
├── output/               # 可选：输出目录
├── package.json          # 可选：Node.js 依赖
└── README.md             # 推荐：版本记录
```

**SKILL.md 核心结构**:

```markdown
---
name: <skill-id>
description: >
  技能描述，包含触发关键词
---

# <Skill Name> Skill

## 触发规则
- 关键词匹配
- 上下文匹配

## 执行流程
1. 步骤 1
2. 步骤 2
...

## 工具调用
- exec: 执行命令
- write: 写文件
- message: 发送消息
```

---

### 3.2 实战案例：PPT-Master 技能

**技能背景**:
- 需求：将 Markdown/PDF/DOCX转换为专业PPTX
- 核心功能：SVG 生成、多模板支持、PPTX 导出
- 开发周期：2 周（含测试和优化）

**技能结构**:

```
skills/ppt-master/
├── SKILL.md              # 16KB，完整工作流定义
├── scripts/
│   ├── project_manager.py    # 项目管理（初始化、验证）
│   ├── svg_to_pptx.py        # PPTX 导出（核心）
│   ├── pdf_to_md.py          # PDF 转换
│   ├── doc_to_md.py          # DOCX 转换
│   ├── web_to_md.py          # 网页转换
│   ├── image_gen.py          # AI 图像生成
│   ├── svg_quality_checker.py # 质量检查
│   └── README.md
├── templates/
│   ├── layouts/              # 16:9、4:3布局模板
│   ├── charts/               # KPI、柱状图、矩阵等
│   └── icons/                # 图标库
├── workflows/
│   └── create-template.md    # 模板创建工作流
└── projects/                 # 运行时生成
```

**核心工作流**（简化版）:

```
1. 源内容处理（PDF/DOCX→MD）
   ↓
2. 项目初始化（创建目录结构）
   ↓
3. 设计规范（Eight Confirmations）⛔ BLOCKING
   ↓ 【用户确认】
4. SVG 生成（逐页生成）
   ↓
5. 质量检查
   ↓
6. PPTX 导出（原生 + 兼容双格式）
   ↓
7. 交付
```

**关键脚本**（svg_to_pptx.py 片段）:

```python
#!/usr/bin/env python3
"""
SVG to PPTX Exporter
将 SVG 页面导出为可编辑的 PowerPoint 文件
"""

import sys
from pptx import Presentation
from pptx.util import Inches

def export_svg_to_pptx(svg_dir, output_path):
    prs = Presentation()
    
    # 遍历 SVG 文件
    for svg_file in sorted(os.listdir(svg_dir)):
        if svg_file.endswith('.svg'):
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            # 添加 SVG 为原生形状（非图片）
            # ...
    
    prs.save(output_path)
    print(f"✅ PPTX 已导出：{output_path}")

if __name__ == "__main__":
    project_dir = sys.argv[1]
    export_svg_to_pptx(f"{project_dir}/svg_final", f"{project_dir}/output.pptx")
```

**执行示例**:

```bash
# 1. 项目初始化
python3 scripts/project_manager.py init world_intel_20260408 --format ppt169

# 2. 导入源文件
python3 scripts/project_manager.py import-sources <project_dir> daily_brief_2026-04-08.md --move

# 3. 导出 PPTX
python3 scripts/svg_to_pptx.py <project_dir> -s final

# 输出:
# ✅ PPTX 已导出：<project_dir>/world_intel_brief_2026-04-08.pptx
# ✅ 兼容版已导出：<project_dir>/world_intel_brief_2026-04-08_compatible.pptx
```

---

### 3.3 常见坑与避坑方案

#### 坑 1: 技能触发失败
- **现象**: 用户说"生成 PPT"，技能不响应
- **原因**: SKILL.md 的 description 中关键词不全
- **解决**:
  ```markdown
  ---
  description: >
    Use when user asks to "create PPT", "make presentation",
    "生成 PPT", "做 PPT", "制作演示文稿", or mentions "ppt-master".
  ---
  ```
- **教训**: 关键词要覆盖中英文、口语化表达

#### 坑 2: 跨阶段执行（最严重）
- **现象**: AI 在 Strategist 阶段就生成 SVG 代码
- **原因**: 未遵守串行执行规则
- **解决**:
  ```markdown
  > [!CAUTION]
  > ## 🚨 Global Execution Discipline (MANDATORY)
  >
  > 1. **SERIAL EXECUTION** — Steps MUST be executed in order
  > 2. **BLOCKING = HARD STOP** — ⛔ BLOCKING steps require explicit user confirmation
  > 3. **NO CROSS-PHASE BUNDLING** — Forbidden
  > 4. **NO SPECULATIVE EXECUTION** — No "pre-preparing" content
  ```
- **教训**: 在 SKILL.md 顶部用最高优先级标注执行纪律

#### 坑 3: SVG 生成质量不稳定
- **现象**: 有时生成的 SVG 格式错乱
- **原因**: 设计上下文未传递到 Executor
- **解决**:
  - 在 Strategist 输出完整的 design_spec.md
  - Executor 读取 design_spec.md 作为全局上下文
  - 逐页生成时保持上下文一致
- **教训**: 上下文传递要显式、完整

#### 坑 4: PPTX 导出后不可编辑
- **现象**: PPTX 中的图表是图片，无法编辑
- **原因**: 使用了图片嵌入而非原生形状
- **解决**:
  ```python
  # 错误：添加为图片
  slide.shapes.add_picture(svg_path, x, y)
  
  # 正确：添加为原生形状
  # 使用 python-pptx 的 Shape 对象构建
  ```
- **教训**: PPTX 导出要保证原生可编辑性

#### 坑 5: 模板管理混乱
- **现象**: 模板太多，找不到合适的
- **解决**:
  - 建立模板索引（layouts_index.json, charts_index.json）
  - 按场景分类（封面、内容页、图表页、封底）
  - 提供模板选择指南
- **教训**: 模板要系统化组织

**技能开发检查清单**:

- [ ] SKILL.md 包含完整的触发规则
- [ ] 执行流程有明确的步骤和检查点
- [ ] 关键步骤有 ⛔ BLOCKING 标注
- [ ] 脚本有错误处理和日志输出
- [ ] 有测试用例和示例
- [ ] README.md 包含版本号和使用说明
- [ ] 已发布到 ClawHub（可选）

---

## 4. 实践篇：Multi-Agent 体系开发

### 4.1 关键要素

**Multi-Agent 核心概念**:

| 概念 | 说明 | 示例 |
|------|------|------|
| 主 Agent | 任务协调者，负责路由和汇总 | `main` |
| 子 Agent | 任务执行者，专注特定领域 | `ai_intel`, `tech_analyst` |
| 任务路由 | 根据关键词匹配任务类型 | `task_routing_rules.yaml` |
| 会话隔离 | 每个 Agent 有独立工作空间 | `workspace-AI-INTEL/` |
| 状态跟踪 | 通过共享文件同步状态 | `task_status.md` |

**Agent 能力映射**（当前配置）:

```yaml
ai_intel:
  name: AI 情报官
  workspace: /home/Vincent/.openclaw/workspace-AI-INTEL
  model: bailian/qwen3-max-2026-01-23
  capabilities: [情报采集、市场监控、趋势分析]

tech_analyst:
  name: 技术分析师
  workspace: /home/Vincent/.openclaw/workspace-TECH-ANALYST
  model: bailian/qwen3-max-2026-01-23
  capabilities: [技术分析、架构拆解、战略规划]

content_creator:
  name: 内容创作官
  workspace: /home/Vincent/.openclaw/workspace-CONTENT-CREATOR
  model: bailian/qwen3-coder-plus
  capabilities: [公众号文章、视频脚本、传播策略]

work_present_output:
  name: 工作演示输出代理
  workspace: /home/Vincent/.openclaw/workspace-WORK-PRESENT-OUTPUT
  model: bailian/qwen3-max-2026-01-23
  capabilities: [HTML 幻灯片、PPTX、汇报视频]
```

---

### 4.2 实战案例：当前 Multi-Agent 体系

**任务路由规则**（task_routing_rules.yaml）:

```yaml
task_classification:
  # 简单任务 - 直接执行
  - type: math_tutoring
    keywords: ["数学", "小瑜", "辅导", "练习题"]
    workflow_mode: direct
    agents: [main]
    
  # 中等复杂度 - Reactor 简化审核
  - type: intelligence_collection
    keywords: ["情报", "动态", "论文", "行业趋势"]
    primary_agent: ai_intel
    workflow_mode: reactor_simple
    
  # 高复杂度 - 完整 Reactor 审核
  - type: technical_analysis
    keywords: ["架构", "技术评估", "竞品分析"]
    primary_agent: tech_analyst
    secondary_agents: [ai_intel]
    workflow_mode: reactor_full
    
  - type: content_creation
    keywords: ["公众号", "文章", "视频", "脚本"]
    primary_agent: content_creator
    secondary_agents: [tech_analyst, ai_intel]
    workflow_mode: reactor_full
    
  - type: complex_research
    keywords: ["深度研究", "综合分析", "战略报告"]
    primary_agent: tech_analyst
    secondary_agents: [ai_intel, official_operate]
    workflow_mode: reactor_full
```

**任务执行流程**（以"深度分析中国 MaaS 市场"为例）:

```
[1] 用户输入："深度分析中国 MaaS 市场，包含商业洞察、技术架构、主流厂家分析"
    ↓
[2] 主 Agent 读取 task_routing_rules.yaml
    ↓
[3] 关键词匹配："深度分析" → complex_research
    ↓
[4] Agent 选择：
    - primary_agent: tech_analyst
    - secondary_agents: ai_intel, official_operate
    ↓
[5] 启动子 Agent（并行）:
    sessions_spawn(agent_id="tech_analyst", task="...", mode="run")
    sessions_spawn(agent_id="ai_intel", task="【辅助】...", mode="run")
    sessions_spawn(agent_id="official_operate", task="【辅助】...", mode="run")
    ↓
[6] 状态跟踪：
    更新 task_status.md:
    | 任务 ID | 任务名称 | 主 Agent | 状态 | 更新时间 |
    | 20260331001 | 中国 MaaS 市场分析 | tech_analyst | running | 2026-03-31 16:10 |
    ↓
[7] 结果汇总：
    主 Agent 收集各子 Agent 输出，生成最终报告
    ↓
[8] 任务完成：
    更新 task_status.md: 状态 → success
```

---

### 4.3 通信问题与解决方案

#### 问题 1: 子 Agent 未启动（最严重）
- **现象**: 调度脚本存在，但子 Agent 从未执行
- **根因**: 主 Agent 只打印命令，未调用 `sessions_spawn` 工具
- **发现过程**:
  1. 查看 task_status.md，所有任务都是 `cancelled`
  2. 检查调度脚本，发现只生成命令字符串
  3. 查看主 Agent 日志，未找到 `sessions_spawn` 调用
- **解决方案**:
  ```javascript
  // 错误：只打印命令
  console.log("sessions_spawn(agent_id='tech_analyst', ...)")
  
  // 正确：直接调用工具
  sessions_spawn(
    runtime = "subagent",
    agent_id = "tech_analyst",
    task = "【任务 ID: 20260331001】深度分析中国 MaaS 市场",
    mode = "run"
  )
  ```
- **验证方法**:
  ```bash
  # 查看子 Agent 列表
  subagents list
  
  # 查看会话列表
  sessions_list
  ```

#### 问题 2: Agent 间上下文丢失
- **现象**: 子 Agent 不知道主 Agent 的决策
- **根因**: 工作空间隔离，文件不共享
- **解决方案**:
  1. 使用共享目录：`/home/Vincent/.openclaw/workspace/shared/`
  2. 通过 task_status.md 传递状态
  3. 主 Agent 在 task 参数中包含完整上下文
  ```javascript
  sessions_spawn(
    agent_id = "content_creator",
    task = "基于以下材料撰写公众号文章：[材料内容]...",
    mode = "run"
  )
  ```

#### 问题 3: 飞书推送冲突
- **现象**: 多个 Agent 同时推送飞书，用户收到重复消息
- **根因**: 未统一推送出口
- **解决方案**:
  1. 只有主 Agent 负责最终推送
  2. 子 Agent 输出到共享文件
  3. 主 Agent 汇总后统一推送
  ```javascript
  // 子 Agent：输出到文件
  write(path = "/home/Vincent/.openclaw/workspace/shared/ai_intel_output.md", ...)
  
  // 主 Agent：读取并推送
  read(path = "/home/Vincent/.openclaw/workspace/shared/ai_intel_output.md")
  message(channel = "feishu", to = "ou_xxx", message = "...")
  ```

---

### 4.4 协同问题与解决方案

#### 问题 1: 任务依赖未满足
- **现象**: content_creator 启动时，ai_intel 的材料还没生成
- **根因**: 并行启动但未等待依赖完成
- **解决方案**:
  ```yaml
  # task_routing_rules.yaml
  - type: content_creation
    primary_agent: content_creator
    secondary_agents: [tech_analyst, ai_intel]
    dependencies:
      - ai_intel: intelligence_output
      - tech_analyst: analysis_output
    workflow_mode: reactor_full
  ```
  ```javascript
  // 主 Agent 检查依赖
  while (!fileExists("shared/ai_intel_output.md")) {
    await sleep(5000);  // 等待 5 秒
  }
  // 依赖满足，启动 content_creator
  sessions_spawn(agent_id = "content_creator", ...)
  ```

#### 问题 2: 结果格式不一致
- **现象**: 各 Agent 输出格式不同，难以汇总
- **根因**: 未定义统一的输出规范
- **解决方案**:
  ```markdown
  # shared/output_template.md
  ## 输出规范
  1. 标题：## <任务 ID> <任务名称>
  2. 摘要：100 字以内
  3. 正文：Markdown 格式
  4. 来源：所有结论有链接
  5. 置信度：0-100 评分
  ```

#### 问题 3: 超时处理不统一
- **现象**: 某些 Agent 超时后无错误处理
- **解决方案**:
  ```javascript
  sessions_spawn(
    agent_id = "tech_analyst",
    task = "...",
    timeoutSeconds = 1800,  // 30 分钟超时
    mode = "run"
  )
  
  // 主 Agent 监控超时
  const status = await checkSessionStatus(sessionKey);
  if (status === 'timeout') {
    updateTaskStatus(taskId, 'failed', '超时');
  }
  ```

---

### 4.5 任务监控问题与解决方案

#### 监控系统架构

```
┌─────────────────────────────────────────┐
│         任务调度器 (每 5 分钟)            │
│  /home/Vincent/.openclaw/workspace/     │
│  shared/.scheduler/task_scheduler.sh    │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         检查项                           │
│  1. 超时任务扫描                         │
│  2. 子 Agent 状态同步                     │
│  3. Agent 负载状态更新                   │
│  4. 审核轮次推进                         │
│  5. 旧任务清理（30 天）                   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         状态更新                          │
│  task_status.md                          │
│  load_balance.json                       │
│  fingerprints.json                       │
└─────────────────────────────────────────┘
```

#### 任务状态表（task_status.md）

```markdown
| 任务 ID | 任务名称 | 主 Agent | 辅助 Agent | 状态 | 置信度 | 审核轮次 | 创建时间 | 更新时间 | 备注 |
|--------|----------|---------|-----------|------|--------|----------|----------|----------|------|
| 20260331001 | 中国 MaaS 市场分析 | tech_analyst | ai_intel | success | 95 | 3 | 2026-03-31 16:10 | 2026-03-31 16:25 | 已完成全流程审核 |
| 20260331002 | 多智能体实战公众号改写 | official_operate | tech_analyst,ai_intel | success | 92 | 3 | 2026-03-31 20:20 | 2026-03-31 20:23 | 已完成全流程审核 |
```

#### 状态机规则

```
pending → running → review → success
   ↑          ↑         ↑
   └──────────┴─────────┴→ failed (超时/错误)
```

**自动流转条件**:

| 流转 | 触发条件 |
|------|----------|
| pending→running | 子 Agent 启动成功 |
| running→review | 主 Agent 完成执行，置信度<90 |
| running→success | 主 Agent 完成执行，置信度≥90 |
| review→success | 审核通过 |
| any→failed | 超时 (>24h) 或 子 Agent 执行失败 |

#### 超时规则

| 任务类型 | 超时阈值 |
|----------|----------|
| math_tutoring / simple_query | 30 分钟 |
| intelligence_collection | 2 小时 |
| technical_analysis / content_creation | 6 小时 |
| complex_research | 24 小时 |
| work_presentation | 6 小时 |

#### 监控脚本（task_scheduler.sh 片段）

```bash
#!/bin/bash
# 任务调度器 - 每 5 分钟运行

# 1. 检查超时任务
check_timeout_tasks() {
    # 读取 task_status.md
    # 检查 running 状态的任务
    # 如果超过超时阈值，标记为 failed
}

# 2. 同步子 Agent 状态
sync_subagent_status() {
    # 调用 subagents list
    # 更新 task_status.md
}

# 3. 更新 Agent 负载状态
update_load_balance() {
    # 统计每个 Agent 的任务数
    # 写入 load_balance.json
}

# 4. 推进审核轮次
advance_review() {
    # 检查 review 状态的任务
    # 置信度≥90 → success
    # 置信度<90 → 推送审核
}

# 主流程
check_timeout_tasks
sync_subagent_status
update_load_balance
advance_review
```

---

### 4.6 Multi-Agent 开发检查清单

**启动前**:
- [ ] task_routing_rules.yaml 已配置
- [ ] 各 Agent 工作空间已创建
- [ ] 共享目录已设置（shared/）
- [ ] task_status.md 模板已准备

**开发中**:
- [ ] 主 Agent 调用 sessions_spawn（不是打印命令）
- [ ] 子 Agent 输出到共享文件
- [ ] 超时处理已配置
- [ ] 错误处理已配置

**上线前**:
- [ ] 任务调度器已部署
- [ ] 监控系统已运行
- [ ] 告警通知已配置
- [ ] 回滚方案已准备

**运维中**:
- [ ] 每日检查 task_status.md
- [ ] 每周清理旧任务（>30 天）
- [ ] 每月分析任务成功率
- [ ] 持续优化路由规则

---

## 附录

### A. 常用命令速查

```bash
# Cron 管理
cron list                          # 列出所有任务
cron add --job <job.json>          # 添加任务
cron run --jobId <id>              # 手动触发
cron runs --jobId <id>             # 查看执行历史

# 会话管理
sessions_list                      # 列出会话
sessions_history --sessionKey <key> # 查看会话历史
sessions_send --label <label> --message "..." # 发送消息

# 子 Agent 管理
subagents list                     # 列出子 Agent
subagents kill --target <id>       # 终止子 Agent
subagents steer --target <id> --message "..." # 指导子 Agent

# 任务监控
cat shared/task_status.md          # 查看任务状态
cat shared/.scheduler/log.md       # 查看调度日志
```

### B. 故障排查流程

```
1. 用户报告问题
   ↓
2. 查看 task_status.md（任务状态）
   ↓
3. 查看 shared/.scheduler/log.md（调度日志）
   ↓
4. 查看 sessions_list（会话状态）
   ↓
5. 查看 subagents list（子 Agent 状态）
   ↓
6. 定位问题根因
   ↓
7. 修复并验证
   ↓
8. 更新 SELF_IMPROVEMENT_REMINDER.md
```

### C. 参考文档

- OpenClaw 官方文档：`/home/Vincent/.openclaw/workspace/docs/`
- ClawHub 技能市场：https://clawhub.ai
- 社区 Discord: https://discord.com/invite/clawd

---

**培训材料版本**: v1.0  
**最后更新**: 2026-04-09  
**维护者**: Vincent
