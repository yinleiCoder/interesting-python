import cv2
import numpy as np
"""
高通滤波：Sobel(索贝尔)

Sobel算子：
    先向X方向求导，然后在Y方向求导
    最终结果 |G| = |Gx| + |Gy|

Sobel(src, ddepth, dx, dy, ksize=3, scale=1, delta=0, borderType=BORDER_DEFAULT)
ksize=-1时，变成沙尔算法
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')

# 同时x、y方向效果不好
# y方向边缘
res = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# x方向边缘
res2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
result = cv2.add(res, res2)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.imshow('res2', res2)
cv2.imshow('result', result)
cv2.waitKey(0)



