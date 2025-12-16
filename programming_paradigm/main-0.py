# main-0.py

# This file interacts with the BankAccount class using command line arguments

import sys
from bank_account import BankAccount

def main():
    # Create a bank account with a starting balance of 100
    account = BankAccount(100)

    # Check if the user provided a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        return

    # Get the command input (example: "deposit:50")
    user_input = sys.argv[1]

    # Split the command and amount using ":"
    parts = user_input.split(":")

    command = parts[0]           # deposit / withdraw / display
    amount = float(parts[1]) if len(parts) > 1 else None

    # Handle deposit
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    # Handle withdraw
    elif command == "withdraw" and amount is not None:
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    # Handle display balance
    elif command == "display":
        account.display_balance()

    # Handle invalid command
    else:
        print("Invalid command.")

# This ensures the main function runs when the file is executed
if __name__ == "__main__":
    main()
