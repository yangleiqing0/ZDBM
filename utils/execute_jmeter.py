from utils.exec_wins import con_wins
from Common.configure import TEST_REPORT_TXT_NAME, ZDBM_VERSION, IP

Desk = r"C:\Users\yl\Desktop"
TarFolder = Desk + r'\reports'
ResultName = "result.jtl"


def clear_file():
    command = "del/f/s/q " + TarFolder + "\\" + ResultName
    con_wins(command)


def clear_folder():
    command = "rd/s/q " + TarFolder + "\\" + "http"
    con_wins(command)


def clear_env():
    clear_folder()
    clear_file()


def start():
    clear_env()
    command = r"jmeter -Jzdbm_ip={} -n -t {}\jmeter\ZDBM接口测试-v{}.jmx -l {}\{} -e -o {}\http".format(IP, Desk, ZDBM_VERSION, TarFolder, ResultName, TarFolder)
    con_wins(command)


def analysis_jmeter_report():
    # 读取本地报告html文件
    path = TarFolder + '\\' + ResultName

    with open(path, 'r', encoding='utf-8') as f:
        cases = f.readlines()[1:]

    lists = {}
    for case in cases:
        case = case.split(",")
        if case[2] not in lists.keys():
            re = "测试成功" if case[7] == "true" else "测试失败"
            test_case = {case[2]: {"t_description": case[2], "t_hope": "--", "t_actual": "--" if re == "测试成功" else case[8],
                                   "t_result": re, "old_database_value" : "--",
                                   "new_database_value": "--", 't_pkg': 'Jmeter', 't_object': 'Jmeter', 't_method':'Jmeter'}}
            lists.update(test_case)
            print(test_case)
    test_cases = list(lists.values())
    for t in range(len(test_cases)):
        if t == 0:
            test_cases[t] = str(test_cases[t])
        else:
            test_cases[t] = '\n' + str(test_cases[t])

    print(test_cases)

    with open(r'..\Data\%s.txt' % TEST_REPORT_TXT_NAME, 'a+', encoding='utf-8') as f:
        f.writelines(test_cases)


if __name__ == '__main__':
    analysis_jmeter_report()
