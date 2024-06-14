import re
from typing import List, Any

limit = int(input())
i_dig = {i for i in range(1, 99)}
print(i_dig)
i_str = (",".join(map(str, i_dig)))
i_fin1 = re.findall(r'(g\d)', i_str)
# i_fin1 = re.findall({'high': 45, 'low': 0}', i_str)
# r'([0-4][0-5])', i_str)
i_fin: list[Any] = re.findall(r'((?>[0123456789].))', i_str)
print(*i_fin1)
print(*i_fin)
