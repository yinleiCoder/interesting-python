"""
python中的常见内置类型：
    对象的3个特征：身份(id())、类型、值
    常见的内置类型：
        None(全局只有一个)
        数值类型(int float complex bool)
        迭代类型(迭代器与生成器)
        序列类型(list bytes bytearray memoryview range tuple str array)
        映射dict类型
        集合类型(set frozenset)
        上下文管理类型(with)
        其他(模块类型、class和实例、函数类型、方法类型、代码类型、obejct对象、type类型、ellipsis类型、notimplemented类型)
"""

# 身份(地址)
a = 24
print(id(a))

b = None
c = None
print(id(b) == id(c))# True