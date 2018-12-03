# Author：Steve
import time

print("time():", time.time())  # 加时间戳，时间戳是秒为单位，以unix元年1970?为计算基准

print("localtime():", time.localtime())  # 结构化元组
x = time.localtime()
# help(x)  ---》可以通过help来看帮助
print("x.tm_year:", x.tm_year)
print("this is 1973 day：%d" % x.tm_yday)

# 结构化元组转换为时间戳用time.mktime()
y = time.struct_time([2018, 11, 29, 19, 23, 13, 3, 333, 0])
print(time.mktime(y))

# 格式化输出
# strftime('格式'，'struct_time格式化时间字符串')  定义输出对应格式的时间
print(time.strftime("%Y~~%d %H~%M~%S %m", x))
# strptime('struct_time格式化时间字符串'，'格式')  把对应格式的时间转回struct_time元组
print(time.strptime('~11~29 19~34~36 2018', "~%m~%d %H~%M~%S %Y"))  # 必须年月日时分秒一一对应

# asctime(): convert tuple to string, 默认值为localtime()
print(time.asctime())
# ctime(): convert Time stamp时间戳(单位秒) to string ,默认为localtime()
print(time.ctime(1543490593))
