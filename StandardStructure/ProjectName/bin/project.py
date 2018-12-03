# Author：Steve

print(__file__)   # 打印当前路径
#  为了导入conf和core的执行文件加载到环境变量后这边就可以直接调用

import os
print(os.path.abspath(__file__))   #  获取绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   #  dirname()是返回目录名不要文件名，但是此时只在bin下，得去父级目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #  此时到了bin的父级目录

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(BASE_DIR)    # 把父级目录加入环境变量，这样才能调用core和conf下面的文件

#from conf import settings
from core import main        # 直接可以调用main中login()方法，报错是因为python是动态加载的
main.login()
