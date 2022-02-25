"""
call_soon call_at call_later call_soon_threadsafe:


call_soon：立即运行(下一次loop)
call_later: 指定时间运行
call_at: 指定时间运行(loop里的单调时间)
call_soon_threadsafe：和call_soon一样。但线程安全
"""

import asyncio

# 普通函数
def callback(sleep_times):
    print(f'sleep {sleep_times} success.')

# 停止loop
def stop_loop(loop):
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()# 内部时钟时间
    loop.call_later(now+2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()