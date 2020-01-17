import paramiko
import time
from Common.configure import *


class GetLicense:

    def __init__(self, key=None):
        self.key = key
        self.ssh = paramiko.SSHClient()
        # 設定自動加入 遠端主機的 SSH Key
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    def write_key(self):
        self.ssh.connect(ZDBM_LICENSE_COMPANY_IP, port=ZDBM_LICENSE_PORT, username=ZDBM_LICENSE_ROOT, password=ZDBM_LICENSE_PASSWORD,
                         allow_agent=False, look_for_keys=False)
        # 設定連接 ssh 的主機名稱, 使用者名稱, ssh 私鑰路徑
        self.ssh.exec_command("rm -rf /usr/local/zdbm-license/zdbm_license.dat")
        self.ssh.exec_command("rm -rf /usr/local/zdbm-license/zdbm_license_key.dat")
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[0]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[1]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[2]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[3]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[4]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[5]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[6]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[7]))
        time.sleep(0.1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && echo %s >> zdbm_license_key.dat' % str(self.key[8]))
        time.sleep(1)
        self.ssh.exec_command('cd /usr/local/zdbm-license/ && ./zdbm-license-linux-386-v1.0.10 -k zdbm_license_key.dat -d 100 --serviceDays=100 -e standard -s 100 -v 100')
        time.sleep(1)
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command('cat /usr/local/zdbm-license/zdbm_license.dat')
        result = ssh_stdout.read()
        print(result)
        return result

    def auto_deployment(self):
        pass

    def linux_mkdir(self, dir):
        self.ssh.exec_command('mkdir -p %s' % dir)

    def linux_command(self, com, ip=IP, port=SSH_PORT, password=ROOT_PASSWORD, username=ROOT_NAME):
        self.ssh.connect(ip, port=port, username=username, password=password)
        print("连接ssh:", ip, port, password)
        print("com命令:", com)
        try:
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(com)
            stout = ssh_stdout.readlines()
            errs = ssh_stderr.readlines()
            for s in stout:
                print("ssh_stdout:", s)
            for err in errs:
                print("error: ", err)
        except Exception as e:
            print(e)

    def get_result(self, com, ip=IP, port=SSH_PORT, password=ROOT_PASSWORD, username=ROOT_NAME):
        self.ssh.connect(ip, port=port, username=username, password=password)
        print("连接ssh:", ip, port, password)
        print("com命令:", com)
        stout = errs = None
        try:
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(com)
            stout = ssh_stdout.readlines()
            errs = ssh_stderr.readlines()
            for s in stout:
                print("ssh_stdout:", s)
            for err in errs:
                print("error: ", err)
        except Exception as e:
            print(e)
            errs = "{}".format(e)
        return stout, errs

if __name__ == '__main__':
    GetLicense().linux_mkdir('/home/oracle/zdbm/vJ6eH4MlXanKO1jN')