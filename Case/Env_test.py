import json
import time
import datetime
from ZDBM.Common.Request_method import RequestMethod
from ZDBM.Common.connect_mysql import ConnMysql
from ZDBM.Common.configure import *
from ZDBM.Common.CLEARE_ENV import ClearEnv as Ce
from ZDBM.Case.DeleteMySql import DeleteWords


class EnvTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

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
                   '"toolPath": "%s","hostType": "%s/Vmware/KVM"}' % \
                   (
                     self.params['envName'], self.params['envType'],
                     self.params['ip'], self.params['port'],
                     self.params['username'], self.params['password'], self.params['toolPath'], hostType
                   )
            if 'clusterHome' in self.params:
                data = """
                {
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
                "asMdb": %s
            }
            """ % \
                   (
                     self.params['envName'],  hostType,
                     self.params['ip'], self.params['port'],self.params['envType'],
                     self.params['username'], self.params['password'], self.params['toolPath'],
                     self.params['asMdb']
                   )
        query_env_id_sql = 'select id from zdbm_orcl_envs where env_name="%s" and isnull(deleted_at)' % self.params['envName']
        old_database_value = ConnMysql().select_mysql(query_env_id_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'env/add', data=data)
        result = json.loads(content)
        print('ENV ADD result is :', result)
        try:
            print(result['data']['env'])
        except Exception as e:
            print("清理环境报错: ", e)
            # DeleteWords().select_tables()
            old_database_value = ConnMysql().select_mysql(query_env_id_sql)[0]
            content = RequestMethod().to_requests(self.request_method, 'env/add', data=data)
            result = json.loads(content)
            print(result['data']['env'])
        if 'm' not in self.params['envName'] :
            NEED_PARAMETER.update({
                               self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                               self.params['envName'] + '_id': result['data']['env']['id'],
                               self.params['envName'] + '_softwares_id': result['data']['env']['softwares'][0]['id']
                               })
            for l in range(len(result['data']['env']['softwares'][0]['database'])):
                NEED_PARAMETER.update(
                    {self.params['envName'] + '_' + result['data']['env']['softwares'][0]['database'][l]['dbName'] +
                     '_database_id': result['data']['env']['softwares'][0]['database'][l]['id']}
                )
        else:
            NEED_PARAMETER.update(
                {
                 self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                 self.params['envName'] + '_id': result['data']['env']['id'],
                 self.params['envName'] + '_softwares_id': result['data']['env']['softwares'][0]['id'],

                 })
        print(NEED_PARAMETER)
        new_database_value = ConnMysql().select_mysql(query_env_id_sql)[0]
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
        status_sql = 'select count(*) from zdbm_orcl_source_db_backups where source_id="%s"' % (NEED_PARAMETER[self.params['envName'] + '_' + self.params['dbName'] + '_source_id'])
        time.sleep(2)
        while 1:
            result = ConnMysql().select_mysql(sql)[0]
            print("添加源库状态：", result, '时间过去：', 600-archive_time, '秒')
            archive_time -= 2
            if result == 'PROCESSING':
                time.sleep(2)
                continue
            elif result == 'FAILURE':
                content = ConnMysql().select_mysql(content_sql)[0]
                break
            elif result == 'SUCCESS':
                time.sleep(2)
                while times > 0:
                    status = ConnMysql().select_mysql(status_sql)[0]
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


if __name__ == '__main__':
    pass
