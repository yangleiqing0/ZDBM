import time
from Common.Request_method import RequestMethod
from Common.connect_mysql import ConnMysql
from Common.configure import *
from Common.clear_env import ClearEnv


class CellTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_cell_test(self):
        # 测试节点功能支持，比如vt
        ip = self.params['ip']
        port = self.params['port']
        username = self.params['username']
        password = self.params['password']
        data = """{
  "ip": "%s",
  "port": %s,
  "username": "%s",
  "password": "%s"
}""" % (ip, port, username, password)
        content = RequestMethod().to_requests(self.request_method, 'cell/test', data=data)
        return {
            'actualresult': content
        }

    def test_cell_get(self):
        # 获取节点详细信息
        query_cell_id = 'select id from zdbm_cells where ip="%s"' % IP
        cell_id = ConnMysql().select_mysql(query_cell_id)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/get/%s' % cell_id)
        return {
            'actualresult': content
        }

    def test_cell_list(self):
        # 列出节点
        content = RequestMethod().to_requests(self.request_method, 'cell/list')
        return {
            'actualresult': content
        }

    def test_cell_add(self):
        # 添加节点
        # 先清理zdbm_cells,zdbm_cell_services,zdbm_cell_network_cards表
        ClearEnv().clear_cell_mysql()
        data = """
{
  "cellName": "%s",
  "cellType": "%s",
  "description": "%s",
  "ip": "%s",
  "port": %s,
  "username": "%s",
  "password": "%s"
}
""" % (
         self.params['cellName'], self.params['cellType'], self.params['description'], self.params['ip'],
         self.params['port'], self.params['username'], self.params['password']
        )
        query_sql = 'select cell_name from zdbm_cells'
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/add', data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
             'actualresult': content, 'old_database_value': 'cell_name:' + old_database_value,
             'new_database_value': 'cell_name:' + new_database_value, 'database_assert_method': False
        }

    def test_cell_update(self):
        # 修改节点信息
        data = """
        {
          "cellName": "%s",
          "description": "%s",
          "ip": "%s",
          "username": "%s",
          "password": "%s",
          "port": %s
        }
        """ % (
            self.params['cellName'], self.params['description'], self.params['ip'],
            self.params['username'], self.params['password'], self.params['port']
        )
        query_cell_id = 'select id from zdbm_cells where ip="%s"' % IP
        cell_id = ConnMysql().select_mysql(query_cell_id)[0]
        query_sql = 'select cell_name from zdbm_cells'
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/update/%s' % cell_id, data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
             'actualresult': content, 'old_database_value': 'cell_name:' + old_database_value,
             'new_database_value': 'cell_name:' + new_database_value, 'database_assert_method': False
        }

    def test_cell_update_service(self):
        # 修改节点服务信息
        data = '{"serviceName":"%s","operateType":"%s","operateValue":"%s"}' % (
            self.params['serviceName'], self.params['operateType'], self.params['operateValue']
        )
        query_cell_id = 'select id from zdbm_cells where ip="%s"' % IP
        cell_id = ConnMysql().select_mysql(query_cell_id)[0]
        query_sql = 'select auto_start from zdbm_cell_services where service_type="%s" and cell_id=%s ' % \
                    (self.params['serviceName'], cell_id)
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/updateService/%s' % cell_id, data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
            'actualresult': content, 'old_database_value': 'auto_start:' + str(old_database_value),
            'new_database_value': 'auto_start:' + str(new_database_value), 'database_assert_method': False
        }

    def test_cell_default_network(self):
        # 设置节点主网卡
        query_cell_id = 'select id from zdbm_cells where ip="%s"' % IP
        cell_id = ConnMysql().select_mysql(query_cell_id)[0]
        query_net_card_name = 'select name from zdbm_cell_network_cards where type="bridge" and ' \
                              'running_status="connected"'
        net_card_name = ConnMysql().select_mysql(query_net_card_name)[0]
        data = '{"netCardName":"%s","used":true}' % net_card_name
        query_sql = 'select virtual_net_used from zdbm_cell_network_cards where name="%s"' % net_card_name
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/default/network/%s' % cell_id, data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
            'actualresult': content, 'old_database_value': 'virtual_net_used:' + str(old_database_value),
            'new_database_value': 'virtual_net_used:' + str(new_database_value), 'database_assert_method': False
        }

    def test_delete_cell(self):
        # 删除节点
        query_cell_id = 'select id from zdbm_cells where ip="%s"' % IP
        cell_id = ConnMysql().select_mysql(query_cell_id)[0]
        data = """{
  "ids": [
    %s
  ]
}""" % cell_id
        query_sql = 'select deleted_at from zdbm_cells where ip="%s"' % IP
        old_database_value = ConnMysql().select_mysql(query_sql)[0]
        content = RequestMethod().to_requests(self.request_method, 'cell/delete', data=data)
        new_database_value = ConnMysql().select_mysql(query_sql)[0]
        return {
            'actualresult': content, 'cell_id': cell_id, 'old_database_value': 'deleted_at:' + str(old_database_value),
            'new_database_value': 'deleted_at:' + str(new_database_value), 'database_assert_method': False
        }


if __name__ == '__main__':
    CellTest().test_cell_test()