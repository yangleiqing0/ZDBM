# import paramiko
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