"""
python对象的自省机制：
    自省，通过一定的机制查询到对象的内部结构。
    __dict__查询属性
    dir()列出所有属性,不含属性值
"""
class Person:
    name = "person"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
    stu = Student("yinlei")
    print(stu.__dict__)
    print(stu.name)

    print(Person.__dict__)

    stu.__dict__['school_addr'] = '眉山市'
    print(stu.school_addr)

    print(dir(stu))