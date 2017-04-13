# coding=utf-8
from die import Die
import pygal

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 创建一个列表来存放扔骰子的结果
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# 分析结果
frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for value in range(2, max_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print frequencies

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times."
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')