from random import choice

import pymysql

class  MySql(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root', passwd='11142000lg', database='proxytest', charset='utf8')
        self.cur=self.conn.cursor()

    def getip(self):
        # 随机选一个
        sql = "SELECT * FROM PROXY "
        if self.cur.execute(sql):
            results = self.cur.fetchall()
            # 随机化results
            return choice(results)
        else:
            print('ip获取失败')
            return ''

    def disconnect(self):
        self.conn.close()
        self.cur.close()