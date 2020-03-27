import time
from Common.configure import *
import cx_Oracle  # 引用模块cx_Oracle


class ConnOracle:

    def __init__(self, user=MDB1_ORACLE_USER, pwd=MDB1_ORACLE_PASSWORD, ip=MDB1_IP, port=MDB1_ORACLE_PORT, oracle_name="", mode=None):
        to = ip+':'+port+'/'+oracle_name
        self.to = to
        print('要连接的路径:', to, '用户:', user, '密码: ', pwd, "mode:", mode)
        if mode is None:
            self.conn = cx_Oracle.connect(user, pwd, to)  # 连接数据库
        else:
            self.conn = cx_Oracle.connect(user, pwd, to, mode)  # 连接数据库
        self.c = self.conn.cursor()  # 获取cursor

    def init_system(self):
        self.conn = cx_Oracle.connect("system", "root1234", self.to)
        self.c = self.conn.cursor()

    def selcet_oracle(self, sql):
        print('要查询的语句为: ', sql)
        self.c.execute(sql)  # 使用cursor进行各种操作
        r = self.c.fetchall()
        print('数据库获取到的: ', r[0])
        if r == []:
            print("最后输出的: ", r[0])
            return '查询结果为空',
        print("最后输出的: ", r[0])
        return r[0]

    def operate_oracle(self, sql):
        print('要执行的sql语句为 : ', sql)
        self.c.execute(sql)
        self.conn.commit()

    def exeute_oracle(self, sql):
        print('要执行的sql语句为 : ', sql)
        self.c.execute(sql)

    def init_operate(self):
        self.init_system()
        sql = "grant create table,drop any table to zdbm"
        sql2 = "grant unlimited tablespace to zdbm"
        self.operate_oracle(sql)
        self.operate_oracle(sql2)

    def switch_archive(self):
        self.init_system()
        sql = "alter system archive log current"
        self.operate_oracle(sql)

    def new_table(self):
        sql = """declare
      num   number;
begin
    select count(1) into num from user_tables where table_name = upper('dept') ;
    if num > 0 then
        execute immediate 'drop table DEPT' ;
    end if;
end;"""
        sql1 = 'create table DEPT(id number(10),content varchar(20))'
        self.operate_oracle(sql)
        self.operate_oracle(sql1)
        timestamp = str(time.strftime("%Y.%m.%d %H.%M.%S")).replace(' ', '.').replace('.','')
        print(timestamp)
        sql2 = "insert into DEPT values(1,'%s')" % timestamp
        self.operate_oracle(sql2)

    def insert_dept(self):
        sql = """declare
              num   number;
        begin
            select count(1) into num from user_tables where table_name = upper('dept') ;
            if num = 0 then
                execute immediate 'create table DEPT(id number(10),content varchar(20))' ;
            end if;
        end;"""
        self.operate_oracle(sql)
        timestamp = str(time.strftime("%Y.%m.%d %H.%M.%S")).replace(' ', '.').replace('.', '')
        print(timestamp)
        sql2 = "insert into DEPT values(2,'%s')" % timestamp
        self.operate_oracle(sql2)

    def __del__(self):
        try:
            self.c.close()
            self.conn.close()  # 关闭连接
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # ConnOracle(oracle_name='vdb_D6QJ').new_table()
    ConnOracle(ip='192.168.12.1', user='system', pwd='system', oracle_name='auto', mode=True).switch_archive()
    # ConnOracle(oracle_name='vdb_D6QJ').selcet_oracle('select content from DEPT')