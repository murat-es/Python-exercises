def isLapYear(year):
    if (year%400==0 or (year%100!=0 and year%4==0)):
        return True

def calculateDay(month,day,year):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(isLapYear(year)):
        days[1]=29

    if(days[month-1]<day):
        raise ValueError(f'{month}th month of year does not contains {day} days')

    countDay=0
    for i in range(month):
        if(i==month-1):
            countDay+=day
            break
        countDay+=days[i]

    return countDay
    
print(calculateDay(1,111,2020))