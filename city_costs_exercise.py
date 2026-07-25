costs = [300, 250, 30, 15]
total = 0

for cost in costs:
    print(f"Cost: ${cost}")
    total = total + cost
    if cost > 100:
        print(f"High cost: ${cost}")

print(f"Total: ${total}")