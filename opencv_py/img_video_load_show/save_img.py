import cv2
"""
OpenCV保存图片：
    imwrite(name, img) [img是Mat类型]
    
"""
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(r"E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png")

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite(r"C:\Users\10991\Desktop/yinzihao.png", img)
    else:
        print(key)