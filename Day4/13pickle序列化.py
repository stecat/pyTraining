# Author：Steve

#如果要处理复杂的数据格式就要用pickle，比如带函数的序列化
#pickle可以序列化一切数据

def sayhi(name):
    print("hello",name)

info={
    'name':"alex",
    'age':22,
    'func_sayhi':sayhi    #直接传函数sayhi的内存地址，不要调用（调用式sayhi()）
}

f=open("test.txt","wb")

import pickle
print(pickle.dumps(info))
f.write(pickle.dumps(info))   #pickle.dumps()默认是二进制，需要用wb的读方式变成str
f.close()