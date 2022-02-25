"""
什么是魔法函数：
    以双下划线开头、以双下划线结尾的python内部定义好了的函数。

python的数据模型以及数据模型对python的影响:
    魔法函数本身是python数据模型的一个概念。
    魔法函数是会影响python语法的，比如下面的代码中直接迭代对象。
    魔法函数的调用是隐式的，可理解为独立的存在。在类中加入这些方法后，可以增强自定义类的类型。
    python通过自己内置的一些魔法函数让我们去定义一些对象或者类的时候它的行为可以很神奇。

python的魔法函数：
    我们不能随便去自定义魔法函数，这些魔法函数是由python提供好了的。
    非数学运算——
        字符串表示 __repr__ __str__
        集合序列相关 __len__ __getitem__ __setitem__ __delitem__ __contains__
        迭代相关 __iter__ __next__
        可调用 __call__
        with上下文管理器 __enter__ __exit__
        数值转换 __abs__ __bool__ __int__ __float__ __hash__ __index__
        元类相关 __new__ __init__
        属性相关 __getattr__ __setattr__ __getattribute__ __setattribute__ __dir__
        属性描述符 __get__ __set__ __delete__
        协程 __await__ __aiter__ __anext__ __aenter_ __aexit__
    数学运算——
        一元运算符 __neg__ __pos__ __abs__
        二元运算符 __lt__ __le__ __eq__ __ne__ __gt__ __ge__..
        算术运算符 __add__ __sub__ __mul__ __truediv__ __floordiv__ __mod__ ....
        反向算术运算符 __radd__ __rsub__ __rmul__ ...
        增量赋值算术运算符__iadd__ __isub__ __imul__..
        位运算符__xor__ __rshift__...
        反向位运算符__rlshift__ __rrshift__ __rand__...
        增量赋值位运算符 __ilshift__ __ior__...
"""
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    # 不实现__len__调用len()也可以成功，是因为会先尝试调用__len__，如果没有就退一步去调__getitem__
    # def __len__(self):
    #     return len(self.employee)

    def __str__(self):
        return ",".join(self.employee)

company = Company(['YinLei', 'YuHaiJiao', 'YangQian'])
# emploee = company.employee
# for em in emploee:
#     print(em)
for em in company:
    print(em)

company_drop_last = company[:2]
print(len(company_drop_last))
# len()所作的工作远不止这些,len(set list dict)在cpython中性能很高，会直接读取c语言中的相关维护长度的数据，而不是每次遍历

# 字符串表示的魔法函数
print(company)# 使用之前<__main__.Company object at 0x000001FB819FC520>
print(company)# 使用之后YinLei,YuHaiJiao,YangQian

class CustomNum:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)
my_num = CustomNum(-24)
print(abs(my_num))