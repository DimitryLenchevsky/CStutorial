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


class Tank:
    size = "big"
    def __init__(self, a, b):
        self.name = a
        self.power = b
    def shoot(self):
        print(f'The {self.name} tank shoots')
        tank.reloading()
    def reloading(self):
        print(f'The {self.name} is realoding its {self.power} ammo')

tank = Tank('t-34', 'powerfull')
print(tank.shoot())