import datetime
import pytz

timezone = pytz.timezone('Europe/Minsk')
print(timezone)

cdt = datetime.datetime.now()
print(cdt)
print(type(cdt))
d = datetime.datetime(2020, 5, 26)
print(d)