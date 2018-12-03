# Author：Steve
# 导入包其实就是在执行包下的__init__.py文件
import package

# 以下是不同目录下调用情况
import sys,os     # 使用os模块可以找到父级变量名
print(sys.path)     # 其实这个就是环境变量，需要把父级目录放到sys.path里面
print(os.path.abspath(__file__))   # 当前目录的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 找到父级路径
''' 将父级路径加入sys.path即可找到import的文件,使用append加入，但是会加到列表最后，如果遍历的时候其他package有重名那会导致哪个package在前面就哪个生效
    解决这个问题的办法是使用insert()进行父级目录地址的插入，insert是在列表最前面进行插入
'''
#sys.path.append()
father_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,father_path)    # insert(index, 变量)
print(sys.path)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 这个是父级的父级路径
import _1module

'''
如果存在重复调用导入方法的情况下，最好使用from 模块名 import 方法名    来进行导入，这样就少了重复检索的过程
'''
