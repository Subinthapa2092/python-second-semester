#  Program to implement the use of break and continue in real world programs. 


password = "admin123"

for attempt in range(1, 6):

    pwd = input(f"Attempt {attempt}: Enter password: ")

    
    if pwd == "":
        print("Empty input not allowed")
        continue

    
    if pwd == password:
        print("Login successful!")
        break

    print("Wrong password")

else:
    print("Account locked after 5 attempts")