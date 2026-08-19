# Program to print the id, name, salary of n employees with average salary using nested dictionaries


n = int(input("Enter number of employees: "))

employees = {}

for i in range(n):
    print(f"\nEnter details of Employee {i+1}")
    
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        "Name": name,
        "Salary": salary
    }

print("\nEmployee Details:")

total_salary = 0

for emp_id, details in employees.items():
    print("Employee ID :", emp_id)
    print("Name        :", details["Name"])
    print("Salary      :", details["Salary"])

    total_salary += details["Salary"]

average_salary = total_salary / n

print("Average Salary =", average_salary)