# ### program in a python to add,multiply, division using multiple inheritance 

# class Calculation1:
#     def Summation(a,b):
#         return a+b 

# class Calculation2:
#     def Multiplication(a,b):
#         return a*b 
    

# class Derived(Calculation1,Calculation2):
#     def Divide(a,b):
#         return a/b 

# d = Derived()
# print(d.Summation(1,2))
# print(d.Multiplication(1,2))
# print(d.Divide(8,2))    
class Frontend_Developer:
    def __init__(self):
        self.salary1 = 5000   # No super()

class Backend_Developer:
    def __init__(self):
        self.salary2 = 6000   # No super()

class FullStack(Frontend_Developer, Backend_Developer):
    def __init__(self):
        super().__init__()    # Calls only Frontend_Developer.__init__()

    def total_salary(self):
        return self.salary1 + self.salary2

stack = FullStack()
print(stack.total_salary())














# class Frontend_Developer:
#     def __init__(self):
#         self.salary1 = 5000

# class Backend_Developer:
#     def __init__(self):
#         self.salary2 = 6000
        
# class fullstack(Frontend_Developer,Backend_Developer):
#     def total_salary(self):
#         result = self.salary2+self.salary1
        
#         return f"My Full stack developer salary is {result}"
    
# result = fullstack()
# print(result.total_salary())


# # print(result.Frontend_Developer()) 
