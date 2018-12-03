# Author：Steve

#多次反序列化,但是3.0无法load多次，所以无法多次
f=open("test.txt","r")


import json
data3=json.loads(f.read())
print(data3['age'])

