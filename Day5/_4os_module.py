# Author：Steve

# os模块：提供对操作系统进行调用的接口
import os
import time

print(os.getcwd())  # 获取当前目录，相当于pwd

os.chdir("/Users/jiruitong/wsh/PyProject/PyTraining")  # 更改当前路径
os.chdir(r"/Users/jiruitong/wsh/PyProject/PyTraining")  # 加r的方式
print(os.getcwd())

print(os.curdir)  # 返回当前目录， .代表当面目录
print(os.pardir)  # 返回上级目录， ..代表上级目录

# 递归地创建目录
os.makedirs(r"/Users/jiruitong/wsh/PyProject/PyTraining/mkdir/mkdirTest")
# 清理空文件夹，递归到上一级目录，如为空则删除以此类推
os.removedirs(r"/Users/jiruitong/wsh/PyProject/PyTraining/mkdir/mkdirTest")
# 生成单目录
# os.mkdir(r"/Users/jiruitong/wsh/PyProject/PyTraining/mkdir/mkdirTest")这样会报错，因为目前pytraining下面没有mkdir这个目录
os.mkdir(r"/Users/jiruitong/wsh/PyProject/PyTraining/mkdir")
# 删除单目录
os.rmdir(r"/Users/jiruitong/wsh/PyProject/PyTraining/mkdir")

# 列出当前目录
print(os.listdir('.'))  # 列出当前目录下的文件夹
print(os.listdir('..'))  # 列出父级目录下的文件夹

# 删除一个文件  os.remove()

# 重命名文件 os.rename("oldname","newname")

# 获取文件信息
print(os.stat(r'快捷键'))

# 输出操作系统指定的路径分隔符
print(os.sep)
# 输出操作系统使用的行终止符
print(os.linesep)
# 输出用于分割文件路径的字符串
print(os.pathsep)
# 输出当前环境变量， {key：value}形式, 所以os.pathsep查看的是：，以区分不同路径
print(os.environ)

# 输出字符串指示当前使用平台
print(os.name)

# 可以直接执行当前系统命令
os.system('ls')

# os.path
# 获取当前文件绝对路径os.path.abspath(path)
print(os.path.abspath('1'))
print(os.path.abspath('./'))
print(os.path.abspath(__file__))

# 将path分割成目录和文件名的二元组形式，不考虑路径是否存在
print(os.path.split(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))

# 返回path目录，其实就是os.path.split(）第一个元素，不考虑路径是否存在
print(os.path.dirname(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))

# 返回path最后的文件名，其实就是os.path.split(）第二个元素，如果以path以/结尾那就会返回空格，不考虑路径是否存在
print(os.path.basename(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))

# 判断path是否存在， 存在返回true，不存在返回false
print(os.path.exists(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5'))

# 判断是否是绝对路径，linux上以/开头就是绝对路径
print(os.path.isabs(r'../jiruitong/wsh/PyProject/PyTraining/Day5'))

# 判断path是否是一个存在的文件
print(os.path.isfile(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))

# 判断是否是一个存在的目录
print(os.path.isdir(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5'))

# 组合多个路径组合返回,第一个绝对路径之前的参数将被忽略-->即/Day6之前的绝对路径被忽略了
print(os.path.join('/Users/jiruitong/wsh/PyProject/PyTraining/Day5', '/Day6', '../1', '2'))

# 返回path所指向文件或目录 最后的存取时间
print(os.path.getatime(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))
print(time.ctime(os.path.getatime(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py')))

# 返回最后修改时间
print(os.path.getmtime(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py'))
print(time.ctime(os.path.getmtime(r'/Users/jiruitong/wsh/PyProject/PyTraining/Day5/_4os_module.py')))