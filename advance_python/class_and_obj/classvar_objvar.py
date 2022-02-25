"""
类变量、实例变量(对象变量)：
    这个要理解作用域及作用域的查找顺序
"""
class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 24
a.aa = 100
print(a.x, a.y, a.aa)
print(A.aa)
print(A.x)# A has not attribute x


