import re
from typing import List, Any

limit = int(input())  # искомое число

i = 0
i_dig = {i for i in range(1, 99)}  # исходный массив
i_str = (",".join(map(str, i_dig)))

i = 0
i_limit_dig = {i for i in range(1, (limit + 1))}  # строка - шаблон
i_limit_str = (",".join(map(str, i_limit_dig)))
# print(11, i_limit_dig) Контролька
# print(22, i_limit_str)
i_fin = re.findall('|'.join(i_str), i_limit_str)  # вывод от 1 до limit
# print(33, *i_fin)
print(*i_fin)
