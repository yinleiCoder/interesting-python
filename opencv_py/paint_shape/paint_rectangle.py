import cv2
import numpy as np
"""
OpenCV绘制基本图形：矩形
    rectangle(img, 开始点， 结束点，颜色...)
"""

img = np.zeros((480, 640, 3), np.uint8)

# 画矩形坐标点(x, y)
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255), 5)
cv2.rectangle(img, (200, 200), (300, 300), (0, 0, 255), -1)

cv2.imshow('rectangle', img)
cv2.waitKey(0)


