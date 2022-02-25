"""
python3.5后原生的协程：
    python为了将语义更明确，就引入async await 来定义原生的协程
    await后跟的是Awaitable对象
"""

from collections import Awaitable

async def downloader(url):
    return "yinlei"

import types
@types.coroutine
def downloader2(url):
    yield "yinlei"

async def download_url(url):
    # yield 1 (x)这是为了加强原生协程与生成器的区别
    html = await downloader(url)
    return html

if __name__ == '__main__':
    coro = download_url('https://github.com')
    coro.send(None)
