import time, subprocess
"""
倒计时程序：
    1.从60倒数
    2.倒数到0时播放声音文件
"""

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['start', 'U_MakeMe.mp3'], shell=True)