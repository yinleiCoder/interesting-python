import cv2
import numpy as np
"""
OpenCV绘制基本图形：直线
    line(img, 开始点， 结束点，颜色, 线宽，线型，坐标缩放比例...)
"""

img = np.zeros((480, 640, 3), np.uint8)

# 画线坐标点(x, y)
cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5)

cv2.imshow('line', img)
cv2.waitKey(0)


