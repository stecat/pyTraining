# Author：Steve

#字典循环
info = {
    'stu2101': "wa",
    'stu2102': "sa",
    'stu2103': "la"
}

for i in info:
    print(i)         # 打印字典key

for i in info:
    print(i, info[i])  # 打印字典key和value的方法1，方法1比2高效很多，因为2会把字典转为列表

for k, v in info.items():   # 打印字典key和value的方法2
    print(k, v)
