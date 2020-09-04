# Script to get different in data

from  datetime import date


today = date.today()

nyd = date(2022,6,30)

print(today)
print(nyd)

print("difference in days is " , (nyd-today).days)