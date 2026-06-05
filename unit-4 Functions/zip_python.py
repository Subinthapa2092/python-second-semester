# ### 
# students = ["Subin Thapa","Rahul Adhikari"]
# percentage = [5,2]
# zipped_list = list(zip(students,percentage))
# mapped_list = list(map(lambda *x:x,students,percentage))
# print(zipped_list,mapped_list)
# ### 
# def adding_number(a,b,c):
#     result = a+b+c 
#     return result
# a = input("Enter the a number :: ")
# b = input("Enter the a number :: ")
# c = input("Enter the a number :: ")
# print(adding_number(a,b,c))

### write a program to filter the even number from the list from 1 to n using filter function 

def even_number(num): 
    if num %2 != 0: 
        return True 
    else: 
        return False
n = int(input("Enter the value of n : ")) 
numbers_list = list(range(1,n+1))
odd_numbers = list(filter(even_number,numbers_list))
print(f"The odd numbers from 1 to {n} are {odd_numbers}")