import pyautogui
import time
import subprocess
"""
用GUI自动化控制键盘和鼠标:
    处理电子表格、运行程序有各种python模块。但也有时候没有相关模块对应你要操作的应用程序。
    在计算机上的终极自动化任务，就是写程序直接控制键盘和鼠标。这些程序可以控制其他应用，向他们发送虚拟按键和鼠标点击事件。
    GUI自动化，我们的程序就像一个用户坐在计算机前一样，能做任何事情。
    一些公司销售的创新的“自动化解决方案”，通常被称为“机器人过程自动化RPA”，这些产品和用pyautogui模块制作的python脚本没什么区别。
    对于linux,需要先安装一些pyautogui依赖的软件。
    对于macos,需要将脚本设置为无障碍应用程序。
    若程序出错，想停止程序，可以考虑：
        1. 暂停和自动防故障装置(pyautogui的故障安全功能，快速将鼠标指针滑动到屏幕的4个角之一，每个pyautogui函数调用在执行动作后都有1/10秒的延迟)
        2. 通过注销关闭所有程序(Ctrl-Alt-Delete或Command-Shift-Option-Q)

pyautogui: pip install pyautogui
pyautogui docs: https://pyautogui.readthedocs.io/en/latest/#
"""

if __name__ == '__main__':
    # 屏幕分辨率
    wh = pyautogui.size()
    print(wh)
    print(wh[0])
    print(wh.width)

    # 移动鼠标指针
    # for i in range(10):
    #     pyautogui.moveTo(100, 100, duration=0.25)
    #     pyautogui.moveTo(200, 100, duration=0.25)
    #     pyautogui.moveTo(200, 200, duration=0.25)
    #     pyautogui.moveTo(100, 200, duration=0.25)
        # move是相对于当前的位置
        # pyautogui.move(100, 0, duration=0.25)# right
        # pyautogui.move(0, 100, duration=0.25)# down
        # pyautogui.move(-100, 0, duration=0.25)# left
        # pyautogui.move(0, -100, duration=0.25)# up

    # 获取鼠标指针位置
    print(pyautogui.position())

    # 控制鼠标交互
    # 1. 单击鼠标
    # pyautogui.click(80, 200, button='left')# 等同于mouseDown+mouseUp, 还可以doubleClick双击 rightClick右键 middleClick中键
    # pyautogui.click(80, 200, button='right')
    # 2. 拖动鼠标
    # subprocess.Popen(r'C:\Program Files\WindowsApps\Microsoft.Paint_11.2203.2.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe')
    # time.sleep(5)# 5秒内手动选中mspaint.exe中的画笔工具并停留在窗口上
    # pyautogui.click()# click to make the window active
    # distance = 300
    # change = 20
    # while distance > 0:
    #     pyautogui.drag(distance, 0, duration=0.5)# right
    #     distance -= change
    #     pyautogui.drag(0, distance, duration=0.5)# down
    #     pyautogui.drag(-distance, 0, duration=0.5)# left
    #     distance -= change
    #     pyautogui.drag(0, -distance, duration=0.5)# up

    # 3. 滚动鼠标
    # pyautogui.scroll(200)

    # 规划鼠标运动(找到想单击的地方的x和y坐标)
    # pyautogui.mouseInfo()

    # 处理屏幕
    im = pyautogui.screenshot()# 获取屏幕快照
    print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))# 获取鼠标当前位置处的像素颜色
    print(pyautogui.pixelMatchesColor(pyautogui.position().x, pyautogui.position().y, (0, 0, 0)))# 获取鼠标当前位置处的像素颜色是否和给定的颜色匹配

    # 图像识别(像pyautogui提供希望单击的图像，让它去弄清楚坐标)
    try:
        locate_box = pyautogui.locateOnScreen('wechat.png')
        # pyautogui.click((locate_box.left, locate_box.top, locate_box.width, locate_box.height))
        # pyautogui.doubleClick('wechat.png')
    except:
        print('image could not be found.')

    # 获取窗口信息(找到屏幕上某个特定窗口的位置)
    fw = pyautogui.getActiveWindow()# 获取活动窗口
    print(fw)
    print(str(fw))
    print(fw.title)
    print(fw.size)
    print(fw.left, fw.top, fw.right, fw.bottom)
    print(fw.topleft)
    print(fw.area)
    pyautogui.getAllWindows()# 屏幕上所有可见窗口的window对象列表
    pyautogui.getWindowsAt(100, 100)# 返回所有包含点(100, 100)的可见窗口的window对象列表
    pyautogui.getWindowsWithTitle('demo.py')# 返回所有在标题栏中包含字符串title的可见窗口的window对象的列表
    pyautogui.getAllTitles()# 所有可见窗口的字符串列表

    # 操纵窗口
    fw.width = 1000
    fw.topleft = (800, 400)
    print(fw.isMaximized)
    print(fw.isMinimized)
    print(fw.isActive)
    time.sleep(3)
    fw.maximize()
    time.sleep(3)
    fw.minimize()
    time.sleep(3)
    fw.restore()
    time.sleep(5)
    fw.activate()
    # fw.close()

    # 控制键盘
    pyautogui.click()
    pyautogui.write('Hello World!', 0.25)# 通过键盘发送一个字符串
    # 键名
    pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])
    print(pyautogui.KEYBOARD_KEYS)
    # 按下和释放键盘按键
    pyautogui.keyDown('shift')
    pyautogui.press('4')
    pyautogui.keyUp('shift')
    # 快捷键组合
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.countdown(3)
    # 显示消息框
    pyautogui.alert('this is a message', 'Important')
    pyautogui.confirm('Do you want to continue?')
    pyautogui.prompt("what is your cat's name?")
    pyautogui.password('what is the password?')






