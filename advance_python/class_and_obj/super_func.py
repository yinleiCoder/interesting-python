"""
super调用的真是父类吗：
    调用父类的init是因为像多线程类，很多参数需要写，而父类有，从而重用代码。
    super()调用的是父类的构造函数(x)
    牵扯到MRO，所以，调用的是MRO顺序下一个类的构造函数
    __mro__
"""
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        # super(B, self).__init__()# python2的写法
        super().__init__()# python3的写法

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()

if __name__ == '__main__':
    d = D()# D B C A
