#Bank Account Class
#This class represents a bank account with basic functionality for deposits, withdrawals, and displaying account information.

import random


class bankaccount:

    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(1, 999999)
        self.balance = 0.00

    def deposit(self, amount):
        #Add money to the account. Returns True if successful.
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        #Remove money from the account.
 
        #Returns True if successful, False if the amount is invalid or exceeds the current balance.
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def display_info(self):
        #Print the customer's name, account number, and balance.
        print("\n--- Account Information ---")
        print(f"Name:           {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance:        ${self.balance:,.2f}")