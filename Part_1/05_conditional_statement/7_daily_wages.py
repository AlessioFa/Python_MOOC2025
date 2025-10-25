# Write your solution here

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ").capitalize()

if day_of_week not in week:
    print("Invalid day of the week")
else:
    if day_of_week == "Sunday":
        daily_wages = hourly_wage * hours_worked * 2
    else:
        daily_wages = hourly_wage * hours_worked

    print(f"Daily wages: {daily_wages} euros")
