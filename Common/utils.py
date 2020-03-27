# encoding=utf-8
import time


def get_now(mode="s"):
    if mode == "s":
        return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))