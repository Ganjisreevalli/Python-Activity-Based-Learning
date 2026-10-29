


balance = 5000.0
transaction_history = []

print("===== ATM TRANSACTION SYSTEM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Current Balance: Rs.", round(balance, 2))

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: Rs. "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                balance += amount
                transaction_history.append(
                    f"Deposited Rs. {amount:.2f}"
                )
                print("Deposit successful.")
                print("Updated Balance: Rs.", round(balance, 2))

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: Rs. "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                transaction_history.append(
                    f"Withdrew Rs. {amount:.2f}"
                )
                print("Withdrawal successful.")
                print("Updated Balance: Rs.", round(balance, 2))

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "4":
        print("\n===== TRANSACTION HISTORY =====")

        if len(transaction_history) == 0:
            print("No transactions yet.")
        else:
            for transaction in transaction_history:
                print(transaction)

    elif choice == "5":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")

print("=================================")
