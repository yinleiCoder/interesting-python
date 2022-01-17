import cv2
"""
OpenCV从摄像头采集视频/或从多媒体文件中读取视频帧:
    VideoCapure()
    cap.read()
    cap.release()
"""
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)
#获取视频设备
cap = cv2.VideoCapture(0)
#从多媒体文件中读取视频帧
# cap = cv2.VideoCapture(r'C:\Users\10991\Desktop\尹磊相册\yinzihao\yinzihao.mp4')

while cap.isOpened():
    #从摄像头读取视频帧
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

