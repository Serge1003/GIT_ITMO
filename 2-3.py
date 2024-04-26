N = int(input('Вы ввели: '))
f: int = 1
for i in range(1, N):
    f = f * (i + 1)
    i += 1
print(f'Факториал числа {N}!:', f)
