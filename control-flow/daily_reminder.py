# Prompt user for task information
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"High priority task: '{task}'"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " - please address this soon."
    
    case "medium":
        reminder = f"Medium priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - complete this by the end of the week."
        else:
            reminder += " - schedule this for the upcoming weeks."
    
    case "low":
        reminder = f"Low priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - try to complete this when you have free time."
        else:
            reminder += " - no rush on this task."
    
    case _:
        reminder = "Invalid priority level entered."

# Print the customized reminder
print("\nTask Reminder:")
print(reminder)