"""
python中的迭代协议：
    迭代协议主要指的是迭代器。
    迭代器是访问集合内元素的一种方式，一般用来遍历数据。
    迭代器和以下标的访问方式不一样，迭代器是不能返回的。
    迭代器提供了一种惰性访问数据的方式。
    [] list, __iter__(Iterable)
    iterator: __next__

    list就实现了__iter__，所以它是可迭代对象，但并不是迭代器，未实现__next__
    Iterator继承自Iterable
"""

from collections.abc import Iterable, Iterator
a = [23, 24]# list
print(isinstance(a, Iterable))# True
print(isinstance(a, Iterator))# False