"""
使用多剪贴板自动回复消息

Usage: 打开Terminal, 进入该路径下，输入python main.py 命令行参数。
如： python main.py agree
然后再选择ctrl + v粘贴试试。
"""

# 程序设计和数据结构：字典
TEXT = {'agree': """Yes, i agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# 处理命令行参数
import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage: python main.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

# 复制正确的短语
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}")


