#   refer program 6 for details about date time
from datetime import date, timedelta
#   timedelta - A duration expressing the difference between two date,
#   time, or datetime instances to microsecond resolution.
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)