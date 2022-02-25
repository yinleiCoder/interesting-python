"""
dict、set的实现原理：
    dict查找的性能远大于 list
    list中随着list数据的增大而查找时间增大
    dict中查找元素不会随着dict的增大而增大

    dict的实现背后是hash table。
    dict的ket或者set的值都必须是可以hash的，即不可变对象都是可hash的。
    自己实现的类需要重载__hash__

    dict的内存花销大，但是查询速度快，自定义对象或内部的对象都是用dict包装的
    dict的存储顺序和元素添加顺序有关。
    添加数据可能改变已有数据。
"""

