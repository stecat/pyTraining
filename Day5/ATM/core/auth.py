# Author：Steve

import json
# 程序的解耦：独立拆分对应的功能，因为可能很多地方需要调用
import os
import time

from conf import settings
from core import db_handler


def acc_auth(account, password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication, return the account obj, other?
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() > exp_time_stamp
                    print("\033[31;1mAccount [%s] has expired, fail to login\033[0m" % account)
                else:  # passed the authentication
                    return account_data
            else:
                print("\033[31;1mAccount or password is incorrect!, fail to login\033[0m")
    else:
        print("\033[31:1mAccount [%s] does not exist!\033[0m" % account)


def acc_login(user_data, log_obj):
    '''
    account login func
    :param user_data: user info data, only saving in memory
    :param log_obj:
    :return:
    '''

    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password)

        if auth:  # not None means passed the authentication,因为用户验证错误的时候是没有返回值的，有返回说明验证成功
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            # print('welcome')
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()
