from utils.exec_wins import con_wins

Desk = r"C:\Users\yl\Desktop"
TarFolder = Desk + r'\reports'


def clear_file():
    command = "del/f/s/q " + TarFolder + "\\" + "result.jtl"
    con_wins(command)


def clear_folder():
    command = "rd/s/q " + TarFolder + "\\" + "http"
    con_wins(command)


def clear_env():
    clear_folder()
    clear_file()


def start():
    clear_env()
    command = r"jmeter -n -t {}\ZDBM接口测试.jmx -l {}\result.jtl -e -o {}\http".format(Desk, TarFolder, TarFolder)
    con_wins(command)


if __name__ == '__main__':
    start()
