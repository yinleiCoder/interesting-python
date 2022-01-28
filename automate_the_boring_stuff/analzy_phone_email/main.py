import pyperclip, re
"""
电话号码和E-mail地址提取(模式匹配与正则表达式):
    要在一篇长的网页或者文章何总，找出所有的电话号码和email。
    如果手动翻页，可能需要查找很长时间，
    如果有一个程序，可以在剪贴板的文本中查找电话号码和E-mail地址，那么就只要按ctrl+A选择所有文本，然后ctrl+c复制到剪贴板，
    然后运行程序就会用找到的电话号码和E-mail地址替换掉剪贴板中的文本。
    测试数据：
        i am yinlei, i like coding, i want to become coding master. 
        you can concat with me by (0816)137-9595-0539. on the other way, you also can email to me,
        there is my email address: 1099129793@qq.com
    测试结果：
        Copied to clipboard.
        (0816)-137-9595-0539
        1099129793@qq.com
代码分析：
    1. 使用pyperclip模块复制和粘贴字符串
    2. 创建2个正则表达式
    3. 对2个正则表达式找到所有的匹配，而不只是第一次匹配
    4. 将匹配的字符串整理好格式放在一个字符串中，用于粘贴
    5. 如果文本没有找到匹配，则显示某种消息
Usage: pyhon main.py

应用扩展：
    1. 考虑寻找网站的URL，以http://或https://开始
    2. 考虑整理不同日期格式的日期(如3/14/2015、03-14-2015、2015/3/14), 用唯一的标准格式替代
    3. 考虑删除敏感的信息，如web app 中替换掉用户的真实姓名
    4. 考虑寻找常见打字错误，如单词间的多个空格、不小心重复的单词或句子末尾处多出的感叹号 (替换可以考虑sub()方法)
"""
phoneRegex = re.compile(r"""(
    (\d{4}|\(\d{4}\))? #区号非贪婪匹配
    (\s|-|\.)? #分割符
    (\d{3}) # 前3个数字
    (\s|-|\.)? #分割符
    (\d{4}) # 中间4个数字
    (\s|-|\.) #分割符
    (\d{4}) # 最后4个数字
)""", re.VERBOSE)

emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+ #@前面的部分
    @ # @符号
    [a-zA-Z0-9]+ #域名
    (\.[a-zA-Z]{2,4}) # .com或者其他
)""", re.VERBOSE)

# 从剪贴板取得文本
match_results = []
text_from_clipboard = str(pyperclip.paste())

# 找出文本中所有的电话号码和E-mail地址
for groups in phoneRegex.findall(text_from_clipboard):# 因为正则表达式中分组了的，所以findall返回的是包含元组的列表
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    match_results.append(phoneNum)
for groups in emailRegex.findall(text_from_clipboard):
    match_results.append(groups[0])# 分组0表示整个正则表达式

# 将他们粘贴到剪贴板
if len(match_results) > 0:
    pyperclip.copy('\n'.join(match_results))
    print('Copied to clipboard.')
    print('\n'.join(match_results))
else:
    print("No phone numbers or email addresses found.")