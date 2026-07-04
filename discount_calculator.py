price = float(input("Original price: "))
discount_percent = float(input("Discount percentage: "))

if discount_percent < 0 or discount_percent > 100:
    print("Invalid discount")
else:
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Final price: ${final_price:.2f}")

    if discount_percent == 0:
        print("No discount")
    elif discount_percent < 20:
        print("Small discount")
    elif discount_percent < 50:
        print("Good discount")
    else:
        print("Huge discount")