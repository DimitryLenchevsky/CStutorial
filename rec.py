import datetime
import pytz

#timezone
timezone = pytz.timezone('Europe/Minsk')
print(timezone)

#преобразования из/в строку
tn = datetime.datetime.now()
print(type(tn))

str_tn = tn.strftime('%d.%Y.%A %H.%M.%S')
print(str_tn)

