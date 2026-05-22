##### program in a python to do the keyword argumen are matched by name, 
## default values 

def fun(a,b=4,c=88):
    print(a,b,c)
fun(1) ### 1,4,88 
# print(b=5,a=7,c=9) ### 7,5,9 
# fun(42,c=9)
### **kwargs 
def func(**kwargs):
    print(kwargs)
func(a=1,b=42)
func(**{'a':1,'b':42})
func(**dict(a=1,b=42))