"""
python中一切皆对象：
    python的面向对象比java更彻底。【动态语言和静态语言的区别】
    python一切皆对象的理念是python语言灵活的根本。
    python中的class也是对象，函数也是对象，代码和模块也是对象。
    python中的函数和类是对象，属于python的一等公民：
        1. 赋值给一个变量
        2. 可以添加到集合对象中
        3. 可以作为参数传递给函数
        4. 可以当作函数的返回值
"""
# 赋值给一个变量
def ask(name="yinlei"):
    print(name)

class Person:
    def __init__(self):
        print("yinlei_class")

my_func = ask
my_func("yinleiCoder")
my_class = Person
my_class()

# 可以添加到集合对象中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())

# 可以当作函数的返回值
def decorator_func():
    print("decorator ask")
    return ask
my_func_ret = decorator_func()
my_func_ret()