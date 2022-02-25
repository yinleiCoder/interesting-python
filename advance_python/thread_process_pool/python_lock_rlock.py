"""
线程同步——Lock RLock：
    用锁会影响性能、引起死锁
    RLock，在同一个线程里面，可连续调用多次acquire, 一定要注定acquire的次数和release的次数相同
"""
import threading
from threading import Lock

total = 0
lock = Lock()
def add(lock):
    global total
    for i in range(1000000):
        lock.acquire()
        dosomething(lock)
        # lock.acquire()# 造成死锁
        total += 1
        lock.release()

def dosomething(lock):
    lock.acquire()# 也会造成死锁,为了解决这个问题，用可重入的锁RLock
    lock.release()

def desc(lock):
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

thread1 = threading.Thread(target=add, args=(lock,))
thread2 = threading.Thread(target=desc, args=(lock,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)

"""
1. load a
2. load 1
3. + 
4. 赋值给a
"""
# def add1(a):
#     a += 1
# def desc1(a):
#     a -= 1
# import dis
# print(dis.dis(add1))
# print(dis.dis(desc1))