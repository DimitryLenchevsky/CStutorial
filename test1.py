import datetime

class Interval:
    end = datetime.datetime.now()
    def __init__(self, start):
        self.start = start
    def begin(self):
        return self.end - self.start

num = Interval(datetime.datetime(2019,4,26, 19,0,0))
print(num.begin())