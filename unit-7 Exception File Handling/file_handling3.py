import csv
with open(r'C:\Users\Lenovo\Desktop\python programming\unit-7 Exception File Handling\subin.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)