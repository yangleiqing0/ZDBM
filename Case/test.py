import paramiko
import time
trans = paramiko.Transport(('192.168.12.1', 1521))    # 【坑1】 如果你使用 paramiko.SSHClient() cd后会回到连接的初始状态
trans.start_client()
# 用户名密码方式
trans.auth_password(username='sys', password='root')
# 打开一个通道
channel = trans.open_session()
channel.settimeout(7200)
# 获取一个终端
channel.get_pty()
# 激活器
channel.invoke_shell()
cmd = 'select * from tab'
# 发送要执行的命令
channel.send(cmd)
while True:
        time.sleep(0.2)
        rst = channel.recv(1024)
        rst = rst.decode('utf-8')
        print(rst)
channel.close()
trans.close()
# ssh = paramiko.SSHClient()
# # 設定自動加入 遠端主機的 SSH Key
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # 設定連接 ssh 的主機名稱, 使用者名稱, ssh 私鑰路徑
# # ssh.connect(hostname=REMOTEHOST, username=USERNAME, pkey=key)
# ssh.connect('192.168.12.80', port=22, username='root', password='root1234')
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
# result = ssh_stdout.read()
# print(result)

# a = {1:"d1",2:"d21"}
# b = {'actualresult': '{"code":0,"data":{"user":{"id":25,"createdAt":"2019-04-29T09:03:22.721194733+08:00","updatedAt":"2019-04-29T09:03:22.721194733+08:00","username":"yangleiqing","name":"lXO7Ypm","mail":"253775405@qq.com","phone":"15155492421","enable":true,"isInitialCipher":true}},"errMsg":""}', 'new_database_value': 'name:lXO7Ypm', 'database_assert_method': False, 'name': 'lXO7Ypm'}
# print(b.get('name'))
# import time
# a = "快照 " + (time.strftime("%Y-%m-%d %H:%M:%S"))
# print(type(a))
a = {"a":1}
b = {"a":2}
a.update(b)
print(a)