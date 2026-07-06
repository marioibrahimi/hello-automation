current_savings = float(input("Current savings: "))
target_savings = float(input("Target savings: "))
monthly_savings = float(input("Monthly savings: "))

months = 0

if monthly_savings<= 0:
    print("Monhtly savings must be greater than 0.")
elif current_savings >= target_savings:
    print("You already reached your target.")
else:
    while current_savings < target_savings:
        current_savings = current_savings + monthly_savings
        months = months + 1

    print(f"Months needed: {months}")
    print(f"Final savings ${current_savings:.2f}")