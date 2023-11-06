import os
import abc
import datetime
import random
import subprocess
import time
from pathlib import Path
import cv2

import paddlehub as hub

"""

Docs：
    https://www.paddlepaddle.org.cn/tutorials/projectdetail/3991855#anchor-7
Usage:
    pip install --upgrade paddlepaddle -i https://mirror.baidu.com/pypi/simple
    pip install --upgrade paddlehub -i https://mirror.baidu.com/pypi/simple
    hub install deeplabv3p_xception65_humanseg
"""


class BaseAI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        pass


class CvPaddle(BaseAI):

    def __init__(self, use_ffmpeg=False, data_path=None):
        self.ffmpeg_flag = use_ffmpeg
        self.human_seg = hub.Module(name="deeplabv3p_xception65_humanseg")
        self.human_datasetpath = Path(data_path)

    def cvt_video_toimg(self):
        human_videos = []
        if self.ffmpeg_flag and self.human_datasetpath.exists() and self.human_datasetpath.is_dir():
            for file_path in self.human_datasetpath.glob('*.mp4'):
                human_videos.append(os.path.join(self.human_datasetpath, os.path.basename(file_path)))
            for i in range(len(human_videos)):
                ffmpeg_cmd = f"ffmpeg -i {human_videos[i]} -vf \"select='eq(pict_type,PICT_TYPE_I)'\" -vsync vfr " \
                             f"{os.path.join(self.human_datasetpath, str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + str(random.randint(0, 999)))}%04d.png"
                proc = subprocess.Popen(ffmpeg_cmd, shell=True)
        else:
            print('you must point out right ffmpeg_flag and data_path.')

    def run(self):
        girl_imgs = [os.path.join(self.human_datasetpath, filename) for filename in os.listdir(self.human_datasetpath)
                     if filename.endswith('png')]
        save_path = self.human_seg.segmentation(paths=girl_imgs, visualization=True, output_dir='humanseg_output',
                                                batch_size=3)
        print(save_path)


if __name__ == '__main__':
    cv_paddle = CvPaddle(use_ffmpeg=False, data_path=os.path.realpath('data'))
    cv_paddle.cvt_video_toimg()
    cv_paddle.run()
