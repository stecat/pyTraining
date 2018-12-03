# Author：Steve

from core import auth
from core import accounts
from core import transaction

# 以下为全局日志模块，可以直接在全局各个方法里面直接写日志
# 用access_log模块直接把文件打开，之后只需要append就可以了，不需要重复打开文件效率比较高一些
# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')

# temp account data, only saving the data in memeory
# 全局字典，可以用于用户登录成功后各接口认证用户是否登录
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def pay_check(acc_data):
    pass

def logout(acc_data):
    pass

def interactive(acc_data):
    '''
    interact with user
    :param acc_data:
    :return:
    '''
    menu=u'''
    -----------bank----------
    \033[32;1m1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单
    6. 退出
    
    '''
    menu_dic = {
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':pay_check,
        '6':logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # menu_dic里直接写了对应func，比如输入6，对应的是logout方法
            menu_dic[user_option](acc_data)
        else
            print("\033[31:1mOption does not exist!\033[0m")
def run():
    '''
    this func is the gate for the program when started

    :return:
    '''

    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data']=acc_data
        interactive(user_data)   #交互


def repay(acc_data):
    '''
    print current balance and make user repay the bill
    :param acc_data:
    :return:
    '''

    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance='''------------balance info--------------
    Credit:   %s
    Balance:  %s
    '''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
            #print('ddd 00')
            new_balance=transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew balance:%s\033[0m''' %(new_balance['balance']))
        else:
            print("\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m"%repay_amount)
        if repay_amount == 'b':
            back_flag =True


def account_info(acc_data):
    print(user_data)

def withdraw(acc_data):
    '''
    print current balance and execute the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''-----------balance info------------
    Credit:      %s
    Balance:     %s'''%(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag=False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInupt withdraw amount:\033[0m").strip()
        if len(withdraw_amount)>0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew balance:%s\033[0m''' % (new_balance['balance']))

            else:
                print("\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m" % withdraw_amount)
            if withdraw_amount=='b':
                back_flag=True

def transfer(acc_data):
    pass


