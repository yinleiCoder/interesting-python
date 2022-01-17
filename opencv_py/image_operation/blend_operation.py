import cv2
import numpy as np
"""
OpenCV图像运算：图像溶合
    addWeighted(A, alpha, B, bate, gamma)
    alpha、beta是权重
    gamma静态权重

只有2张图的属性是一样的才可以进行溶合
"""
boy = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\boy.png')
space = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\space.png')
print(boy.shape)
print(space.shape)

result = cv2.addWeighted(boy, 0.7, space, 0.3, 0)

cv2.imshow('addWeighted', result)
cv2.waitKey(0)
