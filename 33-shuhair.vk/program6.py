from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
print("First Date",f_date)
print("Second Date",l_date)
print("Earlier Date is:")
if f_date<l_date:
    print(f_date)
else:
    print(l_date)
    
