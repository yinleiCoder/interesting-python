"""
算法，algorithm.

数学领域：算法是用于解决某一类问题的公式和思想。
计算机科学领域：算法本质是一系列程序指令，用于解决特定的运算和逻辑问题。

算法有简单的，也有复杂的。
算法有高效的，也有拙劣的。

衡量算法好坏的重要标准：时间复杂度、空间复杂度

算法的应用领域多种多样：运算、查找、排序、最优决策、面试。
考查算法问题：检验程序员对计算机底层知识的了解、衡量程序员的逻辑思维能力。
"""

"""
数据结构，data structure.

数据结构，是数据的组织、管理和存储格式，其使用目的是高效访问和修改数据。

组成方式：线性结构、树、图、其他数据结构。

在解决问题时，不同的算法会选用不同的数据结构。
"""

"""
衡量程序好坏的重要因素：运行时间的长短、占用内存空间的大小。

由于受运行环境和输入规模的影响，代码的绝对执行时间是无法预估的。但可以预估代码的基本操作执行次数。

基本操作执行次数：设T(n)为程序基本操作执行次数的函数(程序的相对执行时间函数),n为输入规模。
程序中最常见的4种执行方式：线性、对数、常数、多项式

渐进时间复杂度：若存在函数f(n)，使得当n趋近于无穷大时，T(n)/f(n)的极限值为不等于0的常数，则称f(n)是T(n)的同数量级函数。
             记作T(n) = O(f(n))，称为O(f(n))，O为算法的渐进时间复杂度，简称时间复杂度。也被称为大O表示法。
             简单的说，时间复杂度就是把程序的相对执行时间函数T(n)简化为一个数量级，可以是n、n^2、n^3等

推导时间复杂度的原则：
            1.如果运行时间是常数量级，则用常数1表示
            2.只保留时间函数中的最高阶项
            3.如果最高阶项存在，则省去最高阶项前面的系数
"""
def eat1(n):
    for i in range(n):
        print("等待1min")
        print("等待1min")
        print("吃1cm面包")

def eat2(n):
    while n > 1:
        print("等待1min")
        print("等待1min")
        print("等待1min")
        print("等待1min")
        print("吃一半面包")
        n /= 2

def eat3(n):
    print("等待1min")
    print("吃一个鸡腿")

def eat4(n):
    for i in range(n):
        for j in range(i):
            print("等待1min")
        print("吃1cm面包")

"""
空间复杂度：
时间复杂度是执行算法的时间成本，空间复杂度是执行算法的空间成本。
在运行一段程序时，不仅要执行各种运算指令，也会根据需要存储一些临时的中间数据，以便后续指令可以更方便地继续执行。

空间复杂度是对一个算法在运行过程中临时占用存储空间大小的量度，使用大O表示法。
程序占用空间大小的计算公式：S(n)=O(f(n))，n为问题的规模，f(n)为算法所占存储空间的函数。

常见的空间复杂度的增长趋势：
    1. 常量空间：算法的存储空间大小固定，和输入规模没有直接的关系。
    2. 线性空间：算法分配的空间是一个线性的集合，集合大小和输入规模n成正比。
    3. 二维空间：算法分配的空间是一个二维列表集合，并且集合的长度和宽度都与输入规模n成正比。
    4. 递归空间：代码中没有显式声明变量或集合，但计算机在执行程序时，会专门分配一块内存，用来存储”函数调用栈“
                函数调用栈：进栈、出栈
                当进入一个新函数时，执行入栈操作，把调用的函数和参数信息压入栈中
                当函数返回时，执行出栈操作，把调用的函数和参数信息从栈中弹出
                执行递归操作所需要的内存空间和递归的深度成正比。纯粹的递归操作的空间复杂度也是线性的，如果递归的深度是n，那么空间复杂度就是O(n)
"""
def fun1(n):
    i = 23
    # do something

def fun2(n):
    temp_array =[[0] * n]
    # do something

def fun3(n):
    matrix = [[0] * n] * n
    # do something

def fun4(n):
    if n > 0:
        fun4(n - 1)
    # do something

"""
时间与空间的取舍：
花大力气去评估算法的时间复杂度和空间复杂度，根本原因是计算机的运算速度和空间资源都是有限的。
绝大多数时候，时间复杂度更为重要一些，宁可多分配一些内存空间，也要提升程序的执行速度。
"""