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
回归问题: 超参数搜索(基于sklearn实现超参数的随机化搜索)
    
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

# 模型构建(超参数的随机化搜索RandomizedSearchCV)
def build_model(hidden_layers=1, layer_size=30, learning_rate=3e-3):
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(layer_size, activation='relu', input_shape=x_train.shape[1:]))
    for _ in range(hidden_layers - 1):
        model.add(keras.layers.Dense(layer_size, activation='relu'))
    model.add(keras.layers.Dense(1))
    optimizer = keras.optimizers.SGD(learning_rate)
    model.compile(loss='mse', optimizer=optimizer)
    return model

# 1.转化为sklearn的model
sklearn_model = keras.wrappers.scikit_learn.KerasRegressor(build_model)
callbacks = [
    keras.callbacks.EarlyStopping(patience=5, min_delta=1e-2),
]
history = sklearn_model.fit(x_train_scaled, y_train, epochs=100, validation_data=(x_valid_scaled, y_valid), callbacks=callbacks)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()

plot_learning_curves(history)

# 2.定义参数集合
from scipy.stats import reciprocal
# f(x)=1/(x*log(b/a)) a<=x<=b
param_distribution = {
    "hidden_layers": [1, 2, 3, 4],
    "layer_size": np.arange(1, 100),
    "learning_rate": reciprocal(1e-4, 1e-2),
}
from sklearn.model_selection import RandomizedSearchCV
random_serach_cv = RandomizedSearchCV(sklearn_model, param_distribution, n_iter=10, n_jobs=1)
random_serach_cv.fit(x_train_scaled, y_train, epochs=100, validation_data=(x_valid_scaled, y_valid), callbacks=callbacks)
# 3.搜索参数
print(random_serach_cv.best_params_)
print(random_serach_cv.best_score_)
print(random_serach_cv.best_estimator_)
model = random_serach_cv.best_estimator_.model
print(model.evaluate(x_test_scaled, y_test))