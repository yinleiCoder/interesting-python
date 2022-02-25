import torch
import numpy as np
"""
机器学习问题的构成元素：
    样本、模型、训练、测试、推理

PyTorch的基本概念：
    Tensor
    Variable(autograd)
    nn.Module
    
Tensor:
    每一个tensor有torch.dtype、torch.device、torch.layout属性
    torch.device：torch.Tensor对象在创建后存储在的设备名称
    torch.layout：torch.Tensor内存布局的对象
    稀疏的张量：torch.sparse_coo_tensor
              coo类型表示了非0元素的坐标形式
    Tensor乘法：哈达玛积element wise对应元素相乘          
    矩阵的运算：二维矩阵乘法操作torch.mm() torch.matmul() @
              对于高纬的Tensor(dim>2)，定义其矩阵乘法仅在最后的2个维度上，要求前面的维度必须保持一致，
              就像矩阵的索引一样并且运算操只有torch.matmul()
    
    统计学习之分布函数torch.distributions:
        distributions包含可参数化的概率分布和采样函数
        得分函数——强化学习中策略梯度方法的基础
        pathwise derivative估计器——变分自动编码器中的重新参数化技巧
    
    Tensor中的随机抽样：
        定义随机种子——torch.manual_seed(seed)
        定义随机数满足的分布——torch.normal()
        
    Tensor中的范数运算：
        范数——在泛函分析中，它定义在赋范线性空间中，并满足一定的条件——非负性、齐次性、三角不等式
        常被用来度量某个向量空间或矩阵中的每个向量的长度或大小
        0范数/1范数/2范数/P范数/核范数：
            torch.dist(input, other, p=2)计算p范数
            torch.norm()计算2范数
"""
# 创建张量
a = torch.Tensor([[1, 2], [3, 4]])
print(a)
print(a.type())

b = torch.Tensor(2, 3)# 指定shape（2*3）
print(b)
print(b.type())

c = torch.ones(2, 2)
print(c)
print(c.type())

d = torch.eye(2, 2)
print(d)
print(d.type())

e = torch.zeros(2, 2)
print(e)
print(e.type())

f = torch.zeros_like(a)
g = torch.ones_like(a)
print(f)
print(g)

# 随机tensor
h = torch.rand(2, 2)
print(h)

# 正太分布的tensor
i = torch.normal(mean=torch.rand(5), std=torch.rand(5))
print(i)

# 均匀分布的tensor
j = torch.Tensor(2, 2).uniform_(-1, 1)
print(j)

# 序列tensor
k = torch.arange(0, 10, 2)
print(k)
# 等间隔切分
l = torch.linspace(2, 10, 3)
print(l)
# 打乱tensor
m = torch.randperm(10)
print(m)

# tensor的属性
dev = torch.device('cpu')
a = torch.tensor([2, 2], dtype=torch.float32, device=dev)
print(a)

# 稀疏张量
i = torch.tensor([[0, 1, 2], [0, 1, 2]])
v = torch.tensor([6, 24, 23])
a = torch.sparse_coo_tensor(i, v, (4, 4))
print(a)
# 转为稠密的张量
print(a.to_dense())

# tensor的算术运算
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
print(a + b)
print(a.add(b))
print(torch.add(a, b))
print(a.add_(b))
print(a)

print(a - b)
print(torch.sub(a, b))
print(a.sub(b))

print(a * b)
print(torch.mul(a, b))
print(a.mul(b))

print(a / b)
print(torch.div(a, b))
print(a.div(b))

# 矩阵运算
a = torch.ones(2, 1)
b = torch.ones(1, 2)
print(a @ b)
print(a.matmul(b))
print(torch.matmul(a, b))
print(torch.mm(a, b))
print(a.mm(b))

# 高维tensor
a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
print(a.matmul(b).shape)

# 指数运算
a = torch.tensor([1, 2])
print(torch.pow(a, 3))
print(a.pow(3))
print(a**3)

# e的n次方
a = torch.tensor([1, 2], dtype=torch.float32)
print(torch.exp(a))
print(a.exp())

# log运算
a = torch.tensor([10, 2])
print(torch.log(a))
print(a.log())

# 开平方
print(torch.sqrt(a))
print(a.sqrt())

# 取整取余
a = torch.rand(2, 2)
a = a * 10
print(a)
print(torch.floor(a))
print(torch.ceil(a))
print(torch.round(a))
print(torch.trunc(a))
print(torch.frac(a))
print(a % 2)

# 比较运算
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
print(torch.eq(a, b))
print(torch.equal(a, b))
print(torch.ge(a, b))
print(torch.gt(a, b))
print(torch.le(a, b))
print(torch.lt(a, b))
print(torch.ne(a, b))
a = torch.tensor([24, 6, 23])
print(torch.sort(a))
a = torch.tensor([[2, 4, 3, 1, 5],
                  [2, 3, 5, 1, 4]])
print(torch.topk(a, k=1, dim=0))
print(torch.kthvalue(a, k=2, dim=0))

a = torch.rand(2, 3)
print(a)
print(torch.isfinite(a))
print(torch.isfinite(a/0))
print(torch.isinf(a/0))
print(torch.isnan(a))
a = torch.tensor([1, 2, np.nan])
print(torch.isnan(a))

# 三角函数
a = torch.rand(2, 3)
print(torch.cos(a))

# 统计学方法
a = torch.rand(2, 2)
print(a)
print(torch.mean(a))
print(torch.sum(a))
print(torch.prod(a))
print(torch.argmax(a, dim=0))
print(torch.argmin(a, dim=0))
print(torch.std(a))
print(torch.var(a))
print(torch.median(a))
print(torch.mode(a))
a = torch.rand(2, 2) * 10
print(torch.histc(a, 6, 0, 0))
a = torch.randint(0, 10, [10])
print(torch.bincount(a))# 只支持一维tensor

# 随机抽样
torch.manual_seed(1)
print(torch.normal(mean=torch.rand(1, 2), std=torch.rand(1, 2)))

# 范数运算计算距离
a = torch.rand(1, 1)
b = torch.rand(1, 1)
print(torch.dist(a, b, p=1))
print(torch.dist(a, b, p=2))
print(torch.dist(a, b, p=3))
print(torch.norm(a))
