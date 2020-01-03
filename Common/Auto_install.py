import time
from ZDBM.Common.configure import *
from ZDBM.Common.get_license import GetLicense


class AutoInstall:

    def __init__(self):
        pass

    def reset_vi(self):
        # 将/etc/ssh/ssh_config设置为不校验key
        GetLicense().linux_command('sed -i "35c StrictHostKeyChecking no"   /etc/ssh/ssh_config &&  sed -i "35s/^/    &/"    /etc/ssh/ssh_config')
        print('将/etc/ssh/ssh_config设置为不校验key成功')
        GetLicense().linux_command('cd /opt && rm -rf auto_install*.sh %s ' % ZDBM_PACKAGE_NAME_TAR)
        print('清除/opt下的文件成功')
        time.sleep(1)
        GetLicense().linux_command('sshpass  -p %s scp -P %s -o StrictHostKeychecking=no '
                                   '%s /soft/%s root@%s:/opt' %
                                   (ROOT_PASSWORD, SSH_PORT, ZDBM_PACKAGE_NAME, Install_Data, IP), ip=ZDBM_PACKAGE_IP, port=ZDBM_PACKAGE_PORT,password=ZDBM_PACKAGE_PWD)
        print('将安装脚本和安装包放入目标服务器成功')
        time.sleep(15)
        print('开始进行预安装')
        if Install_Data == 'auto_install_1014.sh':
            GetLicense().linux_command('cd /opt &&sh %s %s %s %s' % (Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, ROOT_PASSWORD))
        else:
            GetLicense().linux_command('cd /opt &&sh %s %s %s %s %s' % (Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD))
        print('预安装ZDBM所需软件结束')
        time.sleep(120)
        # GetLicense().linux_command('echo nameserver 192.168.0.1 > /etc/resolv.conf')
        # print("设置DNS为192.168.0.1成功")
        print('开始进行安装ZDBM')
        GetLicense().linux_command('cd /opt/zdbm && sh zdbm_install.sh')
        print('安装ZDBM结束')
        time.sleep(10)
        print('开始创建存储池')
        self.add_mpool()
        print('存储池创建结束')
        GetLicense().linux_command('docker restart zdbm')
        GetLicense().linux_command('systemctl restart zdbm_server')
        print('重启zdbm')
        time.sleep(2)

    def add_mpool(self):
        GetLicense().linux_command('zpool  create -f  mpool   sdb   sdc  &&zpool  create -f  mpool01 sdd sde')


if __name__ == '__main__':
    AutoInstall().reset_vi()