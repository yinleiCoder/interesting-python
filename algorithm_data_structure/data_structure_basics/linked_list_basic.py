"""
链表, linked list.
物理上非连续、非顺序的数据结构，由若干节点node所组成。

链表的第一个节点叫头节点，最后一个节点叫尾节点，尾节点的指针指向空。
数组在内存中的存储方式是顺序存储，链表在内存中的存储方式是随机存储。

单项链表：每一个节点包含存放数据的变量data、指向下一节点的指针next
双向链表：每个节点包含data和next指针、拥有指向前置节点的prev指针

"""

# 节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 链表
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围！")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围！")
        node = Node(data)
        if self.size == 0:
            # 空链表
            self.head = node
            self.last = node
        elif index == 0:
            # 插入头部：1.把新节点的next指针指向头节点，2.把新节点变为链表的头节点
            node.next = self.head
            self.head = node
        elif self.size == index:
            # 插入尾部: 把最后一个节点的next指针指向新插入的节点
            self.last.next = node
            self.last = node
        else:
            # 插入中间：1.新节点的next指针指向插入位置的节点，2.插入位置前置节点的next指针指向新节点
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围！")
        # 暂存被删除的节点，用于返回
        if index == 0:
            # 删除头节点: 把头节点设为原头节点的next指针所指向的节点
            removed_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            # 删除尾节点：把倒数第2个节点的next指针指向空
            prev_node = self.get(index - 1)
            removed_node = prev_node.next
            self.last = prev_node
        else:
            # 删除中间节点：把要删除节点的前置节点的next指针指向要删除元素的下一个节点
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            removed_node = prev_node.next
            prev_node.next = next_node
        self.size -= 1
        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

linkedList = LinkedList()
linkedList.insert(3, 0)
linkedList.insert(4, 0)
linkedList.insert(9, 2)
linkedList.insert(5, 3)
linkedList.insert(6, 1)
linkedList.remove(0)
linkedList.output()


"""
数组和链表都属于线性的数据结构。
    
    查找      更新      插入      删除
数组 O(1)    O(1)      O(n)     O(n)
链表 O(n)    O(1)      O(1)     O(1)

频繁插入、删除元素，链表更合适。
"""
