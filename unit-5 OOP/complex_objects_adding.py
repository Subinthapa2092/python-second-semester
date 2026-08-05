#### Adding Two Complex Objects 



class Complex:
    
    def __init__(self,real= 0,imaginary = 0):
        self.real = real 
        self.imaginary = imaginary 
    def __str__(self):
        return "({0}+{1}i)".format(self.real,self.imaginary)
    def __add__(self,other):
        real = self.real+other.real 
        imaginary = self.imaginary+other.imaginary 
        return Complex(real,imaginary)
num1 = Complex(3,4)
num2 = Complex(5,7)
result = Complex()
result = num1+num2 
print(result)
        