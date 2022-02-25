"""
列表推导式、生成器表达式、字典推导式:
    列表生成式性能高于列表操作，如果过于复杂就考虑可读性
"""

# 列表生成式(推导式)
odd_list = []
for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)
# 以上代码可以用列表生成式一行代码完成
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)
print(type(odd_list))

# 如果逻辑复杂
odd_list_squre = [i**2 for i in range(21) if i % 2 == 1]
print(odd_list_squre)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1)
print(odd_gen)
print(type(odd_gen))
for item in odd_gen:
    print(item)

# 字典推导式
my_dict = {'yinlei': 23, 'yinwei': 22, "yinzihao": 6}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))# <class 'set'>
print(my_set)