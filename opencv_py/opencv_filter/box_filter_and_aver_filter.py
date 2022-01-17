import cv2
import numpy as np
"""
OpenCV: 方盒滤波与均值滤波

方盒滤波、均值滤波：
    boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
    blur(src, ksize, anchor, borderType) # 均值滤波
    
     | 1 1 .. .. 1 |
K = a| 1 1 .. .. 1 |
     | .. ... .... |
     | 1 1 ..  ..1 |
     normalize = true, a = 1 / W * H, 方盒滤波==平均滤波
     normalize = false, a = 1
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinlei.jpg')

dst = cv2.blur(img, (5, 5),)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)