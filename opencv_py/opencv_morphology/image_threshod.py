import cv2
import numpy as np
"""
图像二值化：
    将图像中的每个像素变成2种值，如0,255
    分为：全局二值化、局部二值化

全局二值化:
    threshold(img, thresh, maxValue, type)
    img: 图像，最好是灰度图
    thresh: 阈值
    maxVal: 超过阈值，替换为maxVal
    type: THRESH_BINARY、THRESH_BINARY_INV、THRESH_TRUNC、THRESH_TOZERO、THRESH_TOZERO_INV
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

# 色彩空间转换
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, res = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('res', res)
cv2.waitKey(0)