import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""
数据可视化，让甲方爸爸不说话！
数据可视化：通过可视化表示来探索数据，与数据分析紧密相关。
数据分析：使用代码来探索数据集的规律和关联。
数据集：可以是一行代码就能表示的小型数字列表，也可以是数千兆字节的数据。

数据可视化的意义：通过引人注目的方式呈现数据，发现数据集中原本未知的规律和意义。

Matplotlib: https://matplotlib.org/
pip install matplotlib

"""
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)# figsize指定生成的图形的尺寸，单位为英寸，matplotlib假定屏幕分辨率为100像素/英寸. 1英寸=2.54厘米
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0, 0, c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('make another walk?(y/n)')
    if keep_running == 'n':
        break

# 散点图
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)# cmap为颜色映射
# ax.set_title('Square Number', fontsize=24)
# ax.set_xlabel('Number', fontsize=14)
# ax.set_ylabel("Number's square", fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)#刻度标记的大小
# ax.axis([0, 1100, 0, 1100000])# 设置每个坐标轴的取值范围
# plt.savefig('squares_plot.png', bbox_inches='tight')
# # plt.show()

## 简单的折线图
# print(plt.style.available)# 获取可用的内置样式
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.style.use('Solarize_Light2')# 使用内置样式
# flg, ax = plt.subplots()# flg为整张图，ax为图片中的各个图表
# ax.plot(input_values, squares, linewidth=3)
# ax.set_title('Square Number', fontsize=24)
# ax.set_xlabel('Number', fontsize=14)
# ax.set_ylabel("Number's square", fontsize=14)
# ax.tick_params(axis='both', labelsize=14)#刻度标记的大小
# plt.show()