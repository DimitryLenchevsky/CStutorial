class Dog:
    paws = 4
    def __init__(self, a, b):
        self.name = a
        self.age = b
    @property
    def month(self):
        return self.age * 12

dog = Dog('Шарик', 3)
print(dog.month())
dog.month = 45
print(dog.month())