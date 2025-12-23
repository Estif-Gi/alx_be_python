# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process and display the customized reminder using Match Case
print("\nReminder:", end=" ")

match priority:
    case "high":
        print(f"'{task}' is a high priority task", end=" ")
        if time_bound == "yes":
            print("that requires immediate attention today!")
        else:
            print("that should be completed soon.")
    
    case "medium":
        print(f"'{task}' is a medium priority task", end=" ")
        if time_bound == "yes":
            print("that requires timely attention today.")
        else:
            print("that should be addressed when possible.")
    
    case "low":
        print(f"'{task}' is a low priority task", end=" ")
        if time_bound == "yes":
            print("but it still has a deadline — don't forget it!")
        else:
            print("Consider completing it when you have free time.")
    
    case _:
        print(f"Invalid priority level: '{priority}'. Please use high, medium, or low.")