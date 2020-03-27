# encoding=utf-8
import requests
import random
import time
from Common.Request_method import RequestMethod
from Common.connect_mysql import ConnMysql
from Common import get_now
from Common.configure import *

requests.packages.urllib3.disable_warnings()


class ArchiveTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_scan_archive(self):
        select_archive_sql = "select * from zdbm_orcl_source_db_archives order by sequence desc limit 1"
        archive = ConnMysql().select_mysql_new(select_archive_sql, ac_re=True)
        source_id, sequence = archive[4], archive[10]
        print(archive)
        archive = list(archive)
        now = get_now()
        _id = random.randint(10000, 99999)
        archive[0] = _id
        archive[1] = archive[2] = archive[12] = archive[13] = archive[25] = archive[26] = archive[27] = \
            archive[28] = archive[29] = archive[30] = now
        archive[10] += 2
        insert_sql = "insert into zdbm_orcl_source_db_archives values {}".format(tuple(archive))
        ConnMysql().operate_mysql(insert_sql)
        select_count_sql = "select count(*) from zdbm_orcl_source_db_archives where source_id={}".format(source_id)
        old_value = ConnMysql().select_mysql_new(select_count_sql)
        content = RequestMethod().to_requests(self.request_method, "source/archive/scan/{}".format(source_id))
        time.sleep(5)
        print(old_value, content)
        new_value = ConnMysql().select_mysql_new(select_count_sql)
        print(new_value)
        del_sql = "delete from zdbm_orcl_source_db_archives where id in ({},{})".format(_id, _id+1)
        ConnMysql().operate_mysql(del_sql)
        return {
            'actualresult': content, 'old_database_value': 'mysql_value: {}'.format(old_value),
            'new_database_value': 'mysql_value:{}'.format(new_value), 'database_assert_method': False
        }


if __name__ == '__main__':
    ArchiveTest({"request_method": "post"}).test_scan_archive()