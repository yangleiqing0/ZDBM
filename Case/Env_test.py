import json
import time
import datetime
from Common.Request_method import RequestMethod
from Common.connect_mysql import ConnMysql
from Common.configure import *
from Common.CLEARE_ENV import ClearEnv as Ce
from utils import wait_for
from Case.DeleteMySql import DeleteWords


class EnvTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']
        self.mysql = ConnMysql()

    def test_env_test(self):
        # 测试目标主机连通性
        # Ce(IP).login()
        data = """
        {
        "ip":"%s",
        "port":%s,
        "username":"%s",
        "password":"%s",
        "envName":"%s"
        }
        """ % (
            self.params['ip'], self.params['port'],
            self.params['username'], self.params['password'], self.params['envName']
               )
        if 'clusterHome' in self.params:
            data = """
            {"ip":"%s",
            "port":%s,
            "username":"%s",
            "password":"%s",
            "envName":"%s",
            "clusterHome":"%s"
            }
            """ % (
             self.params['ip'], self.params['port'], self.params['username'],
             self.params['password'], self.params['envName'],self.params['clusterHome']
               )
        content = RequestMethod().to_requests(self.request_method, 'env/test', data=data)
        print(content)
        return {
            'actualresult': content
        }

    def test_env_get(self):
        # 获取环境详细信息
        env_id_sql = 'select id from zdbm_orcl_envs where '
        content = RequestMethod().to_requests(self.request_method, 'env/get/%s')
        print(content)
        return {
            'actualresult': content
        }

    def test_env_add(self):
        # 添加环境
        hostType = "物理机".encode('utf-8').decode('latin1')
        data = None
        if self.params['envType'] == 'SOURCE':
            data = '{"envName": "%s","envType": "%s","ip": "%s","port": %s,"username": "%s","password": "%s",' \
                   '"toolPath": "%s","hostType": "%s/Vmware/KVM", "useSsh": true}' % \
                   (
                     self.params['envName'], self.params['envType'],
                     self.params['ip'], self.params['port'],
                     self.params['username'], self.params['password'], self.params['toolPath'], hostType
                   )
            if 'clusterHome' in self.params:
                data = """
                {
                "useSsh": true,
                "envName":"%s",
                "clusterHome":"%s",
                "ip":"%s",
                "port":%s,
                "envType":"%s",
                "username":"%s",
                "password":"%s",
                "toolPath":"%s",
                "hostType":"%s/Vmware/KVM"}
                """ % \
                   (
                     self.params['envName'], self.params['clusterHome'],
                     self.params['ip'], self.params['port'],self.params['envType'],
                     self.params['username'], self.params['password'], self.params['toolPath'], hostType
                   )
        elif self.params['envType'] == 'TARGET':
            data = """
            {
                "envName": "%s",
                "hostType": "%s/Vmware/KVM",
                "ip": "%s",
                "port": %s,
                "envType": "%s",
                "username": "%s",
                "password": "%s",
                "toolPath": "%s",
                "asMdb": %s,
                "useSsh": true
            }
            """ % \
                   (
                     self.params['envName'],  hostType,
                     self.params['ip'], self.params['port'],self.params['envType'],
                     self.params['username'], self.params['password'], self.params['toolPath'],
                     self.params['asMdb']
                   )
        query_env_id_sql = 'select id from zdbm_orcl_envs where env_name="%s" and isnull(deleted_at)' % self.params['envName']
        old_database_value = self.mysql.select_mysql(query_env_id_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'env/add', data=data)
        result = json.loads(content)
        print('ENV ADD result is :', result)
        try:
            print(result['data']['env'])
        except Exception as e:
            print("清理环境报错: ", e)
            # DeleteWords().select_tables()
            old_database_value = self.mysql.select_mysql(query_env_id_sql)[0]
            content = RequestMethod().to_requests(self.request_method, 'env/add', data=data)
            result = json.loads(content)
            print(result['data']['env'])
        if 'm' not in self.params['envName']:
            software_id = result['data']['env']['softwares'][0]['id']
            NEED_PARAMETER.update({
                               self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                               self.params['envName'] + '_id': result['data']['env']['id'],
                               self.params['envName'] + '_softwares_id': software_id
                               })
            dbs_sql = 'select db_name, id from zdbm_orcl_env_databases where software_id={}'.format(software_id)
            dbs = self.mysql.select_mysql_new(dbs_sql, one=False, ac_re=True)
            for db in dbs:
                if db:
                    db_name, db_id = db
                    NEED_PARAMETER.update(
                            {self.params['envName'] + '_' + db_name + '_database_id': db_id}
                        )
            # for l in range(len(result['data']['env']['softwares'][0]['database'])):
            #     NEED_PARAMETER.update(
            #         {self.params['envName'] + '_' + result['data']['env']['softwares'][0]['database'][l]['dbName'] +
            #          '_database_id': result['data']['env']['softwares'][0]['database'][l]['id']}
            #     )
        else:
            NEED_PARAMETER.update(
                {
                 self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                 self.params['envName'] + '_id': result['data']['env']['id'],
                 self.params['envName'] + '_softwares_id': result['data']['env']['softwares'][0]['id'],

                 })
        print(NEED_PARAMETER)
        new_database_value = self.mysql.select_mysql(query_env_id_sql)[0]
        print(old_database_value, type(old_database_value))
        return {
            'actualresult': content, 'old_database_value': 'id:' + old_database_value,
            'new_database_value': 'id:' + str(new_database_value), 'database_assert_method': False
        }

    def test_env_database_add(self):
        # 添加数据库信息
        node, all_online = Ce(IP).listen_nodes_online()
        if all_online is False:
            content = " {} 节点 一直不在线".format(node)
            return {
                'actualresult': content
            }
        data = """
{"databaseID":%s,
"username":"%s",
"password":"%s",
"archiveZpoolID":1,
"datafileZpoolID":2,
"parallels":[{"nodeID":%s,"parallel":4}],
"tacticID":2,
"mdbEnvID":%s,
"mdbSoftwareID":%s}
        """ % (NEED_PARAMETER[self.params['envName'] + '_' + self.params['dbName']+'_database_id'], self.params['ORACLE_USER'], self.params['ORACLE_PASSWORD'],
               NEED_PARAMETER[self.params['envName'] + '_node_id'],
               NEED_PARAMETER[self.params['MDB_NAME'] + '_id'], NEED_PARAMETER[self.params['MDB_NAME'] + '_softwares_id'],
               )

        content = RequestMethod().to_requests(self.request_method, 'source/add', data=data)
        result = json.loads(content)
        print("result = ", result)
        NEED_PARAMETER.update({
            self.params['envName'] + '_' + self.params['dbName'] + '_source_id': result['data']['source']['id']

        })
        sql = 'select job_status from zdbm_jobs where env_id=%s order by id desc limit 1' % (NEED_PARAMETER[self.params['envName'] + '_id'])
        content_sql = 'select err_msg from zdbm_jobs where env_id="%s" order by id desc limit 1' % (NEED_PARAMETER[self.params['envName'] + '_id'])
        print(sql, content_sql)
        archive_time = 10 * 60 # 5分钟
        times = 10*60
        status_sql = 'select count(*) from zdbm_orcl_source_db_snapshots where source_id="%s"' % (NEED_PARAMETER[self.params['envName'] + '_' + self.params['dbName'] + '_source_id'])
        time.sleep(2)
        while 1:
            try:
                result = self.mysql.select_mysql(sql)[0]
            except AttributeError as e:
                result = self.mysql.select_mysql(sql)[0]
            print("添加源库状态：", result, '时间过去：', 600-archive_time, '秒')
            archive_time -= 2
            if result == 'PROCESSING':
                time.sleep(2)
                continue
            elif result == 'FAILURE':
                content = self.mysql.select_mysql(content_sql)[0]
                break
            elif result == 'SUCCESS':
                time.sleep(2)
                while times > 0:
                    status = self.mysql.select_mysql(status_sql)[0]
                    print("归档状态：", status, '时间过去：', 600-times, '秒')
                    if status == 1:
                        break
                    times -= 2
                    time.sleep(2)
                break

            if archive_time == 0:
                content = '归档状态异常，5分钟未恢复'
                break

        return {
            'actualresult': content
        }

    def test_env_refresh(self):
        env_id = self.del_env_soft()
        content = RequestMethod().to_requests(self.request_method, 'env/fresh/{}'.format(env_id))
        print(content)
        #
        sql = "select software_count from zdbm_orcl_envs where id={}".format(env_id)
        time.sleep(2)
        new_database_value = self.mysql.select_mysql(sql)[0]
        # print(new_database_value)
        sql1 = 'delete from zdbm_orcl_env_softwares where env_id={} and deleted_at is null'.format(env_id)
        sql2 = 'update zdbm_orcl_env_softwares set deleted_at =null where env_id={}'.format(env_id)
        self.mysql.operate_mysql(sql1)
        self.mysql.operate_mysql(sql2)
        return {
            'actualresult': content, 'old_database_value': 'mysql_value:' + str(0),
            'new_database_value': 'mysql_value:' + str(new_database_value), 'database_assert_method': False
        }

    def del_env_soft(self):
        select_sql = "select id, env_name from zdbm_orcl_envs where deleted_at is null"
        env_id, env_name = self.mysql.select_mysql(select_sql, True)[-1]
        del_sql = "update zdbm_orcl_env_softwares set deleted_at='2020-03-18 17:28:50' where env_id={}".format(env_id)
        update_count_sql = "update zdbm_orcl_envs set software_count=0 where id='{}'".format(env_id)
        self.mysql.operate_mysql(del_sql)
        self.mysql.operate_mysql(update_count_sql)
        return env_id

    def test_env_clear(self):
        Ce(IP).login()
        return {'actualresult': 0}


if __name__ == '__main__':
    EnvTest({"request_method": "put"}).test_env_refresh()
