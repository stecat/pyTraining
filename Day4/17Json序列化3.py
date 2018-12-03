# Author：Steve

# 多次序列化

info={
    'name':"alex",
    'age':22,
}
import json
f=open("test.txt","w")

f.write(json.dumps(info))

info['age']=18
f.write(json.dumps(info))

f.close()