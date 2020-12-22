import re
import json
from Common.Request_method import RequestMethod
from Common.connect_mysql import ConnMysql
from Common.get_license import Linux
from Common.configure import *
# from Common.CLEARE_ENV import ClearEnv
from utils import wait_for
from Case.DeleteMySql import DeleteWords


class AgentTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']
        self.mysql = ConnMysql()
        self.linux = None

    def _copy_agent(self):
        agent_ip = self.params['agent_ip']
        agent_port = self.params['agent_port']
        ssh_port = self.params['ssh_port']
        agent_username = self.params['agent_username']
        agent_root_password = self.params['agent_root_password']
        agent_path = self.params['agent_path']
        tool_path = self.params['tool_path']
        Linux().linux_command("sshpass -p %s scp -r -P %s -o StrictHostKeychecking=no "
                                          "%s %s:%s/" % (
                                              agent_root_password, ssh_port, ZDBM_AGENT_PATH, agent_ip, agent_path),
                                          ip=ZDBM_PACKAGE_IP, port=ZDBM_PACKAGE_PORT,
                                          password=ZDBM_PACKAGE_PWD)
        self.linux = Linux()
        self.linux.connect(ip=agent_ip, port=ssh_port, password=agent_root_password)
        self.linux.linux_tar("{}/{} -C {}".format(agent_path, ZDBM_AGENT_NAME, agent_path))
        self._start_agent(agent_ip, agent_port, tool_path, IP, agent_username,
                          target=agent_path + "/install_client/install.yaml", agent_path=agent_path)

    def _start_agent(self, *args, **kwargs):
        self.linux.linux_echo("""
#install_mode: config,input
install_mode=config
local_ip={}
listen_port={}
tool_path={}
tag=
server_ip={}
install_user={}
install_group=oinstall
cluster_home=
""".format(*args), kwargs["target"])
        if 'Active: active (running)' in self.linux.linux_ssh_cmd("cd {}/install_client && sh install.sh".format(kwargs["agent_path"])):
            print("zdbm-agent安装成功")
        else:
            print("zdbm-agent安装失败")

    def test_agent_env_search(self):
        self._copy_agent()
        content = RequestMethod().to_requests(self.request_method, 'agent/list?isAdded=false&page=0')
        regex = "id\":(\d+)[^{}]*ip\":\"%s\"" % self.params['agent_ip']
        agent_id = re.findall(regex, content)[0]
        NEED_PARAMETER[self.params['agent_ip'] + "_id"] = agent_id
        return {
            'actualresult': content
        }

    def test_agent_env_test(self):
        content = RequestMethod().to_requests(self.request_method, 'agent/info/{}'.format(NEED_PARAMETER[self.params['ip'] + "_id"]))
        print(content)
        return {
            'actualresult': content
        }

    def test_agent_env_add(self):
        agent_env_id = NEED_PARAMETER[self.params['ip'] + "_id"]
        print("agent_id", agent_env_id)
        linux = Linux()
        linux.connect(self.params['ip'], "22", "oracle", "oracle")
        linux.lsnrctl_start()

        data = '{' + """"id": {0},
                    "envName": "{envName}",
                    "envType": "{envType}",
                    "ip": "{ip}",
                    "useSsh": false""".format(agent_env_id, **self.params)
        if self.params.get("asMdb"):
            data += ", \n \"asMdb\": {}".format(self.params['asMdb'])
        data += '}'
        content = RequestMethod().to_requests(self.request_method, 'env/add', data=data)
        print(content)
        result = json.loads(content)
        if 'm' not in self.params['envName']:
            software_id = result['data']['env']['softwares'][0]['id']
            NEED_PARAMETER.update({
                               self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                               self.params['envName'] + '_id': result['data']['env']['id'],
                               self.params['envName'] + '_softwares_id': software_id
                               })
            dbs_sql = 'select db_name, id from zdbm_orcl_env_databases where software_id={}'.format(software_id)
            dbs = self.mysql.select_mysql_new(dbs_sql, one=False, ac_re=True)
            for db in dbs:
                if db:
                    db_name, db_id = db
                    NEED_PARAMETER.update(
                            {self.params['envName'] + '_' + db_name + '_database_id': db_id}
                        )
        else:
            NEED_PARAMETER.update(
                {
                 self.params['envName'] + '_node_id': result['data']['env']['nodes'][0]['id'],
                 self.params['envName'] + '_id': result['data']['env']['id'],
                 self.params['envName'] + '_softwares_id': result['data']['env']['softwares'][0]['id'],

                 })
        print(NEED_PARAMETER)
        return {
            'actualresult': content
        }

    def test_agent_delete(self):
        pass


if __name__ == '__main__':
    AgentTest({
        "request_method": "put",
        "agent_ip": "192.168.12.1",
        "agent_port": "agent_port",
        "ssh_port": 22,
        "agent_username": "zdbm",
        "agent_root_password": "root1234",
        "agent_path": "/opt",
        "tool_path": "/opt/zdbm"
    })._copy_agent()
