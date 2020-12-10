class Car: # класс
    wheels = 4 # свойство класса
    def __init__(self, model, engine_volume): # основной метод с инициализацией (данные ожидаются при вызове класса)
        self.model = model
        self.__engine__ = engine_volume
    def ready(self): # метод (данные уже вводятся по мере необходимости)
        print("The {} car with {} engine volume is ready to drive!!!" .format(self.model, self.__engine__))
    def start_engine(self): # метод (данные уже вводятся по мере необходимости)
        print("Model {} has started the engine, wroom wroom!!!" .format(self.model))
    def drive(self):  # метод (данные уже вводятся по мере необходимости)
        print("{} is driving now" .format(self.model))

car = Car("Ferari", 5.5)
print(car.ready())
print(car.start_engine())
print(car.drive())

print('#################################################################')
# Achtung
import datetime
class MyInterval:
    class_end = datetime.datetime.now() #классинициируется только 1 раз, поэтому class_end не будет обновляться и будет устаревшим

    def __init__(self, start):
        self.start = start

    def get_len(self):
        """
        returns length in days
        """
        return self.class_end - self.start

my_int = MyInterval(datetime.datetime(2020,5,27))

print('###################################################################')

# Наследование


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



class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_area(self):
        return self.a * self.b 


class Square:
    def __init__(self, a):
        self.a = a
    def get_area(self):
        return self.a**2

class Circle:
    def __init__(self, r):
        self.r = r
    def get_area(self):
        return 3.14 * self.r**2


