"""
线程间通信——Queue消息队列:
    通过queue的方式进行线程间的通信与同步
    Queue本身就是线程安全的
"""
from queue import Queue

import time
import threading

def get_detail_html(queue):
    while True:
            url = queue.get()
            # for url in detail_url_list:
            # 文章详情页
            print('get detail html started')
            time.sleep(2)
            print('get detail html end')

def get_detail_url(queue):
    while True:
        # 文章列表页
        print('get detail url started')
        time.sleep(2)
        for i in range(20):
            queue.put("https://baidu.com/{id}".format(id=i))
        print('get detail url end')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()
    print('last time {}'.format(time.time() - start_time))

