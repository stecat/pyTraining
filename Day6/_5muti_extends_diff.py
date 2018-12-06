# Author：Steve

# 多继承的区别

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")


class C(A):
    def __init__(self):
        print("C")


# 继承了B的构造函数__init__(self)后就不会去继承C的了,找到第一个就停下
# 继承的顺序是先走B，如果B有构造函数就执行B的构造函数，如果B没有就找C，再没有再找A
# 这个就是【广度优先】的查找策略，即D->B,C->A, 如果是【深度优先】则是D->B/C->A
# PYTHON3是广度优先，PYTHON2是深度优先的
# python3的新式类(class A(object))和经典类都是按广度优先的,
# python2的经典类(class A:)是按深度优先来继承的，python2的新式类(class A(object):)是按广度优先来继承的，
class D(B, C):
    pass
    # def __init__(self):
    #     print("D")


obj = D()
