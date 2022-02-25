"""
set、frozenset:
    frozenset——不可变集合
    集合无序，不重复
"""

a = set('yinlei')
a = set(['y', 'i', 'l'])
print(a)

a = {'a', 'b'}# set, 注意这里和dict的区分
print(type(a))
a.add('c')
print(a)

# frozenset, 可以作为dict的key
s = frozenset('yinlei')
print(s)

# set添加数据
one_set = set('yin')
another_set = set('lei')
one_set.update(another_set)
print(one_set)

# 求差集
print(one_set.difference(another_set))
print(one_set - another_set)
print(one_set & another_set)
print(one_set | another_set)

if 'y' in one_set:
    print('one_set contain yi')