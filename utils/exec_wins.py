import os


def con_wins(api):
    print("执行的命令如下：", api)
    try:
        with os.popen(api) as result:
            print("con_wins:", result.read())
            return result.read()

    except Exception as e:
        print("con_wins error:", e)
        return "{}".format(e)
