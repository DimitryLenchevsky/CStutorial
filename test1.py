c = [x for x in range(0, 11)]
print(c)
b = (x for x in range(0, 11))
print(b)
it = iter(c)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
lst = (x for x in range(10000000000))
for i in lst:
    print(i, end=' ')
    if i > 100:
        break
    
print('\nnew loop')

for i in lst:
    print(i, end=' ')
    if i > 200:
        break


z = (x**2 for x in range(0, 11))
v = list(z)
print(v[::-1])


text = 'Рассматривается способ перебора элементов коллекций\n с помощью итераторов. Формирование значений через выражения-генераторы\n и функции-генераторы.Оператор yield. Функции iter и next.'
print(text)

def word_func(text):
    for i in text.split():
        yield i

for i in word_func(text):
    print(i)
    
