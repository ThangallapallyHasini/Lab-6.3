# A simple Bank Account class
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # Starting balance is 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Money deposited:", amount)
        else:
            print("Please enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to withdraw.")
        elif amount > self.balance:
            print("Not enough money in the account.")
        else:
            self.balance -= amount
            print("Money withdrawn:", amount)

    def show_balance(self):
        print("Current balance:", self.balance)


# ----------- Let's use the BankAccount class ------------

# Ask for user's name
name = input("Enter your name to open a bank account: ")
account = BankAccount(name)

print("\nWelcome to your bank account,", name)

# Let the user do actions in a loop
while True:
    print("\nChoose an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1 to 4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Goodbye,", name)
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")