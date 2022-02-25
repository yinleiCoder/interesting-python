"""
asyncio模拟http请求：
    asyncio没有提供http协议的接口。

"""

import asyncio
import socket
from urllib.parse import urlparse

async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_lines.append(data)
    return "\n".join(all_lines)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    for url in range(20):
        url = "https://www.github.com/{}".format(url)
        tasks.append(asyncio.ensure_future(get_url(url)))
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print(task.result())