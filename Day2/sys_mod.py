# -*- coding:utf-8 -*-
# Author：Steve

# 模块导入：
# python3 中自己命名的模块名和库名相同的情况下（如sys）不会报错，会直接调用你命名的sys文件的路径，但实际sys.path是sys库自带的方法
# 所以模块名尽量不要和库名重复
# python 库一般存放在/usr/local/lib/python3.7/site-packages,所以只要找site-packages即可，
# sys模块找不到是因为是python解释器自带的是c语言编译

import sys
print(sys.path)  # 打印环境变量
print(sys.argv)  # pycharm会打印绝对路径，终端会打印相对路径
print(sys.argv[2])  # 取路径中的第3个[0],[1],[2]

