class Car:
    wheels = 4
    def __init__(self, a, b):
        self.color = a
        self.engine_volume = b
    def start_engine(self):
        return 'Wroom'


class Truck(Car):
    def open_trunk(self):
        return 'the trunk is opened'
    def __secret__(self):
        return 'secret'




man = Truck('red', 4.5)

print(man.open_trunk())
print(man.color)
print(man.__secret__())

