import pyinputplus as pyip
import random, time
"""
定时的乘法测验：
    向用户提出10个乘法问题，其中有效的输入是问题的正确答案。
    PyinputPlus模块可以处理各种输入的函数，包括处理字符串、数字、日期、yes/no、True/False、电子邮件和文本的函数，甚至是自定义处理函数。
    而input()总是返回字符串，需要我们手动编写正则表达式和冗长的while循环来检查有效输入并提示用户。
"""

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num_one = random.randint(0, 9)
    num_two = random.randint(0, 9)
    prompt = f'第{questionNumber}道: {num_one} * {num_two} = '
    try:
        # 8秒有效时间，回答次数3次
        pyip.inputStr(prompt, allowRegexes=[f'^{num_one * num_two}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print(f'Score: {correctAnswers} / {numberOfQuestions}')