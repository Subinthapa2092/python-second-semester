### wap to calculat the bmi value according  to 
##3 accoridng to weight (in kg) and height (in meter)
## using the formula 
# """
# bmi = weight / height *height 
# also display the message on the basis of the following  conditions
# if bmi >18.5 display underwe\ight 
# if bmi >= 18.5 and bmi <24.9 display normal weight
# if bmi >= 24.0 amd bmi <30 display over weight 
# else obsese
# """
weight = float(input("Enter the weight of the person  "))
height_infeet = float(input("Enter the  height of the person "))
## 1 heightinmeter  is equal to 0.305
heightinmeter = 0.305 * height_infeet 
bmi = weight / (heightinmeter ** 2)
if bmi> 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <24.9 :
    print("normal weight")
elif bmi >= 24.0 and bmi <30:
    print("Over weight")
else:
    print("obese")
### calculate the gpa according to smstu in semester one 
m1 = float(input("Enter the marks in c programming : "))
m2 = float(input("Enter the marks in Statictic : "))
m3 = float(input("Enter the marks in  Calculus : "))
m4 = float(input("Enter the marks in Basic computer organization  : "))
m5 = float(input("Enter the marks in data science : "))
gpa = (m1+m2+m3+m4+m5)/25 
if gpa >= 4.0:
    print("A+")
elif gpa <= 3.6 and gpa > 3.2:
    print("A")
elif gpa >= 3.2 and gpa > 2.8:
    print("B+")
elif gpa >= 2.8 and gpa > 2.4:
    print("B")
elif gpa >= 2.0 and gpa > 2.0:
    print("c+")
else:
    print("Pass")

