# 所有文件的参数配置
NEED_PARAMETER = {}
TEST_REPORT_EXCEL_NAME = 'ZDBM_test_report'
TEST_REPORT_TXT_NAME = 'ZDBM_test_result'
TEST_TITLE_NAME = 'ZDBM接口测试'
# 用于分割txt内的内容
# 服务器配置
IP = '192.168.12.201'
PORT = '40010'
GATEWAY = '61.139.2.69'
USERNAME = 'yanglei'
PASSWORD = 'yanglei1'
SSH_PORT = '22'
ROOT_NAME = 'root'
ROOT_PASSWORD = 'root123'
NEWPASSWORD = 'yanglei2'
SCR_PASSWORD = '$2a$10$YspahrSiuR.w8HShr4mgLOqz604DOGw/zFmRZrlONcJyrLhEYWt1m'
ORACLE_USER = 'oracle'
ORACLE_PWD = ORACLE_USER

# 默认存放zdbm.license在80服务器上
ZDBM_LICENSE_COMPANY_IP = '192.168.12.80'
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
ZDBM_VERSION = '1.0.13'

# 存放zdbm包的地址
ZDBM_PACKAGE_IP = '192.168.12.10'
ZDBM_PACKAGE_PORT = '22222'
ZDBM_PACKAGE_PWD = 'root1234'
# ZDBM_PACKAGE_NAME = '/soft/zdbm/zdbm-201905151636-v1.0.13.5.tar.gz'
ZDBM_PACKAGE_NAME = '/var/lib/jenkins/workspace/Zdbm/zdbm-*.tar.gz'
# ZDBM_PACKAGE_NAME = '/soft/zdbm/zdbm-201905301604-v1.0.10.12.tar.gz'
# ZDBM_PACKAGE_NAME = '/var/lib/jenkins/workspace/zdbm_auto_page/zdbm-*.tar.gz'
ZDBM_PACKAGE_NAME_TAR = ZDBM_PACKAGE_NAME.split('/')[-1]
MY_JENKINS_NAME = 'myjenkins.tar'
# test_license_update_name
LICENSE_UPDATE_NAME = 'testD'

# mysql信息
MYSQL_PORT = 3306
MYSQL_DATABASE = 'zdbm'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'zdbm123'

# 默认系统用户和数据库用户账号密码相同
# 源环境
# sysdba用户
SYSDBA = 'sys'
SYSDBAPWD = 'root'
# 单实例11.2.0.4数据库版本
OR11204_PACKAGE = 'app11204.tar.gz'
OR11204_IP = '192.168.12.1'
OR11204_SYS_USER = 'zdbm'
OR11204_NAME = 't12.1'
OR11204_ORACLE_ORCL_NAME ='orcl'
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
OR11204RAC_SYS_USER = 'oracle'
OR11204RAC_NAME = 'rac12.151'
OR11204RAC_GRID_HOME = '/u01/app/grid/11204'

# 目标中间环境192.168.12.50
MDB1_IP = '192.168.12.50'
MDB1_NAME = 'm12.50'
MDB1_USER = 'oracle'
MDB1_ORACLE_PORT = '1521'
MDB1_ORACLE_USER = 'system'
MDB1_ORACLE_PASSWORD = 'root123'
MDB1_V2P_PATH = '/home/oracle/v2p'
# 目标中间环境192.168.12.80
MDB2_IP = '192.168.12.80'
MDB2_NAME = 'm12.80'
MDB2_USER = 'oracle'
# 目标中间环境192.168.12.143
MDB3_IP = '192.168.12.143'
MDB3_NAME = 'm12.143'
MDB3_USER = 'oracle'
# 目标中间环境192.168.12.10
MDB4_IP = '192.168.12.10'
MDB4_NAME = 'm12.10'
MDB4_USER = 'oracle'
MDB4_PORT = 22222
# 目标中间环境 192.168.12.201
MDB5_IP = '192.168.12.201'
MDB5_NAME = 'm12.201'
MDB5_USER = 'oracle'
MDB5_PORT = 22
# toolpath默认为/opt/zdbm
TOOLPATH = '/opt/zdbm'
ORACLE_TOOLPATH = '/home/oracle/zdbm'
