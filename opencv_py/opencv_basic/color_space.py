import cv2
"""
OpenCV的色彩空间及其色彩空间变换:
    RGB与BGR

RGB: 人眼的色彩空间
OpenCV默认使用BGR
OpenCV最常用：HSV/HSB/HSL、YUV（视频）

HSV:(opencv)
    Hue——色相，即色彩，如红色、蓝色
    Saturation——饱和度，颜色的纯度
    Value——明度

HSL:
    Hue——色相，即色彩，如红色、蓝色
    Saturation——饱和度，颜色的纯度
    Ligthness——亮度

YUV（视频）:
    YUV4:2:0
    YUV4:2:2
    YUV4:4:4
"""

def callback():
    pass

cv2.namedWindow('color', cv2.WINDOW_NORMAL)
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

# 色彩空间的转换
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL,
               cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces)-1, callback)

while True:
    index = cv2.getTrackbarPos('curcolor', 'color')

    # 色彩空间的转换
    cvt_img = cv2.cvtColor(img, colorspaces[index])

    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
