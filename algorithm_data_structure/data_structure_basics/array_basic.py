"""
数组, array.
有限个相同类型的变量所组成的有序集合，数组中的每一个变量称为元素。
数组是最简单、最常用的数据结构。

数组的特点：
    1. 每一个元素都有自己的下标，下标从0开始，一直到数组的长度-1
    2. 在内存中顺序存储，可很好的实现逻辑上的顺序表

内存是由一个个连续的内存单元组成，每一个内存单元都有自己的地址。
在这些内存单元中，有些被其他数据占用了的，有些是空闲的。
数组中的每一个元素，都存储在小小的内存单元中，并且元素之间紧密排列，既不能打乱元素的存储顺序，也不能跳过某个存储单元进行存储。

python中使用list列表、元组tuple表示数组这个概念，本质都是对数组的封装。
"""

# 数组的基本操作：读取元素
# 初始化列表
my_list = [3, 1, 2, 5, 4, 9, 7, 2]
# 随机读取元素
print(my_list[2])

# 数组的基本操作：更新元素
my_list[3] = 10
print(my_list[3])

# 数组的基本操作：插入元素(尾部插入、中间插入、超范围插入)
# 尾部插入元素
my_list.append(6)
#中间插入元素
my_list.insert(5,  11)
print(my_list)

# 自定义插入操作实现上述insert方法
class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    # def insert_custom(self, index, element):
    #     if index < 0 or index > self.size:
    #         raise Exception("超出数组实际元素范围")
    #     # 从右向左循环，逐个元素向右挪1位
    #     for i in range(self.size - 1, -1, -1):
    #         self.array[i + 1] = self.array[i]
    #     # 腾出的位置放入新元素
    #     self.array[index] = element
    #     self.size += 1

    """
    超范围插入：需要扩容数组。数组的长度在创建时就已经确定了，可以创建一个新数组，长度是旧数组的２倍，把旧数组中的元素都复制过去。
    """
    def insert_custom(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围")
        # 如果实际元素达到数组容量上线，数组扩容
        if self.size >= len(self.array):
            self.resize()
        # 从右向左循环，逐个元素向右挪1位
        for i in range(self.size - 1, -1, -1):
            self.array[i + 1] = self.array[i]
        # 腾出的位置放入新元素
        self.array[index] = element
        self.size += 1

    # 数组的删除
    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围")
        # 从左到右，逐个元素向左挪动1位
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    # 数组的扩容
    def resize(self):
        array_new = [None] * len(self.array) * 2
        # 从旧数组复制到新数组
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def output(self):
        for i in range(self.size):
            print(self.array[i])

array_custom = MyArray(4)
array_custom.insert_custom(0, 10)
array_custom.insert_custom(0, 11)
array_custom.insert_custom(0, 15)
array_custom.output()
array_custom.remove(1)
array_custom.output()

"""
数组的删除的另一种方式：把最后一个元素复制到要删除的元素所在的位置，再删除最后一个元素。
前提是数组元素没有顺序要求。
"""

"""
数组的优势：非常高效的随机访问能力，给出下标，旧可以用常量时间找到对应元素。二分查找就是利用的该优势。
数组的劣势：插入、删除都会导致大量的元素被迫移动，影响效率。

数组适合：读操作多，写操作少的场景。
"""