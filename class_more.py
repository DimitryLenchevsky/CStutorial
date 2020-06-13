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

# Множественное наследование
class Input:
    def can_input(self):
        return "I can input data"

class Output:
    def can_output(self):
        return "I can output data"

class InputOutput(Input, Output):
    pass

twoway = InputOutput()
inp = Input()
opt = Output()
print(inp.can_input())
print(opt.can_output())
print(twoway.can_input())
print(twoway.can_output())

# Миксин - просто добавляет еще 1 класс к множественному наследованию.
class MyMixin:
    def mixin_method(self):
        print('from mixin')

m = MyMixin()
class InputOutput(MyMixin, Input, Output):
    pass

ioo = InputOutput()
print(ioo.mixin_method())


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
