import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = "data/sitka_weather_07-2018_simple.csv"
filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 日期、最高温度、最低温度
    dates, highs, lows = [], [], []
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'missing data of {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title('the max temp of 2018 every day', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temp(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()