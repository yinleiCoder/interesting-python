"""
isinstance、type的区别:
    尽量使用isinstance而不是type去判断
    因为isinstance可以查找继承链，类似于js中的原型链
"""
class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, B))# 找继承链
print(isinstance(b, A))

print(type(b))
print(type(b) is B)# 判断id是否相同
print(type(b) == B)# 判断值是否相等

print(type(b) is A)# 不找继承链