import cv2
import numpy as np

"""
GrabCut法：通过交互的方式获得前景物体。【如PS抠图】
    用户指定前景的大体区域，剩下的为背景区域
    用户还可以明确指定某些地方为前景或背景
    GrabCut采用分段迭代的方法分析前景物体形成模型树
    最后根据权重决定某个像素是前景还是背景
grabCut(img, mask, rect, bgdModel, fgdModel, 5,//iterator,mode )
    mask生成的掩码：
        BGD背景0
        FGD前景1
        PR_BGD可能是背景2
        PR_FGD可能是前景3
    bgdModel： np.float64 type zero arrays of size(1, 65)
    mode: GC_INIT_WITH_RECT
          GC_INIT_WITH_MASK
"""
class GrabCutApp:
    startX = 0
    startY = 0
    flag_rect = False
    rect = (0, 0, 0, 0)
    def onmouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
        elif event == cv2.EVENT_LBUTTONUP:
            self.flag_rect = False
            cv2.rectangle(self.img, (self.startX, self.startY), (x, y), (0, 0, 255), 3)
            self.rect = (min(self.startX, x), min(self.startY, y), abs(self.startX - x), abs(self.startY - y))
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect:
                self.img = self.copy_img.copy()
                cv2.rectangle(self.img, (self.startX, self.startY), (x, y), (255, 0, 0), 3)

    def run(self):
        cv2.namedWindow('input')
        cv2.setMouseCallback('input', self.onmouse)
        self.img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao2.png')
        self.copy_img = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)
        while True:
            cv2.imshow('input', self.img)
            cv2.imshow('output', self.output)
            k = cv2.waitKey(100) & 0xFF
            if k == ord('g'):
                bgdmodel = np.zeros((1, 65), np.float64)
                fgdmodel = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.copy_img, self.mask, self.rect,
                            bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
                mask2 = np.where((self.mask==1)|(self.mask==3), 255, 0).astype('uint8')
                self.output = cv2.bitwise_and(self.copy_img, self.copy_img, mask=mask2)
if __name__ == '__main__':
    GrabCutApp().run()