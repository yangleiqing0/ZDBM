import json
import time
import datetime
from ZDBM.Common.Request_method import RequestMethod
from ZDBM.Common.connect_mysql import ConnMysql
from ZDBM.Common.connect_oracle import ConnOracle
from ZDBM.Common.configure import *
from ZDBM.Common.get_license import GetLicense




class VdbTest:

    def __init__(self, params=None):
        print(params)
        self.params = params
        self.request_method = self.params['request_method']

    def test_vdb_add(self):
        #  添加VDB
        env_tag_name_sql = 'select tag from zdbm_orcl_envs where id=%s and deleted_at is null'% NEED_PARAMETER[self.params['MDB_NAME'] + '_id']
        env_tag_name = ConnMysql().select_mysql(env_tag_name_sql)[0]
        TAGNAME = ORACLE_TOOLPATH+'/'+env_tag_name
        vdbName = "vdb_" + self.params['vdbName']
        print('路径', TAGNAME)
        time.sleep(1)
        TIME_STAMP_sql = 'select full_backup_ended_at from zdbm_orcl_source_dbs where db_name="%s" and deleted_at is null' % self.params['dbName']
        TIME_STAMP = ConnMysql().select_mysql(TIME_STAMP_sql)[0]
        word = "白银".encode('utf-8').decode('latin1')
        data = '{"envID":%s,"softwareID":%s,"sourceID":%s,"timestamp":"%s","vdbName":"%s",' \
               '"tacticParam":{"name":"%s_%s","vdbRetainDay":60,"snapshotIntervalHour":12,"snapshotRetainDay":60},"contactID":0,"parameters":' \
               '[{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_files","value":"4000","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"compatible","value":"11.2.0.4.0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_create_file_dest","value":"%s/%s/datafile","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_recovery_file_dest_size","value":"500G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"memory_max_target","value":"8G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"memory_target","value":"8G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"sga_max_size","value":"4G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"sga_target","value":"4G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_cache_advice","value":"off","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_cache_size","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"shared_pool_size","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"streams_pool_size","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"java_pool_size","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"large_pool_size","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"pga_aggregate_target","value":"2G","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"open_cursors","value":"300","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"remote_listener","value":"","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_domain","value":"","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"dispatchers","value":"(PROTOCOL=TCP) (SERVICE=orclXDB)","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"fast_start_mttr_target","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"log_archive_dest_1","value":"","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"log_archive_dest_state_1","value":"enable","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"processes","value":"5000","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"global_names","value":"FALSE","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"local_listener","value":"","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"open_links","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_file_multiblock_read_count","value":"44","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"fast_start_parallel_rollback","value":"LOW","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"job_queue_processes","value":"0","parameterType":"ADVISE_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_name","value":"%s","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_block_size","value":"8192","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"control_files","value":"%s/%s/datafile/controlfile.ctl","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_unique_name","value":"%s","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"instance_name","value":"%s","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"undo_tablespace","value":"UNDOTBS1","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"core_dump_dest","value":"%s/%s/cdump","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"diagnostic_dest","value":"%s/%s/diagnostic","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"audit_file_dest","value":"%s/%s/adump","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"audit_trail","value":"NONE","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"audit_sys_operations","value":"FALSE","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"db_recovery_file_dest","value":"%s/%s/datafile","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"remote_login_passwordfile","value":"EXCLUSIVE","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"instance_number","value":"1","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"cluster_database","value":"FALSE","parameterType":"CANNOT_EDIT"},' \
               '{"createdAt":"0001-01-01T00:00:00Z","updatedAt":"0001-01-01T00:00:00Z","name":"thread","value":"0","parameterType":"CANNOT_EDIT"}]}' % \
               (
                NEED_PARAMETER[self.params['MDB_NAME'] + '_id'], NEED_PARAMETER[self.params['MDB_NAME'] + '_softwares_id'],
                NEED_PARAMETER[self.params['envName'] +'_'+self.params['dbName'] + '_source_id'],TIME_STAMP, vdbName, word, vdbName, TAGNAME,vdbName,self.params['dbName'], TAGNAME, vdbName, vdbName, vdbName,
                TAGNAME, vdbName, TAGNAME, vdbName, TAGNAME, vdbName, TAGNAME, vdbName
                )
        content = RequestMethod().to_requests(self.request_method, 'vdb/add', data=data)
        result = json.loads(content)
        NEED_PARAMETER.update({
            self.params['envName'] + '_' + self.params['dbName'] + '_vdb_id': result['data']['vdb']['id']
        })
        vdb_status_sql = 'select open_mode from zdbm_orcl_virtual_dbs where id=%s' % NEED_PARAMETER[self.params['envName'] + '_' + self.params['dbName'] + '_vdb_id']
        archive_time = 5 * 60  # 5分钟
        time.sleep(2)
        while 1:
            vdb_status = ConnMysql().select_mysql(vdb_status_sql)[0]
            print(self.params['vdbName'], 'vdb状态：', vdb_status, '时间过去：', 300-archive_time, '秒')
            if vdb_status == 'READ WRITE':
                break
            if archive_time == 0:
                content = self.params['vdbName']+'VDB状态是%s 非READ WRITE' % vdb_status
                break
            else:
                archive_time -= 2
                time.sleep(2)
                continue
        return {
            'actualresult': content, 'vdbName': self.params['vdbName']
        }

    def test_vdb_snapshot_add(self):
        # 添加VDB快照,先获取一次DEPT表内的时间戳
        snap_name = "快照 ".encode('utf-8').decode('latin1') + (time.strftime("%Y-%m-%d %H:%M:%S"))
        vdb_id_sql = 'select id,vdb_name from zdbm_orcl_virtual_dbs where open_mode="READ WRITE" and deleted_at is ' \
                     'null and db_name= "%s" order by id desc' % self.params['dbName']
        name = self.params['description'].encode('utf-8').decode('latin1')
        vdb_id, vdb_name = ConnMysql().select_mysql(vdb_id_sql)
        data = '{"vdbID":%s,"name":"%s","description":"%s"}' % \
               (vdb_id, snap_name, name)
        content = RequestMethod().to_requests(self.request_method, 'vdb/snapshot/add', data=data)
        result = json.loads(content)
        NEED_PARAMETER.update({
            'vdb'+'_' + self.params['dbName']+'_name': vdb_name, 'snapshot'+'_' + self.params['dbName']+'_id': result['data']['snapshot']['id'], 'vdb'+'_' + self.params['dbName']+'_id': vdb_id
        })
        return {
            'actualresult': content, 'description': self.params['description']
        }

    def test_vdb_reset(self):
        # 重置VDB
        ConnOracle(ip=self.params['MDB_IP'], user=self.params['ORACLE_USER'],pwd=self.params['ORACLE_PASSWORD'],
                   oracle_name=NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name']).new_table()

        old_database_value = ConnOracle(ip=self.params['MDB_IP'], user=self.params['ORACLE_USER'], pwd=self.params['ORACLE_PASSWORD'],
                                        oracle_name=NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name']).selcet_oracle('select content from DEPT')[0]
        data = '{"snapshotID":%s}' % NEED_PARAMETER['snapshot'+'_' + self.params['dbName']+'_id']
        content = RequestMethod().to_requests(self.request_method, 'vdb/reset/%s' % NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_id'], data=data)
        status_sql = 'select job_status from zdbm_jobs where vdb_name="%s" order by id desc limit 1' % (NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name'])
        archive_time = 5 * 60  # 5分钟
        content_sql = 'select err_msg from zdbm_jobs where vdb_name="%s" order by id desc limit 1' % (NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name'])
        time.sleep(2)
        while 1:
            status = ConnMysql().select_mysql(status_sql)[0]
            print(NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name'], 'VDB重置状态：', status,'时间过去：', 300-archive_time, '秒')
            archive_time -=2
            if status == 'PROCESSING':
                time.sleep(2)
                continue
            elif status == 'FAILURE':
                content = ConnMysql().select_mysql(content_sql)[0]
                break
            elif status == 'SUCCESS':
                break
            if archive_time == 0:
                content = '归档状态异常，5分钟未恢复'
                break
        ConnOracle(ip=self.params['MDB_IP'], user=self.params['ORACLE_USER'],pwd=self.params['ORACLE_PASSWORD'],
                   oracle_name=NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name']).insert_dept()
        new_database_value = \
        ConnOracle(ip=self.params['MDB_IP'], user=self.params['ORACLE_USER'],pwd=self.params['ORACLE_PASSWORD'], oracle_name=NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name']).selcet_oracle('select content from (select * from DEPT order by id desc) where rownum < 2')[0]
        return {
            'actualresult': content, 'old_database_value': 'oracle_value:' + old_database_value,
            'new_database_value': 'oracle_value:' + new_database_value, 'database_assert_method': False
        }

    def test_recovery_preset_by_vdb(self):
        # 预生成通过vdb全量恢复源库需要的参数
        data = '{"vdbID":%s,"targetDir":"%s"}' % (NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_id'], MDB1_V2P_PATH)
        content = RequestMethod().to_requests(self.request_method, 'recovery/preset/by/vdb', data=data)
        print(content)
        return {
            'actualresult': content
        }

    def test_v2p(self):
        # 通过vdb全量恢复源库
        # 先创建路径
        GetLicense().linux_command('mkdir -p /home/oracle/v2p')
        # 给予此文件夹添加所有人和组
        GetLicense().linux_command('chown -R oracle:oinstall /home/oracle/v2p')
        # 通过test_recovery_preset_by_vdb方法获得提交的参数
        parameters = self.test_recovery_preset_by_vdb()
        if json.loads(parameters['actualresult'])['data']['canParameters'] is None:
            parameters = json.loads(parameters['actualresult'])['data']['adviseParameters'] + \
                         json.loads(parameters['actualresult'])['data']['cannotParameters']
        else:
            parameters = json.loads(parameters['actualresult'])['data']['adviseParameters'] + \
                         json.loads(parameters['actualresult'])['data']['cannotParameters'] + \
                         json.loads(parameters['actualresult'])['data']['canParameters']
        print('parameters:', parameters)
        data = '{"vdbID":%s,"targetSoftwareID":%s,"targetDir":"%s","parameters":%s}' % \
               (NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_id'], NEED_PARAMETER[MDB1_NAME+'_softwares_id'],MDB1_V2P_PATH,str(parameters).replace('\'', '\"'))
        print('data:', data)
        content = RequestMethod().to_requests(self.request_method, 'recovery/full/by/vdb', data=data)
        job_status_sql = 'select job_status from zdbm_jobs where vdb_name="%s" and job_type="RECOVERY_V2P" and deleted_at is null order by id desc' % \
                         NEED_PARAMETER['vdb'+'_' + self.params['dbName']+'_name']
        time.sleep(2)
        times = 5 * 60  # 5分钟
        while 1:
            job_status = ConnMysql().select_mysql(job_status_sql)[0]
            print("V2P恢复状态: ", job_status, '时间过去：', 300 - times, '秒')
            times -= 2
            if job_status == 'FAILURE':
                content = 'V2P恢复失败'
                break
            if times == 0:
                content = "5分钟内V2P未恢复成功"
                break
            elif job_status == 'SUCCESS':
                break
            else:
                time.sleep(2)
                continue

        return {
            'actualresult': content
        }

