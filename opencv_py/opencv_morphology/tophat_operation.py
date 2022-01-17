import cv2
import numpy as np
"""
顶帽：
顶帽= 原图 - 开运算
morphologyEx(img, MORPH_TOPHAT, kernel)
保留噪点
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\tophat.png')

# kernel = np.ones((7, 7), np.uint8)# 手动创建
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19))
print(kernel)
res = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('erode', res)
cv2.waitKey(0)