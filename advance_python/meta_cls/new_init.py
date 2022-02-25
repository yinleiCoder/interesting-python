"""
__new__ __init__的区别：
    __new__在__init__之前
    __new__是用来控制对象的生成过程，在对象生成之前
    __init__是用来完善对象的
    如果__new__方法不返回对象，则不会调用__init__
"""
class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self, name):
        print('in init')
        self.name = name

if __name__ == '__main__':
    user = User('yinlei')
