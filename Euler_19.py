'''

Euler Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''
firsts = [1,32,60,91,121,152,182,213,244,274,305,335]
firsts = [1,32,61,92,122,153,183,214,245,275,306,336]

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
week = {'Monday':'Tuesday','Tuesday':'Wednesday',
        'Wednesday':'Thursday','Thursday':'Friday','Friday':'Saturday',
        'Saturday':'Sunday','Sunday':'Monday'}
startingDay = 'Tuesday'

def findSundaysOnFirst(year, isLeapYear, first):
    sundays = 0
    if isLeapYear:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
        firsts = [1,32,61,92,122,153,183,214,245,275,306,336]    
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        firsts = [1,32,60,91,121,152,182,213,244,274,305,335]

    day = first
    for i in range(1, sum(months)+1):
        if i in firsts:
            if day == "Sunday":
                sundays += 1

        day = week[day]
        
    return sundays, day

def is_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

sundays = 0
for i in range(1901,2001):
    s, startingDay = findSundaysOnFirst(i,is_leapyear(i),startingDay)        
    sundays += s
    
print sundays
