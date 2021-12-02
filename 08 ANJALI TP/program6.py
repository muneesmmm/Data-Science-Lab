from datetime import date
def numOfDays(date1,date2):
    return(date2-date1).days
date1=date(1998,12,5)
date2=date(2021,11,23)
print(numOfDays(date1,date2),"days")
