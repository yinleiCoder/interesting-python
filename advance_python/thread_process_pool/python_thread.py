"""
多线程编程：
    对于IO操作而言，多线程、多进程性能差别不大

"""
import time
import threading
# 1. 通过Thread类实例化
def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')

def get_detail_url(url):
    print('get detail url started')
    time.sleep(2)
    print('get detail url end')

# 2. 通过继承Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html started')
        time.sleep(2)
        print('get detail html end')

class GetDetailURL(threading.Thread):
    def run(self):
        print('get detail url started')
        time.sleep(2)
        print('get detail url end')

if __name__ == '__main__':
    thread1 = GetDetailHtml('html')
    thread2 = GetDetailHtml('url')
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    # thread1.setDaemon(True)# 守护进程
    # thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('last time {}'.format(time.time() - start_time))


