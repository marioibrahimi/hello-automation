expenses = [300,100,250]

print("Original expenses:")
print(expenses)

print(f"First expense: ${expenses[0]}")
print(f"Second expense: ${expenses[1]}")

expenses.append(50)

print("After adding a new expense:")
print(expenses)

expenses.remove(100)

print("After removing one expense:")
print(expenses)

total = 0

for expense in expenses:
    total = total + expense

print(f"Total expenses: ${total:.2f}")