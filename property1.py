### @property 

"""
Basic concept is to use any method like a peoperty 
class Info:
      def email(self):
          print(self.email)
in = Info()
print(in.email)## property 
"""
class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    @property
    def email(self):
        return '{}{}.sms.tu.edu.np'.format(self.firstname,self.lastname)
    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname) 
    @fullname.setter
    def fullname(self,name):
        firstname,lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname
    @fullname.deleter
    def fullname(self):
        print("Deleteor Property")
        self.firstname = None
        self.lastname = None

emp = Employee("Subin","Thapa")
# print(f"My email is {emp.email}")
print("My email is",emp.email)
emp.firstname = "beein"
# print(f"My email is {emp.email()}")
print("My email is",emp.email)
emp.fullname = "Saubhagya Dhungana"
print(f"My name is {emp.fullname}")
# print("My email is",emp.email)
del emp.fullname 
print(emp.fullname)