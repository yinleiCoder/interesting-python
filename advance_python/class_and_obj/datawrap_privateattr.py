"""
数据封装、私有属性：
    java或者其他语言有Private, 不过可以反射修改。
    而python中没有private关键词。

"""
class User:
    def __init__(self, birthday):
        # self.birthday = birthday
        self.__birthday = birthday# 数据封装以__开头

    def get_age(self):
        return 2022 - self.__birthday

if __name__ == '__main__':
    user = User(1998)
    # print(user.birthday)# 不希望让别人访问
    # print(user.__birthday)# User' object has no attribute '__birthday'
    print(user._User__birthday)# 这是python将birthday属性重命名后仍然可以访问
    print(user.get_age())
