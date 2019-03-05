#-*- coding: utf-8 -*-
"""
# datetime - робота з датою і часом
Класи для роботи з датою і часом. Містить класи `date` (дата), `time` (час), `datetime` (дата і час), `timedelta` (період часу), `tzinfo` (абстрактний клас для роботи з часовими поясами). Дозволяє виконувати різноманітні математичні операції над значеннями дати і часу.
"""
import datetime, time
d0=datetime.datetime.now() # поточна дата (datetime)
d1=datetime.datetime(2015,2,17,0,0,0,0) # задана дата (datetime)
print d0.year, d0.month, d0.day, d0.hour, d0.minute, d0.second, d0.microsecond, d0.tzinfo # атрибути datetime
st=d0.timetuple() # об'єкт (time.struct_time)
print time.mktime(st) # кількість секунд з початку Епохи
print datetime.datetime.strptime("Mon Apr 26 11:31:53 2010", "%a %b %d %H:%M:%S %Y").strftime("%d%M%Y") # конвертація з формату в формат
print d0.isoweekday() # ISO день тиждня (1 - понеділок)
print d1.replace(year=2014) # дозволяє змінити певні атрибути дати

# тут місяців і років немає, бо вони можуть мати різну к-сть днів
td1=datetime.timedelta(weeks=1,days=2,hours=1)
print td1.days, td1.seconds, td1.microseconds 
print d1+td1 # додати до дати період (datetime)
print d1+td1*2-abs(-td1) # допустимі операції (datetime)
td2=d0-d1 # різниця дат (datetime)
print d0>d1 # порівняння дат
print td1>td2 # порівняння періодів
# datetime знає про високосні роки:
print datetime.datetime(2016,3,1)-datetime.datetime(2016,2,28) # результат 2 дня
#print datetime.datetime(2015,2,29) # помилка!
