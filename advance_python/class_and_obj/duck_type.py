"""
鸭子类型与多态：
    鸭子类型——当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
"""
class Cat:
    def say(self):
        print('i am a cat')
class Dog:
    def say(self):
        print('i am a dog')
class Duck:
    def say(self):
        print('i am a duck')

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# extend() indicate duck_type
a = ["yinlei", "zhangming"]
b = ["songyang", "yinwei"]
name_tuple = ("yangqian", "wangfuling")
name_set = set()
name_set.add("yuhaijiao")
name_set.add("chenjiajia")
a.extend(b)
print(a)
a.extend(name_tuple)
print(a)
a.extend(name_set)
print(a)