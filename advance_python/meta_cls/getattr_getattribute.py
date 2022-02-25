"""
__getattr__ __getattribute__:
    __getattr__在查找不到属性的时候调用
    __getattribute__所有属性查找先进该方法
"""

class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 查找不到属性进入这个
    def __getattr__(self, item):
        # return "not find attr"
        return self.info[item]

    # 不管查不查的到属性，先进这个方法(所有属性访问的入口)
    def __getattribute__(self, item):
        return "yinlei"

if __name__ == '__main__':
    user = User('yinlei', 1998, info={'company': 'unicom'})
    # print(user.age)# 'User' object has no attribute 'age'
    print(user.company)