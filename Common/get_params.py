import re
from Common.configure import *
from Common.rand_name import RangName


class GetParams:

    def __init__(self, params_dict=None, lis=None):
        self.params_dict = params_dict
        self.lis = lis

    def analysis_param(self):
        print(self.lis, self.params_dict, type(self.params_dict))
        lis = self.lis.split('\n')
        for l in lis:
            param = l.replace(" ", "").split('=')
            if param[0] != '':
                print(param[1])
                if '$' in param[1]:
                    print({param[0]: param[1]})
                    param[1] = eval(param[1][1:])

                elif '随机' in param[1]:
                    param[1] = RangName().rand_str(param[1])
                self.params_dict.update({param[0]: param[1]})
        print(self.params_dict)
        return self.params_dict
        # [(self.params_dict.update({item.split('=')[0]: (item.split('=')[1])})) for item in lis[6] if '=' in item]

    @staticmethod
    def get_value(i):
        try:
            i = eval(i)
        except Exception:
            pass
        return i

    def analysis_describe(self, string):
        really_value = ''.join([str(self.get_value(i)) for i in re.split(r'\${|}', string)])
        print('用例介绍: ', really_value)
        return really_value

if __name__ == '__main__':
    GetParams().analysis_param(account=15155492421)