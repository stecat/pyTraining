# Author：Steve
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE= {
    'engine': 'file_storage', #support mysql, postgresql in the future,目前是文件形式的
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR  #文件路径
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction':'transactions.log',
    'access':'access.log'
}

TRANSACTION_TYPE={
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}