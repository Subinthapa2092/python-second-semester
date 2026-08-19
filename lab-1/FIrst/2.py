# Write a python program to find the gpa according to the criteria implemented in Data Science 
# (BDS) using logical and operators.

s1, s2, s3, s4, s5 = map(float, input("Enter marks in 5 subjects: ").split())

average = (s1 +s2 + s3 + s4 + s5) / 5

if average >= 90 and average <= 100:
    gpa = 4.0
    grade = "A"

elif average >= 80 and average < 90:
    gpa = 3.7
    grade = "A-"

elif average >= 70 and average < 80:
    gpa = 3.3
    grade = "B+"

elif average >= 60 and average < 70:
    gpa = 3
    grade = "B"

elif average >= 50 and average < 60:
    gpa = 2.7
    grade = "B-"

elif average >= 40 and average < 50:
    gpa = 2.3
    grade = "C"

elif average >= 0 and average < 40:
    gpa = 0.0
    grade = "F"

else:
    print("Invalid marks entered!")
    exit()

print("Grade:", grade)
print("GPA:", gpa)