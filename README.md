# AI Agent 深度评测报告

## 项目概述

本项目对三个 AI Agent 工具进行了系统性评测：

| Agent | 名称 | 评测任务数 |
|-------|------|-----------|
| OpenClaw | OpenClaw Agent | 7 题 |
| Qoder | Qoder CLI | 9 题 |
| Claude | Claude Code | 9 题 |

**实验环境**：Windows Subsystem for Linux 2（WSL2），统一使用 MiniMax 2.5 模型 API 进行推理。

## 目录结构

```
AI_Agent_Eval/
├── README.md                    # 本文件
├── 核心成果/
│   ├── agent_评测报告.tex       # LaTeX 格式完整评测报告
│   └── ai_agent_调研模板.xlsx   # 三 Agent 对比表格
├── OpenClaw/
│   ├── exec_records/            # OpenClaw 各题答题记录（7个md）
│   └── README.md               # OpenClaw 目录说明
├── Qoder/
│   ├── exec_records/           # Qoder 各题执行记录（9个md）
│   ├── data/                   # 测试数据文件（notes1-3.txt）
│   ├── code_eval/              # Bug 修复任务文件
│   ├── Qoder02~08.png          # 执行过程截图（7张）
│   ├── eval_design.md          # 评测设计说明
│   ├── summary.md              # 统计汇总
│   ├── result.csv              # 结构化结果数据
│   ├── stats.py                # 统计脚本
│   ├── stats.txt               # 统计输出
│   └── README.md               # Qoder 目录说明
└── Claude/
    ├── exec_records/           # Claude Code 各题执行记录（9个md）
    ├── data/                   # 测试数据文件
    └── README.md               # Claude 目录说明
```

## 各目录说明

### 核心成果

- **agent_评测报告.tex** — 完整的 LaTeX 评测报告，包含 OpenClaw / Qoder / Claude 三个 Agent 的逐题分析、总结和对比表格
- **ai_agent_调研模板.xlsx** — 调研对比表格，涵盖 Agent 概述、任务规划、工具调用、记忆管理、安全性、部署便捷性等维度

### OpenClaw

OpenClaw Agent 的评测记录。评测任务共 7 题（Q1-Q7），涵盖：任务规划、文件创建、内容理解、错误修复、代码编写、信息检索、Bug 调试。

注：OpenClaw 无独立的工作目录截图，执行记录从 tex 报告中提取。

### Qoder

Qoder CLI 的评测记录和测试数据。评测任务共 9 题，包含：
- 执行记录（exec_records/）：每个任务的完整执行过程文档
- 测试数据（data/）：3 个主题 txt 文件
- Bug 修复任务（code_eval/）：scores.csv、score_report.py（含4个bug）、repair_report.md
- 7 张执行过程截图

### Claude

Claude Code 的评测记录和测试数据。评测任务共 9 题，包含执行记录和数据文件。

注：Claude 测试中部分题目（Q6-Q9）的内容涉及协助完成 Qoder 的 tex 报告整理和 xlsx 填写，与其他 Agent 的评测任务有所不同。

## 原始题目来源

评测题目嵌入在各 Agent 的 exec_record 文件的"用户指令"章节中，未单独保存为独立文件。

## 文件来源

| 文件 | 来源 |
|------|------|
| /home/wsy/qoder/ | Qoder 和 OpenClaw Agent 的原始工作目录 |
| /home/wsy/claude/ | Claude Code 的原始工作目录 |
| agent_评测报告.tex | /home/wsy/qoder/ |
| ai_agent_调研模板.xlsx | /home/wsy/qoder/ |
