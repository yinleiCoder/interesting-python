"""
抽象基类（abc模块）：
    类似于java中的interface。
    而python中的抽象基类也是无法实例化的，python是没有变量的类型的。
    python从语言层面就已经是多态了。
    python去实现class时不需要指定类型，其特性看到底实现了什么魔法函数。
    抽象基类代表在类中设定方法，然后所有继承该类的类必须实现抽象基类中定义的方法。

"""
# 应用场景1：检查某个类是否有某种方法
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

company = Company(['yinlei', 'yinwei'])
print(hasattr(company, "__len__"))# True
# 在某些情况下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(company, Sized))
print(len(company))

# 应用场景2： 强制某个子类必须实现某些方法(例如web框架集成cache)
import abc

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    
    @abc.abstractmethod
    def set(self, key, vlaue):
        pass

class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()
redis_cache.set("yinlei", "yinwei")

