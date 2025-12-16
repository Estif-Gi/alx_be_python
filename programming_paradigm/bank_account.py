# bank_account.py

# This file defines the BankAccount class

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        This method runs when a new BankAccount is created.
        initial_balance is optional. If not given, it starts at 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add money to the account balance
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Remove money from the account if there is enough balance.
        Returns True if successful, False if not.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current account balance
        """
        print(f"Current Balance: ${self.account_balance}")
