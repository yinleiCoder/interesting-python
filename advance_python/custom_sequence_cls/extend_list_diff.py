"""
序列的+ += extend的区别：

"""

a = [1, 2]
b = a + [3, 4]
print(b)
# c = b + (5, 6)# can only concatenate list (not "tuple") to list
# print(c)

# += 就地加, 可以为任意的序列类型，是通过__iadd__魔法函数，其内部还是调用了extend()
a += [3, 4]
print(a)

a += (5, 6)
print(a)

a.extend(range(3))
print(a)

a.append([22, 23])
print(a)

a.append((22, 23))
print(a)