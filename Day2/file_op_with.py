# Author：Steve

# with语句，打开文件会自行关闭
with open("yesterday2", "r", encoding="utf-8") as f:
    print(f.readline())
    for line in f:
        print(line)

print(f.closed)

# with打开多个文件：
with open("yesterday2", "r", encoding="utf-8") as f3,\
open("yesterday3", "r", encoding="utf-8") as f4:        # 分行记得用 ",\"
    print(f3.readline())
    print(f4.readline())

print(f3.closed)
print(f4.closed)
