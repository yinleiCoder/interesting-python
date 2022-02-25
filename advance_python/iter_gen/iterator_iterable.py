"""
迭代器、可迭代对象：

"""
from collections.abc import Iterable, Iterator
a = [23, 24]# list
print(isinstance(a, Iterable))# True
print(isinstance(a, Iterator))# False

iter_rator = iter(a)# 迭代器
print(isinstance(iter_rator, Iterator))# True

class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]

# 自定义迭代器
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 返回迭代值
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['yinlei', 'yinwei', 'zhangming', 'songyang'])
    my_itor = iter(company)
    # while True:
    #     try:
    #         print(next(my_itor))
    #     except StopIteration:
    #         break
    # for 循环会去尝试调用iter(company),会去找__iter__, 如果没有就创建默认的迭代器，利用__getitem__遍历。
    for item in company:
        print(item)
