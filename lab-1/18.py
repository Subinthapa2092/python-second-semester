# Using nested dictionary write a program to calculate the percentage of n students having roll, name, fee, marks(5 subjects). And calculate the average percentage of the students. Display the data in descending order. 


n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    print(f"\nEnter details of Student {i+1}")
    
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    fee = float(input("Enter Fee: "))

    marks = []
    total = 0

    print("Enter marks of 5 subjects:")
    for j in range(5):
        m = float(input(f"Subject {j+1}: "))
        marks.append(m)
        total += m

    percentage = total / 5

    students[roll] = {
        "Name": name,
        "Fee": fee,
        "Marks": marks,
        "Percentage": percentage
    }

sorted_students = sorted(
    students.items(),
    key=lambda x: x[1]["Percentage"],
    reverse=True
)

print("\nStudent Details (Descending Order of Percentage)")

total_percentage = 0

for roll, details in sorted_students:
    print("Roll Number :", roll)
    print("Name        :", details["Name"])
    print("Fee         :", details["Fee"])
    print("Marks       :", details["Marks"])
    print("Percentage  :", details["Percentage"])

    total_percentage += details["Percentage"]

average_percentage = total_percentage / n

print("Average Percentage of Students =", average_percentage)