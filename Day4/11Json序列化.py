# Author：Steve
#序列化，把内存数据对象变成字符串

def sayhi(name):
    print("hello",name)

info={
    'name':"alex",
    'age':22,
   # 'func_sayhi':sayhi    #直接传函数sayhi的内存地址，不要调用（调用式sayhi()）
}

f=open("test.txt","w")
#f.write(info)  需要转成字符串,使用以下
#f.write(str(info))


# 直接用json序列化,json是不同语言通用，不同语言和程序间数据交互的方式，但默认只进行简单的，xml正在被json取代
import json
print(json.dumps(info))
f.write(json.dumps(info))
f.close()
#如果要处理复杂的数据格式就要用pickle