import os
import cv2
import paddlehub

'''
OCR解决增值税发票内容文本识别：
方案1：找个现成的财务OCR票据模型，比如经典的CTRN+CRNN
方案2：百度OCR，Github PaddleOCR2.X,采用DB+CRNN（但是字段无序，很多东西识别不出来）
还有个issue，就是手机拍的或者扫描件拍的弯曲的话咋个识别？
[思路]：考虑对图像进行预处理，
根据标准的增值税发票，发票每一块区域的位置都是固定的，
发票中的名称、纳税人识别号等都在固定的区域，可以考虑将每个区域单独切分扔进模型识别训练，
针对财务票据模型，可以自己去找数据集训练模型,弯曲的手机拍的图片可以考虑用寻找轮廓+透视变换拉平+划分区域。

这里我不想造轮子，可以采用百度飞桨PaddleHub下的预训练模型，他下面有很多预训练模型。
paddleHub：https://www.paddlepaddle.org.cn/hub
paddleHub列表：https://www.paddlepaddle.org.cn/hublist
踩坑：PaddleHub依赖shapely、pyclipper库
pip install shapely 
pip install pyclipper
'''


class ChinaUnicomBillOCR:
    def __init__(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        imgs_filename = os.listdir(f'{current_path}\\china_unicom_bill_imgs')
        all_imgs_path = [os.path.join(f'{current_path}\\china_unicom_bill_imgs\\', f) for f in imgs_filename]

        ocr = paddlehub.Module(name="chinese_ocr_db_crnn_server")
        np_imgs = [cv2.imread(item) for item in all_imgs_path]
        result = ocr.recognize_text(
            images=np_imgs,
            use_gpu=False,
            visualization=True,
            box_thresh=0.3,
            text_thresh=0.5
        )
        for item in result[0]['data']:
            # print(f"{item['text']}")
            print(f"{item}")
        # 对齐文本行



if __name__ == '__main__':
    china_unicom_bill_ocr = ChinaUnicomBillOCR()
