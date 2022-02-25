"""
type、object、class之间的关系：
    type: 生成一个类(元类编程)、返回一个对象的类型
          type自身也是一个类，同时也是一个对象
          type->class->obj

    object：最顶层基类

    实例------|
    |        |
    |------type<-------实例------object<--
             |  -------继承------>       |
             |                    |     |
          实例                    继承   |
             |                    |     |
             |------------------list----|
             |                          |----实例----"yinlei"
             |------------------str-----|
             |                          |
             |------------------dict----|
             |                          |
             |------------------tuple---|

"""

a = 1
b = "abc"
print(type(1))# <class 'int'>
print(type(int))# <class 'type'>
# 以上，即type生成int,int生成1

class Student:
    pass
class MyStudent(Student):
    pass
stu = Student()
print(type(stu))# <class '__main__.Student'>
print(type(Student)) # <class 'type'>
print(Student.__base__) # <class 'object'>
print(MyStudent.__base__)# <class '__main__.Student'>

print(type.__base__) # <class 'object'>
print(type(object))# <class 'type'>
print(object.__base__) # None