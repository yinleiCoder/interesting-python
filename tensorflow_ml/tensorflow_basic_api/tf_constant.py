import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import os
import sys
import time
import tensorflow as tf
from tensorflow import keras
"""
TF API: 基础数据类型

TF API列表：
    基础数据类型：
        tf.constant tf.string
        tf.ragged.constant tf.SparseTensor tf.Variable
    自定义损失函数：tf.reduce_mean
    自定义层次：Keras.layers.Lambda、继承法
    tf.function:
        tf.function tf.autograph.to_code get_concret_function
    GraphDef:
        get_operations get_operation_by_name
        get_tensor_by_name as_graph_def
    自动求导：
        tf.GradientTape Optimzier.apply_gradients
        
"""
print(tf.__version__)
print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)

# 常量
t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
# 索引操作
print(t)
print(t[:, 1:])
print(t[..., 1])
# 算子操作
print(t + 10)
print(tf.square(t))
print(t @ tf.transpose(t))# 矩阵乘以其转置

# 与numpy转换
print(t.numpy())
print(np.square(t))
np_t = np.array([[1., 2., 3.], [4., 5., 6.]])
print(tf.constant(np_t))

# 0维：Scalars
t = tf.constant(2.718)
print(t.numpy())
print(t.shape)

# 字符串
t = tf.constant('tensorflow')
print(t)
print(tf.strings.length(t))
print(tf.strings.length(t, unit="UTF8_CHAR"))
print(tf.strings.unicode_decode(t, "UTF8"))

# 字符串数组
t = tf.constant(['cafe', 'tensorflow', '尹磊'])
print(tf.strings.length(t, unit="UTF8_CHAR"))
print(tf.strings.unicode_decode(t, "UTF8"))

# RaggedTensor: 不等长的、不规则的tensor
r = tf.ragged.constant([[47, 40], [75, 75, 85], [], [24]])
r3 = tf.ragged.constant([[47, 40], [75, 75, 85], [], [24]])
print(r)
print(r[1])
print(r[1:2])
r2 = tf.ragged.constant([[50, 47], [], [23]])
print(tf.concat([r, r2], axis=0))
# 横向拼接需要tensor有一样的行数
# print(tf.concat([r, r2], axis=1))
print(tf.concat([r, r3], axis=1))
# 转为普通tensor, 空闲位置用0补齐, 且0值在正常值后
print(r.to_tensor())

# SparseTensor: 如果矩阵中，大部分为0，少部分为1，就记录少部分值的坐标 indices需要有序，无序的话需要调用tf.sparse.reorder()
s = tf.SparseTensor(indices=[[0, 1], [1, 0], [2, 3]], values=[1., 2., 3.], dense_shape=[3, 4])
print(s)
# 转为普通tensor
print(tf.sparse.to_dense(s))

s2 = s * 2.0
print(s2)
try:
    s3 = s + 1
except TypeError as ex:
    print(ex)
s4 = tf.constant([[10., 20.], [30., 40.], [50., 60.], [70., 80.]])
print(tf.sparse.sparse_dense_matmul(s, s4))# 矩阵相乘

# 变量
v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
print(v)
print(v.value()) # 转为tensor
print(v.numpy())
# assign: 变量的重新赋值
v.assign(2*v)
print(v.numpy())
v[0, 1].assign(24)
print(v.numpy())
v[1].assign([7., 8., 9.])
print(v.numpy())