# ========== re 模块零基础学习 ==========

import re

print("=" * 50)
print("第1课：最简单的查找 - search()")
print("=" * 50)

# 例子1：在文本中找一个数字
text = "我叫小王，今年25岁"
result = re.search(r'\d', text)  # \d 表示找一个数字
print(f"文本：{text}")
print(f"找到的第一个数字：{result.group()}")
print()

# 例子2：在文本中找一个邮箱
text2 = "请发送至 zhangsan@qq.com"
result2 = re.search(r'\w+@\w+\.\w+', text2)  # 简单的邮箱模式
print(f"文本：{text2}")
print(f"找到的邮箱：{result2.group()}")
print()

print("=" * 50)
print("第2课：找出所有匹配项 - findall()")
print("=" * 50)

# 例子3：找出文本中所有的数字
text3 = "我买了3个苹果、5个香蕉、10个橙子"
numbers = re.findall(r'\d+', text3)  # \d+ 表示找连续的数字
print(f"文本：{text3}")
print(f"找到的所有数字：{numbers}")
print()

# 例子4：找出所有的单词
text4 = "apple banana cherry"
words = re.findall(r'\w+', text4)
print(f"文本：{text4}")
print(f"找到的所有单词：{words}")
print()

print("=" * 50)
print("第3课：替换文本 - sub()")
print("=" * 50)

# 例子5：把所有数字替换成 *
text5 = "我的身份证是 123456789"
new_text = re.sub(r'\d', '*', text5)  # 把所有数字换成 *
print(f"原文本：{text5}")
print(f"替换后：{new_text}")
print()

# 例子6：把所有数字替换成 X
text6 = "我的电话：13812345678"
new_text2 = re.sub(r'\d', 'X', text6)
print(f"原文本：{text6}")
print(f"替换后：{new_text2}")
print()

print("=" * 50)
print("第4课：提取括号里的数据 - group()")
print("=" * 50)

# 例子7：提取括号内的内容
text7 = "小王的年龄是25岁"
match = re.search(r'年龄是(\d+)', text7)  # () 表示要提取的部分
print(f"文本：{text7}")
print(f"提取的年龄：{match.group(1)}")
print()

# 例子8：同时提取多个数据
text8 = "用户名：张三，年龄：30"
match2 = re.search(r'用户名：(\w+)，年龄：(\d+)', text8)
print(f"文本：{text8}")
print(f"用户名：{match2.group(1)}")
print(f"年龄：{match2.group(2)}")
print()

print("=" * 50)
print("常用符号速查表")
print("=" * 50)
print(r"\d          = 任意数字 (0-9)")
print(r"\w          = 任意字母、数字、下划线")
print(r"\s          = 空格、制表符、换行符")
print(r"+           = 1个或多个")
print(r"*           = 0个或多个")
print(r"?           = 0个或1个")
print(r".           = 任意字符（除了换行）")
print(r"[abc]       = 只能是 a 或 b 或 c")
print(r"[0-9]       = 数字 0 到 9")
print(r"[a-z]       = 小写字母 a 到 z")
print(r"()          = 括号内的作为一个整体，可以用 group() 提取")
print()

print("现在运行这个文件，看看输出，就能理解 re 模块了！")
