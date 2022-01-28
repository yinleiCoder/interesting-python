import sys, pyperclip, shelve
"""
可更新的多重剪贴板：(shelve)
    如果你曾用类似的措辞回复大量的电子邮件，那么可能不得不完成很多重复的输入操作。
    也许你保留了包含这些措辞的文本文档，可以使用windows的剪贴板轻松的复制和粘贴他们。
    但你的剪贴板一次只能存储一封邮件，这不是很方便。
    使用存储多种措辞的程序，可以让这个过程更容易些。
    [update]: 用户现在可以保存新字符串，以便加载到剪贴板，而无须更改源代码
              利用一个关键字保存每段剪贴板文本。
              如当运行python multi_clipboard.py save yes，剪贴板中当前的内容就用关键字yes保存
              如当运行python multi_clipboard.py yes，这段文本稍后将重新加载到剪贴板中
              如用户忘记了都有哪些关键字，可以运行python multi_clipboard.py list,将所有关键字的列表复制到剪贴板中
    1. 针对要检查的关键字来提供命令行参数
    2. 如果参数是save，那么将剪贴板的内容保存到关键字
    3. 如果参数是list, 将所有的关键字复制到剪贴板
    4. 否则，就将关键字对应的文本复制到剪贴板
    
    测试数据：
        我爱陈爽
    结果：
    ['love']
    我爱陈爽
Usage:  python multi_clipboard.py save love
        python multi_clipboard.py list
        python multi_clipboard.py love
"""

# shelf设置
mcbShelf = shelve.open('mcb')
# 用一个关键字保存剪贴板内容
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # 列出关键字和加载关键字的内容
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
