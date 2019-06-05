import pymysql
from ZDBM.Common.configure import *


class ConnMysql:

    def __init__(self):
        self.db = pymysql.connect(host=IP, port=MYSQL_PORT, user=MYSQL_USERNAME,
                                  passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE, charset='utf8')

    def select_mysql(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)
        r = cur.fetchall()
        if r == ():
            return '查询结果为空',
        return r[0]

    def operate_mysql(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)

    def __del__(self):
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    ConnMysql().select_mysql('select name from zdbm_license_infos where id=1')
