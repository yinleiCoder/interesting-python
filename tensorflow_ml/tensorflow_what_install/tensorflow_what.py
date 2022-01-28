"""
Tensorflow是什么：（高度的灵活性、真正的可移植性、产品和科研结合、自动求微分、多语言支持、性能最优化）
    Google的开源软件库
    采用数据流图，用于数值计算
        数据流图包括：
            节点——处理数据
            线——节点间的输入输出关系
            线上运输张量Tensor,即数据
            节点被分配到各种计算设备上运行
    支持多种平台(GPU、CPU、移动设备)
    最初用于深度学习，变得越来越通用

Tensorflow版本变迁：
    2015年——11月Tensorflow宣布开源并首次发布；
            12月支持GPUs, Python3.3(v0.6)
    2016年——4月分布式Tensorflow(v0.8)
            11月支持windows(v0.11)
    2017年——2月性能改进，API稳定性(v1.0)
            4月Keras集成(v1.1)
            8月高级API，预算估算器，更多模型，初始TPU支持(v1.3)
            11月Eager execution、Tensorflow Lite(v1.5)
    2018年——3月推出TF Hub,Tensorflow.js,Tensorflow Extended(TFX)
            5月Cloud TPU模块于管道(v1.6)
            6月新的分布式策略API，概率编程工具Tensorflow Probability(v1.8)
            8月Cloud Big Table集成(v1.10)
            10月侧重于可用性的API改进(v1.12)
    2019年——Tensorflow v2.0发布

Tensorflow1.0主要特性：
    XLA——Accelerate Linear Algebra(提升训练速度58倍，可在移动设备上运行)
    引入更高级的API——tf.layers/tf.metrics/tf.losses/tf.keras
    Tensorflow调试器
    支持docker镜像，引入tensorflow serving服务

Tensorflow1.0架构：
    CannedEstimators
    Estimator KerasModel        Datasets
    Layers
    PythonFrontend C++ JAVA GO 。。。
    Tensorflow Distributed Execution Engine
    CPU GPU ANDROID IOS XLA
                        CPU、GPU、TPU。。。

Tensorflow2.0主要特性：
    使用tf.keras和eager mode进行更加简单的模型构建
    鲁棒的跨平台模型部署
    强大的研究实验
    清除不推荐使用的API和减少重复来简化API

Tensorflow2.0架构：
    TRAINING                                                DEPLOYMENT
Read & Preprocess Data
tf.data, feature columns                                Tensorflow Serving(cloud, on-prem)
 |                  |
 | TensorFlow Hub   |                                   Tensorflow Lite(Android, iOS, Raspberry Pi)
tf.keras         Premade Estimators       SavedModel
 |                  |
Distribution Strategy                                   Tensorflow.js(Browser and Node Server)
        |
CPU     GPU         TPU                                 Other Language Bindings(C, JAVA, GO, C#, RUST, R...)

Tensorflow2.0简化模型开发流程：
    使用tf.data加载数据
    使用tf.keras构建模型，也可以使用premade estimator验证模型
    使用tensorflow hub进行迁移学习
    使用eager mode进行运行和调试
    使用分发策略来进行分布式训练
    导出到SavedModel
    使用Tensorflow Serve(直接通过HTTP/REST或GRPC/协议缓冲区)、Tensorflow Lite、Tensorflow.js部署模型

Tensorflow2.0强大的研究实验：
    Keras功能API和子类API，允许创建复杂的拓扑结构
    自定义训练逻辑，使用tf.GradientTape和tf.custom_gradient进行更细粒度的控制
    低层API自始至终可以于高层结合使用，完全的可定制
    高级扩展：Ragged Tensors、Tensor2Tensor等

Tensorflow VS Pytorch:
    入门时间:
        Tensorflow1.x静态图、学习额外概念(图、会话、变量)、写样板代码
        Tensorflow2.x动态图、Eager mode避免1.x缺点，直接集成在python中
        Pytorch动态图、Numpy的扩展，直接集成在python中
    图创建和调试
        Tensorflow1.x静态图、难以调试，需要学习tfdbg调试
        Tensorflow2.x动态图、Python自带的调试工具
        Pytorch动态图、==Python自带的调试工具
    全面性
        随着时间的变化，越来越接近，
        pytorch缺少：
            沿维翻转张量(np.flip, np.flipud, np.fliplr)
            检查无穷与非数值张量(np.is_nan,np.is_inf)
            快速傅里叶变换(np.fft)
    序列化与部署
        Tensorflow支持更加广泛：图保存为protocol buffer, 跨平台、跨语言
        Pytorch支持比较简单

Tensorflow环境搭建：
    本地配置：
        GPU版(安装显卡驱动->Cuda安装->Cudnn安装)：https://blog.csdn.net/u014595019/article/details/53732015
        非GPU版：pip install tensorflow
                https://tensorflow.google.cn/
                Kaggle Tensorflow: https://www.kaggle.com/c/tensorflow-great-barrier-reef
    云端配置：
        Google Cloud
        Amazon
        Colab笔记本(推荐)

为什么要学习Tensorflow:
    深度学习迅猛发展
    模型框架强大灵活
    Google+开源社区背书
    在公司中应用广泛
    Tensorflow2.x颠覆了1.x反人类写法

实战训练：
    图像分类
    房价预测
    泰坦尼克生存预测
    文本分类
    文本生成
    机器翻译

学习目标：
    模型训练
    模型保存与部署
    分布式训练
    Tensorboard
    Tfds/tfhub
    tensor2tensor

多平台云端环境GPU搭建：
    Google cloud
    AWS

用到的kaggle数据集:
    Kaggle 10 Monkeys数据集
    Kaggle cifar10数据集
    Kaggle文本分类
    Kaggle Titanic生存预测
"""
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy())