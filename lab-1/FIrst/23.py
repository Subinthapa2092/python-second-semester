#  WAP to find the Body Mass Index of a person using the following formula and conditions.  
# BMI=Weight/Height*Height  
# BMI <18.0 then Underweight  
# BMI >=18.0 and BMI<24.9 then Normal  
# BMI >=25 and BMI<30 then Over Weight  
# BMI>=30 then Obese 



weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", round(bmi, 2))

if bmi < 18.0:
    print("Category : Underweight")

elif bmi >= 18.0 and bmi < 24.9:
    print("Category : Normal")

elif bmi >= 25 and bmi < 30:
    print("Category : Over Weight")

else:
    print("Category : Obese")