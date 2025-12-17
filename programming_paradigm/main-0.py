# main-0.py
# This is the main program that uses BankAccount via command-line arguments

import sys
from bank_account import BankAccount

def main():
    # Create a bank account with a starting balance of 100 (as intended)
    account = BankAccount(100)  # ← FIXED: was missing the initial balance

    # Check if the user provided a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount>    → e.g., deposit:50")
        print("  withdraw:<amount>   → e.g., withdraw:30")
        print("  display             → shows current balance (no amount needed)")
        return

    # Get the input from command line, e.g., "deposit:50" or "display"
    user_input = sys.argv[1]

    # Split by ":" to separate command and possible amount
    parts = user_input.split(":")

    command = parts[0].lower().strip()  # Get the command and make it lowercase for safety

    # Only try to read amount if there's a second part
    amount = None
    if len(parts) > 1:
        try:
            amount = float(parts[1])
            if amount < 0:
                print("Amount cannot be negative.")
                return
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

    # Handle the different commands
    if command == "deposit":
        if amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
            account.display_balance()  # Optional: show new balance
        else:
            print("Deposit requires an amount (e.g., deposit:50)")

    elif command == "withdraw":
        if amount is not None:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount:.2f}")
                account.display_balance()  # Optional: show remaining balance
            else:
                print("Insufficient funds.")
                account.display_balance()
        else:
            print("Withdraw requires an amount (e.g., withdraw:30)")

    elif command == "display":
        # Display doesn't need an amount, so we ignore any extra part
        account.display_balance()

    else:
        print("Invalid command. Use 'deposit', 'withdraw', or 'display'.")

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()