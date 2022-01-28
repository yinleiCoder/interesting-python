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
分类问题之深度神经网络(批归一化)：
    深度神经网络：
        层次非常深的神经网络

归一化：
    将输入输出做一个规整——均值为0，方差为1
    其他的归一化：
        Min-max归一化：x*=(x-min)/(max-min)
        Z-score归一化：x*=(x-u)/方差
批归一化：
    从输入数据上给扩展到网络的每层激活值上，每层的输出是上层的输入，在每层的输入上都去做归一化。
    即每层的激活值都做归一化
    另外，批归一化可以缓解梯度消失
    
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

# 归一化：x=(x-u) / std
# x_train: [None, 28, 28] -> [None, 784]
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_valid_scaled = scaler.transform(x_valid.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)
x_test_scaled = scaler.transform(x_test.astype(np.float32).reshape(-1, 1)).reshape(-1, 28, 28)

# 模型构建(深度神经网络)
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
for _ in range(20):
    model.add(keras.layers.Dense(100, activation='relu'))
    # 批归一化
    model.add(keras.layers.BatchNormalization())
    """
        model.add(keras.layers.Dense(100, ))
        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Activation('relu', ))
    """
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

print(model.layers)
print(model.summary())

# 回调函数: Tensorborad、EarlyStopping、ModelCheckpoint
logdir = './dnn-bn-callbacks'
if not os.path.exists(logdir):
    os.mkdir(logdir)
output_model_file = os.path.join(logdir, 'fashion_mnist_model.h5')
callbacks = [
    # tensorboard --logdir=callbacks
    keras.callbacks.TensorBoard(logdir),
    keras.callbacks.ModelCheckpoint(output_model_file, save_best_only=True),
    keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
]

history = model.fit(x_train_scaled, y_train, epochs=10, validation_data=(x_valid_scaled, y_valid), callbacks=callbacks)
print(type(history))
print(history.history)


def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 3)
    plt.show()


plot_learning_curves(history)

print(model.evaluate(x_test_scaled, y_test))
