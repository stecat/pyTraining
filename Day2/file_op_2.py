# Author：Steve

# 读写文件用迭代器，效率高，每次读一行内存存一行，读完后内存删除
f = open("yesterday")
count = 0
for line in f:      # f此时变成了迭代器，此时就没有下标了，需要自己添加计数器
    if count == 9:
        print("-------第10行分割线——————————")
        count += 1      # 如果count +=1不写这边会一直打印上句，因为到9时就一直在if判断里面continue
        continue
    count += 1        # 这边也要有对应加的计数器
    print("%s:" % count, line)
f.close()