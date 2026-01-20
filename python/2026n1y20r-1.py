import re

# 1. 找数字
text = "我25岁"
result = re.search(r'\d+', text)
print(f"找到：{result.group()}")  # 输出：25

# 2. 找所有数字
text = "1个苹果、2个香蕉、3个橙子"
numbers = re.findall(r'\d+', text)
print(f"所有数字：{numbers}")  # 输出：['1', '2', '3']

# 3. 替换
text = "我的电话13812345678"
new_text = re.sub(r'\d', '*', text)
print(f"替换后：{new_text}")  # 输出：我的电话**********

# 4. 提取括号里的数据
text = "年龄是25岁"
match = re.search(r'年龄是(\d+)', text)
print(f"年龄：{match.group(1)}")  # 输出：25
