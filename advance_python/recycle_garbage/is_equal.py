"""
is、==的区别：

"""

a = [1, 2, 3]
b = a
print(a is b)# True

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]# 赋值符号会重新声明对象
print(a is b)# False
print(a == b)# True
print(id(a), id(b))

a = 1
b = 1
print(id(a), id(b)) # 这里考虑常量池
print(a == b)# True
