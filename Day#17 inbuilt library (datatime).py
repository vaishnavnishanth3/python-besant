print("")
import Day17module
user=int(input("Enter the Number: "))

if user==1:
    Day17module.goa()
elif user==2:
    Day17module.ooty()
else:
    print('1 OR 2 ONLY')
print("")

import datetime
x=datetime.datetime.now()
print(x)
print("")

cur_second=x.strftime("%S")
print(cur_second)
print("")

cur_minute=x.strftime("%M")
print(cur_minute)
print("")

cur_hour=x.strftime("%H")
print(cur_hour)
print("")

cur_date=x.strftime("%d")
print(cur_date)
print("")

cur_day=x.strftime("%A")
print(cur_day)
print("")

cur_month=x.strftime("%B")
print(cur_month)
print("")

cur_month2=x.strftime("%m")
print(cur_month2)
print("")

cur_year=x.strftime("%Y")
print(cur_year)
print("")