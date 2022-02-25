"""
生成器是可以暂停的函数:
    协程的调度依然是 事件循环+协程模式，协程是单线程模式
    python3.5开始用原生协程，而不是生成器
"""
import inspect
def gen_func():
    value = yield from 1
    # 1. 返回值给调用方，2.调用方通过send返回值给gen，即上面的1是发送出去的，value是接受send进来的。
    return 'yinlei'

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))