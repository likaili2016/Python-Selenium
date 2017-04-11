# coding=utf-8
import matplotlib.pyplot as plt

x_value = list(range(0, 1001))
y_value = [x**3 for x in x_value]
plt.plot(x_value, y_value, linewidth=5)
# 设置图表的标题
plt.title('Test1', fontsize=20)
# 设置x轴的参数名称
plt.xlabel('value', fontsize=14)
# 设置y轴的参数名称
plt.ylabel('Cube of Value', fontsize=14)
# 设置刻度的大小
plt.show()

