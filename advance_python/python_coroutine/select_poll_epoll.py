"""
IO多路复用——select poll epoll:

C10k问题：
    C10K是一个在1999年被提出来的技术挑战。
    如何在一颗1GHz CPU 2G内存 1gbps网络环境下，让单台服务器同时为1万个客户端提供FTP服务。

Unix中的5种I/O模型：
    阻塞式I/O
    非阻塞式I/O
    I/O复用
    信号驱动式I/O
    异步I/O(POSIX的aio_系列函数)

select, poll, epoll都是IO多路复用的机制。I/O多路复用就是通过一种机制，
一个进程可以监视多个描述符，一旦某个描述符就绪(一般是读就绪或写就绪)，能够
通知程序进行相应的读写操作。但select poll epoll本质上都是同步I/O。因为他们都需要
在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的，而异步I/O则无需自己负责进行
读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。

select函数监视的文件描述符分为：writefds readfds exceptfds。调用select函数会阻塞，
直到有描述符就绪(有数据可读、可写、有except)或者超时(timeout指定等待时间，如果立即返回设为null即可)，
函数返回。当select函数返回后，可以通过遍历fdset来找到就绪的描述符。select目前几乎在所有的平台上支持，
其良好跨平台支持也是它的一个优点。select的缺点是单个进程能够监视的文件描述符的数量存在最大限制，在linux上
一般为1024，可以通过修改宏定义甚至重新编译内核的方式提升这以限制，但这样会造成效率的降低。

select使用3个位图来表示是3个fdset的方式，poll使用一个pollfd的指针实现。
pollfd结构包含要监视的event和发生的event，不再使用select'参数-值'传递的方式。
同时，pollfd并没有最大数量限制(但数量过大后性能也会下降)。和select函数一样，poll返回后，需要
轮询pollfd来获取就绪的描述符。

select poll都需要在返回后，通过遍历文件描述符来获取已经就绪的socket。事实上，同时连接的大量客户端在一时刻可能只有很少的处于就绪状态，
因此随着监视的描述符数量的增长，其效率也会线性下降。

epoll在linux下支持，windows下不支持。在2.6内核中提出，是select poll的增强版本。相对于select poll来说，
epoll更加灵活，没有描述符限制。epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个事件表中，
这样在用户空间和内核空间的copy只需一次。
"""

# epoll 不代表一定比select好，高并发下，连接活跃度不是很高，epoll比select好
# 并发性不高，连接很活跃，select比epoll好

# 通过非阻塞io实现http请求
import socket
from urllib.parse import urlparse

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as ex:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
            break
        except OSError as e:
            pass
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    print(data)
    client.close()

if __name__ == '__main__':
    get_url("https://baidu.com")