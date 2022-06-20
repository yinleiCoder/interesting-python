import os
import time
from pathlib import Path

from PIL import ImageColor, Image, ImageDraw, ImageFont

def handle_imgs_concat(filenames, vertical=True):
    """
    处理一批图片的拼接
    :param filenames:
    :return:
    """
    someIms = [Image.open(Path.cwd() / Path('docs') / Path(filename)) for filename in filenames]
    if vertical:
        temp_increase_height = 0
        # 竖直拼接，宽度不变，高度变化
        im_heights = [oneIm.size[1] for oneIm in someIms]
        new_height = sum(im_heights)
        new_width = someIms[0].size[0]
        new_im = Image.new('RGBA', (new_width, new_height), 'white')
        for index, one_im in enumerate(someIms):
            one_copy_im = one_im.copy()
            new_im.paste(one_copy_im, (0, temp_increase_height))
            temp_increase_height += im_heights[index]
        new_im.save(f'vertical_concat_{time.time()}.png')
    else:
        pass

if __name__ == '__main__':
    docs_dir = Path.cwd() / Path('docs')
    judge_names, doc_analzy_names = os.listdir(docs_dir)[:2], os.listdir(docs_dir)[2:]
    handle_imgs_concat(judge_names)
    handle_imgs_concat(doc_analzy_names)