import numpy as np
import cv2
"""
背景抠除：
    视频背景扣除原理：
        视频是一组连续的帧
        帧与帧之间关系密切GOP (关于这部分涉及音视频知识，可以看我的微信公众号 尹哥)
        在GOP中，背景几乎是不变的

方法1：MOG2去背景
    同MOG类似，不过对亮度产生的阴影有更好的识别
    createBackgroundSubtractorMOG2(
        history, // 500毫秒
        ...
        detectShadows// 是否检测阴影，True
    )
    但会产生很多噪点。
方法2：GMG去背景
    静态背景图像估计和每个像素的贝叶斯分割抗噪性更强
    createBackgroundSubtractorGMG(
        initializationFrames, // 初始帧，120
        ....
    )
    
"""

cap = cv2.VideoCapture(r'E:\PycharmProjects\funnyPython\opencv_py\data\videos\qianqian4.mp4')
# mog = cv2.bgsegm.createBackgroundSubtractorMOG()
# mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.bgsegm.createBackgroundSubtractorGMG()

while True:
    ret, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow('img', fgmask)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()