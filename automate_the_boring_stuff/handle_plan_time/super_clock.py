import time
"""
超级秒表:
    假设要记录在没有自动化的繁琐任务上花了多少时间。你又没有物理秒表，要为计算机或智能手机找到一个免费的、没有广告且不会将你的浏览
    历史发送给市场营销人员的秒表应用。可以自己写一个简单的秒表程序.
    1. 记录从按回车键开始每次按键的时间，每次按键都是一个新的“单圈”
    2. 输出圈数、总时间、单圈时间
"""

input('Please ENETER to begin. Afterward, press ENTER to "click" the stopwatch. Please Ctrl-C to quit.')
print('Started!')
startTime = time.time()
lastTime = startTime
lapNum = 1

# 开始并记录单圈时间
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone!')
