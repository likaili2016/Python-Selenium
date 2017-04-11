# coding=utf-8

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()  # num_points默认值是5000，在RandomWalk定义的
    rw.fill_walk()

    # 设置绘图窗口的大小
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # plt.plot(rw.x_value, rw.y_value, linewidth=5)

    # 突出起点和终点,如果这两行代码放在前面的话就会被各个点埋没
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴,False 为不显示
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # 只有把弹出的图表关闭了才会执行下面的语句
    keep_running = raw_input("Make another walk (y/n):")  # python 版本是2.7的是raw_input 函数，Python3是input函数
    if keep_running == 'n':
        break

