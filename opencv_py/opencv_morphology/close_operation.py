import cv2
import numpy as np
"""
闭运算：
闭运算= 膨胀 + 腐蚀(先膨胀再腐蚀)
morphologyEx(img, MORPH_CLOSE, kernel)

形态学梯度：
    梯度 = 原图 - 腐蚀
    可以得出边缘
morphologyEx(img, MORPH_GRADIENT, kernel)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\dotinj.png')

# kernel = np.ones((7, 7), np.uint8)# 手动创建
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
print(kernel)
res = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('img', img)
cv2.imshow('erode', res)
cv2.waitKey(0)