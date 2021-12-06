from datetime import date,timedelta
x=date(1997,4,9)
y=date(1997,5,8)
print ("date1 is: ",x)
print ("date2 is: ",y)
print ("The earliest date is ")
if x<y:
    print (x)
else:
    print (y)
