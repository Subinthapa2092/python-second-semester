#### Python Programmed :: 

import datetime
x = datetime.datetime.now()
print(x.strftime("%A")) # string format time-i.e. Sunday
print(x.strftime("%a")) # string format time-i.e. Sun
print(x.strftime("%w")) # string format time for weekday[0-6]
print(x.strftime("%d")) # string format time for day[1-31]
print(x.strftime("%b")) # string format time for Month name short-Jan
print(x.strftime("%B")) # string format time for Month name short-January
print(x.strftime("%m")) # string format time for Month number[01-12=-01
print(x.strftime("%y")) # string format time for year short century-23
print(x.strftime("%Y")) # string format time for year full century-2023
print(x.strftime("%H")) # string format Hour[00-23] -18
print(x.strftime("%I")) # string format Hour[00-12] -06
print(x.strftime("%p")) # string format AM/PM -18
print(x.strftime("%M")) # string format Minutes[00-59] -51
print(x.strftime("%S")) # string format Seconds[00-59] -26
print(x.strftime("%f")) # string format Microsecond [000000-999999]
print(x.strftime("%j")) # string format Day number of year [001-366]
print(x.strftime("%U")) # Week number of yr, Sun as the first day of week[00-53]
print(x.strftime("%W")) # Week number of yr, Mon as the first day of week[00-53]
print(x.strftime("%c")) # Local version of date and time[Mon Dec 31 17:41:00 2022]
print(x.strftime("%C")) # Century [20]
print(x.strftime("%x")) # Local version of date [12/31/22]
print(x.strftime("%X")) # Local version of time [17:41:00]
print(x.strftime("%%")) # to print %
