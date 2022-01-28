import random
"""
生成随机的测试试卷：
    假设你是一位老师，班上有xx名学生，你希望进行关于xx主题的小测验。不妙的是，你无法确保学生不会作弊。
    你希望随机调整问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭答案。
    当然，手动完成这件事显然费时费力。
    1. 创建5份不同的测验试卷
    2. 为每份试卷创建10个选择题，次序随机
    3. 为每个问题提供一个正确答案和3个随机的错误答案，次序随机
    4. 将测验试卷写到5个文本文件中
    5. 将答案写到5个文本文件中
Usage: python gen_random_test_paper.py
"""
# 将测验数据保存在一个字典中
workmates = {
    '绵阳市总经理': "许东",
    '绵阳市网络部经理': "龙武红",
    '绵阳市人力部经理': "秦勇",
    '绵阳市涪城区总经理': "陈玲霞",
    '绵阳市涪城区建维中心主任': "曾子元",
    '绵阳市游仙区总经理': "宋红瑞",
    '绵阳市涪城区政企主管': "张娇",
    '绵阳市渠道中心员工': "余海娇",
    '绵阳市江油市建维中心员工': "王福凌",
    '绵阳市财务部员工': "杨倩",
}
for quizNum in range(5):
    # 创建测验文件，并打乱问题的次序
    quizFile = open(f'ChinaUnicom{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'ChinaUnicom_answers{quizNum + 1}.txt', 'w')
    # 创建测验标题，让答卷人填写
    quizFile.write(''*20 + f'中国联通绵阳分公司调查问卷(试卷{quizNum + 1})')
    quizFile.write('\n\n')
    # 打乱问题排序
    stuffs = list(workmates.keys())
    random.shuffle(stuffs)
    # 创建每套问卷的答案选项
    for questionNum in range(10):
        correctAnswer = workmates[stuffs[questionNum]]
        wrongAnswers = list(workmates.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # 将内容写入测验试卷和答案文件中
        quizFile.write(f'{questionNum + 1}. {stuffs[questionNum]}是下面中的哪一个?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()