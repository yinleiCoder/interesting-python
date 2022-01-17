import cv2
import numpy as np
"""
图像运算：图像减法
图的减法运算就是矩阵的减法运算
subtract(A, B)
"""

yinzihao = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
print(yinzihao.shape)# (960, 544, 3)
img = np.ones((960, 544, 3), np.uint8) * 100

result = cv2.subtract(yinzihao, img)

cv2.imshow("result", result)
cv2.waitKey(0)
