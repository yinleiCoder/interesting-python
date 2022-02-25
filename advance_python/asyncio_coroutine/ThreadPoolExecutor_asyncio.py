"""
线程池ThreadPoolExecutor + asyncio完成阻塞IO请求:
    协程是单线程，那为什么要结合多线程。
    asyncio是异步编程的解决方案。异步io是包含了协程、多线程、多进程。
    所以，协程里也是可以使用多线程的。

使用多线程：
    在协程中强行集成阻塞io

这里的示例是socket阻塞IO进行网络请求。
"""
from concurrent.futures import ThreadPoolExecutor

import asyncio
import socket
from urllib.parse import urlparse

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    print(data)
    client.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for url in range(20):
        url = "https://www.baidu.com/{}/".format(url)
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

