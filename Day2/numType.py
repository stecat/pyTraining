# -*- coding:utf-8 -*-
# Author：Steve

# python 中没有long型
print(type(2**32))  # 2的32次方
print(type(2**64))

# 3元运算： result =值1 if 条件 else 值2  如果条件为真result=值1，否则 result=值2
a, b, c = 1, 3, 5
d = a if a > b else c
print(d)

# bytes类型（字节数据类型） strings can be encoded编码 to bytes, and bytes can be decoded解码 back to strings
msg = "迷糊"
print(msg)
print(msg.encode())
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode())
print(msg.encode().decode())
