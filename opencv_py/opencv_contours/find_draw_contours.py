import cv2
import numpy as np

"""
目标识别：图像轮廓(查找轮廓、绘制轮廓、轮廓的面积与周长)
    具有相同颜色或强度的连续点的曲线

轮廓作用：
    用于图形分析
    物体的识别与检测

注：为了检测的准确性，需要先对图像进行二值化或Canny操作，画轮廓时会修改输入的图像。

轮廓查找：
    contours, hierarchy = findContours(img, mode, ApproximationMode...)
    mode: 
        RETR_EXTERNAL=0,只检测外轮廓
        RETR_LIST=1,检测的轮廓不建立等级关系
        RETR_CCOMP=2,每层最多2级
        RETR_TREE=3,按树形存储轮廓
    ApproximationMode：
        CHAIN_APPROX_NONE,保存所有轮廓上的点
        CHAIN_APPROX_SIMPLE,只保存角点

绘制轮廓：
    drawContours(img, contours, contourIdx, color, thickness...)
    contourIdx: -1表示绘制所有轮廓
    color: 颜色(0, 0, 255)
    thickness: 线宽，-1是全部填充
    
轮廓的面积：
    contourArea(contour)

轮廓的周长：
    arLength(curve, closed)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\contours1.jpeg')
print(img.shape)

# 转变为单通道
gary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gary_img.shape)

# 二值化
ret, binary = cv2.threshold(gary_img, 150, 255, cv2.THRESH_BINARY)
print(binary.shape)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

# 计算面积
area = cv2.contourArea(contours[0])
print(f"面积：{area}")

# 计算周长
length = cv2.arcLength(contours[0], True)
print(f"周长：{length}")

cv2.imshow('img', img)
# cv2.imshow('bin', binary)
cv2.waitKey(0)
