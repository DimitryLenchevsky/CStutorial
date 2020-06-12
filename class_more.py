class Car:
    def __init__(self, color):
        self.color = color
    def run(self):
        return "Runs"
    def stop(self):
        return "Stops"
    def __privat(self):
        return "dddd"

# Наследование класса Car
class Passcar(Car):
    def open_trunk(self):
        return "Trunk is opened"

# В потомке методы можно переопределять и унаследоваться от предыдущего наследника
class Lorry(Passcar):
    def open_trunk(self):
        return "Trunk is very big and opened"

# Можно в потомку переписать или добавить методы класса, для потомка
class Tank(Car):
    def __init__(self, wheels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wheels = wheels

    def run(self, *args, **kwargs):
        run_type = super().run(*args,**kwargs)
        return run_type + " " + "slowly"


c = Car('red')
pc = Passcar('blue')
lc = Lorry('white')
t = Tank(6, 'green')
print(c.color)
print(pc.color)
print(lc.color)
print(pc.open_trunk())
print(lc.open_trunk())
print(t.color)
print(t.run())
print(t.wheels)
