import time
import jenkins
from Common.configure import *
from Common.get_license import GetLicense

class ComJenkins:

    def __init__(self):
        self.jenkins_ip = ZDBM_PACKAGE_IP
        self.job_name = 'zdbm_auto_page'
        self.server = jenkins.Jenkins('http://%s:8082' % self.jenkins_ip, username='admin', password='admin')

    def build_job(self):
        print(self.server.build_job(self.job_name))
        # print(self.build_status())
        times = 600
        time.sleep(10)
        while 1:
            status = self.build_status()
            if status == 'SUCCESS':
                print('自动打包任务构建成功')
                break
            elif status == 'FAILURE':
                print('自动打包任务构建失败')
                break
            times -= 2
            print('已经开始构建自动打包%ss  任务状态%s ' % (600-times+10, status))
            time.sleep(2)

    def build_status(self):
        number = self.server.get_job_info(self.job_name)['lastBuild']['number']
        status = self.server.get_build_info(self.job_name, number)['result']
        return status

if __name__ == '__main__':
    ComJenkins().build_job()
