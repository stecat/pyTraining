# Author：Steve
# 简单的学校管理
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("新员工%s注册" % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        def tell(self):  # 学生和老师的信息不同，所以不能直接用
            pass


# Teacher无法直接继承School，因为属于不同的东西，所以想到弄一个schoolmembers类
class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        -----info of Teacher %s-----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        -----info of Student %s-----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tuition for $%s" % (self.name, amount))


# 实例一个学校，几个老师，几个学生，然后关联学生，老师，学校
school = School("ZJU", "ZJ")
t1 = Teacher("Ivan", 25, "m", 100000000, "writing")
t2 = Teacher("Cat", 10, "m", 50, "python")

s1 = Student("steve", 28, "m", 1001, "python")
s2 = Student("boss", 10, "m", 1002, "writing")

t1.tell()
s1.tell()
school.enroll(s1)
school.hire(t1)

print(school.students)
print(school.staffs)

school.staffs[0].teach()  # 老师教课

# 学生缴费
for stu in school.students:
    stu.pay_tuition(500)
