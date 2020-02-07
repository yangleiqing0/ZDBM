class Dict(dict):
    __setattr__ = dict.__setitem__


def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for key, value in dictObj.items():
        inst[key] = dict_to_object(value)
    return inst


def object_to_dict(object):
    dic = {}
    for column in object.__table__.columns:
        dic[column.name] = str(getattr(object, column.name))

    return dic


# a= {"a":1,'b':2}
# a = dict_to_object(a)
# a = object_to_dict(a)
# print(type(a))

# from datetime import datetime
# # print('时间：(%Y-%m-%d %H:%M:%S %f): ' , datetime.now().strftime( '%Y%m%d%H%M%S' ))
# print(datetime.now())

import xlsxwriter

xlsx = xlsxwriter.Workbook('a.xlsx')
xlsx.close()
