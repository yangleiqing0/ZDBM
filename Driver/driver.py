import glob
import xlrd
import sys
import time
from Common.assert_method import AssertMethod
from Common.do_report import Report
from Common.clear_data import ClearData
from Common.get_hode_result import GetHodeResult
from Common.get_params import GetParams
from Common.configure import *
from Common.command_jenkins import ComJenkins
from Common.initialize import Initialize
from Common.install_oracle import InstallOracle
from utils.execute_jmeter import start, analysis_jmeter_report


class Driver:

    def __init__(self):
        # self.tables = glob.glob(r'../Data/*test.xls')
        self.tables = glob.glob(r'../Data/*main_test.xls')
        # self.tables = glob.glob(r'../Data/*1.0.2_test.xls')
        # ClearData().clear_txt()

    @staticmethod
    def install_all():
        # ComJenkins().build_job()    # 触发jenkins自动打包
        Initialize().install_zdbm()   # 自动进行zdbm预安装和安装
        InstallOracle().install_oracle()   # 自动从12.10将oracle包scp到目标服务器的/u01

    def get_data(self):
        ClearData().clear_xlsx()
        # self.install_all()
        # print(self.tables)
        for table in self.tables:
            print(table)
            book = xlrd.open_workbook(table)
            for s in range((len(book.sheets()))):
                sheet = book.sheets()[s]
                for i in range(28, 30):
                # for i in range(1, sheet.nrows):
                    lis = sheet.row_values(i)
                    print("第{}次，参数为{}".format(i, lis))
                    print(lis[5])
                    lis[6] = lis[6].split(',')
                    assert_method, hode_result = lis[7].split(':', 1)
                    params_dict = {'request_method': lis[3]}   # 将请求的方法加入param_dict字典
                    params_dict = GetParams(params_dict, lis[6][0]).analysis_param()  # 通过解析参数得到参数字典
                    t_description = GetParams().analysis_describe(lis[4])  # 对备注进行解析
                    print("params_dict:", params_dict)
                    print("NEED_PARAMETER:", NEED_PARAMETER)
                    if lis[9] != 'n':
                        # try:
                        __import__('Case.'+lis[0])
                        m = sys.modules['Case.'+lis[0]]
                        t = getattr(m, lis[1])
                        method = getattr(t(params_dict), lis[2])
                        value = method()
                        # except Exception as e:
                        #     value = e
                        print("本次请求结果:", value)
                        actualresult = value['actualresult']
                        # print(actualresult, hode_result)
                        # print('试试',value)
                        hode_result = GetHodeResult().get_hode_result(hode_result, value)   # 期望结果解析
                        result = AssertMethod(actualresult, hode_result, assert_method,
                                              old_database_value=value.get('old_database_value', 1),
                                              new_database_value=value.get('new_database_value', 1),
                                              database_assert_method=value.get('database_assert_method', True)
                                              ).assert_database_result()
                        print(result)
                        with open(r'..\Data\%s.txt' % TEST_REPORT_TXT_NAME, 'a+', encoding='utf-8') as f:
                            f.write(str({'t_pkg': lis[0], 't_object': lis[1], 't_method': lis[2], 't_description': t_description,
                                         't_hope': assert_method+":" + hode_result
                                        , 't_actual': actualresult, 't_result': result,
                                         'old_database_value': value.get('old_database_value', ' '),
                                         'new_database_value': value.get('new_database_value', ' ')
                                         }) + '\n')
                        print('%s号测试    测试结果:%s   实际结果: %s ' % (lis[5], result, actualresult))
                    else:
                        continue
        self.to_report()

    @staticmethod
    def test_report():
        data = []
        m = 0
        with open(r'..\Data\%s.txt' % TEST_REPORT_TXT_NAME, 'r', encoding='utf-8') as f:
            result = f.readlines()
            result = result[::-1]
        for res in result:
            res = eval(res)
            if res['t_result'] == '测试成功':
                m += 1
            print(res['t_pkg'], res['t_object'], res['t_method'], res['t_description'], res['t_hope'], res['t_actual'], res['t_result'])
            content = {"t_pkg": res['t_pkg'],
                       "t_object": res['t_object'],
                       "t_method": res['t_method'],
                       "t_description": res['t_description'],
                       "t_result": res['t_result'],
                       "t_hope": res['t_hope'],
                       "t_actual": str(res['t_actual']),
                       "old_database_value": res['old_database_value'],
                       "new_database_value": res['new_database_value']
                       }
            data.append(content)
        data_title = {"test_name": "备份一体机", "test_version": ZDBM_VERSION, "test_pl": "win10", "test_net": "公司内网"}
        data_re = {"test_sum": (len(result)), "test_success": m, "test_failed": ((len(result)) - m),
                   "test_date": time.strftime("%Y-%m-%d  %H:%M:%S")}
        r = Report()
        print(len(result), m)
        r.init(data_title, data_re, int(m * 100 / len(result)))
        r.test_detail(data, len(result), len(data))

    def to_report(self):
        print('开始调用jmeter执行测试其他接口')
        start()
        print('jmeter执行测试接口')
        analysis_jmeter_report()
        self.test_report()
        print('测试完毕，测试报告生成完毕')
        ClearData().clear_txt()


if __name__ == "__main__":
    Driver().get_data()
    # Driver().to_report()
