# Personal Daily Reminder
# This script provides customized reminders based on task priority and time sensitivity

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    
    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' is a task"
    
    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        print(f"Reminder: {reminder} that requires immediate attention today!")
    else:
        if priority == "low":
            print(f"Note: {reminder}. Consider completing it when you have free time.")
        else:
            print(f"Note: {reminder}. Consider completing it when you have time.")

if __name__ == "__main__":
    main()
