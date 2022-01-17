import cv2
import numpy as np
"""
OpenCV图像基本变换: 图像翻转
    flip(img, flipCode)
    flipCode == 0, 上下
    flipCode > 0, 左右
    flipCode < 0, 上下 + 左右
"""
brother = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

new = cv2.flip(brother, 0)
new = cv2.flip(brother, 1)
new = cv2.flip(brother, -1)

cv2.imshow('unicom', brother)
cv2.imshow('unicom new', new)
cv2.waitKey(0)