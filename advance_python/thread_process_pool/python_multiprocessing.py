"""
python多进程编程：multiprocessing
    multiprocessing比ProcessPoolExecutor更底层
"""
import os, time

# fork只能用于linux/unix
# pid = os.fork()
# print('yinlei')
# if pid == 0:
#     print('child process: [}, parent process: {}'.format(os.getpid(), os.getppid()))
# else:
#     print('i am parent process: {}'.format(pid))
#
# time.sleep(2)

from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def get_html(n):
    time.sleep(n)
    print('sub process success')
    return n

class MyProcess(multiprocessing.Process):
    def run(self) -> None: pass

if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2,))
    print(process.pid)
    process.start()
    print(process.pid)
    process.join()
    print('main process end')

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3, ))
    # 等所有任务完成
    pool.close()
    pool.join()
    print(result.get())
    # imap
    for result in pool.imap(get_html, [1, 4, 3]):
        print('{} sleep success'.format(result))
