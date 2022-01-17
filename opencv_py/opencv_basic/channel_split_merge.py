import cv2
import numpy as np
"""
OpenCV: 通道的分割与合并
    split(mat)
    merge((ch1,ch2...))
"""

img = np.zeros((480, 640, 3), np.uint8)

# 通道的分割
b, g, r = cv2.split(img)
b[10:100, 10:100] = 255
g[10:100, 10:100] = 255

# 通道的合并
img2 = cv2.merge((b, g, r))

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('img2', img2)
cv2.waitKey(0)

