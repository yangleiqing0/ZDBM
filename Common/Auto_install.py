import time
from Common.configure import *
from Common.get_license import GetLicense


class AutoInstall:

    def __init__(self):
        pass

    def reset_vi(self):
        # 将/etc/ssh/ssh_config设置为不校验key
        is_centos = True
        version = GetLicense().linux_command_return("hostnamectl | grep 'Kernel: Linux 3.10.0-957.el7.x86_64'")

        if version is None:
            print("当前版本是rhel7.6")
            is_centos = False
        else:
            print("当前版本是centos7.6")
        # time.sleep(50)
        GetLicense().linux_command(
            'sed -i "35c StrictHostKeyChecking no"   /etc/ssh/ssh_config &&  sed -i "35s/^/    &/"    '
            '/etc/ssh/ssh_config')
        print('将/etc/ssh/ssh_config设置为不校验key成功')
        GetLicense().linux_command('cd /opt && rm -rf auto_install*.sh %s ' % ZDBM_PACKAGE_NAME_TAR)
        print('清除/opt下的文件成功')
        time.sleep(1)
        GetLicense().linux_command('sshpass  -p %s scp -P %s -o StrictHostKeychecking=no '
                                   '%s /soft/%s root@%s:/opt' %
                                   (ROOT_PASSWORD, SSH_PORT, ZDBM_PACKAGE_NAME, Install_Data, IP), ip=ZDBM_PACKAGE_IP,
                                   port=ZDBM_PACKAGE_PORT, password=ZDBM_PACKAGE_PWD)
        print('将安装脚本和安装包放入目标服务器成功')
        time.sleep(15)
        print('开始进行预安装')
        if Install_Data == 'auto_install_1014.sh':
            GetLicense().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s' % (
                Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, ROOT_PASSWORD))
        elif Install_Data == 'auto_install_2140.sh':
            if is_centos:
                GetLicense().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s %s' % (
                    Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD, CENTOS_PRE_INSTALL_NAME))
            else:
                GetLicense().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s %s' % (
                    Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD, RHEL_PRE_INSTALL_NAME))
        else:
            GetLicense().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s' % (
                Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD))
        print('预安装ZDBM所需软件结束')
        GetLicense().wait_host_start()
        # GetLicense().linux_command('echo nameserver 192.168.0.1 > /etc/resolv.conf')
        # print("设置DNS为192.168.0.1成功")
        time.sleep(100)
        print('开始进行安装ZDBM')
        if Install_Data == 'auto_install_2140.sh':
            if is_centos:
                GetLicense().linux_command('cd /opt/zdbm && sh {}'.format(CENTOS_INSTSALL_NAME))
            else:
                GetLicense().linux_command('cd /opt/zdbm && sh {}'.format(RHEL_INSTALL_NAME))
        else:
            GetLicense().linux_command('cd /opt/zdbm && sh {}'.format(CENTOS_INSTSALL_NAME))
        print('安装ZDBM结束')

        print('开始创建存储池')
        self.add_mpool()
        print('存储池创建结束')
        GetLicense().linux_command('docker restart zdbm')
        GetLicense().linux_command('systemctl restart zdbm_server')
        print('重启zdbm')
        time.sleep(2)
        GetLicense().linux_command('rm -rf /opt/{}'.format(ZDBM_PACKAGE_NAME))

    def add_mpool(self):
        GetLicense().linux_command('zpool  create -f  mpool sdc  &&zpool  create -f  mpool01 sdd sde')


if __name__ == '__main__':
    AutoInstall().reset_vi()
