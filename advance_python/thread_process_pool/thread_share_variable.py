"""
线程间通信——共享变量:
    共享变量，即全局变量。
    但是不安全，可以加锁解决这个问题。
"""

import time
import threading

detail_url_list = []# 共享变量
def get_detail_html(detail_url_list):
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            # 文章详情页
            print('get detail html started')
            time.sleep(2)
            print('get detail html end')

def get_detail_url(detail_url_list):
    while True:
        # 文章列表页
        print('get detail url started')
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("https://baidu.com/{id}".format(id=i))
        print('get detail url end')


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
    start_time = time.time()
    print('last time {}'.format(time.time() - start_time))

