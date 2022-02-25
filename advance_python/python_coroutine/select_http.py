"""
select+回调+事件循环 完成http请求：

回调之痛：（可读性、共享状态管理困难、异常处理困难）
    如果回调函数执行不正常该如何？
    如果回调嵌套回调如何
    如果嵌套了很多层，其中某个环境出错了会造成什么后果
    如果由个数据需要被每个回调都处理该怎么办？
    怎么使用当前函数中的局部变量？

为了保持同步编程的写法+回调，于是协程登场。
"""
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
# import select

selector = DefaultSelector()
urls = []
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf8')
            print(data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == '':
            self.path = '/'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as ex:
            pass
        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

def loop():
    # 事件循环，并不停的请求socket状态并调用对应的回调函数
    # select本身是不支持register模式
    # socket状态变化以后的回调由程序员完成
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    for url in range(20):
        url = "https://www.baidu.com/{}".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()