# Author：Steve

import time

#装饰器用法： 举例--》实现用户验证登录
# user, pwd = 'ste', '123'
# def auth(func):
#     def wrapper(*args, **kwargs):
#         username = input("username:").strip()
#         pwd = input("pwd:").strip()
#
#         if username == user and pwd == pwd:
#             print("User has passed authentication...")
#             func(*args,**kwargs)
#         else:
#             exit("Invalid username or pwd")
#     return wrapper()
#
#
# def index():
#     print("welcome to the index page...")
#
# @auth
# def home():
#     print("welcome to home page...")
#     return "from home"
#
# @auth
# def bbs():
#     print("welcome to bbs page...")
#
# home()
# print(home)

# 通过装饰器实现不同的登录验证方式：如本地验证和ldap验证
user, pwd = 'ste', '123'
def auth(auth_type):
    print("auth func:", auth_type)
    def ldap_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type=="local":
                username = input("username:").strip()
                pwd = input("pwd:").strip()

                if username == user and pwd == pwd:
                    print("User has passed authentication...")
                    func(*args,**kwargs)
                else:
                    exit("Invalid username or pwd")
            elif auth_type=="ldap":
                print("having no ldap...")
                exit("ldap gets out!")
        return wrapper
    return ldap_wrapper


def index():
    print("welcome to the index page...")

@auth(auth_type="local")    #这句话相当于  home = wrapper()
def home():
    print("welcome to home page...")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page...")

home()
print(home)   #直接调用wrapper

bbs()