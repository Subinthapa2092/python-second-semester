# Rates of tax on gross salary(yearly) are as shown below: 
# Income                           Tax
# Up to Rs. 5,00,000               1%                    
# Rs. 5,00,001 – 7,00,000          10%
# Rs. 7,00,001 – 10,00,000         20% 
# Rs. 10,00,001 – 20,00,000        30% 
# Rs. 20,00,001 – 50,00,000        36% 
# Above Rs. 50,00,000              39% 
# Calculate the exact monthly salary of an individual employee who gets the monthly gross salary of 125000. 



monthly_gross = 125000

yearly_gross = monthly_gross * 12

if yearly_gross <= 500000:
    tax_rate = 0.01

elif yearly_gross <= 700000:
    tax_rate = 0.10

elif yearly_gross <= 1000000:
    tax_rate = 0.20

elif yearly_gross <= 2000000:
    tax_rate = 0.30

elif yearly_gross <= 5000000:
    tax_rate = 0.36

else:
    tax_rate = 0.39

tax = yearly_gross * tax_rate
net_yearly_salary = yearly_gross - tax
exact_monthly_salary = net_yearly_salary / 12

# print("Yearly Gross Salary :", yearly_gross)
# print("Tax Amount          :", tax)
# print("Net Yearly Salary   :", net_yearly_salary)
print("Exact Monthly Salary:", exact_monthly_salary)