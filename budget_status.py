# Day 8 - Budget Status

income = float(input("Enter monthly income: "))
expenses = float(input("Enter monthly expenses: "))

savings = income - expenses

print("Budget Status")
print(f"Income: ${income:.2f}")
print(f"Expenses: ${expenses:.2f}")
print(f"Savings: ${savings:.2f}")

if savings > 0:
    print("Status: Positive savings. Good.")
elif savings == 0:
    print("Status: Break-even. No buffer.")
else:
    print("Status: Negative savings. Danger.")

