# 开发有趣的极客项目、掌握实用的Python:snake编程
`本仓库主要存放Python及实战Python的相关代码,适用于计算机系的本科生、研究生。`
## 开发环境
`注：Jetbrains PyCharm，推荐Eval Reset Plugin.`
- Python(3.10.0)
- Anaconda3(Python 3.8.8)[中国联通发票识别项目需要python 3.8]
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
    - iter_gen: 迭代器、生成器：[python中的迭代协议、迭代器和可迭代对象、生成器函数、python怎么实现生成器的、生成器在UserList中的应用、生成器读取大文件]
    - thread_process_pool: 多线程、多进程、线程池[pyhton中的GIL、多线程编程、线程间通信共享变量和Queue、线程同步Lock RLock condition Semaphore、ThreadPoolExecutor线程池、multiprocessing多进程编程、进程间通信Queue Pipe Manager]
    - python_coroutine: 协程、异步io(并发、同步、异步、阻塞、非阻塞、C10K问题、io多路复用(select poll epoll)、epoll+回调+事件循环方式、回调之痛、C10M问题、协程、生成器的send和yield from、生成器如何变协程、async和await原生协程]
    - asyncio_coroutine: asyncio并发[事件循环、task取消和子协程调用原理、call_soon call_at call_later call_soon_threadsafe、ThreadPoolExecutor+asycio完成阻塞IO请求、asyncio模拟http请求、future和task、asyncio同步和通信]
- **algorithm_data_structure: 数据结构和算法**
    - 算法、数据结构、时间复杂度、空间复杂度
    - 最基本的数据结构：数组、链表、栈、队列、哈希表
    - 树、二叉树
    - 排序算法：冒泡排序、快速排序、堆排序、计数排序、桶排序
    - 职场上的算法面试题及解题思路
    - 职场上的算法应用
- **math_python: 用Python学数学**[Processing]
    - turtle_demo: 用turtle模块绘制多边形
    - mathematics_transformation_storage: 用代数学变换和存储数[解一次方程、解更高次的方程、作图法解方程]
    - change_shape_geometry:用几何学变换形状[变换函数、]
    - 用三角学制造振荡
    - 复数
    - 将矩阵用于计算机图形和方程组
    - 用类构建对象
    - recursive_division:用递归制作分形
    - 元胞自动机
    - 用遗传算法解决问题
- **linear_algebra_learning_basic: 线性代数**
  - linear_algebra_what: 线性代数的定义
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
    - opencv_filter: 滤波器[图像滤波、卷积、低通滤波、高通滤波、方盒滤波、均值滤波、高斯滤波、中值滤波、双边滤波、高通滤波(索贝尔算子、沙尔算子、拉普拉斯算子)、边缘检测Canny]
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
    - data_analysis_tools: 走进数据分析[Excel表格分析、SQL、数据可视化利器Tableau]
    - data_visualize: python编程数据可视化[Matplotlib、Plotly]
    - 建立互联网数据分析框架[初识互联网商业模式、解析数据指标体系、构建用户画像]
    - 销售、市场与运营数据分析[用户引流与转化、分析消费行为、预售额与调整运营策略]
    - 基于数据驱动迭代产品设计[促进用户活跃度、提升用户留存、使用AB实验迭代功能、撰写数据报告]
- **quantitative_trading: 量化交易[量化过去，预测未来(经济领域)]**
    - trading_what: 量化简介[量化交易策略、常用的股票量化指标]
    - get_stock_data: 获取股票数据[股票是什么、使用JQData获取行情数据、Resample函数转化时间序列、使用JQData查询财务指标、]
    - 计算交易指标
    - 设计交易策略：择时策略
    - 设计交易策略：选股策略
    - 数据回测与优化
    - 实现股票实盘交易
    - 进阶计划(结合机器学习)
- **cnn_rnn_gan: 深度学习之神经网络CNN RNN GAN算法原理**
    - 神经网络简介
    - 卷积神经网络
    - 卷积神经网络进阶
    - 卷积神经网络调参
    - 图像风格转换
    - 循环神经网络
    - 图像生成文本
    - 对抗神经网络
    - 自动机器学习网络AutoML
- **深度学习之目标检测常用算法原理+实践**
    - 目标检测算法基础
    - SSD系列算法原理
    - 基于SSD的人脸检测
    - Faster RCNN系列算法原理
    - 基于Faster RCNN的ADAS场景目标检测
    - YOLO系列算法原理
    - 基于YOLOV3的通用物体检测
    - 文本检测系列算法原理
    - 基于EAST的自然场景文本检测
    - 多任务网络原理
    - 基于人脸检测+关键点定位的多任务网络
- **pytorch_ml: Pytorch计算机视觉与自然语言处理(学术界)**
    - pytorch_what_install: Pytorch简介与环境搭建
    - pytorch_basic: Pytorch基础
    - Pytorch搭建简单神经网络
    - 计算机视觉与卷积神经网络CNN基础
    - Pytorch计算机视觉任务1Cifar10图像分类
    - Pytorch计算机视觉任务2Pascal VOC目标检测问题
    - Pytorch计算机视觉任务3COCO目标分割问题
    - Pytorch搭建GAN网络图像风格迁移
    - 循环神经网络RNN与NLP基础
    - Pytorch中文文本情感分类
    - Pytorch机器翻译
    - Pytorch工程应用
- **tensorflow_ml: Tensorflow2.x深度学习(工业界)**
    - tensorflow_what_install: Tensorflow简介与环境搭建[Tensorflow是什么、Tensorflow历史、Tensorflow VS Pytorch、多平台环境配置]
    - tensorflow_keras_basic: Tensorflow keras[tf框架：keras、回调函数；分类问题、回归问题、损失函数、神经网络、激活函数、批归一化、Dropout、Wide & deep模型、超参数搜索。(图像分类、房价预测)]
    - tensorflow_basic_api: Tensorflow基础API[tf框架：基础数据类型、自定义模型与损失函数、自定义求导、tf.function、图结构(图像分类、房价预测)]
    - tensorflow_data_api: Tensorflow dataset使用[tf框架：csv文件读取、tfrecord文件生成与读取、tf.data使用(房价预测)]
    - Tensorflow Estimator使用与tf1.0[tf框架：estimator使用、特征列使用、tf1.0基本使用(泰坦尼克生存预测)]
    - 卷积神经网络[tf框架：卷积实现；卷积、数据增强、迁移学习(图像分类、Kaggle 10monkeys、kaggle cifar10)]
    - 循环神经网络[tf框架：LSTM实现；序列式问题、循环网络、LSTM、双向LSTM(文本分类、文本生成、Kaggle文本分类)]
    - Tensorflow分布式[tf框架：分布式实现；分布式原理与策略(图像分类)]
    - Tensorflow模型保存与部署[tf框架：模型保存、导出tflite、部署;(图像分类)]
    - 机器翻译与tensor2tensor[tf框架：transformer实现、tensor2tensor使用;序列到序列模型、注意力机制、可缩放点积注意力、多头注意力(机器翻译)]
- **hacker_py_vmware_kali: python黑帽子黑客与渗透测试编程**  
`需要准备的环境包括VMWare+Kali VM+Python3+Windows10or11.这里展示的是python的“黑暗面”:1.基于Github的C&C木马服务；2.探测自己是否处于沙箱环境中，并执行各种恶意软件创建操作；
3.扩展web黑客工具Burp Suite的功能；4.通过原创的进程控制框架进行windows提权；5.使用攻击性的取证技巧，从虚拟机中提取密码哈希值及发掘漏洞；6.利用windows COM自动化接口；7.从网络中隐蔽的渗漏数据`
    - basic_network_programming_tools: 基础的网络编程工具[取代netcat、TCP代理、基于Paramiko的SSH通信、SSH隧道]
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
- [利用Python进行数据分析(第二版)]()
- [用Python学数学]()
- [小灰漫画算法(Python版) ]()
- [ Python3网络爬虫开发实战 第二版 (崔庆才) ]()
- [ 西瓜书 ]()

## FFmpeg常用命令(avfilter)
- **视频加水印**：
  - 文字水印：编译时需要支持FreeType、FontConfig、iconv，增加纯字母水印可以使用drawtext滤镜`ffmpeg -re -i 8.mp4 -vf "drawtext=fontsize=60:fontfile=FreeSerif.ttf:fontcolor=white:text='%{localtime\:%Y\-%m\-%d \%H-%M-%S}':box=1:boxcolor=gray:x=20:y=20" output.mp4`
  - 图片水印1：filter滤镜`ffmpeg -i 8.mp4 -i logo.JPG -filter_complex "[1:v]scale=176:144[logo];[0:v][logo]overlay=x=0:y=0" output.mp4`
  - 图片水印2：movie滤镜与colorkey滤镜半透明效果`ffmpeg -i 4.mp4 -vf "movie=logo.JPG,colorkey=black:1.0:1.0[wm];[in][wm]overlay=10:10[out]" output.mp4`
- **画中画**: overlay滤镜 
  - 静态指定位置：`ffmpeg -re -i 6.mp4 -vf "movie=7.mp4,scale=320x480[test];[in][test]overlay=x=main_w-320:y=main_h-480[out]" -vcodec libx264 output.flv`
  - 跑马灯画中画：`ffmpeg -re -i 6.mp4 -vf "movie=7.mp4,scale=320x480[test];[in][test]overlay=x='if(gte(t,2), -w+(t-2)*20, NAN)':y=0 [out]" -vcodec libx264 output.flv`
- **视频多宫格**: `ffmpeg -re -i 7.mp4 -re -i 6.mp4 -re -i 4.mp4 -re -i 8.mp4 -filter_complex "nullsrc=size=360x720[base];[0:v]setpts=PTS-STARTPTS,scale=180x360[upperleft];[1:v]setpts=PTS-STARTPTS,scale=180x360[upperright];[2:v]setpts=PTS-STARTPTS,scale=180x360[lowerleft];[3:v]setpts=PTS-STARTPTS,scale=180x360[lowerright];[base][upperleft] overlay=shortest=1[temp1];[temp1][upperright]overlay=shortest=1:x=180[temp2];[temp2][lowerleft]overlay=shortest=1:y=360[temp3];[temp3][lowerright]overlay=shortest=1:x=180:y=360" -c:v libx264 output.flv`
- **音频流滤镜**: amix、amerge、pan、channelsplit、volume、volumedetect滤镜
  - 双声道合并单声道：stereo变为mono布局`ffmpeg -i input.aac -ac 1 output.aac`
  - 双声道提取：`ffmpeg -i input.aac -map_channel 0.0.0 left.aac -map_channel 0.0.1 right.aac`
  - 双声道提取pan滤镜：`ffmpeg -i input.aac -filter_complex "[0:0]pan=1c|c0=c0[left];[0:0]pan=1c|c0=c1[right]" -map "[left]" left.aac -map "[right]" right.aac`
  - 双声道转双声道频流：大多数情况下默认播放第一个音频stream`ffmpeg -i input.aac -filter_complex channelsplit=channel_layout=stereo output.mka`
  - 单声道转双声道(伪双声)：mono变为stereo布局`ffmpeg -i left.aac -ac 2 output.m4a`
  - 单声道转双声道amerge滤镜(伪双声): `ffmpeg -i left.aac -filter_complex "[0:a][0:a]amerge=inputs=2[aout]" -map "[aout]" output.m4a`
  - 2个音频源合并双声道：`ffmpeg -i left.aac -i right.aac -filter_complex "[0:a][1:a]amerge=inputs=2[aout]" -map "[aout]" output.mka`
  - 多个音频合并多声道：`ffmpeg -i front-left.wav -i front_right.wav -i front_center.wav -i lfe.wav -i back_left.wav -i back_right.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a]amerge=inputs=6=[aout]" -map "[aout]" output.wav`
- **音频音量探测**: 
  - 音频音量获得：volumedetect滤镜`ffmpeg -i power.mp3 -filter_complex volumedetect -c:v copy -f null /dev/null`
  - 绘制音频波形: showwavespic滤镜`ffmpeg -i power.mp3 -filter_complex "showwavespic=s=640x120" -frames:v 1 output.png`
  - 绘制多声道音频波形: showwavespic+split_channel滤镜`ffmpeg -i power.mp3 -filter_complex "showwavespic=s=640x120:split_channels=1" -frames:v 1 output.png`
- **视频加字幕**: 
  - ASS字幕流写入视频流：`ffmpeg -i input.mp4 -vf ass=t1.ass -f mp4 output.mp4`
  - ASS字幕流写入封装容器：`ffmpeg -i input.mp4 -i t1.ass -map 0:0 -map:0:1 -map 1:0 -acodec copy -vcodec copy -scodec copy output.mkv`
- **视频抠图合并**:chromakey滤镜绿幕抠图 `ffmpeg -i input.mp4 -i input_green.mp4 -filter_complex "[1:v]chromakey=Green:0.1:0.2[ckout];[0:v][ckout]overlay[out]" -map "[out]" output.mp4`
- **3D视频处理**: stereo3d滤镜`ffplay -vf "stereo3d=sbsl:aybd(黄蓝眼镜)arbg(红蓝眼镜)" input.mp4`
- **定时视频截图**: 
  - vframe参数指定时间位置截取一张图片：`ffmpeg -i input.flv -ss 00:00:8 -vframes 1 out.png`
  - fps滤镜定时获得图片：`ffmpeg -i input.flv -vf fps=1 out%d.png` fps=1/60就是1秒钟，1/600就是1分钟
  - select通过关键帧I帧截取图片：`ffmpeg -i input.flv -vf "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr thumb%04d.png`
- **生成测试元数据**: 
  - lavfi设备虚拟音频源生成音频测试流(abuffer aevalsrc anullsrc flite anoisesrc sine滤镜)：`ffmpeg -re -f lavfi -i abuffer=sample_rate=44100:sample_fmt=s16p:channel_layout=stereo -acodec aac -y output.aac ffmpeg -re -f lavfi "aevalsrc=sin(420*2*PI*t)|cos(430*2*PI*t):c=FC|BC" -acodec aac output.aac`
  - 生成视频测试流(allrgb allyuv color haldclutsrc nullsrc rgbtestsrc smptebars smptehdbars testsrc testsrc2 yuvtestsrc)：`ffmpeg -re -f lavfi -i testsrc=duration=5.3:size=qcif:rate=25 -vcodec libx264 -r:v 25 output.mp4`
  - 生成视频测试流：纯色`ffmpeg -re -f lavfi -i color=c=red@0.2:s=qcif:r=25 -vcodec libx264 -r:v 25 output.mp4`
  - 生成视频测试流：随机雪花`ffmpeg -re -f lavfi -i "nullsrc=s=256x256,geq=random(1)*25:128:128" -vcodec libx264 -r:v 25 output.mp4`
- **音视频倍速**: 
  - 音频倍速处理(跳帧播放、不跳帧播放)atempo滤镜tempo参数0.5-2：`ffmpeg -i input.wav -filter_complex "atempo=tempo=0.5" -acodec aac output.aac`
  - 视频倍速处理setpts滤镜expr参数描述每一帧的时间戳：`ffmpeg -re -i input.mp4 -filter_complex "setpts=PTS*2(或/2)" output.mp4`
- **采集设备**:
  - Linux平台：fbdev v4l2 x11grab设备类型
    - 查看设备列表：`ffmpeg -hide_banner -devices`
    - fdev录制linux终端中的操作：`ffmpeg -framerate 30 -f fbdev -i /dev/fb0 output.mp4`
    - v412采集摄像头：`ffmpeg -hide_banner -f v4l2 -list_formats all -i /dev/video0`  `ffmpeg -hide_banner -s 1920x1080 -i /dev/video0 output.avi`
    - x11grab采集部分桌面图像：
      - 完整桌面录制：`ffmpeg -f x11grab -framerate 25 -video_size 1366x768 -i :0.0 out.mp4`
      - 桌面录制指定起始位置：`ffmpeg -f x11grab -framerate 25 -video_size 352x288 -i :0.0+300,200 out.mp4`
      - 桌面录制带鼠标记录：`ffmpeg -f x11grab -video_size 1366x768 -follow_mouse 1 -i :0.0 out.mp4`
  - OS X平台: avfoundation -i可以使用设备号或设备索引号
    - 查看设备列表：`ffmpeg -devices` `ffmpeg -f avfoundation -list_devices true -i ""`查看支持的设备号
    - 采集内置摄像头：`ffmpeg -f avfoundation -i "FaceTime HD Camera(Built-in)" out.mp4`
    - 采集OS X桌面：`ffmpeg -f avfoundation -i "Capture screen 0" -r:v 30 out.mp4`
    - 采集OS X桌面带鼠标：`ffmpeg -f avfoundation -capture_cursor 1 -i "Capture screen 0" -r:v 30 out.mp4`
    - 采集麦克风: `ffmpeg -f avfoundation -i "0:0" out.aac` `ffmpeg -f avfoundation -video_device_index 0 -i ":0" out.aac` `ffmpeg -f avfoundation -video_device_index 0 -audio_device_index 0 out.aac`
  - Windows平台:dshow vfwcap gdigrab
    - dshow抓取摄像头、采集卡、麦克风
      - 使用dshow枚举设备：`ffmpeg -f dshow -list_devices true -i dummy`
      - 展示摄像头：`ffplay -f dshow -video_size 1280x720 -i video="Integrated Camera"` video参数看枚举设备名
      - 将摄像头保存为mp4: 摄像头和电脑播放的声音`ffmpeg -rtbufsize 1024M -f dshow -i video="XiaoMi USB 2.0 Webcam" -f dshow -i audio="麦克风 (Realtek(R) Audio)" out.mp4`
    - gdigrab采集桌面或窗口
      - 采集整个桌面(desktop输入方式)：`ffmpeg -f gdigrab -framerate 30 -i desktop -vcodec libx264 -pix_fmt yuv420p -acodec aac out.mp4`
      - 采集某个窗口(window_title输入方式): `ffmpeg -f gdigrab -framerate 30 -i title=窗口名 -vcodec libx264 -pix_fmt yuv420p -acodec aac out.mp4`
      - 采集带偏移量的视频：`ffmpeg -f gdigrab -framerate 6 -offset_x 50 -offset_y 50 -video_size 400x400 -i title=窗口名 out.mp4`
    - vfwcap采集摄像头类设备(过时了)
      - vfwcap枚举设备：`ffmpeg -f vfwcap -i list`
      - 录制摄像头：`ffmpeg -f vfwcap -i 0 -r 25 -vcodec libx264 out.mp4`
  - **Ffmpeg转封装**
    - 音视频文件转MP4格式
      - faststart参数将moov容器移动到mdat的前面：`ffmpeg -i input.flv -c copy -f mp4 -movflags faststart output.mp4`
      - dash参数：Dash格式的MP4存储的容器信息与常规的MP4格式有差别，主要以sidx moof mdat容器为主`ffmpeg -i input.flv -c copy -f mp4 -movflags dash output.mp4`
      - isml参数：ISMV为微软发布的一个流媒体格式，可以发布ISML直播流，将ISMV推流到IIS服务器，可以通过参数isml进行发布：`ffmpeg -re -i input.mp4 -c copy -movflags isml+frag_keyframe -f ismv Stream`
    - 视频文件转FLV（直播、点播场景中常见）
      - flv容器不支持AC3音频，可以将AC3转为flv支持的aac/mp3等格式：`ffmpeg -i input_ac3.mp4 -vcodec copy -acodec aac -f flv output.flv`
      - 生成带关键索引的FLV：`ffmpeg -i input.mp4 -c copy -f flv -flvflags add_keyframe_index out.flv`
      - ffprobe解析flv：`ffprobe -v trace -i output.flv`
    - 视频文件转M3U8（以文件列表的形式存在，支持直播、点播、android ios）
      - 从文件转换HLS直播：将MP4中的H.264数据转换为H.264AnnexB标准的编码，AnnexB标准的编码常见于实时传输流中。如果源文件为FLV、TS等可作为直播传输流的视频，则不需要这个参数`ffmpeg -re -i input.mp4 -c copy -f hls -bsf:v h264_mp4toannexb output.m3u8`
      - start_number参数：设置M3U8列表中的第一片的序列数`ffmpeg -re -i input.mp4 -c copy -f hls -bsf:v h264_mp4toannexb -start_number 300 out.m3u8`
      - hls_time参数：设置M3U8列表中切片的duration，从切片规则采用的方式是从关键帧处开始切片,所以时间并不是均匀的，如果先转码再切片会比较规律`ffmpeg -re -i input.mp4 -c copy -f hls -bsf:v h264_mp4toannexb -hls_time 10 output.m3u8`
      - hls_list_size参数：设置M3u8列表中TS切片的个数`ffmpeg -re -i input.mp4 -c copy -f hls -bsf:v h264_mp4toannexb -hls_list_size 3 output.m3u8
      - hls_wrap参数：为M3U8列表中TS设置刷新回滚参数，当TS分片序号等于hls_wrap参数设置的数值时回滚,但对CDN缓存节点的支持并不友好`ffmpeg -re -i input.mp4 -c copy -f hls -bsf:v h264_mp4toannexb -hls_wrap 3 output.m3u8`
      - hls_base_url参数：为M3U8列表中的文件路径设置前置基本路径参数，ffmpeg生成m3u8时写入的ts切片路径默认为与m3u8生成的路径相同，但TS所存储的路径可以是其他路径`ffmpeg -re -i input.mp4 -c copy -f hls -hls_base_url http://192.168.0.1/live/ -bsf:v h264_mp4toannexb output.m3u8`
      - hls_segment_filename参数：为M3U8列表设置切片文件名的规则模板参数，如果不设置那么生成的TS切片文件名模板与M3U8文件名模板相同`ffmpeg -re -i input.mp4 -c copy -f hls -hls_segment_filename test_output-%d.ts -bsf:v h264_mp4toannexb output.m3u8`
      - hls_flags参数：
        - delete_segments子参数：删除已经不在m3u8列表中的旧文件，ffmpeg删除切片会将hls_list_size的2倍大小作为删除的依据`ffmpeg -re -i input.mp4 -c copy -f hls -hls_flags delete_segments -hls_list_size 4 -bsf:v h264_mp4toannexb output.m3u8`
        - round_durations子参数：切片信息的duration为整数`ffmpeg -re -i input.mp4 -c copy -f hls -hls_flags round_durations -bsf:v h264_mp4toannexb output.m3u8`
        - discont_start子参数：在生成m3u8的时候在切片信息的前边插入discontinuity标签,常用于在切片不连续时做特别声明用`ffmpeg -re -i input.mp4 -c copy -f hls -hls_flags discont_start -bsf:v h264_mp4toannexb output.m3u8`
        - omit_endlist子参数：在生成m3u8结束的时候若不在文件的末尾则不追加endlist标签`ffmpeg -re -i input.mp4 -c copy -f hls -hls_flags omit_endlist -bsf:v h264_mp4toannexb output.m3u8`
        - split_by_time子参数：在生成M3U8时是根据hls_time参数设定的值为秒数参考对TS进行切片的，并不一定要遇到关键帧。hls_time参数设定了值后，切片生成的TS的duration有时候远大于设定的值，使用split_by_time可解决, 必须搭配hls_time参数，且有时候可能会影响首画面体验，如花屏或者首画面显示曼，因为视频的第一帧不一定是关键帧`ffmpeg -re -i input.ts -c copy -f hls -hls_time 2 -hls_flags split_by_time output.m3u8`
      - use_localtime参数：以本地系统时间为切片文件名`ffmpeg -re -i input.mp4 -c copy -f hls -use_localtime 1 -bsf:v h264_mp4toannexb output.m3u8`
      - method参数：设置HLS将M3U8及TS文件上传至HTTP服务器，method方法的put方法可用于实现通过http推流HLS的功能，首先需要配置一个支持上传文件的HTTP服务器，如nginx作为HLS直播的推流服务器，并需要支持WebDAV功能`ffmpeg -i input.mp4 -c copy -f hls -hls_time 3 -hls_list_size 0 -method PUT -t 30 http://127.0.0.1/test/output_test.m3u8`
    - 视频文件切片(与HLS基本类似，但HLS切片在标准中只支持TS格式的切片，并且是直播与点播切片，可以使用segment方式切片，或使用ss加上t参数进行切片)
      - ffmpeg切片segment参数：
        - segment_format指定切片文件的格式：HLS切片的格式主要为MPEGTS文件格式，在segment中，可以根据segment_format指定切片文件的格式`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 test_output-%d.mp4`
        - segment_list与segment_list_type指定切片索引列表：
          - 生成ffconcat格式索引文件: 常用于虚拟轮播场景`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -segment_list_type ffconcat -segment_list output.lst test_output_%d.mp4`
          - 生成FLAT格式索引文件：`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -segment_list_type flat -segment_list filelist.txt test_output_%d.mp4`
          - 生成csv格式索引文件：`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -segment_list_type csv -segment_list filelist.csv test_output_%d.mp4`
          - 生成m3u8格式索引文件：`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -segment_list_type m3u8 -segment_list output.m3u8 test_output_%d.mp4`
        - rest_timestamps使切片时间戳归0：使每一片切片的时间戳都归0`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -rest_timestamps 1 test_output_%d.mp4`
        - segment_times按照时间点剪切：`ffmpeg -re -i input.mp4 -c copy -f segment -segment_format mp4 -segment_times 3,9,12 test_output_%d.mp4`
      - ffmpeg使用ss与t参数进行切片：
        - 使用ss指定剪切开头部分：ss参数可以用作切片定位起始时间点`ffmpeg -ss 10 -i input.mp4 -c copy output.ts`
        - 使用t指定视频总长度：`ffmpeg -i input.mp4 -c copy -t 10 -copyts output.mp4`
        - 使用output_ts_offset指定输出start_time: 指定输出文件的start_time，不将时间戳归0`ffmpeg -i input.mp4 -c copy -t 10 -output_ts_offset 120 output.mp4`
    - 音视频文件音视频流抽取
      - ffmpeg抽取音视频文件中的AAC音频流：`ffmpeg -i input.mp4 -vn -acodec copy output.aac`
      - ffmpeg抽取音视频文件中的H.264视频流：`ffmpeg -i input.mp4 -vcodec copy -an output.h264`
      - ffmpeg抽取音视频文件中的H.265数据：`ffmpeg -i input.mp4 -vcodec copy -an -bsf hevc_mp4toannexb -f hevc output.hevc`
    - 系统资源使用情况: cpu使用率`ffmpeg -re -i input.mp4 -c copy -f mpegts output.ts`转换封装，然后top命令查看cpu使用率，`ffmpeg -re -i input.mp4 -vcodec libx264 -acodec copy -f mpegts output.ts`然后top查看cpu使用率
  - **Ffmpeg转码**
    - 软编码H.264与H.265
      - 编码器预设参数设置preset：x264--full help，设置的预设参数不同，所编码出来的清晰度也会不同
        - ultrafast：最快的编码方式`ffmpeg -i input.mp4 -vcodec libx264 -preset ultrafast -b:v 2000k output.mp4`
        - superfast：超快的编码方式
        - veryfast：非常快速的编码方式
        - faster: 稍微快速的编码方式
        - fast: 快速的编码方式
        - medium: 折中的编码方式`ffmpeg -i input.mp4 -vcodec libx264 -preset medium -b:v 2000k output.mp4`
        - slow: 慢的编码方式
        - slower：更慢的编码方式
        - veryslow: 非常慢的编码方式
        - placebo: 最慢的编码方式
      - H.264编码优化参数tune
        - film、animation、grain、stillimage、psnr、ssim、fastdecode、zerolatency场景。用ffmpeg与x264进行H.264编码并进行推流时，只用tune参数的zerolatency将提升效率，因为降低了因编码导致的延迟
      - H.264的profile与level设置
        - profile档次: Baseline、Extented、Main、High、High10、High422、High444参数。`ffmpeg -i input.mp4 -vcodec libx264 -profile:v baseline -level 3.1 -s 352x288 -an -y -y 10 output_baseline.ts` `ffmpeg -i input.mp4 -vcodec libx264 -profile:v high -level 3.1 -s 352x288 -an -y -y 10 output_high.ts`
      - 控制场景切换关键帧插入参数sc_threshold: -g设置以帧数间隔为gop的长度，但是当遇到场景切换，会强行插入一个关键帧，这时GOP的间隔将会重新开始，这样的场景切换在点播视频中常见，sc_threshold参数设定以决定是否在场景切换时插入关键帧：`ffmpeg -i input.mp4 -c:v libx264 -g 50 -t 60 output.mp4`加入sc_threshold参数让gop插入的更均匀`ffmpeg -i input.mp4 -c:v libx264 -g 50 -sc_threshold 0 -t 60 -y output.mp4`此时场景切换不再插入关键帧，可以控制关键帧，在进行视频切片时会更方便
      - 设置x264内部参数x264opts：通过该参数设置x264内部私有参数(如I帧、P帧、B帧的顺序及规律等)
        - 如：控制I帧、P帧、B帧的顺序及出现频率`ffmpeg -i input.mp4 -c:v libx264 -x264opts "bframes=0" -g 50 -sc_threshold 0 output.mp4`这样可以在50帧内屏蔽B帧。
        - 如：控制I帧、P帧、B帧的频率与规律，可通过控制GOP中B帧的帧数来实现，P帧的帧率可通过x264的参数b-adapt设置,如设置GOP中，每2个P帧之间存放3个B帧`ffmpeg -i input.mp4 -c:v libx264 -x264opts "bframes=3:b-adapt=0" -g 50 -sc_threshold 0 output.mp4`
        - 提示：B帧越多，同等码率时清晰度越高，但越多B帧，编码和解码所带来的复杂度也越高
      - CBR恒定码率设置参数nal-hrd: ffmpeg通过-b:v指定视频的平均码率，并不能控制最大码率和最小码率的波动，可设置-b:v、maxrate、minrate。为了更好控制编码时的波动，还可以-bufsize设置buffer的大小`ffmpeg -i input.mp4 -c:v libx264 -x264opts "bframes=10:b-adapt=0" -b:v 1000k -maxrate 1000k -minrate 1000k -bufsize 50k -nal-hrd cbr -g 50 -sc_threshold 0 output.ts`
    - 硬编解码(基于CPU进行H.264编码成本较高性能低，常见的硬编码包含Nvidia GPU和Intel QSV，还有嵌入式平台树莓派等)
      - Nvidia GPU硬编码：`ffmpeg -h encoder=h264_nvenc` `ffmpeg -h dncoder=h264_nvenc` `ffmpeg -hwaccel cuvid -vcodec h264_cuvid -i input.mp4 -vf scale_npp=1920:1080 -vcodec h264_nvenc -acodec copy -f mp4 -y output.mp4`
      - Intel QSV硬编码：`ffmpeg -hide_banner -codecs|grep h264` `ffmpeg -h encoder=h264_qsv` `ffmpeg -i 10M1080P.mp4 -pix_fmt nv12 -vcodec h264_qsv -an -y output.mp4`
      - 树莓派硬编码：`--enable-omx-pi` `ffmpeg -i input.mp4 -vcodec h264_omx -b:v 500k -acodec copy -y output.mp4`
      - OS X系统硬编解码：硬编码h264_videotoolbox，硬解码h264_vda。`ffmpeg -vcodec h264_vda -i input.mp4 -vcodec h264_videotoolbox -b:v 2000k output.mp4`
    - 输出MP3(libmp3lame)
      - 得到音频编码为mp3封装文件：`ffmpeg -i input -acodec libmp3lame output.mp3`
      - MP3编码质量设置：-qscale: a控制，也可以用q参数控制，质量不同码率也不同`ffmpeg -i input.mp4 -acodec libmp3lame -q:a 8 output.mp3`这设置的是VBR码率,通过-b参数设置常见MP3编码CBR`ffmpeg -i input.mp3 -acodec libmp3lame -b:a 64k output.mp3`
      - 平均码率编码参数ABR: `ffmpeg -i input.mp3 -acodec libmp3lame -b:a 64k -abr 1 output.mp3`
    - 输出AAC(直播、点播最常用的音频编码方式, 比mp3编码效率更高音质更好，常见AAC编码后的文件存储格式为m4a如ipad和iphone）可支持aac ffmpeg内置[一般]、libfaac[最差]、libfdk_aac[最优]编码器
      - ffmpeg中的aac编码器：`ffmpeg -i input.mp4 -c:a aac -b:a 160k output.aac` `ffmpeg -i input.wav -c:a aac -q:a 2 output.m4a`
      - libfdk_aac编解码的Codec库：
        - 恒定码率CBR模式：`ffmpeg -i input.wav -c:a libfdk_aac -b:a 128k output.m4a`
        - 动态码率VBR模式：LC HE HEV2`ffmpeg -i input.wav -c:a libfdk_aac -vbr 3 output.m4a`
      - 高质量AAC设置：
        - HE-AAC:`ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a`
        - HEv2-AAC: `ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he_v2 -b:a 32k output.m4a`
    - 系统资源使用情况: 消耗CPU`ffmpeg -re -i input.mp4 -vcodec libx264 -an output.mp4`
  - **Ffmpeg流媒体**
    - 发布与录制RTMP流
      - rtmp_app参数设置RTMP的推流发布点`ffmpeg -rtmp_app live -i rtmp://publish.chinaffmpeg.com -c copy -f flv output.flv`录制 `ffmpeg -re -i input.mp4 -c copy -f flv -rtmp_app live rtmp://publish.chinaffmpeg.com`发布
      - rtmp_playpath参数解决identify stream failed错误：`ffmpeg -re -i input.mp4 -c copy -f flv -rtmp_app live -rtmp_playpath class rtmp://publish.chinaffmpeg.com` 测试播放`ffmpeg -rtmp_app live -rtmp_playpath class -i rtmp://publish.chinaffmpeg.com -c copy -f flv out.flv`
      - 省略rtmp_app、rtmp_playpath参数，直接设置在RTMP的连接中：`ffmpeg -i input.mp4 -c copy -f flv rtmp://publish.chinaffmpeg.com/live/class` 
      - rtmp_pageurl、rtmp_swfurl、rtmp_tcurl参数：rtmp_pageurl做标识与http请求中的referer防盗链基本认为起着相同作用。rtmp_pageurl参数可以设置pageurl,ffmpeg发起播放时不会在connect命令中携带pageurl字段`ffmpeg -rtmp_pageurl "http://www.chinaffmpeg.com" -i rtmp://publish.chinaffmpeg.com/live/class`只有服务器要求使用swf播放器和指定必须使用指定页时，这些参数的作用才会很大
    - 录制RTSP流（曾经的直播方式，如今在安防领域常见，互联网中大多数转向RTMP HTTP+FLV HLS DASH）
      - TCP方式录制RTSP直播流：ffmpeg默认使用的RTSP拉流的方式为UDP。`ffmpeg -rtsp_transport tcp -i rtsp://47.90.47.25/test.ts -c copy -f mp4 output.mp4`
      - User-Agent设置参数：区分在访问的时候是不是自己访问的流`ffmpeg -user-agent "ChinaFFmpeg-Player" -i rtsp://input:554/live/1/stream.sdp -c copy -f mp4 -y output.mp4`
    - 录制HTTP流(ffmpeg的HTTP既可以做客户端，也可以做服务端)
      - seekable参数进行播放进度移动、定位：`ffmpeg -ss 300 -seekable 0 -i http://bbs.chinaffmpeg.com/test.ts -c copy output.mp4`seekable为0则根据ss指定seek时间位置，会一直处于阻塞状态 `ffmpeg -ss 30 -seekable 1 -i http://bbs.chinaffmpeg.com/test.ts -c copy -y output.mp4`可对HTTP服务进行seek操作
      - headers参数：如使用HTTP传输时需要在header中设置referer字段`ffmpeg -headers "referer: http://bbs.chinaffmpeg.com/index.html" -i http://play.chinaffmpeg.com/live/class.flv -c copy -f flv -y output.flv`
      - user_agent参数：ffmpeg默认useragent为Lavf`ffmpeg -user_agent "YinLei's Player" -i http://bbs.chinaffmpeg.com/1.flv`
      - 拉取HTTP中的流录制FLV:
        - 拉取FLV直播流录制FLV:`ffmpeg -i http://bbs.chinaffmpeg.com/live.flv -c copy -f flv output.flv`
        - 拉取TS直播流录制FLV:`ffmpeg -i http://bbs.chinaffmpeg.com/live.ts -c copy -f flv output.flv`
        - 拉取HLS直播流录制FLV:`ffmpeg -i http://bbs.chinaffmpeg.com/live.m3u8 -c copy -f flv output.flv`
    - 录制和发布UDP\TCP流
      - TCP监听接收流：`ffmpeg -listen 1 -f flv -i tcp://127.0.0.1:1234/live/stream -c copy -f flv output.flv`
      - TCP请求发布流：`ffmpeg -re -i input.mp4 -c copy -f flv tcp://127.0.0.1:1234/lives/stream`
      - 监听端口超时listen_timeout: `ffmpeg -listen_timeout 5000 -listen 1 -f flv -i tcp://127.0.0.1:1234/live.stream -c copy -f flv output.flv`
      - tcp拉流超时timeout: `ffmpeg -timeout 20000000 -i tcp://192.168.100.179:1935/live/stream -c copy -f flv output.flv`
      - TCP传输buffer大小设置send_buffer_size/recv_buffer_size: `ffmpeg -re -i input.mp4 -c copy -send_buffer_size 265 -f flv tcp://192.168.100.179:1234/live/stream`
      - 绑定本地UDP端口localport: `ffmpeg -re -i input.mp4 -c copy -localport 23456 -f flv udp://1+2.168.100.178:1234/live/stream`
    - 推多路流
      - 管道方式输出多路流：一次转码多次输出封装`ffmpeg -i input -acodec aac -vcodec libx264 -f flv - | ffmpeg -f mpegts -i - -c copy output1 -c copy output2 -c copy output3` `ffmpeg -i input.mp4 -vcodec libx264 -acodec aac -f flv - | ffmpeg -f flv -i - -c copy -f flv rtmp://publish.chinaffmpeg.com/live/stream1 -c copy -f flv rtmp://publish.chinaffmpeg.com/live/stream2`
      - tee封装格式输出多路流：-f tee方式指定输出格式一次编码多路输出`ffmpeg -re -i input.mp4 -vcodec libx264 -acodec aac -map 0 -f tee "[f=flv]rtmp://publish.chinaffmpeg.com/live/stream1 | [f=flv]rtmp://publish.chinaffmpeg.com/live/stream2"`
      - tee协议输出多路流：`ffmpeg -re -i input.mp4 -vcodec libx264 -acodec aac -f flv "tee:rtmp://publish.chinaffmpeg.com/live/stream1|rtmp://publish.chinaffmpeg.com/live/stream2"`
    - 生成HDS流
      - window_size参数控制文件列表大小：HDS直播模式需要实时更新列表，可通过该参数控制文件列表窗口大小`ffmpeg -i input -c copy -f hds -window-size 4 output`
      - extra_window_size参数控制文件个数：控制残留文件个数`ffmpeg -re -i input.mp4 -c copy -f hds -window_size 4 -extra_window_size 5 output`
      - remove_at_exit参数在ffmpeg退出时删除所有生成文件.如果min_frag_duration参数的值设置的比较小并且设置在使用codec copy时不会有效果，则需要在重新编码时将gop间隔设置的比min_frag_duration时间短即可
    - 生成DASH流
      - window_size和extra_window_size参数和HDS一样`ffmpeg -re -i input.mp4 -c:v copy -acodec copy -f dash -windows_size 4 -extra_window_size 5 index.mpd`
      - single_file参数：将切片列表中的文件写入到一个文件`ffmpeg -re -i input.mp4 -c:v copy -acodec copy -f dash -window_size 4 -extra_window_size 5 -single_file 1 index.mpd`

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