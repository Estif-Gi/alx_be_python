from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    Saves the current date inside a current_date variable.
    Returns the formatted date/time string.
    """
    # Get current date and time and save in current_date variable
    current_date = datetime.now()
    
    # Format the date/time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date/time
    print(f"Current Date and Time: {formatted_datetime}")
    
    return formatted_datetime

def calculate_future_date():
    """
    Calculate and display a future date based on days added.
    Saves the future date inside a future_date variable.
    Returns the formatted future date string.
    """
    # Get current date
    current_date = datetime.now()
    
    # Prompt user for number of days
    while True:
        try:
            days_input = input("Enter the number of days to add (as an integer): ")
            days_to_add = int(days_input)
            
            if days_to_add < 0:
                print("Please enter a non-negative number.")
                continue
            break
            
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Calculate and save future date in future_date variable
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future Date ({days_to_add} days from now): {formatted_future_date}")
    
    return formatted_future_date

# Call the functions and store their return values
print("=" * 50)
print("CURRENT DATE AND TIME")
print("=" * 50)
formatted_current = display_current_datetime()

print("\n" + "=" * 50)
print("FUTURE DATE CALCULATOR")
print("=" * 50)
formatted_future = calculate_future_date()

# Display the stored/formatted values
print("\n" + "=" * 50)
print("STORED FORMATTED VALUES:")
print("=" * 50)
print(f"Formatted current datetime: {formatted_current}")
print(f"Formatted future date: {formatted_future}")