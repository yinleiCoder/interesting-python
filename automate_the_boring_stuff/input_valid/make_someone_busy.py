import pyinputplus as pyip
"""
如何让人忙几小时：
    1. 询问用户是否想知道如何让人忙几小时
    2. 如果用户回答no, 退出
    3. 如果用户回答yes, 转到步骤1
    当然，我们不知道用户是否会输入yes no以外的内容，因此我们需要执行输入验证。
    用户也可以输入y n而不用输入完整的单词。
Usage: python make_someone_busy.py 
"""

while True:
    prompt = 'Want to know how to keep a person busy for hours?\n'
    # pyip.inputYesNo()保证仅返回字符串yes no
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')