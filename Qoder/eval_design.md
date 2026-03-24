# 最小化评测环境设计

## 用户问题

请围绕目录 qoder 设计一个最小化评测环境，用于测试 AI Agent 的任务规划、文件处理、上下文管理和错误恢复能力。

要求：
1. 先不要执行，只输出 4 到 6 步计划
2. 每一步写清楚目的
3. 计划中至少包含：文件创建、文件读取、结果汇总、错误处理、上下文延续
4. 不要写空泛建议，要写成可执行步骤

---

## 回答：最小化评测环境设计计划

### 步骤 1：创建目录结构与任务定义文件

**目的**：建立标准化的评测输入框架，为后续所有步骤提供基础骨架。

在 `~/qoder/eval/` 下创建以下结构：
```
eval/
  tasks/        # 每个任务一个 JSON 文件，描述输入、预期输出、评分标准
  fixtures/     # 预置的测试用文件（故意包含错误、缺失字段等）
  results/      # 每次运行生成的结构化结果文件
  logs/         # 原始执行日志，按 task_id + timestamp 命名
  scripts/      # 评测驱动脚本
```

每个 `tasks/*.json` 包含字段：`task_id`、`capability`（规划/文件处理/上下文/错误恢复）、`input`、`expected_output`、`scoring_rubric`。

---

### 步骤 2：编写覆盖四项能力的评测任务集

**目的**：确保每项能力都有对应的可执行测试用例，而非泛化描述。

| 能力 | 任务示例 |
|---|---|
| 任务规划 | 给定一段需求描述，要求 Agent 输出有序步骤列表，检查步骤完整性和依赖顺序 |
| 文件处理 | 读取 `fixtures/broken.json`（故意格式错误），修复并写入 `results/fixed.json` |
| 上下文管理 | 第 1 轮告知变量 A，第 3 轮询问 A 的值，检验跨轮上下文保持能力 |
| 错误恢复 | 提供不存在的文件路径，检验 Agent 是否能识别错误并采用备用路径重试 |

---

### 步骤 3：实现评测驱动脚本 `scripts/run_eval.py`

**目的**：自动化执行所有任务，统一捕获 Agent 输出，避免人工记录引入的偏差。

脚本核心逻辑：
1. 遍历 `tasks/*.json`，按 `capability` 分组加载
2. 对每个任务调用 Agent 接口，设置超时（防止挂起）
3. 捕获 stdout/stderr，写入 `logs/<task_id>_<timestamp>.log`
4. 将 Agent 输出与 `expected_output` 对比，打分后写入 `results/<task_id>.json`
5. 遇到异常（超时、崩溃、空输出）时记录 `status: error`，**不中断整体评测**

---

### 步骤 4：构造错误注入 fixtures

**目的**：专门为"文件处理"和"错误恢复"能力提供真实的失败场景，而非模拟。

在 `fixtures/` 下预置：
- `broken.json` — 语法错误的 JSON（缺少引号、多余逗号）
- `missing_ref.txt` — 引用了不存在路径的配置文件
- `partial_data.csv` — 故意截断的 CSV（最后一行不完整）
- `empty.txt` — 空文件，用于测试边界处理

---

### 步骤 5：实现结果汇总脚本 `scripts/summarize.py`

**目的**：将分散的 `results/*.json` 聚合为单一评测报告，支持按能力维度查看得分。

输出格式为 `eval_report.json`，结构如下：
```json
{
  "run_at": "...",
  "total_tasks": 12,
  "by_capability": {
    "planning": {"passed": 3, "failed": 1, "score": 0.75},
    "file_handling": {"passed": 2, "failed": 2, "score": 0.50},
    "context_management": {"passed": 4, "failed": 0, "score": 1.0},
    "error_recovery": {"passed": 1, "failed": 2, "score": 0.33}
  },
  "failed_tasks": ["task_005", "task_009"]
}
```

---

### 步骤 6：添加上下文延续验证机制

**目的**：单独处理多轮对话测试，因为其评分逻辑与单轮任务不同，需要维护会话状态。
在 `scripts/run_eval.py` 中对 `capability == "context_management"` 的任务：
1. 按 `task.turns` 数组顺序逐轮发送消息，**复用同一会话 ID**
2. 仅在指定轮次（`eval_at_turn`）截取 Agent 输出进行评分
3. 若中间轮 Agent 主动重置上下文（如重新询问已知信息），记录为 `context_loss: true` 并扣分

---

## 总结

以上 6 步覆盖了文件创建（步骤1、4）、文件读取（步骤3、6）、结果汇总（步骤5）、错误处理（步骤3、4）、上下文延续（步骤6）全部要求，且每步均可直接执行落地。
