# bank_account.py
# This file defines a simple BankAccount class

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional starting balance.
        Default is 0 if nothing is provided.
        """
        self.account_balance = initial_balance  # Store the balance as a private attribute

    def deposit(self, amount):
        """
        Add money to the account.
        Assumes amount is positive (validation can be added later if needed).
        """
        self.account_balance += amount
        # No return needed unless you want to confirm success

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Returns True if there are sufficient funds, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False  # Not enough money

    def display_balance(self):
        """
        Print the current balance in a nice format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")  # Show 2 decimal places