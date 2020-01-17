from Common.configure import *


class GetHodeResult:

    def __init__(self):
        pass

    @staticmethod
    def get_hode_result(hode_result, value):
        if "$" in hode_result:
            print("1", value, hode_result, hode_result[1:])
            last_result = '无效的参数'
            # last_result = value.get('name', eval('name'))
            try:
                if eval(hode_result[1:]):
                    last_result = eval(hode_result[1:])
            except NameError as e:
                print('取预期参数失败:',e)
            hoderesult = value.get(hode_result[1:], last_result)
            print(hoderesult)
            return hoderesult
        return hode_result
