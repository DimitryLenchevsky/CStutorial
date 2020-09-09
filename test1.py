class Dog:
    paws = 4
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.__address = address
    def sed_dog(self):
        print('Сообщение было отправлено по адресу {}'.format(self.__address))

dog = Dog('Шарик', 26, 'Лазо 16')
print(dog.sed_dog())