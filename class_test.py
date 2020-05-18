class Car:
    def __init__(self, model):
        self.model = model
    def start_engine(self):
        print("Model {} has started the engine, wroom wroom!!!" .format(self.model))
    def drive(self, speed):
        self.speed = speed
        print("Model is driving now {} km/h" .format(self.speed))

car = Car("Ferari123")
car.start_engine()
car.drive("30")
car.model
