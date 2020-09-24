phone_book = {}

while True:
    name = input('Введите пожалуйста имя пользователя ... ')
    phone_number = int(input('Введите пожалуйста номер телефона '))
    phone_book[name] = phone_number
    print('Запись в телефонную книгу добавлена')
    answer = input('Если вы желаете больше не добавлять номера - введите stop, если еще введем пользователя - нажмите enter')
    if answer == 'stop':
        break

print(phone_book)