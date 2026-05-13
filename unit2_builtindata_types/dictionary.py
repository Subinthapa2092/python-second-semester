####  Python Dictionary 

fruits = {1:"Banana",2:"Mango",3:"Litchie"} 

definition = {"Banana":"A fruit contains Potassium","Mango":"Mango contains another mangos","Litchie": "Litchie is good "}

### Methods used in dictionary 

### dictionary . clear(),
### dictionary.copy(),
### dictionary.fromkey(x,y):
### dictionary .get(x),
### dictionary. items(),
### dictionary.values(),
### dictionary.update(dictionary2)
#### dictionary .keys()
### dictionary. pop(key)
###dictionary.popitems()
#### methods in key's 
Student = {"name":"harendra","age":20,"roll_no":34,"address":"Dhading"}
print(Student["address"])
#### 
# Student.clear()
print(Student)
print(type(Student))
#### copy
s1 = Student.copy()
print(s1)
#### from key : get 
print(Student.get("age"))
#### from items, values, key 
print(s1.items())
print(s1.values())
print(s1.keys())
s2 = {"name1":"Subin Thapa","age2":19,"roll_no1":32,"address1":"kalanki"}
s1.update(s2)
print(s2)
### pop, pop through keys 
s1.pop("name1")
print(s1)
### pop, pop items()
s1.popitem()
print(s1)
s1.popitem()
print(s1)
### 
t1 = (1,2,3,4) ### tuples
t2 = 4 ### values
d1 = {}### empty 
d1 = dict.fromkeys(t1,t2)
print(d1)
#### nested examples:: 
dict1 = {
    "student1": {
        "name" :"Subin Thapa","age":19
    },
    "student2" : {
        "name":"Saubhagya Dhugnana","age":19
    }
}
print(dict1)
bookstore = {
    "books1": {"title":"C Programming","author":"subin","edition":9,"price":2500,"publication":"kec"},
    "books2": {"title":"Python","author":"subin","edition":4,"price":2600,"publication":"kec"},
    "books3": {"title":"Romeo and Juliet","author":"subin","edition":6,"price":2500,"publication":"kec"}
}


### find the total income after selling all three books? 
print(bookstore.values())

### 
income = []
for d in bookstore.values():
    income.append(d.get("price"))
print("Total income ",sum(income))