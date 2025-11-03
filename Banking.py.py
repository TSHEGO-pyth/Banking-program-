#Banking App

def show_balance():
    print(f"Your balance is R{balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("That is not valid")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if amount < 0:
        print("That is not valid")
        return 0
    elif amount > balance:
        print("Insufficient funds")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Banking program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice")

print("Thank you have a wonderful day!")