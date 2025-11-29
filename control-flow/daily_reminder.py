def get_valid_input(prompt, valid_options=None):
    """Get validated user input"""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Error: This field cannot be empty!")
            continue
        
        if valid_options and user_input.lower() not in valid_options:
            print(f"Error: Please enter one of: {', '.join(valid_options)}")
            continue
            
        return user_input

# Prompt user for task information with comprehensive validation
print("=== TASK MANAGEMENT SYSTEM ===")
task = get_valid_input("Enter the task description: ")
priority = get_valid_input("Enter the task's priority (high, medium, low): ", 
                          ["high", "medium", "low"]).lower()
time_bound = get_valid_input("Is the task time-bound? (yes or no): ", 
                           ["yes", "no"]).lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"🚨 High priority task: '{task}'"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " - please address this as soon as possible."
    
    case "medium":
        reminder = f"⚠️ Medium priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - aim to complete this within the next few days."
        else:
            reminder += " - schedule this for when you have availability."
    
    case "low":
        reminder = f"✅ Low priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - work on this when you have spare time."
        else:
            reminder += " - no urgent timeline for this task."

# Print the customized reminder
print("\n" + "="*50)
print("TASK REMINDER")
print("="*50)
print(reminder)
print("="*50)