
# Case Study 8: Repeated Transaction Detection

print("===== REPEATED TRANSACTION DETECTION =====")

transactions = [
    "TXN101",
    "TXN102",
    "TXN103",
    "TXN102",
    "TXN104",
    "TXN101",
    "TXN105"
]

seen = set()
repeated = set()

for transaction_id in transactions:
    if transaction_id in seen:
        repeated.add(transaction_id)
    else:
        seen.add(transaction_id)

print("All Transactions:")
for transaction_id in transactions:
    print(transaction_id)

print("\nRepeated Transactions:")

if repeated:
    for transaction_id in sorted(repeated):
        print(transaction_id)
else:
    print("No repeated transactions found.")

print("Total Transactions:", len(transactions))
print("Unique Transactions:", len(seen))
print("Repeated Transaction IDs:", len(repeated))

print("==========================================")
