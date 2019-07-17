import re
ac = 1
ab = 2
a = '123123a${ac},1dwqdqw${ab}'
def get_value(i):
    try:
        i = eval(i)

    except Exception:
        pass
    return i


aa = ''.join([str(get_value(i)) for i in re.split('\${|}',a)])

print(aa)
