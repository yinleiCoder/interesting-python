import cv2
import numpy as np
import pytesseract
"""
Haar + Tesseract车牌识别:
    通过Haar定位车牌的大体位置
    对车牌进行预处理
        车牌二值化处理
        形态学处理
        滤波去除噪点
        缩放
    调用tesseract进行文字识别
        brew install tesseract tesseract-lang
        pip3 install pytesseract
"""
# 创建哈尔级联器
plate = cv2.CascadeClassifier(r'E:\PycharmProjects\funnyPython\opencv_py\opencv_machine_learning_face\haarcascades\haarcascade_russian_plate_number.xml')
# 导入图片并将其灰度化
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\car.jpg')
img = cv2.resize(img, (480, 640))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 调用detectMultiScale进行检测车牌的位置
car_numbers = plate.detectMultiScale(gray_img, 1.1, 3)
for (x, y, w, h) in car_numbers:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 对获取到的车牌进行预处理
# 提取roi
roi = gray_img[y:y+h, x:x+w]
# 二值化
ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(pytesseract.image_to_string(roi, lang='chi_sim+eng', config='--psm 8 --oem 3'))

cv2.imshow('roi_bin', roi_bin)
cv2.imshow('img', img)
cv2.waitKey()