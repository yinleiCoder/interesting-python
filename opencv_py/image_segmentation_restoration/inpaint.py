import cv2
import numpy as np
"""
图像修复：
    inpaint(img,
            mask, 
            inpaintRadius,
            flags)
    inpaintRadius: 每个点的圆形邻域半径
    flags：INPAINT_NS, INPAINT_TELEA
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\inpaint.png')
mask = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\inpaint_mask.png', 0)

result = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
cv2.imshow('inpaint', result)
cv2.waitKey(0)
