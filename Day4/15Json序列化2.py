# Author：Steve
def sayhi(name):
    print("hello",name)

info={
    'name':"alex",
    'age':22,
   # 'func_sayhi':sayhi    #直接传函数sayhi的内存地址，不要调用（调用式sayhi()）
}
import pickle
f=open("test.txt","wb")

pickle.dump(info,f)   # 等于pickle.dumps(info),就不用写write了
f.close()