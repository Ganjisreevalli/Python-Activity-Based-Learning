
# Case Study 6: Multi-Product Shopping Budget Constraint

print("===== SHOPPING BUDGET SYSTEM =====")

products = {
    "Notebook": 50,
    "Pen": 10,
    "School Bag": 500,
    "Water Bottle": 100,
    "Pencil Box": 80
}

budget = 700
total = 0
selected_items = []

print("Your budget is Rs.", budget)
print("\nAvailable Products:")

for name, price in products.items():
    print(name, "- Rs.", price)

for name, price in products.items():
    choice = input(
        "\nDo you want to buy " + name + "? (yes/no): "
    ).lower()

    if choice == "yes":
        if total + price <= budget:
            selected_items.append((name, price))
            total += price
            print("Added:", name)
        else:
            print("Cannot add", name, "- budget exceeded.")

print("\n===== SHOPPING SUMMARY =====")

if len(selected_items) == 0:
    print("No products selected.")
else:
    for name, price in selected_items:
        print(name, "- Rs.", price)

print("Total Cost: Rs.", total)
print("Remaining Budget: Rs.", budget - total)
print("================================")
