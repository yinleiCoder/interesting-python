import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

"""
照片马赛克：
    照片马赛克是一张图像，它被分割成长方形的网格，每个长方形由另一张匹配“目标”的图像替代。
    如果从远处看照片马赛克，会看到目标图像；如果走近，会看到该图像实际上包含许多较小的图像。
    将目标图像划分成较小图像的网格，并用恰当的图像替换网格中的每一小块，创建原始图像的照片马赛克。
    可以指定网格的尺寸，并选择输入图像是否可以在马赛克中重复使用。

    知识点：
        PIL创建图像
        计算图像的平均RGB
        剪切图像
        通过粘贴另一张图像来替代原图像的一部分
        利用平均距离测量来比较RGB值

    原理：
        从目标图像的块状低分辨率版开始(高分辨率的图像，小块图像的数量会太大)
        该图像的分辨率将决定马赛克的维度MxN
        接着根据这种方法替换原始图像中的每一小块：
            1. 读入一些小块图像，他们将取代原始图像中的小块
            2. 读入目标图像，将他们分割成MxN的小块网格
            3. 对于每个小块，从输入的小块图像中找到最佳匹配(平均颜色值)
                计算一个像素中RGB值之间的距离，以便从输入图像中找到最佳匹配。
                对于几何中的三维点，可以用一下的距离计算方法：
                    D1,2 = √(r1-r2)^2+(g1-g2)^2+(b1-b2)^2
            4. 将选择的输入图像安排在MxN的网格中，创建最终的照片马赛克
        下标为(i,j)的小块，左上角坐标为(i*w, i*j), 右下角坐标((i+1)*w, (j+1)*h)
"""


def getAverageRGB(image):
    """
    计算输入图像的平均颜色值
    :param image:
    :return:
    """
    im = np.array(image)
    w, h, d = im.shape
    return tuple(np.average(im.reshape(w*h, d), axis=0))


def splitImage(image, size):
    """
    将目标图像分割成网格
    :param image:
    :param size:
    :return:
    """
    # 目标图像的维度
    W, H = image.size[0], image.size[1]
    # 尺寸
    m, n = size
    # 计算目标图像中每一小块的尺寸
    w, h = int(W/n), int(H/m)
    imgs = []
    for j in range(m):
        for i in range(n):
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs

def getImages(imageDir):
    """
    读入小块图像
    :param imageDir:
    :return:
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            with open(filePath, "rb") as f:
                im = Image.open(f)
                images.append(im)
                im.load()# 强制加载im中的图像数据
        except:
            print(f'Invalid image: {filePath}')
    return images


def getImageFilenames(imageDir):
    """
    given a directory of images, return a list of image filenames
    :param imageDir:
    :return:
    """
    files = os.listdir(imageDir)
    filenames = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            imgType = imghdr.what(filePath)
            if imgType:
                filenames.append(filePath)
        except:
            print(f'Invalid image: {filePath}')
    return filenames

def getBestMatchIndex(input_avg, avgs):
    """
    寻找小块的最佳匹配
    :param input_avg:
    :param avgs:
    :return:
    """
    avg = input_avg
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0])*(val[0]-avg[0]) +
                (val[1] - avg[1])*(val[1]-avg[1]) +
                (val[2] - avg[2])*(val[2]-avg[2]))
        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1
    return min_index

def createImageGrid(images, dims):
    """
    创建图像网格
    :param images:
    :param dims:
    :return:
    """
    # 取得网格的尺寸
    m, n = dims
    assert m*n == len(images)
    # 计算小块图像的最大宽度和高度
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])
    grid_img = Image.new('RGB', (n*width, m*height))
    for index in range(len(images)):
        row = int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))
    return grid_img


def createPhotomosaic(target_image, input_images, grid_size, reuse_images=True):
    """
    创建照片马赛克
    :param target_image:
    :param input_images:
    :param grid_size:
    :param reuse_images: 是否可以复用
    :return:
    """
    print("splitting input image...")
    target_images = splitImage(target_image, grid_size)
    print('finding image matches...')
    output_images = []
    count = 0
    batch_size = int(len(target_images)/10)
    avgs = []
    for img in input_images:
        avgs.append(getAverageRGB(img))
    for img in target_images:
        avg = getAverageRGB(img)
        match_index = getBestMatchIndex(avg, avgs)
        output_images.append(input_images[match_index])
        if count > 0 and batch_size > 10 and count % batch_size is 0:
            print(f'processed {count} of {len(target_images)}...')
        count += 1
        if not reuse_images:
            input_images.remove(match_index)
    print('creating mosaic...')
    mosaic_image = createImageGrid(output_images, grid_size)
    return mosaic_image

def main():
    pass


if __name__ == '__main__':
    main()
