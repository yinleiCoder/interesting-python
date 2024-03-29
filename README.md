# 有趣的极客项目、实用的Python编程
`本仓库主要存放Python及实战Python的相关代码,适用于计算机系的本科生、研究生以及国内教师团体。`

## 开发环境
`注：Jetbrains PyCharm，推荐Eval Reset Plugin或者学生教育优惠.`
- Python(3.10.0)
- Anaconda3(Python 3.8.8)[可选]
- Pycharm
- Processing
- [Windows操作系统(Win11)](https://mp.weixin.qq.com/s?__biz=MzU2NzkxMzg2NQ==&mid=2247484028&idx=1&sn=0c80023581971ed1c9efdda438547025&chksm=fc94be9acbe3378cf2da2e4c6d5fd1c8c3a2459d745309ef9876292fae62a67b1761e30abfe5&token=1365422365&lang=zh_CN#rd)

## 仓库文件夹及文件说明
`算法看起来复杂，但只要方法得当，搞清原理，掌握起来还是很容易的。领悟算法思想、理解算法对内存空间和性能的影响，以及开动脑筋去寻求解决问题的最佳方案。`
- **advance_python: python高级编程**
    - all_is_object: 一切皆对象[python中一切都是对象、type object class之间的关系、内置类型]
    - magic_func: 魔法函数[什么是魔法函数、python的数据模型以及数据模型对python的影响、魔法函数一览、魔法函数的重要性]
    - class_and_obj: 深入类与对象[鸭子类型和多态、抽象基类abc模块、isinstance和type的区别、类变量和实例变量、类和实例属性的查找顺序(mro查找)、类方法 静态方法 实例方法、数据封装和私有属性、对象的自省机制、super真的调用父类吗、mixin继承、with语句、contextlib简化上下文管理器]
    - custom_sequence_cls: 自定义序列类[序列分类、序列类型的abc继承关系、list的extend方法与序列的+ +=区别、实现可切片的对象、bisect维护已排序序列、什么时候不该使用列表、列表推导式、生成器表达式、字典推导式]
    - deep_set_dict: 深入Set和Dict[dict的abc继承关系、dict的常用方法、dict的子类、set和frozenset、dict和set的实现原理]
    - recycle_garbage: 对象引用、可变性、垃圾回收[python中的变量、==和is的区别、del语句和垃圾回收、经典的参数错误]
    - meta_cls: 元类编程[property动态属性、__getattr__ __getattribute__、属性描述符和属性查找过程、__new__ __init__、自定义元类]
    - socket_server_http: Socket编程[Socket概念、Socket和server实现通信、socket实现聊天和多用户连接、socket模拟http请求]
    - iter_gen: 迭代器、生成器[python中的迭代协议、迭代器和可迭代对象、生成器函数、python怎么实现生成器的、生成器在UserList中的应用、生成器读取大文件]
    - thread_process_pool: 多线程、多进程、线程池[pyhton中的GIL、多线程编程、线程间通信共享变量和Queue、线程同步Lock RLock condition Semaphore、ThreadPoolExecutor线程池、multiprocessing多进程编程、进程间通信Queue Pipe Manager]
    - python_coroutine: 协程、异步io(并发、同步、异步、阻塞、非阻塞、C10K问题、io多路复用(select poll epoll)、epoll+回调+事件循环方式、回调之痛、C10M问题、协程、生成器的send和yield from、生成器如何变协程、async和await原生协程]
    - asyncio_coroutine: asyncio并发[事件循环、task取消和子协程调用原理、call_soon call_at call_later call_soon_threadsafe、ThreadPoolExecutor+asycio完成阻塞IO请求、asyncio模拟http请求、future和task、asyncio同步和通信]
- **algorithm_data_structure: 数据结构和算法**
    - algorithm_basic: 算法、数据结构、时间复杂度、空间复杂度
    - data_structure_basic: (最基本的数据结构)数组、链表、栈、队列、哈希表
    - tree_bstree: 树、二叉树
    - sort_basic: 排序算法：冒泡排序、快速排序、堆排序、计数排序、桶排序
    - algorithm_leetcode: 职场上的算法面试题及解题思路
    - algorithm_apply: 职场上的算法应用
- **math_python: 用Python学数学**[Processing]
    - : 用turtle模块绘制多边形
    - : 用代数学变换和存储数[解一次方程、解更高次的方程、作图法解方程]
    - :用几何学变换形状[变换函数、]
    - 用三角学制造振荡
    - 复数
    - 将矩阵用于计算机图形和方程组
    - 用类构建对象
    - recursive_division:用递归制作分形
    - 元胞自动机
    - 用遗传算法解决问题
- **python_reptile: 爬虫**
- **python_web_server: 后端django**
- **automate_the_boring_stuff: 让繁琐工作自动化**
    - pyperclip_reply_msg: 使用多剪贴板自动回复消息(pyperclip)
    - bullet_point_adder: 在Wiki标记中添加无序列表(pyperclip)
    - analzy_phone_email: 电话号码和E-mail地址提取(模式匹配与正则表达式)
    - input_valid: 输入验证(PyInputPlus)
    - read_write_file: 读写文件(pathlib与/)[生成随机的测试试卷、可更新的多重剪贴板(shelve)]
    - manage_file: 组织文件[将带有美国风格日期的文件重命名为欧洲风格日期、将一个文件夹备份到一个ZIP文件(zipfile、send2trash、shutil)]
    - logging_debug: 调试(logging)
    - web_browser: 从Web抓取信息(webbrowser、requests、bs4、selenium)[ webbrowser打开剪贴板中的内容对应的浏览器地图、浏览器分标签页打开所有搜索结果、下载所有XKCD漫画、selenium控制浏览器自动化]
    - handle_microsoft_excel: 处理Microsoft Excel电子表格(openpyxl)[更新电子表格][关于办公office自动化可以参考我的博文](https://blog.csdn.net/qq_39969226/article/details/106376115?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164856626016782184629518%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=164856626016782184629518&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-106376115.nonecase&utm_term=%E8%87%AA%E5%8A%A8%E5%8C%96&spm=1018.2226.3001.4450)
    - handle_microsoft_pdf_word: 处理PDF、Word(PyPDF2、python-docx)[从多个pdf中合并选择、从Word中创建PDF]
    - handle_csv_json: 处理CSV、JSON(csv、json)
    - handle_plan_time: 保持时间、计划任务和启动程序(time、datetime、subprocess)[超级秒表、刷题倒计时、并发下载所有XKCD漫画、python启动其他程序、python中的调度程序（windows的Task Scheduler、macOS的launched、Linux的cron调度程序允许安排应用程序在特定的时间启动）]
    - send_email_message: 发送电子邮件和短信(smtp、imapclient、ezgmail控制Gmail)[Twilio发送短信]
    - handle_img: 操作图像(pillow)
    - auto_gui_keyboard_mouse: 用GUI自动化控制键盘和鼠标(pyautogui)
- **geek_funny: 极客项目[热身运动、模拟生命、图像之乐、走进三维、玩转硬件]**
    - itunes_playlist_parse: 解析iTunes播放列表
    - 万花尺
    - Conway生命游戏
    - 用Karplus-Strong算法产生音乐泛音
    - 类鸟群：仿真鸟群
    - ascii_text_img: ASCII文本图形
    - photo_mosaic: 照片马赛克
    - 三维立体图
    - 理解OpenGL
    - 粒子系统
    - 体渲染
    - Arduino
    - 激光音乐秀
    - 基于树莓派的天气监控器
- **opencv_py: 计算机视觉与OpenCV**
    - opencv_what: OpenCV介绍
    - img_video_load_show: 图像与视频的加载和展示
    - opencv_basic: OpenCV基础[色彩空间变换、像素访问、矩阵的操作、Mat数据结构]
    - paint_shape: 基本图形的绘制[线、矩形、圆、椭圆、多边形、字体]
    - image_operation: 图像运算[图像的加法、减法、乘法、除法、溶合、位操作]
    - image_transform: 图像基本变换[图像的放大、缩小、翻转、旋转、仿射变换、透视变换]
    - opencv_filter: 滤波器[图像滤波、卷积、低通滤波{方盒滤波、均值滤波、高斯滤波、中值滤波、双边滤波}、高通滤波{高通滤波(索贝尔算子、沙尔算子、拉普拉斯算子)、边缘检测Canny}]
    - opencv_morphology: 形态学图像处理[二值化、腐蚀与膨胀、开运算、闭运算、顶帽、黑帽]
    - opencv_contours: 目标识别/轮廓[查找轮廓、绘制轮廓、轮廓的面积与周长、多边形逼近与凸包、外接矩形]
    - vehicle_count: 车辆统计[结合以上opencv知识实战]
    - feature_detection: 特征点检测与匹配[Harris角点检测、Shi-Tomasi角点检测、SIFT关键点检测、SURF特征检测、ORB特征检测、暴力特征匹配、FLANN特征匹配、图像查找单应性矩阵]
    - image_connect: 图像拼接[结合以上特征点检测与匹配知识实战]
    - image_segmentation_restoration: 图像分割与修复[分水岭法、GrabCut法、MeanShift法、背景扣除(MOG去背景、MOG2去背景、GMG去背景)、图像修复]
    - opencv_machine_learning_face: OpenCV机器学习[Haar(哈尔)级联方法人脸识别、深度学习DNN人脸识别方法、Haar+Tesseract识别车牌]
- **china_unicom_ocr_text_bill：中国联通增值税发票OCR**
- **game_development: 游戏编程**
    - alien_invasion: 外星人入侵(PyGame 2D)
- **data_analysis_visualize: 数据分析与可视化[用数据解析世界]**
    - data_visualize: python编程数据可视化[Matplotlib、Plotly]
    - [data_pandas_numpy](https://wesmckinney.com/book/): python数据分析基础[pandas、numpy]
      - 数据清洗与准备
      - 数据规整：连接、联合、重塑
      - 绘图与可视化
      - 数据聚合与分组操作
      - 时间序列
- **quantitative_trading: 量化交易[量化过去，预测未来(经济领域)]**
    - trading_what: 量化简介[量化交易策略、常用的股票量化指标]
    - get_stock_data: 获取股票数据[股票是什么、使用JQData获取行情数据、Resample函数转化时间序列、使用JQData查询财务指标、]
    - 计算交易指标
    - 设计交易策略：择时策略
    - 设计交易策略：选股策略
    - 数据回测与优化
    - 实现股票实盘交易
    - 进阶计划(结合机器学习)
- **pytorch_ml: Pytorch计算机视觉与自然语言处理(学术界)**
- **tensorflow_ml: Tensorflow2.x深度学习(工业界)**
- **hacker_py_vmware_kali: python黑帽子黑客与渗透测试编程**  
`需要准备的环境包括VMWare+Kali VM+Python3+Windows10or11.这里展示的是python的“黑暗面”:1.基于Github的C&C木马服务；2.探测自己是否处于沙箱环境中，并执行各种恶意软件创建操作；
3.扩展web黑客工具Burp Suite的功能；4.通过原创的进程控制框架进行windows提权；5.使用攻击性的取证技巧，从虚拟机中提取密码哈希值及发掘漏洞；6.利用windows COM自动化接口；7.从网络中隐蔽的渗漏数据`
    - : 基础的网络编程工具[取代netcat、TCP代理、基于Paramiko的SSH通信、SSH隧道]
    - 流量嗅探器[基于UDP的主机发现工具、Windows和Linux上的包嗅探、解析IP层及IP解码器、解码ICMP]
    - Scapy网络的掌控者[窃取邮箱身份凭证、ARP投毒、pcap文件处理]
    - Web攻击[拓印WordPress系统结构、扫描在线目标、暴力破解目录和文件位置、暴力破解HTML登录表单]
    - Burp插件[配置BurpSuite、Burp模糊测试插件、Burp中调用Bing搜索、利用网页内容生成爆破字典]
    - 基于Github服务的C&C通信[木马模块、木马配置文件、构建基于Github通信的木马]
    - Windows下的木马常用功能[键盘记录、截取屏幕、执行shellcode、沙箱检测]
    - 数据渗漏[文件的加密与解密、电子邮件的数据渗漏、文件传输的渗漏、web服务器的数据渗漏]
    - Windows系统提权[模拟受害服务、进程监视器WMI监视进程、Windows系统的令牌权限、条件竞争、代码注入]
    - 攻击取证[Volatility、探查基本情况、探查用户信息、探查潜在漏洞、volshell控制界面、Volatility插件]

## 后续学习方向建议
`研究生及以后职业规划的学习方向，仅供参考`
- [人工智能](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NzkxMzg2NQ==&action=getalbum&album_id=1733540329405923330#wechat_redirect)
- ESP8266+STM32+51单片机+树莓派
- 金融

## 推荐相关书籍
`以下图书均可在“京东图书”购买电子版阅读。`
- [Python编程：从入门到实践(第二版)]()
- [Python编程快速上手——让繁琐工作自动化(第二版)]()
- [Python极客项目编程]()
- [利用Python进行数据分析(第3版)](https://wesmckinney.com/book/)
- [用Python学数学]()
- [小灰漫画算法(Python版) ]()
- [ Python3网络爬虫开发实战 第二版 (崔庆才) ]()
- [ 西瓜书 ]()
- [ 动手学习深度学习 ]()

### Python黑客涉及的资料链接(补)
- [微软开发者官网windows虚拟机](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)  
- [kali虚拟机镜像](https://www.kali.org/downloads/)  
- [kali官方文档](https://www.kali.org/docs/installation/)  
- [pycharm](https://www.jetbrains.com/pycharm/download/)  
- [WinIDE](https://wingware.com/downloads/)  
- [VSCode](https://code.visualstudio.com/download/)  
- [Python PEP8规范](https://www.python.org/dev/peps/pep-0008/)  
- [Python Socket](http://docs.python.org/3/library/socket.html)  
链接 10：http://www.paramiko.org/  
链接 11：https://github.com/paramiko/paramiko/  
第 3 章  
链接 12：https://Wireshark.org/  
链接 13：https://en.wikipedia.org/wiki/Ioctl  
链接 14：https://docs.python.org/3/library/struct.html  
第 4 章  
链接 15：https://scapy.net/  
链接 16：http://www.opencv.org/  
链接 17：http://www.fideloper.com/facial-detection/  
第 5 章  
链接 18：https://wordpress.org/download/  
链接 19：boodelyboo.com/  
链接 20：https://github.com/OJ/gobuster/  
链接 21：https://www.netsparker.com/blog/web-security/svn-digger-better-lists-for-forcedbrowsing/  
链接 22：https://owasp.org/www-project-vulnerable-web-applications-directory/  
链接 23：
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Software/
cain-and-abel.txt  
链接 24：boodelyboo.com/  
第 6 章  
链接 25：http://www.porstswigger.net/  
链接 26：https://www.jython.org/download.html  
链接 27：http://testphp.vulnweb.com/  
链接 28：https://www.microsoft.com/en-us/bing/apis/bing-web-search-api/  
链接 29：http://testphp.vulnweb.com/  
链接 30：http://testphp.vulnweb.com/  
第 7 章  
链接 31：https://pypi.org/project/github3.py/  
链接 32：https://docs.github.com/en/github/authenticating-to-github/  
链接 33：https://www.pyinstaller.org/downloads.html  
第 8 章  
链接 34：https://pypi.org/project/pyWinhook/  
链接 35：http://www.offensive-security.com/metasploit-unleashed/Generating_Payloads/  
第 9 章  
链接 36：http://pastebin.com/  
第 10 章  
链接 37：https://nostarch.com/black-hat-python2E/  
链接 38：http://timgolden.me.uk/python/wmi/tutorial.html  
链接 39：http://msdn.microsoft.com/  
第 11 章  
链接 40：https://git-scm.com/downloads/  
链接 41：https://github.com/volatilityfoundation/volumetric/  
链接 42：https://www.osforensics.com/tools/volatility-workbench.html/  
链接 43：https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples/  