##### Inheritance 

class Employee():
    def __init__(self,salary):
        self.salary = salary 
### Derived Class 

class Programmer(Employee):
    def __init__(self,salary,bonus):
        super().__init__(salary)
        self.bonus = bonus  

class MobileDeveloper(Programmer):
    def __init__(self,salary,bonus,allowance):
        super().__init__(salary,bonus)
        self.allowance = allowance 
    
    def TotalSal(self):
        return self.salary+self.bonus+self.allowance 

class IOSDeveloper(MobileDeveloper):
    def __init__(self,salary,bonus,allowance):
        super().__init__(salary,bonus,allowance)
        self.allowance = allowance + 0.1 * salary
    def TotalSal(self):
        return self.salary+self.bonus+self.allowance 
class AndroidDeveloper(MobileDeveloper):
    def __init__(self,salary,bonus,allowance):
        super().__init__(salary,bonus,allowance)
        self.allowance = allowance + 0.5 * salary
    def TotalSal(self):
        return self.salary+self.bonus+self.allowance 


user1 = MobileDeveloper(5000,500,200)
iso1 = IOSDeveloper(5000,500,300)
andro1 = AndroidDeveloper(5000,500,300)
print(user1.TotalSal())
print(iso1.TotalSal())