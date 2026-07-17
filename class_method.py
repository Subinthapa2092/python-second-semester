##### Class Method 
from datetime import date 

class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    @classmethod
    def age_calculator(cls,name,birth_year):
        ### 
        return cls(name,date.today().year - birth_year)
    ### Similar to return student(name,age)
    
    def show(self):
        print(self.name + "'s age is "+str(self.age))
### method1 
st1 = Student('Mahesh',20)
st1.show()
st2 = Student.age_calculator("Subin Thapa",2007)### Accessing class method
st2.show()
