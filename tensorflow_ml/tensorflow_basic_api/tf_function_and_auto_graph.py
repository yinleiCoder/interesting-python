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
tf.function和autograph

@tf.function:
    将python函数编译成图
    易于将模型导出成为GraphDef + checkpoint或SavedModel
    使得eager execution可以默认打开
    1.0代码可以通过tf.function来继续在2.x里继续使用
    替代session
autograph：
    实现中转换的机制
    
"""
print(tf.__version__)
print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)

def scaled_elu(z, scale=1.0, alpha=1.0):
    # z >= 0 ? scale * z : scale * alpha * tf.nn.elu(z)
    is_positive = tf.greater_equal(z, 0.0)
    return scale * tf.where(is_positive, z, alpha * tf.nn.elu(z))

print(scaled_elu(tf.constant(-3.)))
print(scaled_elu(tf.constant([-3., -2.5])))

# tf.function将python函数转为图结构。其优势就是图的优化，可以更快
scaled_elu_tf = tf.function(scaled_elu)
print(scaled_elu_tf(tf.constant(-3.)))
print(scaled_elu_tf(tf.constant([-3., -2.5])))
print(scaled_elu_tf.python_function is scaled_elu)

# @tf.function注解将python函数转为图结构
# 1 +1 /2 + 1/2^2 + ... 1/2^n
@tf.function
def converge_to_2(n_inters):
    total = tf.constant(0.)
    increment = tf.constant(1.)
    for _ in range(n_inters):
        total += increment
        increment /= 2.0
    return total
print(converge_to_2(20))

# 查看转化图结构过程
def display_tf_code(func):
    code = tf.autograph.to_code(func)
    from IPython.display import display, Markdown
    display(Markdown('```python\n{}\n```'.format(code)))

display_tf_code(scaled_elu)

var = tf.Variable(0) # 不能放在@tf.function里
@tf.function
def add_21():
    return var.assign_add(21)
print(add_21())

@tf.function(input_signature=[tf.TensorSpec([None], tf.int32, name='x')])
def cube(z):
    return tf.pow(z, 3)
try:
    print(cube(tf.constant([1., 2., 3.])))
except ValueError as ex:
    print(ex)
print(cube(tf.constant([1, 2, 3])))
# tf.Tensor([ 1.  8. 27.], shape=(3,), dtype=float32)
# tf.Tensor([ 1  8 27], shape=(3,), dtype=int32)
# 如果我们希望明确类型进行类型限制，就需要函数签名, 通过加input_signature

# @tf.function py func -> graph
# get_concrete_function -> add input signature -> SavedModel
cube_func_int32 = cube.get_concrete_function(tf.TensorSpec([None], tf.int32))
print(cube_func_int32)
print(cube_func_int32 is cube.get_concrete_function(tf.TensorSpec([5], tf.int32)))
print(cube_func_int32 is cube.get_concrete_function(tf.constant([1, 2, 3])))
# 查看图结构
print(cube_func_int32.graph)
print(cube_func_int32.graph.get_operations())
pow_op = cube_func_int32.graph.get_operations()[2]
print(pow_op)
print(list(pow_op.inputs))
print(list(pow_op.outputs))
print(cube_func_int32.graph.get_operations_by_name('x'))
print(cube_func_int32.graph.as_graph_def())
