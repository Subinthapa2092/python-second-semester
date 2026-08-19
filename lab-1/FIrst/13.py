#  Program to implement nested dictionaries.


student = {
    "name": "Kaushal",
    "marks": {
        "Math": 90,
        "Science": 85
    }
}

print("Name:", student["name"])
print("Math Marks:", student["marks"]["Math"])
print("Science Marks:", student["marks"]["Science"])