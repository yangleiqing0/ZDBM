# encoding=utf-8
import time
from Common.connect_mysql import ConnMysql
delay = 5


def look_select(sql, success):
    re = ConnMysql().select_mysql_new(sql)
    return re == success


def wait_for(func, *args, seconds=600, **kwargs):
    while seconds > 0:
        seconds -= delay
        try:
            re = func(*args, **kwargs)
            print("本次运行结果：", re)
            if re:
                return True

        except Exception as err:
            print("wait_for {} error: {}".format(func.__name__, err))

        finally:
            time.sleep(delay)
            print("sleep {}  then run".format(delay))
    return False
