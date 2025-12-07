from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    # Get current date and time
    current_date = datetime.now()
    
    # Format and print in readable format
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")
    
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate and display a future date based on days added.
    
    Args:
        current_date: The starting date as a datetime object
        days_to_add: Number of days to add (integer)
    """
    # Calculate future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date ({days_to_add} days from now): {formatted_future_date}")
    
    return future_date

def main():
    # Part 1: Display Current Date and Time
    print("=" * 50)
    print("PART 1: CURRENT DATE AND TIME")
    print("=" * 50)
    current_date = display_current_datetime()
    
    # Part 2: Calculate Future Date
    print("\n" + "=" * 50)
    print("PART 2: FUTURE DATE CALCULATOR")
    print("=" * 50)
    
    # Prompt user for number of days
    while True:
        try:
            days_input = input("Enter the number of days to add (as an integer): ")
            days_to_add = int(days_input)
            
            if days_to_add < 0:
                print("Please enter a non-negative number.")
                continue
                
            future_date = calculate_future_date(current_date, days_to_add)
            break
            
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()