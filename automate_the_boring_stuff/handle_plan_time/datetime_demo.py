import datetime
import time

"""
datetime:
"""


print(datetime.datetime.now())
dt = datetime.datetime(2022, 3, 31)
print(dt.year, dt.month, dt.day)

print(datetime.datetime.fromtimestamp(time.time()))

dt1 = datetime.datetime(2021, 6, 30)
dt2 = datetime.datetime(2022, 3, 31)
print(dt1 == dt2)
print(dt1 < dt2)
print(dt1 > dt2)
print(dt1 != dt2)


# timedelta表示时段
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

# 日期计算, 如计算10天后
dt = datetime.datetime.now()
tenDays = datetime.timedelta(days=10)
print(dt + tenDays)

# datetime转为字符串
"""
%Y 带世纪的年份，如2022
%y 不带世纪的年份，00到99
%m 数字表示的月份，01到12
%B 完整的月份,如November
%b 简写的月份，如Nov
%d 一月中的第几天,01到31
%j 一年中的第几天，001到366
%w 一周中的第几天,0表示周日到6周六
%A 完整的周几，如  Monday
%a 简写的周几，如Mon
%H 小时 00到23
%l 小时 01到12
%M 分 00到59
%S 秒 00到59
%% 就是%
"""
monthDemo = datetime.datetime(2022, 4, 1, 8, 0, 0)
print(monthDemo.strftime('%Y/%m/%d %H:%M:%S'))

# 字符串转为datetime
print(type(datetime.datetime.strptime('2022/04/01 08:00:00', '%Y/%m/%d %H:%M:%S')))

