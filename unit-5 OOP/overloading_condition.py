#### WAP to implement the left shift  Operator ::


class Number:
    def __init__(self,num):
        self.num = num 
    def __lshift__(self,other):
        return Number(self.num << other.num)
    def __rshift__(self, other):
        return Number(self.num>> other.num)
    def __str__(self):
        return f"The number after shifting by 2 is {self.num}"

num = Number(57)
shift = Number(2)
newnum = num<< shift
rshiftnum = num >> shift 
print(newnum)
print(rshiftnum)
    