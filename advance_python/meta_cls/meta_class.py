"""
自定义元类：
    type获取某个对象的类型、type创建类
    type(object_or_name, bases, dict)
    type(object) -> the object's type
    type(name, bases, dict) -> a new type

    元类：创建类的类。
    type就是一个元类。
    实际编码很少用type创建class, 一般用元类的写法

    python中类的实例化过程：
    type去创建类对象(实例)。而元类中会首先去寻找metaclass属性，如果找到了
    就去调用metaclass去实例化类对象。
"""

def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return "company"
        return Company


def say(self):
    # return "i am yinlei"
    return self.name

class BaseCls:
    def answer(self):
        return "i am base class"

# python3中元类的写法，替代type写法, 控制类实例化的过程
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class Person(metaclass=MetaClass):
    pass

if __name__ == '__main__':
    # myClass = create_class('user')
    # my_obj = myClass()
    # print(my_obj)
    # print(type(my_obj))
    # type动态创建类
    User = type('User', (BaseCls, ), {'name': 'yinlei', "say": say})
    my_obj = User()
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())