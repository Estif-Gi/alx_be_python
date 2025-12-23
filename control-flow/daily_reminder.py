# daily_reminder.py

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

print("\nReminder:", end=" ")

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            print(message + " that requires immediate attention today!")
        else:
            print(message + " that should be completed soon.")
    
    case "medium":
        message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            print(message + " that requires timely attention today.")
        else:
            print(message + " that should be addressed when possible.")
    
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task but it still has a deadline — don't forget it!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print(f"Invalid priority level: '{priority}'. Please use high, medium, or low.")