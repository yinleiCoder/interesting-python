import cv2
import numpy as np
"""
自适应阈值二值化:
    通过权值阈值对图像做二值化，这种方法对某些图像效果不好，由于光照不均匀以及阴影的存在，
    只有一个阈值会使得在阴影处的白色被二值化为黑色。

    adaptiveThreshold(img, maxValue, adaptiveMethod, type, blocksize, C)
    adaptiveMethod: 计算阈值的方法 ADAPTIVE_THRESH_MEAN_C(计算邻近区域的平均值)、ADAPTIVE_THRESH_GAUSSIAN_C(高斯窗口加权平均值)
    blockSize: 邻近区域的大小
    C: 常量，应从计算出的平均值或加权平均值中减去
    type: THRESH_BINARY、THRESH_BINARY_INV
    THRESH_TRUNC、THRESH_TOZERO、THRESH_TOZERO_INV [不属于二值化范畴]
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

# 色彩空间转换
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

res = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 3, 0)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('res', res)
cv2.waitKey(0)