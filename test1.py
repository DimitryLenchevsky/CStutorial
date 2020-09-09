import datetime

class Interval:
    end = datetime.datetime.now()
    def __init__(self, start):
        self.start = start
    def get_len(self):
        return self.end - self.start

my_int = Interval(datetime.datetime(2018,12,12, 19,0,0))
print(my_int.get_len())