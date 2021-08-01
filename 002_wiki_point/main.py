"""
编译一篇维基百科的文章时，可以让每个表项占据一行，并在前面放置一个星号。
或者编写其他文章时需要添加非常大的列表，并在前面自动化添加星号。
本程序从剪贴板取得文本并在每一行开始处添加星号和空格，最后将新闻本贴回剪贴板

[扩展]：自动化删除每行末尾的空格或者其他操作
Usage:
先copy类似下面的话到剪贴板，然后运行本程序后再ctrl + v试试。
我爱王可尔
真的很爱很爱她
也很爱很爱赵权芳

Result:
* 我爱王可尔
* 真的很爱很爱她
* 也很爱很爱赵权芳
"""

# 从剪贴版中复制和粘贴
import pyperclip
text = pyperclip.paste()

# 分离文本中的行，并添加星号
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f'* {lines[i]}'

# 连接修改过的行
text = '\n'.join(lines)

pyperclip.copy(text)