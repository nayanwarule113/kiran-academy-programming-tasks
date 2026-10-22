
balance = 10000

print("Welcome to Kiran Bank")
print(f"Opening Balance: ₹{balance:.2f}")

while True:
    print("\n----- Banking Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount. Enter an amount greater than 0.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount. Enter an amount greater than 0.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print(f"Current Balance: ₹{balance:.2f}")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
