import datetime
import pytz
import calendar

#timezone
timezone = pytz.timezone('Europe/Minsk')
print(timezone)

#преобразования из/в строку
tn = datetime.datetime.now()
print(type(tn))

#.strftime
str_tn = tn.strftime('%d.%Y.%A %H.%M.%S')
print(str_tn)

#.strptime
time_as_atring = "18.10.20 13:27"
time_obj = datetime.datetime.strptime("1810201327", "%d%m%y%H%M")
print(time_obj)

#calendar
wd = calendar.Calendar()
for d in wd.iterweekdays():
    print(d)