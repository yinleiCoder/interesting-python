"""
Keras:
    基于python的高级神经网络API
    Francois Chollet于2014-2015年编写Keras
    以Tensorflow、CNTK或者Theano为后端运行，Keras必须有后端才能运行
    后端可以切换，但现在多用Tensorflow
    极方便于快速实验，帮助用户以最少的时间验证自己的想法

Tensorflow-keras:
    Tensorflow对Keras API规范的实现
    相对于以Tensorflow为后端的keras, Tensorflow-keras与Tensorflow结合更加紧密
    实现在tf.keras空间下

Tf-keras和Keras:
    基于同一套API：
        keras程序可以通过改导入方式轻松转为tf.keras程序
        反之可能不成立，因为tf.keras有其他特性
        相同的JSON和HDF5模型序列化格式和语义
    Tf.keras全面支持eager mode:
        只是用keras.Sequential、keras.Model时没影响
        自定义Model内部运算逻辑的时候会有影响
        Tf低层API可以使用keras的model.fit等抽象
        适用于研究人员
    Tf.keras支持基于tf.data的模型训练
    Tf.keras支持TPU训练
    Tf.keras支持tf.distribution中的分布式策略
    Tf.keras可以与Tensorflow中的estimator集成
    Tf.keras可以保存为SavedModel

如果想用tf.keras的任何一个特性，那么选tf.keras.如果后端互换性很重要，那么就选keras.如果都不重要，那么随便。
"""