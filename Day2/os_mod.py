# -*- coding:utf-8 -*-
# Author：Steve

# os模块可以直接调用使用命令行：
import os
os.system("ls")

lunix_res = os.system("ls")  # 执行结果为0，在lunix下执行成功为0，所以此语句只记录执行结果不记录执行内容
print("----->", lunix_res)

lunix_res2 = os.popen("ls")   # 执行结果为对应地址
print("lunix_res2----->", lunix_res2)

lunix_res3 = os.popen("ls").read()   # 执行结果为对应内容
print("lunix_res3----->", lunix_res3)

'''
# 创建目录
os.mkdir("haha")
'''
