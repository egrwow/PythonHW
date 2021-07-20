proc = int(input('Количество прицентов:'))

if proc < 0:
    print('Ошибка, введите положительное число')
elif proc % 10 == 1 and proc % 100 != 11:
    print(proc, 'процент')
elif proc % 10 >= 2 and proc % 10 <= 4 and (proc % 100 < 10 or proc % 100 > 20):
    print(proc, 'процента')
else:
    print(proc, 'процентов')