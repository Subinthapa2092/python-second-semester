# ### dictionary comprehension :: 
# centigrade = {'kathmandu':30, "Butwal":40, "Dharan":35, "Mustang":15, "Dhangadi":42}
# fahrenheit = {key:{value*(9/5)+32} for (key,value) in centigrade.items()}
# print(fahrenheit)
# fahrenheit = {key:round(value*(9/5)+32) for (key,value) in centigrade.items()}
# print(fahrenheit)

# WAP to covert the salary of sofware devellopers gained in USD into NPR. Input n employees.
# dictionary is in plattter{ name,salary,....}
### without dictionary Comprehension 
# n=int(input("enter employee:"))
# dict= {}
# # usd = 152.3
# for i in range(n):
#     salary = float(input("enyer salary:"))
#     name = input("enter name of employee:")
#     # salary = float(input("enyer salary:"))
#     # salary= usd*salary
#     dict[salary] = name
#     # salary= usd*salary
    
# # print(dict)
# ### With the Dictionary Comphrension 
# #### expression + iterables ## case or conditions::
# result = {152.2 * key : value  for (key,value) in dict.items()}
# print(result)
# print(dict.items())
#### example 3 ::
def temp_func(value):
    if value>40:
        return "Hot"
    elif 40<=value>=35:
        return "Warm"
    else:
        return "cold"
centigrade={"kathmandu":35, "Butwal":44, "chitwan":45}
weather_function = {key: temp_func(value) for (key,value) in centigrade.items()}
print(weather_function)
