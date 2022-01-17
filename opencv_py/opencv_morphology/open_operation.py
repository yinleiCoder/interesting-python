import cv2
import numpy as np
"""
开运算：
开运算= 腐蚀 + 膨胀 (先腐蚀再膨胀)
morphologyEx(img, MORPH_OPEN, kernel)

"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\dotj.png')

# kernel = np.ones((7, 7), np.uint8)# 手动创建
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
print(kernel)
res = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('img', img)
cv2.imshow('erode', res)
cv2.waitKey(0)