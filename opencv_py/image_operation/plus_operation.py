import cv2
import numpy as np
"""
图像运算：图像相加
图的加法运算就是矩阵的加法运算
    add(A, B)

乘法：multiply(A, B)
除法：divide(A, B)
"""

yinzihao = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
print(yinzihao.shape)# (960, 544, 3)
img = np.ones((960, 544, 3), np.uint8) * 100
cv2.imshow('origin', yinzihao)

result = cv2.add(yinzihao, img)

cv2.imshow("result", result)
cv2.waitKey(0)
