# encoding=utf-8

from pymysql import *


class ConnectMysql(object):
    def __init__(self, host, port, user, password, database):
        self.conn = connect(host=host, port=port, user=user, password=password, database=database, charset='utf8')
        # 得Cursor对象
        self.cs = self.conn.cursor()
        # 设置事务自动提交
        self.conn.autocommit(True)
