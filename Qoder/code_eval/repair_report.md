# Python Bug 修复报告

## 发现的 Bug

### Bug 1: 无效分数导致程序崩溃

**位置**: `load_scores()` 函数第 10 行

**问题**: `int(row["score"])` 对空值或非数字字符串会抛出 `ValueError`

**原始代码**:
```python
"score": int(row["score"])
```

**修复后**:
```python
try:
    score = int(row["score"])
    records.append({
        "name": row["name"],
        "score": score
    })
except (ValueError, TypeError):
    continue
```

---

### Bug 2: 平均分被整除截断

**位置**: `average_score()` 函数第 16 行

**问题**: 使用 `//` 整除运算符，小数部分被截断

**原始代码**:
```python
return total // len(records)
```

**修复后**:
```python
return total / len(records)
```

---

### Bug 3: 及格线判断错误

**位置**: `passed_students()` 函数第 19 行

**问题**: 使用 `> 60` 排除了刚好 60 分的学生

**原始代码**:
```python
return [r for r in records if r["score"] > 60]
```

**修复后**:
```python
return [r for r in records if r["score"] >= 60]
```

---

### Bug 4: 最高分学生返回错误

**位置**: `top_student()` 函数第 22 行

**问题**: 排序后取 `[0]` 返回的是最低分学生

**原始代码**:
```python
records = sorted(records, key=lambda x: x["score"])
return records[0]
```

**修复后**:
```python
records = sorted(records, key=lambda x: x["score"], reverse=True)
return records[0]
```

---

## 修改汇总

| 函数 | 修改类型 | 说明 |
|------|----------|------|
| `load_scores` | 异常处理 | 添加 try-except 跳过无效分数 |
| `average_score` | 运算符修改 | `//` 改为 `/` |
| `passed_students` | 条件修改 | `>` 改为 `>=` |
| `top_student` | 参数添加 | 添加 `reverse=True` |

---

## 最终结果

**运行输出**:
```
total: 5
average: 74.0
passed: 4
top: Alice 95
```

**验证结果**: ✅ 所有输出符合预期

| 指标 | 预期值 | 实际值 | 状态 |
|------|--------|--------|------|
| total | 5 | 5 | ✅ |
| average | 74.0 | 74.0 | ✅ |
| passed | 4 | 4 | ✅ |
| top | Alice 95 | Alice 95 | ✅ |

---

## 数据处理说明

原始数据中：
- Frank: 空值 → 已忽略
- Grace: "abc" 非数字 → 已忽略

有效记录共 5 条：Alice(95), Bob(60), Cindy(88), David(41), Eva(86)
