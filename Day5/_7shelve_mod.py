# --* utf-8 *--
# Author：Steve

# shelve模块：是一个简单的kv(key,value)，将内存数据通过文件持久化的模块，可以持久化pickle可支持的python数据格式
# shelve是pickle更上一层的封装
import shelve
import datetime

d = shelve.open("shelve")  # d是一个句柄，打开文件
'''写入'''
name = ['steve', 'rain', 'test']
info = {
    'age': 22,
    'job': 'sales',
}
d["name"] = name  # 持久化列表
d["info"] = info
d['date']=datetime.datetime.now()
d.close()

'''读
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
'''