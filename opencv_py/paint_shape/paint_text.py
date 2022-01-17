import cv2
import numpy as np
"""
OpenCV绘制基本图形：文本
    putText(img, 字符串，起始点， 字体，字号...)
"""

img = np.zeros((480, 640, 3), np.uint8)

# 画矩形坐标点(x, y)
cv2.putText(img, "Yin Lei", (10, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0))

cv2.imshow('text', img)
cv2.waitKey(0)


