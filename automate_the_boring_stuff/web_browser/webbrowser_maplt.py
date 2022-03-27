import webbrowser
import pyperclip
import sys
"""
webbrowser打开剪贴板中的内容对应的浏览器地图：
    webbrowser模块中的open()可以启动一个新浏览器来打开指定的URL。
    1.从命令行参数或剪贴板中取得街道地址
    2.打开web浏览器，指向该地址的高德地图页面
    
    流程：
    1. 从sys.argv读取命令行参数
    2. 读取剪贴板内容
    3. 调用webbrowser.open()打开外部浏览器

如果没有这个程序，那么你需要手动取得地图：
    1. 高亮标记地址
    2. 复制地址
    3. 打开web浏览器
    4. 打开Google地图
    5. 单机地址文本字段
    6. 复制地址
    7. 按回车键

程序拓展：
    只要你有一个URL，webbrowser模块就可以让用户不必打开浏览器而直接加载一个网站。
    其他程序可以利用这项功能完成以下任务：
        - 在独立的浏览器窗口中，打开一个页面中的所有链接
        - 用浏览器打开本地天气的URL
        - 打开你经常查看的几个社交网站

测试：
    乐山三桥翡翠滨江(copy it!)
Usage:
    python webbrowser_maplt.py
"""

if len(sys.argv) > 1:
    # get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # get address from clipborad
    address = pyperclip.paste()

webbrowser.open(f'https://www.amap.com/search?query={address}&city=510000&geoobj=103.30622%7C30.28585%7C105.220348%7C31.133623&zoom=9.6')

