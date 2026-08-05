#### Subtract two time objects using the Operator Overloading::: 

class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours 
        self.minutes = minutes 
        self.seconds = seconds 
    
    def __sub__(self,other):### Operator Overloading
        # t1 = self.hours - other.hours 
        # t2 = self.minutes - other.minutes 
        # t3 = self.seconds - other.seconds 
        # return t1,t2,t3
        t1secs = self.hours*3600+ self.minutes*60 +self.seconds 
        
        t2secs = other.hours*3600+other.minutes*60 +other.seconds 
        
        diffsecs = t1secs-t2secs 
        hr = diffsecs//3600 
        remsecs = diffsecs %3600
        min = remsecs //60 
        sec = remsecs % 60 
        return Time(hr,min,sec)
        
    
    def __str__(self):### built in function 
        return "({0}:{1}:{2})".format(self.hours,self.minutes,self.seconds)

result1 = Time(5,30,45)
result2 = Time(2,15,55) 
print(result1 - result2)