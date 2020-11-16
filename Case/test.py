a = '1li5155492421,'

import re


regex = '\d+'
result = "".join(re.findall(regex, a))
print(result)
