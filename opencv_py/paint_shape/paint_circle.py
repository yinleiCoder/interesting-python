import cv2
import numpy as np
"""
OpenCV绘制基本图形：圆
    circle(img, 圆心点，半径，颜色...)
"""

img = np.zeros((480, 640, 3), np.uint8)

# 画圆坐标点(x, y)
cv2.circle(img, (int(640/2), int(480/2)), 100, (0, 0, 255), 5)

cv2.imshow('circle', img)
cv2.waitKey(0)


