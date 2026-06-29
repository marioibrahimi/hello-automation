# Day 9 - Rent Check

income = float(input("Enter monthly income: "))
rent = float(input("Enter monthly rent: "))

rent_percentage = (rent / income) * 100

print("Rent Check")
print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Rent percentage: {rent_percentage:.2f}%")

if rent_percentage <=30:
    print("Status: SAFE")
elif rent_percentage <= 40:
    print("Status: STRETCH")
else:
    print("Status: DANGER")