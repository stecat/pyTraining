# Author：Steve
# 静态属性的应用  调用航班信息
class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        # 这边是写的调用查航班状态接口的伪代码
        print("checking flight %s status" % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()  # 去调给出的checking_status接口
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arriving...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...please check")


f = Flight("CA980")
f.flight_status


# 如果有改状态的需求则可以采用如下方法：
class Flight2(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        # 这边是写的调用查航班状态接口的伪代码
        print("checking flight %s status" % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()  # 去调给出的checking_status接口
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arriving...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...please check")

    @flight_status.setter  # 可以传参直接改status
    def flight_status(self, status):
        print("flight %s has been changed status to %s" % (self.flight_name, status))


f2 = Flight2("CA980")
f2.flight_status
f2.flight_status = 2
f2.flight_status
