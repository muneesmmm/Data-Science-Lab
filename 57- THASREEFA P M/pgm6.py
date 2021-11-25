from datetime import date
fdate = date(2020, 4, 8)
sdate = date(2021, 4, 8)
print("First Date",fdate)
print("Second Date",sdate)
if fdate<sdate:
    print("The earlier date : ",fdate)
else:
    print("the earlier date : ",sdate)
