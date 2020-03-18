# # coding=utf-8
#
#
# class Dict(dict):
#     __setattr__ = dict.__setitem__
#
#
# def dict_to_object(dictObj):
#     if not isinstance(dictObj, dict):
#         return dictObj
#     inst = Dict()
#     for key, value in dictObj.items():
#         inst[key] = dict_to_object(value)
#     return inst
#
#
# def object_to_dict(object):
#     dic = {}
#     for column in object.__table__.columns:
#         dic[column.name] = str(getattr(object, column.name))
#
#     return dic
#
#
# data = {
#   "access_token": "ACCESS_TOKEN",
#   "app_id": "APP_ID",
#   "data": ["bb", "aa"],
#   "data_table": {"bb": "bb", "aaa": "aaa", "a1": "a1"},
#   "game_id": "GAME_ID",
#   "nonce": "123456789ABC",
#   "timestamp": 1575957433,
#   "version": "1.0"
# }
#
# data_keys = sorted(data)
# query_str = ""
#
#
# def sort_dict(_dict):
#     _dict_keys = _dict.keys()
#     sorted(_dict_keys)
#     return _dict_keys
#
#
# for d in data_keys:
#     if isinstance(data[d], dict):
#         d_keys = sort_dict(data[d])
#         for d1 in d_keys:
#             query_str += "&{}[{}]={}".format(d, d1, data[d][d1])
#     elif isinstance(data[d], list):
#         for d2 in range(len(data[d])):
#             query_str += "&{}[{}]={}".format(d, d2, data[d][d2])
#     else:
#         query_str += "&{}={}".format(d, data[d])
# query_str = query_str.replace("&", "", 1)
# print(query_str)
#
#
a = [1, 2, "a", 3]
for i in a:
    try:
        print(int(i))
    except Exception as e:
        print(e)
#

print(list(set(a)))

a = "1"
print(a.isdigit())