import os.path

from PIL import ImageColor, Image, ImageDraw, ImageFont
"""
pillow操作图像：
    pillow的模块名称是PIL,是保持了老模块Python Imaging Library的向后兼容。
pip install pillow
"""
# 获取rgba
print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))

# 坐标和box元组: 左上角为原点，4个整数表示左、顶、右、底

# 操作图像
yinIm = Image.open('yinlei.jpg')

# 处理Image数据类型
print(yinIm.size)
print(yinIm.filename)
print(yinIm.format)
print(yinIm.format_description)
yinIm.save('yinleilei.jpg')


# 新建图像
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# 裁剪图像
croppedIm = yinIm.crop((335, 345, 1000, 1000))
croppedIm.save('cropped.png')

# 复制和粘贴图像到其他图像
yinCopyIm = yinIm.copy()
yinCopyIm.paste(croppedIm, (0, 0))
yinCopyIm.save('pasted.png')

# 循环复制粘贴平铺
yinImWidth, yinImHeight = yinIm.size
croppedImWidth, croppedImHeight = croppedIm.size
yinCopyTwo = yinIm.copy()
for left in range(0, yinImWidth, croppedImWidth):
    for top in range(0, yinImHeight, croppedImHeight):
        print(left, top)
        yinCopyTwo.paste(croppedIm, (left, top))
yinCopyTwo.save('tiled.png')

# 调整图像大小
width, height = yinIm.size
quartersizedIm = yinIm.resize((int(width / 2), int(height/2)))
quartersizedIm.save('scale.png')
svelteIm = yinIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# 旋转图像
yinIm.rotate(90).save('rotated90.png')
yinIm.rotate(6, expand=True).save('rotated6_expanded.png')

# 翻转
yinIm.transpose(Image.FLIP_LEFT_RIGHT).save('hor_flip.png')
yinIm.transpose(Image.FLIP_TOP_BOTTOM).save('ver_flip.png')

# 更改单个像素,一次绘制一个像素不是很方便，如果绘制形状，使用ImageDraw模块
print(yinIm.getpixel((0, 0)))
for x in range(100):
    for y in range(50):
        yinIm.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
print(yinIm.getpixel((0, 0)))
yinIm.save('putpixel.png')

# 图像上绘画
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i-100)], fill='green')
im.save('drawing.png')

# 绘制文本
draw.text((20, 150), 'Hello', fill='black')
fontsFolder = 'FONT_FOLDER'
ariaFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'World!', fill='gray', font=ariaFont)
im.show('text.png')
