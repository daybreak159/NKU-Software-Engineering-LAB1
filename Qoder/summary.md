# 评测文件统计汇总

## 文件状态总览

| 文件名 | 状态 | 主题 | 行数 |
|--------|------|------|------|
| notes1.txt | ✅ 存在 | 任务规划 | 10 |
| notes2.txt | ✅ 存在 | 工具调用 | 10 |
| notes3.txt | ✅ 存在 | 记忆与上下文管理 | 10 |
| note4.txt | ❌ 缺失 | - | - |

## 详细内容摘要

### notes1.txt - 任务规划能力评测要点
- 任务规划是 AI Agent 的核心能力之一
- 包括：任务分解、依赖识别、动态调整、优先级分配
- 评测关注：步骤完整性、顺序合理性、异常处理能力

### notes2.txt - 工具调用能力评测要点
- 工具调用体现 Agent 与外部系统交互水平
- 包括：场景识别、工具选择、参数构造、结果解析、降级策略
- 评测关注：参数准确性、错误处理、调用效率

### notes3.txt - 记忆与上下文管理能力评测要点
- 决定 Agent 在长对话中的一致性
- 包括：短期记忆、长期记忆、上下文窗口管理、遗忘机制
- 评测关注：跨轮信息保持、冲突检测、上下文压缩

### note4.txt
**状态：文件不存在**

按要求未编造内容，已标记为缺失状态。

---

## 统计结果

- 有效文件数：3
- 缺失文件数：1
- 总行数：30（仅统计存在文件）

---

## 官方文档补充说明

以下内容来源于 Qoder 官方文档站点 (docs.qoder.com)，检索时间 2026-03-20。

### Tools（工具）

Qoder CLI 内置工具包括 Grep、Read、Write、Bash，用于文件/目录操作和 Shell 命令执行。Agent 模式下还可使用文件搜索、文件读取、命令执行等工具，命令执行默认需用户确认，除非在 Qoder Settings 中配置了允许列表。此外支持通过 MCP 扩展外部工具。

> 来源：[Using CLI - Qoder Docs](https://docs.qoder.com/cli/using-cli)

### Skills（技能）

技能是 Qoder CLI 中将专业知识打包成可复用功能的机制。每个 Skill 是一个包含 `SKILL.md` 文件的文件夹，用于教 Qoder CLI 执行特定任务。创建 Skill 需要建立目录并编写包含 YAML 元数据的 `SKILL.md`。使用时可自动触发，也可手动输入 `/skill-name` 调用。

> 来源：[Skills - Qoder Docs](https://docs.qoder.com/cli/Skills)

### Agent Mode（Agent 模式）

Agent 模式具备自主决策、环境感知和工具调用能力，可处理项目级别的变更。Agent 会生成计划供用户审查，用户可通过状态指示器（空心圆、加载圆、勾选框）追踪进度。还支持一键增强提示词功能，用于优化用户输入。

> 来源：[Agent Mode - Qoder Docs](https://docs.qoder.com/user-guide/chat/agent)

### Planning（规划）

Planning Agent 在编写代码前先生成实施方案和计划，适用于复杂功能开发或需要多轮迭代的场景。用户描述任务后，Agent 生成计划，用户审查并调整步骤，然后开始执行，执行期间待办状态会实时更新。

> 来源：[Planning Agent - Qoder Docs](https://docs.qoder.com/user-guide/chat/plan-agent)
