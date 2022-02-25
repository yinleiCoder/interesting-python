"""
task取消和协程嵌套：
    loop会被放到future中
    取消future(task)

    子协程调度请查阅官网文档。重点在Task与嵌套的子协程直接建立双通道。
    协程done就触发StopIteration，被yield from捕捉到。
"""

import asyncio
import time

"""loop = asyncio.get_event_loop()
loop.run_forever()
# loop.run_until_complete()"""

async def get_html(sleep_times):
    print('waiting')
    await asyncio.sleep(sleep_times)
    print(f'done after {sleep_times}s.')

if __name__ == '__main__':
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)
    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
