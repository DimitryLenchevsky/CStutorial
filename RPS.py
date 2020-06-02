class Dog:

    paws = 4
    def __init__(self, a, b):
        self.name = a
        self.age = b

dog = Dog('Белка', 3)
dog1 = Dog('Стрелка', 4)
c = Dog('Полина', 10)

#print(dog.name, dog.age, "годика")
#print(dog1.name, dog1.age, "годика")
print(c.name, c.age, 'годиков')

dog.i_wasnt_here = 'string'
print(dog.i_wasnt_here)


print(dog.paws)