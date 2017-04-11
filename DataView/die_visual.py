# coding=utf-8
from die import Die
import pygal

# 创建一个D6
die = Die()

# 创建一个列表来存放扔骰子的结果
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print results

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 100 times."
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')