"""
进程间通信——Queue Pipe Manager
    用queue包下的Queue,则TypeError: cannot pickle '_thread.lock' object
    应该用multiprocessing包下的Queue

    共享全局变量不能适用于多进程编程。【操作系统】

    multiprocessing包下的Queue不能用于pool进程池, 用Manager().Queue()

    Pipe是简化版的Queue, pipe只能适用于2个进程
    pipe的性能高于Queue

    可以使用Manager类完成进程间的数据共享
"""
import time
from multiprocessing import Process, Queue, Pipe
# from queue import Queue

def producer(queue):
    queue.put('a')
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == '__main__':
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue, ))
    my_consumer = Process(target=consumer, args=(queue, ))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

    # receive_pipe, send_pipe = Pipe()
