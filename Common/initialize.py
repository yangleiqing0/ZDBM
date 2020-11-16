from Common.Auto_install import AutoInstall
from Common.connect_mysql import ConnMysql
from Common.get_license import Linux


class Initialize:

    def __init__(self):
        pass

    def install_zdbm(self):
        AutoInstall().reset_vi()
        self.reset_mysql()

    @staticmethod
    def reset_mysql():
        # 将docker-compose文件的mysql的端口设置为3306映射容器内的3306，然后重新加载通过docker-compose文件更新mysql
        Linux().linux_command(
            'cd /opt/zdbm/config && sed -i "51c     ports:"   docker-compose.yaml &&  sed -i "51s/^/    &/" docker-compose.yaml &&'
            'sed -i "52c        - 3306:3306"   docker-compose.yaml &&  sed -i "52s/^/    &/" docker-compose.yaml &&'
            '/usr/local/bin/docker-compose -f /opt/zdbm/config/docker-compose.yaml up -d && docker restart zdbm')
        print('将zdbm的mysql端口暴露')

        sql = 'insert into zdbm_users values(999,"2019-05-17 09:15:37","2019-05-17 09:15:37",NULL,"yanglei",' \
              '"$2a$10$j0c7si1lQucFAUXIGysyWel4GB0RpEy3maVz2bW.7u5zuhy5JfaaS",NULL,"1@qq.com",NULL,1,0) '
        ConnMysql().operate_mysql(sql)
        print('预设置用户yanglei')


if __name__ == '__main__':
    # Initialize().reset_mysql()
    Linux().linux_command(
        'cd /opt/zdbm/config && sed -i "51c     ports:"   docker-compose.yaml &&  sed -i "51s/^/    &/" docker-compose.yaml &&'
        'sed -i "52c        - 3306:3306"   docker-compose.yaml &&  sed -i "52s/^/    &/" docker-compose.yaml &&'
        '/usr/local/bin/docker-compose -f /opt/zdbm/config/docker-compose.yaml up -d && docker restart zdbm',
        ip='192.168.12.50', username='root', password='root1234', port='22')
    print('将zdbm的mysql端口暴露')
    # sql = 'insert into zdbm_users values(2,"2019-05-17 09:15:37","2019-05-17 09:15:37",NULL,"yanglei",' \
    #       '"$2a$10$j0c7si1lQucFAUXIGysyWel4GB0RpEy3maVz2bW.7u5zuhy5JfaaS",NULL,"1@qq.com",NULL,1,0) '
    # ConnMysql().operate_mysql(sql)
    # print('预设置用户yanglei')
