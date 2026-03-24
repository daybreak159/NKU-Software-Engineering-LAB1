# 执行记录：Python Bug 修复任务

## 用户指令

请在 <测试目录>/code_eval 中完成一个最小化 Python bug 修复任务。

任务要求：
1. 先创建目录 <测试目录>/code_eval
2. 在该目录下创建文件 scores.csv
3. 在该目录下创建文件 score_report.py
4. 完成以下事情：
   - 先阅读代码并指出其中的问题
   - 给出一个简短修复计划
   - 修复代码，但尽量不要无必要地完全重写
   - 运行脚本并验证输出
   - 在同目录下生成一个 repair_report.md

正确行为要求：
1. 无效分数（空值、非数字）不能导致程序崩溃，应被忽略
2. average 应按有效成绩计算，并保留为正常数值结果，不要被整除截断
3. 及格线按 >= 60 计算
4. top student 应该是最高分学生，而不是最低分学生
5. 最终正确输出应满足：
   - total: 5
   - average: 74.0
   - passed: 4
   - top: Alice 95

---

## 执行过程

### 步骤 1：创建目录和文件

```bash
mkdir -p /home/wsy/claude/code_eval
```

创建文件：
- `scores.csv` - 包含 7 条成绩记录（含 2 条无效数据）
- `score_report.py` - 原始 Python 脚本

### 步骤 2：运行原始代码观察错误

```bash
cd /home/wsy/claude/code_eval && python3 score_report.py
```

**错误输出**:
```
ValueError: invalid literal for int() with base 10: ''
```

### 步骤 3：分析代码问题

| 函数 | 问题 | 影响 |
|------|------|------|
| `load_scores` | `int(row["score"])` 对空值/非数字抛异常 | 程序崩溃 |
| `average_score` | 使用 `//` 整除，截断小数 | 结果不精确 |
| `passed_students` | 使用 `> 60`，应为 `>= 60` | 及格线错误 |
| `top_student` | 排序后取 `[0]` 返回最低分 | 逻辑错误 |

### 步骤 4：修复代码

**修改 1** - `load_scores()`: 添加 try-except 处理无效分数

**修改 2** - `average_score()`: `//` 改为 `/`

**修改 3** - `passed_students()`: `>` 改为 `>=`

**修改 4** - `top_student()`: 添加 `reverse=True`

### 步骤 5：运行验证

```bash
cd /home/wsy/claude/code_eval && python3 score_report.py
```

**输出**:
```
total: 5
average: 74.0
passed: 4
top: Alice 95
```

### 步骤 6：生成修复报告

创建 `repair_report.md`，详细说明发现的 bug、修改内容和最终结果。

---

## 最终报告

### 修改的文件

| 文件 | 操作 |
|------|------|
| `/home/wsy/claude/code_eval/scores.csv` | 新建 |
| `/home/wsy/claude/code_eval/score_report.py` | 新建 + 修改 |
| `/home/wsy/claude/code_eval/repair_report.md` | 新建 |

### 执行的命令

1. `mkdir -p /home/wsy/claude/code_eval`
2. `python3 score_report.py`（首次运行，失败）
3. `python3 score_report.py`（修复后运行，成功）

### 最终是否达到预期输出

✅ **完全达到预期输出**

| 指标 | 预期值 | 实际值 |
|------|--------|--------|
| total | 5 | 5 |
| average | 74.0 | 74.0 |
| passed | 4 | 4 |
| top | Alice 95 | Alice 95 |
