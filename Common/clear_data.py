import os


class ClearData:

    def __init__(self):
        pass

    @staticmethod
    def clear_txt():
        try:
            os.remove(r'../Data/ZDBM_test_result.txt')
        except Exception:
            pass

    @staticmethod
    def clear_xlsx():
        try:
            os.remove(r'../Data/ZDBM_test_report.xlsx')
        except Exception:
            pass


if __name__ == '__main__':
    ClearData().clear_txt()