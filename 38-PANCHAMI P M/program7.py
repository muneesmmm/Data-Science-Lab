from datetime import date,timedelta
today_date=date.today()
print("current date:",today_date)
td=timedelta(5)
print("before 5 days the date will be:",today_date-td)
