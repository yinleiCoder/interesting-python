"""
dict的子类：
    不建议继承list dict
    建议继承UserDict, 有__missing__
    defaultdict重写了__missing__
"""

# class MyDict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)


from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


from collections import defaultdict



if __name__ == '__main__':
    my_dict = MyDict(one=1)# 不生效[UserDict则生效]
    # my_dict['one'] = 1# 生效
    print(my_dict)

    my_dict = defaultdict(dict)
    print(my_dict['yinleilei'])
