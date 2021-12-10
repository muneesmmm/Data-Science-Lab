from datetime import date
def numOfDays(date1,date2):
    return(date2-date1).days
date1=date(2019,1,25)
date2=date(2019,2,25)
print(numOfDays(date1,date2),"days")
