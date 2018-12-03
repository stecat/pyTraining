# Author：Steve

import random

# 生成4位随机的验证码
checkcode = ''

for i in range(4):
    randm = random.randint(0, 9)
    checkcode += str(randm)

print(checkcode)

# 随机生成字母+数字的验证码

code = ''
for i in range(4):
    randm = random.randrange(0, 4)
    # 字母 用chr(90)把数字转换为字母
    if randm == i:
        tmp = chr(random.randint(65, 90))
    # 数字
    else:
        tmp = random.randint(0, 9)

    code += str(tmp)

print(code)
