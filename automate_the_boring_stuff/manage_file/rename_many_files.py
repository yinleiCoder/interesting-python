import shutil, os, re
"""
将带有美国风格日期的文件重命名为欧洲风格日期:
    假设你的领导用电子右键发给你上千个文件，
    文件名包含美国风格的日期(MM-DD-YYYY),需要将他们重命名为欧洲风格的日期(DD-MM-YYYYY)
    手动完成这个繁琐的任务可能需要几天的时间。
    1. 检查当前工作目录的所有文件名，寻找美国风格的日期
    2. 如果找到，将该文件重命名，交换月份和日期的位置，使之成为欧洲风格的日期
Usage: python rename_many_files.py
"""
# 为美国风格的日期创建一个正则表达式
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)- #one or two digits for the month
    ((0|1|2|3)?\d)- #one or two digits for the day
    ((19|20)\d\d) #four digits for the year
    (.*?)$ # all text after the date
""", re.VERBOSE)
# 识别文件名中的日期部分
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo is None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # 构成新文件名，并对文件重命名
    euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    shutil.move(amerFilename, euroFilename)