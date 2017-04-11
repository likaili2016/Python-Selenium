# coding=utf-8
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]  # plot()函数默认第一个数据点对应的x坐标为0，为了改变默认我们要提供输入值和输出值
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # 设置曲线的宽度为5

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)  # 给图表指定标题
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.ticklabel_format(axis="both", lablesize=14)
plt.show()
