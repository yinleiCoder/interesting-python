import cv2
import numpy as np
"""
OpenCV图像基本变换: 图像旋转[但是该api不能指定角度，要靠仿射变换]
    rotate(img, rotateCode)
    rotateCode: ROTATE_90_CLOCKWISE
    rotateCode: ROTATE_180
    rotateCode: ROTATE_90_COUNTERCLOCKWISE
"""
brother = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

new = cv2.rotate(brother, cv2.ROTATE_90_CLOCKWISE)
new = cv2.rotate(brother, cv2.ROTATE_180)
new = cv2.rotate(brother, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('unicom', brother)
cv2.imshow('unicom new', new)
cv2.waitKey(0)