###m Composite Address
class Address:
    def __init__(self,city,state,country):
        self.city = city 
        self.state = state 
        self.country = country 
class Student():
    def __init__(self,id,name):
        self.id = id 
        self.name = name 
        self.address = Address("Kathmandu","Bagmati","Nepal")
    def display(self):
        return f"My name is {self.name}. I live in {self.address.country} in a city {self.address.city} in {self.address.state}"
class Doctor():
    def __init__(self,did,dname):
        self.did = did 
        self.dname = dname
        self.address = Address("Kathmandu","Bagmati","Nepal")
    def display(self):
        return f" I have a id {self.did} her name is {self.dname}. I live in {self.address.country} in a city {self.address.city} in {self.address.state}"
    
s1 = Student(15,"Subin Thapa")
doc = Doctor(15,"Anamika Shahi")
print(s1.display())
print(doc.display())