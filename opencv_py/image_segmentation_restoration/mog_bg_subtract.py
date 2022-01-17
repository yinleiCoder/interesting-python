import numpy as np
import cv2
"""
背景抠除：
    视频背景扣除原理：
        视频是一组连续的帧
        帧与帧之间关系密切GOP (关于这部分涉及音视频知识，可以看我的微信公众号 尹哥)
        在GOP中，背景几乎是不变的

方法1：MOG去背景
    混合高斯模型为基础的前景/背景分割算法
    createBackgroundSubtractorMOG(
        history, // 默认200
        nmixtures, // 高斯范围值，默认5
        backgroundRatio, //背景比率，默认0.7
        noiseSigma, // 默认0， 自动降噪    
    )
"""

cap = cv2.VideoCapture(r'E:\PycharmProjects\funnyPython\opencv_py\data\videos\qianqian4.mp4')
# mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow('img', fgmask)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()