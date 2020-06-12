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

