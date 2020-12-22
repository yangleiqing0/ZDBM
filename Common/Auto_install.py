import time
from Common.configure import *
from Common.get_license import Linux


class AutoInstall:

    def __init__(self):
        pass

    def reset_vi(self):
        # 将/etc/ssh/ssh_config设置为不校验key
        is_centos = True
        version = Linux().linux_command_return("hostnamectl | grep 'Kernel: Linux 3.10.0-957.el7.x86_64'",
                                                    username=ROOT_NAME, password=ROOT_PASSWORD)

        if version is None:
            print("当前版本是rhel7.6")
            is_centos = False
        else:
            print("当前版本是centos7.6")
        # time.sleep(50)
        Linux().linux_command(
            'sed -i "35c StrictHostKeyChecking no"   /etc/ssh/ssh_config &&  sed -i "35s/^/    &/"    '
            '/etc/ssh/ssh_config')
        print('将/etc/ssh/ssh_config设置为不校验key成功')
        Linux().linux_command('cd /opt && rm -rf /u01/app11204.tar.gz && rm -rf auto_install*.sh %s ' % ZDBM_PACKAGE_NAME_TAR)
        print('清除/opt下的文件成功')
        time.sleep(1)
        Linux().linux_command('echo "" > /root/.ssh/known_hosts && sshpass  -p %s scp -P %s -o '
                                   'StrictHostKeychecking=no %s /soft/%s root@%s:/opt' %
                                   (ROOT_PASSWORD, SSH_PORT, ZDBM_PACKAGE_NAME, Install_Data, IP), ip=ZDBM_PACKAGE_IP,
                                   port=ZDBM_PACKAGE_PORT, password=ZDBM_PACKAGE_PWD)
        print('将安装脚本和安装包放入目标服务器成功')
        time.sleep(15)
        print('开始进行预安装')
        if Install_Data == 'auto_install_1014.sh':
            Linux().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s' % (
                Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, ROOT_PASSWORD))
        elif Install_Data == 'auto_install_2140.sh':
            if is_centos:
                Linux().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s %s' % (
                    Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD, CENTOS_PRE_INSTALL_NAME))
            else:
                Linux().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s %s' % (
                    Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD, RHEL_PRE_INSTALL_NAME))
        else:
            Linux().linux_command('hwclock --hctosys && cd /opt &&sh %s %s %s %s %s' % (
                Install_Data, ZDBM_PACKAGE_NAME_TAR, IP, SSH_PORT, ROOT_PASSWORD))
        print('预安装ZDBM所需软件结束')
        Linux().wait_host_start()
        Linux().linux_command('echo nameserver 192.168.0.1 > /etc/resolv.conf')
        if IP == "192.168.12.206":
            cmd = """TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="none"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="eth0"
UUID="1be3ef9c-950f-4564-934f-59edf345ca8f"
DEVICE="eth0"
ONBOOT="yes"
MACADDR="random"
IPADDR="192.168.12.206"
PREFIX="16"
GATEWAY="192.168.0.1"
DNS1="192.168.0.1"
IPV6_PRIVACY=no"""
            Linux().linux_command('echo """{}""" > /etc/sysconfig/network-scripts/ifcfg-eth0'.format(cmd))
        print("设置DNS为192.168.0.1成功")
        time.sleep(100)
        print('开始进行安装ZDBM')
        if Install_Data == 'auto_install_2140.sh':
            if is_centos:
                Linux().linux_command('cd /opt/zdbm && sh {}'.format(CENTOS_INSTSALL_NAME))
            else:
                Linux().linux_command('cd /opt/zdbm && sh {}'.format(RHEL_INSTALL_NAME))
        else:
            Linux().linux_command('cd /opt/zdbm && sh {}'.format(CENTOS_INSTSALL_NAME))
        print('安装ZDBM结束')

        print('开始创建存储池')
        self.add_mpool()
        print('存储池创建结束')
        Linux().linux_command('docker restart zdbm')
        Linux().linux_command('systemctl restart zdbm_server')
        print('重启zdbm')
        time.sleep(2)
        Linux().linux_command('rm -rf /opt/{}'.format(ZDBM_PACKAGE_NAME))

    def add_mpool(self):
        Linux().linux_command('zpool  create -f  mpool sdc  &&zpool  create -f  mpool01 sdd sde')


if __name__ == '__main__':
    AutoInstall().reset_vi()
