# temp_conversion_tool.py - Enhanced Version

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_FAHRENHEIT = -459.67

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius
    """
    # Validate temperature is above absolute zero
    if fahrenheit < ABSOLUTE_ZERO_FAHRENHEIT:
        raise ValueError(f"Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_FAHRENHEIT}°F)")
    
    # Using the global conversion factor
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
    # Validate temperature is above absolute zero
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError(f"Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_CELSIUS}°C)")
    
    # Using the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def display_conversion(temperature, unit, converted_temp, target_unit):
    """
    Display the conversion result in a formatted way.
    """
    print("\n" + "=" * 50)
    print("CONVERSION RESULT")
    print("=" * 50)
    print(f"{temperature:.2f}°{unit} = {converted_temp:.2f}°{target_unit}")
    
    # Add some interesting comparisons
    if target_unit == 'C':
        if converted_temp < 0:
            print("That's below freezing!")
        elif converted_temp > 100:
            print("That's boiling hot!")
    else:  # target_unit == 'F'
        if converted_temp < 32:
            print("That's below freezing!")
        elif converted_temp > 212:
            print("That's above water's boiling point!")

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    print("=" * 50)
    print("TEMPERATURE CONVERSION TOOL")
    print("=" * 50)
    print("Convert temperatures between Celsius and Fahrenheit")
    print("=" * 50)
    
    try:
        # Get temperature input from user
        while True:
            try:
                temp_input = input("\nEnter the temperature to convert: ")
                temperature = float(temp_input)
                break
            except ValueError:
                print("Invalid temperature. Please enter a numeric value.")
        
        # Get unit input from user
        while True:
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            if unit in ['C', 'CELSIUS']:
                unit = 'C'
                target_unit = 'F'
                break
            elif unit in ['F', 'FAHRENHEIT']:
                unit = 'F'
                target_unit = 'C'
                break
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Perform conversion
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
        
        # Display result
        display_conversion(temperature, unit, converted_temp, target_unit)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def run_tests():
    """
    Function to test the conversion functions with example values.
    """
    print("\n" + "=" * 50)
    print("TEST EXAMPLES")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        (32, 'F', 0, 'C'),      # Freezing point
        (212, 'F', 100, 'C'),   # Boiling point
        (0, 'C', 32, 'F'),      # Freezing point
        (100, 'C', 212, 'F'),   # Boiling point
        (-40, 'C', -40, 'F'),   # Same in both scales
        (-40, 'F', -40, 'C')    # Same in both scales
    ]
    
    for temp, unit, expected, target in test_cases:
        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°{unit} -> {result:.2f}°{target} (expected: {expected}°{target})")
        else:
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°{unit} -> {result:.2f}°{target} (expected: {expected}°{target})")

if __name__ == "__main__":
    main()
    
    # Optional: Uncomment to run tests
    # run_tests()