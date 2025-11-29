# Prompt user for task information
task = input("Enter the task description: ")

# Get priority with validation
while True:
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter only: high, medium, or low")

# Get time-bound status with validation
while True:
    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please enter only: yes or no")

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