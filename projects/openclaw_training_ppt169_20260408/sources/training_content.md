# OpenClaw 内部培训材料

## 封面页

**标题**: OpenClaw 内部培训材料
**副标题**: 从原理到实践，掌握 AI Agent 操作系统
**日期**: 2026 年 4 月 9 日
**培训对象**: 部门内部技术团队
**演讲者**: Vincent

---

## 目录

1. 原理篇：OpenClaw 技术基础
2. 实践篇 1：第一个 Cron 定时任务
3. 实践篇 2：第一个技能开发
4. 实践篇 3：Multi-Agent 体系开发
5. Q&A 与实战演示

**培训时长**: 2.5 小时

---

## 1.1 OpenClaw 介绍

**OpenClaw 是什么？**

- AI Agent 操作系统
- 让 AI 从"聊天机器人"变成"自主执行者"
- 支持复杂任务的自动化和持续化
- 提供企业级任务监控和质量保障

**核心价值**

- 会话管理：主会话、子会话、隔离会话
- 任务调度：Cron 定时任务、Heartbeat 心跳机制
- 技能系统：可扩展的技能开发和执行框架
- Multi-Agent：多 Agent 协同工作体系
- 记忆系统：短期记忆、长期记忆、自我改进记忆

---

## 1.2 技术架构

**核心组件**

| 组件 | 职责 |
|------|------|
| Gateway | 核心服务，管理所有组件 |
| Session Manager | 会话生命周期管理 |
| Cron Scheduler | 定时任务调度 |
| Skills Engine | 技能加载和执行 |
| Memory System | 记忆存储和检索 |
| Tools Proxy | 工具调用代理 |

**架构层次**

```
Gateway → Agent → Tools → 外部系统
              ↓
        结果返回 → 用户输出
```

---

## 1.3 信息架构

**信息流向**

```
用户输入 → Gateway → Agent → Tools → 外部系统
                                    ↓
                              结果返回 → 用户输出
```

**关键信息类型**

1. 用户消息：微信、飞书、Discord 等
2. 系统事件：Cron 触发、Heartbeat、内部通知
3. 工具调用：API、命令、文件读写
4. 会话状态：任务进度、子 Agent 状态、错误

**数据持久化**

| 类型 | 存储位置 | 用途 |
|------|----------|------|
| 会话历史 | Gateway 内存 + 数据库 | 对话上下文 |
| 长期记忆 | MEMORY.md | 用户偏好、重要事件 |
| 每日日志 | memory/YYYY-MM-DD.md | 原始执行记录 |
| 自我改进 | ~/self-improving/ | 执行优化规则 |

---

## 1.4 记忆架构

**三层记忆系统**

```
┌─────────────────────────────────┐
│    短期记忆 (Session Context)    │
│  - 当前会话消息历史              │
│  - 工具调用结果                  │
│  - 临时变量                      │
└─────────────────────────────────┘
              ↓ 定期提炼
┌─────────────────────────────────┐
│    长期记忆 (MEMORY.md)          │
│  - 用户背景和偏好                │
│  - 重要决策和事件                │
│  - 项目上下文                    │
└─────────────────────────────────┘
              ↓ 经验固化
┌─────────────────────────────────┐
│ 自我改进 (~/self-improving/)    │
│  - 执行优化规则 (memory.md)      │
│  - 领域知识 (domains/)           │
│  - 项目配置 (projects/)          │
│  - 错误修正 (corrections.md)     │
└─────────────────────────────────┘
```

---

## 1.5 技能架构

**技能定义**

技能是 OpenClaw 的可扩展功能模块，包含：
- SKILL.md: 技能描述、触发规则、执行流程
- scripts/: 执行脚本（Shell、Python、Node.js）
- references/: 参考文档和模板
- output/: 技能输出目录（可选）

**技能结构示例（ppt-master）**

```
skills/ppt-master/
├── SKILL.md              # 16KB 技能定义
├── scripts/              # 执行脚本
│   ├── project_manager.py
│   ├── svg_to_pptx.py
│   └── pdf_to_md.py
├── templates/            # 模板库
│   ├── layouts/
│   ├── charts/
│   └── icons/
└── projects/             # 项目输出
```

---

## 1.6 SubAgent 架构

**SubAgent 类型**

| 类型 | runtime | 用途 | 会话模式 |
|------|---------|------|----------|
| subagent | subagent | 通用子任务 | run/session |
| acp | acp | ACP harness | thread |

**调用方式**

```javascript
sessions_spawn(
  runtime = "subagent",
  agent_id = "tech_analyst",
  task = "深度分析中国 MaaS 市场",
  mode = "run",
  timeoutSeconds = 1800
)
```

**工作空间隔离**

```
/home/Vincent/.openclaw/
├── workspace/                    # 主空间
├── workspace-AI-INTEL/           # ai_intel
├── workspace-TECH-ANALYST/       # tech_analyst
└── workspace-CONTENT-CREATOR/    # content_creator
```

---

## 1.7 Cron 任务原理

**调度机制**

```
┌─────────────────────────────────┐
│      Cron Scheduler (13 任务)     │
│  - 国际形势日报 (工作日 8:00)     │
│  - 国际形势 PPT+ 视频 (8:30)      │
│  - 国际形势周报 (周六 10:00)      │
│  - AI 情报日报 (每天 6:40)        │
│  - 质量监控日报 (每天 21:00)      │
└─────────────────────────────────┘
```

**Cron Job 结构**

```json
{
  "name": "国际形势日报",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * 1-5"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "生成今日国际形势日报...",
    "timeoutSeconds": 1800
  }
}
```

---

## 2.1 第一个 Cron 任务：关键要素

**5 个步骤**

1. 明确任务目标：要做什么？输出什么？
2. 设计执行流程：Agent 需要执行哪些步骤？
3. 配置 Cron Job：时间、会话、payload、delivery
4. 测试验证：手动触发测试
5. 监控优化：观察执行情况，调整参数

**关键配置项**

| 配置项 | 说明 | 示例 |
|--------|------|------|
| schedule.kind | 调度类型 | cron / every / at |
| schedule.expr | Cron 表达式 | 0 8 * * 1-5 |
| sessionTarget | 执行会话 | isolated / main |
| payload.kind | 负载类型 | agentTurn / systemEvent |
| timeoutSeconds | 超时时间 | 1800 (30 分钟) |

---

## 2.2 实战案例：国际形势日报

**任务背景**

- 需求：每天早上 8 点获取国际形势 5 分钟快读
- 内容：中东局势、俄乌冲突、中美关系、全球市场
- 输出：飞书推送 + Markdown 文档

**执行流程**

```
[08:00] Cron 触发
    ↓
[08:00] isolated session 启动
    ↓
[08:00] Agent 执行：
    1. Tavily 搜索 7 个主题
    2. 整理新闻（每条 3-5 条）
    3. 生成 Markdown（1500-2000 字）
    4. 保存到指定路径
    5. 发送飞书通知
    ↓
[08:02] 任务完成（耗时约 2 分钟）
```

---

## 2.3 执行数据与复盘

**实际执行数据（2026-04-08 测试）**

| 指标 | 数值 |
|------|------|
| 启动时间 | 19:02 |
| 完成时间 | 19:04 |
| 总耗时 | 124 秒 |
| 输出字数 | 1800 字 |
| 搜索主题 | 7 个 |
| 飞书推送 | ✅ 成功 |

**遇到的 3 个坑**

1. 输出目录不一致 → 统一路径配置
2. 搜索超时 → 增加 timeout + 并行化
3. 飞书推送失败 → 检查 token + 重试逻辑

---

## 3.1 第一个技能开发：关键要素

**技能开发流程**

```
1. 需求分析 → 2. 设计结构 → 3. 编写代码 
→ 4. 测试验证 → 5. 文档编写 → 6. 发布部署
```

**技能文件结构**

```
skills/<skill-name>/
├── SKILL.md              # 必须：技能定义
├── scripts/              # 必须：执行脚本
├── references/           # 可选：参考文档
├── templates/            # 可选：模板文件
├── output/               # 可选：输出目录
└── README.md             # 推荐：版本记录
```

**SKILL.md 核心结构**

- 触发规则：关键词匹配
- 执行流程：步骤和检查点
- 工具调用：exec/write/message

---

## 3.2 实战案例：PPT-Master 技能

**技能背景**

- 需求：将 Markdown/PDF/DOCX 转换为专业 PPTX
- 核心功能：SVG 生成、多模板支持、PPTX 导出
- 开发周期：2 周（含测试和优化）

**核心工作流**

```
1. 源内容处理（PDF/DOCX→MD）
    ↓
2. 项目初始化
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

---

## 3.3 技能开发 5 大坑

**坑 1: 技能触发失败**
- 现象：用户说"生成 PPT"，技能不响应
- 原因：SKILL.md 关键词不全
- 解决：覆盖中英文、口语化表达

**坑 2: 跨阶段执行（最严重）**
- 现象：AI 在 Strategist 阶段就生成 SVG
- 原因：未遵守串行执行规则
- 解决：SKILL.md 顶部标注执行纪律

**坑 3: SVG 质量不稳定**
- 现象：生成的 SVG 格式错乱
- 原因：设计上下文未传递
- 解决：显式传递 design_spec.md

**坑 4: PPTX 导出后不可编辑**
- 现象：图表是图片，无法编辑
- 原因：使用图片嵌入而非原生形状
- 解决：使用 python-pptx 原生 Shape

**坑 5: 模板管理混乱**
- 现象：模板太多，找不到合适的
- 解决：建立模板索引，按场景分类

---

## 4.1 Multi-Agent 关键要素

**核心概念**

| 概念 | 说明 | 示例 |
|------|------|------|
| 主 Agent | 任务协调者 | main |
| 子 Agent | 任务执行者 | ai_intel, tech_analyst |
| 任务路由 | 关键词匹配 | task_routing_rules.yaml |
| 会话隔离 | 独立工作空间 | workspace-AI-INTEL/ |
| 状态跟踪 | 共享文件同步 | task_status.md |

**Agent 能力映射**

```yaml
ai_intel:
  capabilities: [情报采集、市场监控、趋势分析]
  
tech_analyst:
  capabilities: [技术分析、架构拆解、战略规划]
  
content_creator:
  capabilities: [公众号文章、视频脚本、传播策略]
```

---

## 4.2 实战案例：任务路由

**任务分类规则**

```yaml
# 简单任务 - 直接执行
- type: math_tutoring
  keywords: ["数学", "小瑜", "辅导"]
  agents: [main]
  
# 中等复杂度 - Reactor 简化审核
- type: intelligence_collection
  keywords: ["情报", "动态", "论文"]
  primary_agent: ai_intel
  
# 高复杂度 - 完整 Reactor 审核
- type: content_creation
  keywords: ["公众号", "文章", "视频"]
  primary_agent: content_creator
  secondary_agents: [tech_analyst, ai_intel]
```

---

## 4.3 通信问题与解决方案

**问题 1: 子 Agent 未启动（最严重）**
- 现象：调度脚本存在，但子 Agent 从未执行
- 根因：主 Agent 只打印命令，未调用 sessions_spawn
- 解决：直接调用 sessions_spawn 工具

**问题 2: Agent 间上下文丢失**
- 现象：子 Agent 不知道主 Agent 的决策
- 根因：工作空间隔离，文件不共享
- 解决：使用共享目录 + task_status.md

**问题 3: 飞书推送冲突**
- 现象：多个 Agent 同时推送，用户收到重复消息
- 根因：未统一推送出口
- 解决：只有主 Agent 负责最终推送

---

## 4.4 协同问题与解决方案

**问题 1: 任务依赖未满足**
- 现象：content_creator 启动时，ai_intel 材料还没生成
- 解决：定义 dependencies，主 Agent 检查依赖

**问题 2: 结果格式不一致**
- 现象：各 Agent 输出格式不同，难以汇总
- 解决：定义统一的 output_template.md

**问题 3: 超时处理不统一**
- 现象：某些 Agent 超时后无错误处理
- 解决：配置 timeoutSeconds + 主 Agent 监控

---

## 4.5 任务监控系统

**监控系统架构**

```
┌─────────────────────────────────┐
│   任务调度器 (每 5 分钟)          │
│  1. 超时任务扫描                 │
│  2. 子 Agent 状态同步             │
│  3. Agent 负载状态更新           │
│  4. 审核轮次推进                 │
│  5. 旧任务清理（30 天）           │
└─────────────────────────────────┘
```

**状态机规则**

```
pending → running → review → success
   ↑          ↑         ↑
   └──────────┴─────────┴→ failed
```

---

## 4.6 超时规则

| 任务类型 | 超时阈值 |
|----------|----------|
| math_tutoring / simple_query | 30 分钟 |
| intelligence_collection | 2 小时 |
| technical_analysis / content_creation | 6 小时 |
| complex_research | 24 小时 |
| work_presentation | 6 小时 |

---

## 4.7 Multi-Agent 开发检查清单

**启动前**
- [ ] task_routing_rules.yaml 已配置
- [ ] 各 Agent 工作空间已创建
- [ ] 共享目录已设置
- [ ] task_status.md 模板已准备

**开发中**
- [ ] 主 Agent 调用 sessions_spawn
- [ ] 子 Agent 输出到共享文件
- [ ] 超时处理已配置
- [ ] 错误处理已配置

**上线前**
- [ ] 任务调度器已部署
- [ ] 监控系统已运行
- [ ] 告警通知已配置
- [ ] 回滚方案已准备

---

## 附录：常用命令速查

**Cron 管理**
```bash
cron list                          # 列出所有任务
cron add --job <job.json>          # 添加任务
cron run --jobId <id>              # 手动触发
```

**会话管理**
```bash
sessions_list                      # 列出会话
sessions_history --sessionKey <key>
sessions_send --label <label> --message "..."
```

**子 Agent 管理**
```bash
subagents list                     # 列出子 Agent
subagents kill --target <id>       # 终止
subagents steer --target <id> --message "..."
```

---

## 故障排查流程

```
1. 用户报告问题
    ↓
2. 查看 task_status.md（任务状态）
    ↓
3. 查看调度日志
    ↓
4. 查看 sessions_list（会话状态）
    ↓
5. 查看 subagents list
    ↓
6. 定位问题根因
    ↓
7. 修复并验证
    ↓
8. 更新自我改进记忆
```

---

## Q&A

**培训总结**

- 原理篇：掌握 OpenClaw 核心架构
- 实践篇 1：学会创建 Cron 定时任务
- 实践篇 2：学会开发技能，避开 5 大坑
- 实践篇 3：学会 Multi-Agent 协同与监控

**后续支持**

- 官方文档：/home/Vincent/.openclaw/workspace/docs/
- ClawHub 技能市场：https://clawhub.ai
- 社区 Discord: https://discord.com/invite/clawd

---

## 谢谢！

**联系方式**

- 演讲者：Vincent
- 日期：2026 年 4 月 9 日
- 版本：v1.0

**Q&A 时间**
