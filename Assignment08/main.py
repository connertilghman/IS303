#Bank Account Transactions
#This program allows a user to create a bank account, make deposits and withdrawals, and view account information.

from BankAccount import bankaccount

def get_amount(prompt):
    """Ask for a dollar amount; return a float, or None if invalid."""
    try:
        return float(input(prompt).replace("$", "").replace(",", ""))
    except ValueError:
        return None
 
 
def show_menu():
    print("\n===== Bank Menu =====")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
 
 
def main():
    name = ""
    while not name:
        name = input("Welcome! Please enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
 
    account = bankaccount(name)
    print(f"\nThank you, {account.name}. Your account has been created.")
    print(f"Your account number is {account.account_number}.")
    print(f"Starting balance: ${account.balance:,.2f}")
 
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
 
        if choice == "1":
            amount = get_amount("How much would you like to deposit? $")
            if amount is not None and account.deposit(amount):
                print(f"Deposited ${amount:,.2f}. New balance: ${account.balance:,.2f}")
            else:
                print("Invalid amount. Please enter a number greater than 0.")
 
        elif choice == "2":
            amount = get_amount("How much would you like to withdraw? $")
            if amount is None or amount <= 0:
                print("Invalid amount. Please enter a number greater than 0.")
            elif amount > account.balance:
                print(f"Insufficient funds. Your balance is ${account.balance:,.2f}.")
            else:
                account.withdraw(amount)
                print(f"Withdrew ${amount:,.2f}. New balance: ${account.balance:,.2f}")
 
        elif choice == "3":
            account.display_info()
 
        elif choice == "4":
            print(f"\nThank you for banking with us, {account.name}. Goodbye!")
            break
 
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
 
 
if __name__ == "__main__":
    main()

