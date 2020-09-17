class Airplane:
    engines = 4
    def __init__(self, a, b):
        self.seats = a
        self.rows = b
    def start_engines(self):
        print(f'the airplane starts all {self.engines} engines, and all {self.seats} seats are occupied.')
    def take_off(self):
        print('The airplane took off')
    @property
    def landing(self):
        print('the airplane landed')

airbus_a380 = Airplane(380, 2)
print(airbus_a380)
print(airbus_a380.engines)
print(airbus_a380.seats)
print(airbus_a380.rows)
print(airbus_a380.start_engines())
print(airbus_a380.take_off())
print(airbus_a380.landing)