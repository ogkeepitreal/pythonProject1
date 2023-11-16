


#2 # Write a program to print yesterdays, today and tomorrow dates
from datetime import datetime, timedelta

today = datetime.today().date()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(f"Yesterday date: {yesterday}")
print(f"Today date: {today}")
print(f"Tomorrow date: {tomorrow}")

#3 # Write a program to convert given timestamp to dd.mm.yyyy format
from datetime import datetime

some_day = 1014163200
date_obj = datetime.fromtimestamp(some_day)
formated_date = date_obj.strftime('%d.%m.%Y')

print(f"Date format DD.MM.YYYY: {formated_date}")

