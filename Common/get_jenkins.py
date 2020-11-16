import time
from Common.configure import *
from Common.get_license import Linux


class GetJenkins:

    def __init__(self):
        pass

    def get_jenkins(self):
        # 先清除192.168.12.50服务器上的镜像和容器
        Linux().linux_command(
            'docker stop myjenkins && docker rm myjenkins && docker rmi myjenkins:v3 && rm -rf myjenkins.tar')

        Linux().linux_command('sshpass -p %s scp -o StrictHostKeychecking=no '
                                   '/soft/%s root@%s:/opt && echo "scp OK"' %
                                   (ROOT_PASSWORD, MY_JENKINS_NAME, IP), ip=ZDBM_PACKAGE_IP, port=ZDBM_PACKAGE_PORT,
                                   password=ZDBM_PACKAGE_PWD)
        Linux().linux_command('cd /opt && docker load -i %s && '
                                   'docker run -d -it -p 8082:8080 -p 50000:50000 -u root  --name myjenkins '
                                   'myjenkins:v3 /start.sh && '
                                   'echo "start OK"' % MY_JENKINS_NAME)


# docker stop myjenkins && docker rm myjenkins && docker rmi myjenkins:v1 && rm -rf myjenkins.tar


if __name__ == '__main__':
    GetJenkins().get_jenkins()
