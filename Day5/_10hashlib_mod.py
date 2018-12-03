# Author：Steve
# hashlib模块：3.x里代理了md5模块和sha模块：加密算法，都是基于hash，可用户网站防篡改。sha比md5更安全
# md5值无法反解
import hashlib

m = hashlib.md5()
m.update(b"hello")  # b 是bytes类型
print(m.digest())
m.update(b"it's me")
print(m.hexdigest())  # hexdigest为十六进制， 这里打印其实表示的是it's me + hello

m2 = hashlib.md5()
m.update(b"helloit's me")
print(m.hexdigest())

# sha512是目前最复杂的， 有sha1，sha256, sha384.....， 尾数越大越复杂
s2 = hashlib.sha3_512()
s2.update(b"hello it's me")
print(s2.hexdigest())


'''
更屌的加密， hmac模块：内部对创建key和内容再进行处理再加密
'''

import hmac
h = hmac.new(b"hi!steve", b"the king")
print(h.digest())
print(h.hexdigest())
h_encode = hmac.new("哈哈哈哈哈".encode(encoding="utf-8"))  # 若不加.encode()则会报错，因为是unicode
print(h_encode.hexdigest())