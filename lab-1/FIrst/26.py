#  Program to convert the date of birth from B.S. to A.D. using proper conditions and criteria.


bs_year = int(input("Enter B.S. Year : "))
bs_month = int(input("Enter B.S. Month: "))
bs_day = int(input("Enter B.S. Day  : "))

ad_year = bs_year - 56
ad_month = bs_month - 8
ad_day = bs_day

if ad_month <= 0:
    ad_month += 12
    ad_year -= 1

print("\nDate of Birth in A.D.")
print("Year :", ad_year)
print("Month:", ad_month)
print("Day  :", ad_day)