class Dog:
    def __init__(self, a, b):
        self.name = a
        self.age = b

dog = Dog('Белка', 3)
dog1 = Dog('Стрелка', 4)

print(dog.name, dog.age, "годика")
print(dog1.name, dog1.age, "годика")