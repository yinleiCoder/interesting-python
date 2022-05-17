import subprocess
"""
python启动其他程序:
    利用内置的subprocess模块中的Popen()，python可以启动计算机中的其他程序。
    Popen()含糊名中的P表示process，即进程。
    如果你打开了一个应用程序的多个实例，那么每个实例都是同一个程序的不同进程。
"""

notepadProc = subprocess.Popen(r'C:\Windows\notepad.exe')
print(notepadProc.poll() == None)
print(notepadProc.wait())
print(notepadProc.poll())

# 传递参数
subprocess.Popen([r'C:\Windows\notepad.exe', r'E:\PycharmProjects\funnyPython\automate_the_boring_stuff\handle_plan_time\demo.txt'])

# 用默认的应用程序打开文件windows start, macos open, linux see.
with open('demo.txt', 'w') as fileObj:
    fileObj.write('Hello, World!')
    subprocess.Popen(['start', 'demo.txt'], shell=True)

