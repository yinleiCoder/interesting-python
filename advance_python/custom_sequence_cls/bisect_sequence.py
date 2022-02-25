"""
bisect维护已排序序列：
    用来处理已排序的序列(不要将list和序列混为一谈)，来维持已排序的序列，升序。
"""
import bisect

# bisect算法是二分查找
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)

print(bisect.bisect(inter_list, 3))# 现在插入3，找到3该插入的位置,返回索引
print(bisect.bisect_left(inter_list, 3))# 现在插入3，找到3该插入的位置(相同元素的左边)



