"""
python中序列类型的abc继承关系：
    __all__ = ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
            'UserString', 'Counter', 'OrderedDict', 'ChainMap']

    _collections_abc.Sequence

    _collections_abc.MutableSequence

    其中Sequence继承了Reversible Collection类，里面定义了魔法函数。
    而MutableSequence则是继承了Sequence。
"""
from collections import abc

