"""
类属性、实例属性的查找循序（mro查找）:
    D           E
    |           |
    |           |
    B           C
    \           /
     \         /
      \       /
        A

DFS: A B D C E
BFS: A B C D E(x)

          D
        /   \
       /     \
      B       C
      \      /
        \   /
          A
DFS: A B D C(x)
BFS: A B C D

所以，现在统一为C3属性查找算法。
"""
class A:
    name = "A"
    # def __init__(self):
    #     self.name = "obj"

a = A()
print(a.name)

# 以菱形继承为例
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)# 属性查找顺序,python3以后为新式类，默认都会继承object