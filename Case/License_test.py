from Common.Request_method import RequestMethod
from Common.rand_name import RangName
from Common.connect_mysql import ConnMysql
from Common.get_license import Linux


class LicenseTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_license_get(self):
        # 获取版权信息
        content = RequestMethod().to_requests(self.request_method, 'license/get')
        return {'actualresult': content}

    def test_license_key_zdbm_license_key(self):
        # 获取版权Key
        content = RequestMethod().to_requests(self.request_method, 'license/key/zdbm_license_key.dat')
        print(content)
        return {'actualresult': content}

    def test_license_update_name(self):
        # 设置客户名称
        name = self.params['name']
        data = '{"name":"%s"}' % name
        sql = 'select name from zdbm_license_infos where id=1'
        old_database_value = ConnMysql().select_mysql(sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'license/update/name', data=data)
        new_database_value = ConnMysql().select_mysql(sql)[0]
        return {
            'actualresult': content, 'name': name, 'old_database_value': 'name:' + old_database_value,
            'new_database_value': 'name:' + new_database_value, 'database_assert_method': False
        }

    def test_license_update_license(self):
        # 更新授权码
        lice = self.params['license']
        if lice == '获取':
            key = LicenseTest({'request_method': 'get'}).test_license_key_zdbm_license_key()['actualresult']
            key = key.split('\n')
            lice = str(Linux(key).write_key())[2:-1]
        print("lice:", lice)
        data = '{"license":"%s"}' % lice
        del_sql = 'update zdbm_license_infos set license=" " where id=1'
        ConnMysql().operate_mysql(del_sql)
        old_sql = 'select license from zdbm_license_infos where id=1'
        old_database_value = ConnMysql().select_mysql(old_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'license/update/license', data=data)
        new_sql = 'select license from zdbm_license_infos where id=1'
        new_database_value = ConnMysql().select_mysql(new_sql)[0]
        print(old_database_value, new_database_value)
        return {
            'actualresult': content, 'old_database_value': 'license:' + old_database_value,
            'new_database_value': 'license:' + new_database_value, 'database_assert_method': False
        }


if __name__ == '__main__':
    LicenseTest({'request_method': 'get'}).test_license_key_zdbm_license_key()
