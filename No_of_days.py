'''Program to find no of days between given two date in YYYY-MM-DD format considering leap year
    and no time travel'''
def  isLeapYear(year):
    if (year%4==0 or year%400==0 and year%100!=0):
        return True
    else:
        return False

def daysInMonth(year,month):
    if (month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        return 31
    if month==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 30


    
def nextDay(year,month,day):
    if day<daysInMonth(year,month):
        return year,month,day+1
    else:
        if month==12:
            return year+1,1,1
        else:
            return year,month+1,1

def dateIsBefore(from_year,from_month,from_day,to_year,to_month,to_day):
    #Return True if from_date>to_date else return false
    if(from_year<to_year):
        return True
    if(from_year==to_year):
        if (from_month<to_month):
            return True
        if(from_month==to_month):
                return from_day<to_day
    return False

def dayBetweenDates(from_year,from_month,from_day,to_year,to_month,to_day):
    assert not dateIsBefore(to_year,to_month,to_day,from_year,from_month,from_day)
    days=0;
    while dateIsBefore(from_year,from_month,from_day,to_year,to_month,to_day):
        from_year,from_month,from_day=nextDay(from_year,from_month,from_day)
        days+=1
    return days


#print (dayBetweenDates(2011,12,31,2012,12,31))
