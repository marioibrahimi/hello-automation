# Day 4 - Income Calculator

gross_hourly = 6.96
hours_per_month = 160
tax_rate = 0.32

gross_monthly = gross_hourly * hours_per_month
tax_amount = gross_monthly * tax_rate
net_monthly = gross_monthly - tax_amount

print("Income Calculator")
print(f"Gross hourly: ${gross_hourly}")
print(f"Hours per month: {hours_per_month}")
print(f"Gross monthly: ${gross_monthly:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Estimated net monthly: ${net_monthly:.2f}")