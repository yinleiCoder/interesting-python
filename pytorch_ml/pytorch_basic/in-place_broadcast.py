import torch
"""
Pytorch中的in-place操作：
    就地操作，即不允许使用临时变量。也称原位操作
    x = x + y
    add_ sub_ mul_等
    
Pytorch中的广播机制：
    张量参数可以自动扩展为相同大小
    需要满足2个条件：
        每个张量至少有一个维度
        满足右对齐[不够补1, 从右往前看，2个数逐位比较，=1或者相等]
        如：torch.rand(2, 1, 1) + torch.rand(3)
    
"""

a = torch.rand(2, 3)
b = torch.rand(3)
# a, 2*3
# b, 1*3
# c, 2*3
c = a + b
print(a)
print(b)
print(c)
print(c.shape)