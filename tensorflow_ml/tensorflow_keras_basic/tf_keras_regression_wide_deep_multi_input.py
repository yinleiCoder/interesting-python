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
回归问题: Wide & Deep模型(多输入)
    Wide & Deep模型：
        Google于16年发布，用于分类和回归问题
        应用到了Google Play中的应用推荐
        论文：https://arxiv.org/pdf/1606.07792v1.pdf
    稀疏特征：
        离散值特征、One-hot表示。
        Eg: 词表={人工智能,你, 我, 他,....} 他=[0,0,0,1,....]
        Eg: 专业={计算机, 人文, 其他,....} 人文=[0,1,0,....]
        可以做叉乘(即组合) = {(计算机，人工智能),(计算机，你),...}
        稀疏特征做叉乘获取共现信息，实现记忆的效果。
        稀疏特征有效，广泛用于工业界。但需要人工设计，可能过拟合，所有特征都叉乘，相当于记住每一个样本。
    密集特征：
        向量表达。
        Eg: 词表={人工智能,你, 他, 我}
            他=[0.3,0.2,0.6,(n维向量),]
        Word2vec工具。
        如：男-女=国王-王后
        密集特征带有语义信息，不同向量之间有相关性通过向量之间的距离计算，
        且兼容没有出现过的特征组合，更少的人工参与。
        但是其过渡泛化，推荐不怎么相关的产品。
    Wide & Deep模型的实现方式：
        1. 子类API
        2. 功能API（函数式API）
        3. 多输入和多输出
"""
print(tf.__version__)
print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)

# 数据集读取与展示(关于加利福尼亚房价的数据集，每个样本的特征维度是8，收入、房龄、房间数量、卧室数量、街道人口、入住人家、房屋经度、房屋维度等)
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
print(housing.DESCR)
print(housing.data.shape)
print(housing.target.shape)

# 划分数据集
from sklearn.model_selection import train_test_split
# test_size指的是划分的训练集和测试集的比例。默认为0.25表示数据分为4份，测试集占一份
x_train_all, x_test, y_train_all, y_test = train_test_split(housing.data, housing.target, random_state=7)
x_train, x_valid, y_train, y_valid = train_test_split(x_train_all, y_train_all, random_state=11)
print(x_train.shape, y_train.shape)
print(x_valid.shape, y_valid.shape)
print(x_test.shape, y_test.shape)

# 归一化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_valid_scaled = scaler.transform(x_valid)
x_test_scaled = scaler.transform(x_test)

# Wide & Deep 模型构建(多输入)
input_wide = keras.layers.Input(shape=[5])
input_deep = keras.layers.Input(shape=[6])
hidden1 = keras.layers.Dense(30, activation='relu')(input_deep)
hidden2 = keras.layers.Dense(30, activation='relu')(hidden1)
concat = keras.layers.concatenate([input_wide, hidden2])
output = keras.layers.Dense(1)(concat)
model = keras.models.Model(inputs=[input_wide, input_deep], outputs=[output])

print(model.summary())
# 均方误差函数，优化函数为随机梯度下降
model.compile(loss='mean_squared_error', optimizer='sgd', )

# 回调函数: EarlyStopping
callbacks = [
    keras.callbacks.EarlyStopping(patience=5, min_delta=1e-2),
]

x_train_scaled_wide = x_train_scaled[:, :5]
x_train_scaled_deep = x_train_scaled[:, 2:]
x_valid_scaled_wide = x_valid_scaled[:, :5]
x_valid_scaled_deep = x_valid_scaled[:, 2:]
x_test_scaled_wide = x_test_scaled[:, :5]
x_test_scaled_deep = x_test_scaled[:, 2:]
history = model.fit([x_train_scaled_wide, x_train_scaled_deep],
                    y_train,
                    epochs=100,
                    validation_data=([x_valid_scaled_wide, x_valid_scaled_deep], y_valid), callbacks=callbacks)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()


plot_learning_curves(history)

print(model.evaluate([x_test_scaled_wide, x_test_scaled_deep], y_test))
