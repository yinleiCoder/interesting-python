import cv2
import numpy as np
"""
黑帽：
黑帽= 原图 - 闭运算
morphologyEx(img, MORPH_BLACKHAT, kernel)
保留噪点
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\dotinj.png')

# kernel = np.ones((7, 7), np.uint8)# 手动创建
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
print(kernel)
res = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.waitKey(0)