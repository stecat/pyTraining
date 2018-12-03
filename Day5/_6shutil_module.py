# Author：Steve


# shutil 模块:高级的文件，文件夹，压缩包处理模块

import shutil

f1 = open("shutil模块")
f2 = open("copy_shutil模块", 'w', encoding='gbk')

# shutil.copyfileobj(f1,f2)方法
shutil.copyfileobj(f1, f2)

# shutil.copy("现有模块名","希望copy的模块名"):拷贝文件和权限， 直接省去了你自己去写打开文件的部分
shutil.copy("shutil模块", "shutil模块copy1")

# shutil.copy2(): 拷贝文件和状态信息

# shutil.copymode() 仅copy权限。内容，组，用户均不变

# shutil.copystat(src, dst) 拷贝状态信息，包括：mode bits, atime, mtime, flags

# shutil.copytree(原目录，目标目录):递归拷贝文件
shutil.copytree("ATM", "new_copyATM")
shutil.rmtree("new_copyATM")

# shutil.move(src,dst) 递归的去移除文件

# shutil.make_archive(base_name,format...)
'''
base_name:压缩文件名，也可是压缩包路径(/users/python/t.txt)
format: 压缩包种类zip,tar,bztar,gztar
root_dir:要压缩的文件夹路径（默认当前目录）
owner:用户，默认当前用户
group：组，默认当前组
logger：用于记录日志，通常是logging.Logger对象
'''
# 放到当前目录
# ret=shutil.make_archive("copy_shutil模块",'gztar',root_dir='/Users/jiruitong/wsh/PyProject/PyTraining/Day5/')
# 放到指定目录
# ret=shutil.make_archive("/Users/jiruitong/wsh/PyProject/PyTraining/Day5/copy_shutil模块",'gztar',root_dir='/Users/jiruitong/wsh/PyProject/PyTraining/Day5/')

'''
shutil对压缩包的处理是调用zipFile和TarFile两个模块来进行的

import zipfile

# 压缩
z = zipfile.ZipFile('压缩.zip', 'w')
z.write('copy_shutil模块')  # 要进行压缩的文件名
z.write('shutil模块')
z.close()

# 解压
z = zipfile.ZipFile('压缩.zip', 'r')
z.extractall()
z.close()
'''

'''
import tarfile

# 压缩
tar = tarfile.open('压缩.tar', 'w')
tar.add('/Users/jiruitong/wsh/PyProject/PyTraining/Day5/copy_shutil模块', arcname='copy_shutil.zip')
tar.close()

# 解压
tar = tarfile.open('压缩.tar', 'r')
tar.extractall()  # 可设置压缩地址
tar.close()
'''