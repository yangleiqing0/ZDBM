# 所有文件的参数配置
NEED_PARAMETER = {'192.168.12.1_id': '11', '192.168.12.206_id': '6', '192.168.12.211_id': '12', 't12.1_node_id': 70, 't12.1_id': 1180, 't12.1_softwares_id': 92, 't12.1_yang_database_id': 130, 't12.1_auto_database_id': 131, 't12.1_orcl_database_id': 132, 'm12.206_node_id': 71, 'm12.206_id': 1181, 'm12.206_softwares_id': 93, 'm12.211_node_id': 72, 'm12.211_id': 1182, 'm12.211_softwares_id': 94, 't12.1_yang_source_id': 56, 't12.1_auto_source_id': 57, 'increment_source_id': 57, 'vdb_script_name': 'V2QBCH7D8YGB437J.sh', 'vdb_script_file_name': 'test.sh', 't12.1_auto_vdb_id': 5179, 't12.1_yang_vdb_id': 5180, 'vdb_auto_name': 'vdb_y0ou', 'snapshot_auto_id': 33, 'vdb_auto_id': 5179, 'vdb_yang_name': 'vdb_C2ul', 'snapshot_yang_id': 34, 'vdb_yang_id': 5180}


TEST_REPORT_EXCEL_NAME = 'ZDBM_test_report'
TEST_REPORT_TXT_NAME = 'ZDBM_test_result'
TEST_TITLE_NAME = 'ZDBM接口测试'
# 用于分割txt内的内容
# 服务器配置
IP = '192.168.12.206'
PORT = '40010'
GATEWAY = '61.139.2.69'
USERNAME = 'yanglei'
PASSWORD = 'yanglei1'
SSH_PORT = '22'
SERVER_NAME = 'm12.206'
ROOT_NAME = 'root'
ROOT_PASSWORD = 'root1234'
ROOT_PASSWORD_123 = 'root1234'
NEWPASSWORD = 'yanglei2'
SCR_PASSWORD = '$2a$10$YspahrSiuR.w8HShr4mgLOqz604DOGw/zFmRZrlONcJyrLhEYWt1m'
ORACLE_USER = 'oracle'
ORACLE_PWD = ORACLE_USER


O_USER = "oracle"
O_PWD = "oracle"


# 默认存放zdbm.license在80服务器上
ZDBM_LICENSE_COMPANY_IP = '192.168.12.10'

ZDBM_LICENSE_PORT = '22222'
ZDBM_LICENSE_ROOT = 'root'
ZDBM_LICENSE_PASSWORD = 'root1234'
# 个人yanglei账户信息
Y_PHONE = '15155492421'
Y_EMAIL = '253775405@qq.com'

# 个人yangleiqing账户信息
Y_USERNAME = 'yangleiqing'
YL_PHONE = '18200585160'

# ZDBM版本信息
# ZDBM_VERSION = '1.0.12'
# ZDBM_VERSION = '1.0.14'
# ZDBM_VERSION = '2.1.0'
ZDBM_VERSION = '2.1.6'


# 存放zdbm包的地址
ZDBM_PACKAGE_IP = '192.168.12.10'
ZDBM_PACKAGE_PORT = '22222'
ZDBM_PACKAGE_PWD = 'root1234'
# ZDBM_PACKAGE_NAME = '/soft/zdbm/zdbm-package/v1.0.14/zdbm-20190827174700-v1.0.14-rc12.tar.gz'
# ZDBM_PACKAGE_NAME = '/var/lib/jenkins/workspace/Zdbm/zdbm-*.tar.gz'
# ZDBM_PACKAGE_NAME = '/soft/zdbm/zdbm-package/v{}/zdbm*.t'.format(ZDBM_VERSION)
# ZDBM_PACKAGE_NAME = '/var/lib/jenkins/workspace/zdbm_auto_page/zdbm-*.tar.gz'
# ZDBM_PACKAGE_NAME = '/var/lib/jenkins/workspace/Zdbm2.0/zdbm-*.tar.gz'
ZDBM_PACKAGE_NAME = '/soft/zdbm/zdbm-package/v{}/zdbm-202010291749-v2.1.6-rc1.tar.gz'.format(ZDBM_VERSION)
ZDBM_PACKAGE_NAME_TAR = ZDBM_PACKAGE_NAME.split('/')[-1]
ZDBM_AGENT_NAME = 'zdbm-client-agent-rc1.tar.gz'
ZDBM_AGENT_PATH = '/soft/zdbm/zdbm-package/v{}/{}'.format(ZDBM_VERSION, ZDBM_AGENT_NAME)
MY_JENKINS_NAME = 'myjenkins.tar'
CENTOS_PRE_INSTALL_NAME = 'zdbm_pre_install.sh'
RHEL_PRE_INSTALL_NAME = 'zdbm_pre_install_rhel.sh'
CENTOS_INSTSALL_NAME = 'zdbm_install.sh'
RHEL_INSTALL_NAME = 'zdbm_install_rhel.sh'
# Install_Data = 'auto_install_1014.sh'
# v2.1.4 之前
# Install_Data = 'auto_install_2000.sh'
Install_Data = 'auto_install_2140.sh'
# test_license_update_name
LICENSE_UPDATE_NAME = 'testD'


# mysql信息
MYSQL_PORT = 3333
MYSQL_DATABASE = 'zdbm'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'zdbm123'

# 默认系统用户和数据库用户账号密码相同
# 源环境
# sysdba用户
SYSDBA = 'sys'
SYSDBAPWD = 'root'

AGENT_PATH = '/opt'

# 单实例11.2.0.4数据库版本
OR11204_PACKAGE = 'app11204.tar.gz'
OR11204_IP = '192.168.12.1'
OR11204_PORT = '22'
OR11204_SYS_USER = 'zdbm'
OR11204_ROOT_PASSWORD = 'root1234'
OR11204_UUID = "087C8E3A-99A3-43E3-8001-9E78A8859658"
OR11204_NAME = 't12.1'
OR11204_ORACLE_ORCL_NAME = 'orcl'
OR11204_ORACLE_ORCL_USER = 'zdbm'
OR11204_ORACLE_ORCL_PASSWORD = 'zdbm'
OR11204_ORACLE_TEST_USER = 'zdbm'
OR11204_ORACLE_TEST_PASSWORD = 'zdbm'
OR11204_ORACLE_YANG_USER = 'zdbm'
OR11204_ORACLE_YANG_PASSWORD = 'zdbm'
# 单实例12.1.0.2数据库版本
OR12102_IP = '192.168.12.43'
OR12102_SYS_USER = 'zdm'
OR12102_NAME = 't12.43'
# 单实例12.2.0.1数据库版本
OR12201_IP = '192.168.12.144'
OR12201_SYS_USER = 'zdm'
OR12201_NAME = 't12.144'
# 单实例18c数据库版本
OR18C_IP = '192.168.12.196'
OR18C_SYS_USER = 'zdbm'
OR18C_NAME = 't12.196'
# 单实例aix环境11204数据库版本
AIX_IP = '192.168.150.10'
AIX_SYS_USER = 'oracle'
AIX_NAME = 't150.10'
# RAC环境11.2.0.4数据库版本
OR11204RAC_IP = '192.168.12.151'
OR11204RAC_PORT = '22'
OR11204RAC_SYS_USER = 'oracle'
OR11204RAC_NAME = 'rac12.151'
OR11204RAC_GRID_HOME = '/u01/app/grid/11204'

# 目标中间环境192.168.12.206
MDB1_IP = '192.168.12.206'
MDB1_NAME = 'm12.206'
MDB1_PORT = '22'
MDB1_USER = 'oracle'
MDB1_ORACLE_PORT = '1521'
MDB1_ORACLE_USER = 'zdbm'
MDB1_ORACLE_PASSWORD = 'zdbm'
MDB1_V2P_PATH = '/home/oracle'
MDB1_ROOT_PASSWORD = 'root1234'
MDB1_UUID = "499f3eb8-0c86-4f22-ae68-cb086a87dd41"
# 目标中间环境192.168.12.80
MDB2_IP = '192.168.12.80'
MDB2_NAME = 'm12.80'
MDB2_USER = 'oracle'
MDB2_PORT = 22
# 目标中间环境192.168.12.143
MDB3_IP = '192.168.12.143'
MDB3_NAME = 'm12.143'
MDB3_USER = 'oracle'
# 目标中间环境192.168.12.10
MDB4_IP = '192.168.12.10'
MDB4_NAME = 'm12.10'
MDB4_USER = 'oracle'
MDB4_PORT = 22222
# 目标中间环境 192.168.12.211
MDB5_IP = '192.168.12.211'
MDB5_NAME = 'm12.211'
MDB5_USER = 'oracle'
MDB5_PORT = 22
MDB5_ROOT_PASSWORD = 'root1234'
MDB5_UUID = "48c73aca-3e32-4725-bcc9-0904dbe02acf"
# 目标中间环境 192.168.12.41
MDB6_IP = '192.168.12.41'
MDB6_NAME = 'm12.41'
MDB6_USER = 'oracle'
MDB6_PORT = 22222

# toolpath默认为/opt/zdbm
TOOLPATH = '/opt/zdbm'
ORACLE_TOOLPATH = '/home/oracle/zdbm'
