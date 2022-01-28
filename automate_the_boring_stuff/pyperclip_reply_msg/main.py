import sys, pyperclip
"""
使用多剪贴板自动回复消息：
    如果你曾用类似的措辞回复大量的电子邮件，那么可能不得不完成很多重复的输入操作。
    也许你保留了包含这些措辞的文本文档，可以使用windows的剪贴板轻松的复制和粘贴他们。
    但你的剪贴板一次只能存储一封邮件，这不是很方便。
    使用存储多种措辞的程序，可以让这个过程更容易些。

Usage: 运行mclip.bat批处理文件。cmd输入mclip busy或者python main.py busy，然后看到提示就可以粘贴了
Yes, I agree. That sounds fine to me.
"""

# 程序设计和数据结构
TEXT_DIC = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy':  "Sorry, can we do this later this week or next week?",
}

# 处理命令行参数
if len(sys.argv) < 2:
    print(f'Usage: python {sys.argv[0]} [keyphrase] copy phrase text.')
    sys.exit()

keyphrase = sys.argv[1]

# 赋值正确的语句
if keyphrase in TEXT_DIC:
    pyperclip.copy(TEXT_DIC[keyphrase])
    print(f'Text for: {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}')

