
from ZDBM.Common.get_license import GetLicense
from ZDBM.Common.configure import *


class InstallOracle:

    def __init__(self):
        pass

    @staticmethod
    def install_oracle():
        GetLicense().linux_command('cd /opt/zdbm/shell && sh mdb_env_setting.sh')
        print('设置中间环境关于ORACLE变量配置结束')
        GetLicense().linux_command('sshpass -p %s scp -P %s -o StrictHostKeychecking=no '
                                   '/soft/%s root@%s:/u01' %
                                   (ROOT_PASSWORD, SSH_PORT,  OR11204_PACKAGE, IP), ip=ZDBM_PACKAGE_IP, port=ZDBM_PACKAGE_PORT,password=ZDBM_PACKAGE_PWD)
        print('将ORACLE打包文件scp到目标服务器结束')
        GetLicense().linux_command('cd /u01 && rm -rf app && tar -xf %s && chown -R oracle:oinstall app && cp /u01/app/oratab /u01/app/oraInst.loc /etc && chown -R oracle:oinstall /etc/oraInst.loc' % OR11204_PACKAGE)
        print('解压%s结束' % OR11204_PACKAGE)
        GetLicense().linux_command('export ORACLE_HOME=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4 &&'
                                   'export PATH=$ORACLE_HOME/bin:$PATH:/usr/sbin && export PATH=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4/bin:/usr/local/bin:/usr/bin &&'
                                   'lsnrctl start', username=ORACLE_USER, password=ORACLE_PWD)
        print('设置ORACLE变量启动监听结束')

# export PATH=$ORACLE_HOME/bin:$PATH:/usr/sbin && export PATH=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4/bin:/usr/local/bin:/usr/bin && export ORACLE_HOME=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4
# export PATH=$ORACLE_HOME/bin:$PATH:/usr/sbin && export PATH=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4/bin:/usr/local/bin:/usr/bin && export ORACLE_HOME=/u01/app/oracle/product/11.2.0.4/dbhome_11.2.0.4




if __name__ == '__main__':
    InstallOracle().install_oracle()