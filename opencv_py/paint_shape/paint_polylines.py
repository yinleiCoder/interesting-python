import cv2
import numpy as np
"""
OpenCV绘制基本图形：多边形
    polylines(img, 点集， 是否闭环，颜色...)
    fillPoly(img, 点集， 颜色)填充多边形
"""

img = np.zeros((480, 640, 3), np.uint8)
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# 画多边形坐标点(x, y)
cv2.polylines(img, [pts], True, (0, 0, 255), 5)
# 填充多边形
cv2.fillPoly(img, [pts], (255, 0, 0))

cv2.imshow('polylines', img)
cv2.waitKey(0)


