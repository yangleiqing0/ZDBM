import os


class ClearData:

    def __init__(self):
        pass

    @staticmethod
    def clear_txt():
        os.remove(r'../Data/ZDBM_test_result.txt')

if __name__ == '__main__':
    ClearData().clear_txt()