class Car: # класс
    wheels = 4 # свойство класса
    def __init__(self, model, engine_volume): # основной сметод с инициализацией
        self.model = model
        self.__engine__ = engine_volume
    def ready(self): # метод
        print("The {} car with {} engine volume is ready to drive!!!" .format(self.model, self.__engine__))
    def start_engine(self): # метод
        print("Model {} has started the engine, wroom wroom!!!" .format(self.model))
    def drive(self):  # метод
        print("{} is driving now" .format(self.model))

car = Car("Ferari", 5.5)
print(car.ready())
print(car.start_engine())
print(car.drive())

