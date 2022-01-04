#The datetime module supplies classes for manipulating dates and times.#
from datetime import date 
fdate = date(2021, 4, 8)#raw input first date#
sdate = date(2022, 4, 8)#raw input seond date#
print("First Date",fdate)
print("Second Date",sdate)
print("Smallest date is ")
if fdate<sdate: # comparison #
    print(fdate)
else:
    print(sdate)

