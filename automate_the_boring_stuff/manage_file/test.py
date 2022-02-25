import shutil, os, zipfile
from pathlib import Path
"""
测试api
"""
# 复制文件和文件夹
p = Path.home() / 'Desktop'
print(shutil.copy(p/'停车费明细2.jpg', p/'新建文件夹'))# 复制文件到文件夹
print(shutil.copy(p/'停车费明细2.jpg', p/'新建文件夹'/'test.jpg'))# 复制文件到文件夹并重命名
print(shutil.copytree(p/'新建文件夹', p/'新建文件夹_backup'))# 复制文件夹及其包含的文件夹和文件

# 文件和文件夹的移动
print(shutil.move(p/'新建文件夹', p/'新名称'))# 也可以指定文件名，相当于移动并重命名,且必须存在目录

# 永久删除文件和文件夹os.unlink os.rmdir shutil.rmtree
os.unlink(p/'新建文件夹_backup'/'test.jpg')# 删除文件
os.rmdir(p/'新建文件夹_backup'/'新建文件夹')# 删除文件夹，其子文件夹和文件必须为空
shutil.rmtree(p/'新建文件夹_backup') # 删除文件夹及其他的所有文件夹和子文件

# send2trash模块安全删除，先发送到回收站而不是永久删除

# 遍历目录树
for folderName, subfolders, filenames in os.walk(p):
    print(f'当前文件夹：{folderName}')
    for subfolder in subfolders:
        print(f'文件夹{folderName}的{subfolder}子文件夹')
    for filename in filenames:
        print(f'文件夹{folderName}的{filename}文件')

# zipfile压缩文件
exampleZip = zipfile.ZipFile(p/'新名称.zip')# 读取zip文件
print(exampleZip.namelist())
print(exampleZip.getinfo('╨┬├√│╞/1071264352/╠╪└┤╡τ│Σ╡τ▒¿╧·╡Ñ.pdf').file_size)
print(exampleZip.getinfo('╨┬├√│╞/1071264352/╠╪└┤╡τ│Σ╡τ▒¿╧·╡Ñ.pdf').compress_size)

print(exampleZip.extractall('C:\\Users\\10991\\Desktop\\testtest'))# 解压缩
exampleZip.close()


