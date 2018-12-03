# Author：Steve

# 密文pwd输入
# pycharm用不了getpass包，直接去terminal中启就可以：直接到cd到encrptPwd.py存放目录下，输入python encrptPwd.py启动

import getpass

name = input("name:")
password = getpass.getpass("password:")

print(name, password)
