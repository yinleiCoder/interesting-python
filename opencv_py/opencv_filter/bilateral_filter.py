import cv2
import numpy as np
"""
OpenCV: 双边滤波

双边滤波：
    bilateralFilter(img, d, sigmaColor, sigmaSpace...)
    d: 核大小
    sigmaColor: 空域核
    sigmaSpace: 值域核
可以保留边缘，同时对边缘内的区域进行平滑处理。
最常见的应用是美颜
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinlei.jpg')

dst = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)