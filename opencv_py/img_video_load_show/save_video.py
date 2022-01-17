import cv2
"""
OpenCV将视频数据录制成多媒体文件：
    VideoWriter
    write
    release
"""

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# 参数1：输出文件
# 参数2：多媒体文件格式
# 参数3：帧率
# 参数4：电脑摄像头的分辨率
vw = cv2.VideoWriter(r'C:\Users\10991\Desktop/out00.mp4', fourcc, 25, (640, 480))

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

#从电脑摄像头获取视频设备
cap = cv2.VideoCapture(0)

#判断摄像头是否打开
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('video', frame)
        # 写数据到多媒体文件
        vw.write(frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            cap.release()
            vw.release()
            cv2.destroyAllWindows()
            break
    else:
        break