class Car:
    wheels = 4
    def __init__(self, model, engine_volume):
        self.model = model
        self.__engine__ = engine_volume
    def ready(self):
        print("The {} car with {} engine volume is ready to drive!!!" .format(self.model, self.__engine__))
    def start_engine(self):
        print("Model {} has started the engine, wroom wroom!!!" .format(self.model))
    def drive(self):
        print("{} is driving now" .format(self.model))

car = Car("Ferari", 5.5)
print(car.ready())
print(car.start_engine())
print(car.drive())

