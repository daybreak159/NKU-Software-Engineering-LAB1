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
