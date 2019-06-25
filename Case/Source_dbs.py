import time
import cx_Oracle
from ZDBM.Common.connect_oracle import ConnOracle
from ZDBM.Common.configure import *
from ZDBM.Case.Env_test import EnvTest
from ZDBM.Common.get_license import GetLicense
from ZDBM.Common.CLEARE_ENV import ClearEnv as Ce
from ZDBM.Common.Request_method import RequestMethod
from ZDBM.Common.Command import *

class SourceDbs:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_source(self):
        # 测试数据库参数
        data = """{"databaseID": %s,"username": "%s", "password": "%s"}""" \
                % (NEED_PARAMETER[self.params['envName'] + '_' + self.params['dbName']+'_database_id'],
                   self.params['ORACLE_USER'],self.params['ORACLE_PASSWORD'])
        content = RequestMethod().to_requests(self.request_method, 'source/test', data=data)
        return {
            'actualresult': content
        }

    def source_archive(self):
        # 源库开启关闭归档
        shutdwn_oracle = 'echo "shutdown immediate\n exit" > /home/oracle/shutdowntest.sql &&source /home/oracle/.bash_profile && export ORACLE_SID=%s' \
                      '&&sqlplus / as sysdba @/home/oracle/shutdowntest.sql ' % self.params['dbName']
        GetLicense().linux_command(com=shutdwn_oracle, ip=self.params['ORACLE_IP'], username=ORACLE_USER, password=ORACLE_PWD)

        startup_oracle = 'echo "startup mount\n exit" > /home/oracle/startuptest.sql &&' \
                         'source /home/oracle/.bash_profile && export ORACLE_SID=%s' \
                         '&&sqlplus / as sysdba @/home/oracle/startuptest.sql ' % self.params['dbName']
        GetLicense().linux_command(com=startup_oracle, ip=self.params['ORACLE_IP'], username=ORACLE_USER,
                                   password=ORACLE_PWD)

        alter_oracle = 'echo "alter database %s;\n exit" > /home/oracle/alteroracletest.sql &&' \
                         'source /home/oracle/.bash_profile && export ORACLE_SID=%s' \
                         '&&sqlplus / as sysdba @/home/oracle/alteroracletest.sql ' % (self.params['archivemode'],self.params['dbName'])
        GetLicense().linux_command(com=alter_oracle, ip=self.params['ORACLE_IP'], username=ORACLE_USER,
                               password=ORACLE_PWD)
        open_oracle = 'echo "alter database open;\n exit" > /home/oracle/opentest.sql &&' \
                       'source /home/oracle/.bash_profile && export ORACLE_SID=%s' \
                       '&&sqlplus / as sysdba @/home/oracle/opentest.sql ' % self.params['dbName']
        GetLicense().linux_command(com=open_oracle, ip=self.params['ORACLE_IP'], username=ORACLE_USER,
                                   password=ORACLE_PWD)
        node, all_online = Ce(IP).listen_nodes_online()
        content = self.test_source()
        if all_online is False:
            content = " {} 节点 一直不在线".format(node)
        return {
            'actualresult': content
        }

    def source_force(self):
        # 开启关闭强制归档状态
        forcelog_oracle = 'echo "alter database %s force logging;\n exit" > /home/oracle/forcelogtest.sql &&' \
                       'source /home/oracle/.bash_profile && export ORACLE_SID=%s' \
                       '&&sqlplus / as sysdba @/home/oracle/forcelogtest.sql ' % (
                       self.params['forcelogmode'], self.params['dbName'])
        GetLicense().linux_command(com=forcelog_oracle, ip=self.params['ORACLE_IP'], username=ORACLE_USER,
                                   password=ORACLE_PWD)
        content = self.test_source()
        return {
            'actualresult': content
        }

    def source_redo(self):
        #
        pass

    def env_lsnrctl(self):
        # 环境的监听启动状态
        Ce().login()
        lsnrctl_status_com = '%s && lsnrctl %s' % (ORACLE_HOME_COMMAND, self.params['lsnrctl_status'])
        GetLicense().linux_command(com=lsnrctl_status_com, ip=self.params['ip'], username=ORACLE_USER,
                                   password=ORACLE_PWD)

        content = EnvTest(params=self.params).test_env_test()['actualresult']
        return {
            'actualresult': content
        }

