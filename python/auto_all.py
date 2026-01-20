import os
from datetime import datetime
import re

def create_daily_file():
    """创建今日日期命名的Python文件，格式: YYYYnMMyCCr-X.py"""
    
    # 获取当前日期
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    
    # 生成文件名前缀
    prefix = f"{year}n{month}y{day}r"
    
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 查找已有的文件序号
    pattern = rf"^{re.escape(prefix)}-(\d+)\.py$"
    max_num = 0
    
    for filename in os.listdir(current_dir):
        match = re.match(pattern, filename)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)
    
    # 生成新文件名
    new_num = max_num + 1
    new_filename = f"{prefix}-{new_num}.py"
    new_filepath = os.path.join(current_dir, new_filename)
    
    # 创建文件
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write("")  # 创建空文件
    
    print(f"✓ 成功创建文件: {new_filename}")
    return new_filename

if __name__ == "__main__":
    create_daily_file()
