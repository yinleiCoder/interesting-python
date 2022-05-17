from plotly.graph_objs import Bar, Layout
from plotly import offline

from die_visual import Die
"""
Plotly模拟掷骰子：
    抛掷一个6面的常规骰子时，可能出现的结果为1~6点，且出现每种结果的可能性相同。
    然而，若同事抛掷2个骰子，某些点数出现的可能性将比其他点数大。
    为确定那些点数出现的可能性最大，将生成一个表示投掷骰子结果的数据集，并绘制图形。

Plotly(交互式图表)：https://plotly.com/
pip install plotly
"""

die1 = Die()
die2 = Die()
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# print(results)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 可视化结果
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'point', 'dtick': 1}
y_axis_config = {'title': 'frequency'}
my_layout = Layout(title='The result of throwing a D6 that 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
