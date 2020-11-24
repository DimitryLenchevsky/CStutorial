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
        print('Найдено отрицательное число под индексом ', i)


x = [1, 2, 3, 4]
new_x = [i*i for i in x]
print(new_x)


x = [1, 2, 3, 4]
new_x_dict = {i : i*i for i in x}
print(new_x_dict)


x = [0, 2, 5, -2, -6, 3, 6, -1, 8]
non_negative_list = [i for i in x if i >= 0]
print(non_negative_list)


aaaaa = (i for i in range(1, 101) if i%2)
for square in aaaaa:
    print(square, )


cubic = {i : i**3 for i in range(11, 16)}
print(cubic)