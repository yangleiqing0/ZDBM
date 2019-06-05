import requests
import json
from ZDBM.Common.configure import *
requests.packages.urllib3.disable_warnings()


class RequestMethod:

    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json, text/plain, */*'
        }

    def login(self):
        url = 'https://{}:{}/api/login'.format(IP, PORT)
        data = '{"username":"%s","password":"%s","captchaID":"","captchaText":""}' % (USERNAME, PASSWORD)
        login_html = self.session.post(url, data, headers=self.headers, verify=False).text
        self.get_token(login_html)


    def get_token(self,login_html):
        login_html = json.loads(login_html)
        token = login_html['data']['token']
        self.headers.update({'token': token})

    def to_requests(self, request_method,  route, data=None, isneedlogin=True):
        url = 'https://{}:{}/api/{}'.format(IP, PORT, route)
        data = '{}'.format(data)
        print(url, request_method,data, isneedlogin)
        if isneedlogin:
            self.login()
        if request_method == 'get':
            content = self.session.get(url, headers=self.headers, verify=False).text
        elif request_method == 'post':
            content = self.session.post(url, headers=self.headers, data=data, verify=False).text
        elif request_method == 'put':
            content = self.session.put(url, headers=self.headers, data=data, verify=False).text
        elif request_method == 'delete':
            content = self.session.delete(url, headers=self.headers, data=data, verify=False).text
        else:
            content = '未知的请求方法'
        return content


if __name__ == '__main__':
    RequestMethod().login()
