# temp_conversion_tool.py

# Define Global Conversion Factors as specified in requirements
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Conversion factor for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Conversion factor for C to F

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius
    """
    # Use the global conversion factor FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # Use the global conversion factor CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    print("Temperature Conversion Tool")
    print("-" * 30)
    
    # Get temperature input from user
    while True:
        temp_input = input("Enter the temperature to convert: ")
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    
    # Get unit input from user
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C' or unit == 'F':
            break
        else:
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    # Perform conversion based on unit
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:  # unit == 'C'
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")

if __name__ == "__main__":
    main()