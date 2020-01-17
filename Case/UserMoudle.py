from Common.requests_method import JsonRequest
import time
from Common.get_params import get_params

class UserMoudle:

    def __init__(self, params=None):
        self.time = int(time.time()*1000)
        self.params = params


    def gold_mall_token(self):

        uid = self.params['uid']
        auth = self.params['auth']
        if self.params.get('account'):
            account = self.params['account']
            print(account)
            uid, auth = get_params().get_uid_auth(account)


        print('1',uid,auth)
        """
        金币商城首页token获取
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/GoldMallTokenApiService'
        data = '''
            {
          "reqBaseVO": {
            "netStandard": "GSM",
            "address": "",
            "os": "ios",
            "auth": "%s",
            "netType": "4G",
            "idfa": "",
            "channel": "014585",
            "imsi": "",
            "deviceId": "1234",
            "osVer": "iOS11.2.6",
            "mac": "AG:22:0B:CB:12:4C",
            "caller": "",
            "phoneModel": "",
            "clientVer": "1.0.0",
            "imei": "",
            "myUid": "%s",
            "androidId": "",
            "openuuid": ""
          }
        }
        '''%(auth, uid)
        content = JsonRequest().post(url, data=data)
        print(content)
        return content

    def lease_auth(self):
        """
        授权续租
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/LeaseAuthApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "lastDate": %d
}
        '''%self.time
        content = JsonRequest().post(url, data=data)
        print(content)

    def login(self, account, pwd='e10adc3949ba59abbe56e057f20f883e'):
        """
        账号密码登录
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/LoginApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "pwd": "%s",
  "account": "%d"
}
        '''%(pwd,int(account))
        content = JsonRequest().post(url, data=data)
        return content

    def loginout(self):
        """
        退出登陆
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/LogoutApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  }
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def password_change(self):
        """
        修改密码
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/PasswordChangeApiService'
        data = '''
        {
  "verifyCode": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "",
  "newPwd": "",
  "sessionId": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def password_check(self):
        """
        校验原密码
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/PasswordCheckApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "oldPwd": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def phone_bind(self):
        """
        绑定手机号
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/PhoneBindApiService'
        data = '''
        {
  "password": "",
  "verifyCode": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "",
  "sessionId": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def phone_exits(self):
        """
        校验手机号是否存在
        :return:
        """
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/PhoneExitsApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "15155492421"
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def register(self):
        """注册接口"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/RegisterApiService'
        data = '''
        {
  "password": "eb122c107de9e4f26c854df111b3ccf1",
  "verifyCode": "000000",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "",
  "sessionId": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def social_bind(self):
        """绑定第三方账号"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/SocialBindApiService'
        data = '''
        {
  "unionid": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "openId": "",
  "nickname": "",
  "source": "",
  "avatar": "",
  "expireAt": %d
}
        '''%self.time
        content = JsonRequest().post(url, data=data)
        print(content)

    def social_unbind(self):
        """解绑第三方账号"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/SocialUnbindApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "source": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def verification_code_get(self):
        """获取短信验证码"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/VerificationCodeGetApiService'
        data = '''
        {
  "verifyCode": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "",
  "sessionId": "",
  "type": 1
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def verification_valid(self):
        """验证码验证接口"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/VerificationValidApiService'
        data = '''
        {
  "verifyCode": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "phone": "",
  "sessionId": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def user_detail(self):
        """用户详情"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/UserDetailApiService'
        data = '''
        {
  "uid": "",
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  }
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def user_profile_detail(self):
        """用户个人资料详情获取"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/UserProfileDetailApiService'
        data = '''
        {
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  }
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

    def user_profile_update(self):
        """用户个人资料修改"""
        url = 'http://61.191.24.229:6083/kypbtool/api/req/kuyin_move_test/UserProfileUpdateApiService'
        data = '''
        {
  "area": "",
  "birthday": "",
  "gender": 0,
  "reqBaseVO": {
    "netStandard": "GSM",
    "address": "",
    "os": "ios",
    "auth": "",
    "netType": "4G",
    "idfa": "",
    "channel": "014585",
    "imsi": "",
    "deviceId": "1234",
    "osVer": "iOS11.2.6",
    "mac": "AG:22:0B:CB:12:4C",
    "caller": "",
    "phoneModel": "",
    "clientVer": "1.0.0",
    "imei": "",
    "myUid": "",
    "androidId": "",
    "openuuid": ""
  },
  "signature": "",
  "nickname": "",
  "avatar": ""
}
        '''
        content = JsonRequest().post(url, data=data)
        print(content)

if __name__ == '__main__':

    # UserMoudle().gold_mall_token(uid=3,auth=4)
    # UserMoudle().lease_auth()
    UserMoudle().login()
    # UserMoudle().loginout()
    # UserMoudle().password_change()
    # UserMoudle().password_check()
    # UserMoudle().phone_bind()
    # UserMoudle().phone_exits()
    # UserMoudle().register()
    # UserMoudle().social_bind()
    # UserMoudle().social_unbind()
    # UserMoudle().verification_code_get()
    # UserMoudle().verification_valid()
    # UserMoudle().user_detail()
    # UserMoudle().user_profile_detail()
    # UserMoudle().user_profile_update()