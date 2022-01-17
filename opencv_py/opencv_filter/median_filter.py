import cv2
import numpy as np
"""
OpenCV: 中值滤波

中值滤波：
    medianBlur(img, ksize)

假设有一个数组[1556789],取其中的中间值作为卷积后的结果值
对胡椒噪音效果明显
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\hujiao.png')

dst = cv2.medianBlur(img, 5)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)