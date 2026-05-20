"""
A program to find the list of the products that is goining 
to expire tommorrow : there is an offer of 20% discount. 
We are using continue statement to skip the iterations where expiration
date is not equal to today.
"""
products = [
    {
        "Subin Thapa":'1','expiration_date':'today','price':50.0
    },
    {
        "Subin Thapa":'2','expiration_date':'yesterday','price':850.0
    },
    {
        "Subin Thapa":'3','expiration_date':'today','price':350.0
    },
    {
        "Subin Thapa":'4','expiration_date':'tomorrow','price':950.0
    }
]
for product in products:
    if product['expiration_date'] != 'today':
        continue  
    product['price'] *= 0.8 ## equivalent to applying 20% discount 
    print(product["Subin Thapa"],product['price'])
### program to listout the products that are not expired 
### using the Datetime Module. Apply this criteriaby making your own 
### list of Dictionaries of Products 
import datetime as dt 
products = products = [
    {
        "Subin Thapa":'1','expiration_date':dt.datetime(2026,4,30),'price':50.0
    },
    {
        "Subin Thapa":'2','expiration_date':dt.datetime(2027,4,30),'price':850.0
    },
    {
        "Subin Thapa":'3','expiration_date':dt.datetime(2028,4,30),'price':350.0
    },
    {
        "Subin Thapa":'4','expiration_date':dt.datetime(2025,4,30),'price':950.0
    }
] ### list of the products:: 
from datetime import datetime 
for product in products:
    if product["expiration_date"]> datetime.now():
        print(product)
### for else 
people = [("Subin",9),("kritik",17),("Garima",15),("Harrendra",8)]
for person,age in people:
    if age >= 18:
        driver = (person,age)
        print(driver,"is found elligible")
    else:
        print((person,age),"is not eligible")
else:
    print("Driver not found ! ")