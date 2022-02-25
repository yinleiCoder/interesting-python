from pathlib import Path
import os
"""
api 测试
"""

# 文件路径pathlib代替旧的os.path()
print(Path('spam', 'bacon', 'eggs'))# 返回正确的操作系统的路径分隔符
print(Path(r'C:\Users\yinlei', 'test.txt'))# 连接文件夹与文件名
print(Path('spam')/'bacon'/'eggs')# /运算符连接路径
print(Path('spam')/Path('bacon/eggs'))# /运算符连接路径
print(Path('spam')/Path('bacon', 'eggs'))# /运算符连接路径
print(Path.cwd())# 当前工作目录取代os.getcwd()
os.chdir('C:\\Users\\10991')# 更改当前工作目录
print(Path.cwd())# 当前工作目录
print(Path.home())# 主目录
os.makedirs('C:\\Users\\10991\\Desktop\\tests\\subtests')# 创建新文件夹, 创建中间所有必要的中间文件夹
Path(r'C:\Users\10991\Desktop\tests2').mkdir() # 一次智能创建一个目录
print(Path.cwd().is_absolute())# 相对路径与绝对路径 os.path.abspath(path) os.path.isabs(path) os.path.relpath(path, start)
print(Path('Users\\10991').is_absolute())# 相对路径与绝对路径
print(os.path.relpath('C:\\Windows', "C:\\"))
print(os.path.relpath('C:\\Windows', "C:\\Users"))

# 取得文件路径各部分 os.path.dirname(path) os.path.basename(path)
p = Path(r'C:\Users\10991\yarn.lock')
print(p.anchor)
print(p.drive)
print(p.parent)
print(p.parents[1])
print(p.name)
print(p.stem)
print(p.suffix)
# 分割每个部分
calcFilePath = (r'C:\Users\10991\yarn.lock')
print(calcFilePath.split(os.sep))

# 查看文件大小和文件夹内容
print(os.path.getsize(r'C:\Users\10991\yarn.lock'))
print(os.listdir(r'C:\Users\10991'))

# 通配符模式修改文件列表
p = Path(r'C:\Users\10991\Desktop')
print(list(p.glob('*')))
print(list(p.glob('*.jpg')))

# 检查路径是否存在 os.path.exists(path) os.path.isfile os.path.isdir
winDir = Path(r'C:\Windows')
notExistsDir = Path(r'C:\yinlei')
print(winDir.exists())
print(winDir.is_dir())
print(winDir.is_file())
print(notExistsDir.exists())

# 文件读写 Path仅提供与文件的基本交互 写入文件常见open()
p = Path('test.txt')
print(p.write_text('Hello, World!'))
print(p.read_text())
print(p.cwd())


