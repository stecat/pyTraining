# Author：Steve
# 简单的学校管理
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teacher = []

    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        def tell(self):  # 学生和老师的信息不同，所以不能直接用
            pass


# Teacher无法直接继承School，因为属于不同的东西，所以想到弄一个schoolmembers类
class Teacher(SchoolMember):

