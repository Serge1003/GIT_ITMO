print('''При вводе денежных средств придерживайтесь формата: 0000.00
Окончание ввода: 0'''/n)
cash = list(iter(input, '0'))
n = len(cash)
summ = 0
for pay in cash:
    summ = summ + float(pay)
else:
    print(f'Средняя заработная плата: {summ/n} руб')