import zipfile, os
"""
将一个文件夹备份到一个ZIP文件:
    假如你有一个文件夹保存在本地，文件夹里面是我弟弟的照片。
    你担心照片和视频会丢失，因此希望为整个文件夹创建一个zip文件以作为快照。
    希望保存不同的版本，希望zip文件的文件名每次创建时都有所变化。如yinzihao_1.zip、yinzihao_2.zip
    如果手动去做这件事，很可能会不小心弄错zip文件的编号。
Usage: python copy_dir_to_zip.py
"""
# 弄清楚zip文件的名称
def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    # 创建新zip文件
    print(f"Creating {zipFileName}...")
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    # 遍历目录数并添加到zip文件
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):# 以前备份过的不要
                continue
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
    print('Done')

if __name__ == '__main__':
    backupToZip(r"C:\Users\10991\Desktop\尹磊相册\yinzihao")