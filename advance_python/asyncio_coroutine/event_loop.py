"""
异步编程3要素：
事件循环 + 回调(驱动生成器/协程) + epoll(IO多路复用)

asyncio: 之前的协程脱离事件循环意义不大。协程需要搭配事件循环发出它的最大功能
    异步io的库，解决异步io中遇到的所有问题，包括多线程、多进程、协程。
    包含各种特定系统实现的模块化事件循环
    传输和协议抽象
    对TCP UDP SSL 子进程 延时调用及其他的具体支持
    模仿futures模块但适用于事件循环使用的Future类
    基于yield from的协议和任务，可以让我们用顺序的方式编写并发代码
    必须使用一个将产生阻塞IO的调用时，有接口可以把这个事件转移到线程池
    模仿threading模块中的同步原语、可以用在单线程内的协程之间

asyncio是python用于解决异步io编程的一整套解决方案。
partial可以将函数包装为另一个函数，以便解决add_done_callback固定参数future

asyncio中的gather、wait的区别：
gather更加高层，还可以将task进行分组
group1, group2 =[], []
loop.run_until_complete(asyncio.gather(*group1, *group2))
"""
import asyncio
import time
from functools import partial

async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')
    return "yinlei"

def callback(url, future):
    print(url)
    print('send email to yinlei')

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html('https://www.baidu.com'))
    task = loop.create_task(get_html('https://www.baidu.com'))
    task.add_done_callback(partial(callback, 'https://www.github.com'))
    loop.run_until_complete(task)
    print(task.result())

    # tasks = [get_html('https://www.baidu.com') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))# asyncio.gather(*tasks)
    # loop.run_until_complete(get_html('https://www.baidu.com'))
    print(time.time() - start_time)