# Day 10 - Move Decision

income = float(input("Enter monthly income: "))
rent = float(input("Enter monthly rent: "))
buffer = float(input("Enter savings buffer: "))
has_visa = input("Do you have the right visa/status? yes/no: ")

rent_percentage = (rent / income) * 100

income_ok = income >= 1000
rent_safe = rent_percentage <= 35
buffer_ok = buffer >= 1500
visa_ok = has_visa == "yes"

print("Move Decision")
print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Rent percentage: {rent_percentage:.2f}%")
print(f"Buffer: ${buffer:.2f}")
print(f"Visa/status OK: {visa_ok}")

if income_ok and rent_safe and buffer_ok and visa_ok:
    print("Decision: MOVE POSSIBLE")
elif income_ok and rent_safe and visa_ok:
    print("Decision: WAIT - BUILD MORE BUFFER")
elif not visa_ok:
    print("Decision: DO NOT MOVE - VISA/STATUS PROBLEM")
else:
    print("Decision: DO NOT MOVE - FINANCES TOO WEAK")
    
