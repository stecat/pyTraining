# Author：Steve
# vim是把文件全部加载到内存里，所以大文件用vim打开就要好久，不过还有另外一种方式，就是重新创建一个一样的文件进行更改

f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday_new", "w", encoding="utf-8")

for line in f:
    if "狂野的乐趣" in line:
        line = line.replace("狂野的乐趣等待我去享用", "lalallalalla")
        f_new.write(line)
    else:
        f_new.write(line)

f.close()
f_new.close()
