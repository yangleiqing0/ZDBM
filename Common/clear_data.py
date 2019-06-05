import os


class ClearData:

    def __init__(self):
        pass

    @staticmethod
    def clear_txt():
        os.remove(r'../Data/ZDBM接口测试结果.txt')