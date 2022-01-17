import cv2
import numpy as np

"""
车辆统计：
1. 图像运算
2. 去除背景(论文：An improved adaptive background mixture model for real-time tracking with shadow detection)
2. 形态学识别车辆
3. 轮廓查找进行统计车辆信息
"""

def vehicle_center(x, y, w, h):
    """
    将车的中心看成一个点，来判断是否过线
    :param x:
    :param y:
    :param w:
    :param h:
    :return:
    """
    return x + int(w / 2), y + int(h / 2)

cap = cv2.VideoCapture(r'E:\PycharmProjects\funnyPython\opencv_py\data\videos\vechile.mp4')

# 去除背景
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

# 形态学kernel卷积
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

cars = []
car_number = 0
while True:
    ret, frame = cap.read()
    close = None
    if ret:
        # 灰度化
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(frame.shape)# (720, 1280, 3)
        # 高斯去噪
        blur = cv2.GaussianBlur(frame, (5, 5), sigmaX=8)
        # 去背景
        mask = bgsubmog.apply(blur)
        # 形态学处理：腐蚀
        erode = cv2.erode(mask, kernel)
        # 膨胀还原图像
        dilate = cv2.dilate(erode, kernel, iterations=2)
        # 闭操作去除车辆内部的噪音小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        for _ in range(2):
            close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
        # 查找轮廓
        contours, hierarchy = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 画标准线
        cv2.line(frame, (10, 600), (1270, 600), (255, 255, 0), 3)
        for index, contour in enumerate(contours):
            # 画出最大外接矩形
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if w < 90 or h < 90:# 去除不必要的错误识别
                continue
            vehicle_point = vehicle_center(x, y, w, h)
            cars.append(vehicle_point)
            for x, y in cars:
                # 判断车辆是否过线
                if 600 + 3 > y > 600 - 3:
                    car_number += 1
                    cars.remove((x, y))
                    # print(car_number)
        cv2.putText(frame, f'Cars Number: {car_number}', (600, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('vehicle frame', frame)
        cv2.imshow('vehicle', mask)
        # cv2.imshow('erode', erode)
        # cv2.imshow('dilate', dilate)
        # cv2.imshow('close', close)
    key = cv2.waitKey(1)
    if key == 27:  # esc
        break

cap.release()
cv2.destroyAllWindows()