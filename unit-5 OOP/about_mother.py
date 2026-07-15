# class Frontend_Developer:
#     def __init__(self):
#         self.salary1 = 5000

# class Backend_Developer:
#     def __init__(self):
#         self.salary2 = 6000

# class FullStack(Frontend_Developer, Backend_Developer):
#     def __init__(self):
#         Frontend_Developer.__init__(self)
#         Backend_Developer.__init__(self)

#     def total_salary(self):
#         return self.salary1 + self.salary2

# stack = FullStack()
# print(stack.total_salary())
#### 
#### Abpit the Mother 
class GrandFather:
    def __init__(self):
        print('Grandpa-Hii')
    def age(self,a):
        print(f"Printing the age of grandpa is {a}")
class Father(GrandFather):
    def __init__(self):
        print('Father-Hii')
        super().__init__()
    def age(self,a):
        print(f'Printing the age(father) : {a}')
        super().age(a+20)
class Mother(Father):
    def __init__(self):
        print('Mother -Hii')
        super().__init__()
    
    def age(self,a):
        print(f'Printing the age(Mother) : {a}')
        super().age(a+20)
## Main Function 
if __name__ == '__main__':
    o = Mother()
    o.age(39)