# Day 5 - Income Calculator with user input

gross_hourly = float(input("Enter gross hourly rate: "))
hours_per_month = float(input("Enter hours per month: "))
tax_rate_percent= float(input("Enter tax rate percentage: "))

tax_rate = tax_rate_percent / 100

gross_monthly = gross_hourly * hours_per_month
tax_amount = gross_monthly * tax_rate
net_monthly = gross_monthly - tax_amount

print("Income Calculator")
print(f"Gross hourly: ${gross_hourly}")
print(f"Hours per month: {hours_per_month}")
print(f"Gross monthly: ${gross_monthly:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Estimated net monthly: ${net_monthly:.2f}")