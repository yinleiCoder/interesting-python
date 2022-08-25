import os
import time
from pathlib import Path

from PIL import ImageColor, Image, ImageDraw, ImageFont

def handle_imgs_concat(filenames, vertical=True):
    """
    处理一批图片的拼接v1.0.1 宽高各异
    :param filenames:
    :return:
    """
    someIms = [Image.open(Path.cwd() / Path('docs') / Path(filename)) for filename in filenames]
    origin_width_heights = [(oneIm.size[0], oneIm.size[1]) for oneIm in someIms]
    origin_widths = [item[0] for item in origin_width_heights]
    origin_heights = [item[1] for item in origin_width_heights]
    sum_width = sum(origin_widths)
    sum_height = sum(origin_heights)
    print(origin_widths, origin_heights)
    if vertical:# 竖直拼接
        temp_increase_height = 0
        res_im_width = max(origin_widths)
        res_im = Image.new('RGBA', (res_im_width, sum_height), 'white')
        for index, one_im in enumerate(someIms):
            one_copy_im = one_im.copy()
            res_im.paste(one_copy_im, (0, temp_increase_height))
            temp_increase_height += origin_heights[index]
        res_im.save(f'vertical_concat_{time.time()}.png')
    else:# 水平拼接
        temp_increate_width = 0
        res_im_height = max(origin_heights)
        res_im = Image.new('RGBA', (sum_width, res_im_height), 'white')
        for index, one_im in enumerate(someIms):
            one_copy_im = one_im.copy()
            res_im.paste(one_copy_im, (temp_increate_width, 0))
            temp_increate_width += origin_widths[index]
        res_im.save(f'horizontal_concat_{time.time()}.png')

if __name__ == '__main__':
    docs_dir = Path.cwd() / Path('docs')
    yinzihao_names = os.listdir(docs_dir)[:4]
    handle_imgs_concat(yinzihao_names, vertical=False)
    handle_imgs_concat(yinzihao_names)
