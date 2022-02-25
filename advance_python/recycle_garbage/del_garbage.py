"""
del语句、垃圾回收：
    python中的垃圾回收的算法采用的是引用计数
    cpython2.0中，是分代垃圾回收机制。
    这块可对比看看JVM中的垃圾回收怎么做的。

"""
a = object()
b = a
del a
print(b)
print(a)# NameError: name 'a' is not defined

class A:
    def __del__(self):
        pass
