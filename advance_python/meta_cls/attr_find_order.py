"""
属性描述符、属性查找过程：
    数据属性描述符__get__ __set__
    非数据属性描述符__get__

    属性查找过程：
        如果user是某个类的实例，那么user.age(以及等价的getattr(user, 'age'))
        首先调用__getattribute__。如果类定义了__getattr__方法，
        那么在__getattribute__抛出AttributeError的时候就会调用__getattr__。
        而对于描述符__get__的调用，则是发生在__getattribute__内部的。
        user = User(), 那么user.age顺序：
            1。若age是出现在User或其基类的__dict__中，且age是data descriptor,那么调用其__get__
            2. 若age出现在user的__dict__中，那么直接返回user.__dict__['age'],否则
            3. 若age出现在User或其基类的__dict中
                如果age是non-data descriptor,那么调用__get__
                否则返回__dict__['age']
            4. 若User有__getattr__，调用__getattr__,否则
            5.抛出AttributeError
"""
import numbers
class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataIntField:
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField()# 属性描述符对象
    # age = NonDataIntField()

if __name__ == '__main__':
    user = User()
    # user.age = 24
    print(user.__dict__)
    user.__dict__['age'] = 'yinlei'
    print(user.__dict__)
    print(user.__dict__['age'])
    print(user.age)

    # user.age = "test|"
    # print(user.age)
