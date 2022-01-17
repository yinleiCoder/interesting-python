import cv2
import numpy as np
"""
哈尔级联法：
    Haar是专门为解决人脸识别而推出的
    在深度学习还流行的时，Haar已可以商用
    
    detectMultiScale(img, double scaleFactor=1.1,int minNeighbors=3...)
步骤：
    创建Haar级联器
    导入图片并将其灰度化
    调用detectMultiScale进行人脸识别
    
人脸识别方法：
    哈尔级联方法
    深度学习DNN方法
"""

# 创建哈尔级联器
facer = cv2.CascadeClassifier(r'E:\PycharmProjects\funnyPython\opencv_py\opencv_machine_learning_face\haarcascades\haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(r'E:\PycharmProjects\funnyPython\opencv_py\opencv_machine_learning_face\haarcascades\haarcascade_eye.xml')
mouth = cv2.CascadeClassifier(r'E:\PycharmProjects\funnyPython\opencv_py\opencv_machine_learning_face\haarcascades\haarcascade_mcs_mouth.xml')
nose = cv2.CascadeClassifier(r'E:\PycharmProjects\funnyPython\opencv_py\opencv_machine_learning_face\haarcascades\haarcascade_mcs_nose.xml')
# 导入图片并将其灰度化
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\qianqian_face.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 调用detectMultiScale进行人脸识别
faces = facer.detectMultiScale(gray_img, 1.1, 3)
i = 0
j = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_img = img[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_img, 1.1, 3)
    for (x,y,w,h) in eyes:
        cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_eye=roi_img[y:y+h, x:x+w]
        eyename = 'eye' + str(j)
        j = j+1
        cv2.imshow(eyename, roi_eye)

    i = i+1
    winname = 'face' + str(i)
    cv2.imshow(winname, roi_img)
cv2.imshow('img', img)

cv2.waitKey()