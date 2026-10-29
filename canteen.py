
print("===== CAMPUS CANTEEN BILLING SYSTEM =====")
print("1. Burger   - PKR 350")
print("2. Pizza    - PKR 500")
print("3. Sandwich - PKR 250")
print("4. Tea      - PKR 100")
print("0. Checkout")

subtotal = 0
total_quantity = 0

while True:
    choice = input("\nSelect item (0 to checkout): ")

    if choice == "0":
        break
    elif choice == "1":
        item = "Burger"
        price = 350
    elif choice == "2":
        item = "Pizza"
        price = 500
    elif choice == "3":
        item = "Sandwich"
        price = 250
    elif choice == "4":
        item = "Tea"
        price = 100
    else:
        print("Invalid choice!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be positive!")
        continue

    cost = price * quantity
    subtotal = subtotal + cost
    total_quantity = total_quantity + quantity

    print(item, "x", quantity, "= PKR", cost)

if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0

final_bill = subtotal - discount

print("\n========== FINAL BILL ==========")
print("Subtotal: PKR", subtotal)
print("Total quantity:", total_quantity)
print("Discount: PKR", discount)
print("Final bill: PKR", final_bill)
print("Thank you for visiting!")
