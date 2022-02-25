"""
python的协程：

C10M问题：如何利用8核心CPU、64G内存，在10gbps的网络上保持1000万并发连接。

回调模式编码复杂度高、同步编程的并发性不高、多线程编程需要线程间同步lock降低了并发性能。
所以，采用同步的方式去编写异步的代码，使用单线程去切换任务。
    1. 线程由操作系统切换，单线程切换意味着我们需要程序员自己去调度任务
    2. 不再需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高。

协程，
"""

# def get_url(url):
#     # do something
#     html = get_html(url)# 此处暂停，切换到另一个函数去执行
#     urls = parse_url(html)
#
# def get_url2(url):
#     # do something
#     html = get_html(url)# 此处暂停，切换到另一个函数去执行
#     urls = parse_url(html)

# 即我们需要一个可暂停的函数，并在适当时候恢复该函数继续执行
# 所以出现了协程，即可以暂停的函数，可以向暂停的地方传入值。

# 生成器可以暂停
def gen_func():
    # 1. 可以产出值 2. 可以接收值(调用方传递进来的值)
    html = yield "https://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return 'yinlei'

# 1. 生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)# gen.send(None)
    # gen.close()
    # gen.throw(Exception, 'download error') # 需要自己处理异常
    # download url
    html = "yinlei2"
    print(gen.send(html)) # send传递值进入生成器内部，同时可以重启生成器执行到下一个next
    # 1.启动生成器方式2种：next() send()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
