# Author：Steve

f=open("test.txt","rb")

#data=f.read()
#print(data)
# data1=eval(f.read())
# print(data1)

#用json反序列化  pickle.load(文件句柄)
import pickle
data3=pickle.load(f)   # 等于data3=pickle.loads(f.read())，就不用用read()
print(data3['age'])
