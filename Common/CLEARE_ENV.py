import requests
import json
import time
from Common.configure import *
from Common.connect_mysql import ConnMysql
requests.packages.urllib3.disable_warnings()


class ClearEnv:

    def __init__(self, ip=IP):
        self.SERVER_IP = ip
        self.ip = 'https://{}:40010/api/'.format(self.SERVER_IP)
        self.session = requests.session()
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json, text/plain, */*'
        }
        self.username = 'admin'
        self.password = 'admin1'

    def login(self):
        # choose = input('确认是否重置%s 服务器的环境请输入Y/N' % (self.SERVER_IP))
        # if choose == 'Y':
        url = '{}login'.format(self.ip)
        data = '{"username":"%s","password":"%s","captchaID":"","captchaText":""}' % (self.username, self.password)
        login_html = self.session.post(url, data, headers=self.headers, verify=False).text
        self.get_token(login_html)
        # self.get_source_list()
        self.get_env_list()
        # else:
        #     print('请修改配置后再进行重置')
        #     exit()

    def get_token(self,login_html):
        login_html = json.loads(login_html)
        token = login_html['data']['token']
        self.headers.update({'token': token})

    # def get_source_list(self):
    #     url = '{}source/list'.format(self.ip)
    #     sources = self.session.get(url, headers=self.headers).text
    #     sources = json.loads(sources)['data']['sources']
        # for source in sources:
        #     self.enable_source(source['id'])
        #     print('已执行关闭源库id：%s' % source['id'])
        #     self.delete_source(source['id'])
        #     print('已执行删除源库id：%s' % source['id'])

    def enable_source(self, sid):
        url = '{}source/enable/{}'.format(self.ip, sid)
        self.session.put(url, headers=self.headers, verify=False)

    def delete_source(self, sid):
        url = '{}source/delete/{}'.format(self.ip, sid)
        self.session.delete(url, headers=self.headers, verify=False)

    def get_env_list(self):
        url = '{}env/list'.format(self.ip)
        envs = self.session.get(url, headers=self.headers).text
        envs = json.loads(envs)['data']['envs']
        for env in envs:
            self.enable_env(env['id'])
            print('已执行关闭环境id：%s' % env['id'])
            self.delete_env(env['id'])
            print('已执行删除环境id：%s' % env['id'])

    def enable_env(self, eid):
        url = '{}env/enable/{}'.format(self.ip, eid)
        data = '{"isEnable": false}'
        self.session.put(url, data, headers=self.headers, verify=False)

    def delete_env(self, eid):
        url = '{}env/delete/{}'.format(self.ip, eid)
        self.session.delete(url, headers=self.headers, verify=False)

    def listen_nodes_online(self, times=10):
        url1 = '{}login'.format(self.ip)
        data1 = '{"username":"%s","password":"%s","captchaID":"","captchaText":""}' % (self.username, self.password)
        login_html = self.session.post(url1, data1, headers=self.headers, verify=False).text
        login_html = json.loads(login_html)
        token = login_html['data']['token']
        self.headers.update({'token': token})
        url = '{}env/list'.format(self.ip)
        envs = self.session.get(url, headers=self.headers, verify=False).text
        print(envs)
        envs = json.loads(envs)['data']['envs']
        for env in envs:
            min_time = times*60
            is_online = False
            select_sql = 'select is_online from zdbm_orcl_env_nodes where env_id="%s"' % env['id']
            while min_time > 0:
                is_online = ConnMysql().select_mysql(select_sql)[0]
                print(str(env['id']) + '节点', '在线状态:' + str(is_online), '时间过去了', 600 - min_time, '秒')
                if is_online == 1:
                    break
                time.sleep(2)
                min_time = min_time - 2
            if is_online is False:
                return env['id'], is_online
        return 0, True


if __name__ == "__main__":
    ClearEnv("192.168.12.201").login()

