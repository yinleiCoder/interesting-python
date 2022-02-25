"""
生成器函数的使用：
    生成器函数，函数里只要有yield关键字。

"""

def gen_func():
    yield 1
    yield 2
    yield 3

def func():
    return 1

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1

if __name__ == '__main__':
    gen = gen_func()# 返回的是生成器对象，python编译字节码的时候就产生了。
    for value in gen:
        print(value)
    res = func()
    print(gen)
    print(res)

    print(fib(10))
    print(fib2(10))
    for data in gen_fib(10):
        print(data)