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
回归问题: 超参数搜索(手动实现超参数搜索)
    神经网络有很多训练过程中不变的参数。
        如：网络结构参数，eg: 几层、每层宽度、每层激活函数等
        又如：batch_size、学习率、学习率衰减算法等
    手工去试耗费人力。
    搜索策略：
        网格搜索：定义n维方格，每一方格对应一组超参数，一组组参数尝试
        随机搜索：参数的生成方式随机，可探索的空间更大
        遗传算法搜索：对自然界的模拟，
                    A. 初始化候选参数集合 -> 训练 -> 得到模型指标作为生存概率
                    B. 选择 -> 交叉 -> 变异 -> 产生下一代集合
                    C. 重新回到A
        启发式搜索：研究热点AutoML
                  使用循环神经网络来生成参数
                  使用强化学习来进行反馈，使用模型来训练生成参数
                  
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

# 查看前5个数据是什么样子
import pprint
pprint.pprint(housing.data[0:5])
pprint.pprint(housing.target[0:5])

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

# 模型构建(手动实现超参数搜索，例如想搜索learning-rate: [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2]
# W = W + GRAD(导数) * learning_rate
learing_rate = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2]
histories = []
for lr in learing_rate:
    model = keras.models.Sequential([
        keras.layers.Dense(30, activation='relu', input_shape=x_train.shape[1:]),
        keras.layers.Dense(1),
    ])
    optimizer = keras.optimizers.SGD(lr)
    model.compile(loss='mean_squared_error', optimizer=optimizer, )
    callbacks = [
        keras.callbacks.EarlyStopping(patience=5, min_delta=1e-2),
    ]
    history = model.fit(x_train_scaled, y_train, epochs=100, validation_data=(x_valid_scaled, y_valid), callbacks=callbacks)
    histories.append(history)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
for lr, history in zip(learing_rate, histories):
    print("Learning rate: ", lr)
    plot_learning_curves(history)