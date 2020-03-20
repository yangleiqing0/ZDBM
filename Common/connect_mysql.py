import pymysql
from Common.configure import *


class ConnMysql:

    def __init__(self):
        self.db = pymysql.connect(host=IP, port=MYSQL_PORT, user=MYSQL_USERNAME,
                                  passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE, charset='utf8')

    def select_mysql(self, sql, _all=False):
        cur = self.db.cursor()
        cur.execute(sql)
        r = cur.fetchall()
        print("select_mysql select result:", r)
        if _all:
            return r
        if r == ():
            return '查询结果为空',
        return r[0]

    def select_mysql_new(self, sql, one=True, ac_re=False):
        cur = self.db.cursor()
        cur.execute(sql)
        if one:
            r = cur.fetchone()
        else:
            r = cur.fetchall()
        print("select_mysql_new select result:", r)
        if r == ():
            return '查询结果为空',

        if ac_re:
            return r
        return r[0]

    def operate_mysql(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)

    def __del__(self):
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    ConnMysql().select_mysql('select name from zdbm_license_infos where id=1')
