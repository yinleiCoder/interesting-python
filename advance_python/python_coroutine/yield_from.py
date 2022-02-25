"""
生成器进阶：send close throw
         (yield from)python3.3新加

yield from iterable
"""
from itertools import chain

"""my_list = [1, 2, 3]
my_dict = {
    'yinlei1': "http://github.com",
    'yinlei2': "http://github2.com",
}
def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value

for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)
    """

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)# range(0, 10)
#
# for value in g2(range(10)):
#     """
#         0
#         1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#     """
#     print(value)

def g1(gen):
    yield from gen
# 1. main调用方  g1委托生成器 gen子生成器
# 2. yield from会在调用方与子生成器之间建立一个双向通道
# yield from 还帮我们处理了StopIteration
def main():
    g = g1()
    g.send(None)
