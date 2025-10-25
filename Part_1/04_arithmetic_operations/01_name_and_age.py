"""
Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:
Sample output

What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
"""

user_name: str = input("Enter your name and your surname: ").title()
user_year: int = int(input("Enter your born year: "))

print(f"Hi {user_name}, you will be {2021 - user_year} years old at the end of the year 2021")
