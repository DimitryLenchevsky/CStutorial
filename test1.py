somelist = [(2, 3), (5, 8), (1, 9)]
result = 0
for i in somelist:
    result = result = (i[0] + i[1])
    print(result)


somelist = [(2, 3), (5, 8), (1, 9)]
result = 0
for x, y in somelist:
    result = result + (x + y)
    print(result)


x = [0, 2, 5, -2, -6, 3, 6, -1, 8]
for i, n in enumerate(x):
    if n < 0:
        print('Найдено отрицательное число ао индексом ', i)