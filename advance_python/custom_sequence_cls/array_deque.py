"""
什么时候不该使用列表：
    array, deque

    array是c语言中的数组，性能很高。
    array和list的一个重要区别就是array只能存放指定的数据类型。

    array指定类型：
        _IntTypeCode = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
        _FloatTypeCode = Literal["f", "d"]
        _UnicodeTypeCode = Literal["u"]
        _TypeCode = Union[_IntTypeCode, _FloatTypeCode, _UnicodeTypeCode]

        _T = TypeVar("_T", int, float, str)
"""

import array

my_array = array.array('i')
my_array.append(24)
my_array.append('yinlei')# 不行，指定了参数i为int类型，不能放入str  TypeError: an integer is required (got type str)
print(my_array)


