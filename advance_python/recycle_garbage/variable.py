"""
python中的变量是什么：
    python和java中的变量本质不一样。
    可把python中的变量实质上就是一个指针，类似于js中的变量。
    就像便利贴一样，那里需要往那里贴。
"""

a = 24
# a贴在24上面
# 先生成对象，然后贴便利贴

a = [1, 2, 3]
b = a
b.append(4)
print(a)

print(a is b)# True
print(id(a), id(b))


