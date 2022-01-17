import cv2
import numpy as np
"""
高通滤波：Scharr(沙尔)

Scharr算子：
    与Sobel类似，只不过使用的kernel值不同
    Scharr只能求x方向或y方向的边缘
    只支持3*3

Scharr(src, ddepth, dx, dy, scale=1, delta=0, borderType=BORDER_DEFAULT)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')

# 同时x、y方向效果不好
# y方向边缘
res = cv2.Scharr(img, cv2.CV_64F, 1, 0,)
# x方向边缘
res2 = cv2.Scharr(img, cv2.CV_64F, 0, 1,)
result = cv2.add(res, res2)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.imshow('res2', res2)
cv2.imshow('result', result)
cv2.waitKey(0)



