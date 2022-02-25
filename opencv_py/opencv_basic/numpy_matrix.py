import cv2
import numpy as np
"""
矩阵的操作Numpy:
    OpenCV中用到的矩阵都要转换成Numpy数组
    Numpy是一个经高度优化的Python数组库
"""
# a = np.array([1, 2, 3])
# print(a)
#
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
#
# c = np.zeros((8, 8, 3), np.uint8)
# print(c)
#
# d = np.ones((8, 8), np.uint8)
# print(d)
#
# e = np.full((8, 8), 24, np.uint8)
# print(e)
#
# # 单位矩阵
# f = np.identity(4)
# print(f)
# # 单位矩阵非正方形
# g = np.eye(5, 7, k=1)
# print(g)

# # 从矩阵中检索与赋值
# img = np.zeros((480, 640, 3), np.uint8)
# print(img[100, 100])# [y, x, channel]
# count = 0
# while count < 200:
#     img[count, 100, 0] = 255
#     count += 1
#
# cv2.imshow('img', img)
# key = cv2.waitKey(0)
# if key & 0xFF == ord('q'):
#     cv2.destroyAllWindows()

# 获取子矩阵Region of Image(ROI)
# OpenCV中如果想对图像中的某个区域进行修改的话，需要先将这个区域找到，然后再对里面的内容做修改
# ROI是OpenCV中特别重要的一个概念，比如在图像中添加水印，对这图像中的某一块进行修改等都需要使用ROI
#[y1:y2, x1:x2] [:, :]
img = np.zeros((480, 640, 3), np.uint8)
roi = img[100:400, 100:600]
roi[:, :] = [0, 0, 255]
roi[10:200, 10:200] = [0, 255, 0]
cv2.imshow('img', roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()
