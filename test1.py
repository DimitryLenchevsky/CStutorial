class Dog:
    paws = 4
    def __init__(self, a, b):
        self.name = a
        self.age = b
    def bark(self, times):
        print(f'The dog {self.name} at the age of {self.age} can bark {times} times')

    def run(self):
        print(f'The {self.name} runs!')
        dog.bark(3)
        

dog = Dog('Шарик', 3)
print(dog.age, dog.name)
print(dog.run())