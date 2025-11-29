# Prompt user for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Please address this soon.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task with a deadline. Complete it this week.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Schedule it for later.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("\nError: Invalid priority entered. Please use high, medium, or low.")