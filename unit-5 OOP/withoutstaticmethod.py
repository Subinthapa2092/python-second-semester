#### with the Statitics Method 
class Person:
    count = 0

    def __init__(self, name, sex='Male', age=20):
        # Default values: sex='Male', age=20
        Person.count = Person.count + 1   # Static (class) variable
        self.name = name
        self.sex = sex
        self.age = age

    @staticmethod
    def countPerson():
        # No self parameter because it is a static method
        print("Number of persons ->", Person.count)


# Create 3 objects of Person class
p1 = Person("Harendra")
p2 = Person("Rajesh")
p3 = Person("Rukmani", "Female", 30)
p4 = Person("Subin Thapa")

# Call the static method
Person.countPerson()
#### without the Statitics Method 
class Person:
    count = 0

    def __init__(self, name, sex='Male', age=20):
        Person.count += 1
        self.name = name
        self.sex = sex
        self.age = age

    def countPerson(self):
        print("Number of persons ->", Person.count)


# Creating 3 objects
p1 = Person("Harendra")
p2 = Person("Rajesh")
p3 = Person("Rukmani", "Female", 30)

# Call using an object
p1.countPerson()
