# coding=utf-8
import matplotlib.pyplot as plt

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolors='none', s=40)
# 设置图表的标题
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')  # 如果不把plt.show()注释保存的图片内容是空的
plt.savefig('squares_plot1.png')