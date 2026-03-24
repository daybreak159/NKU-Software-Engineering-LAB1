# 执行记录：创建统计脚本并运行

## 用户指令

请在 <测试目录> 中创建一个 Python 脚本 stats.py，用来统计 <测试目录>/data 目录下所有 txt 文件的以下信息：

1. 文件数量
2. 总行数
3. 总字数
4. 出现频率最高的 5 个词

然后运行这个脚本，并把输出保存为 <测试目录>/stats.txt。

要求：
- 脚本内容尽量简洁
- 如果运行失败，请先排查并修复
- 最后告诉我：
  1. 脚本路径
  2. 输出文件路径
  3. 运行是否成功

---

## 执行过程

### 步骤 1：创建 stats.py 脚本

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计 data 目录下所有 txt 文件的信息"""

import os
import re
from collections import Counter

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

file_count = 0
total_lines = 0
total_chars = 0
word_counter = Counter()

for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(data_dir, filename)
        file_count += 1

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        total_lines += len(lines)
        total_chars += len(content.replace(" ", "").replace("\n", ""))

        # 提取中文词（连续汉字）和英文词
        words = re.findall(r"[\u4e00-\u9fa5]+|[a-zA-Z]+", content)
        word_counter.update(words)

top5 = word_counter.most_common(5)

print("=== 统计结果 ===")
print(f"文件数量: {file_count}")
print(f"总行数: {total_lines}")
print(f"总字数: {total_chars}")
print("出现频率最高的 5 个词:")
for word, count in top5:
    print(f"  {word}: {count} 次")
```

### 步骤 2：运行脚本

```bash
cd /home/wsy/claude && python3 stats.py > stats.txt 2>&1
```

**运行结果：SUCCESS**

---

## 运行输出

```
=== 统计结果 ===
文件数量: 3
总行数: 14
总字数: 115
出现频率最高的 5 个词:
  任务: 3 次
  工具: 2 次
  记忆: 2 次
  上下文: 2 次
  管理: 2 次
```

---

## 最终报告

| 项目 | 结果 |
|------|------|
| 脚本路径 | `/home/wsy/claude/stats.py` |
| 输出文件路径 | `/home/wsy/claude/stats.txt` |
| 运行是否成功 | ✅ 成功 |

---

## 备注

- 脚本使用正则表达式提取中文连续字符和英文单词
- 由于中文分词较复杂，高频词统计结果为连续汉字片段，非精确词语
- 如需更精确的中文分词，可引入 jieba 等分词库
