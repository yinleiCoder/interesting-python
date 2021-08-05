"""
小型动画程序，创建往复的锯齿形图案

Usage:
"""

import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == 10:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()