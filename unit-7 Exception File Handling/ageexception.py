class ageException(Exception):
    def __init__(self,message):
        self.message = message 
def Age(age):
    if age <0:
        raise ageException("Age less than zero exception")
    else:
        print("Age is valid")
# age = int(input("Enter your age "))
# Age(age)
if __name__ == "__main__":
    while True:
        age = int(input("Enter your age :: "))
        try:
            Age(age)
            break 
        except ageException:
            print("Exception occurred and handled")