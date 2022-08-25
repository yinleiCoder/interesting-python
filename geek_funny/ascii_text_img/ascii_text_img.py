import sys, random, argparse
import numpy as np
import math
from PIL import Image

"""
ASCII文本图形:
    ASCII文本图形的源头是19世纪后期出现的打字机文本图形。20世纪60年代，计算机有了较弱的图形处理硬件，ASCII被用于表示图形。
    今天，ASCII文本图形继续作为因特网上的一种表现形式。
    功能：从图像生成ASCII文本图形。指定输出文本列数的宽度，并设置垂直比例因子，支持2种灰度值到ASCII字符的映射：稀疏的10级映射和更精细校正的70级映射。
    
    知识点：
        用Pillow将彩色图像转换为灰度图像，它是PIL库的一个分支
        numpy计算灰度图像的平均亮度
        使用一个字符串作为灰度值的快速查找表
        
    原理：从远处看，我们将灰度图像看成是他们亮度的平均值。将图像分割成小块，并用ascii字符替换一小块的平均RGB值。
        从远处看，因为眼睛的分辨率有限，我们大致会丢失细节，看到的ASCII文本图形中的平均值，否则文本图形看起来就不那么真实。
        将给定的图像先转换为8位的灰度，让每个像素有一个灰度值，范围是[0,255].
        将这个8位值看成是亮度，0表示黑色，255表示白色，中间值是不同程度的灰色。
        将该图像分割成MXN个小块构成的网格，然后程序计算网格中每个小块的平均亮度值，通过预定义的一些有梯度的ASCII字符来表示[0,255]范围的灰度值，与适当的ASCII字符匹配，它将用这些值作为亮度值的查找表。
        完成的ASCII文本图形只是一些文本行，要显示文本，就要用到Courier这样的等宽字体，因为如果每个文本字符宽度不相同，图像中字符将无法正确的按网格排列，会得到间隔不均和失真的输出。
        所用字体的"纵横比"也会影响最终图像，如果一个字符所占空间的纵横比与该字符取代的图像小块的纵横比不同，则最终的ASCII字符图形会出现失真。
        实际上，试图用一个ASCII字符来替换图像小块，所以他们的形状要匹配。
        为了解决这个问题，需要缩放网格中的行数，以匹配Courier的长宽比。
    
    步骤：
        将输入图像转为灰度
        将图像分为MxN个小块
        修正M行数，以匹配图像和字体的纵横比
        计算每个小块图像的平均亮度，然后为每个小块查找合适的ASCII字符
        汇集各行ASCII字符串，将他们打印到文件，形成最终图像
    
    要了解如何用字符表示灰度值的更多内容，参见http://paulbourke.net/dataformats/asciiart
    
    Usage:
        python .\ascii_text_img.py --file .\meinv.jpeg --cols 100
"""

# 定义灰度等级和网格。灰度等级用于将亮度值转换为ASCII字符
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."  # 70级灰度梯度
gscale2 = " .:-=+*#%@"  # 10级灰度梯度



def getAverageL(image):
    """
    计算平均亮度
    :param image:
    :return:
    """
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))


def convertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dimensions(rows, cols), returns an m*n list of Images
    :param fileName:
    :param cols:
    :param scale:
    :param moreLevels:
    :return:
    """
    global gscale1, gscale2
    # 将图像转为灰度图像。L代表Luminance,是图像亮度的单位
    image = Image.open(fileName).convert('L')
    # 保存输入图像的宽高
    W, H = image.size[0], image.size[1]
    print(f"input image dims: {W} x {H}")
    # 根据用户指定的列数计算小块的宽度
    w = W / cols
    # 利用垂直比例系数计算高度
    h = w / scale
    # 利用网格的高度计算行数
    rows = int(H/h)
    print(f"cols: {cols}, rows: {rows}")
    print(f"tile dims: {w} x {h}")
    if cols > W or rows > H:
        print("Image too small for specified cols")

    # an ASCII image is a list of character strings
    aimgs = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        # correct the last tile
        if j == rows-1:
            y2 = H
        aimgs.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
            # correct the last tile
            if i == cols-1:
                x2 = W
            # crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # get the average luminance
            avg = int(getAverageL(img))
            # look up the ASCII character for grayscale value(avg)
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            # append the ascii character to the string
            aimgs[j] += gsval
    return aimgs

def main():
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--output', dest='outputFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')
    args = parser.parse_args()
    imgFile = args.imgFile
    outputFile = 'output.txt'
    if args.outputFile:
        outputFile = args.outputFile
        # set scale default as 0.43, which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    cols = 80
    if args.cols:
        cols = int(args.cols)
    print('generating ASCII art...')
    aimg = convertImageToAscii(imgFile, cols, scale, args.moreLevels)
    with open(outputFile, 'w') as f:
        for row in aimg:
            f.write(row+'\n')
    print(f'ascii art written to {outputFile}')


if __name__ == '__main__':
    main()
