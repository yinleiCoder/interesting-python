import cv2
import numpy as np
"""
高通滤波：Laplacian(拉普拉斯)

Laplacian算子：
    可以同时求2个方向的边缘。
    但是对噪音敏感，一半需要先进行去噪再调用Laplacian算子

Laplacian(img, ddepth, ksize=1, scale=1, delta=0, borderType=BORDER_DEFAULT)

"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')

res = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.waitKey(0)



