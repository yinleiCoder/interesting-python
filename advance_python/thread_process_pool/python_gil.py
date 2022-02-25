"""
python中的GIL: global interpreter lock(cpython)
    python中一个线程对应c语言中的一个线程
    gil使得同一时刻只有一个线程在一个cpu上执行字节码,无法将多个线程映射到多个CPU上。
    所以无法利用多核优势

    由下面代码可以知道，GIL会在适当的时候释放。
    GIL会根据执行的字节码行数和时间片释放.
    GIL在遇到IO操作时主动释放。
"""
import threading
# 字节码
# import dis
#
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)