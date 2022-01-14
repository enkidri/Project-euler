#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

months={
'jan': 31,
'feb': 28,
'mars': 31,
'april': 30,
'may': 31,
'june': 30,
'july': 31,
'aug': 31,
'sep': 30,
'oct': 31,
'nov': 30,
'dec': 31,
}
monthOrder=['jan', 'feb', 'mars', 'april', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']

startDate=datetime.datetime(1901, 1, 1)
endDate=datetime.datetime(2000, 12, 31)
currentDate=datetime.datetime(1901, 1, 1)
totSunday=0

while currentDate<endDate:
    if currentDate.year % 4==0 or (currentDate.year / 100 == 0 and currentDate.year % 400 ==0):
        months['feb']=29
    elif months['feb']!=28:
        months['feb']=28

    for month in monthOrder:
        monthDays=months[month]
        nextMonth=datetime.timedelta(days=monthDays)
        currentDate=currentDate+nextMonth
        dayOfWeek=currentDate.weekday()
        if dayOfWeek==6:
            totSunday+=1
        else:
            continue
print(f'Total nr of months starting with sun between {startDate} and {endDate} is {totSunday}.')
