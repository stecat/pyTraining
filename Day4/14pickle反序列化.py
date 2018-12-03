# Author：Steve
f=open("test.txt","rb")


def sayhi(name):
    print("hello2",name)

#用pickle反序列化  pickle.loads()
import pickle
data3=pickle.loads(f.read())
print(data3)
print(data3['func_sayhi']("steve"))   #请先执行文件 13pickle序列化，才能用

#会报AttributeError: Can't get attribute 'sayhi' on <module '__main__' from...的error，因为函数会在执行完毕时生命周期就已经结束，所以就没有
#所以想序列化函数就在同一个程序文件内进行
