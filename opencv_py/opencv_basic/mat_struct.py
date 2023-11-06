import cv2
import numpy as np
"""
OpenCV的重要结构体Mat及其深浅拷贝:

Mat: 就是一个矩阵，可以通过numpy对其以矩阵的方式进行访问

Mat底层实现：
    Header
      |
      |
    Data
class CV_EXPORTS Mat {
public:
    ...
    int dims; //维数
    int rows, cols; //行列数
    uchar *data; //存储数据的指针
    int *refcount;//引用计数
    // depth: 像素的位深
    // channels: 通道数RGB是3
    // size：矩阵大小
    // type: dep+dt+chs CV_8UC3
    ...
}

浅拷贝(C++)：
    Mat A
    A = imread(file, IMREAD_COLOR)
    Mat B(A)
深拷贝(C++):
    cv::Mat::clone()
    cv::Mat::copyTo()
    copy() [python]
    
OpenCV中imread返回的就是Mat结构体，当我们需要对原始图像进行修改时用深拷贝，
而不想影响原始图像时用深拷贝。
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
# 访问图像Mat的属性
print(img.shape)
print(img.size)
print(img.dtype)
#浅拷贝: 发现结果一样
img2 = img
#深拷贝：结果不一样
img3 = img.copy()

img[10:100, 10:100] = [0, 0, 255]
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
