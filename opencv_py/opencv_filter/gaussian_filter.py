import cv2
import numpy as np
"""
OpenCV: 高斯滤波

高斯滤波：
    GaussianBlur(img, kernel, sigmaX, sigmaY...)
    sigma: 中心滤波延展的宽度，即到原点（中心点）的差距
高斯权重，越靠近锚点，权重越高，呈现正太分布
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\boy.png')

dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1,)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)