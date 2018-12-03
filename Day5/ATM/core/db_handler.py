# Author：Steve

def file_db_handle(conn_parms):
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    print('file db:',conn_parms)
    db_path='%s%s' %(conn_parms['path'],conn_parms['name'])
    return db_path

def mysql_db_handle(conn_parms):
    pass


def db_handler(conn_parms):
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return: a
    '''

    if conn_parms['engine'] == 'file_storage':     # 这部分就是解耦的过程，以便以后增加mysql的db
        return file_db_handle(conn_parms)

    if conn_parms['engine'] == 'mysql':
        return mysql_db_handle(conn_parms)