# Author：Steve
# datetime 模块
import datetime

print(datetime.datetime.now())  # 获取当前时间
# datetime.timedelta()不能独立使用，必须和固定时间点进行合用
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(hours=-3))  # 当前时间-3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=-3))  # 当前时间-3分钟

# replace()  时间替换
# datetime.datetime.now().replace(minute=3, hour=2)
current_time = datetime.datetime.now()
print(current_time.replace(minute=3, hour=2))  # 时间替换