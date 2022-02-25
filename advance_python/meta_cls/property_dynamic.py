"""
property动态属性：

"""
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        # self.age = 0
        self._age = 0

    def get_age(self):
        return 2022 - self.birthday

    @property
    def age(self):
        return 2022 - self.birthday

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':
    user = User('yinlei', 1998)
    print(user.get_age())
    print(user.age)
    user.age = 23
    print(user._age)
    print(user.age)
