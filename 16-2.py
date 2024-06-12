import re

limit = int(input())
i_dig = {i for i in range(1, (limit + 1))}
print(", ".join(map(str, i_dig)))
