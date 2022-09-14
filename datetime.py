import datetime

now = datetime.datetime.now()
day_of_year=(now-datetime.datetime(now.year,1,1)).days+1
print(day_of_year)

today=datetime.datetime.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)

print('Yesterday',yesterday)
print('Today',today)
print('Tomorrow',tomorrow)
print('_____')
for x in range(0,5):
    print(today+datetime.timedelta(days=x))
