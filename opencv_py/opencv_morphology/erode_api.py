import cv2
import numpy as np
"""
腐蚀：就是缩小
erode(img, kernel, iterations=1)

腐蚀的卷积核全1，如：
| 1 1 1 |  | 1 1 1 1 1 |
| 1 1 1 |  | 1 1 1 1 1 |
| 1 1 1 |  | 1 1 1 1 1 |
           | 1 1 1 1 1 |
           | 1 1 1 1 1 |
获取卷积核：
    getStructuringElement(type, size)
    size: (3, 3)、(5, 5)……
    type: MORPH_RECT、MORPH_ELLIPSE、MORPH_CROSS
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\j.png')

# kernel = np.ones((7, 7), np.uint8)# 手动创建
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(kernel)
res = cv2.erode(img, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('erode', res)
cv2.waitKey(0)