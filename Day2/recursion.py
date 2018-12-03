# Author：Steve
# 递归recursion, 最大递归次数是999
# 递归特性：1.必须有结束条件； 2.问题规模比上一次递归有所减少；3.递归效率不高，会导致栈溢出，每进一层栈就加一层栈桢，每当返回就会减一层栈桢


def recursion(n):
    print(n)
    if int(n/2) > 0:   # int可以直接取整
        return recursion(int(n/2))
    print('-->',n)

recursion(10)
