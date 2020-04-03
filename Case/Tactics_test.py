# encoding=utf-8
import random
from Common.configure import *
from Common.connect_mysql import ConnMysql
from Common.utils import get_now


class TacticsTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        if self.params:
            self.request_method = self.params['request_method']
            self.mysql = ConnMysql()

    def pre_clear_data(self):
        # 预处理数据成过期
        self.expire_data()
        self.expire_snapshot()
        self.expire_vdb_snapshot()
        self.expire_vdb()

    def expire_data(self):
        source_id = NEED_PARAMETER["increment_source_id"]
        sql = "select id from zdbm_orcl_source_db_archives where source_id={} limit 2".format(source_id)
        mdb_archive_expire, source_archive_expire = self.mysql.select_mysql_new(sql, one=False, ac_re=True)
        print(mdb_archive_expire, source_archive_expire)
        mdb_archive_expire_id = mdb_archive_expire[0]
        source_archive_expire_id = source_archive_expire[0]
        NEED_PARAMETER["mdb_archive_expire_id"] = mdb_archive_expire_id
        NEED_PARAMETER["source_archive_expire_id"] = source_archive_expire_id
        source_expire_sql = "UPDATE zdbm_orcl_source_db_archives  set next_time = DATE_SUB(" \
                            "next_time, INTERVAL 31 day ) where id={}".format(
                             source_archive_expire_id)
        mdb_expire_sql = "UPDATE zdbm_orcl_source_db_archives  set next_time = DATE_SUB(" \
                         "next_time, INTERVAL 61 day ) where id={}".format(
                            mdb_archive_expire_id)
        self.mysql.operate_mysql(source_expire_sql)
        self.mysql.operate_mysql(mdb_expire_sql)

    def expire_snapshot(self):
        source_id = NEED_PARAMETER["increment_source_id"]
        sql = 'select id from zdbm_orcl_source_db_snapshots where source_id = {} limit 1'.format(source_id)
        snapshot_expire_id = self.mysql.select_mysql_new(sql)
        NEED_PARAMETER["source_snapshot_expire_id"] = snapshot_expire_id
        print(snapshot_expire_id)
        snapshot_expire_sql = 'UPDATE zdbm_orcl_source_db_snapshots set snapshot_time = DATE_SUB(' \
                              'snapshot_time, INTERVAL 61 day ) where id = {}'.format(snapshot_expire_id)
        self.mysql.operate_mysql(snapshot_expire_sql)

    def expire_vdb_snapshot(self):
        now = get_now()
        source_id = NEED_PARAMETER["increment_source_id"]
        sql = "select id from zdbm_orcl_virtual_dbs where deleted_at is null " \
              "and vdb_status='RUNNING' limit 2".format(source_id)
        vdb, expire_vdb = self.mysql.select_mysql_new(sql, one=False, ac_re=True)
        vdb_snapshot_expire_id = random.randint(10000, 90000)
        NEED_PARAMETER["vdb_expire_id"] = expire_vdb[0]
        NEED_PARAMETER["vdb_snapshot_expire_id"] = vdb_snapshot_expire_id
        select_sql = " select created_at, updated_at, source_id, virtual_id, snapshot_id, " \
                      "name, description, target_time, parameters from zdbm_orcl_virtual_parameter_snaps where id =" \
                     "(select id from zdbm_orcl_virtual_parameter_snaps where virtual_id = {} limit 1)".format(vdb[0])
        sn = list(self.mysql.select_mysql_new(select_sql, ac_re=True))
        sn[0] = sn[1] = sn[7] = now
        sn[4] = sn[4] -1
        sn.insert(0, vdb_snapshot_expire_id)
        vdb_expire_snapshot_sql = "insert into zdbm_orcl_virtual_parameter_snaps values {}".format(tuple(sn))
        update_sql = "update zdbm_orcl_virtual_parameter_snaps set created_at=DATE_SUB(created_at, INTERVAL 61 day ) " \
                     "where id={}".format(vdb_snapshot_expire_id)
        print(vdb, expire_vdb, vdb_snapshot_expire_id)
        self.mysql.operate_mysql(vdb_expire_snapshot_sql)
        self.mysql.operate_mysql(update_sql)

    def expire_vdb(self):
        sql = 'update zdbm_orcl_virtual_dbs set created_at=DATE_SUB(created_at, INTERVAL 61 day ) ' \
              'where id ={}'.format(NEED_PARAMETER["vdb_expire_id"])
        self.mysql.operate_mysql(sql)




if __name__ == '__main__':
    a = TacticsTest({"request_method": "put"})
    a.expire_vdb_snapshot()
    a.expire_vdb()
