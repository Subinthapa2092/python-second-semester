#### Python in a program to do the immutable and mutable sequence
### Immutable sequences are the collections that are used when the stored data is read only
## for Eg:: strings, bytes, and tuples 
### Mutable sequences are the collections that  are modifiable ## 
### for eg: list, bytearrays, set etc . 
### Immutable means that are changeable 
### tuple() : class that holds different types of data
# heterogenous data: 
t1 = ("Subin Thapa",2,4,6,8,"Saubhagaya Dhungana")
print(f"My name is {t1[-6]}")
# t1[1] = "Rahul Sharma"### item assigment is not supported inmmutable sequences 

print(t1)
### bytes for the data 
list1 = [234,123,156,255,252]
b1 = bytes(list1)
print(b1)
### strings are the enclosed by the " ", '' and """ """
name = """ Subin\rThapa"""
print(name)
print(type(name))
### for the displaying the path of the url :: raw string 
s = r'C:\tver\nPython\t3'
print(s)
print(type(s))
### \r and \b are the escape sequence 
### \r is the carriage return and \b is the backspace 
## example of \r        
s1 = "Hello\rWorld"
print(s1)
### Three different types of the formating 
### first types
name = "Subin Thapa" 
age = 19 
print("My name is %s and i am %d year old " %(name,age))
### second types 
message = "My name is {}  and i am {} old".format(name,age)
print(message)
### Positional formating arguments
st1 = "My name is {0}, I live in {1}, I study in {2}"
message = st1.format("Subin Thapa",19,"Kritipur")
print(message)
#### keyword  formating arguments
st2 = "My name is {a}, I live in {b}, I study in {c}"
message = st2.format(a = "Subin Thapa",b = "kalanki",c = "kritipur")
print(message)