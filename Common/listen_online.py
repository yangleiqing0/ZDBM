import time
from Common.connect_mysql import ConnMysql


class ListenOnLine:

    def __init__(self):
        pass

    @staticmethod
    def listen_nodes_online(node_name, times=2):
        min_time = times * 60
        is_online = False
        select_sql = 'select is_online from zdbm_orcl_env_nodes where node_name="%s"' % node_name
        while min_time > 0 or is_online is True:
            is_online = ConnMysql().select_mysql(select_sql)
            time.sleep(2)
            min_time = min_time - 2
        return is_online
