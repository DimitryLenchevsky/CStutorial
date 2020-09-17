class Airplane:
    engines = 4
    def __init__(self, a, b):
        self.seats = a
        self.rows = b
    def start_engines(self):
        print(f'the airplane starts all {self.engines} engines, and all {self.seats} seats are occupied.')

airobus_a380 = Airplane(380, 2)
print(airobus_a380)
print(airobus_a380.engines)
print(airobus_a380.seats)
print(airobus_a380.rows)
print(airobus_a380.start_engines())