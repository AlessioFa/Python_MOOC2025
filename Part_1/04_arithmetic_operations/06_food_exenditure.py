"""
Please write a program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical food expenditure both weekly and daily.

The program should function as follows:
Sample output

How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""

student_cafeteria_weekly: int = int(input("How many times do you eat at the cafeteria? "))

price_typical_lunch: float = float(input("The price of a typical student lunch? "))

grocery_weekly: float = float(input("How much money do you spend on groceries in a week? "))

weekly_total: float = (price_typical_lunch * student_cafeteria_weekly) + grocery_weekly
daily_average: float = weekly_total / 7

print("\nAverage food expenditure:")
print("Daily:", round(daily_average, 2), "euros")
print("Weekly:", round(weekly_total, 2), "euros")
