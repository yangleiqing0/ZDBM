from Common.connect_mysql import ConnMysql
from Common.configure import *


class ClearEnv:

    def __init__(self):
        pass

    @staticmethod
    def clear_cell_mysql():
        delete_sql = 'delete from zdbm_cells'
        delete_zdbm_cell_services = 'delete from zdbm_cell_services'
        delete_zdbm_cell_network_cards = 'delete from zdbm_cell_network_cards'
        ConnMysql().operate_mysql(delete_sql)
        ConnMysql().operate_mysql(delete_zdbm_cell_services)
        ConnMysql().operate_mysql(delete_zdbm_cell_network_cards)

    @staticmethod
    def delete_exists_mysql(table_name, col_name, exsits_name):
        query_sql = 'select * from %s where %s="%s"' % (table_name, col_name, exsits_name)
        r = ConnMysql().select_mysql(query_sql)
        if r[0] == ' ':
            print('%s表 不存在 %s' % (table_name, exsits_name))

        else:
            delete_sql = 'delete from %s where %s="%s"' % (table_name, col_name, exsits_name)
            ConnMysql().operate_mysql(delete_sql)
            print('%s表 删除 %s' % (table_name, exsits_name))

    @staticmethod
    def update_user_password():
        update_sql = 'update zdbm_users set password="%s" where username="%s"' % (SCR_PASSWORD, USERNAME)
        ConnMysql().operate_mysql(update_sql)

    @staticmethod
    def update_user_enable():
        update_sql = 'update zdbm_users set enable=1 where username="%s"' % USERNAME
        ConnMysql().operate_mysql(update_sql)

if __name__ == '__main__':
    ClearEnv().delete_exists_mysql("zdbm_users", "username", "yangleiqing")