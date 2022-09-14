import datetime
import time

print(datetime.date(2022,9,9).isocalendar()[1])

milli_sec=int(round(time.time()*1000))
print(milli_sec)

a=datetime.date(1991,8,11)
b=datetime.date(2020,11,20)
print(b-a)

def all_sundays(year):
    dt=datetime.date(year,1,1)
    dt+=datetime.timedelta(days=6-dt.weekday())
    while dt.year==year:
        yield dt
        dt+=datetime.timedelta(days=7)
for s in all_sundays(1991):
    print(s)
