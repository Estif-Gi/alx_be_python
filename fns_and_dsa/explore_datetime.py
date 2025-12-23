from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return the datetime object for later use

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        if days < 0:
            print("Please enter a non-negative number of days.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Calculate future date
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    print("Exploring Python's datetime module\n")
    
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate and display future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()