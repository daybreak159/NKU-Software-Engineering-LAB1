# 执行记录：检索官方文档并补充到 summary.md

## 用户指令

请检索Qoder官方文档中关于"tools / skills / agent mode / planning"相关的说明，并把结果补充到 <测试目录>/summary.md 中。

要求：
1. 必须优先使用官方文档或官方帮助页面
2. 给出你实际参考的来源名称
3. 新增一个小节，标题为"官方文档补充说明"
4. 不要编造搜索结果

---

## 执行过程

### 步骤 1：检索官方文档

通过 WebSearch 搜索 Qoder 官方文档站点 (docs.qoder.com)，定位到以下四个页面：

| 主题 | 来源页面 |
|------|----------|
| Tools | [Using CLI - Qoder Docs](https://docs.qoder.com/cli/using-cli) |
| Skills | [Skills - Qoder Docs](https://docs.qoder.com/cli/Skills) |
| Agent Mode | [Agent Mode - Qoder Docs](https://docs.qoder.com/user-guide/chat/agent) |
| Planning | [Planning Agent - Qoder Docs](https://docs.qoder.com/user-guide/chat/plan-agent) |

### 步骤 2：逐页获取内容

使用 WebFetch 抓取每个页面的核心内容摘要。

### 步骤 3：更新 summary.md

在 summary.md 末尾新增"官方文档补充说明"小节，包含四个子标题：

- **Tools**：内置工具 Grep/Read/Write/Bash，支持 MCP 扩展
- **Skills**：可复用的 SKILL.md 机制，支持自动触发和手动调用
- **Agent Mode**：自主决策、环境感知、工具调用，支持计划审查和进度追踪
- **Planning**：先生成方案再执行，适用于复杂功能和多轮迭代

---

## 实际参考来源

1. [Using CLI - Qoder Docs](https://docs.qoder.com/cli/using-cli)
2. [Skills - Qoder Docs](https://docs.qoder.com/cli/Skills)
3. [Agent Mode - Qoder Docs](https://docs.qoder.com/user-guide/chat/agent)
4. [Planning Agent - Qoder Docs](https://docs.qoder.com/user-guide/chat/plan-agent)

所有内容均从 docs.qoder.com 官方文档站点获取，未编造任何搜索结果。
