import pymysql
import paramiko
from Common.configure import *

RETAIN_TABLES = [
    'zdbm_zpools','zdbm_zpool_disks', 'zdbm_users','zdbm_user_tokens','zdbm_task_weights','zdbm_tactics',
    'zdbm_system_setups','zdbm_system_components','zdbm_server_oracles','zdbm_license_infos','zdbm_codes',
    'zdbm_cell_network_cards', 'zdbm_cell_services', 'zdbm_cells',
    # 'zdbm_virtual_ips',
    # 'zdbm_virtual_machines',
    'zdbm_virtual_networks', 'zdbm_vm_templates'
                 ]


class DeleteWords:
    def __init__(self):
        self.host = '192.168.12.202'
        # self.host = IP
        self.linux_port = 22
        self.linux_user = 'root'
        self.linux_passwd = 'root123'
        mysql_port = 3333
        user = 'root'
        passwd = 'zdbm123'
        db = 'zdbm'
        # choose = input('确认是否重置%s 服务器的%s数据库表信息,请输入Y/N'%(self.host,db))
        # if  choose == 'Y':
        self.db = pymysql.connect(host=self.host, port=mysql_port, user=user, passwd=passwd, db=db, charset='utf8')
        # else:
        #     print('请修改配置后再进行清理')
        #     exit()

    def select_tables(self):
        sql = 'show tables'
        self.cur = self.db.cursor()
        self.cur.execute(sql)
        tables = self.cur.fetchall()
        self.clear_tables(tables)

    def clear_tables(self,tables):
        for table in tables:
            # print(table[0])
            if table[0] in RETAIN_TABLES:
                continue
            sql = "truncate table %s"%table
            self.cur.execute(sql)
            print('已清理: %s 表'%table)

        self.db.commit()
        self.db.close()
        print('清除%s数据库完毕'%self.host)

    def clear_mpool(self):

        ssh = paramiko.SSHClient()
        # 設定自動加入 遠端主機的 SSH Key
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 設定連接 ssh 的主機名稱, 使用者名稱, ssh 私鑰路徑
        # ssh.connect(hostname=REMOTEHOST, username=USERNAME, pkey=key)
        ssh.connect(self.host, port=self.linux_port, username=self.linux_user, password=self.linux_passwd)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /mpool')
        result = ssh_stdout.readlines()
        # ssh.exec_command('zfs destroy -r {}'.format(r))
        for r in result:
            r = "mpool/"+r.strip()
            excute = 'zfs destroy -r {}'.format(r)
            ssh.exec_command(excute,timeout=15)
            _, content, _ = ssh.exec_command('echo $?')
            content = content.read().strip()
            print(content)
            if content == 0:
                print('清除{}成功,命令{}'.format(r,excute))
            else:
                print('清除{}失败,命令{},返回码{}'.format(r,excute,content))






if __name__ == "__main__":
    DeleteWords().select_tables()
