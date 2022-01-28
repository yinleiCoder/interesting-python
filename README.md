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
- advance_python: python高级编程
- 高等数学
- 线性代数
- algorithm_data_structure: 数据结构和算法
    - 算法、数据结构、时间复杂度、空间复杂度
    - 最基本的数据结构：数组、链表、栈、队列、哈希表
    - 树、二叉树
    - 排序算法：冒泡排序、快速排序、堆排序、计数排序、桶排序
    - 职场上的算法面试题及解题思路
    - 职场上的算法应用
- automate_the_boring_stuff: 让繁琐工作自动化
    - pyperclip_reply_msg: 使用多剪贴板自动回复消息(pyperclip)
    - bullet_point_adder: 在Wiki标记中添加无序列表(pyperclip)
    - analzy_phone_email: 电话号码和E-mail地址提取(模式匹配与正则表达式)
    - input_valid: 输入验证(PyInputPlus)
    - read_write_file: 读写文件(pathlib与/)【生成随机的测试试卷、可更新的多重剪贴板(shelve)】
    - manage_file: 组织文件【将带有美国风格日期的文件重命名为欧洲风格日期、将一个文件夹备份到一个ZIP文件(zipfile、send2trash、shutil)】
    - 调试
    - 从Web抓取信息
    - 处理Excel电子表格
    - 处理Google电子表格
    - 处理PDF、Word
    - 处理CSV、JSON
    - 保持时间、计划任务和启动程序
    - 发送电子邮件和短信
    - 操作图像
    - 用GUI自动化控制键盘和鼠标 
- 爬虫
- 极客项目
- opencv_py: 计算机视觉与OpenCV
    - opencv_what: OpenCV介绍
    - img_video_load_show: 图像与视频的加载和展示
    - opencv_basic: OpenCV基础【色彩空间变换、像素访问、矩阵的操作、Mat数据结构】
    - paint_shape: 基本图形的绘制【线、矩形、圆、椭圆、多边形、字体】
    - image_operation: 图像运算【图像的加法、减法、乘法、除法、溶合、位操作】
    - image_transform: 图像基本变换【图像的放大、缩小、翻转、旋转、仿射变换、透视变换】
    - opencv_filter: 滤波器【图像滤波、卷积、低通滤波、高通滤波、方盒滤波、均值滤波、高斯滤波、中值滤波、双边滤波、高通滤波(索贝尔算子、沙尔算子、拉普拉斯算子)、边缘检测Canny】
    - opencv_morphology: 形态学图像处理【二值化、腐蚀与膨胀、开运算、闭运算、顶帽、黑帽】
    - opencv_contours: 目标识别/轮廓【查找轮廓、绘制轮廓、轮廓的面积与周长、多边形逼近与凸包、外接矩形】
    - vehicle_count: 车辆统计【结合以上opencv知识实战】
    - feature_detection: 特征点检测与匹配【Harris角点检测、Shi-Tomasi角点检测、SIFT关键点检测、SURF特征检测、ORB特征检测、暴力特征匹配、FLANN特征匹配、图像查找单应性矩阵】
    - image_connect: 图像拼接【结合以上特征点检测与匹配知识实战】
    - image_segmentation_restoration: 图像分割与修复【分水岭法、GrabCut法、MeanShift法、背景扣除(MOG去背景、MOG2去背景、GMG去背景)、图像修复】
    - opencv_machine_learning_face: OpenCV机器学习【Haar(哈尔)级联方法人脸识别、深度学习DNN人脸识别方法、Haar+Tesseract识别车牌】
- china_unicom_ocr_text_bill：中国联通增值税发票OCR
- 游戏编程：
    - 外星人入侵
- 数据可视化:
- 数据分析
- 后端django
- quantitative_trading: 量化交易[量化过去，预测未来(经济领域)]
    - trading_what: 量化简介【量化交易策略、常用的股票量化指标】
    - get_stock_data: 获取股票数据【股票是什么、使用JQData获取行情数据、Resample函数转化时间序列、使用JQData查询财务指标、】
    - 计算交易指标
    - 设计交易策略：择时策略
    - 设计交易策略：选股策略
    - 数据回测与优化
    - 实现股票实盘交易
    - 进阶计划(结合机器学习)
- 深度学习之神经网络CNN RNN GAN算法原理
    - 神经网络简介
    - 卷积神经网络
    - 卷积神经网络进阶
    - 卷积神经网络调参
    - 图像风格转换
    - 循环神经网络
    - 图像生成文本
    - 对抗神经网络
    - 自动机器学习网络AutoML 
- tensorflow_ml: Tensorflow2.x深度学习
    - tensorflow_what_install: Tensorflow简介与环境搭建【Tensorflow是什么、Tensorflow历史、Tensorflow VS Pytorch、多平台环境配置】
    - tensorflow_keras_basic: Tensorflow keras【tf框架：keras、回调函数；分类问题、回归问题、损失函数、神经网络、激活函数、批归一化、Dropout、Wide & deep模型、超参数搜索。(图像分类、房价预测)】
    - Tensorflow基础API【tf框架：基础数据类型、自定义模型与损失函数、自定义求导、tf.function、图结构(图像分类、房价预测)】
    - Tensorflow dataset使用【tf框架：csv文件读取、tfrecord文件生成与读取、tf.data使用(房价预测)】
    - Tensorflow Estimator使用与tf1.0【tf框架：estimator使用、特征列使用、tf1.0基本使用(泰坦尼克生存预测)】
    - 卷积神经网络【tf框架：卷积实现；卷积、数据增强、迁移学习(图像分类、Kaggle 10monkeys、kaggle cifar10)】
    - 循环神经网络【tf框架：LSTM实现；序列式问题、循环网络、LSTM、双向LSTM(文本分类、文本生成、Kaggle文本分类)】
    - Tensorflow分布式【tf框架：分布式实现；分布式原理与策略(图像分类)】
    - Tensorflow模型保存与部署【tf框架：模型保存、导出tflite、部署;(图像分类)】
    - 机器翻译与tensor2tensor【tf框架：transformer实现、tensor2tensor使用;序列到序列模型、注意力机制、可缩放点积注意力、多头注意力(机器翻译)】

## 后续学习方向建议
`研究生及以后职业规划的学习方向，仅供参考`
- 微积分
- 线性代数
- [人工智能](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NzkxMzg2NQ==&action=getalbum&album_id=1733540329405923330#wechat_redirect)
- 树莓派

## 推荐相关书籍
`以下图书均可在“京东图书”购买电子版阅读。`
- [Python编程：从入门到实践(第二版)]()
- [Python编程快速上手——让繁琐工作自动化(第二版)]()
- [Python极客项目编程]()
- [用Python学数学]()
- [小灰漫画算法(Python版) ]()
- [ Python3网络爬虫开发实战 第二版 (崔庆才) ]()
- [ 西瓜书 ]()

## Hacker
`抛开用工具做脚本小子的想法，做黑客要有创新、研发的精神。抛开浮躁，静下心来从头开始学习基础，为将来的成长做好足够的准备！`
- [Python白帽子]()

## 推荐B站UP主
`以下均是素未蒙面的各领域的启蒙老师或本人觉得十分干货的UP主，感谢各位前辈！`
- [(公务员)刘文超](https://space.bilibili.com/300722822/video)
- [(英语)英语兔](https://space.bilibili.com/483162496/video)
- [(C)谭玉刚](https://space.bilibili.com/41036636/channel/detail?cid=161507&ctype=0)
- [(C++、算法)代码随想录](https://space.bilibili.com/525438321/video)
- [(C++、C、Kotlin)bennyhuo不是算命的](https://space.bilibili.com/28615855/video)
- [(C++、算法)花花酱的表世界](https://space.bilibili.com/9880352/video)
- [(C)编程日课DailyCoding](https://space.bilibili.com/494537125/)
- [(全栈)free-coder](https://space.bilibili.com/31273057/video)
- [(Go)橙卡](https://space.bilibili.com/10/video)
- [(Go)幼麟实验室](https://space.bilibili.com/567195437/video)
- [(Java)颜群](https://space.bilibili.com/326782142/video)
- [(人工智能)同济子豪兄](https://space.bilibili.com/1900783/video)
- [(前端)CodingStartup起码课](https://space.bilibili.com/451368848/)
- [(前端)峰华前端工程师](https://space.bilibili.com/302954484/)
- [(前端)向军大叔](https://space.bilibili.com/282190994/video)
- [(Android)longway777](https://space.bilibili.com/137860026/video)
- [(Android)扔物线](https://space.bilibili.com/27559447/video)
- [(iOS)Xiaoyouxinqing](https://space.bilibili.com/502566212/video)
- [(Flutter)ducafecat](https://space.bilibili.com/404904528/video)
- [(硬件)硬件茶谈](https://space.bilibili.com/14871346/video)
- [(嵌入式)太极创客](https://space.bilibili.com/103589285/video)
- [(理财)DeltaF](https://space.bilibili.com/31721731/video)
- [(吉他)吉他情报局](https://space.bilibili.com/103600069/video)

### —— Google.End@YinLei.Coder ——