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
分类问题：
    预测的是类别，模型输出的是概率分布。
    如三分类问题输出例子[0.2 0.7 0.1]

回归问题：
    预测的是值，模型的输出是一个实数值。

目标函数：
    参数是逐步调整的。目标函数可以帮助衡量模型的好坏。
    如：Model A:[0.1 0.4 0.5]
       Model B:[0.1 0.2 0.7]
    对于分类问题，目标函数需要衡量目标类别与当前预测的差距。
        如三分类问题输出例子：[0.2 0.7 0.1]
          三分类真实类别：2 -> one_hot -> [0, 0, 1]
          one-hot编码，把正整数变为向量表达，生成一个长度不小于正整数的向量，只有正整数的位置处为1，其余位置都为0
        常用平方差损失、交叉熵损失
    对于回归问题，目标函数预测值与真实值的差距。
        常用平方差损失、绝对值损失。

模型的训练就是调整参数，使得目标函数逐渐变小的过程。

神经网络的训练：
    model.compile(optimizer='sgd')
    sgd算法是类似于“下山”，找到方向、走一步。即梯度下降，包括求导、更新参数。

激活函数：
    activation='relu',
    其他常见的激活函数：Sigmoid、Leaky ReLu、tanh、Maxout、ReLu、ELU
    
归一化：
    将输入输出做一个规整——均值为0，方差为1
    其他的归一化：
        Min-max归一化：x*=(x-min)/(max-min)
        Z-score归一化：x*=(x-u)/方差
"""
print(tf.__version__)
print(sys.version_info)
for module in mpl, np, pd, sklearn, tf, keras:
    print(module.__name__, module.__version__)

# 数据集读取与展示
fashion_mnist = keras.datasets.fashion_mnist
(x_train_all, y_train_all), (x_test, y_test) = fashion_mnist.load_data()
x_valid, x_train = x_train_all[:5000], x_train_all[5000:]
y_valid, y_train = y_train_all[:5000], y_train_all[5000:]
print(x_valid.shape, y_valid.shape)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

def show_single_image(img_arr):
    plt.imshow(img_arr, cmap='binary')
    plt.show()

show_single_image(x_train[0])

def show_imgs(n_rows, n_cols, x_data, y_data, class_names):
    assert len(x_data) == len(y_data)
    assert n_rows * n_cols < len(x_data)
    plt.figure(figsize=(n_cols*1.4, n_rows*1.6))
    for row in range(n_rows):
        for col in range(n_cols):
            index = n_cols * row + col
            plt.subplot(n_rows, n_cols, index+1)
            plt.imshow(x_data[index], cmap='binary', interpolation='nearest')
            plt.axis('off')
            plt.title(class_names[y_data[index]])
    plt.show()

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
show_imgs(3, 5, x_train, y_train, class_names)

# 模型构建
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
# relu: y=max(0, x)
model.add(keras.layers.Dense(300, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
# softmax: 将向量变为概率分布 x = [x1, x2, x3] , y=[e^x1/num,e^x2/num,e^x2/num], sum=e^x1+e^x2+e^x3
model.add(keras.layers.Dense(10, activation='softmax'))
# sparse: y->index, y->one_hot->[]
model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

print(model.layers)
print(model.summary())

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_valid, y_valid))
print(type(history))
print(history.history)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
plot_learning_curves(history)