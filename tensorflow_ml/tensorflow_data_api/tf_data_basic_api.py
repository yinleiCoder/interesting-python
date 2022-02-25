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
Tf.data API:
    Dataset基础API
        tf.data.Dataset.from_tensor_slices
        repeat batch interleave map shuffle list_files 
    Dataset读取csv文件
        tf.data.TextLineDataset tf.io.decode_csv
    Dataset读取tfrecord文件
        tf.train.FloatList tf.train.Int64List tf.train.BytesList
        tf.train.Feature tf.train.Features tf.train.Example
        example.SerializeToString
        tf.io.ParseSingleExample
        tf.io.VarLenFeature tf.io.FixedLenFeature
        tf.data.TFRecordDataset tf.io.TFRecordOptions
"""

print(tf.__version__)
print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)

# from_tensor_slices从内存中构建数据集: 支持numpy
dataset = tf.data.Dataset.from_tensor_slices(np.arange(10))
print(dataset)
for item in dataset:
    print(item)

# 1.repeat epoch
# 2.get batch
dataset = dataset.repeat(3).batch(7)
for item in dataset:
    print(item)

# interleave:
# case: 文件dataset -> 具体数据集
dataset2 = dataset.interleave(
    lambda v: tf.data.Dataset.from_tensor_slices(v),# map_fn
    cycle_length=5,# cycle_length
    block_length=5,# block_length
)
for item in dataset2:
    print(item)

# from_tensor_slices从内存中构建数据集: 支持元组
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array(['cat', 'dog', 'fox'])
dataset3 = tf.data.Dataset.from_tensor_slices((x, y))
print(dataset3)
for item_x, item_y in dataset3:
    print(item_x, item_y)

# from_tensor_slices从内存中构建数据集: 支持字典
dataset4 = tf.data.Dataset.from_tensor_slices({"feature": x, "label": y})
for item in dataset4:
    print(item)