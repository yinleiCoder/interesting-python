"""
ThreadPoolExecutor线程池：
    futures可以让多线程和多进程编码接口一致
    Future贯穿异步编程的核心
"""

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
import time

# 线程池
def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit提交执行的函数到线程池, 是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))


# 获取已经成功的task
urls = [3, 2, 4]
all_tasks = [executor.submit(get_html, (url)) for url in urls]
wait(all_tasks, return_when=FIRST_COMPLETED)
print("main ")
for future in as_completed(all_tasks):
    data = future.result()
    print('get page {} success'.format(data))

# 另一个方法获取已经完成的task
for data in executor.map(get_html, urls):
    print('get page {} success'.format(data))


"""# done用判定某个任务是否完成
print(task1.done())
print(task2.cancel())# 执行中无法取消
time.sleep(3)
print(task1.done())
# result可以获取task的执行结果
print(task1.result())"""


