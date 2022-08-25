"""
Pytorch简介与环境搭建:
    Facebook人工智能研究员FAIR于2017年在Github上开源
    Torch(c、c++)->PyTorch
    对于人工智能入门，想要快速取得成就，推荐Pytorch，最后过渡到Tensorflow上。

    为什么选择Pytorch:
        活跃度——逐渐形成了完整的开发生态，资源多
        动态图——动态图架构，且运行速度较快
            动态图：编好程序即可执行
            静态图：先搭建计算图，后运行；允许编译器进行优化
        代码简洁——易于理解，设计优雅，易于调试
        简洁性——编程同Python几乎一致
        动态计算
        visdom
        部署不方便
        （学术界Pytorch，工业界Tensorflow)

    Pytorch环境搭建：
        Ubuntu18.x -> CUDA+cuDNN -> Python3+pip3(Anaconda) -> Pytorch
        Ubuntu最好安装双系统，不要使用虚拟机
        如果有条件，尽量使用高配置台式机或高性能的笔记本(GTX1080Ti+16G内存，但是最好是台式机，笔记本玩深度学习本来就...)
        安装显卡驱动：去Tensorflow官网上看，教程很详细(nvidia-smi)
                    CUDA9.0 或 CUDA10.0 或 CUDA10.1
                    cuDNN

        Pytorch: https://pytorch.org/
                官网上copy命令即可,如我这里下载的是CPU版本：pip install torch torchvision torchaudio

"""