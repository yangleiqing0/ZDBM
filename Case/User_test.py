from ZDBM.Common.Request_method import RequestMethod
from ZDBM.Common.connect_mysql import ConnMysql
from ZDBM.Common.configure import *
from ZDBM.Common.clear_env import ClearEnv


class UserTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_user_get(self):
        # 获取当前用户信息
        content = RequestMethod().to_requests(self.request_method, 'user/get')
        print(content)
        return {
            'actualresult': content
        }

    def test_user_list(self):
        # 列出用户信息
        content = RequestMethod().to_requests(self.request_method, 'user/list?keyword=%s' % USERNAME)
        print(content)
        return {
            'actualresult': content
        }

    def test_user_add(self):
        # 添加用户
        data = """
        {
  "username": "%s",
  "password": "%s",
  "name": "%s",
  "mail": "%s",
  "phone": "%s",
  "enable": true
}
        """ % (
            self.params['username'], self.params['password'], self.params['name'],
            self.params['mail'], self.params['phone']
               )

        ClearEnv().delete_exists_mysql("zdbm_users", "username", self.params['username'])
        # 如果用户存在就删除此用户信息
        query_sql = 'select name from zdbm_users where username="%s";' % self.params['username']
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/add', data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        print(new_database_value, type(new_database_value),'name'+ self.params['name'])
        return {
            'actualresult': content,'old_database_value': 'name:' + str(old_database_value),
            'new_database_value': 'name:' + str(new_database_value), 'database_assert_method': False,
            'name': self.params['name']
        }

    def test_user_update(self):
        # 更新用户信息
        data = """
        {
  "password": "%s",
  "name": "%s",
  "mail": "%s",
  "phone": "%s",
  "enable": true
}
        """ % (
            self.params['password'], self.params['name'],
            self.params['mail'], self.params['phone']
               )
        query_user_id_sql = 'select id from zdbm_users where username="%s";' % self.params['username']
        user_id = ConnMysql().select_mysql(query_user_id_sql)[0]
        query_user_name_sql = 'select name from zdbm_users where username="%s";' % self.params['username']
        old_database_value = ConnMysql().select_mysql(query_user_name_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/update/%s' % user_id, data=data)
        new_database_value = ConnMysql().select_mysql(query_user_name_sql)[0]
        return {
            'actualresult': content, 'old_database_value': 'name:' + old_database_value,
            'new_database_value': 'name:' + new_database_value, 'database_assert_method': False,
            'name': self.params['name']
        }

    def test_user_self(self):
        # 更新当前用户信息

        data = """
        {
  "name": "%s",
  "mail": "%s",
  "phone": "%s",
  "oldPassword": "%s",
  "newPassword": "%s"
}
        """ % (
            self.params['name'], self.params['mail'],
            self.params['phone'], self.params['oldPassword'],self.params['newPassword']
               )
        query_user_name_sql = 'select name from zdbm_users where username="%s";' % USERNAME
        old_database_value = ConnMysql().select_mysql(query_user_name_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/self', data=data)
        new_database_value = ConnMysql().select_mysql(query_user_name_sql)[0]
        return {
            'actualresult': content, 'old_database_value': 'name:' + old_database_value,
            'new_database_value': 'name:' + new_database_value, 'database_assert_method': False,
            'name': self.params['name']
        }

    def test_user_password(self):
        # 更新当前用户密码
        data = """
        {
  "oldPassword": "%s",
  "newPassword": "%s"
}
        """ % (PASSWORD, NEWPASSWORD)
        query_user_password_sql = 'select password from zdbm_users where username="%s";' % USERNAME
        old_database_value = ConnMysql().select_mysql(query_user_password_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/password', data=data)
        new_database_value = ConnMysql().select_mysql(query_user_password_sql)[0]
        ClearEnv().update_user_password()
        # 将密码重置为yanglei1
        return {
            'actualresult': content, 'old_database_value': 'password:' + old_database_value,
            'new_database_value': 'password:' + new_database_value, 'database_assert_method': False
        }

    def test_user_enable(self):
        # 设置用户有效性
        data = '{"enable": false}'
        user_id_sql = 'select id from zdbm_users where username="%s";' % USERNAME
        user_id = ConnMysql().select_mysql(user_id_sql)[0]
        query_user_enable_sql = 'select enable from zdbm_users where username="%s";' % USERNAME
        old_database_value = ConnMysql().select_mysql(query_user_enable_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/enable/%s' % user_id, data=data)
        new_database_value = ConnMysql().select_mysql(query_user_enable_sql)[0]
        ClearEnv().update_user_enable()
        # 将用户有效性重置为1
        return {
            'actualresult': content, 'old_database_value': 'enable:' + str(old_database_value),
            'new_database_value': 'enable:' + str(new_database_value), 'database_assert_method': False
        }

    def test_user_delete(self):
        # 删除目标用户
        query_user_id = 'select id from zdbm_users where username="%s";' % self.params['username']
        user_id = ConnMysql().select_mysql(query_user_id)[0]
        query_sql = 'select deleted_at from zdbm_users where username="%s";' % self.params['username']
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'user/delete/%s' % user_id)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
            'actualresult': content, 'old_database_value': 'deleted_at:' + str(old_database_value),
            'new_database_value': 'deleted_at:' + str(new_database_value), 'database_assert_method': False
        }


if __name__ == '__main__':
    UserTest({'request_method': 'get'}).test_user_get()