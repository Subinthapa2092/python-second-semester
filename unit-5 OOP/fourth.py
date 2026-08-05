#### python in a program to take nothing's 
def minimum(*n):
    print(n)## n is a tuple 
    if n: 
        mn = n[0]
    for value in n[1:]:
        if value <mn:
            mn = value 
        print(mn)
minimum(1,3,-7,9)
minimum()
### **
"""
    WAp to subract two time objects using oop(use class method decorator )
    """
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def subtract_times1(cls, time1, time2):
        total_seconds1 = time1.hours * 3600 + time1.minutes * 60 + time1.seconds 
        total_seconds2 = time1.hours *3600 + time2.minutes*60 +time2.seconds 
        difference = total_seconds1- total_seconds2 
        return 
        