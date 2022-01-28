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
分类问题之数据归一化：
    
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
print(np.max(x_train), np.min(x_train))
# 归一化：x=(x-u) / std
# x_train: [None, 28, 28] -> [None, 784]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_valid_scaled = scaler.transform(x_valid.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_test_scaled = scaler.transform(x_test.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
print(np.max(x_train_scaled), np.min(x_train_scaled))

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

history = model.fit(x_train_scaled, y_train, epochs=10, validation_data=(x_valid_scaled, y_valid))
print(type(history))
print(history.history)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
plot_learning_curves(history)

print(model.evaluate(x_test_scaled, y_test))