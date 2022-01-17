import cv2
import numpy as np
"""
边缘检测终极大法：Canny
不像前面3种高通滤波的问题。

Canny:
    使用5*5高斯滤波消除噪声
    计算图像梯度的方向(0°/45°/90°/135°)
    取局部极大值
    阈值计算 
Canny(img, minVal, maxVal, ...)
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinlei.jpg')

res = cv2.Canny(img, 5, 100)

cv2.imshow('img', img)
cv2.imshow('canny', res)
cv2.waitKey(0)
