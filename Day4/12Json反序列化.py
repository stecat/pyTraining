# Author：Steve

f=open("test.txt","r")

#data=f.read()
#print(data)
# data1=eval(f.read())
# print(data1)

#用json反序列化  json.loads()
import json
data3=json.loads(f.read())
print(data3['age'])
