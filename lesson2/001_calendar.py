'''
import time

start = time.time()
#time.sleep(5)

print(time.asctime())
print(time.gmtime())
print(time.localtime()[0])

stop = time.time()

print(stop - start)
'''
'''
import datetime

d = datetime.date(1988, 3, 16)
print(d)
print(type(d))

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print(type(today - d))
print(today - d)

#date1 - date2 = timedeltda
#date1 -/+ timedelta = date2

tdelta = datetime.timedelta(days=7)
print(tdelta)
print(type(tdelta))


import datetime

dt = datetime.datetime(2023, 10, 24, 17,23,45)
#print(dt.date())
#print(dt.time())
tdelta = datetime.timedelta(days=5, hours=12, minutes=37)

#print((dt - tdelta).time())

today = datetime.datetime.now()
print(today)

ts = 574525800
ts_date = datetime.date.fromtimestamp(ts)
print(ts_date)
'''
import datetime

today = datetime.datetime.today()

today_str = today.strftime('%A, %d. %B %Y')
print(today_str)

date_str = ('24.10.23 20:20:15')
d = datetime.datetime.strptime(date_str, '%d.%m.%y %H:%M:%S')

print(d)
print(type(d))