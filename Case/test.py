
import sys
__import__('ZDBM.Case.'+'Env_test')
m = sys.modules['ZDBM.Case.'+'Env_test']
t = getattr(m, 'EnvTest')
method = getattr(t({'request_method': 'post'}), 'test_env_database_add')
value = method()
# except Exception as e:
#     value = e
# print(value)
actualresult = value['actualresult']