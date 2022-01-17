import cv2
import numpy as np
"""
OpenCV绘制基本图形：椭圆
    ellipse(img, 中心点， 长宽的一半，角度，从哪个角度开始，到哪个角度结束...)
"""

img = np.zeros((480, 640, 3), np.uint8)

# 画椭圆坐标点(x, y)
cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 360, (0, 0, 255))

cv2.imshow('ellipse', img)
cv2.waitKey(0)


