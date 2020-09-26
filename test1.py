phone_book = {}

while True:
    name = input('Введите пожалуйста имя пользователя ... ')
    phone_number = int(input('Введите пожалуйста номер телефона '))
    phone_book[name] = phone_number
    print('Запись в телефонную книгу добавлена')
    answer = input('Если вы желаете больше не добавлять номера - введите stop, если еще введем пользователя - нажмите enter')
    if answer == 'stop':
        break



# sort - это метод списка
# sorted - это встроенная функция
a = [-4, 5, 300, 136, -469, 235, 2]
b = 'hello world'
c = ('albatros', 'trosablat', 'salbatros', 'solbatras')
c = sorted(c, reverse=True)
print(c) 