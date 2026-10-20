
# Case Study 1: Retail Billing with Multiple Discount Rules

products = [
    ("Notebook", 50, "Stationery", 5),
    ("Pen", 10, "Stationery", 5),
    ("School Bag", 500, "Accessories", 12)
]

subtotal = 0
bill_items = []

print("===== RETAIL BILLING SYSTEM =====")

# Get product quantities
for product in products:
    name, price, category, tax_rate = product

    quantity = int(input("Enter quantity of " + name + ": "))

    if quantity < 0:
        print("Invalid quantity. Using 0.")
        quantity = 0

    amount = price * quantity
    subtotal = subtotal + amount

    bill_items.append(
        (name, quantity, price, amount, tax_rate)
    )

# Calculate discount
discount = 0

if subtotal >= 100:
    discount = subtotal * 0.10

# Maximum discount limit
if discount > 200:
    discount = 200

# Display bill
print("\n========== ITEMIZED BILL ==========")
print("Product       Qty   Price   Amount")

for item in bill_items:
    name, quantity, price, amount, tax_rate = item

    print(name, " ", quantity, "   Rs.", price,
          "   Rs.", amount)

print("-----------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))

# Calculate category-specific tax after discount
total_tax = 0

for item in bill_items:
    name, quantity, price, amount, tax_rate = item

    if subtotal > 0:
        item_discount = discount * amount / subtotal
    else:
        item_discount = 0

    taxable_amount = amount - item_discount
    item_tax = taxable_amount * tax_rate / 100
    total_tax = total_tax + item_tax

print("Tax: Rs.", round(total_tax, 2))

final_amount = subtotal - discount + total_tax

print("-----------------------------------")
print("FINAL BILL: Rs.", round(final_amount, 2))
print("Thank you for shopping!")

