import pyperclip
"""
在Wiki标记中添加无序列表:
    在编辑一篇维基百科的文章时，可以创建一个无序列表。
    即让每个表项占据一行，并在前面放置一个星号。
    假设有一个非常大的列表，希望在前面添加星号，可以用一小段python脚本自动化这个任务。
    
    (这里假定从剪贴板中取得文本，并在每一行开始处加上星号和空格,再将这段新的文本贴回剪贴板。)
    测试文本：
        我喜欢陈爽
        我喜欢过赵权芳
    测试结果：
        * 我喜欢陈爽
        * 我喜欢过赵权芳
Usage: python main.py
"""

# 从剪贴板中复制和粘贴
text_from_clipbord = pyperclip.paste()

# 逻辑处理: 分离文本中的行，并添加星号
lines = text_from_clipbord.split('\n')
for i in range(len(lines)):
    lines[i] = f'* {lines[i]}'
text_from_clipbord = '\n'.join(lines)

# 将新的文本复制到剪贴板
pyperclip.copy(text_from_clipbord)
