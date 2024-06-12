import re
from typing import List, Any

limit = int(input())
i_dig = {i for i in range(1, 99)}
i_str = (", ".join(map(str, i_dig)))
# i_fin = re.findall(r'(.[0-9])'
#                        r'(.[0-4][0-5])', i_str)
i_fin: list[Any] = re.findall(r'(.[0-4][0-5])', i_str)
print(*i_fin)
