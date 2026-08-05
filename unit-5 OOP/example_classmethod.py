"""
    WAp to subract two time objects using oop(use class method decorator )
    """
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def subtract_times(cls, time1, time2):
        total_seconds1 = time1.hours * 3600 + time1.minutes * 60 + time1.seconds
        total_seconds2 = time2.hours * 3600 + time2.minutes * 60 + time2.seconds
        diff_seconds = total_seconds1 - total_seconds2

        hours = diff_seconds // 3600
        minutes = (diff_seconds % 3600) // 60
        seconds = diff_seconds % 60

        return cls(hours, minutes, seconds)

s1 = Time(5, 30, 45)
s2 = Time(2, 15, 30)
result = Time.subtract_times(s1, s2)
print(f"Result: {result.hours}:{result.minutes}:{result.seconds}")
